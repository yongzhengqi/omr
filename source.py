class Book:
    def __init__(self, title):
        self.title = title


BBL = Book("Ball Bearing Lubrication: The Elastohydrodynamics of Elliptical Contacts")
BDM = Book("Bearing Design in Machinery: Engineering Tribology and Lubrication")
ECBT = Book("Essential Concepts of Bearing Technology")
ACBT = Book("Advanced Concepts of Bearing Technology")


class Source:
    def __init__(self, book, page):
        self.book = book
        self.page = page
