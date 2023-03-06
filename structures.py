class User:
    def __init__(self, **kwargs):
        self.username: str = kwargs.get("username", "")
        self.display: str = kwargs.get("display", "")
        self.id: int = kwargs.get("id", -1)
        self.__password: str = kwargs.get("password", "")

        self.grade: str = kwargs.get("grade", "")
        self.field_of_study: str = kwargs.get("field_of_study", "")
        self.optional_subject: str = kwargs.get("optional_subject", "")

    def __repr__(self) -> str:
        return "User(%s (%s [%i]))" % (self.display, self.username, self.id)

    def get_password(self):
        return self.__password
