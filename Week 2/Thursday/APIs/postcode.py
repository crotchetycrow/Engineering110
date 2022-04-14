class Postcode:
    def __init__(self, postcode_dict):
        self.postcode = postcode_dict["postcode"]
        self.country = postcode_dict["country"]
        self.region = postcode_dict["region"]
        self.admin_district = postcode_dict["admin_district"]
        self.parish = postcode_dict["[parish]"]

