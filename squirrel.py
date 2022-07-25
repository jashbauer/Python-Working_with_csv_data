import pandas

data = pandas.read_csv("squirrel_data.csv")
# print(data.head())
# print(data.columns)

# Try using Group By
# new_data = data[["Primary Fur Color", "Unique Squirrel ID"]]
# new_data = new_data.groupby("Primary Fur Color").count()
# print(new_data)

fur_col = data["Primary Fur Color"].value_counts()
print(fur_col)
fur_col = fur_col.rename({"Gray": "grey", "Cinnamon": "red", "Black": "black"})
print(fur_col)

fur_col.to_csv("squirrel_datacol2.csv")

# Renaming manually byr creating a dictionary
# color_count = []
# for color in fur_col:
#     color_count.append(color)
# print(color_count)
# new_color_names = ["grey", "red", "black"]

# color_data = {
#     "colors": new_color_names,
#     "count": color_count
# }
# print(color_data)
# col_df = pandas.DataFrame.from_dict(color_data)
# print(col_df)
# col_df.to_csv("squirrel_coldata.csv")