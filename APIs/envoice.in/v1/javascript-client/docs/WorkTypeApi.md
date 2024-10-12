# ApiV100.WorkTypeApi

All URIs are relative to *https://www.envoice.in*

Method | HTTP request | Description
------------- | ------------- | -------------
[**workTypeApiAll**](WorkTypeApi.md#workTypeApiAll) | **GET** /api/worktype/all | Return all work types for the account
[**workTypeApiDelete**](WorkTypeApi.md#workTypeApiDelete) | **POST** /api/worktype/delete | Delete an existing work type
[**workTypeApiDetails**](WorkTypeApi.md#workTypeApiDetails) | **GET** /api/worktype/details | Return work type details
[**workTypeApiNew**](WorkTypeApi.md#workTypeApiNew) | **POST** /api/worktype/new | Create a work type
[**workTypeApiSearch**](WorkTypeApi.md#workTypeApiSearch) | **GET** /api/worktype/search | Return all work types for the account that match the query param
[**workTypeApiUpdate**](WorkTypeApi.md#workTypeApiUpdate) | **POST** /api/worktype/update | Update an existing work type



## workTypeApiAll

> [WorkTypeDetailsApiModel] workTypeApiAll(xAuthKey, xAuthSecret)

Return all work types for the account

### Example

```javascript
import ApiV100 from 'api_v1_0_0';

let apiInstance = new ApiV100.WorkTypeApi();
let xAuthKey = "'[authentication key]'"; // String | 
let xAuthSecret = "'[authentication secret]'"; // String | 
apiInstance.workTypeApiAll(xAuthKey, xAuthSecret, (error, data, response) => {
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
 **xAuthKey** | **String**|  | [default to &#39;[authentication key]&#39;]
 **xAuthSecret** | **String**|  | [default to &#39;[authentication secret]&#39;]

### Return type

[**[WorkTypeDetailsApiModel]**](WorkTypeDetailsApiModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/html, text/json, text/xml


## workTypeApiDelete

> Number workTypeApiDelete(xAuthKey, xAuthSecret, workTypeDeleteApiModel)

Delete an existing work type

### Example

```javascript
import ApiV100 from 'api_v1_0_0';

let apiInstance = new ApiV100.WorkTypeApi();
let xAuthKey = "'[authentication key]'"; // String | 
let xAuthSecret = "'[authentication secret]'"; // String | 
let workTypeDeleteApiModel = new ApiV100.WorkTypeDeleteApiModel(); // WorkTypeDeleteApiModel | 
apiInstance.workTypeApiDelete(xAuthKey, xAuthSecret, workTypeDeleteApiModel, (error, data, response) => {
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
 **xAuthKey** | **String**|  | [default to &#39;[authentication key]&#39;]
 **xAuthSecret** | **String**|  | [default to &#39;[authentication secret]&#39;]
 **workTypeDeleteApiModel** | [**WorkTypeDeleteApiModel**](WorkTypeDeleteApiModel.md)|  | 

### Return type

**Number**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/html, text/json, text/xml
- **Accept**: application/json, application/xml, text/html, text/json, text/xml


## workTypeApiDetails

> WorkTypeDetailsApiModel workTypeApiDetails(workTypeId, xAuthKey, xAuthSecret)

Return work type details

### Example

```javascript
import ApiV100 from 'api_v1_0_0';

let apiInstance = new ApiV100.WorkTypeApi();
let workTypeId = 56; // Number | 
let xAuthKey = "'[authentication key]'"; // String | 
let xAuthSecret = "'[authentication secret]'"; // String | 
apiInstance.workTypeApiDetails(workTypeId, xAuthKey, xAuthSecret, (error, data, response) => {
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
 **workTypeId** | **Number**|  | 
 **xAuthKey** | **String**|  | [default to &#39;[authentication key]&#39;]
 **xAuthSecret** | **String**|  | [default to &#39;[authentication secret]&#39;]

### Return type

[**WorkTypeDetailsApiModel**](WorkTypeDetailsApiModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/html, text/json, text/xml


## workTypeApiNew

> Number workTypeApiNew(xAuthKey, xAuthSecret, workTypeCreateApiModel)

Create a work type

### Example

```javascript
import ApiV100 from 'api_v1_0_0';

let apiInstance = new ApiV100.WorkTypeApi();
let xAuthKey = "'[authentication key]'"; // String | 
let xAuthSecret = "'[authentication secret]'"; // String | 
let workTypeCreateApiModel = new ApiV100.WorkTypeCreateApiModel(); // WorkTypeCreateApiModel | 
apiInstance.workTypeApiNew(xAuthKey, xAuthSecret, workTypeCreateApiModel, (error, data, response) => {
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
 **xAuthKey** | **String**|  | [default to &#39;[authentication key]&#39;]
 **xAuthSecret** | **String**|  | [default to &#39;[authentication secret]&#39;]
 **workTypeCreateApiModel** | [**WorkTypeCreateApiModel**](WorkTypeCreateApiModel.md)|  | 

### Return type

**Number**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/html, text/json, text/xml
- **Accept**: application/json, application/xml, text/html, text/json, text/xml


## workTypeApiSearch

> [WorkTypeDetailsApiModel] workTypeApiSearch(xAuthKey, xAuthSecret, opts)

Return all work types for the account that match the query param

### Example

```javascript
import ApiV100 from 'api_v1_0_0';

let apiInstance = new ApiV100.WorkTypeApi();
let xAuthKey = "'[authentication key]'"; // String | 
let xAuthSecret = "'[authentication secret]'"; // String | 
let opts = {
  'queryOptionsQuery': "queryOptionsQuery_example", // String | 
  'queryOptionsOrderBy': "queryOptionsOrderBy_example", // String | 
  'queryOptionsOrder': "queryOptionsOrder_example", // String | 
  'queryOptionsPage': 56, // Number | 
  'queryOptionsPageSize': 56 // Number | 
};
apiInstance.workTypeApiSearch(xAuthKey, xAuthSecret, opts, (error, data, response) => {
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
 **xAuthKey** | **String**|  | [default to &#39;[authentication key]&#39;]
 **xAuthSecret** | **String**|  | [default to &#39;[authentication secret]&#39;]
 **queryOptionsQuery** | **String**|  | [optional] 
 **queryOptionsOrderBy** | **String**|  | [optional] 
 **queryOptionsOrder** | **String**|  | [optional] 
 **queryOptionsPage** | **Number**|  | [optional] 
 **queryOptionsPageSize** | **Number**|  | [optional] 

### Return type

[**[WorkTypeDetailsApiModel]**](WorkTypeDetailsApiModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/html, text/json, text/xml


## workTypeApiUpdate

> workTypeApiUpdate(xAuthKey, xAuthSecret, workTypeUpdateApiModel)

Update an existing work type

### Example

```javascript
import ApiV100 from 'api_v1_0_0';

let apiInstance = new ApiV100.WorkTypeApi();
let xAuthKey = "'[authentication key]'"; // String | 
let xAuthSecret = "'[authentication secret]'"; // String | 
let workTypeUpdateApiModel = new ApiV100.WorkTypeUpdateApiModel(); // WorkTypeUpdateApiModel | 
apiInstance.workTypeApiUpdate(xAuthKey, xAuthSecret, workTypeUpdateApiModel, (error, data, response) => {
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
 **xAuthKey** | **String**|  | [default to &#39;[authentication key]&#39;]
 **xAuthSecret** | **String**|  | [default to &#39;[authentication secret]&#39;]
 **workTypeUpdateApiModel** | [**WorkTypeUpdateApiModel**](WorkTypeUpdateApiModel.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/html, text/json, text/xml
- **Accept**: Not defined

