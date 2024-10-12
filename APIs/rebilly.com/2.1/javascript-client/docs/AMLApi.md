# RebillyRestApi.AMLApi

All URIs are relative to *https://api-sandbox.rebilly.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getAmlEntry**](AMLApi.md#getAmlEntry) | **GET** /aml | Search PEP/Sanctions/Adverse Media lists



## getAmlEntry

> [AML] getAmlEntry(firstName, lastName, opts)

Search PEP/Sanctions/Adverse Media lists

Search multiple PEP/Sanctions/Adverse Media lists with first and last name to find any blocklisted identities. Performs a fuzzy search including soundex. Not all fields are guaranteed to be filled. 

### Example

```javascript
import RebillyRestApi from 'rebilly_rest_api';
let defaultClient = RebillyRestApi.ApiClient.instance;
// Configure API key authorization: SecretApiKey
let SecretApiKey = defaultClient.authentications['SecretApiKey'];
SecretApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//SecretApiKey.apiKeyPrefix = 'Token';
// Configure Bearer (JWT) access token for authorization: JWT
let JWT = defaultClient.authentications['JWT'];
JWT.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new RebillyRestApi.AMLApi();
let firstName = "firstName_example"; // String | First name of individual to search.
let lastName = "lastName_example"; // String | Last name of individual to search.
let opts = {
  'organizationId': "organizationId_example", // String | Organization identifier in scope of which need to perform request (if not specified, the default organization will be used).
  'dob': "dob_example", // String | Date of birth in format YYYY-MM-DD.
  'country': "country_example" // String | Country of individual as an ISO Alpha-2 code.
};
apiInstance.getAmlEntry(firstName, lastName, opts, (error, data, response) => {
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
 **firstName** | **String**| First name of individual to search. | 
 **lastName** | **String**| Last name of individual to search. | 
 **organizationId** | **String**| Organization identifier in scope of which need to perform request (if not specified, the default organization will be used). | [optional] 
 **dob** | **String**| Date of birth in format YYYY-MM-DD. | [optional] 
 **country** | **String**| Country of individual as an ISO Alpha-2 code. | [optional] 

### Return type

[**[AML]**](AML.md)

### Authorization

[SecretApiKey](../README.md#SecretApiKey), [JWT](../README.md#JWT)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

