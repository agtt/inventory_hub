# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'Customer.home_phone'
        db.delete_column('customers_customer', 'home_phone')

        # Deleting field 'Customer.work_phone'
        db.delete_column('customers_customer', 'work_phone')

        # Deleting field 'Customer.cell_phone'
        db.delete_column('customers_customer', 'cell_phone')


    def backwards(self, orm):
        
        # Adding field 'Customer.home_phone'
        db.add_column('customers_customer', 'home_phone', self.gf('django.db.models.fields.CharField')(default='', max_length=50, blank=True), keep_default=False)

        # Adding field 'Customer.work_phone'
        db.add_column('customers_customer', 'work_phone', self.gf('django.db.models.fields.CharField')(default='', max_length=50, blank=True), keep_default=False)

        # Adding field 'Customer.cell_phone'
        db.add_column('customers_customer', 'cell_phone', self.gf('django.db.models.fields.CharField')(default='', max_length=50, blank=True), keep_default=False)


    models = {
        'customers.customer': {
            'Meta': {'unique_together': "(('first_name', 'last_name'),)", 'object_name': 'Customer'},
            'business_registration_number': ('django.db.models.fields.CharField', [], {'max_length': '9', 'blank': 'True'}),
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['geography.City']", 'null': 'True', 'blank': 'True'}),
            'company_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['geography.Country']", 'null': 'True', 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2010, 10, 10, 12, 54, 50, 21195)', 'auto_now_add': 'True', 'blank': 'True'}),
            'customer_no': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'discount_percent': ('django.db.models.fields.FloatField', [], {'default': '0', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'price_type': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'street': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'unit_number': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2010, 10, 10, 12, 54, 50, 21195)', 'auto_now': 'True', 'blank': 'True'}),
            'vat_registration_number': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'})
        },
        'geography.city': {
            'Meta': {'ordering': "['name']", 'object_name': 'City'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        },
        'geography.country': {
            'Meta': {'ordering': "['name']", 'object_name': 'Country'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        }
    }

    complete_apps = ['customers']
