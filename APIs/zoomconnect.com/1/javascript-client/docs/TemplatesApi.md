# WwwZoomconnectCom.TemplatesApi

All URIs are relative to *https://www.zoomconnect.com/app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiRestV1TemplatesAllGet**](TemplatesApi.md#apiRestV1TemplatesAllGet) | **GET** /api/rest/v1/templates/all | all
[**apiRestV1TemplatesTemplateIdDelete**](TemplatesApi.md#apiRestV1TemplatesTemplateIdDelete) | **DELETE** /api/rest/v1/templates/{templateId} | delete
[**apiRestV1TemplatesTemplateIdGet**](TemplatesApi.md#apiRestV1TemplatesTemplateIdGet) | **GET** /api/rest/v1/templates/{templateId} | get



## apiRestV1TemplatesAllGet

> WebServiceTemplates apiRestV1TemplatesAllGet()

all

Returns all templates

### Example

```javascript
import WwwZoomconnectCom from 'www_zoomconnect_com';

let apiInstance = new WwwZoomconnectCom.TemplatesApi();
apiInstance.apiRestV1TemplatesAllGet((error, data, response) => {
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

[**WebServiceTemplates**](WebServiceTemplates.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## apiRestV1TemplatesTemplateIdDelete

> apiRestV1TemplatesTemplateIdDelete(templateId)

delete

Deletes a  template

### Example

```javascript
import WwwZoomconnectCom from 'www_zoomconnect_com';

let apiInstance = new WwwZoomconnectCom.TemplatesApi();
let templateId = 789; // Number | templateId
apiInstance.apiRestV1TemplatesTemplateIdDelete(templateId, (error, data, response) => {
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
 **templateId** | **Number**| templateId | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiRestV1TemplatesTemplateIdGet

> WebServiceTemplate apiRestV1TemplatesTemplateIdGet(templateId)

get

Returns details for a single template

### Example

```javascript
import WwwZoomconnectCom from 'www_zoomconnect_com';

let apiInstance = new WwwZoomconnectCom.TemplatesApi();
let templateId = 789; // Number | templateId
apiInstance.apiRestV1TemplatesTemplateIdGet(templateId, (error, data, response) => {
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
 **templateId** | **Number**| templateId | 

### Return type

[**WebServiceTemplate**](WebServiceTemplate.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

