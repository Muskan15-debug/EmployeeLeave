def validate_leave(balance, requested):
    if balance < 0:
        return False
    if requested<=0:
        return False
    if requested>balance:
        return False
    return True 

if __name__ == "__main__":
    balance = 10
    requested = 5

    if validate_leave(balance, requested):
        print("Leave request is valid")
    else:
        print("Invalid")