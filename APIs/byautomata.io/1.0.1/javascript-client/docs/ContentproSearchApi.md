# AutomataMarketIntelligenceApi.ContentproSearchApi

All URIs are relative to *https://api.byautomata.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**contentproSearchGet**](ContentproSearchApi.md#contentproSearchGet) | **GET** /contentpro-search | Send search terms to receive the most relevant articles and companies.



## contentproSearchGet

> ContentproSearchGet200Response contentproSearchGet(terms)

Send search terms to receive the most relevant articles and companies.

### Example

```javascript
import AutomataMarketIntelligenceApi from 'automata_market_intelligence_api';

let apiInstance = new AutomataMarketIntelligenceApi.ContentproSearchApi();
let terms = null; // String | We provide information about related companies and articles based on the search terms you provide. Separate search terms with commas. Ex. https://api.byautomata.io/contentpro-search?terms=cloud+computing,enterprise,security
apiInstance.contentproSearchGet(terms, (error, data, response) => {
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
 **terms** | [**String**](.md)| We provide information about related companies and articles based on the search terms you provide. Separate search terms with commas. Ex. https://api.byautomata.io/contentpro-search?terms&#x3D;cloud+computing,enterprise,security | 

### Return type

[**ContentproSearchGet200Response**](ContentproSearchGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

