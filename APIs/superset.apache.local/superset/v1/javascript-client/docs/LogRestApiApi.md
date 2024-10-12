# Superset.LogRestApiApi

All URIs are relative to *http://superset.apache.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**logGet**](LogRestApiApi.md#logGet) | **GET** /log/ | 
[**logPkGet**](LogRestApiApi.md#logPkGet) | **GET** /log/{pk} | 
[**logPost**](LogRestApiApi.md#logPost) | **POST** /log/ | 



## logGet

> LogGet200Response logGet(opts)



Get a list of models

### Example

```javascript
import Superset from 'superset';
let defaultClient = Superset.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new Superset.LogRestApiApi();
let opts = {
  'q': new Superset.GetListSchema() // GetListSchema | 
};
apiInstance.logGet(opts, (error, data, response) => {
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
 **q** | [**GetListSchema**](.md)|  | [optional] 

### Return type

[**LogGet200Response**](LogGet200Response.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## logPkGet

> LogPkGet200Response logPkGet(pk, opts)



Get an item model

### Example

```javascript
import Superset from 'superset';
let defaultClient = Superset.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new Superset.LogRestApiApi();
let pk = 56; // Number | 
let opts = {
  'q': new Superset.GetItemSchema() // GetItemSchema | 
};
apiInstance.logPkGet(pk, opts, (error, data, response) => {
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
 **pk** | **Number**|  | 
 **q** | [**GetItemSchema**](.md)|  | [optional] 

### Return type

[**LogPkGet200Response**](LogPkGet200Response.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## logPost

> LogPost201Response logPost(logRestApiPost)



### Example

```javascript
import Superset from 'superset';
let defaultClient = Superset.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new Superset.LogRestApiApi();
let logRestApiPost = new Superset.LogRestApiPost(); // LogRestApiPost | Model schema
apiInstance.logPost(logRestApiPost, (error, data, response) => {
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
 **logRestApiPost** | [**LogRestApiPost**](LogRestApiPost.md)| Model schema | 

### Return type

[**LogPost201Response**](LogPost201Response.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

