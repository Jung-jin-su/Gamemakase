# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Authority(models.Model):
    authority_name = models.CharField(primary_key=True, max_length=10)

    class Meta:
        managed = False
        db_table = 'authority'


class BackgroundTask(models.Model):
    id = models.BigAutoField(primary_key=True)
    task_name = models.CharField(max_length=190)
    task_params = models.TextField()
    task_hash = models.CharField(max_length=40)
    verbose_name = models.CharField(max_length=255, blank=True, null=True)
    priority = models.IntegerField()
    run_at = models.DateTimeField()
    repeat = models.BigIntegerField()
    repeat_until = models.DateTimeField(blank=True, null=True)
    queue = models.CharField(max_length=190, blank=True, null=True)
    attempts = models.IntegerField()
    failed_at = models.DateTimeField(blank=True, null=True)
    last_error = models.TextField()
    locked_by = models.CharField(max_length=64, blank=True, null=True)
    locked_at = models.DateTimeField(blank=True, null=True)
    creator_object_id = models.PositiveIntegerField(blank=True, null=True)
    creator_content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'background_task'


class BackgroundTaskCompletedtask(models.Model):
    id = models.BigAutoField(primary_key=True)
    task_name = models.CharField(max_length=190)
    task_params = models.TextField()
    task_hash = models.CharField(max_length=40)
    verbose_name = models.CharField(max_length=255, blank=True, null=True)
    priority = models.IntegerField()
    run_at = models.DateTimeField()
    repeat = models.BigIntegerField()
    repeat_until = models.DateTimeField(blank=True, null=True)
    queue = models.CharField(max_length=190, blank=True, null=True)
    attempts = models.IntegerField()
    failed_at = models.DateTimeField(blank=True, null=True)
    last_error = models.TextField()
    locked_by = models.CharField(max_length=64, blank=True, null=True)
    locked_at = models.DateTimeField(blank=True, null=True)
    creator_object_id = models.PositiveIntegerField(blank=True, null=True)
    creator_content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'background_task_completedtask'


class Chat(models.Model):
    chat_id = models.BigAutoField(primary_key=True)
    chatting_room = models.ForeignKey('ChattingRoom', models.DO_NOTHING)
    writer = models.ForeignKey('User', models.DO_NOTHING)
    game = models.ForeignKey('Game', models.DO_NOTHING)
    content = models.CharField(max_length=200)
    created_at = models.TimeField()

    class Meta:
        managed = False
        db_table = 'chat'


class ChattingRoom(models.Model):
    chatting_room_id = models.BigAutoField(primary_key=True)
    game = models.ForeignKey('Game', models.DO_NOTHING)
    chatting_room_name = models.CharField(max_length=40)
    game_0 = models.IntegerField(db_column='game')  # Field renamed because of name conflict.

    class Meta:
        managed = False
        db_table = 'chatting_room'


