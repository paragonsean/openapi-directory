# InterzoidGetFullNameParsedMatchSimilarityKeyApi.FullNameParsedSimilarityKeyApi

All URIs are relative to *https://api.interzoid.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getfullnameparsedmatch**](FullNameParsedSimilarityKeyApi.md#getfullnameparsedmatch) | **GET** /getfullnameparsedmatch | Gets a similarity key for matching purposes for parsed full name data



## getfullnameparsedmatch

> Getfullnameparsedmatch200Response getfullnameparsedmatch(license, firstname, lastname)

Gets a similarity key for matching purposes for parsed full name data

Gets a similarity key for matching purposes for parsed full name data, where the first name and last name are split into separate fields in the source data rather than combined.

### Example

```javascript
import InterzoidGetFullNameParsedMatchSimilarityKeyApi from 'interzoid_get_full_name_parsed_match_similarity_key_api';

let apiInstance = new InterzoidGetFullNameParsedMatchSimilarityKeyApi.FullNameParsedSimilarityKeyApi();
let license = "license_example"; // String | Your Interzoid license API key. Register at www.interzoid.com/register
let firstname = "firstname_example"; // String | First name from which to generate similarity key
let lastname = "lastname_example"; // String | Last name from which to generate similarity key
apiInstance.getfullnameparsedmatch(license, firstname, lastname, (error, data, response) => {
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
 **firstname** | **String**| First name from which to generate similarity key | 
 **lastname** | **String**| Last name from which to generate similarity key | 

### Return type

[**Getfullnameparsedmatch200Response**](Getfullnameparsedmatch200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

