# AutomataMarketIntelligenceApi.SimilarApi

All URIs are relative to *https://api.byautomata.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**similarGet**](SimilarApi.md#similarGet) | **GET** /similar | Send a company website to receive a list of companies related to them.



## similarGet

> SimilarGet200Response similarGet(link, opts)

Send a company website to receive a list of companies related to them.

### Example

```javascript
import AutomataMarketIntelligenceApi from 'automata_market_intelligence_api';

let apiInstance = new AutomataMarketIntelligenceApi.SimilarApi();
let link = null; // String | We'll provide information about related companies based on the site you provide. If a LinkedIn page is sent, we will try to identify the company related to the page. Ex. https://api.byautomata.io/similar?link=ibm.com
let opts = {
  'page': '0' // String | Page number of search results. Ex. https://api.byautomata.io/similar?link=ibm.com&page=1
};
apiInstance.similarGet(link, opts, (error, data, response) => {
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
 **link** | [**String**](.md)| We&#39;ll provide information about related companies based on the site you provide. If a LinkedIn page is sent, we will try to identify the company related to the page. Ex. https://api.byautomata.io/similar?link&#x3D;ibm.com | 
 **page** | [**String**](.md)| Page number of search results. Ex. https://api.byautomata.io/similar?link&#x3D;ibm.com&amp;page&#x3D;1 | [optional] [default to &#39;0&#39;]

### Return type

[**SimilarGet200Response**](SimilarGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