class DailyRecommendation(models.Model):
    daily_recommendation_id = models.BigAutoField(primary_key=True)
    game = models.ForeignKey('Game', models.DO_NOTHING)
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'daily_recommendation'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoApschedulerDjangojob(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    next_run_time = models.DateTimeField(blank=True, null=True)
    job_state = models.TextField()

    class Meta:
        managed = False
        db_table = 'django_apscheduler_djangojob'


class DjangoApschedulerDjangojobexecution(models.Model):
    id = models.BigAutoField(primary_key=True)
    status = models.CharField(max_length=50)
    run_time = models.DateTimeField()
    duration = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    finished = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    exception = models.CharField(max_length=1000, blank=True, null=True)
    traceback = models.TextField(blank=True, null=True)
    job = models.ForeignKey(DjangoApschedulerDjangojob, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_apscheduler_djangojobexecution'
        unique_together = (('job', 'run_time'),)


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Game(models.Model):
    game_id = models.BigAutoField(primary_key=True)
    game_name = models.CharField(max_length=200)
    game_price = models.IntegerField()
    release_date = models.DateTimeField()
    game_description = models.TextField()
    score = models.IntegerField()
    average_playtime = models.IntegerField(blank=True, null=True)
    publisher = models.CharField(max_length=100, blank=True, null=True)
    is_korean = models.IntegerField(blank=True, null=True)
    windows = models.IntegerField(blank=True, null=True)
    mac = models.IntegerField(blank=True, null=True)
    linux = models.IntegerField(blank=True, null=True)
    peak_ccu = models.IntegerField(blank=True, null=True)
    average_playtime_2weeks = models.IntegerField(blank=True, null=True)
    recommendations = models.IntegerField(blank=True, null=True)
    estimated_owners = models.CharField(max_length=200, blank=True, null=True)
    reviews = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'game'


class GameHistory(models.Model):
    game_history_id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey('User', models.DO_NOTHING)
    game = models.ForeignKey(Game, models.DO_NOTHING)
    total_play_game = models.IntegerField(blank=True, null=True)
    two_week_play_time = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'game_history'


class GameSmall(models.Model):
    game_id = models.BigAutoField(primary_key=True)
    game_name = models.CharField(max_length=200)
    game_price = models.IntegerField()
    release_date = models.DateTimeField()
    game_description = models.TextField()
    score = models.IntegerField()
    average_playtime = models.IntegerField(blank=True, null=True)
    publisher = models.CharField(max_length=100, blank=True, null=True)
    is_korean = models.IntegerField(blank=True, null=True)
    windows = models.IntegerField(blank=True, null=True)
    mac = models.IntegerField(blank=True, null=True)
    linux = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'game_small'


class GameVideo(models.Model):
    game = models.ForeignKey(Game, models.DO_NOTHING)
    youtube_id = models.CharField(max_length=255, db_collation='utf8mb3_bin')
    created_at = models.DateTimeField()
    game_video_id = models.BigAutoField(primary_key=True)
    youtube_name = models.TextField(db_collation='utf8mb3_bin')

    class Meta:
        managed = False
        db_table = 'game_video'


class Genre(models.Model):
    genre_id = models.BigAutoField(primary_key=True)
    game = models.ForeignKey(Game, models.DO_NOTHING)
    genre_name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'genre'


class Image(models.Model):
    image_id = models.BigAutoField(primary_key=True)
    type = models.CharField(max_length=20)
    type_id = models.BigIntegerField()
    image_path = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'image'


class LikeGame(models.Model):
    like_id = models.BigAutoField(primary_key=True)
    game = models.ForeignKey(Game, models.DO_NOTHING)
    user = models.ForeignKey('User', models.DO_NOTHING)
    type = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'like_game'


class Rating(models.Model):
    game_id = models.BigIntegerField(blank=True, null=True)
    steam_id = models.BigIntegerField(blank=True, null=True)
    playtime = models.IntegerField(blank=True, null=True)
    frequency = models.FloatField(blank=True, null=True)
    rating = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rating'


class RatingSmall(models.Model):
    game_id = models.BigIntegerField(blank=True, null=True)
    steam_id = models.IntegerField(blank=True, null=True)
    playtime = models.IntegerField(blank=True, null=True)
    frequency = models.FloatField(blank=True, null=True)
    rating = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rating_small'


class Recommendation(models.Model):
    steam = models.ForeignKey('User', models.DO_NOTHING)
    game = models.ForeignKey(Game, models.DO_NOTHING)
    rating = models.FloatField()
    recommendation_id = models.BigAutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'recommendation'


class Review(models.Model):
    review_id = models.BigAutoField(primary_key=True)
    game = models.ForeignKey(Game, models.DO_NOTHING)
    user = models.ForeignKey('User', models.DO_NOTHING)
    review_title = models.CharField(max_length=20)
    review_content = models.TextField()
    review_grade = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'review'


class TendencyResult(models.Model):
    tendency_result_id = models.BigAutoField(primary_key=True)
    tendency_result = models.CharField(max_length=20)
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tendency_result'


class TendencyTest(models.Model):
    tendency_quest = models.CharField(primary_key=True, max_length=100)
    tendency_comm = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'tendency_test'


class User(models.Model):
    user_id = models.BigAutoField(primary_key=True)
    user_steam_id = models.BigIntegerField()
    user_name = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'user'


class UserAuthorityJoin(models.Model):
    authority_name = models.ForeignKey(Authority, models.DO_NOTHING, db_column='authority_name')
    user = models.ForeignKey(User, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'user_authority_join'


class UserOpenid(models.Model):
    openid_url = models.CharField(primary_key=True, max_length=100)
    user = models.ForeignKey(User, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'user_openid'
