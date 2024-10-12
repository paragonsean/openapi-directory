# PaylocityApi.EmergencyContactsApi

All URIs are relative to *https://api.paylocity.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addOrUpdateEmergencyContacts**](EmergencyContactsApi.md#addOrUpdateEmergencyContacts) | **PUT** /v2/companies/{companyId}/employees/{employeeId}/emergencyContacts | Add/update emergency contacts



## addOrUpdateEmergencyContacts

> addOrUpdateEmergencyContacts(companyId, employeeId, emergencyContact)

Add/update emergency contacts

Sends new or updated employee emergency contacts directly to Web Pay.

### Example

```javascript
import PaylocityApi from 'paylocity_api';
let defaultClient = PaylocityApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: paylocity_auth
let paylocity_auth = defaultClient.authentications['paylocity_auth'];
paylocity_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PaylocityApi.EmergencyContactsApi();
let companyId = "companyId_example"; // String | Company Id
let employeeId = "employeeId_example"; // String | Employee Id
let emergencyContact = new PaylocityApi.EmergencyContact(); // EmergencyContact | Emergency Contact Model
apiInstance.addOrUpdateEmergencyContacts(companyId, employeeId, emergencyContact, (error, data, response) => {
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
 **companyId** | **String**| Company Id | 
 **employeeId** | **String**| Employee Id | 
 **emergencyContact** | [**EmergencyContact**](EmergencyContact.md)| Emergency Contact Model | 

### Return type

null (empty response body)

### Authorization

[paylocity_auth](../README.md#paylocity_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

