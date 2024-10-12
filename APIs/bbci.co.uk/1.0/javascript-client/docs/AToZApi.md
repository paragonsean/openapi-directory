# BbcIPlayerBusinessLayer.AToZApi

All URIs are relative to *https://ibl.api.bbci.co.uk/ibl/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getProgrammesAtoZSearch**](AToZApi.md#getProgrammesAtoZSearch) | **GET** /atoz/{letter}/programmes | Programmes by initial title character



## getProgrammesAtoZSearch

> Object getProgrammesAtoZSearch(letter, rights, page, perPage, initialChildCount, sort, sortDirection, availability)

Programmes by initial title character

Get the Programmes whose title begins with the given initial character.

### Example

```javascript
import BbcIPlayerBusinessLayer from 'bbc_i_player_business_layer';

let apiInstance = new BbcIPlayerBusinessLayer.AToZApi();
let letter = "letter_example"; // String | Letter to search by, a to z or the string '0-9'
let rights = "'web'"; // String | The rights group to limit results to.
let page = 789; // Number | The page index.
let perPage = 789; // Number | The number of results to return.
let initialChildCount = 4; // Number | The depth to return child entities.
let sort = "sort_example"; // String | The sort order of the results.
let sortDirection = "sortDirection_example"; // String | Whether to sort ascending or descending
let availability = "'available'"; // String | Whether to return all, or available programmes
apiInstance.getProgrammesAtoZSearch(letter, rights, page, perPage, initialChildCount, sort, sortDirection, availability, (error, data, response) => {
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
 **letter** | **String**| Letter to search by, a to z or the string &#39;0-9&#39; | 
 **rights** | **String**| The rights group to limit results to. | [default to &#39;web&#39;]
 **page** | **Number**| The page index. | 
 **perPage** | **Number**| The number of results to return. | 
 **initialChildCount** | **Number**| The depth to return child entities. | [default to 4]
 **sort** | **String**| The sort order of the results. | 
 **sortDirection** | **String**| Whether to sort ascending or descending | 
 **availability** | **String**| Whether to return all, or available programmes | [default to &#39;available&#39;]

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

