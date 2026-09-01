import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned dataset
df = pd.read_csv(r"C:\Users\Siddu\Desktop\Bank-Loan-Risk-Approval-Analytics\Data\loan_data_cleaned.csv")

print("\n========== DATASET INFORMATION ==========")
print(df.info())

print("\n========== BASIC STATISTICS ==========")
print(df.describe())

# ------------------------------------------------
# 1. Loan Status Count
# ------------------------------------------------
print("\n========== LOAN STATUS COUNT ==========")
print(df["loan_status"].value_counts())

plt.figure(figsize=(7, 5))
df["loan_status"].value_counts().plot(kind="bar")
plt.title("Loan Approval Status")
plt.xlabel("Loan Status")
plt.ylabel("Number of Applications")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()


# ------------------------------------------------
# 2. Categorical Feature Analysis
# ------------------------------------------------

categorical_columns = [
    "education",
    "self_employed"
]

for column in categorical_columns:
    print(f"\n========== {column.upper()} ==========")
    print(df[column].value_counts())

    plt.figure(figsize=(7, 5))
    df[column].value_counts().plot(kind="bar")
    plt.title(f"Distribution of {column}")
    plt.xlabel(column)
    plt.ylabel("Number of Applications")
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.show()


# ------------------------------------------------
# 3. Loan Status by Education
# ------------------------------------------------

education_status = pd.crosstab(
    df["education"],
    df["loan_status"]
)

print("\n========== LOAN STATUS BY EDUCATION ==========")
print(education_status)

education_status.plot(kind="bar", figsize=(8, 5))
plt.title("Loan Status by Education")
plt.xlabel("Education")
plt.ylabel("Number of Applications")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()


# ------------------------------------------------
# 4. Loan Status by Self Employment
# ------------------------------------------------

employment_status = pd.crosstab(
    df["self_employed"],
    df["loan_status"]
)

print("\n========== LOAN STATUS BY SELF EMPLOYMENT ==========")
print(employment_status)

employment_status.plot(kind="bar", figsize=(8, 5))
plt.title("Loan Status by Self Employment")
plt.xlabel("Self Employed")
plt.ylabel("Number of Applications")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()


# ------------------------------------------------
# 5. Correlation Analysis
# ------------------------------------------------

numeric_df = df.select_dtypes(include="number")

correlation = numeric_df.corr()

print("\n========== CORRELATION MATRIX ==========")
print(correlation)

plt.figure(figsize=(12, 8))
plt.imshow(correlation, cmap="coolwarm", interpolation="nearest")
plt.colorbar()

plt.xticks(
    range(len(correlation.columns)),
    correlation.columns,
    rotation=90
)

plt.yticks(
    range(len(correlation.columns)),
    correlation.columns
)

plt.title("Correlation Heatmap")
plt.tight_layout()
plt.show()


print("\n========== EDA COMPLETED SUCCESSFULLY ==========")
