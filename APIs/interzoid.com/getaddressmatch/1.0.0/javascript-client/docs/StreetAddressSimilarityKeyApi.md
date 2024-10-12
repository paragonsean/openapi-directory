# InterzoidGetAddressMatchSimilarityKeyApi.StreetAddressSimilarityKeyApi

All URIs are relative to *https://api.interzoid.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getaddressmatch**](StreetAddressSimilarityKeyApi.md#getaddressmatch) | **GET** /getaddressmatch | Gets a similarity key for matching purposes for address data



## getaddressmatch

> Getaddressmatch200Response getaddressmatch(license, address)

Gets a similarity key for matching purposes for address data

Gets a similarity key for matching purposes for street address data 

### Example

```javascript
import InterzoidGetAddressMatchSimilarityKeyApi from 'interzoid_get_address_match_similarity_key_api';

let apiInstance = new InterzoidGetAddressMatchSimilarityKeyApi.StreetAddressSimilarityKeyApi();
let license = "license_example"; // String | Your Interzoid license API key. Register at www.interzoid.com/register
let address = "address_example"; // String | Address from which to generate similarity key
apiInstance.getaddressmatch(license, address, (error, data, response) => {
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
 **address** | **String**| Address from which to generate similarity key | 

### Return type

[**Getaddressmatch200Response**](Getaddressmatch200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

