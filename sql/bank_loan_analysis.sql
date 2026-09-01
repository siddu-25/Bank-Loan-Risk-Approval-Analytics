CREATE DATABASE bank_loan_analytics;
USE bank_loan_analytics;
SELECT DATABASE();
SELECT *
FROM loan_applications
LIMIT 10;
SELECT COUNT(*) AS total_applications
FROM loan_applications;
SELECT 
    loan_status,
    COUNT(*) AS application_count
FROM loan_applications
GROUP BY loan_status;
SELECT
    COUNT(*) AS total_applications,
    SUM(CASE WHEN loan_status = 'Approved' THEN 1 ELSE 0 END) AS approved_loans,
    SUM(CASE WHEN loan_status = 'Rejected' THEN 1 ELSE 0 END) AS rejected_loans,
    ROUND(
        SUM(CASE WHEN loan_status = 'Approved' THEN 1 ELSE 0 END)
        * 100.0 / COUNT(*), 2
    ) AS approval_rate
FROM loan_applications;
SELECT
    ROUND(AVG(income_annum), 2) AS avg_annual_income,
    ROUND(AVG(loan_amount), 2) AS avg_loan_amount,
    ROUND(AVG(cibil_score), 2) AS avg_cibil_score
FROM loan_applications;
SELECT
    loan_status,
    COUNT(*) AS applications,
    ROUND(AVG(cibil_score), 2) AS average_cibil_score
FROM loan_applications
GROUP BY loan_status
ORDER BY average_cibil_score DESC;
SELECT
    loan_status,
    ROUND(AVG(income_annum), 2) AS average_income,
    ROUND(AVG(loan_amount), 2) AS average_loan_amount
FROM loan_applications
GROUP BY loan_status;
SELECT
    CASE
        WHEN cibil_score >= 750 THEN 'Excellent'
        WHEN cibil_score >= 650 THEN 'Good'
        WHEN cibil_score >= 550 THEN 'Average'
        ELSE 'Poor'
    END AS cibil_category,
    COUNT(*) AS applicants
FROM loan_applications
GROUP BY cibil_category
ORDER BY applicants DESC;
SELECT
    CASE
        WHEN cibil_score >= 750 THEN 'Excellent'
        WHEN cibil_score >= 650 THEN 'Good'
        WHEN cibil_score >= 550 THEN 'Average'
        ELSE 'Poor'
    END AS cibil_category,

    COUNT(*) AS total_applicants,

    SUM(
        CASE
            WHEN loan_status = 'Approved' THEN 1
            ELSE 0
        END
    ) AS approved,

    SUM(
        CASE
            WHEN loan_status = 'Rejected' THEN 1
            ELSE 0
        END
    ) AS rejected,

    ROUND(
        SUM(
            CASE
                WHEN loan_status = 'Approved' THEN 1
                ELSE 0
            END
        ) * 100.0 / COUNT(*), 2
    ) AS approval_rate

FROM loan_applications

GROUP BY cibil_category

ORDER BY approval_rate DESC;
