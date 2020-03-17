def verify(password):
    if (not password) or (not [char.islower() for char in password].__contains__(True)):
        raise AssertionError("Password must contain at least 1 lowercase letter")

    failed_rules = []

    if len(password) < 8:
        failed_rules.append("Password must be more than 8 characters")
     
    valid = [char.isupper() for char in password]
    if not valid.__contains__(True):
        failed_rules.append("Password must contain at least 1 uppercase letter")

    valid = [char.isdigit() for char in password]
    if not valid.__contains__(True):
        failed_rules.append("Password must contain at least 1 number")
    
    if len(failed_rules) > 1:
        raise AssertionError(failed_rules)
    else:
        return password
