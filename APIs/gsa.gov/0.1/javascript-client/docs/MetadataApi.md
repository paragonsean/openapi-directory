# DiscoveryMarketResearch.MetadataApi

All URIs are relative to *https://discovery.gsa.gov*

Method | HTTP request | Description
------------- | ------------- | -------------
[**metadataGET**](MetadataApi.md#metadataGET) | **GET** /api/metadata/ | This endpoint returns metadata for the most recent data loads of SAM and FPDS data



## metadataGET

> Object metadataGET()

This endpoint returns metadata for the most recent data loads of SAM and FPDS data

&lt;p&gt;This endpoint returns metadata for the most recent data loads of SAM and FPDS data. It takes no parameters.&lt;/p&gt;

### Example

```javascript
import DiscoveryMarketResearch from 'discovery_market_research';

let apiInstance = new DiscoveryMarketResearch.MetadataApi();
apiInstance.metadataGET((error, data, response) => {
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

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

