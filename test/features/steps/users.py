from behave import *
import requests
import json
from flask import jsonify
from hamcrest import assert_that, equal_to


@given(u'app is running')
def app_running(context):
    context.url = 'http://localhost:5000/users/'
    # //raise NotImplementedError(u'STEP: Given app is running')


@when(u'I hit url with \'{userid}\'')
def step_impl(context,userid):
    context.res = requests.session().get(url=context.url+userid)
    # print(context.res)


@then(u'I should get a \'{status}\' response')
def step_impl(context,status):
    assert_that(context.res.status_code,equal_to(int(status)))


@then(u'the following user details are returned')
def step_impl(context):
    for row in context.table:
        assert_that(context.res.json(),equal_to(row['name']))