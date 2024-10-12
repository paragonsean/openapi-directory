# TechPort.DefaultApi

All URIs are relative to *http://techport.nasa.gov/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiGet**](DefaultApi.md#apiGet) | **GET** /api | 
[**apiProjectsFormatGet**](DefaultApi.md#apiProjectsFormatGet) | **GET** /api/projects{.format} | 
[**apiProjectsIdFormatGet**](DefaultApi.md#apiProjectsIdFormatGet) | **GET** /api/projects/{id}{.format} | 



## apiGet

> apiGet()



Returns the swagger specification for the API.

### Example

```javascript
import TechPort from 'tech_port';

let apiInstance = new TechPort.DefaultApi();
apiInstance.apiGet((error, data, response) => {
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


## apiProjectsFormatGet

> ApiProjectsFormatGet200Response apiProjectsFormatGet(updatedSince, format, format2)



Returns a list of available technology project IDs.

### Example

```javascript
import TechPort from 'tech_port';

let apiInstance = new TechPort.DefaultApi();
let updatedSince = new Date("2013-10-20"); // Date | ISO 8601 full-date in the format YYYY-MM-DD. Filters the list of available ID values by their lastUpdated parameter.
let format = "'json'"; // String | The response type desired.
let format2 = "format_example"; // String | Automatically added
apiInstance.apiProjectsFormatGet(updatedSince, format, format2, (error, data, response) => {
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
 **updatedSince** | **Date**| ISO 8601 full-date in the format YYYY-MM-DD. Filters the list of available ID values by their lastUpdated parameter. | 
 **format** | **String**| The response type desired. | [default to &#39;json&#39;]
 **format2** | **String**| Automatically added | 

### Return type

[**ApiProjectsFormatGet200Response**](ApiProjectsFormatGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## apiProjectsIdFormatGet

> Project apiProjectsIdFormatGet(id, format, format2)



Returns information about a specific technology project.

### Example

```javascript
import TechPort from 'tech_port';

let apiInstance = new TechPort.DefaultApi();
let id = 789; // Number | ID of project to fetch
let format = "'xml'"; // String | The response type desired.
let format2 = "format_example"; // String | Automatically added
apiInstance.apiProjectsIdFormatGet(id, format, format2, (error, data, response) => {
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
 **id** | **Number**| ID of project to fetch | 
 **format** | **String**| The response type desired. | [default to &#39;xml&#39;]
 **format2** | **String**| Automatically added | 

### Return type

[**Project**](Project.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

