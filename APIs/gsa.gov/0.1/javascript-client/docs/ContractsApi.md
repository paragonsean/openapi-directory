# DiscoveryMarketResearch.ContractsApi

All URIs are relative to *https://discovery.gsa.gov*

Method | HTTP request | Description
------------- | ------------- | -------------
[**listContractsGET**](ContractsApi.md#listContractsGET) | **GET** /api/contracts/ | This endpoint returns contract history from FPDS for a specific vendor



## listContractsGET

> Object listContractsGET(duns, opts)

This endpoint returns contract history from FPDS for a specific vendor

&lt;p&gt;This endpoint returns contract history from FPDS for a specific vendor. The vendor&#39;s DUNS number is a required parameter. You can also filter contracts by their NAICS code to find contracts relevant to a particular category.&lt;/p&gt;

### Example

```javascript
import DiscoveryMarketResearch from 'discovery_market_research';

let apiInstance = new DiscoveryMarketResearch.ContractsApi();
let duns = "duns_example"; // String | A 9-digit DUNS number that uniquely identifies a vendor (required).
let opts = {
  'naics': "naics_example", // String | a six digit NAICS code used to filter by contracts with a certain NAICS
  'sort': "sort_example", // String | a field to sort on. Choices are date, status, agency, and amount
  'direction': "direction_example", // String | The sort direction of the results. Choices are asc or desc.
  'page': "page_example" // String | the page to start on. Results are paginated in increments of 100. Begins at page=1.
};
apiInstance.listContractsGET(duns, opts, (error, data, response) => {
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
 **duns** | **String**| A 9-digit DUNS number that uniquely identifies a vendor (required). | 
 **naics** | **String**| a six digit NAICS code used to filter by contracts with a certain NAICS | [optional] 
 **sort** | **String**| a field to sort on. Choices are date, status, agency, and amount | [optional] 
 **direction** | **String**| The sort direction of the results. Choices are asc or desc. | [optional] 
 **page** | **String**| the page to start on. Results are paginated in increments of 100. Begins at page&#x3D;1. | [optional] 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

