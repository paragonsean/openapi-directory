# LhPartnerApi.PreflightApi

All URIs are relative to *https://api.lufthansa.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**autoCheckIn**](PreflightApi.md#autoCheckIn) | **PUT** /preflight/autocheckin/{ticketnumber} | Auto Check-In



## autoCheckIn

> String autoCheckIn(ticketnumber, emailAddress, accept)

Auto Check-In

Trigger an automatic check-in given a ticket number. This service is only accessible for LH privileged partners

### Example

```javascript
import LhPartnerApi from 'lh_partner_api';
let defaultClient = LhPartnerApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: auth
let auth = defaultClient.authentications['auth'];
auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LhPartnerApi.PreflightApi();
let ticketnumber = "ticketnumber_example"; // String | Ticket number
let emailAddress = "emailAddress_example"; // String | Email address
let accept = "accept_example"; // String | http header: application/json or application/xml (Acceptable values are: \"application/json\", \"application/xml\")
apiInstance.autoCheckIn(ticketnumber, emailAddress, accept, (error, data, response) => {
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
 **ticketnumber** | **String**| Ticket number | 
 **emailAddress** | **String**| Email address | 
 **accept** | **String**| http header: application/json or application/xml (Acceptable values are: \&quot;application/json\&quot;, \&quot;application/xml\&quot;) | 

### Return type

**String**

### Authorization

[auth](../README.md#auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

