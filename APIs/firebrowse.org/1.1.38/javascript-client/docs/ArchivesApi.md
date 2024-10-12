# FireBrowseBetaApi.ArchivesApi

All URIs are relative to *http://firebrowse.org/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**standardData**](ArchivesApi.md#standardData) | **GET** /Archives/StandardData | Retrieve standard data archives.



## standardData

> standardData(opts)

Retrieve standard data archives.

This service returns the archive URLs for our Firehose standard data runs, providing a RESTful interface similar in spirit to the command line &lt;a href&#x3D;\&quot;https://confluence.broadinstitute.org/display/GDAC/Download\&quot;&gt;firehose_get&lt;/a&gt; tool. The archives can be filtered based on date, cohort, data type, platform, center, data level, and protocol.

### Example

```javascript
import FireBrowseBetaApi from 'fire_browse_beta_api';

let apiInstance = new FireBrowseBetaApi.ArchivesApi();
let opts = {
  'format': "'json'", // String | Format of result.
  'date': [new Date("null")], // [Date] | Select one or more date stamps.
  'cohort': ["null"], // [String] | Narrow search to one or more TCGA disease cohorts from the scrollable list.
  'dataType': ["null"], // [String] | Narrow search to one or more TCGA data types from the scrollable list.
  'tool': ["null"], // [String] | Narrow search to include only data/results produced by the selected Firehose tool.
  'platform': ["null"], // [String] | Narrow search to one or more TCGA data generation platforms from the scrollable list.
  'center': ["null"], // [String] | Narrow search to one or more TCGA centers from the scrollable list.
  'level': [null], // [Number] | Narrow search to one or more TCGA data levels.
  'protocol': ["null"], // [String] | Narrow search to one or more sample characterization protocols from the scrollable list.
  'page': [1], // [Number] | Which page (slice) of entire results set should be returned. 
  'pageSize': [250], // [Number] | Number of records per page of results.  Max is 2000.
  'sortBy': "'cohort'" // String | Which column in the results should be used for sorting paginated results?
};
apiInstance.standardData(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **String**| Format of result. | [optional] [default to &#39;json&#39;]
 **date** | [**[Date]**](Date.md)| Select one or more date stamps. | [optional] 
 **cohort** | [**[String]**](String.md)| Narrow search to one or more TCGA disease cohorts from the scrollable list. | [optional] 
 **dataType** | [**[String]**](String.md)| Narrow search to one or more TCGA data types from the scrollable list. | [optional] 
 **tool** | [**[String]**](String.md)| Narrow search to include only data/results produced by the selected Firehose tool. | [optional] 
 **platform** | [**[String]**](String.md)| Narrow search to one or more TCGA data generation platforms from the scrollable list. | [optional] 
 **center** | [**[String]**](String.md)| Narrow search to one or more TCGA centers from the scrollable list. | [optional] 
 **level** | [**[Number]**](Number.md)| Narrow search to one or more TCGA data levels. | [optional] 
 **protocol** | [**[String]**](String.md)| Narrow search to one or more sample characterization protocols from the scrollable list. | [optional] 
 **page** | [**[Number]**](Number.md)| Which page (slice) of entire results set should be returned.  | [optional] 
 **pageSize** | [**[Number]**](Number.md)| Number of records per page of results.  Max is 2000. | [optional] 
 **sortBy** | **String**| Which column in the results should be used for sorting paginated results? | [optional] [default to &#39;cohort&#39;]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

