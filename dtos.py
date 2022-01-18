class UserLoginDto:
    def __init__(self, email, password, two_fa_code):
        self.email = email
        self.password = password
        self.two_fa_code = two_fa_code


class UserDto:
    def __init__(self, name, email, phone, password, gender, country, city, enable_2fa, otp_secret, id=None):
        self.id = id
        self.name = name
        self.email = email
        self.phone = phone
        self.password = password
        self.gender = gender
        self.country = country
        self.city = city
        self.enable_2fa = enable_2fa
        self.otp_secret = otp_secret

        
