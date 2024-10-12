# ConfigCatPublicManagementApi.SegmentsApi

All URIs are relative to *https://api.configcat.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createSegment**](SegmentsApi.md#createSegment) | **POST** /v1/products/{productId}/segments | Create Segment
[**deleteSegment**](SegmentsApi.md#deleteSegment) | **DELETE** /v1/segments/{segmentId} | Delete Segment
[**getSegment**](SegmentsApi.md#getSegment) | **GET** /v1/segments/{segmentId} | Get Segment
[**getSegments**](SegmentsApi.md#getSegments) | **GET** /v1/products/{productId}/segments | List Segments
[**updateSegment**](SegmentsApi.md#updateSegment) | **PUT** /v1/segments/{segmentId} | Update Segment



## createSegment

> SegmentModelHaljson createSegment(productId, createSegmentModel)

Create Segment

This endpoint creates a new Segment in a specified Product  identified by the &#x60;productId&#x60; parameter, which can be obtained from the [List Products](#operation/get-products) endpoint.

### Example

```javascript
import ConfigCatPublicManagementApi from 'config_cat_public_management_api';
let defaultClient = ConfigCatPublicManagementApi.ApiClient.instance;
// Configure HTTP basic authorization: Basic
let Basic = defaultClient.authentications['Basic'];
Basic.username = 'YOUR USERNAME';
Basic.password = 'YOUR PASSWORD';

let apiInstance = new ConfigCatPublicManagementApi.SegmentsApi();
let productId = "productId_example"; // String | The identifier of the Product.
let createSegmentModel = new ConfigCatPublicManagementApi.CreateSegmentModel(); // CreateSegmentModel | 
apiInstance.createSegment(productId, createSegmentModel, (error, data, response) => {
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
 **productId** | **String**| The identifier of the Product. | 
 **createSegmentModel** | [**CreateSegmentModel**](CreateSegmentModel.md)|  | 

### Return type

[**SegmentModelHaljson**](SegmentModelHaljson.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

- **Content-Type**: application/*+json, application/json, text/json
- **Accept**: application/hal+json, application/json


## deleteSegment

> deleteSegment(segmentId)

Delete Segment

This endpoint removes a Segment identified by the &#x60;segmentId&#x60; parameter.

### Example

```javascript
import ConfigCatPublicManagementApi from 'config_cat_public_management_api';
let defaultClient = ConfigCatPublicManagementApi.ApiClient.instance;
// Configure HTTP basic authorization: Basic
let Basic = defaultClient.authentications['Basic'];
Basic.username = 'YOUR USERNAME';
Basic.password = 'YOUR PASSWORD';

let apiInstance = new ConfigCatPublicManagementApi.SegmentsApi();
let segmentId = "segmentId_example"; // String | The identifier of the Segment.
apiInstance.deleteSegment(segmentId, (error, data, response) => {
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
 **segmentId** | **String**| The identifier of the Segment. | 

### Return type

null (empty response body)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getSegment

> SegmentModelHaljson getSegment(segmentId)

Get Segment

This endpoint returns the metadata of a Segment identified by the &#x60;segmentId&#x60;.

### Example

```javascript
import ConfigCatPublicManagementApi from 'config_cat_public_management_api';
let defaultClient = ConfigCatPublicManagementApi.ApiClient.instance;
// Configure HTTP basic authorization: Basic
let Basic = defaultClient.authentications['Basic'];
Basic.username = 'YOUR USERNAME';
Basic.password = 'YOUR PASSWORD';

let apiInstance = new ConfigCatPublicManagementApi.SegmentsApi();
let segmentId = "segmentId_example"; // String | The identifier of the Segment.
apiInstance.getSegment(segmentId, (error, data, response) => {
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
 **segmentId** | **String**| The identifier of the Segment. | 

### Return type

[**SegmentModelHaljson**](SegmentModelHaljson.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/hal+json, application/json


## getSegments

> [SegmentListModelHaljson] getSegments(productId)

List Segments

This endpoint returns the list of the Segments that belongs to the given Product identified by the &#x60;productId&#x60; parameter, which can be obtained from the [List Products](#operation/get-products) endpoint.

### Example

```javascript
import ConfigCatPublicManagementApi from 'config_cat_public_management_api';
let defaultClient = ConfigCatPublicManagementApi.ApiClient.instance;
// Configure HTTP basic authorization: Basic
let Basic = defaultClient.authentications['Basic'];
Basic.username = 'YOUR USERNAME';
Basic.password = 'YOUR PASSWORD';

let apiInstance = new ConfigCatPublicManagementApi.SegmentsApi();
let productId = "productId_example"; // String | The identifier of the Product.
apiInstance.getSegments(productId, (error, data, response) => {
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
 **productId** | **String**| The identifier of the Product. | 

### Return type

[**[SegmentListModelHaljson]**](SegmentListModelHaljson.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/hal+json, application/json


## updateSegment

> SegmentModelHaljson updateSegment(segmentId, updateSegmentModel)

Update Segment

This endpoint updates a Segment identified by the &#x60;segmentId&#x60; parameter.

### Example

```javascript
import ConfigCatPublicManagementApi from 'config_cat_public_management_api';
let defaultClient = ConfigCatPublicManagementApi.ApiClient.instance;
// Configure HTTP basic authorization: Basic
let Basic = defaultClient.authentications['Basic'];
Basic.username = 'YOUR USERNAME';
Basic.password = 'YOUR PASSWORD';

let apiInstance = new ConfigCatPublicManagementApi.SegmentsApi();
let segmentId = "segmentId_example"; // String | The identifier of the Segment.
let updateSegmentModel = new ConfigCatPublicManagementApi.UpdateSegmentModel(); // UpdateSegmentModel | 
apiInstance.updateSegment(segmentId, updateSegmentModel, (error, data, response) => {
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
 **segmentId** | **String**| The identifier of the Segment. | 
 **updateSegmentModel** | [**UpdateSegmentModel**](UpdateSegmentModel.md)|  | 

### Return type

[**SegmentModelHaljson**](SegmentModelHaljson.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

- **Content-Type**: application/*+json, application/json, text/json
- **Accept**: application/hal+json, application/json

