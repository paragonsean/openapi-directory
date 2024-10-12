# VestorlyApi.GroupsApi

All URIs are relative to *https://staging.vestorly.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createGroup**](GroupsApi.md#createGroup) | **POST** /groups | 
[**deleteGroup**](GroupsApi.md#deleteGroup) | **DELETE** /groups/{id} | 
[**findGroupByID**](GroupsApi.md#findGroupByID) | **GET** /groups/{id} | 
[**findGroups**](GroupsApi.md#findGroups) | **GET** /groups | 
[**updateGroupById**](GroupsApi.md#updateGroupById) | **PUT** /groups/{id} | 



## createGroup

> Groupresponse createGroup(vestorlyAuth, group, opts)



Creates a new Group

### Example

```javascript
import VestorlyApi from 'vestorly_api';
let defaultClient = VestorlyApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VestorlyApi.GroupsApi();
let vestorlyAuth = "vestorlyAuth_example"; // String | Vestorly Auth Token
let group = new VestorlyApi.GroupInput(); // GroupInput | Group to add
let opts = {
  'accessToken': "accessToken_example" // String | OAuth Token
};
apiInstance.createGroup(vestorlyAuth, group, opts, (error, data, response) => {
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
 **vestorlyAuth** | **String**| Vestorly Auth Token | 
 **group** | [**GroupInput**](GroupInput.md)| Group to add | 
 **accessToken** | **String**| OAuth Token | [optional] 

### Return type

[**Groupresponse**](Groupresponse.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteGroup

> Groupresponse deleteGroup(vestorlyAuth, id, opts)



Deletes a Group

### Example

```javascript
import VestorlyApi from 'vestorly_api';
let defaultClient = VestorlyApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VestorlyApi.GroupsApi();
let vestorlyAuth = "vestorlyAuth_example"; // String | Vestorly Auth Token
let id = "id_example"; // String | id of group to delete
let opts = {
  'accessToken': "accessToken_example" // String | OAuth Token
};
apiInstance.deleteGroup(vestorlyAuth, id, opts, (error, data, response) => {
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
 **vestorlyAuth** | **String**| Vestorly Auth Token | 
 **id** | **String**| id of group to delete | 
 **accessToken** | **String**| OAuth Token | [optional] 

### Return type

[**Groupresponse**](Groupresponse.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## findGroupByID

> Groupresponse findGroupByID(vestorlyAuth, id, opts)



Returns a single group if user has access

### Example

```javascript
import VestorlyApi from 'vestorly_api';
let defaultClient = VestorlyApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VestorlyApi.GroupsApi();
let vestorlyAuth = "vestorlyAuth_example"; // String | Vestorly Auth Token
let id = "id_example"; // String | Mongo ID of group to fetch
let opts = {
  'accessToken': "accessToken_example" // String | OAuth Token
};
apiInstance.findGroupByID(vestorlyAuth, id, opts, (error, data, response) => {
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
 **vestorlyAuth** | **String**| Vestorly Auth Token | 
 **id** | **String**| Mongo ID of group to fetch | 
 **accessToken** | **String**| OAuth Token | [optional] 

### Return type

[**Groupresponse**](Groupresponse.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## findGroups

> Groups findGroups(vestorlyAuth, opts)



Returns all groups

### Example

```javascript
import VestorlyApi from 'vestorly_api';
let defaultClient = VestorlyApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VestorlyApi.GroupsApi();
let vestorlyAuth = "vestorlyAuth_example"; // String | Vestorly Auth Token
let opts = {
  'accessToken': "accessToken_example" // String | OAuth Token
};
apiInstance.findGroups(vestorlyAuth, opts, (error, data, response) => {
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
 **vestorlyAuth** | **String**| Vestorly Auth Token | 
 **accessToken** | **String**| OAuth Token | [optional] 

### Return type

[**Groups**](Groups.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## updateGroupById

> Groupresponse updateGroupById(vestorlyAuth, id, group, opts)



Updates a Group

### Example

```javascript
import VestorlyApi from 'vestorly_api';
let defaultClient = VestorlyApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VestorlyApi.GroupsApi();
let vestorlyAuth = "vestorlyAuth_example"; // String | Vestorly Auth Token
let id = "id_example"; // String | id of group to update
let group = new VestorlyApi.GroupInput(); // GroupInput | Group to update
let opts = {
  'accessToken': "accessToken_example" // String | OAuth Token
};
apiInstance.updateGroupById(vestorlyAuth, id, group, opts, (error, data, response) => {
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
 **vestorlyAuth** | **String**| Vestorly Auth Token | 
 **id** | **String**| id of group to update | 
 **group** | [**GroupInput**](GroupInput.md)| Group to update | 
 **accessToken** | **String**| OAuth Token | [optional] 

### Return type

[**Groupresponse**](Groupresponse.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

