# PiWebApi2018Sp1SwaggerSpec.AttributeCategoryApi

All URIs are relative to *https://devdata.osisoft.com/piwebapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**attributeCategoryCreateSecurityEntry**](AttributeCategoryApi.md#attributeCategoryCreateSecurityEntry) | **POST** /attributecategories/{webId}/securityentries | Create a security entry owned by the attribute category.
[**attributeCategoryDelete**](AttributeCategoryApi.md#attributeCategoryDelete) | **DELETE** /attributecategories/{webId} | Delete an attribute category.
[**attributeCategoryDeleteSecurityEntry**](AttributeCategoryApi.md#attributeCategoryDeleteSecurityEntry) | **DELETE** /attributecategories/{webId}/securityentries/{name} | Delete a security entry owned by the attribute category.
[**attributeCategoryGet**](AttributeCategoryApi.md#attributeCategoryGet) | **GET** /attributecategories/{webId} | Retrieve an attribute category.
[**attributeCategoryGetByPath**](AttributeCategoryApi.md#attributeCategoryGetByPath) | **GET** /attributecategories | Retrieve an attribute category by path.
[**attributeCategoryGetSecurity**](AttributeCategoryApi.md#attributeCategoryGetSecurity) | **GET** /attributecategories/{webId}/security | Get the security information of the specified security item associated with the attribute category for a specified user.
[**attributeCategoryGetSecurityEntries**](AttributeCategoryApi.md#attributeCategoryGetSecurityEntries) | **GET** /attributecategories/{webId}/securityentries | Retrieve the security entries associated with the attribute category based on the specified criteria. By default, all security entries for this attribute category are returned.
[**attributeCategoryGetSecurityEntryByName**](AttributeCategoryApi.md#attributeCategoryGetSecurityEntryByName) | **GET** /attributecategories/{webId}/securityentries/{name} | Retrieve the security entry associated with the attribute category with the specified name.
[**attributeCategoryUpdate**](AttributeCategoryApi.md#attributeCategoryUpdate) | **PATCH** /attributecategories/{webId} | Update an attribute category by replacing items in its definition.
[**attributeCategoryUpdateSecurityEntry**](AttributeCategoryApi.md#attributeCategoryUpdateSecurityEntry) | **PUT** /attributecategories/{webId}/securityentries/{name} | Update a security entry owned by the attribute category.



## attributeCategoryCreateSecurityEntry

> attributeCategoryCreateSecurityEntry(webId, securityEntry, opts)

Create a security entry owned by the attribute category.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.AttributeCategoryApi();
let webId = "webId_example"; // String | The ID of the attribute category where the security entry will be created.
let securityEntry = new PiWebApi2018Sp1SwaggerSpec.SecurityEntry(); // SecurityEntry | The new security entry definition. The full list of allow and deny rights must be supplied.
let opts = {
  'applyToChildren': true, // Boolean | If false, the new access permissions are only applied to the associated object. If true, the access permissions of children with any parent-child reference types will change when the permissions on the primary parent change.
  'webIdType': "webIdType_example" // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
};
apiInstance.attributeCategoryCreateSecurityEntry(webId, securityEntry, opts, (error, data, response) => {
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
 **webId** | **String**| The ID of the attribute category where the security entry will be created. | 
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


## attributeCategoryDelete

> attributeCategoryDelete(webId)

Delete an attribute category.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.AttributeCategoryApi();
let webId = "webId_example"; // String | The ID of the attribute category to delete.
apiInstance.attributeCategoryDelete(webId, (error, data, response) => {
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
 **webId** | **String**| The ID of the attribute category to delete. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## attributeCategoryDeleteSecurityEntry

> attributeCategoryDeleteSecurityEntry(name, webId, opts)

Delete a security entry owned by the attribute category.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.AttributeCategoryApi();
let name = "name_example"; // String | The name of the security entry. For every backslash character (\\) in the security entry name, replace with asterisk (*). As an example, use domain*username instead of domain\\username.
let webId = "webId_example"; // String | The ID of the attribute category where the security entry will be deleted.
let opts = {
  'applyToChildren': true // Boolean | If false, the new access permissions are only applied to the associated object. If true, the access permissions of children with any parent-child reference types will change when the permissions on the primary parent change.
};
apiInstance.attributeCategoryDeleteSecurityEntry(name, webId, opts, (error, data, response) => {
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
 **webId** | **String**| The ID of the attribute category where the security entry will be deleted. | 
 **applyToChildren** | **Boolean**| If false, the new access permissions are only applied to the associated object. If true, the access permissions of children with any parent-child reference types will change when the permissions on the primary parent change. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## attributeCategoryGet

> AttributeCategory attributeCategoryGet(webId, opts)

Retrieve an attribute category.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.AttributeCategoryApi();
let webId = "webId_example"; // String | The id of the attribute category.
let opts = {
  'selectedFields': "selectedFields_example", // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
  'webIdType': "webIdType_example" // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
};
apiInstance.attributeCategoryGet(webId, opts, (error, data, response) => {
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
 **webId** | **String**| The id of the attribute category. | 
 **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 
 **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] 

### Return type

[**AttributeCategory**](AttributeCategory.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/html, application/x-ms-application


## attributeCategoryGetByPath

> AttributeCategory attributeCategoryGetByPath(path, opts)

Retrieve an attribute category by path.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.AttributeCategoryApi();
let path = "path_example"; // String | The path to the target attribute category.
let opts = {
  'selectedFields': "selectedFields_example", // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
  'webIdType': "webIdType_example" // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
};
apiInstance.attributeCategoryGetByPath(path, opts, (error, data, response) => {
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
 **path** | **String**| The path to the target attribute category. | 
 **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 
 **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] 

### Return type

[**AttributeCategory**](AttributeCategory.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/html, application/x-ms-application


## attributeCategoryGetSecurity

> ItemsSecurityRights attributeCategoryGetSecurity(webId, userIdentity, opts)

Get the security information of the specified security item associated with the attribute category for a specified user.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.AttributeCategoryApi();
let webId = "webId_example"; // String | The ID of the attribute category for the security to be checked.
let userIdentity = ["null"]; // [String] | The user identity for the security information to be checked. Multiple security identities may be specified with multiple instances of the parameter. If the parameter is not specified, only the current user's security rights will be returned.
let opts = {
  'forceRefresh': true, // Boolean | Indicates if the security cache should be refreshed before getting security information. The default is 'false'.
  'selectedFields': "selectedFields_example", // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
  'webIdType': "webIdType_example" // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
};
apiInstance.attributeCategoryGetSecurity(webId, userIdentity, opts, (error, data, response) => {
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
 **webId** | **String**| The ID of the attribute category for the security to be checked. | 
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


## attributeCategoryGetSecurityEntries

> ItemsSecurityEntry attributeCategoryGetSecurityEntries(webId, opts)

Retrieve the security entries associated with the attribute category based on the specified criteria. By default, all security entries for this attribute category are returned.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.AttributeCategoryApi();
let webId = "webId_example"; // String | The ID of the attribute category.
let opts = {
  'nameFilter': "nameFilter_example", // String | The name query string used for filtering security entries. The default is no filter.
  'selectedFields': "selectedFields_example", // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
  'webIdType': "webIdType_example" // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
};
apiInstance.attributeCategoryGetSecurityEntries(webId, opts, (error, data, response) => {
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
 **webId** | **String**| The ID of the attribute category. | 
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


## attributeCategoryGetSecurityEntryByName

> SecurityEntry attributeCategoryGetSecurityEntryByName(name, webId, opts)

Retrieve the security entry associated with the attribute category with the specified name.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.AttributeCategoryApi();
let name = "name_example"; // String | The name of the security entry. For every backslash character (\\) in the security entry name, replace with asterisk (*). As an example, use domain*username instead of domain\\username.
let webId = "webId_example"; // String | The ID of the attribute category.
let opts = {
  'selectedFields': "selectedFields_example", // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
  'webIdType': "webIdType_example" // String | Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \"WebIDType\".
};
apiInstance.attributeCategoryGetSecurityEntryByName(name, webId, opts, (error, data, response) => {
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
 **webId** | **String**| The ID of the attribute category. | 
 **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 
 **webIdType** | **String**| Optional parameter. Used to specify the type of WebID. Useful for URL brevity and other special cases. Default is the value of the configuration item \&quot;WebIDType\&quot;. | [optional] 

### Return type

[**SecurityEntry**](SecurityEntry.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/html, application/x-ms-application


## attributeCategoryUpdate

> attributeCategoryUpdate(webId, category)

Update an attribute category by replacing items in its definition.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.AttributeCategoryApi();
let webId = "webId_example"; // String | The ID of the attribute category to update.
let category = new PiWebApi2018Sp1SwaggerSpec.AttributeCategory(); // AttributeCategory | A partial attribute category containing the desired changes.
apiInstance.attributeCategoryUpdate(webId, category, (error, data, response) => {
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
 **webId** | **String**| The ID of the attribute category to update. | 
 **category** | [**AttributeCategory**](AttributeCategory.md)| A partial attribute category containing the desired changes. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: Not defined


## attributeCategoryUpdateSecurityEntry

> attributeCategoryUpdateSecurityEntry(name, webId, securityEntry, opts)

Update a security entry owned by the attribute category.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.AttributeCategoryApi();
let name = "name_example"; // String | The name of the security entry.
let webId = "webId_example"; // String | The ID of the attribute category where the security entry will be updated.
let securityEntry = new PiWebApi2018Sp1SwaggerSpec.SecurityEntry(); // SecurityEntry | The new security entry definition. The full list of allow and deny rights must be supplied or they will be removed.
let opts = {
  'applyToChildren': true // Boolean | If false, the new access permissions are only applied to the associated object. If true, the access permissions of children with any parent-child reference types will change when the permissions on the primary parent change.
};
apiInstance.attributeCategoryUpdateSecurityEntry(name, webId, securityEntry, opts, (error, data, response) => {
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
 **webId** | **String**| The ID of the attribute category where the security entry will be updated. | 
 **securityEntry** | [**SecurityEntry**](SecurityEntry.md)| The new security entry definition. The full list of allow and deny rights must be supplied or they will be removed. | 
 **applyToChildren** | **Boolean**| If false, the new access permissions are only applied to the associated object. If true, the access permissions of children with any parent-child reference types will change when the permissions on the primary parent change. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: Not defined

