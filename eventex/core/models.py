# coding: utf-8
from django.db import models
from django.db.models import signals
from django.template.defaultfilters import slugify
from django.utils.translation import ugettext_lazy as _


class Speaker(models.Model):
    name = models.CharField(_('Nome'), max_length=255)
    slug = models.SlugField(_('Slug'), unique=True)
    url = models.URLField(_('Url'))
    description = models.TextField(_(u'Descrição'), blank=True)

    def __unicode__(self):
        return self.name

def speaker_pre_save(signal, instance, sender, **kwargs):
    slug = slugify(instance.name)
    instance.slug = slug
    novoSlug = slug
    i=0
    while Speaker.objects.filter(slug=novoSlug).exclude(id=instance.id).count()>0: 
        i += 1
        novoSlug = '%s%d' % (slug,i)
    instance.slug = novoSlug

class Contact(models.Model):
    KINDS = (
        ('P', _('Telefone')),
        ('E',_('E-mail')),
        ('F', _('Fax')),
    )
    speaker = models.ForeignKey('Speaker', verbose_name=_('palestrante'))
    kind = models.CharField(_('tipo'), max_length=1, choices=KINDS)
    value = models.CharField(_('valor'), max_length=255)

    def __unicode__(self):
        return self.value

#def speaker_post_save(signal, instance, sender, **kwargs):
#    instance.slug = '%s%d' % (slugify(instance.name),instance.id)

signals.pre_save.connect(speaker_pre_save,sender=Speaker)
        
#    def save(self, *args, **kwargs):
#        if not self.id:
#            slug = slugify(self.name)
#            super(Speaker,self).save(*args, **kwargs)
