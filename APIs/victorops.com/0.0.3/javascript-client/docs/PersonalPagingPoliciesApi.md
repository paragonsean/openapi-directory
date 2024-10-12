# VictorOps.PersonalPagingPoliciesApi

All URIs are relative to *https://api.victorops.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiPublicV1ProfileUsernamePoliciesGet**](PersonalPagingPoliciesApi.md#apiPublicV1ProfileUsernamePoliciesGet) | **GET** /api-public/v1/profile/{username}/policies | Get the user&#39;s paging policy
[**apiPublicV1ProfileUsernamePoliciesPost**](PersonalPagingPoliciesApi.md#apiPublicV1ProfileUsernamePoliciesPost) | **POST** /api-public/v1/profile/{username}/policies | Create a paging policy step
[**apiPublicV1ProfileUsernamePoliciesStepGet**](PersonalPagingPoliciesApi.md#apiPublicV1ProfileUsernamePoliciesStepGet) | **GET** /api-public/v1/profile/{username}/policies/{step} | Get a paging policy step
[**apiPublicV1ProfileUsernamePoliciesStepPost**](PersonalPagingPoliciesApi.md#apiPublicV1ProfileUsernamePoliciesStepPost) | **POST** /api-public/v1/profile/{username}/policies/{step} | Create a rule for a paging policy step
[**apiPublicV1ProfileUsernamePoliciesStepPut**](PersonalPagingPoliciesApi.md#apiPublicV1ProfileUsernamePoliciesStepPut) | **PUT** /api-public/v1/profile/{username}/policies/{step} | Update a paging policy step
[**apiPublicV1ProfileUsernamePoliciesStepRuleDelete**](PersonalPagingPoliciesApi.md#apiPublicV1ProfileUsernamePoliciesStepRuleDelete) | **DELETE** /api-public/v1/profile/{username}/policies/{step}/{rule} | Delete a rule from a paging policy step
[**apiPublicV1ProfileUsernamePoliciesStepRuleGet**](PersonalPagingPoliciesApi.md#apiPublicV1ProfileUsernamePoliciesStepRuleGet) | **GET** /api-public/v1/profile/{username}/policies/{step}/{rule} | Get a rule from a paging policy step
[**apiPublicV1ProfileUsernamePoliciesStepRulePut**](PersonalPagingPoliciesApi.md#apiPublicV1ProfileUsernamePoliciesStepRulePut) | **PUT** /api-public/v1/profile/{username}/policies/{step}/{rule} | Update a rule for a paging policy step



## apiPublicV1ProfileUsernamePoliciesGet

> ApiPublicV1ProfileUsernamePoliciesGet200Response apiPublicV1ProfileUsernamePoliciesGet(username, xVOApiId, xVOApiKey)

Get the user&#39;s paging policy

Get all the paging policy steps for the user on the org associated with the API key  This API may be called a maximum of 60 times per minute. 

### Example

```javascript
import VictorOps from 'victor_ops';

let apiInstance = new VictorOps.PersonalPagingPoliciesApi();
let username = "username_example"; // String | Your username
let xVOApiId = "xVOApiId_example"; // String | Your API ID
let xVOApiKey = "xVOApiKey_example"; // String | Your API Key
apiInstance.apiPublicV1ProfileUsernamePoliciesGet(username, xVOApiId, xVOApiKey, (error, data, response) => {
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
 **username** | **String**| Your username | 
 **xVOApiId** | **String**| Your API ID | 
 **xVOApiKey** | **String**| Your API Key | 

### Return type

[**ApiPublicV1ProfileUsernamePoliciesGet200Response**](ApiPublicV1ProfileUsernamePoliciesGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiPublicV1ProfileUsernamePoliciesPost

> ApiPublicV1ProfileUsernamePoliciesPost200Response apiPublicV1ProfileUsernamePoliciesPost(username, xVOApiId, xVOApiKey, body)

Create a paging policy step

Create a paging policy step  This API may be called a maximum of 60 times per minute. 

### Example

```javascript
import VictorOps from 'victor_ops';

let apiInstance = new VictorOps.PersonalPagingPoliciesApi();
let username = "username_example"; // String | Your username
let xVOApiId = "xVOApiId_example"; // String | Your API ID
let xVOApiKey = "xVOApiKey_example"; // String | Your API Key
let body = new VictorOps.AddGroupPayload(); // AddGroupPayload | 
apiInstance.apiPublicV1ProfileUsernamePoliciesPost(username, xVOApiId, xVOApiKey, body, (error, data, response) => {
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
 **username** | **String**| Your username | 
 **xVOApiId** | **String**| Your API ID | 
 **xVOApiKey** | **String**| Your API Key | 
 **body** | [**AddGroupPayload**](AddGroupPayload.md)|  | 

### Return type

[**ApiPublicV1ProfileUsernamePoliciesPost200Response**](ApiPublicV1ProfileUsernamePoliciesPost200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiPublicV1ProfileUsernamePoliciesStepGet

> ApiPublicV1ProfileUsernamePoliciesPost200Response apiPublicV1ProfileUsernamePoliciesStepGet(username, step, xVOApiId, xVOApiKey)

Get a paging policy step

Get a paging policy step  This API may be called a maximum of 60 times per minute. 

### Example

```javascript
import VictorOps from 'victor_ops';

let apiInstance = new VictorOps.PersonalPagingPoliciesApi();
let username = "username_example"; // String | Your username
let step = 3.4; // Number | Paging policy step
let xVOApiId = "xVOApiId_example"; // String | Your API ID
let xVOApiKey = "xVOApiKey_example"; // String | Your API Key
apiInstance.apiPublicV1ProfileUsernamePoliciesStepGet(username, step, xVOApiId, xVOApiKey, (error, data, response) => {
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
 **username** | **String**| Your username | 
 **step** | **Number**| Paging policy step | 
 **xVOApiId** | **String**| Your API ID | 
 **xVOApiKey** | **String**| Your API Key | 

### Return type

[**ApiPublicV1ProfileUsernamePoliciesPost200Response**](ApiPublicV1ProfileUsernamePoliciesPost200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiPublicV1ProfileUsernamePoliciesStepPost

> ApiPublicV1ProfileUsernamePoliciesStepPost200Response apiPublicV1ProfileUsernamePoliciesStepPost(username, step, xVOApiId, xVOApiKey, body)

Create a rule for a paging policy step

Create a rule for a paging policy step  This API may be called a maximum of 60 times per minute. 

### Example

```javascript
import VictorOps from 'victor_ops';

let apiInstance = new VictorOps.PersonalPagingPoliciesApi();
let username = "username_example"; // String | Your username
let step = 3.4; // Number | Paging policy step
let xVOApiId = "xVOApiId_example"; // String | Your API ID
let xVOApiKey = "xVOApiKey_example"; // String | Your API Key
let body = new VictorOps.AddStepPayload(); // AddStepPayload | 
apiInstance.apiPublicV1ProfileUsernamePoliciesStepPost(username, step, xVOApiId, xVOApiKey, body, (error, data, response) => {
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
 **username** | **String**| Your username | 
 **step** | **Number**| Paging policy step | 
 **xVOApiId** | **String**| Your API ID | 
 **xVOApiKey** | **String**| Your API Key | 
 **body** | [**AddStepPayload**](AddStepPayload.md)|  | 

### Return type

[**ApiPublicV1ProfileUsernamePoliciesStepPost200Response**](ApiPublicV1ProfileUsernamePoliciesStepPost200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiPublicV1ProfileUsernamePoliciesStepPut

> ApiPublicV1ProfileUsernamePoliciesPost200Response apiPublicV1ProfileUsernamePoliciesStepPut(username, step, xVOApiId, xVOApiKey, body)

Update a paging policy step

Update a paging policy step  This API may be called a maximum of 60 times per minute. 

### Example

```javascript
import VictorOps from 'victor_ops';

let apiInstance = new VictorOps.PersonalPagingPoliciesApi();
let username = "username_example"; // String | Your username
let step = 3.4; // Number | Paging policy step
let xVOApiId = "xVOApiId_example"; // String | Your API ID
let xVOApiKey = "xVOApiKey_example"; // String | Your API Key
let body = new VictorOps.AddGroupPayload(); // AddGroupPayload | 
apiInstance.apiPublicV1ProfileUsernamePoliciesStepPut(username, step, xVOApiId, xVOApiKey, body, (error, data, response) => {
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
 **username** | **String**| Your username | 
 **step** | **Number**| Paging policy step | 
 **xVOApiId** | **String**| Your API ID | 
 **xVOApiKey** | **String**| Your API Key | 
 **body** | [**AddGroupPayload**](AddGroupPayload.md)|  | 

### Return type

[**ApiPublicV1ProfileUsernamePoliciesPost200Response**](ApiPublicV1ProfileUsernamePoliciesPost200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiPublicV1ProfileUsernamePoliciesStepRuleDelete

> ApiPublicV1ProfileUsernamePoliciesStepPost200Response apiPublicV1ProfileUsernamePoliciesStepRuleDelete(username, step, rule, xVOApiId, xVOApiKey)

Delete a rule from a paging policy step

Delete a rule from a paging policy step  This API may be called a maximum of 60 times per minute. 

### Example

```javascript
import VictorOps from 'victor_ops';

let apiInstance = new VictorOps.PersonalPagingPoliciesApi();
let username = "username_example"; // String | Your username
let step = 3.4; // Number | Paging policy step
let rule = 3.4; // Number | Rule for a paging policy step
let xVOApiId = "xVOApiId_example"; // String | Your API ID
let xVOApiKey = "xVOApiKey_example"; // String | Your API Key
apiInstance.apiPublicV1ProfileUsernamePoliciesStepRuleDelete(username, step, rule, xVOApiId, xVOApiKey, (error, data, response) => {
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
 **username** | **String**| Your username | 
 **step** | **Number**| Paging policy step | 
 **rule** | **Number**| Rule for a paging policy step | 
 **xVOApiId** | **String**| Your API ID | 
 **xVOApiKey** | **String**| Your API Key | 

### Return type

[**ApiPublicV1ProfileUsernamePoliciesStepPost200Response**](ApiPublicV1ProfileUsernamePoliciesStepPost200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiPublicV1ProfileUsernamePoliciesStepRuleGet

> ApiPublicV1ProfileUsernamePoliciesStepPost200Response apiPublicV1ProfileUsernamePoliciesStepRuleGet(username, step, rule, xVOApiId, xVOApiKey)

Get a rule from a paging policy step

Get a rule from a paging policy step  This API may be called a maximum of 60 times per minute. 

### Example

```javascript
import VictorOps from 'victor_ops';

let apiInstance = new VictorOps.PersonalPagingPoliciesApi();
let username = "username_example"; // String | Your username
let step = 3.4; // Number | Paging policy step
let rule = 3.4; // Number | Rule for a paging policy step
let xVOApiId = "xVOApiId_example"; // String | Your API ID
let xVOApiKey = "xVOApiKey_example"; // String | Your API Key
apiInstance.apiPublicV1ProfileUsernamePoliciesStepRuleGet(username, step, rule, xVOApiId, xVOApiKey, (error, data, response) => {
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
 **username** | **String**| Your username | 
 **step** | **Number**| Paging policy step | 
 **rule** | **Number**| Rule for a paging policy step | 
 **xVOApiId** | **String**| Your API ID | 
 **xVOApiKey** | **String**| Your API Key | 

### Return type

[**ApiPublicV1ProfileUsernamePoliciesStepPost200Response**](ApiPublicV1ProfileUsernamePoliciesStepPost200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiPublicV1ProfileUsernamePoliciesStepRulePut

> ApiPublicV1ProfileUsernamePoliciesStepPost200Response apiPublicV1ProfileUsernamePoliciesStepRulePut(username, step, rule, xVOApiId, xVOApiKey, body)

Update a rule for a paging policy step

Update a rule for a paging policy step  This API may be called a maximum of 60 times per minute. 

### Example

```javascript
import VictorOps from 'victor_ops';

let apiInstance = new VictorOps.PersonalPagingPoliciesApi();
let username = "username_example"; // String | Your username
let step = 3.4; // Number | Paging policy step
let rule = 3.4; // Number | Rule for a paging policy step
let xVOApiId = "xVOApiId_example"; // String | Your API ID
let xVOApiKey = "xVOApiKey_example"; // String | Your API Key
let body = new VictorOps.AddStepPayload(); // AddStepPayload | 
apiInstance.apiPublicV1ProfileUsernamePoliciesStepRulePut(username, step, rule, xVOApiId, xVOApiKey, body, (error, data, response) => {
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
 **username** | **String**| Your username | 
 **step** | **Number**| Paging policy step | 
 **rule** | **Number**| Rule for a paging policy step | 
 **xVOApiId** | **String**| Your API ID | 
 **xVOApiKey** | **String**| Your API Key | 
 **body** | [**AddStepPayload**](AddStepPayload.md)|  | 

### Return type

[**ApiPublicV1ProfileUsernamePoliciesStepPost200Response**](ApiPublicV1ProfileUsernamePoliciesStepPost200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

