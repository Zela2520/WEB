
from django.db import models
from django.contrib.auth.models import User
from django.db.models import Count


class ProfileManager(models.Manager):
    def get_top_users(self, count=5):
        return self.annotate(answers_count=Count('answer')).order_by('-answers_count')[:count]


class Profile(models.Model):
    avatar = models.ImageField(null=True, blank=True, upload_to='media/avatars/',
                               default='media/avatars/dwight.jpeg')

    counter_questions = models.IntegerField(default=0)
    counter_answers = models.IntegerField(default=0)
    counter_resolved_answers = models.IntegerField(default=0)

    user = models.OneToOneField(User, on_delete=models.CASCADE, null=False)
    objects = ProfileManager()

    def __str__(self):
        return f"{self.user.username}"


class TagManager(models.Manager):
    def top_tags(self, count=10):
        return self.annotate(que_count=Count('question')).order_by('-que_count')[:count]


class Tag(models.Model):
    name = models.CharField(max_length=32)
    objects = TagManager()

    def __str__(self):
        return self.name


class QuestionManager(models.Manager):
    def count_answers(self):
        return self.annotate(answers=Count('answer', distinct=True))

    def new(self):
        return self.count_answers().order_by('-publish_date')

    def old(self):
        return self.count_answers().order_by('publish_date')

    def hot(self):
        return self.count_answers().order_by('-rating')

    def by_tag(self, tag):
        return self.count_answers().filter(tags__name=tag)

    def by_id(self, id):
        return self.get(id=id)


class Question(models.Model):
    title = models.CharField(max_length=256)
    text = models.TextField()
    tags = models.ManyToManyField(Tag)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    publish_date = models.DateTimeField(auto_now_add=True)

    rating = models.IntegerField(default=0)

    counter_votes = models.IntegerField(default=0)
    counter_answers = models.IntegerField(default=0)
    counter_views = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    objects = QuestionManager()


class AnswerManager(models.Manager):
    def answer_by_question(self, que_id):
        return self.annotate(likes=Count('likeanswer')) \
            .order_by('publish_date').filter(question_id=que_id)


class Answer(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=256)
    text = models.TextField()
    is_correct = models.BooleanField(default=False)
    publish_date = models.DateTimeField(auto_now_add=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    objects = AnswerManager()


class LikeQuestion(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)


class LikeAnswer(models.Model):
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)