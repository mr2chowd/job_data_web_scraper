from indeed import indeed_data
from linkedIn import linkedin_data
import pandas as pd

def calculate_total_posting(job, company):
    l_df = linkedin_data(job, company)
    i_df = indeed_data(job, company)

    print("Total from linkedin :", len(l_df))
    print("Total from indeed :", len(i_df))

    df  = pd.concat([l_df, i_df],ignore_index = True)
    print("grand total : ", len(df))
    df=df.drop_duplicates(ignore_index = True)
    print("Total new job postings : ", len(df))

if __name__ == "__main__":
    calculate_total_posting("IT","Utica")