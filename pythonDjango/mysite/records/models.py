from django.db import models


# Create your models here.
class Record(models.Model):
    """
    Класс для хранения записей.

    С атрибутами:
        title (str): Заголовок записи.
        description (str): Описание записи.
        created_at (datetime): Дата и время создания записи.
    """
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        Возвращает строковое представление записи.

        Возврощает:
            Заголовок записи.
        """
        return self.title
