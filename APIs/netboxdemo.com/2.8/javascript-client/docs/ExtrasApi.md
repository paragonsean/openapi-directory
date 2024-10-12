# NetBoxApi.ExtrasApi

All URIs are relative to *https://netboxdemo.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**extrasConfigContextsCreate**](ExtrasApi.md#extrasConfigContextsCreate) | **POST** /extras/config-contexts/ | 
[**extrasConfigContextsDelete**](ExtrasApi.md#extrasConfigContextsDelete) | **DELETE** /extras/config-contexts/{id}/ | 
[**extrasConfigContextsList**](ExtrasApi.md#extrasConfigContextsList) | **GET** /extras/config-contexts/ | 
[**extrasConfigContextsPartialUpdate**](ExtrasApi.md#extrasConfigContextsPartialUpdate) | **PATCH** /extras/config-contexts/{id}/ | 
[**extrasConfigContextsRead**](ExtrasApi.md#extrasConfigContextsRead) | **GET** /extras/config-contexts/{id}/ | 
[**extrasConfigContextsUpdate**](ExtrasApi.md#extrasConfigContextsUpdate) | **PUT** /extras/config-contexts/{id}/ | 
[**extrasCustomFieldChoicesList**](ExtrasApi.md#extrasCustomFieldChoicesList) | **GET** /extras/_custom_field_choices/ | 
[**extrasCustomFieldChoicesRead**](ExtrasApi.md#extrasCustomFieldChoicesRead) | **GET** /extras/_custom_field_choices/{id}/ | 
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
[**extrasReportsList**](ExtrasApi.md#extrasReportsList) | **GET** /extras/reports/ | 
[**extrasReportsRead**](ExtrasApi.md#extrasReportsRead) | **GET** /extras/reports/{id}/ | 
[**extrasReportsRun**](ExtrasApi.md#extrasReportsRun) | **POST** /extras/reports/{id}/run/ | 
[**extrasScriptsList**](ExtrasApi.md#extrasScriptsList) | **GET** /extras/scripts/ | 
[**extrasScriptsRead**](ExtrasApi.md#extrasScriptsRead) | **GET** /extras/scripts/{id}/ | 
[**extrasTagsCreate**](ExtrasApi.md#extrasTagsCreate) | **POST** /extras/tags/ | 
[**extrasTagsDelete**](ExtrasApi.md#extrasTagsDelete) | **DELETE** /extras/tags/{id}/ | 
[**extrasTagsList**](ExtrasApi.md#extrasTagsList) | **GET** /extras/tags/ | 
[**extrasTagsPartialUpdate**](ExtrasApi.md#extrasTagsPartialUpdate) | **PATCH** /extras/tags/{id}/ | 
[**extrasTagsRead**](ExtrasApi.md#extrasTagsRead) | **GET** /extras/tags/{id}/ | 
[**extrasTagsUpdate**](ExtrasApi.md#extrasTagsUpdate) | **PUT** /extras/tags/{id}/ | 



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



Call to super to allow for caching

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
  'id': "id_example", // String | 
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
  'clusterGroupId': "clusterGroupId_example", // String | 
  'clusterGroup': "clusterGroup_example", // String | 
  'clusterId': "clusterId_example", // String | 
  'tenantGroupId': "tenantGroupId_example", // String | 
  'tenantGroup': "tenantGroup_example", // String | 
  'tenantId': "tenantId_example", // String | 
  'tenant': "tenant_example", // String | 
  'tag': "tag_example", // String | 
  'idN': "idN_example", // String | 
  'idLte': "idLte_example", // String | 
  'idLt': "idLt_example", // String | 
  'idGte': "idGte_example", // String | 
  'idGt': "idGt_example", // String | 
  'nameN': "nameN_example", // String | 
  'nameIc': "nameIc_example", // String | 
  'nameNic': "nameNic_example", // String | 
  'nameIew': "nameIew_example", // String | 
  'nameNiew': "nameNiew_example", // String | 
  'nameIsw': "nameIsw_example", // String | 
  'nameNisw': "nameNisw_example", // String | 
  'nameIe': "nameIe_example", // String | 
  'nameNie': "nameNie_example", // String | 
  'regionIdN': "regionIdN_example", // String | 
  'regionN': "regionN_example", // String | 
  'siteIdN': "siteIdN_example", // String | 
  'siteN': "siteN_example", // String | 
  'roleIdN': "roleIdN_example", // String | 
  'roleN': "roleN_example", // String | 
  'platformIdN': "platformIdN_example", // String | 
  'platformN': "platformN_example", // String | 
  'clusterGroupIdN': "clusterGroupIdN_example", // String | 
  'clusterGroupN': "clusterGroupN_example", // String | 
  'clusterIdN': "clusterIdN_example", // String | 
  'tenantGroupIdN': "tenantGroupIdN_example", // String | 
  'tenantGroupN': "tenantGroupN_example", // String | 
  'tenantIdN': "tenantIdN_example", // String | 
  'tenantN': "tenantN_example", // String | 
  'tagN': "tagN_example", // String | 
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
 **id** | **String**|  | [optional] 
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
 **clusterGroupId** | **String**|  | [optional] 
 **clusterGroup** | **String**|  | [optional] 
 **clusterId** | **String**|  | [optional] 
 **tenantGroupId** | **String**|  | [optional] 
 **tenantGroup** | **String**|  | [optional] 
 **tenantId** | **String**|  | [optional] 
 **tenant** | **String**|  | [optional] 
 **tag** | **String**|  | [optional] 
 **idN** | **String**|  | [optional] 
 **idLte** | **String**|  | [optional] 
 **idLt** | **String**|  | [optional] 
 **idGte** | **String**|  | [optional] 
 **idGt** | **String**|  | [optional] 
 **nameN** | **String**|  | [optional] 
 **nameIc** | **String**|  | [optional] 
 **nameNic** | **String**|  | [optional] 
 **nameIew** | **String**|  | [optional] 
 **nameNiew** | **String**|  | [optional] 
 **nameIsw** | **String**|  | [optional] 
 **nameNisw** | **String**|  | [optional] 
 **nameIe** | **String**|  | [optional] 
 **nameNie** | **String**|  | [optional] 
 **regionIdN** | **String**|  | [optional] 
 **regionN** | **String**|  | [optional] 
 **siteIdN** | **String**|  | [optional] 
 **siteN** | **String**|  | [optional] 
 **roleIdN** | **String**|  | [optional] 
 **roleN** | **String**|  | [optional] 
 **platformIdN** | **String**|  | [optional] 
 **platformN** | **String**|  | [optional] 
 **clusterGroupIdN** | **String**|  | [optional] 
 **clusterGroupN** | **String**|  | [optional] 
 **clusterIdN** | **String**|  | [optional] 
 **tenantGroupIdN** | **String**|  | [optional] 
 **tenantGroupN** | **String**|  | [optional] 
 **tenantIdN** | **String**|  | [optional] 
 **tenantN** | **String**|  | [optional] 
 **tagN** | **String**|  | [optional] 
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



Call to super to allow for caching

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


## extrasCustomFieldChoicesList

> extrasCustomFieldChoicesList()





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
apiInstance.extrasCustomFieldChoicesList((error, data, response) => {
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


## extrasCustomFieldChoicesRead

> extrasCustomFieldChoicesRead(id)





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
apiInstance.extrasCustomFieldChoicesRead(id, (error, data, response) => {
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


## extrasExportTemplatesCreate

> ExportTemplate extrasExportTemplatesCreate(writableExportTemplate)





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
let writableExportTemplate = new NetBoxApi.WritableExportTemplate(); // WritableExportTemplate | 
apiInstance.extrasExportTemplatesCreate(writableExportTemplate, (error, data, response) => {
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
 **writableExportTemplate** | [**WritableExportTemplate**](WritableExportTemplate.md)|  | 

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



Call to super to allow for caching

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
  'id': "id_example", // String | 
  'contentType': "contentType_example", // String | 
  'name': "name_example", // String | 
  'templateLanguage': "templateLanguage_example", // String | 
  'idN': "idN_example", // String | 
  'idLte': "idLte_example", // String | 
  'idLt': "idLt_example", // String | 
  'idGte': "idGte_example", // String | 
  'idGt': "idGt_example", // String | 
  'contentTypeN': "contentTypeN_example", // String | 
  'nameN': "nameN_example", // String | 
  'nameIc': "nameIc_example", // String | 
  'nameNic': "nameNic_example", // String | 
  'nameIew': "nameIew_example", // String | 
  'nameNiew': "nameNiew_example", // String | 
  'nameIsw': "nameIsw_example", // String | 
  'nameNisw': "nameNisw_example", // String | 
  'nameIe': "nameIe_example", // String | 
  'nameNie': "nameNie_example", // String | 
  'templateLanguageN': "templateLanguageN_example", // String | 
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
 **id** | **String**|  | [optional] 
 **contentType** | **String**|  | [optional] 
 **name** | **String**|  | [optional] 
 **templateLanguage** | **String**|  | [optional] 
 **idN** | **String**|  | [optional] 
 **idLte** | **String**|  | [optional] 
 **idLt** | **String**|  | [optional] 
 **idGte** | **String**|  | [optional] 
 **idGt** | **String**|  | [optional] 
 **contentTypeN** | **String**|  | [optional] 
 **nameN** | **String**|  | [optional] 
 **nameIc** | **String**|  | [optional] 
 **nameNic** | **String**|  | [optional] 
 **nameIew** | **String**|  | [optional] 
 **nameNiew** | **String**|  | [optional] 
 **nameIsw** | **String**|  | [optional] 
 **nameNisw** | **String**|  | [optional] 
 **nameIe** | **String**|  | [optional] 
 **nameNie** | **String**|  | [optional] 
 **templateLanguageN** | **String**|  | [optional] 
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

> ExportTemplate extrasExportTemplatesPartialUpdate(id, writableExportTemplate)





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
let writableExportTemplate = new NetBoxApi.WritableExportTemplate(); // WritableExportTemplate | 
apiInstance.extrasExportTemplatesPartialUpdate(id, writableExportTemplate, (error, data, response) => {
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
 **writableExportTemplate** | [**WritableExportTemplate**](WritableExportTemplate.md)|  | 

### Return type

[**ExportTemplate**](ExportTemplate.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## extrasExportTemplatesRead

> ExportTemplate extrasExportTemplatesRead(id)



Call to super to allow for caching

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

> ExportTemplate extrasExportTemplatesUpdate(id, writableExportTemplate)





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
let writableExportTemplate = new NetBoxApi.WritableExportTemplate(); // WritableExportTemplate | 
apiInstance.extrasExportTemplatesUpdate(id, writableExportTemplate, (error, data, response) => {
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
 **writableExportTemplate** | [**WritableExportTemplate**](WritableExportTemplate.md)|  | 

### Return type

[**ExportTemplate**](ExportTemplate.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## extrasGraphsCreate

> Graph extrasGraphsCreate(graph)





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
let graph = new NetBoxApi.Graph(); // Graph | 
apiInstance.extrasGraphsCreate(graph, (error, data, response) => {
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
 **graph** | [**Graph**](Graph.md)|  | 

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



Call to super to allow for caching

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
  'id': "id_example", // String | 
  'type': "type_example", // String | 
  'name': "name_example", // String | 
  'templateLanguage': "templateLanguage_example", // String | 
  'idN': "idN_example", // String | 
  'idLte': "idLte_example", // String | 
  'idLt': "idLt_example", // String | 
  'idGte': "idGte_example", // String | 
  'idGt': "idGt_example", // String | 
  'typeN': "typeN_example", // String | 
  'nameN': "nameN_example", // String | 
  'nameIc': "nameIc_example", // String | 
  'nameNic': "nameNic_example", // String | 
  'nameIew': "nameIew_example", // String | 
  'nameNiew': "nameNiew_example", // String | 
  'nameIsw': "nameIsw_example", // String | 
  'nameNisw': "nameNisw_example", // String | 
  'nameIe': "nameIe_example", // String | 
  'nameNie': "nameNie_example", // String | 
  'templateLanguageN': "templateLanguageN_example", // String | 
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
 **id** | **String**|  | [optional] 
 **type** | **String**|  | [optional] 
 **name** | **String**|  | [optional] 
 **templateLanguage** | **String**|  | [optional] 
 **idN** | **String**|  | [optional] 
 **idLte** | **String**|  | [optional] 
 **idLt** | **String**|  | [optional] 
 **idGte** | **String**|  | [optional] 
 **idGt** | **String**|  | [optional] 
 **typeN** | **String**|  | [optional] 
 **nameN** | **String**|  | [optional] 
 **nameIc** | **String**|  | [optional] 
 **nameNic** | **String**|  | [optional] 
 **nameIew** | **String**|  | [optional] 
 **nameNiew** | **String**|  | [optional] 
 **nameIsw** | **String**|  | [optional] 
 **nameNisw** | **String**|  | [optional] 
 **nameIe** | **String**|  | [optional] 
 **nameNie** | **String**|  | [optional] 
 **templateLanguageN** | **String**|  | [optional] 
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

> Graph extrasGraphsPartialUpdate(id, graph)





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
let graph = new NetBoxApi.Graph(); // Graph | 
apiInstance.extrasGraphsPartialUpdate(id, graph, (error, data, response) => {
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
 **graph** | [**Graph**](Graph.md)|  | 

### Return type

[**Graph**](Graph.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## extrasGraphsRead

> Graph extrasGraphsRead(id)



Call to super to allow for caching

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

> Graph extrasGraphsUpdate(id, graph)





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
let graph = new NetBoxApi.Graph(); // Graph | 
apiInstance.extrasGraphsUpdate(id, graph, (error, data, response) => {
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
 **graph** | [**Graph**](Graph.md)|  | 

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



Call to super to allow for caching

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



Call to super to allow for caching

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
  'id': "id_example", // String | 
  'user': "user_example", // String | 
  'userName': "userName_example", // String | 
  'requestId': "requestId_example", // String | 
  'action': "action_example", // String | 
  'changedObjectType': "changedObjectType_example", // String | 
  'changedObjectId': "changedObjectId_example", // String | 
  'objectRepr': "objectRepr_example", // String | 
  'q': "q_example", // String | 
  'time': "time_example", // String | 
  'idN': "idN_example", // String | 
  'idLte': "idLte_example", // String | 
  'idLt': "idLt_example", // String | 
  'idGte': "idGte_example", // String | 
  'idGt': "idGt_example", // String | 
  'userN': "userN_example", // String | 
  'userNameN': "userNameN_example", // String | 
  'userNameIc': "userNameIc_example", // String | 
  'userNameNic': "userNameNic_example", // String | 
  'userNameIew': "userNameIew_example", // String | 
  'userNameNiew': "userNameNiew_example", // String | 
  'userNameIsw': "userNameIsw_example", // String | 
  'userNameNisw': "userNameNisw_example", // String | 
  'userNameIe': "userNameIe_example", // String | 
  'userNameNie': "userNameNie_example", // String | 
  'actionN': "actionN_example", // String | 
  'changedObjectTypeN': "changedObjectTypeN_example", // String | 
  'changedObjectIdN': "changedObjectIdN_example", // String | 
  'changedObjectIdLte': "changedObjectIdLte_example", // String | 
  'changedObjectIdLt': "changedObjectIdLt_example", // String | 
  'changedObjectIdGte': "changedObjectIdGte_example", // String | 
  'changedObjectIdGt': "changedObjectIdGt_example", // String | 
  'objectReprN': "objectReprN_example", // String | 
  'objectReprIc': "objectReprIc_example", // String | 
  'objectReprNic': "objectReprNic_example", // String | 
  'objectReprIew': "objectReprIew_example", // String | 
  'objectReprNiew': "objectReprNiew_example", // String | 
  'objectReprIsw': "objectReprIsw_example", // String | 
  'objectReprNisw': "objectReprNisw_example", // String | 
  'objectReprIe': "objectReprIe_example", // String | 
  'objectReprNie': "objectReprNie_example", // String | 
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
 **id** | **String**|  | [optional] 
 **user** | **String**|  | [optional] 
 **userName** | **String**|  | [optional] 
 **requestId** | **String**|  | [optional] 
 **action** | **String**|  | [optional] 
 **changedObjectType** | **String**|  | [optional] 
 **changedObjectId** | **String**|  | [optional] 
 **objectRepr** | **String**|  | [optional] 
 **q** | **String**|  | [optional] 
 **time** | **String**|  | [optional] 
 **idN** | **String**|  | [optional] 
 **idLte** | **String**|  | [optional] 
 **idLt** | **String**|  | [optional] 
 **idGte** | **String**|  | [optional] 
 **idGt** | **String**|  | [optional] 
 **userN** | **String**|  | [optional] 
 **userNameN** | **String**|  | [optional] 
 **userNameIc** | **String**|  | [optional] 
 **userNameNic** | **String**|  | [optional] 
 **userNameIew** | **String**|  | [optional] 
 **userNameNiew** | **String**|  | [optional] 
 **userNameIsw** | **String**|  | [optional] 
 **userNameNisw** | **String**|  | [optional] 
 **userNameIe** | **String**|  | [optional] 
 **userNameNie** | **String**|  | [optional] 
 **actionN** | **String**|  | [optional] 
 **changedObjectTypeN** | **String**|  | [optional] 
 **changedObjectIdN** | **String**|  | [optional] 
 **changedObjectIdLte** | **String**|  | [optional] 
 **changedObjectIdLt** | **String**|  | [optional] 
 **changedObjectIdGte** | **String**|  | [optional] 
 **changedObjectIdGt** | **String**|  | [optional] 
 **objectReprN** | **String**|  | [optional] 
 **objectReprIc** | **String**|  | [optional] 
 **objectReprNic** | **String**|  | [optional] 
 **objectReprIew** | **String**|  | [optional] 
 **objectReprNiew** | **String**|  | [optional] 
 **objectReprIsw** | **String**|  | [optional] 
 **objectReprNisw** | **String**|  | [optional] 
 **objectReprIe** | **String**|  | [optional] 
 **objectReprNie** | **String**|  | [optional] 
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


## extrasReportsList

> extrasReportsList()



Compile all reports and their related results (if any). Result data is deferred in the list view.

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
apiInstance.extrasReportsList((error, data, response) => {
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


## extrasReportsRead

> extrasReportsRead(id)



Retrieve a single Report identified as \&quot;&lt;module&gt;.&lt;report&gt;\&quot;.

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
apiInstance.extrasReportsRead(id, (error, data, response) => {
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


## extrasReportsRun

> extrasReportsRun(id)



Run a Report and create a new ReportResult, overwriting any previous result for the Report.

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
apiInstance.extrasReportsRun(id, (error, data, response) => {
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


## extrasScriptsList

> extrasScriptsList()





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
apiInstance.extrasScriptsList((error, data, response) => {
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


## extrasScriptsRead

> extrasScriptsRead(id)





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
apiInstance.extrasScriptsRead(id, (error, data, response) => {
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
let id = 56; // Number | A unique integer value identifying this tag.
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
 **id** | **Number**| A unique integer value identifying this tag. | 

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## extrasTagsList

> ExtrasTagsList200Response extrasTagsList(opts)



Call to super to allow for caching

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
  'id': "id_example", // String | 
  'name': "name_example", // String | 
  'slug': "slug_example", // String | 
  'color': "color_example", // String | 
  'q': "q_example", // String | 
  'idN': "idN_example", // String | 
  'idLte': "idLte_example", // String | 
  'idLt': "idLt_example", // String | 
  'idGte': "idGte_example", // String | 
  'idGt': "idGt_example", // String | 
  'nameN': "nameN_example", // String | 
  'nameIc': "nameIc_example", // String | 
  'nameNic': "nameNic_example", // String | 
  'nameIew': "nameIew_example", // String | 
  'nameNiew': "nameNiew_example", // String | 
  'nameIsw': "nameIsw_example", // String | 
  'nameNisw': "nameNisw_example", // String | 
  'nameIe': "nameIe_example", // String | 
  'nameNie': "nameNie_example", // String | 
  'slugN': "slugN_example", // String | 
  'slugIc': "slugIc_example", // String | 
  'slugNic': "slugNic_example", // String | 
  'slugIew': "slugIew_example", // String | 
  'slugNiew': "slugNiew_example", // String | 
  'slugIsw': "slugIsw_example", // String | 
  'slugNisw': "slugNisw_example", // String | 
  'slugIe': "slugIe_example", // String | 
  'slugNie': "slugNie_example", // String | 
  'colorN': "colorN_example", // String | 
  'colorIc': "colorIc_example", // String | 
  'colorNic': "colorNic_example", // String | 
  'colorIew': "colorIew_example", // String | 
  'colorNiew': "colorNiew_example", // String | 
  'colorIsw': "colorIsw_example", // String | 
  'colorNisw': "colorNisw_example", // String | 
  'colorIe': "colorIe_example", // String | 
  'colorNie': "colorNie_example", // String | 
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
 **id** | **String**|  | [optional] 
 **name** | **String**|  | [optional] 
 **slug** | **String**|  | [optional] 
 **color** | **String**|  | [optional] 
 **q** | **String**|  | [optional] 
 **idN** | **String**|  | [optional] 
 **idLte** | **String**|  | [optional] 
 **idLt** | **String**|  | [optional] 
 **idGte** | **String**|  | [optional] 
 **idGt** | **String**|  | [optional] 
 **nameN** | **String**|  | [optional] 
 **nameIc** | **String**|  | [optional] 
 **nameNic** | **String**|  | [optional] 
 **nameIew** | **String**|  | [optional] 
 **nameNiew** | **String**|  | [optional] 
 **nameIsw** | **String**|  | [optional] 
 **nameNisw** | **String**|  | [optional] 
 **nameIe** | **String**|  | [optional] 
 **nameNie** | **String**|  | [optional] 
 **slugN** | **String**|  | [optional] 
 **slugIc** | **String**|  | [optional] 
 **slugNic** | **String**|  | [optional] 
 **slugIew** | **String**|  | [optional] 
 **slugNiew** | **String**|  | [optional] 
 **slugIsw** | **String**|  | [optional] 
 **slugNisw** | **String**|  | [optional] 
 **slugIe** | **String**|  | [optional] 
 **slugNie** | **String**|  | [optional] 
 **colorN** | **String**|  | [optional] 
 **colorIc** | **String**|  | [optional] 
 **colorNic** | **String**|  | [optional] 
 **colorIew** | **String**|  | [optional] 
 **colorNiew** | **String**|  | [optional] 
 **colorIsw** | **String**|  | [optional] 
 **colorNisw** | **String**|  | [optional] 
 **colorIe** | **String**|  | [optional] 
 **colorNie** | **String**|  | [optional] 
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
let id = 56; // Number | A unique integer value identifying this tag.
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
 **id** | **Number**| A unique integer value identifying this tag. | 
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



Call to super to allow for caching

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
let id = 56; // Number | A unique integer value identifying this tag.
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
 **id** | **Number**| A unique integer value identifying this tag. | 

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
let id = 56; // Number | A unique integer value identifying this tag.
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
 **id** | **Number**| A unique integer value identifying this tag. | 
 **tag** | [**Tag**](Tag.md)|  | 

### Return type

[**Tag**](Tag.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

