class Parameter:
    def __init__(self, title, limit):
        self.title = title
        self.limit = limit

    def limit_int(self):
        try:
            self.limit = int(self.limit)
            if not self.limit >= 1 and self.limit <= 20:
                self.limit = False
        except:
            self.limit = False
        finally:
            return self.limit
