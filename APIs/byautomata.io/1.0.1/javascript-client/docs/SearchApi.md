# AutomataMarketIntelligenceApi.SearchApi

All URIs are relative to *https://api.byautomata.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**searchGet**](SearchApi.md#searchGet) | **GET** /search | Send search terms to receive the most relevant companies along with text snippets.



## searchGet

> SearchGet200Response searchGet(terms, opts)

Send search terms to receive the most relevant companies along with text snippets.

### Example

```javascript
import AutomataMarketIntelligenceApi from 'automata_market_intelligence_api';

let apiInstance = new AutomataMarketIntelligenceApi.SearchApi();
let terms = null; // String | We provide information about related companies based on the search terms you provide. Separate search terms with commas. Ex. https://api.byautomata.io/search?link=cloud+computing,enterprise,security
let opts = {
  'page': '0' // String | Page number of search results. Ex. https://api.byautomata.io/search?page=0&link=cloud+computing,enterprise,security
};
apiInstance.searchGet(terms, opts, (error, data, response) => {
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
 **terms** | [**String**](.md)| We provide information about related companies based on the search terms you provide. Separate search terms with commas. Ex. https://api.byautomata.io/search?link&#x3D;cloud+computing,enterprise,security | 
 **page** | [**String**](.md)| Page number of search results. Ex. https://api.byautomata.io/search?page&#x3D;0&amp;link&#x3D;cloud+computing,enterprise,security | [optional] [default to &#39;0&#39;]

### Return type

[**SearchGet200Response**](SearchGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

