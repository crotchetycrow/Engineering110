import csv


def transform_user_details(cvs_file_name):
    new_user_details = []

    with open(cvs_file_name, newline='') as csvfile:
        user_details_csv = csv.reader(csvfile, delimiter=',')
        for user in user_details_csv:
            transfomation = [user[1], user[2], user[3], user[4]]
            new_user_details.append(transfomation)

    return new_user_details


def create_new_user_details(old_data="user_details.csv", new_file_name="new_user_data.csv"):
    new_user_data = transform_user_details(old_data)
    new_file = open(new_file_name, "w")

    with new_file:
        csv_writer = csv.writer(new_file)
        csv_writer.writerows(new_user_data)


create_new_user_details()
