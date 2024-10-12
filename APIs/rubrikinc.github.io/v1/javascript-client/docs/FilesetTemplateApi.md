# RubrikRestApi.FilesetTemplateApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createFilesetTemplate**](FilesetTemplateApi.md#createFilesetTemplate) | **POST** /fileset_template | Create a fileset template
[**deleteFilesetTemplate**](FilesetTemplateApi.md#deleteFilesetTemplate) | **DELETE** /fileset_template/{id} | Delete a fileset template
[**getFilesetTemplate**](FilesetTemplateApi.md#getFilesetTemplate) | **GET** /fileset_template/{id} | Get information for a fileset template
[**queryFilesetTemplate**](FilesetTemplateApi.md#queryFilesetTemplate) | **GET** /fileset_template | Get summary information for all fileset templates
[**updateFilesetTemplate**](FilesetTemplateApi.md#updateFilesetTemplate) | **PATCH** /fileset_template/{id} | Modify a fileset template



## createFilesetTemplate

> FilesetTemplateDetail createFilesetTemplate(filesetTemplateCreate)

Create a fileset template

Create a fileset template. The template is applied to the host.  Each template is a set of paths on the host.  A template uses full paths and wildcards to define the objects to include, exclude, and exempt from exclusion.  The **_exceptions_** value specifies paths that should not be excluded from the fileset by the **_exclude_** value.  Specify an array of full path descriptions for each property **_include_**, **_exclude_**, and **_exceptions_**.  Acceptable wildcard characters are. + **_\\*_** Single asterisk matches zero or more characters up to a path deliminator. + **_\\*\\*_** Double asterisk matches zero or more characters.  The following rules apply to path descriptions. + Accepts UTF-8 characters. + Case sensitive. + Forward slash character **_/_** is the path deliminator. + Symbolic links must point to a subset of a non symbolic link path. + Paths that do not start with **_/_** are modified to start with **_\\*\\*_/_**. + Paths that do not end with **_\\*_** are modified to end with **_/\\*\\*_**.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.FilesetTemplateApi();
let filesetTemplateCreate = new RubrikRestApi.FilesetTemplateCreate(); // FilesetTemplateCreate | Provide an object with the fileset template definition.
apiInstance.createFilesetTemplate(filesetTemplateCreate, (error, data, response) => {
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
 **filesetTemplateCreate** | [**FilesetTemplateCreate**](FilesetTemplateCreate.md)| Provide an object with the fileset template definition. | 

### Return type

[**FilesetTemplateDetail**](FilesetTemplateDetail.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteFilesetTemplate

> deleteFilesetTemplate(id, opts)

Delete a fileset template

Deletes the specfied fileset template. All associated filesets are deleted.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.FilesetTemplateApi();
let id = "id_example"; // String | ID of the fileset template to remove.
let opts = {
  'preserveSnapshots': true // Boolean | Flag to indicate whether to convert snapshots of all filesets of this template to relics or to delete them.  Default is true.
};
apiInstance.deleteFilesetTemplate(id, opts, (error, data, response) => {
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
 **id** | **String**| ID of the fileset template to remove. | 
 **preserveSnapshots** | **Boolean**| Flag to indicate whether to convert snapshots of all filesets of this template to relics or to delete them.  Default is true. | [optional] 

### Return type

null (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getFilesetTemplate

> FilesetTemplateDetail getFilesetTemplate(id)

Get information for a fileset template

Retrieve summary information for a specified fileset template.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.FilesetTemplateApi();
let id = "id_example"; // String | The ID of the fileset template.
apiInstance.getFilesetTemplate(id, (error, data, response) => {
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
 **id** | **String**| The ID of the fileset template. | 

### Return type

[**FilesetTemplateDetail**](FilesetTemplateDetail.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## queryFilesetTemplate

> FilesetTemplateDetailListResponse queryFilesetTemplate(opts)

Get summary information for all fileset templates

Retrieve summary information for all fileset templates, including: ID and name of the fileset template, fileset template creation timestamp, array of the included filepaths, array of the excluded filepaths.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.FilesetTemplateApi();
let opts = {
  'primaryClusterId': "primaryClusterId_example", // String | Filter the summary information based on the primary_cluster_id of the primary Rubrik cluster. Use **_local_** as the primary_cluster_id of the Rubrik cluster that is hosting the current REST API session.
  'operatingSystemType': "operatingSystemType_example", // String | Filter the summary information based on the operating system type of the fileset. Accepted values: 'Windows', 'UnixLike', 'ANY', 'NONE'. Use **_NONE_** to only return information for fileset templates that do not have operating system type set. Use **_ANY_** to only return information for fileset templates that have operating system type set.
  'shareType': "shareType_example", // String | Filter the summary information based on the share type where the fileset is assigned to. Accepted values: 'NFS', 'SMB', 'ANY', 'NONE'. Use **_NONE_** to only return information for fileset templates that do not have share type set. Use **_ANY_** to only return information for fileset templates that have share type set.
  'name': "name_example", // String | Retrieve fileset templates with a name matching the provided name. The search is performed as a case-insensitive infix search.
  'sortBy': "sortBy_example", // String | Specifies a comma-separated list of fileset attributes to use in sorting the fileset summary information. Performs an ASCII sort of the summary information using each specified attribute, in the order specified.  Valid attributes are: **_name_**, **_includes_**, **_excludes_**, **_exceptions_**, **_hostCount_**, **_shareType_**. Default sort_order is ascending.
  'sortOrder': "sortOrder_example" // String | Sort order, either ascending or descending.
};
apiInstance.queryFilesetTemplate(opts, (error, data, response) => {
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
 **primaryClusterId** | **String**| Filter the summary information based on the primary_cluster_id of the primary Rubrik cluster. Use **_local_** as the primary_cluster_id of the Rubrik cluster that is hosting the current REST API session. | [optional] 
 **operatingSystemType** | **String**| Filter the summary information based on the operating system type of the fileset. Accepted values: &#39;Windows&#39;, &#39;UnixLike&#39;, &#39;ANY&#39;, &#39;NONE&#39;. Use **_NONE_** to only return information for fileset templates that do not have operating system type set. Use **_ANY_** to only return information for fileset templates that have operating system type set. | [optional] 
 **shareType** | **String**| Filter the summary information based on the share type where the fileset is assigned to. Accepted values: &#39;NFS&#39;, &#39;SMB&#39;, &#39;ANY&#39;, &#39;NONE&#39;. Use **_NONE_** to only return information for fileset templates that do not have share type set. Use **_ANY_** to only return information for fileset templates that have share type set. | [optional] 
 **name** | **String**| Retrieve fileset templates with a name matching the provided name. The search is performed as a case-insensitive infix search. | [optional] 
 **sortBy** | **String**| Specifies a comma-separated list of fileset attributes to use in sorting the fileset summary information. Performs an ASCII sort of the summary information using each specified attribute, in the order specified.  Valid attributes are: **_name_**, **_includes_**, **_excludes_**, **_exceptions_**, **_hostCount_**, **_shareType_**. Default sort_order is ascending. | [optional] 
 **sortOrder** | **String**| Sort order, either ascending or descending. | [optional] 

### Return type

[**FilesetTemplateDetailListResponse**](FilesetTemplateDetailListResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateFilesetTemplate

> FilesetTemplateDetail updateFilesetTemplate(id, filesetTemplatePatch)

Modify a fileset template

Modify the values of specified fileset template.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.FilesetTemplateApi();
let id = "id_example"; // String | ID of the fileset template to update.
let filesetTemplatePatch = new RubrikRestApi.FilesetTemplatePatch(); // FilesetTemplatePatch | Provide an object with the fileset template definition.
apiInstance.updateFilesetTemplate(id, filesetTemplatePatch, (error, data, response) => {
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
 **id** | **String**| ID of the fileset template to update. | 
 **filesetTemplatePatch** | [**FilesetTemplatePatch**](FilesetTemplatePatch.md)| Provide an object with the fileset template definition. | 

### Return type

[**FilesetTemplateDetail**](FilesetTemplateDetail.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

