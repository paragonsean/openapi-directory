# OpenChannelMarketApi.DevelopersFindAndModifyDevelopersApi

All URIs are relative to *https://market.openchannel.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**developersDeveloperIdDelete**](DevelopersFindAndModifyDevelopersApi.md#developersDeveloperIdDelete) | **DELETE** /developers/{developerId} | Removes a single developer
[**developersDeveloperIdGet**](DevelopersFindAndModifyDevelopersApi.md#developersDeveloperIdGet) | **GET** /developers/{developerId} | Returns a single developer
[**developersDeveloperIdPatch**](DevelopersFindAndModifyDevelopersApi.md#developersDeveloperIdPatch) | **PATCH** /developers/{developerId} | Updates the developer fields
[**developersDeveloperIdPost**](DevelopersFindAndModifyDevelopersApi.md#developersDeveloperIdPost) | **POST** /developers/{developerId} | Updates the developer record or adds the developer if it doesn&#39;t exist
[**developersGet**](DevelopersFindAndModifyDevelopersApi.md#developersGet) | **GET** /developers | Returns a paginated list of developers



## developersDeveloperIdDelete

> developersDeveloperIdDelete(developerId)

Removes a single developer

### Example

```javascript
import OpenChannelMarketApi from 'open_channel_market_api';
let defaultClient = OpenChannelMarketApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new OpenChannelMarketApi.DevelopersFindAndModifyDevelopersApi();
let developerId = "developerId_example"; // String | The id of the developer to be removed
apiInstance.developersDeveloperIdDelete(developerId, (error, data, response) => {
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
 **developerId** | **String**| The id of the developer to be removed | 

### Return type

null (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## developersDeveloperIdGet

> Developer developersDeveloperIdGet(developerId)

Returns a single developer

### Example

```javascript
import OpenChannelMarketApi from 'open_channel_market_api';
let defaultClient = OpenChannelMarketApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new OpenChannelMarketApi.DevelopersFindAndModifyDevelopersApi();
let developerId = "developerId_example"; // String | The id of the developer to be located
apiInstance.developersDeveloperIdGet(developerId, (error, data, response) => {
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
 **developerId** | **String**| The id of the developer to be located | 

### Return type

[**Developer**](Developer.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## developersDeveloperIdPatch

> Developer developersDeveloperIdPatch(developerId, opts)

Updates the developer fields

### Example

```javascript
import OpenChannelMarketApi from 'open_channel_market_api';
let defaultClient = OpenChannelMarketApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new OpenChannelMarketApi.DevelopersFindAndModifyDevelopersApi();
let developerId = "developerId_example"; // String | The id of the developer to be located
let opts = {
  'type': "type_example", // String | The type for this developer
  'email': "email_example", // String | The developer's email
  'username': "username_example", // String | The developer's username
  'name': "name_example", // String | The developer's name
  'customData': "customData_example" // String | A custom JSON object that you can create and attach to this record
};
apiInstance.developersDeveloperIdPatch(developerId, opts, (error, data, response) => {
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
 **developerId** | **String**| The id of the developer to be located | 
 **type** | **String**| The type for this developer | [optional] 
 **email** | **String**| The developer&#39;s email | [optional] 
 **username** | **String**| The developer&#39;s username | [optional] 
 **name** | **String**| The developer&#39;s name | [optional] 
 **customData** | **String**| A custom JSON object that you can create and attach to this record | [optional] 

### Return type

[**Developer**](Developer.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## developersDeveloperIdPost

> Developer developersDeveloperIdPost(developerId, opts)

Updates the developer record or adds the developer if it doesn&#39;t exist

### Example

```javascript
import OpenChannelMarketApi from 'open_channel_market_api';
let defaultClient = OpenChannelMarketApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new OpenChannelMarketApi.DevelopersFindAndModifyDevelopersApi();
let developerId = "developerId_example"; // String | The id of the developer to be located
let opts = {
  'type': "type_example", // String | The type for this developer
  'email': "email_example", // String | The developer's email
  'username': "username_example", // String | The developer's username
  'name': "name_example", // String | The developer's name
  'customData': "customData_example" // String | A custom JSON object that you can create and attach to this record
};
apiInstance.developersDeveloperIdPost(developerId, opts, (error, data, response) => {
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
 **developerId** | **String**| The id of the developer to be located | 
 **type** | **String**| The type for this developer | [optional] 
 **email** | **String**| The developer&#39;s email | [optional] 
 **username** | **String**| The developer&#39;s username | [optional] 
 **name** | **String**| The developer&#39;s name | [optional] 
 **customData** | **String**| A custom JSON object that you can create and attach to this record | [optional] 

### Return type

[**Developer**](Developer.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## developersGet

> DeveloperPages developersGet(opts)

Returns a paginated list of developers

- Results are paginated and the default is value is 100 if no limit is provided 

### Example

```javascript
import OpenChannelMarketApi from 'open_channel_market_api';
let defaultClient = OpenChannelMarketApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new OpenChannelMarketApi.DevelopersFindAndModifyDevelopersApi();
let opts = {
  'query': "query_example", // String | A query document. Example: {'name':'John'} matches all the developers that have the name 'John'
  'sort': "sort_example", // String | A sort document. Example: {'name':1} sorts the results by name in ascending order
  'pageNumber': 56, // Number | The result set page number to be returned
  'limit': 56 // Number | The maximum number of results to return per page
};
apiInstance.developersGet(opts, (error, data, response) => {
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
 **query** | **String**| A query document. Example: {&#39;name&#39;:&#39;John&#39;} matches all the developers that have the name &#39;John&#39; | [optional] 
 **sort** | **String**| A sort document. Example: {&#39;name&#39;:1} sorts the results by name in ascending order | [optional] 
 **pageNumber** | **Number**| The result set page number to be returned | [optional] 
 **limit** | **Number**| The maximum number of results to return per page | [optional] 

### Return type

[**DeveloperPages**](DeveloperPages.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

