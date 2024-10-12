# InfluxOssApiService.LabelsApi

All URIs are relative to */api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteLabelsID**](LabelsApi.md#deleteLabelsID) | **DELETE** /labels/{labelID} | Delete a label
[**getLabels**](LabelsApi.md#getLabels) | **GET** /labels | List all labels
[**getLabelsID**](LabelsApi.md#getLabelsID) | **GET** /labels/{labelID} | Retrieve a label
[**patchLabelsID**](LabelsApi.md#patchLabelsID) | **PATCH** /labels/{labelID} | Update a label
[**postLabels**](LabelsApi.md#postLabels) | **POST** /labels | Create a label



## deleteLabelsID

> deleteLabelsID(labelID, opts)

Delete a label

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.LabelsApi();
let labelID = "labelID_example"; // String | The ID of the label to delete.
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}" // String | OpenTracing span context
};
apiInstance.deleteLabelsID(labelID, opts, (error, data, response) => {
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
 **labelID** | **String**| The ID of the label to delete. | 
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getLabels

> LabelsResponse getLabels(opts)

List all labels

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.LabelsApi();
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}", // String | OpenTracing span context
  'orgID': "orgID_example" // String | The organization ID.
};
apiInstance.getLabels(opts, (error, data, response) => {
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
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 
 **orgID** | **String**| The organization ID. | [optional] 

### Return type

[**LabelsResponse**](LabelsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getLabelsID

> LabelResponse getLabelsID(labelID, opts)

Retrieve a label

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.LabelsApi();
let labelID = "labelID_example"; // String | The ID of the label to update.
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}" // String | OpenTracing span context
};
apiInstance.getLabelsID(labelID, opts, (error, data, response) => {
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
 **labelID** | **String**| The ID of the label to update. | 
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 

### Return type

[**LabelResponse**](LabelResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## patchLabelsID

> LabelResponse patchLabelsID(labelID, labelUpdate, opts)

Update a label

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.LabelsApi();
let labelID = "labelID_example"; // String | The ID of the label to update.
let labelUpdate = new InfluxOssApiService.LabelUpdate(); // LabelUpdate | Label update
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}" // String | OpenTracing span context
};
apiInstance.patchLabelsID(labelID, labelUpdate, opts, (error, data, response) => {
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
 **labelID** | **String**| The ID of the label to update. | 
 **labelUpdate** | [**LabelUpdate**](LabelUpdate.md)| Label update | 
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 

### Return type

[**LabelResponse**](LabelResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postLabels

> LabelResponse postLabels(labelCreateRequest)

Create a label

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.LabelsApi();
let labelCreateRequest = new InfluxOssApiService.LabelCreateRequest(); // LabelCreateRequest | Label to create
apiInstance.postLabels(labelCreateRequest, (error, data, response) => {
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
 **labelCreateRequest** | [**LabelCreateRequest**](LabelCreateRequest.md)| Label to create | 

### Return type

[**LabelResponse**](LabelResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

