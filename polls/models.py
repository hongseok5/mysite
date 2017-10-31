from django.db import models

# Create your models here.


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text
    # 테이블 명을 표시하기 위해 반드시 써야 하는 함수 2. 버전에서는 unicode 라는 함수 사용

class Choice(models.Model):
    question = models.ForeignKey(Question)
    # FK 는 테이블만 지정해 주면 된다.
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

    # 하나의 테이블이 하나의 클래스로 정의된다.
    # 클래스 멤버 필드는 속성이된다.
    # PK 는 장고에서 자동으로 생성해준다. question_id ( integer )
