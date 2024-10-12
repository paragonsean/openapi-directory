# HackathonWatch.SwaggerDocApi

All URIs are relative to *http://www.hackathonwatch.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**gETSwaggerDocFormat**](SwaggerDocApi.md#gETSwaggerDocFormat) | **GET** /swagger_doc.json | Swagger compatible API description
[**gETSwaggerDocNameFormat**](SwaggerDocApi.md#gETSwaggerDocNameFormat) | **GET** /swagger_doc/{name}.json | Swagger compatible API description for specific API



## gETSwaggerDocFormat

> gETSwaggerDocFormat()

Swagger compatible API description

### Example

```javascript
import HackathonWatch from 'hackathon_watch';

let apiInstance = new HackathonWatch.SwaggerDocApi();
apiInstance.gETSwaggerDocFormat((error, data, response) => {
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


## gETSwaggerDocNameFormat

> gETSwaggerDocNameFormat(name)

Swagger compatible API description for specific API

### Example

```javascript
import HackathonWatch from 'hackathon_watch';

let apiInstance = new HackathonWatch.SwaggerDocApi();
let name = "name_example"; // String | Resource name of mounted API
apiInstance.gETSwaggerDocNameFormat(name, (error, data, response) => {
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
 **name** | **String**| Resource name of mounted API | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

