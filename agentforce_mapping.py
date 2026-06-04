-------------------
APEX Trigger (Case)
-------------------

trigger CaseSpamTrigger on Case (before insert) {

    if (Trigger.isBefore && Trigger.isInsert) {
        SpamClassifierHandler.processCases(Trigger.new);
    }
}

-------------------
Main Handler (Core Logic)
-------------------

public class SpamClassifierHandler {

    public static void processCases(List<Case> cases) {

        for (Case c : cases) {

            // Only process Email Cases
            if (c.Origin != 'Email') continue;

            String subject = c.Subject != null ? c.Subject : '';
            String body = c.Description != null ? c.Description : '';
            String email = c.SuppliedEmail != null ? c.SuppliedEmail : '';

            String domain = extractDomain(email);

            Integer score = 0;

            // PHISHING
            if (match(subject, REGEX.phishing) || match(body, REGEX.phishingBody)) {
                markSpam(c, 'Phishing');
                continue;
            }

            // MARKETING SPAM
            if (match(subject, REGEX.marketing)) {
                markSpam(c, 'Marketing');
                continue;
            }

            // SUSPICIOUS DOMAIN
            if (match(email, REGEX.suspiciousDomains)) {
                score += 20;
            }

            // LOW QUALITY
            if (match(subject, REGEX.lowQuality) || subject.length() < 5) {
                score += 10;
            }

            // 📊 FINAL SCORING
            if (score >= 20) {
                markSpam(c, 'Suspicious');
            }
        }
    }


    // Mark as spam
    private static void markSpam(Case c, String type) {
        c.Status = 'Closed';
        c.Spam__c = true;
        c.Spam_Type__c = type;
    }


    // Extract domain
    private static String extractDomain(String email) {
        if (String.isBlank(email) || !email.contains('@')) return '';
        return email.substringAfter('@').toLowerCase();
    }


    // Regex matcher
    private static Boolean match(String text, String pattern) {
        if (String.isBlank(text)) return false;
        Pattern p = Pattern.compile(pattern);
        Matcher m = p.matcher(text);
        return m.find();
    }
}

-------------------
Regex Class
-------------------
public class REGEX {

    public static final String phishing =
        '(?i)(urgent|verify|account|password|reset|blocked|payment|refund|security)';

    public static final String phishingBody =
        '(?i)(click here|verify your account|reset password|provide details)';

    public static final String marketing =
        '(?i)(newsletter|offer|promotion|webinar|event|attendees list|summit)';

    public static final String suspiciousDomains =
        '(?i)@(qq\\.com|163\\.com|126\\.com|.*\\.top|.*\\.shop|.*\\.club|.*\\.info)';

    public static final String lowQuality =
        '(?i)^(re|fw|rfq\\.?|hi|hello)?$';

}
