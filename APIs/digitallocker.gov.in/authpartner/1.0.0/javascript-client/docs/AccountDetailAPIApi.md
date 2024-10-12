# AuthorizedPartnerApiSpecification.AccountDetailAPIApi

All URIs are relative to *https://betaapi.digitallocker.gov.in/public*

Method | HTTP request | Description
------------- | ------------- | -------------
[**accountDetailAPIId**](AccountDetailAPIApi.md#accountDetailAPIId) | **GET** /oauth2/1/user | Get User Details



## accountDetailAPIId

> Sample5 accountDetailAPIId()

Get User Details

Client applications can call this API to get the DigiLocker Id, name, date of birth and gender of the account holder. An access token is required to call this API. The API will return the user details of the account with which the access token is linked. It is strongly recommended that the API can be called by client application only once after acquiring the access token. Since the user details do not change, the client application may store the values and use them when necessary than calling this API repeatedly.

### Example

```javascript
import AuthorizedPartnerApiSpecification from 'authorized_partner_api_specification';
let defaultClient = AuthorizedPartnerApiSpecification.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new AuthorizedPartnerApiSpecification.AccountDetailAPIApi();
apiInstance.accountDetailAPIId((error, data, response) => {
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

[**Sample5**](Sample5.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

