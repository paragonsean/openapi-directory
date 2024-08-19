# PiWebApi2018Sp1SwaggerSpec.AttributeApi

All URIs are relative to *https://devdata.osisoft.com/piwebapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**attributeCreateAttribute**](AttributeApi.md#attributeCreateAttribute) | **POST** /attributes/{webId}/attributes | Create a new attribute as a child of the specified attribute.
[**attributeCreateConfig**](AttributeApi.md#attributeCreateConfig) | **POST** /attributes/{webId}/config | Create or update an attribute&#39;s DataReference configuration (Create/Update PI point for PI Point DataReference).
[**attributeDelete**](AttributeApi.md#attributeDelete) | **DELETE** /attributes/{webId} | Delete an attribute.
[**attributeGet**](AttributeApi.md#attributeGet) | **GET** /attributes/{webId} | Retrieve an attribute.
[**attributeGetAttributes**](AttributeApi.md#attributeGetAttributes) | **GET** /attributes/{webId}/attributes | Get the child attributes of the specified attribute.
[**attributeGetAttributesQuery**](AttributeApi.md#attributeGetAttributesQuery) | **GET** /attributes/search | Retrieve attributes based on the specified conditions. Returns attributes using the specified search query string.
[**attributeGetByPath**](AttributeApi.md#attributeGetByPath) | **GET** /attributes | Retrieve an attribute by path.
[**attributeGetCategories**](AttributeApi.md#attributeGetCategories) | **GET** /attributes/{webId}/categories | Get an attribute&#39;s categories.
[**attributeGetMultiple**](AttributeApi.md#attributeGetMultiple) | **GET** /attributes/multiple | Retrieve multiple attributes by web id or path.
[**attributeGetValue**](AttributeApi.md#attributeGetValue) | **GET** /attributes/{webId}/value | Get the attribute&#39;s value. This call is intended for use with attributes that have no data reference only. For attributes with a data reference, consult the documentation for Streams.
[**attributeSetValue**](AttributeApi.md#attributeSetValue) | **PUT** /attributes/{webId}/value | Set the value of a configuration item attribute. For attributes with a data reference or non-configuration item attributes, consult the documentation for streams.
[**attributeUpdate**](AttributeApi.md#attributeUpdate) | **PATCH** /attributes/{webId} | Update an attribute by replacing items in its definition.



## attributeCreateAttribute

> attributeCreateAttribute(webId, attribute, opts)

Create a new attribute as a child of the specified attribute.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.AttributeApi();
let webId = "webId_example"; // String | The ID of the parent attribute on which to create the attribute.
let attribute = new PiWebApi2018Sp1SwaggerSpec.Attribute(); // Attribute | The definition of the new attribute.
let opts = {
  'webIdType': "webIdType_example" // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
};
apiInstance.attributeCreateAttribute(webId, attribute, opts, (error, data, response) => {
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
 **webId** | **String**| The ID of the parent attribute on which to create the attribute. | 
 **attribute** | [**Attribute**](Attribute.md)| The definition of the new attribute. | 
 **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: Not defined


## attributeCreateConfig

> attributeCreateConfig(webId, opts)

Create or update an attribute&#39;s DataReference configuration (Create/Update PI point for PI Point DataReference).

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.AttributeApi();
let webId = "webId_example"; // String | The ID of the attribute.
let opts = {
  'webIdType': "webIdType_example" // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
};
apiInstance.attributeCreateConfig(webId, opts, (error, data, response) => {
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
 **webId** | **String**| The ID of the attribute. | 
 **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## attributeDelete

> attributeDelete(webId)

Delete an attribute.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.AttributeApi();
let webId = "webId_example"; // String | The ID of the attribute.
apiInstance.attributeDelete(webId, (error, data, response) => {
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
 **webId** | **String**| The ID of the attribute. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## attributeGet

> Attribute attributeGet(webId, opts)

Retrieve an attribute.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.AttributeApi();
let webId = "webId_example"; // String | The ID of the attribute.
let opts = {
  'associations': "associations_example", // String | Associated values to return in the response, separated by semicolons (;). This call supports DataReference to return attributes with data references. If this parameter is not specified, DataReference values are not returned.
  'selectedFields': "selectedFields_example", // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
  'webIdType': "webIdType_example" // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
};
apiInstance.attributeGet(webId, opts, (error, data, response) => {
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
 **webId** | **String**| The ID of the attribute. | 
 **associations** | **String**| Associated values to return in the response, separated by semicolons (;). This call supports DataReference to return attributes with data references. If this parameter is not specified, DataReference values are not returned. | [optional] 
 **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 
 **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] 

### Return type

[**Attribute**](Attribute.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/html, application/x-ms-application


## attributeGetAttributes

> ItemsAttribute attributeGetAttributes(webId, opts)

Get the child attributes of the specified attribute.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.AttributeApi();
let webId = "webId_example"; // String | The ID of the parent attribute.
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
apiInstance.attributeGetAttributes(webId, opts, (error, data, response) => {
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
 **webId** | **String**| The ID of the parent attribute. | 
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


## attributeGetAttributesQuery

> ItemsAttribute attributeGetAttributesQuery(opts)

Retrieve attributes based on the specified conditions. Returns attributes using the specified search query string.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.AttributeApi();
let opts = {
  'associations': "associations_example", // String | Associated values to return in the response, separated by semicolons (;). This call supports DataReference to return attributes with data references. If this parameter is not specified, DataReference values are not returned.
  'databaseWebId': "databaseWebId_example", // String | The ID of the asset database to use as the root of the query.
  'maxCount': 56, // Number | The maximum number of objects to be returned per call (page size). The default is 1000.
  'query': "query_example", // String | The query string is a list of filters used to perform an AFSearch for the attributes in the asset database. An example would be: \"query=Element:{ Name:='MyElement' } Type:=Int32\".
  'selectedFields': "selectedFields_example", // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
  'startIndex': 56, // Number | The starting index (zero based) of the items to be returned. The default is 0.
  'webIdType': "webIdType_example" // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
};
apiInstance.attributeGetAttributesQuery(opts, (error, data, response) => {
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
 **associations** | **String**| Associated values to return in the response, separated by semicolons (;). This call supports DataReference to return attributes with data references. If this parameter is not specified, DataReference values are not returned. | [optional] 
 **databaseWebId** | **String**| The ID of the asset database to use as the root of the query. | [optional] 
 **maxCount** | **Number**| The maximum number of objects to be returned per call (page size). The default is 1000. | [optional] 
 **query** | **String**| The query string is a list of filters used to perform an AFSearch for the attributes in the asset database. An example would be: \&quot;query&#x3D;Element:{ Name:&#x3D;&#39;MyElement&#39; } Type:&#x3D;Int32\&quot;. | [optional] 
 **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 
 **startIndex** | **Number**| The starting index (zero based) of the items to be returned. The default is 0. | [optional] 
 **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] 

### Return type

[**ItemsAttribute**](ItemsAttribute.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/html, application/x-ms-application


## attributeGetByPath

> Attribute attributeGetByPath(path, opts)

Retrieve an attribute by path.

This method returns an attribute based on the hierarchical path associated with it, and should be used when a path has been received from a separate part of the PI System for use in the PI Web API. Users should primarily search with the WebID when available.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.AttributeApi();
let path = "path_example"; // String | The path to the attribute.
let opts = {
  'associations': "associations_example", // String | Associated values to return in the response, separated by semicolons (;). This call supports DataReference to return attributes with data references. If this parameter is not specified, DataReference values are not returned.
  'selectedFields': "selectedFields_example", // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
  'webIdType': "webIdType_example" // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
};
apiInstance.attributeGetByPath(path, opts, (error, data, response) => {
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
 **path** | **String**| The path to the attribute. | 
 **associations** | **String**| Associated values to return in the response, separated by semicolons (;). This call supports DataReference to return attributes with data references. If this parameter is not specified, DataReference values are not returned. | [optional] 
 **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 
 **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] 

### Return type

[**Attribute**](Attribute.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/html, application/x-ms-application


## attributeGetCategories

> ItemsAttributeCategory attributeGetCategories(webId, opts)

Get an attribute&#39;s categories.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.AttributeApi();
let webId = "webId_example"; // String | The ID of the attribute.
let opts = {
  'selectedFields': "selectedFields_example", // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
  'webIdType': "webIdType_example" // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
};
apiInstance.attributeGetCategories(webId, opts, (error, data, response) => {
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
 **webId** | **String**| The ID of the attribute. | 
 **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 
 **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] 

### Return type

[**ItemsAttributeCategory**](ItemsAttributeCategory.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/html, application/x-ms-application


## attributeGetMultiple

> ItemsItemAttribute attributeGetMultiple(opts)

Retrieve multiple attributes by web id or path.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.AttributeApi();
let opts = {
  'asParallel': true, // Boolean | Specifies if the retrieval processes should be run in parallel on the server. This may improve the response time for large amounts of requested attributes. The default is 'false'.
  'associations': "associations_example", // String | Associated values to return in the response, separated by semicolons (;). This call supports DataReference to return attributes with data references. If this parameter is not specified, DataReference values are not returned.
  'includeMode': "includeMode_example", // String | The include mode for the return list. The default is 'All'.
  'path': ["null"], // [String] | The path of an attribute. Multiple attributes may be specified with multiple instances of the parameter.
  'selectedFields': "selectedFields_example", // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
  'webId': ["null"], // [String] | The ID of an attribute. Multiple attributes may be specified with multiple instances of the parameter.
  'webIdType': "webIdType_example" // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
};
apiInstance.attributeGetMultiple(opts, (error, data, response) => {
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
 **associations** | **String**| Associated values to return in the response, separated by semicolons (;). This call supports DataReference to return attributes with data references. If this parameter is not specified, DataReference values are not returned. | [optional] 
 **includeMode** | **String**| The include mode for the return list. The default is &#39;All&#39;. | [optional] 
 **path** | [**[String]**](String.md)| The path of an attribute. Multiple attributes may be specified with multiple instances of the parameter. | [optional] 
 **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 
 **webId** | [**[String]**](String.md)| The ID of an attribute. Multiple attributes may be specified with multiple instances of the parameter. | [optional] 
 **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] 

### Return type

[**ItemsItemAttribute**](ItemsItemAttribute.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/html, application/x-ms-application


## attributeGetValue

> TimedValue attributeGetValue(webId, opts)

Get the attribute&#39;s value. This call is intended for use with attributes that have no data reference only. For attributes with a data reference, consult the documentation for Streams.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.AttributeApi();
let webId = "webId_example"; // String | The ID of the attribute.
let opts = {
  'selectedFields': "selectedFields_example" // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
};
apiInstance.attributeGetValue(webId, opts, (error, data, response) => {
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
 **webId** | **String**| The ID of the attribute. | 
 **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 

### Return type

[**TimedValue**](TimedValue.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/html, application/x-ms-application


## attributeSetValue

> attributeSetValue(webId, value)

Set the value of a configuration item attribute. For attributes with a data reference or non-configuration item attributes, consult the documentation for streams.

Users must be aware of the value type that the attribute takes before changing the value. If a value entered by the user does not match the value type expressed in the attribute, it will not work or it will return an error. Users should also be careful of what the value type means, for instance, if a value type accepts strings and the user enters a number, the attribute will interpret it as a string of characters and not as the integer value that the user may have wanted.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.AttributeApi();
let webId = "webId_example"; // String | The ID of the attribute.
let value = new PiWebApi2018Sp1SwaggerSpec.TimedValue(); // TimedValue | The value to write.
apiInstance.attributeSetValue(webId, value, (error, data, response) => {
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
 **webId** | **String**| The ID of the attribute. | 
 **value** | [**TimedValue**](TimedValue.md)| The value to write. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: Not defined


## attributeUpdate

> attributeUpdate(webId, attribute)

Update an attribute by replacing items in its definition.

If an attribute is based on a template, the user must make sure to update the attribute appropriately so that it does not conflict with the template&#39;s design. Once a template is applied to an attribute, it can not be changed.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.AttributeApi();
let webId = "webId_example"; // String | The ID of the attribute.
let attribute = new PiWebApi2018Sp1SwaggerSpec.Attribute(); // Attribute | A partial attribute containing the desired changes.
apiInstance.attributeUpdate(webId, attribute, (error, data, response) => {
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
 **webId** | **String**| The ID of the attribute. | 
 **attribute** | [**Attribute**](Attribute.md)| A partial attribute containing the desired changes. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: Not defined

