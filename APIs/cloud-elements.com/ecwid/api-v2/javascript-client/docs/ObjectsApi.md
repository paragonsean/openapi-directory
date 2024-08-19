# Ecwid.ObjectsApi

All URIs are relative to *https://api.cloud-elements.com/elements/api-v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getObjects**](ObjectsApi.md#getObjects) | **GET** /objects | Get a list of all the available objects.
[**getObjectsObjectNameDocs**](ObjectsApi.md#getObjectsObjectNameDocs) | **GET** /objects/{objectName}/docs | Get swagger docs for an object.
[**getObjectsObjectNameMetadata**](ObjectsApi.md#getObjectsObjectNameMetadata) | **GET** /objects/{objectName}/metadata | Get a list of all the field for an object.



## getObjects

> [String] getObjects(authorization, opts)

Get a list of all the available objects.

### Example

```javascript
import Ecwid from 'ecwid';

let apiInstance = new Ecwid.ObjectsApi();
let authorization = "authorization_example"; // String | The authorization tokens. The format for the header value is 'Element &lt;token&gt;, User &lt;user secret&gt;'
let opts = {
  'elementsVersion': "elementsVersion_example" // String | Elements Version to be used for getting metadata, possible options are Hydrogen, Helium. Default value is Hydrogen
};
apiInstance.getObjects(authorization, opts, (error, data, response) => {
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
 **authorization** | **String**| The authorization tokens. The format for the header value is &#39;Element &amp;lt;token&amp;gt;, User &amp;lt;user secret&amp;gt;&#39; | 
 **elementsVersion** | **String**| Elements Version to be used for getting metadata, possible options are Hydrogen, Helium. Default value is Hydrogen | [optional] 

### Return type

**[String]**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getObjectsObjectNameDocs

> SwaggerDocs getObjectsObjectNameDocs(authorization, objectName, opts)

Get swagger docs for an object.

### Example

```javascript
import Ecwid from 'ecwid';

let apiInstance = new Ecwid.ObjectsApi();
let authorization = "authorization_example"; // String | The authorization tokens. The format for the header value is 'Element &lt;token&gt;, User &lt;user secret&gt;'
let objectName = "objectName_example"; // String | The name of the object
let opts = {
  'discovery': true, // Boolean | Include discovery metadata in definitions
  'resolveReferences': true, // Boolean | Optionally resolve swagger references for an inline object definition
  'basic': true, // Boolean | Include only OpenAPI / Swagger properties in definitions
  'version': "'-1'" // String | The element swagger version to get the corresponding element swagger, Passing in \"-1\" gives latest element swagger
};
apiInstance.getObjectsObjectNameDocs(authorization, objectName, opts, (error, data, response) => {
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
 **authorization** | **String**| The authorization tokens. The format for the header value is &#39;Element &amp;lt;token&amp;gt;, User &amp;lt;user secret&amp;gt;&#39; | 
 **objectName** | **String**| The name of the object | 
 **discovery** | **Boolean**| Include discovery metadata in definitions | [optional] 
 **resolveReferences** | **Boolean**| Optionally resolve swagger references for an inline object definition | [optional] 
 **basic** | **Boolean**| Include only OpenAPI / Swagger properties in definitions | [optional] 
 **version** | **String**| The element swagger version to get the corresponding element swagger, Passing in \&quot;-1\&quot; gives latest element swagger | [optional] [default to &#39;-1&#39;]

### Return type

[**SwaggerDocs**](SwaggerDocs.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getObjectsObjectNameMetadata

> ObjectsMetadata getObjectsObjectNameMetadata(authorization, objectName, opts)

Get a list of all the field for an object.

### Example

```javascript
import Ecwid from 'ecwid';

let apiInstance = new Ecwid.ObjectsApi();
let authorization = "authorization_example"; // String | The authorization tokens. The format for the header value is 'Element &lt;token&gt;, User &lt;user secret&gt;'
let objectName = "objectName_example"; // String | The name of the object
let opts = {
  'elementsVersion': "elementsVersion_example" // String | Elements Version to be used for getting metadata, possible options are Hydrogen, Helium. Default value is Hydrogen
};
apiInstance.getObjectsObjectNameMetadata(authorization, objectName, opts, (error, data, response) => {
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
 **authorization** | **String**| The authorization tokens. The format for the header value is &#39;Element &amp;lt;token&amp;gt;, User &amp;lt;user secret&amp;gt;&#39; | 
 **objectName** | **String**| The name of the object | 
 **elementsVersion** | **String**| Elements Version to be used for getting metadata, possible options are Hydrogen, Helium. Default value is Hydrogen | [optional] 

### Return type

[**ObjectsMetadata**](ObjectsMetadata.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

