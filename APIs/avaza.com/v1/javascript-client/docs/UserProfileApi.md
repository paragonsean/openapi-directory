# AvazaApiDocumentation.UserProfileApi

All URIs are relative to *https://api.avaza.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**userProfileGet**](UserProfileApi.md#userProfileGet) | **GET** /api/UserProfile | Get Collection of Users who have roles in the current Avaza account.



## userProfileGet

> UserList userProfileGet(opts)

Get Collection of Users who have roles in the current Avaza account.

Admin and Invoice Managers can see all. Other users are limited to seeing their own profile.

### Example

```javascript
import AvazaApiDocumentation from 'avaza_api_documentation';
let defaultClient = AvazaApiDocumentation.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AvazaApiDocumentation.UserProfileApi();
let opts = {
  'roles': "roles_example", // String | Optional list of comma separated role codes to filter users by (e.g. \"TimesheetUser,Admin\")
  'tags': "tags_example", // String | 
  'currentUserOnly': true, // Boolean | Optional boolean (true/false) to filter to only show current authenticated user (always true for non Admin/InvoiceManager users)
  'companyIDFK': 56 // Number | Optionally filter by Company ID
};
apiInstance.userProfileGet(opts, (error, data, response) => {
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
 **roles** | **String**| Optional list of comma separated role codes to filter users by (e.g. \&quot;TimesheetUser,Admin\&quot;) | [optional] 
 **tags** | **String**|  | [optional] 
 **currentUserOnly** | **Boolean**| Optional boolean (true/false) to filter to only show current authenticated user (always true for non Admin/InvoiceManager users) | [optional] 
 **companyIDFK** | **Number**| Optionally filter by Company ID | [optional] 

### Return type

[**UserList**](UserList.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml

