# VestorlyApi.MembersApi

All URIs are relative to *https://staging.vestorly.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createMember**](MembersApi.md#createMember) | **POST** /members | 
[**findMemberByID**](MembersApi.md#findMemberByID) | **GET** /members/{id} | 
[**findMembers**](MembersApi.md#findMembers) | **GET** /members | 
[**updateMemberByID**](MembersApi.md#updateMemberByID) | **PUT** /members/{id} | 



## createMember

> Memberresponse createMember(vestorlyAuth, member, opts)



Create a new member in the Vestorly Platform

### Example

```javascript
import VestorlyApi from 'vestorly_api';
let defaultClient = VestorlyApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VestorlyApi.MembersApi();
let vestorlyAuth = "vestorlyAuth_example"; // String | Vestorly Auth Token
let member = new VestorlyApi.Member(); // Member | Member you want to create
let opts = {
  'accessToken': "accessToken_example" // String | OAuth Token
};
apiInstance.createMember(vestorlyAuth, member, opts, (error, data, response) => {
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
 **member** | [**Member**](Member.md)| Member you want to create | 
 **accessToken** | **String**| OAuth Token | [optional] 

### Return type

[**Memberresponse**](Memberresponse.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## findMemberByID

> Memberresponse findMemberByID(id, vestorlyAuth, opts)



Returns a single member

### Example

```javascript
import VestorlyApi from 'vestorly_api';
let defaultClient = VestorlyApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VestorlyApi.MembersApi();
let id = "id_example"; // String | Mongo ID of member to fetch
let vestorlyAuth = "vestorlyAuth_example"; // String | Vestorly Auth Token
let opts = {
  'accessToken': "accessToken_example" // String | OAuth Token
};
apiInstance.findMemberByID(id, vestorlyAuth, opts, (error, data, response) => {
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
 **id** | **String**| Mongo ID of member to fetch | 
 **vestorlyAuth** | **String**| Vestorly Auth Token | 
 **accessToken** | **String**| OAuth Token | [optional] 

### Return type

[**Memberresponse**](Memberresponse.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## findMembers

> Members findMembers(vestorlyAuth, opts)



Returns all members

### Example

```javascript
import VestorlyApi from 'vestorly_api';
let defaultClient = VestorlyApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VestorlyApi.MembersApi();
let vestorlyAuth = "vestorlyAuth_example"; // String | Vestorly Auth Token
let opts = {
  'accessToken': "accessToken_example", // String | OAuth Token
  'start': 56, // Number | Skips number of members from start
  'limit': 56 // Number | Number of members to return
};
apiInstance.findMembers(vestorlyAuth, opts, (error, data, response) => {
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
 **start** | **Number**| Skips number of members from start | [optional] 
 **limit** | **Number**| Number of members to return | [optional] 

### Return type

[**Members**](Members.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## updateMemberByID

> Memberresponse updateMemberByID(id, vestorlyAuth, member, opts)



Updates a single member

### Example

```javascript
import VestorlyApi from 'vestorly_api';
let defaultClient = VestorlyApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VestorlyApi.MembersApi();
let id = "id_example"; // String | Mongo ID of member to fetch
let vestorlyAuth = "vestorlyAuth_example"; // String | Vestorly Auth Token
let member = new VestorlyApi.Member(); // Member | Member you want to update
let opts = {
  'accessToken': "accessToken_example" // String | OAuth Token
};
apiInstance.updateMemberByID(id, vestorlyAuth, member, opts, (error, data, response) => {
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
 **id** | **String**| Mongo ID of member to fetch | 
 **vestorlyAuth** | **String**| Vestorly Auth Token | 
 **member** | [**Member**](Member.md)| Member you want to update | 
 **accessToken** | **String**| OAuth Token | [optional] 

### Return type

[**Memberresponse**](Memberresponse.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

