# SmartMe.AccountApi

All URIs are relative to *https://smart-me.com:443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**accountLogin**](AccountApi.md#accountLogin) | **GET** /api/Account/login | 
[**apiAccountLoginPost**](AccountApi.md#apiAccountLoginPost) | **POST** /api/Account/login | 



## accountLogin

> Object accountLogin()



### Example

```javascript
import SmartMe from 'smart_me';

let apiInstance = new SmartMe.AccountApi();
apiInstance.accountLogin((error, data, response) => {
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
- **Accept**: application/json, application/xml, text/json, text/xml


## apiAccountLoginPost

> Object apiAccountLoginPost()



### Example

```javascript
import SmartMe from 'smart_me';

let apiInstance = new SmartMe.AccountApi();
apiInstance.apiAccountLoginPost((error, data, response) => {
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
- **Accept**: application/json, application/xml, text/json, text/xml

