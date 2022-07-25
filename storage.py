
import pandas

data = pandas.read_csv("weather_data.csv")
# print(data)
# print(type(data))
# print(type(data["temp"]))

# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(temp_list)
#
# # Base
# def average(items):
#     sum_items = sum(items)
#     n = len(items)
#     mean = round(sum_items/n, 2)
#     return mean
#
#
# print(average(temp_list))
#
# # Using pandas methods
# avg_temp = data["temp"].mean()
# print(round(avg_temp, 2))
#
# max_temp = data["temp"].max()
# print(max_temp)
#
# # Using columns as attributes
# print(data.condition)
#
# # Accessing rows
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

#
# def celsius_to_farenheit(temperature):
#     far = temperature*(9/5) + 32
#     return far
#
#
# monday = data[data.day == "Monday"]
# # print(monday["temp"])
# monday_temp_far = celsius_to_farenheit(monday.temp)
# print(monday_temp_far)


# # Creating a Dataframe
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
#
# df = pandas.DataFrame.from_dict(data_dict)
# print(df)
# df.to_csv("new_data.csv")