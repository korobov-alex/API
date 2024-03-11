import requests
from behave import given, when, then


# Given steps
@given('the API is available')
def step_impl(context):
    context.base_url = 'http://127.0.0.1:8000'


# When steps
@when('I add a product with correct data')
def step_impl(context):
    # Creating payload with correct data
    payload = {
        "title": "NewBook",
        "author": "NewAuthor",
        "genre": "NewGenre",
        "year": 2000,
        "cover": "NewCover",
        "price": 1200,
        "amount": 10,
        "status": True
    }
    # Sending POST request to add a product
    context.response = requests.post(f'{context.base_url}/', json=payload)


@when('I add a product with negative price')
def step_impl(context):
    # Creating payload with negative price
    payload = {
        "title": "NewBook",
        "author": "NewAuthor",
        "genre": "NewGenre",
        "year": 2000,
        "cover": "NewCover",
        "price": 1200,
        "amount": -10,
        "status": True
    }
    # Sending POST request with negative price
    context.response = requests.post(f'{context.base_url}/', json=payload)


@when('I change a product date to amount 0')
def step_impl(context):
    product_id = '65ef51f5687dcd4e1c910ab6'
    # Creating payload to change amount to 0
    payload = {
        "title": "NewBook",
        "author": "NewAuthor",
        "genre": "NewGenre",
        "year": 2000,
        "cover": "NewCover",
        "price": 1200,
        "amount": 0,
    }
    # Sending PUT request to change product amount
    context.response = requests.put(f'{context.base_url}/{product_id}', json=payload)


@when('I request the history of changes for a specific ID')
def step_impl(context):
    product_id = '65ef51f5687dcd4e1c910ab6'
    # Sending GET request to get history of changes for specific ID
    context.response = requests.get(f'{context.base_url}/history/{product_id}')


# Then steps
@then('the product is successfully added')
def step_impl(context):
    # Asserting that the response status code is 200 (OK)
    assert context.response.status_code == 200


@then('the API returns an error')
def step_impl(context):
    # Asserting that the response status code is 422 (Unprocessable Entity)
    assert context.response.status_code == 422


@then('the product status is False')
def step_impl(context):
    # Asserting that the 'status' key in the response JSON is False
    assert context.response.json()['status'] is False


@then('the API returns the history of changes')
def step_impl(context):
    # Asserting that the response status code is 200 (OK)
    assert context.response.status_code == 200
