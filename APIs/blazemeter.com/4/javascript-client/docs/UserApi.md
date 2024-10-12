# BlazemeterApiExplorer.UserApi

All URIs are relative to *https://a.blazemeter.com/api/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activeSessions**](UserApi.md#activeSessions) | **GET** /user/active/sessions | &amp;nbsp; &lt;i class&#x3D;\&quot;fa fa-lg fa-unlock-alt\&quot;&gt;&lt;/i&gt;
[**panicTerminate**](UserApi.md#panicTerminate) | **POST** /user/active/terminate | &amp;nbsp; &lt;i class&#x3D;\&quot;fa fa-lg fa-unlock-alt\&quot;&gt;&lt;/i&gt;
[**register**](UserApi.md#register) | **POST** /user/register | Registration&amp;nbsp; &lt;i class&#x3D;\&quot;fa fa-lg fa-unlock-alt\&quot;&gt;&lt;/i&gt;
[**registerRetrieve**](UserApi.md#registerRetrieve) | **GET** /user/register | Registration&amp;nbsp; &lt;i class&#x3D;\&quot;fa fa-lg fa-unlock-alt\&quot;&gt;&lt;/i&gt;
[**retrieveCollections**](UserApi.md#retrieveCollections) | **GET** /user/collections | List organization multi-tests&amp;nbsp; &lt;i class&#x3D;\&quot;fa fa-lg fa-unlock-alt\&quot;&gt;&lt;/i&gt;
[**retrieveInvites**](UserApi.md#retrieveInvites) | **GET** /user/invites | &amp;nbsp; &lt;i class&#x3D;\&quot;fa fa-lg fa-unlock-alt\&quot;&gt;&lt;/i&gt;
[**retrieveLocations**](UserApi.md#retrieveLocations) | **GET** /user/locations | Get user available locations&amp;nbsp; &lt;i class&#x3D;\&quot;fa fa-lg fa-unlock-alt\&quot;&gt;&lt;/i&gt;
[**retrieveMasters**](UserApi.md#retrieveMasters) | **GET** /user/masters | List user private masters&amp;nbsp; &lt;i class&#x3D;\&quot;fa fa-lg fa-unlock-alt\&quot;&gt;&lt;/i&gt;
[**retrieveProjects**](UserApi.md#retrieveProjects) | **GET** /user/projects | Get user projects&amp;nbsp; &lt;i class&#x3D;\&quot;fa fa-lg fa-unlock-alt\&quot;&gt;&lt;/i&gt;
[**retrieveTests**](UserApi.md#retrieveTests) | **GET** /user/tests | List user private tests&amp;nbsp; &lt;i class&#x3D;\&quot;fa fa-lg fa-unlock-alt\&quot;&gt;&lt;/i&gt;
[**top**](UserApi.md#top) | **GET** /user/top | &amp;nbsp; &lt;i class&#x3D;\&quot;fa fa-lg fa-unlock-alt\&quot;&gt;&lt;/i&gt;
[**userPasswordPatch**](UserApi.md#userPasswordPatch) | **PATCH** /user/password | Update user name&amp;nbsp; &lt;i class&#x3D;\&quot;fa fa-lg fa-unlock-alt\&quot;&gt;&lt;/i&gt;
[**userPasswordPost**](UserApi.md#userPasswordPost) | **POST** /user/password | Update user name&amp;nbsp; &lt;i class&#x3D;\&quot;fa fa-lg fa-unlock-alt\&quot;&gt;&lt;/i&gt;
[**userPasswordPut**](UserApi.md#userPasswordPut) | **PUT** /user/password | Update user name&amp;nbsp; &lt;i class&#x3D;\&quot;fa fa-lg fa-unlock-alt\&quot;&gt;&lt;/i&gt;



## activeSessions

> Object activeSessions()

&amp;nbsp; &lt;i class&#x3D;\&quot;fa fa-lg fa-unlock-alt\&quot;&gt;&lt;/i&gt;

### Example

```javascript
import BlazemeterApiExplorer from 'blazemeter_api_explorer';
let defaultClient = BlazemeterApiExplorer.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new BlazemeterApiExplorer.UserApi();
apiInstance.activeSessions((error, data, response) => {
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

**Object**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/html, text/javascript, text/csv, text/plain


## panicTerminate

> Object panicTerminate(opts)

&amp;nbsp; &lt;i class&#x3D;\&quot;fa fa-lg fa-unlock-alt\&quot;&gt;&lt;/i&gt;

### Example

```javascript
import BlazemeterApiExplorer from 'blazemeter_api_explorer';
let defaultClient = BlazemeterApiExplorer.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new BlazemeterApiExplorer.UserApi();
let opts = {
  'blazemeterRoutingV4UserModel5': {key: null} // Object | <section class=\"body-param\"><strong>session_ids</strong> (required)<br/></section>
};
apiInstance.panicTerminate(opts, (error, data, response) => {
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
 **blazemeterRoutingV4UserModel5** | **Object**| &lt;section class&#x3D;\&quot;body-param\&quot;&gt;&lt;strong&gt;session_ids&lt;/strong&gt; (required)&lt;br/&gt;&lt;/section&gt; | [optional] 

### Return type

**Object**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json, multipart/form-data, text/csv, text/plain
- **Accept**: application/json, text/html, text/javascript, text/csv, text/plain


## register

> Object register(blazemeterRoutingV4UserModel4)

Registration&amp;nbsp; &lt;i class&#x3D;\&quot;fa fa-lg fa-unlock-alt\&quot;&gt;&lt;/i&gt;

### Example

```javascript
import BlazemeterApiExplorer from 'blazemeter_api_explorer';
let defaultClient = BlazemeterApiExplorer.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new BlazemeterApiExplorer.UserApi();
let blazemeterRoutingV4UserModel4 = {key: null}; // Object | <section class=\"body-param\"><strong>firstName</strong> (required)<br/><strong>lastName</strong> (required)<br/><strong>email</strong> (required)<br/><strong>password</strong> (required)<br/></section>
apiInstance.register(blazemeterRoutingV4UserModel4, (error, data, response) => {
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
 **blazemeterRoutingV4UserModel4** | **Object**| &lt;section class&#x3D;\&quot;body-param\&quot;&gt;&lt;strong&gt;firstName&lt;/strong&gt; (required)&lt;br/&gt;&lt;strong&gt;lastName&lt;/strong&gt; (required)&lt;br/&gt;&lt;strong&gt;email&lt;/strong&gt; (required)&lt;br/&gt;&lt;strong&gt;password&lt;/strong&gt; (required)&lt;br/&gt;&lt;/section&gt; | 

### Return type

**Object**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json, multipart/form-data, text/csv, text/plain
- **Accept**: application/json, text/html, text/javascript, text/csv, text/plain


## registerRetrieve

> Object registerRetrieve(email, password, opts)

Registration&amp;nbsp; &lt;i class&#x3D;\&quot;fa fa-lg fa-unlock-alt\&quot;&gt;&lt;/i&gt;

### Example

```javascript
import BlazemeterApiExplorer from 'blazemeter_api_explorer';
let defaultClient = BlazemeterApiExplorer.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new BlazemeterApiExplorer.UserApi();
let email = "email_example"; // String | Email address
let password = "password_example"; // String | Password
let opts = {
  'firstName': "firstName_example", // String | First name
  'lastName': "lastName_example" // String | Last name
};
apiInstance.registerRetrieve(email, password, opts, (error, data, response) => {
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
 **email** | **String**| Email address | 
 **password** | **String**| Password | 
 **firstName** | **String**| First name | [optional] 
 **lastName** | **String**| Last name | [optional] 

### Return type

**Object**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/html, text/javascript, text/csv, text/plain


## retrieveCollections

> Object retrieveCollections(opts)

List organization multi-tests&amp;nbsp; &lt;i class&#x3D;\&quot;fa fa-lg fa-unlock-alt\&quot;&gt;&lt;/i&gt;

### Example

```javascript
import BlazemeterApiExplorer from 'blazemeter_api_explorer';
let defaultClient = BlazemeterApiExplorer.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new BlazemeterApiExplorer.UserApi();
let opts = {
  'skip': "skip_example", // String | 
  'limit': "limit_example" // String | 
};
apiInstance.retrieveCollections(opts, (error, data, response) => {
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
 **skip** | **String**|  | [optional] 
 **limit** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/html, text/javascript, text/csv, text/plain


## retrieveInvites

> [String] retrieveInvites()

&amp;nbsp; &lt;i class&#x3D;\&quot;fa fa-lg fa-unlock-alt\&quot;&gt;&lt;/i&gt;

### Example

```javascript
import BlazemeterApiExplorer from 'blazemeter_api_explorer';
let defaultClient = BlazemeterApiExplorer.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new BlazemeterApiExplorer.UserApi();
apiInstance.retrieveInvites((error, data, response) => {
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

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/html, text/javascript, text/csv, text/plain


## retrieveLocations

> Object retrieveLocations()

Get user available locations&amp;nbsp; &lt;i class&#x3D;\&quot;fa fa-lg fa-unlock-alt\&quot;&gt;&lt;/i&gt;

### Example

```javascript
import BlazemeterApiExplorer from 'blazemeter_api_explorer';
let defaultClient = BlazemeterApiExplorer.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new BlazemeterApiExplorer.UserApi();
apiInstance.retrieveLocations((error, data, response) => {
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

**Object**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/html, text/javascript, text/csv, text/plain


## retrieveMasters

> Object retrieveMasters(opts)

List user private masters&amp;nbsp; &lt;i class&#x3D;\&quot;fa fa-lg fa-unlock-alt\&quot;&gt;&lt;/i&gt;

### Example

```javascript
import BlazemeterApiExplorer from 'blazemeter_api_explorer';
let defaultClient = BlazemeterApiExplorer.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new BlazemeterApiExplorer.UserApi();
let opts = {
  'skip': 789, // Number | 
  'limit': 1000 // Number | 
};
apiInstance.retrieveMasters(opts, (error, data, response) => {
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
 **skip** | **Number**|  | [optional] 
 **limit** | **Number**|  | [optional] [default to 1000]

### Return type

**Object**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/html, text/javascript, text/csv, text/plain


## retrieveProjects

> Object retrieveProjects()

Get user projects&amp;nbsp; &lt;i class&#x3D;\&quot;fa fa-lg fa-unlock-alt\&quot;&gt;&lt;/i&gt;

### Example

```javascript
import BlazemeterApiExplorer from 'blazemeter_api_explorer';
let defaultClient = BlazemeterApiExplorer.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new BlazemeterApiExplorer.UserApi();
apiInstance.retrieveProjects((error, data, response) => {
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

**Object**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/html, text/javascript, text/csv, text/plain


## retrieveTests

> Object retrieveTests(opts)

List user private tests&amp;nbsp; &lt;i class&#x3D;\&quot;fa fa-lg fa-unlock-alt\&quot;&gt;&lt;/i&gt;

### Example

```javascript
import BlazemeterApiExplorer from 'blazemeter_api_explorer';
let defaultClient = BlazemeterApiExplorer.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new BlazemeterApiExplorer.UserApi();
let opts = {
  'skip': "skip_example", // String | 
  'limit': "limit_example" // String | 
};
apiInstance.retrieveTests(opts, (error, data, response) => {
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
 **skip** | **String**|  | [optional] 
 **limit** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/html, text/javascript, text/csv, text/plain


## top

> [String] top()

&amp;nbsp; &lt;i class&#x3D;\&quot;fa fa-lg fa-unlock-alt\&quot;&gt;&lt;/i&gt;

### Example

```javascript
import BlazemeterApiExplorer from 'blazemeter_api_explorer';
let defaultClient = BlazemeterApiExplorer.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new BlazemeterApiExplorer.UserApi();
apiInstance.top((error, data, response) => {
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

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/html, text/javascript, text/csv, text/plain


## userPasswordPatch

> Object userPasswordPatch(blazemeterRoutingV4UserModel1)

Update user name&amp;nbsp; &lt;i class&#x3D;\&quot;fa fa-lg fa-unlock-alt\&quot;&gt;&lt;/i&gt;

### Example

```javascript
import BlazemeterApiExplorer from 'blazemeter_api_explorer';
let defaultClient = BlazemeterApiExplorer.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new BlazemeterApiExplorer.UserApi();
let blazemeterRoutingV4UserModel1 = {key: null}; // Object | <section class=\"body-param\"><strong>currentPassword</strong> (required)<br/><strong>newPassword</strong> (required)<br/></section>
apiInstance.userPasswordPatch(blazemeterRoutingV4UserModel1, (error, data, response) => {
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
 **blazemeterRoutingV4UserModel1** | **Object**| &lt;section class&#x3D;\&quot;body-param\&quot;&gt;&lt;strong&gt;currentPassword&lt;/strong&gt; (required)&lt;br/&gt;&lt;strong&gt;newPassword&lt;/strong&gt; (required)&lt;br/&gt;&lt;/section&gt; | 

### Return type

**Object**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json, multipart/form-data, text/csv, text/plain
- **Accept**: application/json, text/html, text/javascript, text/csv, text/plain


## userPasswordPost

> Object userPasswordPost(blazemeterRoutingV4UserModel3)

Update user name&amp;nbsp; &lt;i class&#x3D;\&quot;fa fa-lg fa-unlock-alt\&quot;&gt;&lt;/i&gt;

### Example

```javascript
import BlazemeterApiExplorer from 'blazemeter_api_explorer';
let defaultClient = BlazemeterApiExplorer.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new BlazemeterApiExplorer.UserApi();
let blazemeterRoutingV4UserModel3 = {key: null}; // Object | <section class=\"body-param\"><strong>currentPassword</strong> (required)<br/><strong>newPassword</strong> (required)<br/></section>
apiInstance.userPasswordPost(blazemeterRoutingV4UserModel3, (error, data, response) => {
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
 **blazemeterRoutingV4UserModel3** | **Object**| &lt;section class&#x3D;\&quot;body-param\&quot;&gt;&lt;strong&gt;currentPassword&lt;/strong&gt; (required)&lt;br/&gt;&lt;strong&gt;newPassword&lt;/strong&gt; (required)&lt;br/&gt;&lt;/section&gt; | 

### Return type

**Object**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json, multipart/form-data, text/csv, text/plain
- **Accept**: application/json, text/html, text/javascript, text/csv, text/plain


## userPasswordPut

> Object userPasswordPut(blazemeterRoutingV4UserModel2)

Update user name&amp;nbsp; &lt;i class&#x3D;\&quot;fa fa-lg fa-unlock-alt\&quot;&gt;&lt;/i&gt;

### Example

```javascript
import BlazemeterApiExplorer from 'blazemeter_api_explorer';
let defaultClient = BlazemeterApiExplorer.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new BlazemeterApiExplorer.UserApi();
let blazemeterRoutingV4UserModel2 = {key: null}; // Object | <section class=\"body-param\"><strong>currentPassword</strong> (required)<br/><strong>newPassword</strong> (required)<br/></section>
apiInstance.userPasswordPut(blazemeterRoutingV4UserModel2, (error, data, response) => {
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
 **blazemeterRoutingV4UserModel2** | **Object**| &lt;section class&#x3D;\&quot;body-param\&quot;&gt;&lt;strong&gt;currentPassword&lt;/strong&gt; (required)&lt;br/&gt;&lt;strong&gt;newPassword&lt;/strong&gt; (required)&lt;br/&gt;&lt;/section&gt; | 

### Return type

**Object**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json, multipart/form-data, text/csv, text/plain
- **Accept**: application/json, text/html, text/javascript, text/csv, text/plain

