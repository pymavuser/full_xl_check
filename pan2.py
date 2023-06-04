import pandas as pd
import numpy as np

result = pd.DataFrame()
fd = pd.DataFrame()


da = pd.read_excel('ab.xlsx')
db = pd.read_excel('ab1.xlsx')
for col in da.columns:
    print(col)
    for value in da[col]:
        if value in db[col].values:
            result = result._append({'source'+col: value, 'Target'+col: value, 'comp_'+col: 'available'}, ignore_index=True)
        else:
            result = result._append({'source'+col: value, 'Target'+col: 'na','comp_'+col: 'Source delta'}, ignore_index=True)

    # Add rows to the result DataFrame for values in column 'b' not present in column 'a'
    for value in db[col]:
        if value not in da[col].values:
            result = result._append({'source'+col: 'na', 'Target'+col: value, 'comp_'+col: 'Target delta'}, ignore_index=True)

    print(result)
    fd = pd.concat([fd, result], axis=1,ignore_index=False)
    result = result.iloc[:, 3:]
    result = result[0:0]
    print(result)

fd.to_excel("output.xlsx")
data = {'Column Name': [],'Matching count': [],'Source Delta': [],'Target Delta': []}
summary = pd.DataFrame(data)

for col in fd.columns:
    if "comp" in col:
        value1 = 'available'
        value_count = (fd[col] == value1).sum()
        value2 = 'Source delta'
        value_count2 = (fd[col] == value2).sum()
        value3 = 'Target delta'
        value_count3 = (fd[col] == value3).sum()
        new_data = {'Column Name': [col],'Matching count': [value_count],'Source Delta': [value_count2],'Target Delta': [value_count3]}
        summary = summary._append(pd.DataFrame(new_data), ignore_index=True)
print(summary)