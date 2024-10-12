# InterzoidGetEmailInformationApi.EmailAddressInformationApi

All URIs are relative to *https://api.interzoid.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getemailinfo**](EmailAddressInformationApi.md#getemailinfo) | **GET** /getemailinfo | Gets email validation information for an email address



## getemailinfo

> Getemailinfo200Response getemailinfo(license, email)

Gets email validation information for an email address

Get email validation information and other demographics for an email address.

### Example

```javascript
import InterzoidGetEmailInformationApi from 'interzoid_get_email_information_api';

let apiInstance = new InterzoidGetEmailInformationApi.EmailAddressInformationApi();
let license = "license_example"; // String | Your Interzoid license API key. Register at www.interzoid.com/register
let email = "email_example"; // String | Email address to retrieve validation information
apiInstance.getemailinfo(license, email, (error, data, response) => {
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
 **license** | **String**| Your Interzoid license API key. Register at www.interzoid.com/register | 
 **email** | **String**| Email address to retrieve validation information | 

### Return type

[**Getemailinfo200Response**](Getemailinfo200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

