# DiscoveryMarketResearch.NaicsApi

All URIs are relative to *https://discovery.gsa.gov*

Method | HTTP request | Description
------------- | ------------- | -------------
[**listNaicsGET**](NaicsApi.md#listNaicsGET) | **GET** /api/naics/ | This endpoint lists all of the NAICS codes that are relevant to the OASIS family of vehicles



## listNaicsGET

> Object listNaicsGET()

This endpoint lists all of the NAICS codes that are relevant to the OASIS family of vehicles

&lt;p&gt;This endpoint lists all of the NAICS codes that are relevant to the OASIS family of vehicles. It takes no parameters.&lt;/p&gt;

### Example

```javascript
import DiscoveryMarketResearch from 'discovery_market_research';

let apiInstance = new DiscoveryMarketResearch.NaicsApi();
apiInstance.listNaicsGET((error, data, response) => {
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

