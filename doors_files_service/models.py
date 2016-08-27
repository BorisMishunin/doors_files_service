# -*- coding: utf-8 -*-
from django.db import models
from PIL import Image, ImageDraw, ImageFont, ImageEnhance

import localsettings as settings


class DoorsImages(models.Model):
    image = models.ImageField(upload_to='DoorsImages', max_length=200)

    def save(self, add_watermark=False, **kwargs):
        super(DoorsImages, self).save(**kwargs)
        path = self.image.path
        image = Image.open(path)
        width, height = image.size

        base_width = 960
        ratio = 0.5625  # 2560x1440, 1280x720
        base_height = int(base_width * ratio)  # 540

        if not (width == base_width and height == base_height):
            # resize image
            coef = float(base_width) / width
            new_height = int(coef * height)
            image = image.resize((base_width, new_height), Image.ANTIALIAS)

            # crop image
            delta = (new_height - base_height) / 2
            if delta > 0:
                image = image.crop((0, delta, base_width, new_height - delta))

        if not add_watermark:
            image.save(path)
        else:
            # watermark
            image.save(path + '.orig', 'JPEG')
            font_file = settings.WATERMARK_FONT_PATH
            angle = 23
            opacity = 0.2
            text = 'Doors'

            image = image.convert('RGB')
            watermark = Image.new('RGBA', image.size, (0, 0, 0, 0))

            font_size = 2
            font = ImageFont.truetype(font_file, font_size)
            text_width, text_height = font.getsize(text)
            while text_width + text_height < watermark.size[0] * 0.65:
                font_size += 2
                font = ImageFont.truetype(font_file, font_size)
                text_width, text_height = font.getsize(text)

            draw = ImageDraw.Draw(watermark, 'RGBA')
            draw.text(((watermark.size[0] - text_width) / 2, (watermark.size[1] - text_height) / 2), text, font=font)

            watermark = watermark.rotate(angle, Image.BICUBIC)

            alpha = watermark.split()[3]
            alpha = ImageEnhance.Brightness(alpha).enhance(opacity)
            watermark.putalpha(alpha)

            Image.composite(watermark, image, watermark).save(path, 'JPEG')

    def __unicode__(self):
        return u"{0.id}".format(self)

    class Meta:
        verbose_name_plural = u"Фото дверей"
        db_table = 'doors_images'