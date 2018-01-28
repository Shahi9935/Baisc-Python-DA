import quandl
import pandas as pd
import pickle
print("Starting")

fiddy_states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')
print("Read HTML")
main_df=pd.DataFrame();
for abbv in fiddy_states[0][0][1:]:
    #print(abbv)
    print("FMAC/HPI_"+str(abbv))
    query = "FMAC/HPI_"+str(abbv)
    df = quandl.get(query, authtoken="S4V36HwyxCx-Vkwxz6_d")
    print(df.head())
    df.rename(columns={'Value':abbv},inplace=True)
    print("************")
    if main_df.empty:
        main_df = df
    else:
        main_df = main_df.join(df)
    print("%%%%%%%%%%%%")
    print(main_df.head())
