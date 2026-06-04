CASE
  WHEN REGEXP_LIKE(subject, '(?i)(newsletter|offer|promotion)') THEN 'SPAM'
  WHEN REGEXP_LIKE(subject, '(?i)(urgent|verify|password)') THEN 'PHISHING'
  WHEN REGEXP_LIKE(email, '(?i)@(qq.com|163.com)') THEN 'SPAM'
  ELSE 'VALID'
END AS classification
