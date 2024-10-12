# Transform.DefaultApi

All URIs are relative to *https://gateway.wso2apistore.com/transform/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**jsontoxmlPost**](DefaultApi.md#jsontoxmlPost) | **POST** /jsontoxml | 
[**xmltojsonPost**](DefaultApi.md#xmltojsonPost) | **POST** /xmltojson | 



## jsontoxmlPost

> jsontoxmlPost(body)



### Example

```javascript
import Transform from 'transform';

let apiInstance = new Transform.DefaultApi();
let body = "body_example"; // String | JSON payload
apiInstance.jsontoxmlPost(body, (error, data, response) => {
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
 **body** | **String**| JSON payload | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## xmltojsonPost

> xmltojsonPost(body)



### Example

```javascript
import Transform from 'transform';

let apiInstance = new Transform.DefaultApi();
let body = "body_example"; // String | XML payload
apiInstance.xmltojsonPost(body, (error, data, response) => {
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
 **body** | **String**| XML payload | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: text/xml
- **Accept**: Not defined

