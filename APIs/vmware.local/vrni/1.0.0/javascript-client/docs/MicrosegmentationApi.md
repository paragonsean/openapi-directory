# VRealizeNetworkInsightApiReference.MicrosegmentationApi

All URIs are relative to *http://vmware.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**exportNsxRecommendedRules**](MicrosegmentationApi.md#exportNsxRecommendedRules) | **POST** /micro-seg/recommended-rules/nsx | Export recommended rules for NSX-V
[**listRecommendedRules**](MicrosegmentationApi.md#listRecommendedRules) | **POST** /micro-seg/recommended-rules | Get logical recommended rules



## exportNsxRecommendedRules

> File exportNsxRecommendedRules(opts)

Export recommended rules for NSX-V

Export recommended firewall rules based on the flow data gathered by vRealize Network Insight in NSX-V compatible format

### Example

```javascript
import VRealizeNetworkInsightApiReference from 'v_realize_network_insight_api_reference';
let defaultClient = VRealizeNetworkInsightApiReference.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new VRealizeNetworkInsightApiReference.MicrosegmentationApi();
let opts = {
  'recommendedRulesRequest': new VRealizeNetworkInsightApiReference.RecommendedRulesRequest() // RecommendedRulesRequest | NSX Recommended Rules Request
};
apiInstance.exportNsxRecommendedRules(opts, (error, data, response) => {
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
 **recommendedRulesRequest** | [**RecommendedRulesRequest**](RecommendedRulesRequest.md)| NSX Recommended Rules Request | [optional] 

### Return type

**File**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/octet-stream


## listRecommendedRules

> RecommendedRules listRecommendedRules(opts)

Get logical recommended rules

Get recommended firewall rules based on the flow data gathered by vRealize Network Insight. This API provides service to retrieve recommended rules based on flow traffic that is observed between two groups OR for a single group based on all the inbound and outboud traffic for that group. In case two groups are provided, both the groups should be of same type. Currently supported groups are Application, Tier, NSXSecurityGroup, EC2SecurityGroup.

### Example

```javascript
import VRealizeNetworkInsightApiReference from 'v_realize_network_insight_api_reference';
let defaultClient = VRealizeNetworkInsightApiReference.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new VRealizeNetworkInsightApiReference.MicrosegmentationApi();
let opts = {
  'recommendedRulesRequest': new VRealizeNetworkInsightApiReference.RecommendedRulesRequest() // RecommendedRulesRequest | Recommended Rules Request
};
apiInstance.listRecommendedRules(opts, (error, data, response) => {
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
 **recommendedRulesRequest** | [**RecommendedRulesRequest**](RecommendedRulesRequest.md)| Recommended Rules Request | [optional] 

### Return type

[**RecommendedRules**](RecommendedRules.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, results, time_range

