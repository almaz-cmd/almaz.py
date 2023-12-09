# import json
#
# d = {
#     "qiwi": 50,
#     "apelsin": 120,
#     "kartoshka": 200,
#     "apple": 500,
# }
#
# with open("json_file.json", "r") as file:
#     d = json.load(file)
#
# json_file1_data = {}
# json_file2_data = {}
#
# for i, j in d.items():
#     if j <= 500:
#         json_file1_data[i] = j
#     elif j <= 200:
#         json_file2_data[i] = j
#
# with open("json_file1.json", "w") as file1:
#     json.dump(json_file1_data, file1, indent=4, ensure_ascii=False)
#
# with open("json_file2.json", "w") as file2:
#     json.dump(json_file2_data, file2, indent=4, ensure_ascii=False)
#
#
