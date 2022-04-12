import csv


# print(list(csvreader))
#
# # # print(csvreader)
# #
# # iterable_csv = iter(csvreader)
# # next(iterable_csv)
# #
# # for row in csvreader:
# #     print(row[-1])


def transform_user_details(cvs_file_name):
    new_user_details = []

    with open(cvs_file_name, newline='') as csvfile:
        user_details_csv = csv.reader(csvfile, delimiter=',')
        for user in user_details_csv:
            transfomation = [user[1], user[2], user[3], user[4]]
            new_user_details.append(transfomation)

    return new_user_details


print(transform_user_details("user_details.csv"))
