# InfluxOssApiService.ChecksApi

All URIs are relative to */api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createCheck**](ChecksApi.md#createCheck) | **POST** /checks | Add new check
[**deleteChecksID**](ChecksApi.md#deleteChecksID) | **DELETE** /checks/{checkID} | Delete a check
[**deleteChecksIDLabelsID**](ChecksApi.md#deleteChecksIDLabelsID) | **DELETE** /checks/{checkID}/labels/{labelID} | Delete label from a check
[**getChecks**](ChecksApi.md#getChecks) | **GET** /checks | List all checks
[**getChecksID**](ChecksApi.md#getChecksID) | **GET** /checks/{checkID} | Retrieve a check
[**getChecksIDLabels**](ChecksApi.md#getChecksIDLabels) | **GET** /checks/{checkID}/labels | List all labels for a check
[**getChecksIDQuery**](ChecksApi.md#getChecksIDQuery) | **GET** /checks/{checkID}/query | Retrieve a check query
[**patchChecksID**](ChecksApi.md#patchChecksID) | **PATCH** /checks/{checkID} | Update a check
[**postChecksIDLabels**](ChecksApi.md#postChecksIDLabels) | **POST** /checks/{checkID}/labels | Add a label to a check
[**putChecksID**](ChecksApi.md#putChecksID) | **PUT** /checks/{checkID} | Update a check



## createCheck

> Check createCheck(postCheck)

Add new check

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.ChecksApi();
let postCheck = new InfluxOssApiService.PostCheck(); // PostCheck | Check to create
apiInstance.createCheck(postCheck, (error, data, response) => {
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
 **postCheck** | [**PostCheck**](PostCheck.md)| Check to create | 

### Return type

[**Check**](Check.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteChecksID

> deleteChecksID(checkID, opts)

Delete a check

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.ChecksApi();
let checkID = "checkID_example"; // String | The check ID.
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}" // String | OpenTracing span context
};
apiInstance.deleteChecksID(checkID, opts, (error, data, response) => {
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
 **checkID** | **String**| The check ID. | 
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteChecksIDLabelsID

> deleteChecksIDLabelsID(checkID, labelID, opts)

Delete label from a check

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.ChecksApi();
let checkID = "checkID_example"; // String | The check ID.
let labelID = "labelID_example"; // String | The ID of the label to delete.
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}" // String | OpenTracing span context
};
apiInstance.deleteChecksIDLabelsID(checkID, labelID, opts, (error, data, response) => {
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
 **checkID** | **String**| The check ID. | 
 **labelID** | **String**| The ID of the label to delete. | 
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getChecks

> Checks getChecks(orgID, opts)

List all checks

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.ChecksApi();
let orgID = "orgID_example"; // String | Only show checks that belong to a specific organization ID.
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}", // String | OpenTracing span context
  'offset': 56, // Number | 
  'limit': 20 // Number | 
};
apiInstance.getChecks(orgID, opts, (error, data, response) => {
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
 **orgID** | **String**| Only show checks that belong to a specific organization ID. | 
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 
 **offset** | **Number**|  | [optional] 
 **limit** | **Number**|  | [optional] [default to 20]

### Return type

[**Checks**](Checks.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getChecksID

> Check getChecksID(checkID, opts)

Retrieve a check

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.ChecksApi();
let checkID = "checkID_example"; // String | The check ID.
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}" // String | OpenTracing span context
};
apiInstance.getChecksID(checkID, opts, (error, data, response) => {
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
 **checkID** | **String**| The check ID. | 
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 

### Return type

[**Check**](Check.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getChecksIDLabels

> LabelsResponse getChecksIDLabels(checkID, opts)

List all labels for a check

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.ChecksApi();
let checkID = "checkID_example"; // String | The check ID.
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}" // String | OpenTracing span context
};
apiInstance.getChecksIDLabels(checkID, opts, (error, data, response) => {
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
 **checkID** | **String**| The check ID. | 
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 

### Return type

[**LabelsResponse**](LabelsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getChecksIDQuery

> FluxResponse getChecksIDQuery(checkID, opts)

Retrieve a check query

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.ChecksApi();
let checkID = "checkID_example"; // String | The check ID.
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}" // String | OpenTracing span context
};
apiInstance.getChecksIDQuery(checkID, opts, (error, data, response) => {
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
 **checkID** | **String**| The check ID. | 
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 

### Return type

[**FluxResponse**](FluxResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## patchChecksID

> Check patchChecksID(checkID, checkPatch, opts)

Update a check

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.ChecksApi();
let checkID = "checkID_example"; // String | The check ID.
let checkPatch = new InfluxOssApiService.CheckPatch(); // CheckPatch | Check update to apply
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}" // String | OpenTracing span context
};
apiInstance.patchChecksID(checkID, checkPatch, opts, (error, data, response) => {
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
 **checkID** | **String**| The check ID. | 
 **checkPatch** | [**CheckPatch**](CheckPatch.md)| Check update to apply | 
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 

### Return type

[**Check**](Check.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postChecksIDLabels

> LabelResponse postChecksIDLabels(checkID, labelMapping, opts)

Add a label to a check

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.ChecksApi();
let checkID = "checkID_example"; // String | The check ID.
let labelMapping = new InfluxOssApiService.LabelMapping(); // LabelMapping | Label to add
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}" // String | OpenTracing span context
};
apiInstance.postChecksIDLabels(checkID, labelMapping, opts, (error, data, response) => {
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
 **checkID** | **String**| The check ID. | 
 **labelMapping** | [**LabelMapping**](LabelMapping.md)| Label to add | 
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 

### Return type

[**LabelResponse**](LabelResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## putChecksID

> Check putChecksID(checkID, check, opts)

Update a check

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.ChecksApi();
let checkID = "checkID_example"; // String | The check ID.
let check = new InfluxOssApiService.Check(); // Check | Check update to apply
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}" // String | OpenTracing span context
};
apiInstance.putChecksID(checkID, check, opts, (error, data, response) => {
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
 **checkID** | **String**| The check ID. | 
 **check** | [**Check**](Check.md)| Check update to apply | 
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 

### Return type

[**Check**](Check.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

