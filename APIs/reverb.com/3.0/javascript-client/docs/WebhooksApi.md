# Reverb.WebhooksApi

All URIs are relative to *https://api.reverb.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**webhooksRegistrationsGet**](WebhooksApi.md#webhooksRegistrationsGet) | **GET** /webhooks/registrations | Get webhook registrations
[**webhooksRegistrationsIdDelete**](WebhooksApi.md#webhooksRegistrationsIdDelete) | **DELETE** /webhooks/registrations/{id} | Remove a webhook
[**webhooksRegistrationsIdGet**](WebhooksApi.md#webhooksRegistrationsIdGet) | **GET** /webhooks/registrations/{id} | Get details of a webhook registration
[**webhooksRegistrationsPost**](WebhooksApi.md#webhooksRegistrationsPost) | **POST** /webhooks/registrations | Register a webhook



## webhooksRegistrationsGet

> webhooksRegistrationsGet()

Get webhook registrations

Get webhook registrations

### Example

```javascript
import Reverb from 'reverb';

let apiInstance = new Reverb.WebhooksApi();
apiInstance.webhooksRegistrationsGet((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## webhooksRegistrationsIdDelete

> webhooksRegistrationsIdDelete(id)

Remove a webhook

Remove a webhook

### Example

```javascript
import Reverb from 'reverb';

let apiInstance = new Reverb.WebhooksApi();
let id = "id_example"; // String | 
apiInstance.webhooksRegistrationsIdDelete(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## webhooksRegistrationsIdGet

> webhooksRegistrationsIdGet(id)

Get details of a webhook registration

Get details of a webhook registration

### Example

```javascript
import Reverb from 'reverb';

let apiInstance = new Reverb.WebhooksApi();
let id = "id_example"; // String | 
apiInstance.webhooksRegistrationsIdGet(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## webhooksRegistrationsPost

> webhooksRegistrationsPost(opts)

Register a webhook

Register a webhook

### Example

```javascript
import Reverb from 'reverb';

let apiInstance = new Reverb.WebhooksApi();
let opts = {
  'webhooksRegistrationsPostRequest': new Reverb.WebhooksRegistrationsPostRequest() // WebhooksRegistrationsPostRequest | the content of the request
};
apiInstance.webhooksRegistrationsPost(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhooksRegistrationsPostRequest** | [**WebhooksRegistrationsPostRequest**](WebhooksRegistrationsPostRequest.md)| the content of the request | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

