# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Talk'
        db.create_table(u'core_talk', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('start_time', self.gf('django.db.models.fields.TimeField')(blank=True)),
        ))
        db.send_create_signal(u'core', ['Talk'])

        # Adding M2M table for field speakers on 'Talk'
        m2m_table_name = db.shorten_name(u'core_talk_speakers')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('talk', models.ForeignKey(orm[u'core.talk'], null=False)),
            ('speaker', models.ForeignKey(orm[u'core.speaker'], null=False))
        ))
        db.create_unique(m2m_table_name, ['talk_id', 'speaker_id'])


    def backwards(self, orm):
        # Deleting model 'Talk'
        db.delete_table(u'core_talk')

        # Removing M2M table for field speakers on 'Talk'
        db.delete_table(db.shorten_name(u'core_talk_speakers'))


    models = {
        u'core.contact': {
            'Meta': {'object_name': 'Contact'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kind': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'speaker': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Speaker']"}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'core.speaker': {
            'Meta': {'object_name': 'Speaker'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'core.talk': {
            'Meta': {'object_name': 'Talk'},
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'speakers': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['core.Speaker']", 'symmetrical': 'False'}),
            'start_time': ('django.db.models.fields.TimeField', [], {'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['core']