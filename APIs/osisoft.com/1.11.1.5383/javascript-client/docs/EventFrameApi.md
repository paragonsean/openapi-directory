# PiWebApi2018Sp1SwaggerSpec.EventFrameApi

All URIs are relative to *https://devdata.osisoft.com/piwebapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**eventFrameAcknowledge**](EventFrameApi.md#eventFrameAcknowledge) | **PATCH** /eventframes/{webId}/acknowledge | Calls the EventFrame&#39;s Acknowledge method.
[**eventFrameCaptureValues**](EventFrameApi.md#eventFrameCaptureValues) | **POST** /eventframes/{webId}/attributes/capture | Calls the EventFrame&#39;s CaptureValues method.
[**eventFrameCreateAnnotation**](EventFrameApi.md#eventFrameCreateAnnotation) | **POST** /eventframes/{webId}/annotations | Create an annotation on an event frame.
[**eventFrameCreateAttribute**](EventFrameApi.md#eventFrameCreateAttribute) | **POST** /eventframes/{webId}/attributes | Create a new attribute of the specified event frame.
[**eventFrameCreateConfig**](EventFrameApi.md#eventFrameCreateConfig) | **POST** /eventframes/{webId}/config | Executes the create configuration function of the data references found within the attributes of the event frame, and optionally, its children.
[**eventFrameCreateEventFrame**](EventFrameApi.md#eventFrameCreateEventFrame) | **POST** /eventframes/{webId}/eventframes | Create an event frame as a child of the specified event frame.
[**eventFrameCreateSearchByAttribute**](EventFrameApi.md#eventFrameCreateSearchByAttribute) | **POST** /eventframes/searchbyattribute | Create a link for a \&quot;Search EventFrames By Attribute Value\&quot; operation, whose queries are specified in the request content. The SearchRoot is specified by the Web Id of the root EventFrame. If the SearchRoot is not specified, then the search starts at the Asset Database. ElementTemplate must be provided as the Web ID of the ElementTemplate, which are used to create the EventFrames. All the attributes in the queries must be defined as AttributeTemplates on the ElementTemplate. An array of attribute value queries are ANDed together to find the desired Element objects. At least one value query must be specified. There are limitations on SearchOperators.
[**eventFrameCreateSecurityEntry**](EventFrameApi.md#eventFrameCreateSecurityEntry) | **POST** /eventframes/{webId}/securityentries | Create a security entry owned by the event frame.
[**eventFrameDelete**](EventFrameApi.md#eventFrameDelete) | **DELETE** /eventframes/{webId} | Delete an event frame.
[**eventFrameDeleteAnnotation**](EventFrameApi.md#eventFrameDeleteAnnotation) | **DELETE** /eventframes/{webId}/annotations/{id} | Delete an annotation on an event frame. If the annotation has attached media, the attached media will also be deleted.
[**eventFrameDeleteAnnotationAttachmentMediaById**](EventFrameApi.md#eventFrameDeleteAnnotationAttachmentMediaById) | **DELETE** /eventframes/{webId}/annotations/{id}/attachment/media | Delete attached media from an annotation on an event frame.
[**eventFrameDeleteSecurityEntry**](EventFrameApi.md#eventFrameDeleteSecurityEntry) | **DELETE** /eventframes/{webId}/securityentries/{name} | Delete a security entry owned by the event frame.
[**eventFrameExecuteSearchByAttribute**](EventFrameApi.md#eventFrameExecuteSearchByAttribute) | **GET** /eventframes/searchbyattribute/{searchId} | Execute a \&quot;Search EventFrames By Attribute Value\&quot; operation.
[**eventFrameFindEventFrameAttributes**](EventFrameApi.md#eventFrameFindEventFrameAttributes) | **GET** /eventframes/{webId}/eventframeattributes | Retrieves a list of event frame attributes matching the specified filters from the specified event frame.
[**eventFrameGet**](EventFrameApi.md#eventFrameGet) | **GET** /eventframes/{webId} | Retrieve an event frame.
[**eventFrameGetAnnotationAttachmentMediaMetadataById**](EventFrameApi.md#eventFrameGetAnnotationAttachmentMediaMetadataById) | **GET** /eventframes/{webId}/annotations/{id}/attachment/media/metadata | Gets the metadata of the media attached to the specified annotation.
[**eventFrameGetAnnotationById**](EventFrameApi.md#eventFrameGetAnnotationById) | **GET** /eventframes/{webId}/annotations/{id} | Get a specific annotation on an event frame.
[**eventFrameGetAnnotations**](EventFrameApi.md#eventFrameGetAnnotations) | **GET** /eventframes/{webId}/annotations | Get an event frame&#39;s annotations.
[**eventFrameGetAttributes**](EventFrameApi.md#eventFrameGetAttributes) | **GET** /eventframes/{webId}/attributes | Get the attributes of the specified event frame.
[**eventFrameGetByPath**](EventFrameApi.md#eventFrameGetByPath) | **GET** /eventframes | Retrieve an event frame by path.
[**eventFrameGetCategories**](EventFrameApi.md#eventFrameGetCategories) | **GET** /eventframes/{webId}/categories | Get an event frame&#39;s categories.
[**eventFrameGetEventFrames**](EventFrameApi.md#eventFrameGetEventFrames) | **GET** /eventframes/{webId}/eventframes | Retrieve event frames based on the specified conditions. By default, returns all children of the specified root event frame that have been active in the past 8 hours.
[**eventFrameGetEventFramesQuery**](EventFrameApi.md#eventFrameGetEventFramesQuery) | **GET** /eventframes/search | Retrieve event frames based on the specified conditions. Returns event frames using the specified search query string.
[**eventFrameGetMultiple**](EventFrameApi.md#eventFrameGetMultiple) | **GET** /eventframes/multiple | Retrieve multiple event frames by web ids or paths.
[**eventFrameGetReferencedElements**](EventFrameApi.md#eventFrameGetReferencedElements) | **GET** /eventframes/{webId}/referencedelements | Retrieve the event frame&#39;s referenced elements.
[**eventFrameGetSecurity**](EventFrameApi.md#eventFrameGetSecurity) | **GET** /eventframes/{webId}/security | Get the security information of the specified security item associated with the event frame for a specified user.
[**eventFrameGetSecurityEntries**](EventFrameApi.md#eventFrameGetSecurityEntries) | **GET** /eventframes/{webId}/securityentries | Retrieve the security entries associated with the event frame based on the specified criteria. By default, all security entries for this event frame are returned.
[**eventFrameGetSecurityEntryByName**](EventFrameApi.md#eventFrameGetSecurityEntryByName) | **GET** /eventframes/{webId}/securityentries/{name} | Retrieve the security entry associated with the event frame with the specified name.
[**eventFrameUpdate**](EventFrameApi.md#eventFrameUpdate) | **PATCH** /eventframes/{webId} | Update an event frame by replacing items in its definition.
[**eventFrameUpdateAnnotation**](EventFrameApi.md#eventFrameUpdateAnnotation) | **PATCH** /eventframes/{webId}/annotations/{id} | Update an annotation on an event frame by replacing items in its definition.
[**eventFrameUpdateSecurityEntry**](EventFrameApi.md#eventFrameUpdateSecurityEntry) | **PUT** /eventframes/{webId}/securityentries/{name} | Update a security entry owned by the event frame.



## eventFrameAcknowledge

> eventFrameAcknowledge(webId)

Calls the EventFrame&#39;s Acknowledge method.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.EventFrameApi();
let webId = "webId_example"; // String | The ID of the event frame.
apiInstance.eventFrameAcknowledge(webId, (error, data, response) => {
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
 **webId** | **String**| The ID of the event frame. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## eventFrameCaptureValues

> eventFrameCaptureValues(webId)

Calls the EventFrame&#39;s CaptureValues method.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.EventFrameApi();
let webId = "webId_example"; // String | The ID of the event frame.
apiInstance.eventFrameCaptureValues(webId, (error, data, response) => {
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
 **webId** | **String**| The ID of the event frame. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## eventFrameCreateAnnotation

> eventFrameCreateAnnotation(webId, annotation, opts)

Create an annotation on an event frame.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.EventFrameApi();
let webId = "webId_example"; // String | The ID of the owner event frame on which to create the annotation.
let annotation = new PiWebApi2018Sp1SwaggerSpec.Annotation(); // Annotation | The new annotation definition.
let opts = {
  'webIdType': "webIdType_example" // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
};
apiInstance.eventFrameCreateAnnotation(webId, annotation, opts, (error, data, response) => {
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
 **webId** | **String**| The ID of the owner event frame on which to create the annotation. | 
 **annotation** | [**Annotation**](Annotation.md)| The new annotation definition. | 
 **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: Not defined


## eventFrameCreateAttribute

> eventFrameCreateAttribute(webId, attribute, opts)

Create a new attribute of the specified event frame.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.EventFrameApi();
let webId = "webId_example"; // String | The ID of the event frame on which to create the attribute.
let attribute = new PiWebApi2018Sp1SwaggerSpec.Attribute(); // Attribute | The definition of the new attribute.
let opts = {
  'webIdType': "webIdType_example" // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
};
apiInstance.eventFrameCreateAttribute(webId, attribute, opts, (error, data, response) => {
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
 **webId** | **String**| The ID of the event frame on which to create the attribute. | 
 **attribute** | [**Attribute**](Attribute.md)| The definition of the new attribute. | 
 **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: Not defined


## eventFrameCreateConfig

> eventFrameCreateConfig(webId, opts)

Executes the create configuration function of the data references found within the attributes of the event frame, and optionally, its children.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.EventFrameApi();
let webId = "webId_example"; // String | The ID of the event frame.
let opts = {
  'includeChildElements': true // Boolean | If true, includes the child event frames of the specified event frame.
};
apiInstance.eventFrameCreateConfig(webId, opts, (error, data, response) => {
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
 **webId** | **String**| The ID of the event frame. | 
 **includeChildElements** | **Boolean**| If true, includes the child event frames of the specified event frame. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## eventFrameCreateEventFrame

> eventFrameCreateEventFrame(webId, eventFrame, opts)

Create an event frame as a child of the specified event frame.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.EventFrameApi();
let webId = "webId_example"; // String | The ID of the parent event frame on which to create the event frame.
let eventFrame = new PiWebApi2018Sp1SwaggerSpec.EventFrame(); // EventFrame | The new event frame definition.
let opts = {
  'webIdType': "webIdType_example" // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
};
apiInstance.eventFrameCreateEventFrame(webId, eventFrame, opts, (error, data, response) => {
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
 **webId** | **String**| The ID of the parent event frame on which to create the event frame. | 
 **eventFrame** | [**EventFrame**](EventFrame.md)| The new event frame definition. | 
 **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: Not defined


## eventFrameCreateSearchByAttribute

> ItemsEventFrame eventFrameCreateSearchByAttribute(query, opts)

Create a link for a \&quot;Search EventFrames By Attribute Value\&quot; operation, whose queries are specified in the request content. The SearchRoot is specified by the Web Id of the root EventFrame. If the SearchRoot is not specified, then the search starts at the Asset Database. ElementTemplate must be provided as the Web ID of the ElementTemplate, which are used to create the EventFrames. All the attributes in the queries must be defined as AttributeTemplates on the ElementTemplate. An array of attribute value queries are ANDed together to find the desired Element objects. At least one value query must be specified. There are limitations on SearchOperators.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.EventFrameApi();
let query = new PiWebApi2018Sp1SwaggerSpec.SearchByAttribute(); // SearchByAttribute | The query of search by attribute.
let opts = {
  'noResults': true, // Boolean | If false, the response content will contain the first page of the search results. If true, the response content will be empty. The default is false.
  'selectedFields': "selectedFields_example", // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
  'webIdType': "webIdType_example" // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
};
apiInstance.eventFrameCreateSearchByAttribute(query, opts, (error, data, response) => {
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
 **query** | [**SearchByAttribute**](SearchByAttribute.md)| The query of search by attribute. | 
 **noResults** | **Boolean**| If false, the response content will contain the first page of the search results. If true, the response content will be empty. The default is false. | [optional] 
 **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 
 **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] 

### Return type

[**ItemsEventFrame**](ItemsEventFrame.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: application/json, text/json, text/html, application/x-ms-application


## eventFrameCreateSecurityEntry

> eventFrameCreateSecurityEntry(webId, securityEntry, opts)

Create a security entry owned by the event frame.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.EventFrameApi();
let webId = "webId_example"; // String | The ID of the event frame where the security entry will be created.
let securityEntry = new PiWebApi2018Sp1SwaggerSpec.SecurityEntry(); // SecurityEntry | The new security entry definition. The full list of allow and deny rights must be supplied.
let opts = {
  'applyToChildren': true, // Boolean | If false, the new access permissions are only applied to the associated object. If true, the access permissions of children with any parent-child reference types will change when the permissions on the primary parent change.
  'webIdType': "webIdType_example" // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
};
apiInstance.eventFrameCreateSecurityEntry(webId, securityEntry, opts, (error, data, response) => {
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
 **webId** | **String**| The ID of the event frame where the security entry will be created. | 
 **securityEntry** | [**SecurityEntry**](SecurityEntry.md)| The new security entry definition. The full list of allow and deny rights must be supplied. | 
 **applyToChildren** | **Boolean**| If false, the new access permissions are only applied to the associated object. If true, the access permissions of children with any parent-child reference types will change when the permissions on the primary parent change. | [optional] 
 **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: Not defined


## eventFrameDelete

> eventFrameDelete(webId)

Delete an event frame.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.EventFrameApi();
let webId = "webId_example"; // String | The ID of the event frame to delete.
apiInstance.eventFrameDelete(webId, (error, data, response) => {
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
 **webId** | **String**| The ID of the event frame to delete. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## eventFrameDeleteAnnotation

> eventFrameDeleteAnnotation(id, webId)

Delete an annotation on an event frame. If the annotation has attached media, the attached media will also be deleted.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.EventFrameApi();
let id = "id_example"; // String | The Annotation identifier of the annotation to be deleted.
let webId = "webId_example"; // String | The ID of the owner event frame of the annotation to delete.
apiInstance.eventFrameDeleteAnnotation(id, webId, (error, data, response) => {
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
 **id** | **String**| The Annotation identifier of the annotation to be deleted. | 
 **webId** | **String**| The ID of the owner event frame of the annotation to delete. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## eventFrameDeleteAnnotationAttachmentMediaById

> eventFrameDeleteAnnotationAttachmentMediaById(id, webId)

Delete attached media from an annotation on an event frame.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.EventFrameApi();
let id = "id_example"; // String | The Annotation identifier of the annotation to delete the attached media of.
let webId = "webId_example"; // String | The ID of the owner event frame of the annotation to delete the attached media of.
apiInstance.eventFrameDeleteAnnotationAttachmentMediaById(id, webId, (error, data, response) => {
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
 **id** | **String**| The Annotation identifier of the annotation to delete the attached media of. | 
 **webId** | **String**| The ID of the owner event frame of the annotation to delete the attached media of. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/html, application/x-ms-application


## eventFrameDeleteSecurityEntry

> eventFrameDeleteSecurityEntry(name, webId, opts)

Delete a security entry owned by the event frame.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.EventFrameApi();
let name = "name_example"; // String | The name of the security entry. For every backslash character (\\) in the security entry name, replace with asterisk (*). As an example, use domain*username instead of domain\\username.
let webId = "webId_example"; // String | The ID of the event frame where the security entry will be deleted.
let opts = {
  'applyToChildren': true // Boolean | If false, the new access permissions are only applied to the associated object. If true, the access permissions of children with any parent-child reference types will change when the permissions on the primary parent change.
};
apiInstance.eventFrameDeleteSecurityEntry(name, webId, opts, (error, data, response) => {
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
 **name** | **String**| The name of the security entry. For every backslash character (\\) in the security entry name, replace with asterisk (*). As an example, use domain*username instead of domain\\username. | 
 **webId** | **String**| The ID of the event frame where the security entry will be deleted. | 
 **applyToChildren** | **Boolean**| If false, the new access permissions are only applied to the associated object. If true, the access permissions of children with any parent-child reference types will change when the permissions on the primary parent change. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## eventFrameExecuteSearchByAttribute

> ItemsEventFrame eventFrameExecuteSearchByAttribute(searchId, opts)

Execute a \&quot;Search EventFrames By Attribute Value\&quot; operation.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.EventFrameApi();
let searchId = "searchId_example"; // String | The encoded search Id of the \"Search EventFrames By Attribute Value\" operation.
let opts = {
  'canBeAcknowledged': true, // Boolean | Specify the returned event frames' canBeAcknowledged property. The default is no canBeAcknowledged filter.
  'endTime': "endTime_example", // String | The ending time for the search. endTime must be greater than or equal to the startTime. The searchMode parameter will control whether the comparison will be performed against the event frame's startTime or endTime. The default is '*'.
  'isAcknowledged': true, // Boolean | Specify the returned event frames' isAcknowledged property. The default no isAcknowledged filter.
  'maxCount': 56, // Number | The maximum number of objects to be returned per call (page size). The default is 1000.
  'nameFilter': "nameFilter_example", // String | The name query string used for finding event frames. The default is no filter.
  'referencedElementNameFilter': "referencedElementNameFilter_example", // String | The name query string which must match the name of a referenced element. The default is no filter.
  'searchFullHierarchy': true, // Boolean | Specifies whether the search should include objects nested further than the immediate children of the search root. The default is 'false'.
  'searchMode': "searchMode_example", // String | Determines how the startTime and endTime parameters are treated when searching for event frame objects to be included in the returned collection. The default is 'Overlapped'.
  'selectedFields': "selectedFields_example", // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
  'severity': ["null"], // [String] | Specify that returned event frames must have this severity. Multiple severity values may be specified with multiple instances of the parameter. The default is no severity filter.
  'sortField': "sortField_example", // String | The field or property of the object used to sort the returned collection. The default is 'Name'.
  'sortOrder': "sortOrder_example", // String | The order that the returned collection is sorted. The default is 'Ascending'.
  'startIndex': 56, // Number | The starting index (zero based) of the items to be returned. The default is 0.
  'startTime': "startTime_example", // String | The starting time for the search. startTime must be less than or equal to the endTime. The searchMode parameter will control whether the comparison will be performed against the event frame's startTime or endTime. The default is '*-8h'.
  'webIdType': "webIdType_example" // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
};
apiInstance.eventFrameExecuteSearchByAttribute(searchId, opts, (error, data, response) => {
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
 **searchId** | **String**| The encoded search Id of the \&quot;Search EventFrames By Attribute Value\&quot; operation. | 
 **canBeAcknowledged** | **Boolean**| Specify the returned event frames&#39; canBeAcknowledged property. The default is no canBeAcknowledged filter. | [optional] 
 **endTime** | **String**| The ending time for the search. endTime must be greater than or equal to the startTime. The searchMode parameter will control whether the comparison will be performed against the event frame&#39;s startTime or endTime. The default is &#39;*&#39;. | [optional] 
 **isAcknowledged** | **Boolean**| Specify the returned event frames&#39; isAcknowledged property. The default no isAcknowledged filter. | [optional] 
 **maxCount** | **Number**| The maximum number of objects to be returned per call (page size). The default is 1000. | [optional] 
 **nameFilter** | **String**| The name query string used for finding event frames. The default is no filter. | [optional] 
 **referencedElementNameFilter** | **String**| The name query string which must match the name of a referenced element. The default is no filter. | [optional] 
 **searchFullHierarchy** | **Boolean**| Specifies whether the search should include objects nested further than the immediate children of the search root. The default is &#39;false&#39;. | [optional] 
 **searchMode** | **String**| Determines how the startTime and endTime parameters are treated when searching for event frame objects to be included in the returned collection. The default is &#39;Overlapped&#39;. | [optional] 
 **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 
 **severity** | [**[String]**](String.md)| Specify that returned event frames must have this severity. Multiple severity values may be specified with multiple instances of the parameter. The default is no severity filter. | [optional] 
 **sortField** | **String**| The field or property of the object used to sort the returned collection. The default is &#39;Name&#39;. | [optional] 
 **sortOrder** | **String**| The order that the returned collection is sorted. The default is &#39;Ascending&#39;. | [optional] 
 **startIndex** | **Number**| The starting index (zero based) of the items to be returned. The default is 0. | [optional] 
 **startTime** | **String**| The starting time for the search. startTime must be less than or equal to the endTime. The searchMode parameter will control whether the comparison will be performed against the event frame&#39;s startTime or endTime. The default is &#39;*-8h&#39;. | [optional] 
 **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] 

### Return type

[**ItemsEventFrame**](ItemsEventFrame.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/html, application/x-ms-application


## eventFrameFindEventFrameAttributes

> ItemsAttribute eventFrameFindEventFrameAttributes(webId, opts)

Retrieves a list of event frame attributes matching the specified filters from the specified event frame.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.EventFrameApi();
let webId = "webId_example"; // String | The ID of the event frame to use as the root of the search.
let opts = {
  'associations': "associations_example", // String | Associated values to return in the response, separated by semicolons (;). This call supports DataReference to return attributes with data references. If this parameter is not specified, DataReference values are not returned.
  'attributeCategory': "attributeCategory_example", // String | Specify that returned attributes must have this category. The default is no filter.
  'attributeDescriptionFilter': "attributeDescriptionFilter_example", // String | The attribute description filter string used for finding objects. Only the first 440 characters of the description will be searched. For Asset Servers older than 2.7, a 400 status code (Bad Request) will be returned if this parameter is specified. The default is no filter.
  'attributeNameFilter': "attributeNameFilter_example", // String | The attribute name filter string used for finding objects. The default is no filter.
  'attributeType': "attributeType_example", // String | Specify that returned attributes' value type must be this value type. The default is no filter.
  'endTime': "endTime_example", // String | A string representing the latest ending time for the event frames to be matched. The endTime must be greater than or equal to the startTime. The default is '*'.
  'eventFrameCategory': "eventFrameCategory_example", // String | Specify that the owner of the returned attributes must have this category. The default is no filter.
  'eventFrameDescriptionFilter': "eventFrameDescriptionFilter_example", // String | The event frame description filter string used for finding objects. Only the first 440 characters of the description will be searched. For Asset Servers older than 2.7, a 400 status code (Bad Request) will be returned if this parameter is specified. The default is no filter.
  'eventFrameNameFilter': "eventFrameNameFilter_example", // String | The event frame name filter string used for finding objects. The default is no filter.
  'eventFrameTemplate': "eventFrameTemplate_example", // String | Specify that the owner of the returned attributes must have this template or a template derived from this template. The default is no filter.
  'maxCount': 56, // Number | The maximum number of objects to be returned (the page size). The default is 1000.
  'referencedElementNameFilter': "referencedElementNameFilter_example", // String | The name query string which must match the name of a referenced element. The default is no filter.
  'searchFullHierarchy': true, // Boolean | Specifies if the search should include objects nested further than immediate children of the given resource. The default is 'false'.
  'searchMode': "searchMode_example", // String | Determines how the startTime and endTime parameters are treated when searching for event frames. The default is 'Overlapped'.
  'selectedFields': "selectedFields_example", // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
  'sortField': "sortField_example", // String | The field or property of the object used to sort the returned collection. The default is 'Name'.
  'sortOrder': "sortOrder_example", // String | The order that the returned collection is sorted. The default is 'Ascending'.
  'startIndex': 56, // Number | The starting index (zero based) of the items to be returned. The default is 0.
  'startTime': "startTime_example", // String | A string representing the earliest starting time for the event frames to be matched. startTime must be less than or equal to the endTime. The default is '*-8h'.
  'webIdType': "webIdType_example" // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
};
apiInstance.eventFrameFindEventFrameAttributes(webId, opts, (error, data, response) => {
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
 **webId** | **String**| The ID of the event frame to use as the root of the search. | 
 **associations** | **String**| Associated values to return in the response, separated by semicolons (;). This call supports DataReference to return attributes with data references. If this parameter is not specified, DataReference values are not returned. | [optional] 
 **attributeCategory** | **String**| Specify that returned attributes must have this category. The default is no filter. | [optional] 
 **attributeDescriptionFilter** | **String**| The attribute description filter string used for finding objects. Only the first 440 characters of the description will be searched. For Asset Servers older than 2.7, a 400 status code (Bad Request) will be returned if this parameter is specified. The default is no filter. | [optional] 
 **attributeNameFilter** | **String**| The attribute name filter string used for finding objects. The default is no filter. | [optional] 
 **attributeType** | **String**| Specify that returned attributes&#39; value type must be this value type. The default is no filter. | [optional] 
 **endTime** | **String**| A string representing the latest ending time for the event frames to be matched. The endTime must be greater than or equal to the startTime. The default is &#39;*&#39;. | [optional] 
 **eventFrameCategory** | **String**| Specify that the owner of the returned attributes must have this category. The default is no filter. | [optional] 
 **eventFrameDescriptionFilter** | **String**| The event frame description filter string used for finding objects. Only the first 440 characters of the description will be searched. For Asset Servers older than 2.7, a 400 status code (Bad Request) will be returned if this parameter is specified. The default is no filter. | [optional] 
 **eventFrameNameFilter** | **String**| The event frame name filter string used for finding objects. The default is no filter. | [optional] 
 **eventFrameTemplate** | **String**| Specify that the owner of the returned attributes must have this template or a template derived from this template. The default is no filter. | [optional] 
 **maxCount** | **Number**| The maximum number of objects to be returned (the page size). The default is 1000. | [optional] 
 **referencedElementNameFilter** | **String**| The name query string which must match the name of a referenced element. The default is no filter. | [optional] 
 **searchFullHierarchy** | **Boolean**| Specifies if the search should include objects nested further than immediate children of the given resource. The default is &#39;false&#39;. | [optional] 
 **searchMode** | **String**| Determines how the startTime and endTime parameters are treated when searching for event frames. The default is &#39;Overlapped&#39;. | [optional] 
 **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 
 **sortField** | **String**| The field or property of the object used to sort the returned collection. The default is &#39;Name&#39;. | [optional] 
 **sortOrder** | **String**| The order that the returned collection is sorted. The default is &#39;Ascending&#39;. | [optional] 
 **startIndex** | **Number**| The starting index (zero based) of the items to be returned. The default is 0. | [optional] 
 **startTime** | **String**| A string representing the earliest starting time for the event frames to be matched. startTime must be less than or equal to the endTime. The default is &#39;*-8h&#39;. | [optional] 
 **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] 

### Return type

[**ItemsAttribute**](ItemsAttribute.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/html, application/x-ms-application


## eventFrameGet

> EventFrame eventFrameGet(webId, opts)

Retrieve an event frame.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.EventFrameApi();
let webId = "webId_example"; // String | The ID of the event frame.
let opts = {
  'selectedFields': "selectedFields_example", // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
  'webIdType': "webIdType_example" // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
};
apiInstance.eventFrameGet(webId, opts, (error, data, response) => {
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
 **webId** | **String**| The ID of the event frame. | 
 **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 
 **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] 

### Return type

[**EventFrame**](EventFrame.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/html, application/x-ms-application


## eventFrameGetAnnotationAttachmentMediaMetadataById

> MediaMetadata eventFrameGetAnnotationAttachmentMediaMetadataById(id, webId, opts)

Gets the metadata of the media attached to the specified annotation.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.EventFrameApi();
let id = "id_example"; // String | The Annotation identifier of the specific annotation.
let webId = "webId_example"; // String | The ID of the owner event frame.
let opts = {
  'selectedFields': "selectedFields_example", // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
  'webIdType': "webIdType_example" // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
};
apiInstance.eventFrameGetAnnotationAttachmentMediaMetadataById(id, webId, opts, (error, data, response) => {
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
 **id** | **String**| The Annotation identifier of the specific annotation. | 
 **webId** | **String**| The ID of the owner event frame. | 
 **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 
 **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] 

### Return type

[**MediaMetadata**](MediaMetadata.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/html, application/x-ms-application


## eventFrameGetAnnotationById

> Annotation eventFrameGetAnnotationById(id, webId, opts)

Get a specific annotation on an event frame.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.EventFrameApi();
let id = "id_example"; // String | The Annotation identifier of the specific annotation.
let webId = "webId_example"; // String | The ID of the owner event frame.
let opts = {
  'selectedFields': "selectedFields_example", // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
  'webIdType': "webIdType_example" // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
};
apiInstance.eventFrameGetAnnotationById(id, webId, opts, (error, data, response) => {
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
 **id** | **String**| The Annotation identifier of the specific annotation. | 
 **webId** | **String**| The ID of the owner event frame. | 
 **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 
 **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] 

### Return type

[**Annotation**](Annotation.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/html, application/x-ms-application


## eventFrameGetAnnotations

> ItemsAnnotation eventFrameGetAnnotations(webId, opts)

Get an event frame&#39;s annotations.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.EventFrameApi();
let webId = "webId_example"; // String | The ID of the owner event frame.
let opts = {
  'selectedFields': "selectedFields_example", // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
  'webIdType': "webIdType_example" // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
};
apiInstance.eventFrameGetAnnotations(webId, opts, (error, data, response) => {
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
 **webId** | **String**| The ID of the owner event frame. | 
 **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 
 **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] 

### Return type

[**ItemsAnnotation**](ItemsAnnotation.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/html, application/x-ms-application


## eventFrameGetAttributes

> ItemsAttribute eventFrameGetAttributes(webId, opts)

Get the attributes of the specified event frame.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.EventFrameApi();
let webId = "webId_example"; // String | The ID of the event frame.
let opts = {
  'associations': "associations_example", // String | Associated values to return in the response, separated by semicolons (;). This call supports DataReference to return attributes with data references. If this parameter is not specified, DataReference values are not returned.
  'categoryName': "categoryName_example", // String | Specify that returned attributes must have this category. The default is no category filter.
  'maxCount': 56, // Number | The maximum number of objects to be returned per call (page size). The default is 1000.
  'nameFilter': "nameFilter_example", // String | The name query string used for finding attributes. The default is no filter.
  'searchFullHierarchy': true, // Boolean | Specifies if the search should include attributes nested further than the immediate attributes of the searchRoot. The default is 'false'.
  'selectedFields': "selectedFields_example", // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
  'showExcluded': true, // Boolean | Specified if the search should include attributes with the Excluded property set. The default is 'false'.
  'showHidden': true, // Boolean | Specified if the search should include attributes with the Hidden property set. The default is 'false'.
  'sortField': "sortField_example", // String | The field or property of the object used to sort the returned collection. The default is 'Name'.
  'sortOrder': "sortOrder_example", // String | The order that the returned collection is sorted. The default is 'Ascending'.
  'startIndex': 56, // Number | The starting index (zero based) of the items to be returned. The default is 0.
  'templateName': "templateName_example", // String | Specify that returned attributes must be members of this template. The default is no template filter.
  'trait': ["null"], // [String] | The name of the attribute trait. Multiple traits may be specified with multiple instances of the parameter.
  'traitCategory': ["null"], // [String] | The category of the attribute traits. Multiple categories may be specified with multiple instances of the parameter. If the parameter is not specified, or if its value is \"all\", then all attribute traits of all categories will be returned.
  'valueType': "valueType_example", // String | Specify that returned attributes' value type must be the given value type. The default is no value type filter.
  'webIdType': "webIdType_example" // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
};
apiInstance.eventFrameGetAttributes(webId, opts, (error, data, response) => {
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
 **webId** | **String**| The ID of the event frame. | 
 **associations** | **String**| Associated values to return in the response, separated by semicolons (;). This call supports DataReference to return attributes with data references. If this parameter is not specified, DataReference values are not returned. | [optional] 
 **categoryName** | **String**| Specify that returned attributes must have this category. The default is no category filter. | [optional] 
 **maxCount** | **Number**| The maximum number of objects to be returned per call (page size). The default is 1000. | [optional] 
 **nameFilter** | **String**| The name query string used for finding attributes. The default is no filter. | [optional] 
 **searchFullHierarchy** | **Boolean**| Specifies if the search should include attributes nested further than the immediate attributes of the searchRoot. The default is &#39;false&#39;. | [optional] 
 **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 
 **showExcluded** | **Boolean**| Specified if the search should include attributes with the Excluded property set. The default is &#39;false&#39;. | [optional] 
 **showHidden** | **Boolean**| Specified if the search should include attributes with the Hidden property set. The default is &#39;false&#39;. | [optional] 
 **sortField** | **String**| The field or property of the object used to sort the returned collection. The default is &#39;Name&#39;. | [optional] 
 **sortOrder** | **String**| The order that the returned collection is sorted. The default is &#39;Ascending&#39;. | [optional] 
 **startIndex** | **Number**| The starting index (zero based) of the items to be returned. The default is 0. | [optional] 
 **templateName** | **String**| Specify that returned attributes must be members of this template. The default is no template filter. | [optional] 
 **trait** | [**[String]**](String.md)| The name of the attribute trait. Multiple traits may be specified with multiple instances of the parameter. | [optional] 
 **traitCategory** | [**[String]**](String.md)| The category of the attribute traits. Multiple categories may be specified with multiple instances of the parameter. If the parameter is not specified, or if its value is \&quot;all\&quot;, then all attribute traits of all categories will be returned. | [optional] 
 **valueType** | **String**| Specify that returned attributes&#39; value type must be the given value type. The default is no value type filter. | [optional] 
 **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] 

### Return type

[**ItemsAttribute**](ItemsAttribute.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/html, application/x-ms-application


## eventFrameGetByPath

> EventFrame eventFrameGetByPath(path, opts)

Retrieve an event frame by path.

This method returns an event frame based on the hierarchical path associated with it, and should be used when a path has been received from a separate part of the PI System for use in the PI Web API. Users should primarily search with the WebID when available.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.EventFrameApi();
let path = "path_example"; // String | The path to the event frame.
let opts = {
  'selectedFields': "selectedFields_example", // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
  'webIdType': "webIdType_example" // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
};
apiInstance.eventFrameGetByPath(path, opts, (error, data, response) => {
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
 **path** | **String**| The path to the event frame. | 
 **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 
 **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] 

### Return type

[**EventFrame**](EventFrame.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/html, application/x-ms-application


## eventFrameGetCategories

> ItemsElementCategory eventFrameGetCategories(webId, opts)

Get an event frame&#39;s categories.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.EventFrameApi();
let webId = "webId_example"; // String | The ID of the event frame.
let opts = {
  'selectedFields': "selectedFields_example", // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
  'webIdType': "webIdType_example" // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
};
apiInstance.eventFrameGetCategories(webId, opts, (error, data, response) => {
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
 **webId** | **String**| The ID of the event frame. | 
 **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 
 **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] 

### Return type

[**ItemsElementCategory**](ItemsElementCategory.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/html, application/x-ms-application


## eventFrameGetEventFrames

> ItemsEventFrame eventFrameGetEventFrames(webId, opts)

Retrieve event frames based on the specified conditions. By default, returns all children of the specified root event frame that have been active in the past 8 hours.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.EventFrameApi();
let webId = "webId_example"; // String | The ID of the event frame to use as the root of the search.
let opts = {
  'canBeAcknowledged': true, // Boolean | Specify the returned event frames' canBeAcknowledged property. The default is no canBeAcknowledged filter.
  'categoryName': "categoryName_example", // String | Specify that returned event frames must have this category. The default is no category filter.
  'endTime': "endTime_example", // String | The ending time for the search. The endTime must be greater than or equal to the startTime. The searchMode parameter will control whether the comparison will be performed against the event frame's startTime or endTime. The default is '*' if searchMode is not one of the 'Backward*' or 'Forward*' values.
  'isAcknowledged': true, // Boolean | Specify the returned event frames' isAcknowledged property. The default no isAcknowledged filter.
  'maxCount': 56, // Number | The maximum number of objects to be returned per call (page size). The default is 1000.
  'nameFilter': "nameFilter_example", // String | The name query string used for finding event frames. The default is no filter.
  'referencedElementNameFilter': "referencedElementNameFilter_example", // String | The name query string which must match the name of a referenced element. The default is no filter.
  'referencedElementTemplateName': "referencedElementTemplateName_example", // String | Specify that returned event frames must have an element in the event frame's referenced elements collection that derives from the template. Specify this parameter by name.
  'searchFullHierarchy': true, // Boolean | Specifies whether the search should include objects nested further than the immediate children of the search root. The default is 'false'.
  'searchMode': "searchMode_example", // String | Determines how the startTime and endTime parameters are treated when searching for event frame objects to be included in the returned collection. If this parameter is one of the 'Backward*' or 'Forward*' values, none of endTime, sortField, or sortOrder may be specified. The default is 'Overlapped'.
  'selectedFields': "selectedFields_example", // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
  'severity': ["null"], // [String] | Specify that returned event frames must have this severity. Multiple severity values may be specified with multiple instances of the parameter. The default is no severity filter.
  'sortField': "sortField_example", // String | The field or property of the object used to sort the returned collection. The default is 'Name' if searchMode is not one of the 'Backward*' or 'Forward*' values.
  'sortOrder': "sortOrder_example", // String | The order that the returned collection is sorted. The default is 'Ascending' if searchMode is not one of the 'Backward*' or 'Forward*' values.
  'startIndex': 56, // Number | The starting index (zero based) of the items to be returned. The default is 0.
  'startTime': "startTime_example", // String | The starting time for the search. startTime must be less than or equal to the endTime. The searchMode parameter will control whether the comparison will be performed against the event frame's startTime or endTime. The default is '*-8h'.
  'templateName': "templateName_example", // String | Specify that returned event frames must have this template or a template derived from this template. The default is no template filter. Specify this parameter by name.
  'webIdType': "webIdType_example" // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
};
apiInstance.eventFrameGetEventFrames(webId, opts, (error, data, response) => {
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
 **webId** | **String**| The ID of the event frame to use as the root of the search. | 
 **canBeAcknowledged** | **Boolean**| Specify the returned event frames&#39; canBeAcknowledged property. The default is no canBeAcknowledged filter. | [optional] 
 **categoryName** | **String**| Specify that returned event frames must have this category. The default is no category filter. | [optional] 
 **endTime** | **String**| The ending time for the search. The endTime must be greater than or equal to the startTime. The searchMode parameter will control whether the comparison will be performed against the event frame&#39;s startTime or endTime. The default is &#39;*&#39; if searchMode is not one of the &#39;Backward*&#39; or &#39;Forward*&#39; values. | [optional] 
 **isAcknowledged** | **Boolean**| Specify the returned event frames&#39; isAcknowledged property. The default no isAcknowledged filter. | [optional] 
 **maxCount** | **Number**| The maximum number of objects to be returned per call (page size). The default is 1000. | [optional] 
 **nameFilter** | **String**| The name query string used for finding event frames. The default is no filter. | [optional] 
 **referencedElementNameFilter** | **String**| The name query string which must match the name of a referenced element. The default is no filter. | [optional] 
 **referencedElementTemplateName** | **String**| Specify that returned event frames must have an element in the event frame&#39;s referenced elements collection that derives from the template. Specify this parameter by name. | [optional] 
 **searchFullHierarchy** | **Boolean**| Specifies whether the search should include objects nested further than the immediate children of the search root. The default is &#39;false&#39;. | [optional] 
 **searchMode** | **String**| Determines how the startTime and endTime parameters are treated when searching for event frame objects to be included in the returned collection. If this parameter is one of the &#39;Backward*&#39; or &#39;Forward*&#39; values, none of endTime, sortField, or sortOrder may be specified. The default is &#39;Overlapped&#39;. | [optional] 
 **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 
 **severity** | [**[String]**](String.md)| Specify that returned event frames must have this severity. Multiple severity values may be specified with multiple instances of the parameter. The default is no severity filter. | [optional] 
 **sortField** | **String**| The field or property of the object used to sort the returned collection. The default is &#39;Name&#39; if searchMode is not one of the &#39;Backward*&#39; or &#39;Forward*&#39; values. | [optional] 
 **sortOrder** | **String**| The order that the returned collection is sorted. The default is &#39;Ascending&#39; if searchMode is not one of the &#39;Backward*&#39; or &#39;Forward*&#39; values. | [optional] 
 **startIndex** | **Number**| The starting index (zero based) of the items to be returned. The default is 0. | [optional] 
 **startTime** | **String**| The starting time for the search. startTime must be less than or equal to the endTime. The searchMode parameter will control whether the comparison will be performed against the event frame&#39;s startTime or endTime. The default is &#39;*-8h&#39;. | [optional] 
 **templateName** | **String**| Specify that returned event frames must have this template or a template derived from this template. The default is no template filter. Specify this parameter by name. | [optional] 
 **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] 

### Return type

[**ItemsEventFrame**](ItemsEventFrame.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/html, application/x-ms-application


## eventFrameGetEventFramesQuery

> ItemsEventFrame eventFrameGetEventFramesQuery(opts)

Retrieve event frames based on the specified conditions. Returns event frames using the specified search query string.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.EventFrameApi();
let opts = {
  'databaseWebId': "databaseWebId_example", // String | The ID of the asset database to use as the root of the query.
  'maxCount': 56, // Number | The maximum number of objects to be returned per call (page size). The default is 1000.
  'query': "query_example", // String | The query string is a list of filters used to perform an AFSearch for the eventframes in the asset database. An example would be: \"query=Name:=MyEventFrame* Category:=MyCategory Template:=EFTemplate\".
  'selectedFields': "selectedFields_example", // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
  'startIndex': 56, // Number | The starting index (zero based) of the items to be returned. The default is 0.
  'webIdType': "webIdType_example" // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
};
apiInstance.eventFrameGetEventFramesQuery(opts, (error, data, response) => {
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
 **databaseWebId** | **String**| The ID of the asset database to use as the root of the query. | [optional] 
 **maxCount** | **Number**| The maximum number of objects to be returned per call (page size). The default is 1000. | [optional] 
 **query** | **String**| The query string is a list of filters used to perform an AFSearch for the eventframes in the asset database. An example would be: \&quot;query&#x3D;Name:&#x3D;MyEventFrame* Category:&#x3D;MyCategory Template:&#x3D;EFTemplate\&quot;. | [optional] 
 **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 
 **startIndex** | **Number**| The starting index (zero based) of the items to be returned. The default is 0. | [optional] 
 **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] 

### Return type

[**ItemsEventFrame**](ItemsEventFrame.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/html, application/x-ms-application


## eventFrameGetMultiple

> ItemsItemEventFrame eventFrameGetMultiple(opts)

Retrieve multiple event frames by web ids or paths.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.EventFrameApi();
let opts = {
  'asParallel': true, // Boolean | Specifies if the retrieval processes should be run in parallel on the server. This may improve the response time for large amounts of requested attributes. The default is 'false'.
  'includeMode': "includeMode_example", // String | The include mode for the return list. The default is 'All'.
  'path': ["null"], // [String] | The path of an event frame. Multiple event frames may be specified with multiple instances of the parameter.
  'selectedFields': "selectedFields_example", // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
  'webId': ["null"], // [String] | The ID of an event frame. Multiple event frames may be specified with multiple instances of the parameter.
  'webIdType': "webIdType_example" // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
};
apiInstance.eventFrameGetMultiple(opts, (error, data, response) => {
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
 **asParallel** | **Boolean**| Specifies if the retrieval processes should be run in parallel on the server. This may improve the response time for large amounts of requested attributes. The default is &#39;false&#39;. | [optional] 
 **includeMode** | **String**| The include mode for the return list. The default is &#39;All&#39;. | [optional] 
 **path** | [**[String]**](String.md)| The path of an event frame. Multiple event frames may be specified with multiple instances of the parameter. | [optional] 
 **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 
 **webId** | [**[String]**](String.md)| The ID of an event frame. Multiple event frames may be specified with multiple instances of the parameter. | [optional] 
 **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] 

### Return type

[**ItemsItemEventFrame**](ItemsItemEventFrame.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/html, application/x-ms-application


## eventFrameGetReferencedElements

> ItemsElement eventFrameGetReferencedElements(webId, opts)

Retrieve the event frame&#39;s referenced elements.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.EventFrameApi();
let webId = "webId_example"; // String | The ID of the event frame whose referenced elements should be retrieved.
let opts = {
  'associations': "associations_example", // String | Associated values to return in the response, separated by semicolons (;). This call supports Paths to return all paths to the element. If this parameter is not specified, paths are not returned.
  'selectedFields': "selectedFields_example", // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
  'webIdType': "webIdType_example" // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
};
apiInstance.eventFrameGetReferencedElements(webId, opts, (error, data, response) => {
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
 **webId** | **String**| The ID of the event frame whose referenced elements should be retrieved. | 
 **associations** | **String**| Associated values to return in the response, separated by semicolons (;). This call supports Paths to return all paths to the element. If this parameter is not specified, paths are not returned. | [optional] 
 **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 
 **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] 

### Return type

[**ItemsElement**](ItemsElement.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/html, application/x-ms-application


## eventFrameGetSecurity

> ItemsSecurityRights eventFrameGetSecurity(webId, userIdentity, opts)

Get the security information of the specified security item associated with the event frame for a specified user.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.EventFrameApi();
let webId = "webId_example"; // String | The ID of the event frame for the security to be checked.
let userIdentity = ["null"]; // [String] | The user identity for the security information to be checked. Multiple security identities may be specified with multiple instances of the parameter. If the parameter is not specified, only the current user's security rights will be returned.
let opts = {
  'forceRefresh': true, // Boolean | Indicates if the security cache should be refreshed before getting security information. The default is 'false'.
  'selectedFields': "selectedFields_example", // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
  'webIdType': "webIdType_example" // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
};
apiInstance.eventFrameGetSecurity(webId, userIdentity, opts, (error, data, response) => {
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
 **webId** | **String**| The ID of the event frame for the security to be checked. | 
 **userIdentity** | [**[String]**](String.md)| The user identity for the security information to be checked. Multiple security identities may be specified with multiple instances of the parameter. If the parameter is not specified, only the current user&#39;s security rights will be returned. | 
 **forceRefresh** | **Boolean**| Indicates if the security cache should be refreshed before getting security information. The default is &#39;false&#39;. | [optional] 
 **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 
 **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] 

### Return type

[**ItemsSecurityRights**](ItemsSecurityRights.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/html, application/x-ms-application


## eventFrameGetSecurityEntries

> ItemsSecurityEntry eventFrameGetSecurityEntries(webId, opts)

Retrieve the security entries associated with the event frame based on the specified criteria. By default, all security entries for this event frame are returned.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.EventFrameApi();
let webId = "webId_example"; // String | The ID of the event frame.
let opts = {
  'nameFilter': "nameFilter_example", // String | The name query string used for filtering security entries. The default is no filter.
  'selectedFields': "selectedFields_example", // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
  'webIdType': "webIdType_example" // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
};
apiInstance.eventFrameGetSecurityEntries(webId, opts, (error, data, response) => {
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
 **webId** | **String**| The ID of the event frame. | 
 **nameFilter** | **String**| The name query string used for filtering security entries. The default is no filter. | [optional] 
 **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 
 **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] 

### Return type

[**ItemsSecurityEntry**](ItemsSecurityEntry.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/html, application/x-ms-application


## eventFrameGetSecurityEntryByName

> SecurityEntry eventFrameGetSecurityEntryByName(name, webId, opts)

Retrieve the security entry associated with the event frame with the specified name.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.EventFrameApi();
let name = "name_example"; // String | The name of the security entry. For every backslash character (\\) in the security entry name, replace with asterisk (*). As an example, use domain*username instead of domain\\username.
let webId = "webId_example"; // String | The ID of the event frame.
let opts = {
  'selectedFields': "selectedFields_example", // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
  'webIdType': "webIdType_example" // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
};
apiInstance.eventFrameGetSecurityEntryByName(name, webId, opts, (error, data, response) => {
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
 **name** | **String**| The name of the security entry. For every backslash character (\\) in the security entry name, replace with asterisk (*). As an example, use domain*username instead of domain\\username. | 
 **webId** | **String**| The ID of the event frame. | 
 **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 
 **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] 

### Return type

[**SecurityEntry**](SecurityEntry.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/html, application/x-ms-application


## eventFrameUpdate

> eventFrameUpdate(webId, eventFrame)

Update an event frame by replacing items in its definition.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.EventFrameApi();
let webId = "webId_example"; // String | The ID of the event frame to update.
let eventFrame = new PiWebApi2018Sp1SwaggerSpec.EventFrame(); // EventFrame | A partial event frame containing the desired changes.
apiInstance.eventFrameUpdate(webId, eventFrame, (error, data, response) => {
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
 **webId** | **String**| The ID of the event frame to update. | 
 **eventFrame** | [**EventFrame**](EventFrame.md)| A partial event frame containing the desired changes. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: Not defined


## eventFrameUpdateAnnotation

> eventFrameUpdateAnnotation(id, webId, annotation)

Update an annotation on an event frame by replacing items in its definition.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.EventFrameApi();
let id = "id_example"; // String | The Annotation identifier of the annotation to be updated.
let webId = "webId_example"; // String | The ID of the owner event frame of the annotation to update.
let annotation = new PiWebApi2018Sp1SwaggerSpec.Annotation(); // Annotation | A partial annotation containing the desired changes.
apiInstance.eventFrameUpdateAnnotation(id, webId, annotation, (error, data, response) => {
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
 **id** | **String**| The Annotation identifier of the annotation to be updated. | 
 **webId** | **String**| The ID of the owner event frame of the annotation to update. | 
 **annotation** | [**Annotation**](Annotation.md)| A partial annotation containing the desired changes. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: Not defined


## eventFrameUpdateSecurityEntry

> eventFrameUpdateSecurityEntry(name, webId, securityEntry, opts)

Update a security entry owned by the event frame.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.EventFrameApi();
let name = "name_example"; // String | The name of the security entry.
let webId = "webId_example"; // String | The ID of the event frame where the security entry will be updated.
let securityEntry = new PiWebApi2018Sp1SwaggerSpec.SecurityEntry(); // SecurityEntry | The new security entry definition. The full list of allow and deny rights must be supplied or they will be removed.
let opts = {
  'applyToChildren': true // Boolean | If false, the new access permissions are only applied to the associated object. If true, the access permissions of children with any parent-child reference types will change when the permissions on the primary parent change.
};
apiInstance.eventFrameUpdateSecurityEntry(name, webId, securityEntry, opts, (error, data, response) => {
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
 **name** | **String**| The name of the security entry. | 
 **webId** | **String**| The ID of the event frame where the security entry will be updated. | 
 **securityEntry** | [**SecurityEntry**](SecurityEntry.md)| The new security entry definition. The full list of allow and deny rights must be supplied or they will be removed. | 
 **applyToChildren** | **Boolean**| If false, the new access permissions are only applied to the associated object. If true, the access permissions of children with any parent-child reference types will change when the permissions on the primary parent change. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: Not defined

