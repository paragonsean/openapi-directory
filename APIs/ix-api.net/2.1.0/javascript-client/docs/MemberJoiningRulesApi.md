# IxApi.MemberJoiningRulesApi

All URIs are relative to */api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**memberJoiningRulesCreate**](MemberJoiningRulesApi.md#memberJoiningRulesCreate) | **POST** /member-joining-rules | 
[**memberJoiningRulesDestroy**](MemberJoiningRulesApi.md#memberJoiningRulesDestroy) | **DELETE** /member-joining-rules/{id} | 
[**memberJoiningRulesList**](MemberJoiningRulesApi.md#memberJoiningRulesList) | **GET** /member-joining-rules | 
[**memberJoiningRulesPartialUpdate**](MemberJoiningRulesApi.md#memberJoiningRulesPartialUpdate) | **PATCH** /member-joining-rules/{id} | 
[**memberJoiningRulesRead**](MemberJoiningRulesApi.md#memberJoiningRulesRead) | **GET** /member-joining-rules/{id} | 
[**memberJoiningRulesUpdate**](MemberJoiningRulesApi.md#memberJoiningRulesUpdate) | **PUT** /member-joining-rules/{id} | 



## memberJoiningRulesCreate

> MemberJoiningRule memberJoiningRulesCreate(opts)



Create a member joining rule

### Example

```javascript
import IxApi from 'ix_api';
let defaultClient = IxApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IxApi.MemberJoiningRulesApi();
let opts = {
  'memberJoiningRuleRequest': new IxApi.MemberJoiningRuleRequest() // MemberJoiningRuleRequest | Polymorphic Member Joining Rule Request
};
apiInstance.memberJoiningRulesCreate(opts, (error, data, response) => {
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
 **memberJoiningRuleRequest** | [**MemberJoiningRuleRequest**](MemberJoiningRuleRequest.md)| Polymorphic Member Joining Rule Request | [optional] 

### Return type

[**MemberJoiningRule**](MemberJoiningRule.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## memberJoiningRulesDestroy

> MemberJoiningRule memberJoiningRulesDestroy(id)



Delete a joining rule

### Example

```javascript
import IxApi from 'ix_api';
let defaultClient = IxApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IxApi.MemberJoiningRulesApi();
let id = "id_example"; // String | Get by id
apiInstance.memberJoiningRulesDestroy(id, (error, data, response) => {
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
 **id** | **String**| Get by id | 

### Return type

[**MemberJoiningRule**](MemberJoiningRule.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## memberJoiningRulesList

> [MemberJoiningRule] memberJoiningRulesList(opts)



Get a list of joining rules

### Example

```javascript
import IxApi from 'ix_api';
let defaultClient = IxApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IxApi.MemberJoiningRulesApi();
let opts = {
  'id': ["null"], // [String] | Filter by id
  'networkService': "networkService_example" // String | Filter by network_service
};
apiInstance.memberJoiningRulesList(opts, (error, data, response) => {
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
 **id** | [**[String]**](String.md)| Filter by id | [optional] 
 **networkService** | **String**| Filter by network_service | [optional] 

### Return type

[**[MemberJoiningRule]**](MemberJoiningRule.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## memberJoiningRulesPartialUpdate

> MemberJoiningRule memberJoiningRulesPartialUpdate(id, opts)



Partially update a joining rule

### Example

```javascript
import IxApi from 'ix_api';
let defaultClient = IxApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IxApi.MemberJoiningRulesApi();
let id = "id_example"; // String | Get by id
let opts = {
  'memberJoiningRuleUpdatePartial': new IxApi.MemberJoiningRuleUpdatePartial() // MemberJoiningRuleUpdatePartial | Polymorphic Member Joining Rule Update
};
apiInstance.memberJoiningRulesPartialUpdate(id, opts, (error, data, response) => {
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
 **id** | **String**| Get by id | 
 **memberJoiningRuleUpdatePartial** | [**MemberJoiningRuleUpdatePartial**](MemberJoiningRuleUpdatePartial.md)| Polymorphic Member Joining Rule Update | [optional] 

### Return type

[**MemberJoiningRule**](MemberJoiningRule.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/merge-patch+json
- **Accept**: application/json


## memberJoiningRulesRead

> MemberJoiningRule memberJoiningRulesRead(id)



Get a single rule

### Example

```javascript
import IxApi from 'ix_api';
let defaultClient = IxApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IxApi.MemberJoiningRulesApi();
let id = "id_example"; // String | Get by id
apiInstance.memberJoiningRulesRead(id, (error, data, response) => {
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
 **id** | **String**| Get by id | 

### Return type

[**MemberJoiningRule**](MemberJoiningRule.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## memberJoiningRulesUpdate

> MemberJoiningRule memberJoiningRulesUpdate(id, opts)



Update a joining rule

### Example

```javascript
import IxApi from 'ix_api';
let defaultClient = IxApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IxApi.MemberJoiningRulesApi();
let id = "id_example"; // String | Get by id
let opts = {
  'memberJoiningRuleUpdate': new IxApi.MemberJoiningRuleUpdate() // MemberJoiningRuleUpdate | Polymorphic Member Joining Rule Update
};
apiInstance.memberJoiningRulesUpdate(id, opts, (error, data, response) => {
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
 **id** | **String**| Get by id | 
 **memberJoiningRuleUpdate** | [**MemberJoiningRuleUpdate**](MemberJoiningRuleUpdate.md)| Polymorphic Member Joining Rule Update | [optional] 

### Return type

[**MemberJoiningRule**](MemberJoiningRule.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

