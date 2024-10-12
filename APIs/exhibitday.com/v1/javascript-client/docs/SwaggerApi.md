# TestTheExhibitDayApiWithSwagger.SwaggerApi

All URIs are relative to *https://api.exhibitday.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**swaggerGet**](SwaggerApi.md#swaggerGet) | **GET** /api/docs/Swagger | 



## swaggerGet

> Object swaggerGet()



### Example

```javascript
import TestTheExhibitDayApiWithSwagger from 'test_the_exhibit_day_api_with_swagger';

let apiInstance = new TestTheExhibitDayApiWithSwagger.SwaggerApi();
apiInstance.swaggerGet((error, data, response) => {
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
- **Accept**: application/json, text/json, application/xml, text/xml

