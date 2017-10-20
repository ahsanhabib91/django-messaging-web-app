from rest_framework.pagination import (
    PageNumberPagination,
)

class MsgPageNumberPagination(PageNumberPagination):
    page_size = 3