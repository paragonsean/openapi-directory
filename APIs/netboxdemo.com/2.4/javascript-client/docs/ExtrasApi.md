# NetBoxApi.ExtrasApi

All URIs are relative to *http://netboxdemo.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**extrasChoicesList**](ExtrasApi.md#extrasChoicesList) | **GET** /extras/_choices/ | 
[**extrasChoicesRead**](ExtrasApi.md#extrasChoicesRead) | **GET** /extras/_choices/{id}/ | 
[**extrasConfigContextsCreate**](ExtrasApi.md#extrasConfigContextsCreate) | **POST** /extras/config-contexts/ | 
[**extrasConfigContextsDelete**](ExtrasApi.md#extrasConfigContextsDelete) | **DELETE** /extras/config-contexts/{id}/ | 
[**extrasConfigContextsList**](ExtrasApi.md#extrasConfigContextsList) | **GET** /extras/config-contexts/ | 
[**extrasConfigContextsPartialUpdate**](ExtrasApi.md#extrasConfigContextsPartialUpdate) | **PATCH** /extras/config-contexts/{id}/ | 
[**extrasConfigContextsRead**](ExtrasApi.md#extrasConfigContextsRead) | **GET** /extras/config-contexts/{id}/ | 
[**extrasConfigContextsUpdate**](ExtrasApi.md#extrasConfigContextsUpdate) | **PUT** /extras/config-contexts/{id}/ | 
[**extrasExportTemplatesCreate**](ExtrasApi.md#extrasExportTemplatesCreate) | **POST** /extras/export-templates/ | 
[**extrasExportTemplatesDelete**](ExtrasApi.md#extrasExportTemplatesDelete) | **DELETE** /extras/export-templates/{id}/ | 
[**extrasExportTemplatesList**](ExtrasApi.md#extrasExportTemplatesList) | **GET** /extras/export-templates/ | 
[**extrasExportTemplatesPartialUpdate**](ExtrasApi.md#extrasExportTemplatesPartialUpdate) | **PATCH** /extras/export-templates/{id}/ | 
[**extrasExportTemplatesRead**](ExtrasApi.md#extrasExportTemplatesRead) | **GET** /extras/export-templates/{id}/ | 
[**extrasExportTemplatesUpdate**](ExtrasApi.md#extrasExportTemplatesUpdate) | **PUT** /extras/export-templates/{id}/ | 
[**extrasGraphsCreate**](ExtrasApi.md#extrasGraphsCreate) | **POST** /extras/graphs/ | 
[**extrasGraphsDelete**](ExtrasApi.md#extrasGraphsDelete) | **DELETE** /extras/graphs/{id}/ | 
[**extrasGraphsList**](ExtrasApi.md#extrasGraphsList) | **GET** /extras/graphs/ | 
[**extrasGraphsPartialUpdate**](ExtrasApi.md#extrasGraphsPartialUpdate) | **PATCH** /extras/graphs/{id}/ | 
[**extrasGraphsRead**](ExtrasApi.md#extrasGraphsRead) | **GET** /extras/graphs/{id}/ | 
[**extrasGraphsUpdate**](ExtrasApi.md#extrasGraphsUpdate) | **PUT** /extras/graphs/{id}/ | 
[**extrasImageAttachmentsCreate**](ExtrasApi.md#extrasImageAttachmentsCreate) | **POST** /extras/image-attachments/ | 
[**extrasImageAttachmentsDelete**](ExtrasApi.md#extrasImageAttachmentsDelete) | **DELETE** /extras/image-attachments/{id}/ | 
[**extrasImageAttachmentsList**](ExtrasApi.md#extrasImageAttachmentsList) | **GET** /extras/image-attachments/ | 
[**extrasImageAttachmentsPartialUpdate**](ExtrasApi.md#extrasImageAttachmentsPartialUpdate) | **PATCH** /extras/image-attachments/{id}/ | 
[**extrasImageAttachmentsRead**](ExtrasApi.md#extrasImageAttachmentsRead) | **GET** /extras/image-attachments/{id}/ | 
[**extrasImageAttachmentsUpdate**](ExtrasApi.md#extrasImageAttachmentsUpdate) | **PUT** /extras/image-attachments/{id}/ | 
[**extrasObjectChangesList**](ExtrasApi.md#extrasObjectChangesList) | **GET** /extras/object-changes/ | 
[**extrasObjectChangesRead**](ExtrasApi.md#extrasObjectChangesRead) | **GET** /extras/object-changes/{id}/ | 
[**extrasRecentActivityList**](ExtrasApi.md#extrasRecentActivityList) | **GET** /extras/recent-activity/ | 
[**extrasRecentActivityRead**](ExtrasApi.md#extrasRecentActivityRead) | **GET** /extras/recent-activity/{id}/ | 
[**extrasTagsCreate**](ExtrasApi.md#extrasTagsCreate) | **POST** /extras/tags/ | 
[**extrasTagsDelete**](ExtrasApi.md#extrasTagsDelete) | **DELETE** /extras/tags/{id}/ | 
[**extrasTagsList**](ExtrasApi.md#extrasTagsList) | **GET** /extras/tags/ | 
[**extrasTagsPartialUpdate**](ExtrasApi.md#extrasTagsPartialUpdate) | **PATCH** /extras/tags/{id}/ | 
[**extrasTagsRead**](ExtrasApi.md#extrasTagsRead) | **GET** /extras/tags/{id}/ | 
[**extrasTagsUpdate**](ExtrasApi.md#extrasTagsUpdate) | **PUT** /extras/tags/{id}/ | 
[**extrasTopologyMapsCreate**](ExtrasApi.md#extrasTopologyMapsCreate) | **POST** /extras/topology-maps/ | 
[**extrasTopologyMapsDelete**](ExtrasApi.md#extrasTopologyMapsDelete) | **DELETE** /extras/topology-maps/{id}/ | 
[**extrasTopologyMapsList**](ExtrasApi.md#extrasTopologyMapsList) | **GET** /extras/topology-maps/ | 
[**extrasTopologyMapsPartialUpdate**](ExtrasApi.md#extrasTopologyMapsPartialUpdate) | **PATCH** /extras/topology-maps/{id}/ | 
[**extrasTopologyMapsRead**](ExtrasApi.md#extrasTopologyMapsRead) | **GET** /extras/topology-maps/{id}/ | 
[**extrasTopologyMapsRender**](ExtrasApi.md#extrasTopologyMapsRender) | **GET** /extras/topology-maps/{id}/render/ | 
[**extrasTopologyMapsUpdate**](ExtrasApi.md#extrasTopologyMapsUpdate) | **PUT** /extras/topology-maps/{id}/ | 



## extrasChoicesList

> extrasChoicesList()





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.ExtrasApi();
apiInstance.extrasChoicesList((error, data, response) => {
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

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## extrasChoicesRead

> extrasChoicesRead(id)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.ExtrasApi();
let id = "id_example"; // String | 
apiInstance.extrasChoicesRead(id, (error, data, response) => {
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
 **id** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## extrasConfigContextsCreate

> ConfigContext extrasConfigContextsCreate(writableConfigContext)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.ExtrasApi();
let writableConfigContext = new NetBoxApi.WritableConfigContext(); // WritableConfigContext | 
apiInstance.extrasConfigContextsCreate(writableConfigContext, (error, data, response) => {
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
 **writableConfigContext** | [**WritableConfigContext**](WritableConfigContext.md)|  | 

### Return type

[**ConfigContext**](ConfigContext.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## extrasConfigContextsDelete

> extrasConfigContextsDelete(id)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.ExtrasApi();
let id = 56; // Number | A unique integer value identifying this config context.
apiInstance.extrasConfigContextsDelete(id, (error, data, response) => {
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
 **id** | **Number**| A unique integer value identifying this config context. | 

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## extrasConfigContextsList

> ExtrasConfigContextsList200Response extrasConfigContextsList(opts)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.ExtrasApi();
let opts = {
  'name': "name_example", // String | 
  'isActive': "isActive_example", // String | 
  'q': "q_example", // String | 
  'regionId': "regionId_example", // String | 
  'region': "region_example", // String | 
  'siteId': "siteId_example", // String | 
  'site': "site_example", // String | 
  'roleId': "roleId_example", // String | 
  'role': "role_example", // String | 
  'platformId': "platformId_example", // String | 
  'platform': "platform_example", // String | 
  'tenantGroupId': "tenantGroupId_example", // String | 
  'tenantGroup': "tenantGroup_example", // String | 
  'tenantId': "tenantId_example", // String | 
  'tenant': "tenant_example", // String | 
  'limit': 56, // Number | Number of results to return per page.
  'offset': 56 // Number | The initial index from which to return the results.
};
apiInstance.extrasConfigContextsList(opts, (error, data, response) => {
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
 **name** | **String**|  | [optional] 
 **isActive** | **String**|  | [optional] 
 **q** | **String**|  | [optional] 
 **regionId** | **String**|  | [optional] 
 **region** | **String**|  | [optional] 
 **siteId** | **String**|  | [optional] 
 **site** | **String**|  | [optional] 
 **roleId** | **String**|  | [optional] 
 **role** | **String**|  | [optional] 
 **platformId** | **String**|  | [optional] 
 **platform** | **String**|  | [optional] 
 **tenantGroupId** | **String**|  | [optional] 
 **tenantGroup** | **String**|  | [optional] 
 **tenantId** | **String**|  | [optional] 
 **tenant** | **String**|  | [optional] 
 **limit** | **Number**| Number of results to return per page. | [optional] 
 **offset** | **Number**| The initial index from which to return the results. | [optional] 

### Return type

[**ExtrasConfigContextsList200Response**](ExtrasConfigContextsList200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## extrasConfigContextsPartialUpdate

> ConfigContext extrasConfigContextsPartialUpdate(id, writableConfigContext)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.ExtrasApi();
let id = 56; // Number | A unique integer value identifying this config context.
let writableConfigContext = new NetBoxApi.WritableConfigContext(); // WritableConfigContext | 
apiInstance.extrasConfigContextsPartialUpdate(id, writableConfigContext, (error, data, response) => {
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
 **id** | **Number**| A unique integer value identifying this config context. | 
 **writableConfigContext** | [**WritableConfigContext**](WritableConfigContext.md)|  | 

### Return type

[**ConfigContext**](ConfigContext.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## extrasConfigContextsRead

> ConfigContext extrasConfigContextsRead(id)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.ExtrasApi();
let id = 56; // Number | A unique integer value identifying this config context.
apiInstance.extrasConfigContextsRead(id, (error, data, response) => {
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
 **id** | **Number**| A unique integer value identifying this config context. | 

### Return type

[**ConfigContext**](ConfigContext.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## extrasConfigContextsUpdate

> ConfigContext extrasConfigContextsUpdate(id, writableConfigContext)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.ExtrasApi();
let id = 56; // Number | A unique integer value identifying this config context.
let writableConfigContext = new NetBoxApi.WritableConfigContext(); // WritableConfigContext | 
apiInstance.extrasConfigContextsUpdate(id, writableConfigContext, (error, data, response) => {
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
 **id** | **Number**| A unique integer value identifying this config context. | 
 **writableConfigContext** | [**WritableConfigContext**](WritableConfigContext.md)|  | 

### Return type

[**ConfigContext**](ConfigContext.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## extrasExportTemplatesCreate

> ExportTemplate extrasExportTemplatesCreate(exportTemplate)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.ExtrasApi();
let exportTemplate = new NetBoxApi.ExportTemplate(); // ExportTemplate | 
apiInstance.extrasExportTemplatesCreate(exportTemplate, (error, data, response) => {
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
 **exportTemplate** | [**ExportTemplate**](ExportTemplate.md)|  | 

### Return type

[**ExportTemplate**](ExportTemplate.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## extrasExportTemplatesDelete

> extrasExportTemplatesDelete(id)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.ExtrasApi();
let id = 56; // Number | A unique integer value identifying this export template.
apiInstance.extrasExportTemplatesDelete(id, (error, data, response) => {
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
 **id** | **Number**| A unique integer value identifying this export template. | 

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## extrasExportTemplatesList

> ExtrasExportTemplatesList200Response extrasExportTemplatesList(opts)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.ExtrasApi();
let opts = {
  'contentType': "contentType_example", // String | 
  'name': "name_example", // String | 
  'limit': 56, // Number | Number of results to return per page.
  'offset': 56 // Number | The initial index from which to return the results.
};
apiInstance.extrasExportTemplatesList(opts, (error, data, response) => {
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
 **contentType** | **String**|  | [optional] 
 **name** | **String**|  | [optional] 
 **limit** | **Number**| Number of results to return per page. | [optional] 
 **offset** | **Number**| The initial index from which to return the results. | [optional] 

### Return type

[**ExtrasExportTemplatesList200Response**](ExtrasExportTemplatesList200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## extrasExportTemplatesPartialUpdate

> ExportTemplate extrasExportTemplatesPartialUpdate(id, exportTemplate)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.ExtrasApi();
let id = 56; // Number | A unique integer value identifying this export template.
let exportTemplate = new NetBoxApi.ExportTemplate(); // ExportTemplate | 
apiInstance.extrasExportTemplatesPartialUpdate(id, exportTemplate, (error, data, response) => {
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
 **id** | **Number**| A unique integer value identifying this export template. | 
 **exportTemplate** | [**ExportTemplate**](ExportTemplate.md)|  | 

### Return type

[**ExportTemplate**](ExportTemplate.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## extrasExportTemplatesRead

> ExportTemplate extrasExportTemplatesRead(id)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.ExtrasApi();
let id = 56; // Number | A unique integer value identifying this export template.
apiInstance.extrasExportTemplatesRead(id, (error, data, response) => {
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
 **id** | **Number**| A unique integer value identifying this export template. | 

### Return type

[**ExportTemplate**](ExportTemplate.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## extrasExportTemplatesUpdate

> ExportTemplate extrasExportTemplatesUpdate(id, exportTemplate)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.ExtrasApi();
let id = 56; // Number | A unique integer value identifying this export template.
let exportTemplate = new NetBoxApi.ExportTemplate(); // ExportTemplate | 
apiInstance.extrasExportTemplatesUpdate(id, exportTemplate, (error, data, response) => {
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
 **id** | **Number**| A unique integer value identifying this export template. | 
 **exportTemplate** | [**ExportTemplate**](ExportTemplate.md)|  | 

### Return type

[**ExportTemplate**](ExportTemplate.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## extrasGraphsCreate

> Graph extrasGraphsCreate(writableGraph)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.ExtrasApi();
let writableGraph = new NetBoxApi.WritableGraph(); // WritableGraph | 
apiInstance.extrasGraphsCreate(writableGraph, (error, data, response) => {
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
 **writableGraph** | [**WritableGraph**](WritableGraph.md)|  | 

### Return type

[**Graph**](Graph.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## extrasGraphsDelete

> extrasGraphsDelete(id)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.ExtrasApi();
let id = 56; // Number | A unique integer value identifying this graph.
apiInstance.extrasGraphsDelete(id, (error, data, response) => {
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
 **id** | **Number**| A unique integer value identifying this graph. | 

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## extrasGraphsList

> ExtrasGraphsList200Response extrasGraphsList(opts)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.ExtrasApi();
let opts = {
  'type': "type_example", // String | 
  'name': "name_example", // String | 
  'limit': 56, // Number | Number of results to return per page.
  'offset': 56 // Number | The initial index from which to return the results.
};
apiInstance.extrasGraphsList(opts, (error, data, response) => {
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
 **type** | **String**|  | [optional] 
 **name** | **String**|  | [optional] 
 **limit** | **Number**| Number of results to return per page. | [optional] 
 **offset** | **Number**| The initial index from which to return the results. | [optional] 

### Return type

[**ExtrasGraphsList200Response**](ExtrasGraphsList200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## extrasGraphsPartialUpdate

> Graph extrasGraphsPartialUpdate(id, writableGraph)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.ExtrasApi();
let id = 56; // Number | A unique integer value identifying this graph.
let writableGraph = new NetBoxApi.WritableGraph(); // WritableGraph | 
apiInstance.extrasGraphsPartialUpdate(id, writableGraph, (error, data, response) => {
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
 **id** | **Number**| A unique integer value identifying this graph. | 
 **writableGraph** | [**WritableGraph**](WritableGraph.md)|  | 

### Return type

[**Graph**](Graph.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## extrasGraphsRead

> Graph extrasGraphsRead(id)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.ExtrasApi();
let id = 56; // Number | A unique integer value identifying this graph.
apiInstance.extrasGraphsRead(id, (error, data, response) => {
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
 **id** | **Number**| A unique integer value identifying this graph. | 

### Return type

[**Graph**](Graph.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## extrasGraphsUpdate

> Graph extrasGraphsUpdate(id, writableGraph)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.ExtrasApi();
let id = 56; // Number | A unique integer value identifying this graph.
let writableGraph = new NetBoxApi.WritableGraph(); // WritableGraph | 
apiInstance.extrasGraphsUpdate(id, writableGraph, (error, data, response) => {
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
 **id** | **Number**| A unique integer value identifying this graph. | 
 **writableGraph** | [**WritableGraph**](WritableGraph.md)|  | 

### Return type

[**Graph**](Graph.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## extrasImageAttachmentsCreate

> ImageAttachment extrasImageAttachmentsCreate(imageAttachment)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.ExtrasApi();
let imageAttachment = new NetBoxApi.ImageAttachment(); // ImageAttachment | 
apiInstance.extrasImageAttachmentsCreate(imageAttachment, (error, data, response) => {
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
 **imageAttachment** | [**ImageAttachment**](ImageAttachment.md)|  | 

### Return type

[**ImageAttachment**](ImageAttachment.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## extrasImageAttachmentsDelete

> extrasImageAttachmentsDelete(id)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.ExtrasApi();
let id = 56; // Number | A unique integer value identifying this image attachment.
apiInstance.extrasImageAttachmentsDelete(id, (error, data, response) => {
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
 **id** | **Number**| A unique integer value identifying this image attachment. | 

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## extrasImageAttachmentsList

> ExtrasImageAttachmentsList200Response extrasImageAttachmentsList(opts)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.ExtrasApi();
let opts = {
  'limit': 56, // Number | Number of results to return per page.
  'offset': 56 // Number | The initial index from which to return the results.
};
apiInstance.extrasImageAttachmentsList(opts, (error, data, response) => {
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
 **limit** | **Number**| Number of results to return per page. | [optional] 
 **offset** | **Number**| The initial index from which to return the results. | [optional] 

### Return type

[**ExtrasImageAttachmentsList200Response**](ExtrasImageAttachmentsList200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## extrasImageAttachmentsPartialUpdate

> ImageAttachment extrasImageAttachmentsPartialUpdate(id, imageAttachment)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.ExtrasApi();
let id = 56; // Number | A unique integer value identifying this image attachment.
let imageAttachment = new NetBoxApi.ImageAttachment(); // ImageAttachment | 
apiInstance.extrasImageAttachmentsPartialUpdate(id, imageAttachment, (error, data, response) => {
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
 **id** | **Number**| A unique integer value identifying this image attachment. | 
 **imageAttachment** | [**ImageAttachment**](ImageAttachment.md)|  | 

### Return type

[**ImageAttachment**](ImageAttachment.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## extrasImageAttachmentsRead

> ImageAttachment extrasImageAttachmentsRead(id)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.ExtrasApi();
let id = 56; // Number | A unique integer value identifying this image attachment.
apiInstance.extrasImageAttachmentsRead(id, (error, data, response) => {
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
 **id** | **Number**| A unique integer value identifying this image attachment. | 

### Return type

[**ImageAttachment**](ImageAttachment.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## extrasImageAttachmentsUpdate

> ImageAttachment extrasImageAttachmentsUpdate(id, imageAttachment)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.ExtrasApi();
let id = 56; // Number | A unique integer value identifying this image attachment.
let imageAttachment = new NetBoxApi.ImageAttachment(); // ImageAttachment | 
apiInstance.extrasImageAttachmentsUpdate(id, imageAttachment, (error, data, response) => {
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
 **id** | **Number**| A unique integer value identifying this image attachment. | 
 **imageAttachment** | [**ImageAttachment**](ImageAttachment.md)|  | 

### Return type

[**ImageAttachment**](ImageAttachment.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## extrasObjectChangesList

> ExtrasObjectChangesList200Response extrasObjectChangesList(opts)



Retrieve a list of recent changes.

### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.ExtrasApi();
let opts = {
  'user': "user_example", // String | 
  'userName': "userName_example", // String | 
  'requestId': "requestId_example", // String | 
  'action': "action_example", // String | 
  'changedObjectType': "changedObjectType_example", // String | 
  'objectRepr': "objectRepr_example", // String | 
  'q': "q_example", // String | 
  'time': "time_example", // String | 
  'limit': 56, // Number | Number of results to return per page.
  'offset': 56 // Number | The initial index from which to return the results.
};
apiInstance.extrasObjectChangesList(opts, (error, data, response) => {
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
 **user** | **String**|  | [optional] 
 **userName** | **String**|  | [optional] 
 **requestId** | **String**|  | [optional] 
 **action** | **String**|  | [optional] 
 **changedObjectType** | **String**|  | [optional] 
 **objectRepr** | **String**|  | [optional] 
 **q** | **String**|  | [optional] 
 **time** | **String**|  | [optional] 
 **limit** | **Number**| Number of results to return per page. | [optional] 
 **offset** | **Number**| The initial index from which to return the results. | [optional] 

### Return type

[**ExtrasObjectChangesList200Response**](ExtrasObjectChangesList200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## extrasObjectChangesRead

> ObjectChange extrasObjectChangesRead(id)



Retrieve a list of recent changes.

### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.ExtrasApi();
let id = 56; // Number | A unique integer value identifying this object change.
apiInstance.extrasObjectChangesRead(id, (error, data, response) => {
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
 **id** | **Number**| A unique integer value identifying this object change. | 

### Return type

[**ObjectChange**](ObjectChange.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## extrasRecentActivityList

> ExtrasRecentActivityList200Response extrasRecentActivityList(opts)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.ExtrasApi();
let opts = {
  'user': "user_example", // String | 
  'username': "username_example", // String | 
  'limit': 56, // Number | Number of results to return per page.
  'offset': 56 // Number | The initial index from which to return the results.
};
apiInstance.extrasRecentActivityList(opts, (error, data, response) => {
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
 **user** | **String**|  | [optional] 
 **username** | **String**|  | [optional] 
 **limit** | **Number**| Number of results to return per page. | [optional] 
 **offset** | **Number**| The initial index from which to return the results. | [optional] 

### Return type

[**ExtrasRecentActivityList200Response**](ExtrasRecentActivityList200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## extrasRecentActivityRead

> UserAction extrasRecentActivityRead(id)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.ExtrasApi();
let id = 56; // Number | A unique integer value identifying this user action.
apiInstance.extrasRecentActivityRead(id, (error, data, response) => {
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
 **id** | **Number**| A unique integer value identifying this user action. | 

### Return type

[**UserAction**](UserAction.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## extrasTagsCreate

> Tag extrasTagsCreate(tag)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.ExtrasApi();
let tag = new NetBoxApi.Tag(); // Tag | 
apiInstance.extrasTagsCreate(tag, (error, data, response) => {
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
 **tag** | [**Tag**](Tag.md)|  | 

### Return type

[**Tag**](Tag.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## extrasTagsDelete

> extrasTagsDelete(id)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.ExtrasApi();
let id = 56; // Number | A unique integer value identifying this Tag.
apiInstance.extrasTagsDelete(id, (error, data, response) => {
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
 **id** | **Number**| A unique integer value identifying this Tag. | 

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## extrasTagsList

> ExtrasTagsList200Response extrasTagsList(opts)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.ExtrasApi();
let opts = {
  'name': "name_example", // String | 
  'slug': "slug_example", // String | 
  'q': "q_example", // String | 
  'limit': 56, // Number | Number of results to return per page.
  'offset': 56 // Number | The initial index from which to return the results.
};
apiInstance.extrasTagsList(opts, (error, data, response) => {
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
 **name** | **String**|  | [optional] 
 **slug** | **String**|  | [optional] 
 **q** | **String**|  | [optional] 
 **limit** | **Number**| Number of results to return per page. | [optional] 
 **offset** | **Number**| The initial index from which to return the results. | [optional] 

### Return type

[**ExtrasTagsList200Response**](ExtrasTagsList200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## extrasTagsPartialUpdate

> Tag extrasTagsPartialUpdate(id, tag)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.ExtrasApi();
let id = 56; // Number | A unique integer value identifying this Tag.
let tag = new NetBoxApi.Tag(); // Tag | 
apiInstance.extrasTagsPartialUpdate(id, tag, (error, data, response) => {
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
 **id** | **Number**| A unique integer value identifying this Tag. | 
 **tag** | [**Tag**](Tag.md)|  | 

### Return type

[**Tag**](Tag.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## extrasTagsRead

> Tag extrasTagsRead(id)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.ExtrasApi();
let id = 56; // Number | A unique integer value identifying this Tag.
apiInstance.extrasTagsRead(id, (error, data, response) => {
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
 **id** | **Number**| A unique integer value identifying this Tag. | 

### Return type

[**Tag**](Tag.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## extrasTagsUpdate

> Tag extrasTagsUpdate(id, tag)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.ExtrasApi();
let id = 56; // Number | A unique integer value identifying this Tag.
let tag = new NetBoxApi.Tag(); // Tag | 
apiInstance.extrasTagsUpdate(id, tag, (error, data, response) => {
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
 **id** | **Number**| A unique integer value identifying this Tag. | 
 **tag** | [**Tag**](Tag.md)|  | 

### Return type

[**Tag**](Tag.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## extrasTopologyMapsCreate

> TopologyMap extrasTopologyMapsCreate(writableTopologyMap)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.ExtrasApi();
let writableTopologyMap = new NetBoxApi.WritableTopologyMap(); // WritableTopologyMap | 
apiInstance.extrasTopologyMapsCreate(writableTopologyMap, (error, data, response) => {
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
 **writableTopologyMap** | [**WritableTopologyMap**](WritableTopologyMap.md)|  | 

### Return type

[**TopologyMap**](TopologyMap.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## extrasTopologyMapsDelete

> extrasTopologyMapsDelete(id)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.ExtrasApi();
let id = 56; // Number | A unique integer value identifying this topology map.
apiInstance.extrasTopologyMapsDelete(id, (error, data, response) => {
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
 **id** | **Number**| A unique integer value identifying this topology map. | 

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## extrasTopologyMapsList

> ExtrasTopologyMapsList200Response extrasTopologyMapsList(opts)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.ExtrasApi();
let opts = {
  'name': "name_example", // String | 
  'slug': "slug_example", // String | 
  'siteId': "siteId_example", // String | 
  'site': "site_example", // String | 
  'limit': 56, // Number | Number of results to return per page.
  'offset': 56 // Number | The initial index from which to return the results.
};
apiInstance.extrasTopologyMapsList(opts, (error, data, response) => {
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
 **name** | **String**|  | [optional] 
 **slug** | **String**|  | [optional] 
 **siteId** | **String**|  | [optional] 
 **site** | **String**|  | [optional] 
 **limit** | **Number**| Number of results to return per page. | [optional] 
 **offset** | **Number**| The initial index from which to return the results. | [optional] 

### Return type

[**ExtrasTopologyMapsList200Response**](ExtrasTopologyMapsList200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## extrasTopologyMapsPartialUpdate

> TopologyMap extrasTopologyMapsPartialUpdate(id, writableTopologyMap)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.ExtrasApi();
let id = 56; // Number | A unique integer value identifying this topology map.
let writableTopologyMap = new NetBoxApi.WritableTopologyMap(); // WritableTopologyMap | 
apiInstance.extrasTopologyMapsPartialUpdate(id, writableTopologyMap, (error, data, response) => {
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
 **id** | **Number**| A unique integer value identifying this topology map. | 
 **writableTopologyMap** | [**WritableTopologyMap**](WritableTopologyMap.md)|  | 

### Return type

[**TopologyMap**](TopologyMap.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## extrasTopologyMapsRead

> TopologyMap extrasTopologyMapsRead(id)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.ExtrasApi();
let id = 56; // Number | A unique integer value identifying this topology map.
apiInstance.extrasTopologyMapsRead(id, (error, data, response) => {
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
 **id** | **Number**| A unique integer value identifying this topology map. | 

### Return type

[**TopologyMap**](TopologyMap.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## extrasTopologyMapsRender

> TopologyMap extrasTopologyMapsRender(id)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.ExtrasApi();
let id = 56; // Number | A unique integer value identifying this topology map.
apiInstance.extrasTopologyMapsRender(id, (error, data, response) => {
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
 **id** | **Number**| A unique integer value identifying this topology map. | 

### Return type

[**TopologyMap**](TopologyMap.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## extrasTopologyMapsUpdate

> TopologyMap extrasTopologyMapsUpdate(id, writableTopologyMap)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.ExtrasApi();
let id = 56; // Number | A unique integer value identifying this topology map.
let writableTopologyMap = new NetBoxApi.WritableTopologyMap(); // WritableTopologyMap | 
apiInstance.extrasTopologyMapsUpdate(id, writableTopologyMap, (error, data, response) => {
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
 **id** | **Number**| A unique integer value identifying this topology map. | 
 **writableTopologyMap** | [**WritableTopologyMap**](WritableTopologyMap.md)|  | 

### Return type

[**TopologyMap**](TopologyMap.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

