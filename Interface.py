def validate_to_int(str_input):
    while True:
        try:
            user_input = input(str_input)
            return int(str_input)
        except:
            print('Sorry that was not an integer')

            