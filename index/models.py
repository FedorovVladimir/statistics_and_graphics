import datetime

from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=100)
    teacher_name = models.CharField(max_length=100)
    teacher_id = models.CharField(max_length=100)
    count_user = models.IntegerField()
    last_access = models.IntegerField()
    avg_final_grade = models.CharField(max_length=100)
    final_grade = models.CharField(max_length=100)
    count_in = models.IntegerField()
    count_views = models.IntegerField()

    def get_count_in(self):
        if self.count_in:
            return self.count_in
        return 0

    def get_coef(self):
        if self.count_in and self.count_views:
            return self.count_views/self.count_in
        return "-"

    def get_last_access(self):
        if self.last_access:
            return str(datetime.datetime.fromtimestamp(self.last_access))
        return "-"

    def get_avg_final_grade(self):
        if self.avg_final_grade:
            return self.avg_final_grade
        return "-"

    def get_final_grade(self):
        if self.final_grade:
            return self.final_grade
        return "-"

    def get_stat_avg_final_grade(self):
        if self.avg_final_grade:
            return self.avg_final_grade
        return 0


class GradeItems(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    grade_min = models.IntegerField()
    grade_max = models.IntegerField()
    grade = models.IntegerField()
    grade_id = models.IntegerField()
    user_modified = models.CharField(max_length=100)

    def get_type(self):
        if self.type == 'quiz':
            return "Тест"
        elif self.type == 'assign':
            return "Задание"
        elif self.type == 'lesson':
            return "Лекция"
        else:
            return "-"

    def get_grade(self):
        if self.grade:
            return str(self.grade)
        return str(self.grade_min)

    def get_user_modified(self):
        if self.user_modified:
            return str(self.user_modified)
        return 'Система'

    def get_stat_grade(self):
        if self.grade:
            return str(self.grade)
        return 0
