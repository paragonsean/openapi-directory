# InfluxOssApiService.TemplatesApi

All URIs are relative to */api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteDocumentsTemplatesID**](TemplatesApi.md#deleteDocumentsTemplatesID) | **DELETE** /documents/templates/{templateID} | Delete a template
[**deleteDocumentsTemplatesIDLabelsID**](TemplatesApi.md#deleteDocumentsTemplatesIDLabelsID) | **DELETE** /documents/templates/{templateID}/labels/{labelID} | Delete a label from a template
[**getDocumentsTemplates**](TemplatesApi.md#getDocumentsTemplates) | **GET** /documents/templates | List all templates
[**getDocumentsTemplatesID**](TemplatesApi.md#getDocumentsTemplatesID) | **GET** /documents/templates/{templateID} | Retrieve a template
[**getDocumentsTemplatesIDLabels**](TemplatesApi.md#getDocumentsTemplatesIDLabels) | **GET** /documents/templates/{templateID}/labels | List all labels for a template
[**postDocumentsTemplates**](TemplatesApi.md#postDocumentsTemplates) | **POST** /documents/templates | Create a template
[**postDocumentsTemplatesIDLabels**](TemplatesApi.md#postDocumentsTemplatesIDLabels) | **POST** /documents/templates/{templateID}/labels | Add a label to a template
[**putDocumentsTemplatesID**](TemplatesApi.md#putDocumentsTemplatesID) | **PUT** /documents/templates/{templateID} | Update a template



## deleteDocumentsTemplatesID

> deleteDocumentsTemplatesID(templateID, opts)

Delete a template

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.TemplatesApi();
let templateID = "templateID_example"; // String | The template ID.
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}" // String | OpenTracing span context
};
apiInstance.deleteDocumentsTemplatesID(templateID, opts, (error, data, response) => {
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
 **templateID** | **String**| The template ID. | 
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteDocumentsTemplatesIDLabelsID

> deleteDocumentsTemplatesIDLabelsID(templateID, labelID, opts)

Delete a label from a template

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.TemplatesApi();
let templateID = "templateID_example"; // String | The template ID.
let labelID = "labelID_example"; // String | The label ID.
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}" // String | OpenTracing span context
};
apiInstance.deleteDocumentsTemplatesIDLabelsID(templateID, labelID, opts, (error, data, response) => {
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
 **templateID** | **String**| The template ID. | 
 **labelID** | **String**| The label ID. | 
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDocumentsTemplates

> Documents getDocumentsTemplates(opts)

List all templates

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.TemplatesApi();
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}", // String | OpenTracing span context
  'org': "org_example", // String | Specifies the name of the organization of the template.
  'orgID': "orgID_example" // String | Specifies the organization ID of the template.
};
apiInstance.getDocumentsTemplates(opts, (error, data, response) => {
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
 **org** | **String**| Specifies the name of the organization of the template. | [optional] 
 **orgID** | **String**| Specifies the organization ID of the template. | [optional] 

### Return type

[**Documents**](Documents.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDocumentsTemplatesID

> Document getDocumentsTemplatesID(templateID, opts)

Retrieve a template

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.TemplatesApi();
let templateID = "templateID_example"; // String | The template ID.
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}" // String | OpenTracing span context
};
apiInstance.getDocumentsTemplatesID(templateID, opts, (error, data, response) => {
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
 **templateID** | **String**| The template ID. | 
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 

### Return type

[**Document**](Document.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDocumentsTemplatesIDLabels

> LabelsResponse getDocumentsTemplatesIDLabels(templateID, opts)

List all labels for a template

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.TemplatesApi();
let templateID = "templateID_example"; // String | The template ID.
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}" // String | OpenTracing span context
};
apiInstance.getDocumentsTemplatesIDLabels(templateID, opts, (error, data, response) => {
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
 **templateID** | **String**| The template ID. | 
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 

### Return type

[**LabelsResponse**](LabelsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## postDocumentsTemplates

> Document postDocumentsTemplates(documentCreate, opts)

Create a template

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.TemplatesApi();
let documentCreate = new InfluxOssApiService.DocumentCreate(); // DocumentCreate | Template that will be created
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}" // String | OpenTracing span context
};
apiInstance.postDocumentsTemplates(documentCreate, opts, (error, data, response) => {
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
 **documentCreate** | [**DocumentCreate**](DocumentCreate.md)| Template that will be created | 
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 

### Return type

[**Document**](Document.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postDocumentsTemplatesIDLabels

> LabelResponse postDocumentsTemplatesIDLabels(templateID, labelMapping, opts)

Add a label to a template

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.TemplatesApi();
let templateID = "templateID_example"; // String | The template ID.
let labelMapping = new InfluxOssApiService.LabelMapping(); // LabelMapping | Label to add
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}" // String | OpenTracing span context
};
apiInstance.postDocumentsTemplatesIDLabels(templateID, labelMapping, opts, (error, data, response) => {
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
 **templateID** | **String**| The template ID. | 
 **labelMapping** | [**LabelMapping**](LabelMapping.md)| Label to add | 
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 

### Return type

[**LabelResponse**](LabelResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## putDocumentsTemplatesID

> Document putDocumentsTemplatesID(templateID, documentUpdate, opts)

Update a template

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.TemplatesApi();
let templateID = "templateID_example"; // String | The template ID.
let documentUpdate = new InfluxOssApiService.DocumentUpdate(); // DocumentUpdate | Template that will be updated
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}" // String | OpenTracing span context
};
apiInstance.putDocumentsTemplatesID(templateID, documentUpdate, opts, (error, data, response) => {
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
 **templateID** | **String**| The template ID. | 
 **documentUpdate** | [**DocumentUpdate**](DocumentUpdate.md)| Template that will be updated | 
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 

### Return type

[**Document**](Document.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

