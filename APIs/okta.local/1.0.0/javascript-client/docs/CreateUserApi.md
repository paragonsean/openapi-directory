# UsersOktaApi.CreateUserApi

All URIs are relative to *http://okta.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createUserInGroup**](CreateUserApi.md#createUserInGroup) | **POST** /api/v1/users | Create User in Group



## createUserInGroup

> createUserInGroup(opts)

Create User in Group

Create User in Group

### Example

```javascript
import UsersOktaApi from 'users__okta_api';

let apiInstance = new UsersOktaApi.CreateUserApi();
let opts = {
  'activate': "false", // String | 
  'createUserInGroupRequest': {"groupIds":["{{groupId}}"],"profile":{"email":"isaac@{{email-suffix}}","firstName":"Isaac","lastName":"Brock","login":"isaac@{{email-suffix}}"}} // CreateUserInGroupRequest | 
};
apiInstance.createUserInGroup(opts, (error, data, response) => {
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
 **activate** | **String**|  | [optional] 
 **createUserInGroupRequest** | [**CreateUserInGroupRequest**](CreateUserInGroupRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

