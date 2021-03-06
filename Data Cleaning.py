## 3. Reading in to Pandas ##

import pandas as pd

#reading csv into dataframe
loans_2007 = pd.read_csv('loans_2007.csv')

print(loans_2007.head(1))
print(loans_2007.shape[1])

## 5. First group of columns ##

loans_2007.drop(['id', 'member_id', 'funded_amnt', 'funded_amnt_inv', 'grade', 'sub_grade', 'emp_title', 'issue_d'], axis=1, inplace = True)

## 7. Second group of features ##

loans_2007.drop(['zip_code', 'out_prncp', 'out_prncp_inv', 'total_pymnt', 'total_pymnt_inv', 'total_rec_prncp'], axis=1, inplace = True)

## 9. Third group of features ##

loans_2007.drop(['total_rec_int', 'total_rec_late_fee', 'recoveries', 'collection_recovery_fee', 'last_pymnt_d', 'last_pymnt_amnt'], axis=1, inplace = True)
print(loans_2007.head(1))
print(loans_2007.shape[1])

## 10. Target column ##

print(loans_2007['loan_status'].value_counts)

## 12. Binary classification ##

loans_2007 = loans_2007[(loans_2007['loan_status'] == 'Fully Paid') | (loans_2007['loan_status'] == 'Charged Off')]
mapping_dict = {
    "loan_status": {
        "Charged Off": 0,
        "Fully Paid": 1
    }
}
loans_2007.replace(mapping_dict, inplace=True)

## 13. Removing single value columns ##

drop_columns = list()
for col in loans_2007.columns:
    non_null = loans_2007[col].dropna()
    unique_non_null = non_null.unique()
    num_true_unique = len(unique_non_null)
    if num_true_unique == 1:
        drop_columns.append(col)

loans_2007.drop(drop_columns, axis=1, inplace=True)
print(drop_columns)
