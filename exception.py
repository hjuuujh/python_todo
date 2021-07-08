class DuplicateError(Exception):
    def __init__(self, message):
        super().__init__(message + " 이미존재 합니다.")

    # def __str__(self):
    #     return super().__str__ 

class NotFoundError(Exception):
    def __init__(self, message):
        super().__init__(message + " 존재하지 않습니다.")

    # def __str__(self):
    #     return super().__str__()