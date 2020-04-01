# Generated by Django 2.0 on 2019-12-01 15:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apitest', '0002_testtask'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100, verbose_name='名称')),
                ('error', models.IntegerField(verbose_name='错误用例')),
                ('failure', models.IntegerField(verbose_name='失败用例')),
                ('skipped', models.IntegerField(verbose_name='跳过用例')),
                ('tests', models.IntegerField(verbose_name='总用例数')),
                ('run_time', models.FloatField(verbose_name='运行时长')),
                ('result', models.TextField(default='', verbose_name='详细')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
            ],
            options={
                'verbose_name': '测试任务',
                'verbose_name_plural': '测试任务',
            },
        ),
        migrations.AlterField(
            model_name='testtask',
            name='status',
            field=models.IntegerField(choices=[('0', '未执行'), ('1', '执行中'), ('2', '执行完成')], default='0', verbose_name='状态'),
        ),
        migrations.AddField(
            model_name='testresult',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apitest.TestTask', verbose_name='任务名称'),
        ),
    ]
