# Api.MembershipApi

All URIs are relative to *https://tl-api.azurewebsites.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**membershipGet**](MembershipApi.md#membershipGet) | **GET** /api/Membership | Get all of the members details This will return all properties related to member entity             
[**membershipPost**](MembershipApi.md#membershipPost) | **POST** /api/Membership | Add new Member             



## membershipGet

> [MemberDTO] membershipGet()

Get all of the members details This will return all properties related to member entity             

### Example

```javascript
import Api from 'api';
let defaultClient = Api.ApiClient.instance;
// Configure OAuth2 access token for authorization: bearer
let bearer = defaultClient.authentications['bearer'];
bearer.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Api.MembershipApi();
apiInstance.membershipGet((error, data, response) => {
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

[**[MemberDTO]**](MemberDTO.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## membershipPost

> Boolean membershipPost(memberDTO)

Add new Member             

### Example

```javascript
import Api from 'api';
let defaultClient = Api.ApiClient.instance;
// Configure OAuth2 access token for authorization: bearer
let bearer = defaultClient.authentications['bearer'];
bearer.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Api.MembershipApi();
let memberDTO = new Api.MemberDTO(); // MemberDTO | member object
apiInstance.membershipPost(memberDTO, (error, data, response) => {
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
 **memberDTO** | [**MemberDTO**](MemberDTO.md)| member object | 

### Return type

**Boolean**

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

