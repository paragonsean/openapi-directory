# GitHubV3RestApi.GitignoreApi

All URIs are relative to *https://github.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**gitignoreGetAllTemplates**](GitignoreApi.md#gitignoreGetAllTemplates) | **GET** /gitignore/templates | Get all gitignore templates
[**gitignoreGetTemplate**](GitignoreApi.md#gitignoreGetTemplate) | **GET** /gitignore/templates/{name} | Get a gitignore template



## gitignoreGetAllTemplates

> [String] gitignoreGetAllTemplates()

Get all gitignore templates

List all templates available to pass as an option when [creating a repository](https://docs.github.com/enterprise-server@3.2/rest/reference/repos#create-a-repository-for-the-authenticated-user).

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.GitignoreApi();
apiInstance.gitignoreGetAllTemplates((error, data, response) => {
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

**[String]**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## gitignoreGetTemplate

> GitignoreTemplate gitignoreGetTemplate(name)

Get a gitignore template

The API also allows fetching the source of a single template. Use the raw [media type](https://docs.github.com/enterprise-server@3.2/rest/overview/media-types/) to get the raw contents.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.GitignoreApi();
let name = "name_example"; // String | 
apiInstance.gitignoreGetTemplate(name, (error, data, response) => {
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
 **name** | **String**|  | 

### Return type

[**GitignoreTemplate**](GitignoreTemplate.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

