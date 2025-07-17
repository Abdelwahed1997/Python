def get_domain():
    emails = [
        "ali@gmail.com",
        "sara@yahoo.com",
        "mohamed@outlook.com",
        "noha@iti.gov.eg"
    ]

    domain = map(lambda mail:mail.split('@')[1],emails)

    print(list(domain))
get_domain()