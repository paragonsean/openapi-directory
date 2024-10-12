# RudderApi.ArchivesApi

All URIs are relative to *https://rudder.example.local/rudder/api/latest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**callExport**](ArchivesApi.md#callExport) | **GET** /archives/export | Get a ZIP archive of the requested items and their dependencies
[**callImport**](ArchivesApi.md#callImport) | **POST** /archives/import | Import a ZIP archive of policies into Rudder



## callExport

> File callExport(opts)

Get a ZIP archive of the requested items and their dependencies

Get a ZIP archive or rules, directives, techniques and groups with optionally their dependencies

### Example

```javascript
import RudderApi from 'rudder_api';
let defaultClient = RudderApi.ApiClient.instance;
// Configure API key authorization: API-Tokens
let API-Tokens = defaultClient.authentications['API-Tokens'];
API-Tokens.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API-Tokens.apiKeyPrefix = 'Token';

let apiInstance = new RudderApi.ArchivesApi();
let opts = {
  'rules': ["null"], // [String] | IDs (optionally with revision, '+' need to be escaped as '%2B') of rules to include
  'directives': ["null"], // [String] | IDs (optionally with revision, '+' need to be escaped as '%2B') of directives to include
  'techniques': ["null"], // [String] | IDs, ie technique name/technique version (optionally with revision, '+' need to be escaped as '%2B') of techniques to include
  'groups': ["null"], // [String] | IDs (optionally with revision, '+' need to be escaped as '%2B') of groups to include
  'include': ["null"] // [String] | Scope of dependencies to include in archive, where rule as directives and groups dependencies, directives have techniques dependencies, and techniques and groups don't have dependencies. 'none' means no dependencies will be include, 'all' means that the whole tree will,  'directives' and 'groups' means to include them specifically, 'techniques' means to include both directives and techniques.
};
apiInstance.callExport(opts, (error, data, response) => {
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
 **rules** | [**[String]**](String.md)| IDs (optionally with revision, &#39;+&#39; need to be escaped as &#39;%2B&#39;) of rules to include | [optional] 
 **directives** | [**[String]**](String.md)| IDs (optionally with revision, &#39;+&#39; need to be escaped as &#39;%2B&#39;) of directives to include | [optional] 
 **techniques** | [**[String]**](String.md)| IDs, ie technique name/technique version (optionally with revision, &#39;+&#39; need to be escaped as &#39;%2B&#39;) of techniques to include | [optional] 
 **groups** | [**[String]**](String.md)| IDs (optionally with revision, &#39;+&#39; need to be escaped as &#39;%2B&#39;) of groups to include | [optional] 
 **include** | [**[String]**](String.md)| Scope of dependencies to include in archive, where rule as directives and groups dependencies, directives have techniques dependencies, and techniques and groups don&#39;t have dependencies. &#39;none&#39; means no dependencies will be include, &#39;all&#39; means that the whole tree will,  &#39;directives&#39; and &#39;groups&#39; means to include them specifically, &#39;techniques&#39; means to include both directives and techniques. | [optional] 

### Return type

**File**

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/octet-stream


## callImport

> Import200Response callImport(opts)

Import a ZIP archive of policies into Rudder

Import a ZIP archive of techniques, directives, groups and rules in a saved in a normalized format into Rudder

### Example

```javascript
import RudderApi from 'rudder_api';
let defaultClient = RudderApi.ApiClient.instance;
// Configure API key authorization: API-Tokens
let API-Tokens = defaultClient.authentications['API-Tokens'];
API-Tokens.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API-Tokens.apiKeyPrefix = 'Token';

let apiInstance = new RudderApi.ArchivesApi();
let opts = {
  'archive': "/path/to/file", // File | The ZIP archive file containing policies in a conventional layout and serialization format
  'merge': "merge_example" // String | Optional merge algo of the import. Default `override-all` means what is in the archive is the new reality. `keep-rule-groups` will keep existing target definition for existing rules (ignore archive value).
};
apiInstance.callImport(opts, (error, data, response) => {
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
 **archive** | **File**| The ZIP archive file containing policies in a conventional layout and serialization format | [optional] 
 **merge** | **String**| Optional merge algo of the import. Default &#x60;override-all&#x60; means what is in the archive is the new reality. &#x60;keep-rule-groups&#x60; will keep existing target definition for existing rules (ignore archive value). | [optional] 

### Return type

[**Import200Response**](Import200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json

