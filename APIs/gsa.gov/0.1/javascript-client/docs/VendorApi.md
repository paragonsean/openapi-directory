# DiscoveryMarketResearch.VendorApi

All URIs are relative to *https://discovery.gsa.gov*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getVendorGET**](VendorApi.md#getVendorGET) | **GET** /api/vendor/{duns} | This endpoint returns a single vendor by their 9 digit DUNS number



## getVendorGET

> Object getVendorGET(duns)

This endpoint returns a single vendor by their 9 digit DUNS number

&lt;p&gt;This endpoint returns a single vendor by their 9 digit DUNS number. DUNS numbers can be looked up in the &lt;a href&#x3D;\&quot;https://www.sam.gov\&quot;&gt;System for Award Management&lt;/a&gt; by vendor name.&lt;/p&gt;

### Example

```javascript
import DiscoveryMarketResearch from 'discovery_market_research';

let apiInstance = new DiscoveryMarketResearch.VendorApi();
let duns = "duns_example"; // String | a nine digit DUNS number that uniquely identifies the vendor (required)
apiInstance.getVendorGET(duns, (error, data, response) => {
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
 **duns** | **String**| a nine digit DUNS number that uniquely identifies the vendor (required) | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

