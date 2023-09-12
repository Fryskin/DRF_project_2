from rest_framework.serializers import ValidationError


class VideoURLValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        tmp_val = dict(value).get(self.field)
        if 'www.youtube.com/watch' not in tmp_val:
            raise ValidationError('This is not a Youtube-video url.')


class DescriptionValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        tmp_val = dict(value).get(self.field)
        if 'https://' in tmp_val and 'www.youtube.com/watch' not in tmp_val:
            raise ValidationError('If you wanna use some url it supposed to be a Youtube-video url.')
        if 'http://' in tmp_val and 'www.youtube.com/watch' not in tmp_val:
            raise ValidationError('If you wanna use some url it supposed to be a Youtube-video url.')
