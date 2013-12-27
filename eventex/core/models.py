# coding: utf-8
from django.db import models
from django.db.models import signals
from django.template.defaultfilters import slugify
from django.utils.translation import ugettext_lazy as _
from eventex.core.managers import KindContactManager, PeriodManager


class Speaker(models.Model):
    name = models.CharField(_('Nome'), max_length=255)
    slug = models.SlugField(_('Slug'), unique=True)
    url = models.URLField(_('Url'))
    description = models.TextField(_(u'Descrição'), blank=True)

    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return('core:speaker_detail', (), {'slug' : self.slug})

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

    objects = models.Manager()
    emails = KindContactManager('E')
    phones = KindContactManager('P')
    faxes  = KindContactManager('F')

    def __unicode__(self):
        return self.value

class Talk(models.Model):
    title= models.CharField(_(u'Título'), max_length=200)
    description = models.TextField(_(u'Descrição'))
    start_time = models.TimeField(_(u'Horário'),blank=True)
    speakers = models.ManyToManyField('Speaker', verbose_name=_('palestrantes'))

    objects = PeriodManager()

    class Meta:
        verbose_name=_('palestra')
        verbose_name_plural = _('palestras')

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        #TODO : USE reverse.
        return '/palestras/%d/' % self.pk

class Course(Talk):
    slots = models.IntegerField(_('vagas'))
    notes = models.TextField(_(u'observacoes'))

    objects = PeriodManager()

#def speaker_post_save(signal, instance, sender, **kwargs):
#    instance.slug = '%s%d' % (slugify(instance.name),instance.id)

signals.pre_save.connect(speaker_pre_save,sender=Speaker)
        
#    def save(self, *args, **kwargs):
#        if not self.id:
#            slug = slugify(self.name)
#            super(Speaker,self).save(*args, **kwargs)
