# CorrentlyIo.MeteringDecoratorApi

All URIs are relative to *https://api.corrently.io/v2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**meteringGet**](MeteringDecoratorApi.md#meteringGet) | **GET** /metering/reading | Meter Reading
[**meteringPost**](MeteringDecoratorApi.md#meteringPost) | **POST** /metering/reading | Meter Reading



## meteringGet

> MeteringGet200Response meteringGet(opts)

Meter Reading

Retrieves a metered reading using account (Stromkonto). 

### Example

```javascript
import CorrentlyIo from 'corrently_io';

let apiInstance = new CorrentlyIo.MeteringDecoratorApi();
let opts = {
  'account': "account_example" // String | Account/Address (Stromkonto) to retrieve reading for.
};
apiInstance.meteringGet(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account** | **String**| Account/Address (Stromkonto) to retrieve reading for. | [optional] 

### Return type

[**MeteringGet200Response**](MeteringGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## meteringPost

> MeteringPost200Response meteringPost(meteringPostRequest)

Meter Reading

Post meter reading and get it decorated. Best practice is to first create a new Stromkonto with the register method and choose a nice secret to protect updates. Now regularly send updates to get readings (consumption) split into green power (1.8.1) and grey power (1.8.2). 

### Example

```javascript
import CorrentlyIo from 'corrently_io';

let apiInstance = new CorrentlyIo.MeteringDecoratorApi();
let meteringPostRequest = new CorrentlyIo.MeteringPostRequest(); // MeteringPostRequest | 
apiInstance.meteringPost(meteringPostRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **meteringPostRequest** | [**MeteringPostRequest**](MeteringPostRequest.md)|  | 

### Return type

[**MeteringPost200Response**](MeteringPost200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

