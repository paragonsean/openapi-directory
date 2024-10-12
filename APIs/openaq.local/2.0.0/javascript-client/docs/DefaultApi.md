# OpenAq.DefaultApi

All URIs are relative to *http://openaq.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**favicoFaviconIcoGet**](DefaultApi.md#favicoFaviconIcoGet) | **GET** /favicon.ico | Favico
[**pongPingGet**](DefaultApi.md#pongPingGet) | **GET** /ping | Pong



## favicoFaviconIcoGet

> Object favicoFaviconIcoGet()

Favico

### Example

```javascript
import OpenAq from 'open_aq';

let apiInstance = new OpenAq.DefaultApi();
apiInstance.favicoFaviconIcoGet((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## pongPingGet

> Object pongPingGet()

Pong

Sanity check. This will let the user know that the service is operational. And this path operation will: * show a lifesign

### Example

```javascript
import OpenAq from 'open_aq';

let apiInstance = new OpenAq.DefaultApi();
apiInstance.pongPingGet((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

