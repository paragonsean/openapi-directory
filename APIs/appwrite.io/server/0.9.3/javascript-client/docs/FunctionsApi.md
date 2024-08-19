# Appwrite.FunctionsApi

All URIs are relative to *https://appwrite.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**functionsCreate**](FunctionsApi.md#functionsCreate) | **POST** /functions | Create Function
[**functionsCreateExecution**](FunctionsApi.md#functionsCreateExecution) | **POST** /functions/{functionId}/executions | Create Execution
[**functionsCreateTag**](FunctionsApi.md#functionsCreateTag) | **POST** /functions/{functionId}/tags | Create Tag
[**functionsDelete**](FunctionsApi.md#functionsDelete) | **DELETE** /functions/{functionId} | Delete Function
[**functionsDeleteTag**](FunctionsApi.md#functionsDeleteTag) | **DELETE** /functions/{functionId}/tags/{tagId} | Delete Tag
[**functionsGet**](FunctionsApi.md#functionsGet) | **GET** /functions/{functionId} | Get Function
[**functionsGetExecution**](FunctionsApi.md#functionsGetExecution) | **GET** /functions/{functionId}/executions/{executionId} | Get Execution
[**functionsGetTag**](FunctionsApi.md#functionsGetTag) | **GET** /functions/{functionId}/tags/{tagId} | Get Tag
[**functionsList**](FunctionsApi.md#functionsList) | **GET** /functions | List Functions
[**functionsListExecutions**](FunctionsApi.md#functionsListExecutions) | **GET** /functions/{functionId}/executions | List Executions
[**functionsListTags**](FunctionsApi.md#functionsListTags) | **GET** /functions/{functionId}/tags | List Tags
[**functionsUpdate**](FunctionsApi.md#functionsUpdate) | **PUT** /functions/{functionId} | Update Function
[**functionsUpdateTag**](FunctionsApi.md#functionsUpdateTag) | **PATCH** /functions/{functionId}/tag | Update Function Tag



## functionsCreate

> Function functionsCreate(opts)

Create Function

Create a new function. You can pass a list of [permissions](/docs/permissions) to allow different project users or team with access to execute the function using the client API.

### Example

```javascript
import Appwrite from 'appwrite';
let defaultClient = Appwrite.ApiClient.instance;
// Configure API key authorization: Project
let Project = defaultClient.authentications['Project'];
Project.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Project.apiKeyPrefix = 'Token';
// Configure API key authorization: Key
let Key = defaultClient.authentications['Key'];
Key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Key.apiKeyPrefix = 'Token';

let apiInstance = new Appwrite.FunctionsApi();
let opts = {
  'functionsCreateRequest': new Appwrite.FunctionsCreateRequest() // FunctionsCreateRequest | 
};
apiInstance.functionsCreate(opts, (error, data, response) => {
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
 **functionsCreateRequest** | [**FunctionsCreateRequest**](FunctionsCreateRequest.md)|  | [optional] 

### Return type

[**Function**](Function.md)

### Authorization

[Project](../README.md#Project), [Key](../README.md#Key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## functionsCreateExecution

> Execution functionsCreateExecution(functionId, opts)

Create Execution

Trigger a function execution. The returned object will return you the current execution status. You can ping the &#x60;Get Execution&#x60; endpoint to get updates on the current execution status. Once this endpoint is called, your function execution process will start asynchronously.

### Example

```javascript
import Appwrite from 'appwrite';
let defaultClient = Appwrite.ApiClient.instance;
// Configure API key authorization: Project
let Project = defaultClient.authentications['Project'];
Project.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Project.apiKeyPrefix = 'Token';
// Configure API key authorization: JWT
let JWT = defaultClient.authentications['JWT'];
JWT.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//JWT.apiKeyPrefix = 'Token';
// Configure API key authorization: Key
let Key = defaultClient.authentications['Key'];
Key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Key.apiKeyPrefix = 'Token';

let apiInstance = new Appwrite.FunctionsApi();
let functionId = "functionId_example"; // String | Function unique ID.
let opts = {
  'functionsCreateExecutionRequest': new Appwrite.FunctionsCreateExecutionRequest() // FunctionsCreateExecutionRequest | 
};
apiInstance.functionsCreateExecution(functionId, opts, (error, data, response) => {
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
 **functionId** | **String**| Function unique ID. | 
 **functionsCreateExecutionRequest** | [**FunctionsCreateExecutionRequest**](FunctionsCreateExecutionRequest.md)|  | [optional] 

### Return type

[**Execution**](Execution.md)

### Authorization

[Project](../README.md#Project), [JWT](../README.md#JWT), [Key](../README.md#Key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## functionsCreateTag

> Tag functionsCreateTag(functionId, code, command)

Create Tag

Create a new function code tag. Use this endpoint to upload a new version of your code function. To execute your newly uploaded code, you&#39;ll need to update the function&#39;s tag to use your new tag UID.  This endpoint accepts a tar.gz file compressed with your code. Make sure to include any dependencies your code has within the compressed file. You can learn more about code packaging in the [Appwrite Cloud Functions tutorial](/docs/functions).  Use the \&quot;command\&quot; param to set the entry point used to execute your code.

### Example

```javascript
import Appwrite from 'appwrite';
let defaultClient = Appwrite.ApiClient.instance;
// Configure API key authorization: Project
let Project = defaultClient.authentications['Project'];
Project.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Project.apiKeyPrefix = 'Token';
// Configure API key authorization: Key
let Key = defaultClient.authentications['Key'];
Key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Key.apiKeyPrefix = 'Token';

let apiInstance = new Appwrite.FunctionsApi();
let functionId = "functionId_example"; // String | Function unique ID.
let code = "code_example"; // String | Gzip file with your code package. When used with the Appwrite CLI, pass the path to your code directory, and the CLI will automatically package your code. Use a path that is within the current directory.
let command = "command_example"; // String | Code execution command.
apiInstance.functionsCreateTag(functionId, code, command, (error, data, response) => {
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
 **functionId** | **String**| Function unique ID. | 
 **code** | **String**| Gzip file with your code package. When used with the Appwrite CLI, pass the path to your code directory, and the CLI will automatically package your code. Use a path that is within the current directory. | 
 **command** | **String**| Code execution command. | 

### Return type

[**Tag**](Tag.md)

### Authorization

[Project](../README.md#Project), [Key](../README.md#Key)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json


## functionsDelete

> functionsDelete(functionId)

Delete Function

Delete a function by its unique ID.

### Example

```javascript
import Appwrite from 'appwrite';
let defaultClient = Appwrite.ApiClient.instance;
// Configure API key authorization: Project
let Project = defaultClient.authentications['Project'];
Project.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Project.apiKeyPrefix = 'Token';
// Configure API key authorization: Key
let Key = defaultClient.authentications['Key'];
Key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Key.apiKeyPrefix = 'Token';

let apiInstance = new Appwrite.FunctionsApi();
let functionId = "functionId_example"; // String | Function unique ID.
apiInstance.functionsDelete(functionId, (error, data, response) => {
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
 **functionId** | **String**| Function unique ID. | 

### Return type

null (empty response body)

### Authorization

[Project](../README.md#Project), [Key](../README.md#Key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## functionsDeleteTag

> functionsDeleteTag(functionId, tagId)

Delete Tag

Delete a code tag by its unique ID.

### Example

```javascript
import Appwrite from 'appwrite';
let defaultClient = Appwrite.ApiClient.instance;
// Configure API key authorization: Project
let Project = defaultClient.authentications['Project'];
Project.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Project.apiKeyPrefix = 'Token';
// Configure API key authorization: Key
let Key = defaultClient.authentications['Key'];
Key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Key.apiKeyPrefix = 'Token';

let apiInstance = new Appwrite.FunctionsApi();
let functionId = "functionId_example"; // String | Function unique ID.
let tagId = "tagId_example"; // String | Tag unique ID.
apiInstance.functionsDeleteTag(functionId, tagId, (error, data, response) => {
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
 **functionId** | **String**| Function unique ID. | 
 **tagId** | **String**| Tag unique ID. | 

### Return type

null (empty response body)

### Authorization

[Project](../README.md#Project), [Key](../README.md#Key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## functionsGet

> Function functionsGet(functionId)

Get Function

Get a function by its unique ID.

### Example

```javascript
import Appwrite from 'appwrite';
let defaultClient = Appwrite.ApiClient.instance;
// Configure API key authorization: Project
let Project = defaultClient.authentications['Project'];
Project.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Project.apiKeyPrefix = 'Token';
// Configure API key authorization: Key
let Key = defaultClient.authentications['Key'];
Key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Key.apiKeyPrefix = 'Token';

let apiInstance = new Appwrite.FunctionsApi();
let functionId = "functionId_example"; // String | Function unique ID.
apiInstance.functionsGet(functionId, (error, data, response) => {
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
 **functionId** | **String**| Function unique ID. | 

### Return type

[**Function**](Function.md)

### Authorization

[Project](../README.md#Project), [Key](../README.md#Key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## functionsGetExecution

> Execution functionsGetExecution(functionId, executionId)

Get Execution

Get a function execution log by its unique ID.

### Example

```javascript
import Appwrite from 'appwrite';
let defaultClient = Appwrite.ApiClient.instance;
// Configure API key authorization: Project
let Project = defaultClient.authentications['Project'];
Project.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Project.apiKeyPrefix = 'Token';
// Configure API key authorization: JWT
let JWT = defaultClient.authentications['JWT'];
JWT.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//JWT.apiKeyPrefix = 'Token';
// Configure API key authorization: Key
let Key = defaultClient.authentications['Key'];
Key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Key.apiKeyPrefix = 'Token';

let apiInstance = new Appwrite.FunctionsApi();
let functionId = "functionId_example"; // String | Function unique ID.
let executionId = "executionId_example"; // String | Execution unique ID.
apiInstance.functionsGetExecution(functionId, executionId, (error, data, response) => {
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
 **functionId** | **String**| Function unique ID. | 
 **executionId** | **String**| Execution unique ID. | 

### Return type

[**Execution**](Execution.md)

### Authorization

[Project](../README.md#Project), [JWT](../README.md#JWT), [Key](../README.md#Key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## functionsGetTag

> Tag functionsGetTag(functionId, tagId)

Get Tag

Get a code tag by its unique ID.

### Example

```javascript
import Appwrite from 'appwrite';
let defaultClient = Appwrite.ApiClient.instance;
// Configure API key authorization: Project
let Project = defaultClient.authentications['Project'];
Project.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Project.apiKeyPrefix = 'Token';
// Configure API key authorization: Key
let Key = defaultClient.authentications['Key'];
Key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Key.apiKeyPrefix = 'Token';

let apiInstance = new Appwrite.FunctionsApi();
let functionId = "functionId_example"; // String | Function unique ID.
let tagId = "tagId_example"; // String | Tag unique ID.
apiInstance.functionsGetTag(functionId, tagId, (error, data, response) => {
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
 **functionId** | **String**| Function unique ID. | 
 **tagId** | **String**| Tag unique ID. | 

### Return type

[**Tag**](Tag.md)

### Authorization

[Project](../README.md#Project), [Key](../README.md#Key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## functionsList

> FunctionList functionsList(opts)

List Functions

Get a list of all the project&#39;s functions. You can use the query params to filter your results.

### Example

```javascript
import Appwrite from 'appwrite';
let defaultClient = Appwrite.ApiClient.instance;
// Configure API key authorization: Project
let Project = defaultClient.authentications['Project'];
Project.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Project.apiKeyPrefix = 'Token';
// Configure API key authorization: Key
let Key = defaultClient.authentications['Key'];
Key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Key.apiKeyPrefix = 'Token';

let apiInstance = new Appwrite.FunctionsApi();
let opts = {
  'search': "''", // String | Search term to filter your list results. Max length: 256 chars.
  'limit': 25, // Number | Results limit value. By default will return maximum 25 results. Maximum of 100 results allowed per request.
  'offset': 0, // Number | Results offset. The default value is 0. Use this param to manage pagination.
  'orderType': "'ASC'" // String | Order result by ASC or DESC order.
};
apiInstance.functionsList(opts, (error, data, response) => {
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
 **search** | **String**| Search term to filter your list results. Max length: 256 chars. | [optional] [default to &#39;&#39;]
 **limit** | **Number**| Results limit value. By default will return maximum 25 results. Maximum of 100 results allowed per request. | [optional] [default to 25]
 **offset** | **Number**| Results offset. The default value is 0. Use this param to manage pagination. | [optional] [default to 0]
 **orderType** | **String**| Order result by ASC or DESC order. | [optional] [default to &#39;ASC&#39;]

### Return type

[**FunctionList**](FunctionList.md)

### Authorization

[Project](../README.md#Project), [Key](../README.md#Key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## functionsListExecutions

> ExecutionList functionsListExecutions(functionId, opts)

List Executions

Get a list of all the current user function execution logs. You can use the query params to filter your results. On admin mode, this endpoint will return a list of all of the project&#39;s executions. [Learn more about different API modes](/docs/admin).

### Example

```javascript
import Appwrite from 'appwrite';
let defaultClient = Appwrite.ApiClient.instance;
// Configure API key authorization: Project
let Project = defaultClient.authentications['Project'];
Project.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Project.apiKeyPrefix = 'Token';
// Configure API key authorization: JWT
let JWT = defaultClient.authentications['JWT'];
JWT.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//JWT.apiKeyPrefix = 'Token';
// Configure API key authorization: Key
let Key = defaultClient.authentications['Key'];
Key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Key.apiKeyPrefix = 'Token';

let apiInstance = new Appwrite.FunctionsApi();
let functionId = "functionId_example"; // String | Function unique ID.
let opts = {
  'search': "''", // String | Search term to filter your list results. Max length: 256 chars.
  'limit': 25, // Number | Results limit value. By default will return maximum 25 results. Maximum of 100 results allowed per request.
  'offset': 0, // Number | Results offset. The default value is 0. Use this param to manage pagination.
  'orderType': "'ASC'" // String | Order result by ASC or DESC order.
};
apiInstance.functionsListExecutions(functionId, opts, (error, data, response) => {
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
 **functionId** | **String**| Function unique ID. | 
 **search** | **String**| Search term to filter your list results. Max length: 256 chars. | [optional] [default to &#39;&#39;]
 **limit** | **Number**| Results limit value. By default will return maximum 25 results. Maximum of 100 results allowed per request. | [optional] [default to 25]
 **offset** | **Number**| Results offset. The default value is 0. Use this param to manage pagination. | [optional] [default to 0]
 **orderType** | **String**| Order result by ASC or DESC order. | [optional] [default to &#39;ASC&#39;]

### Return type

[**ExecutionList**](ExecutionList.md)

### Authorization

[Project](../README.md#Project), [JWT](../README.md#JWT), [Key](../README.md#Key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## functionsListTags

> TagList functionsListTags(functionId, opts)

List Tags

Get a list of all the project&#39;s code tags. You can use the query params to filter your results.

### Example

```javascript
import Appwrite from 'appwrite';
let defaultClient = Appwrite.ApiClient.instance;
// Configure API key authorization: Project
let Project = defaultClient.authentications['Project'];
Project.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Project.apiKeyPrefix = 'Token';
// Configure API key authorization: Key
let Key = defaultClient.authentications['Key'];
Key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Key.apiKeyPrefix = 'Token';

let apiInstance = new Appwrite.FunctionsApi();
let functionId = "functionId_example"; // String | Function unique ID.
let opts = {
  'search': "''", // String | Search term to filter your list results. Max length: 256 chars.
  'limit': 25, // Number | Results limit value. By default will return maximum 25 results. Maximum of 100 results allowed per request.
  'offset': 0, // Number | Results offset. The default value is 0. Use this param to manage pagination.
  'orderType': "'ASC'" // String | Order result by ASC or DESC order.
};
apiInstance.functionsListTags(functionId, opts, (error, data, response) => {
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
 **functionId** | **String**| Function unique ID. | 
 **search** | **String**| Search term to filter your list results. Max length: 256 chars. | [optional] [default to &#39;&#39;]
 **limit** | **Number**| Results limit value. By default will return maximum 25 results. Maximum of 100 results allowed per request. | [optional] [default to 25]
 **offset** | **Number**| Results offset. The default value is 0. Use this param to manage pagination. | [optional] [default to 0]
 **orderType** | **String**| Order result by ASC or DESC order. | [optional] [default to &#39;ASC&#39;]

### Return type

[**TagList**](TagList.md)

### Authorization

[Project](../README.md#Project), [Key](../README.md#Key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## functionsUpdate

> Function functionsUpdate(functionId, opts)

Update Function

Update function by its unique ID.

### Example

```javascript
import Appwrite from 'appwrite';
let defaultClient = Appwrite.ApiClient.instance;
// Configure API key authorization: Project
let Project = defaultClient.authentications['Project'];
Project.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Project.apiKeyPrefix = 'Token';
// Configure API key authorization: Key
let Key = defaultClient.authentications['Key'];
Key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Key.apiKeyPrefix = 'Token';

let apiInstance = new Appwrite.FunctionsApi();
let functionId = "functionId_example"; // String | Function unique ID.
let opts = {
  'functionsUpdateRequest': new Appwrite.FunctionsUpdateRequest() // FunctionsUpdateRequest | 
};
apiInstance.functionsUpdate(functionId, opts, (error, data, response) => {
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
 **functionId** | **String**| Function unique ID. | 
 **functionsUpdateRequest** | [**FunctionsUpdateRequest**](FunctionsUpdateRequest.md)|  | [optional] 

### Return type

[**Function**](Function.md)

### Authorization

[Project](../README.md#Project), [Key](../README.md#Key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## functionsUpdateTag

> Function functionsUpdateTag(functionId, opts)

Update Function Tag

Update the function code tag ID using the unique function ID. Use this endpoint to switch the code tag that should be executed by the execution endpoint.

### Example

```javascript
import Appwrite from 'appwrite';
let defaultClient = Appwrite.ApiClient.instance;
// Configure API key authorization: Project
let Project = defaultClient.authentications['Project'];
Project.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Project.apiKeyPrefix = 'Token';
// Configure API key authorization: Key
let Key = defaultClient.authentications['Key'];
Key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Key.apiKeyPrefix = 'Token';

let apiInstance = new Appwrite.FunctionsApi();
let functionId = "functionId_example"; // String | Function unique ID.
let opts = {
  'functionsUpdateTagRequest': new Appwrite.FunctionsUpdateTagRequest() // FunctionsUpdateTagRequest | 
};
apiInstance.functionsUpdateTag(functionId, opts, (error, data, response) => {
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
 **functionId** | **String**| Function unique ID. | 
 **functionsUpdateTagRequest** | [**FunctionsUpdateTagRequest**](FunctionsUpdateTagRequest.md)|  | [optional] 

### Return type

[**Function**](Function.md)

### Authorization

[Project](../README.md#Project), [Key](../README.md#Key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

