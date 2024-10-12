# AvazaApiDocumentation.EstimateApi

All URIs are relative to *https://api.avaza.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**estimateGet**](EstimateApi.md#estimateGet) | **GET** /api/Estimate | Gets list of Estimates
[**estimateGetByID**](EstimateApi.md#estimateGetByID) | **GET** /api/Estimate/{id} | Gets Estimate by Estimate ID
[**estimatePost**](EstimateApi.md#estimatePost) | **POST** /api/Estimate | Create a new draft Estimate



## estimateGet

> EstimateList estimateGet(opts)

Gets list of Estimates

EstimateStatusCode values are: \&quot;Draft\&quot;, \&quot;Sent\&quot;, \&quot;Accepted\&quot;, \&quot;Converted\&quot;, \&quot;Expired\&quot;, \&quot;Rejected\&quot;

### Example

```javascript
import AvazaApiDocumentation from 'avaza_api_documentation';
let defaultClient = AvazaApiDocumentation.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AvazaApiDocumentation.EstimateApi();
let opts = {
  'updatedAfter': new Date("2013-10-20T19:20:30+01:00"), // Date | 
  'pageSize': 56, // Number | Number of items per page (max 1000)
  'pageNumber': 56, // Number | Page to display. Starts from 1.
  'sort': "sort_example", // String | 
  'companyIDFK': 56 // Number | 
};
apiInstance.estimateGet(opts, (error, data, response) => {
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
 **updatedAfter** | **Date**|  | [optional] 
 **pageSize** | **Number**| Number of items per page (max 1000) | [optional] 
 **pageNumber** | **Number**| Page to display. Starts from 1. | [optional] 
 **sort** | **String**|  | [optional] 
 **companyIDFK** | **Number**|  | [optional] 

### Return type

[**EstimateList**](EstimateList.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## estimateGetByID

> estimateGetByID(id)

Gets Estimate by Estimate ID

### Example

```javascript
import AvazaApiDocumentation from 'avaza_api_documentation';
let defaultClient = AvazaApiDocumentation.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AvazaApiDocumentation.EstimateApi();
let id = 789; // Number | Estimate Estimate ID number
apiInstance.estimateGetByID(id, (error, data, response) => {
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
 **id** | **Number**| Estimate Estimate ID number | 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## estimatePost

> EstimateDetails estimatePost(model)

Create a new draft Estimate

### Example

```javascript
import AvazaApiDocumentation from 'avaza_api_documentation';
let defaultClient = AvazaApiDocumentation.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AvazaApiDocumentation.EstimateApi();
let model = new AvazaApiDocumentation.NewEstimate(); // NewEstimate | 
apiInstance.estimatePost(model, (error, data, response) => {
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
 **model** | [**NewEstimate**](NewEstimate.md)|  | 

### Return type

[**EstimateDetails**](EstimateDetails.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
- **Accept**: application/json, text/json, application/xml, text/xml

