# RatGenomeDatabaseRestApi.SSLPApi

All URIs are relative to *http://rest.rgd.mcw.edu/rgdws*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getMappedSSLPByPositionUsingGET**](SSLPApi.md#getMappedSSLPByPositionUsingGET) | **GET** /sslps/mapped/{chr}/{start}/{stop}/{mapKey} | Returns a list SSLP for given position and assembly map



## getMappedSSLPByPositionUsingGET

> [MappedSSLP] getMappedSSLPByPositionUsingGET(chr, start, stop, mapKey)

Returns a list SSLP for given position and assembly map

### Example

```javascript
import RatGenomeDatabaseRestApi from 'rat_genome_database_rest_api';

let apiInstance = new RatGenomeDatabaseRestApi.SSLPApi();
let chr = "chr_example"; // String | Chromosome
let start = 789; // Number | Start Position
let stop = 789; // Number | Stop Position
let mapKey = 56; // Number | A list of assembly map keys can be found using the lookup service
apiInstance.getMappedSSLPByPositionUsingGET(chr, start, stop, mapKey, (error, data, response) => {
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
 **chr** | **String**| Chromosome | 
 **start** | **Number**| Start Position | 
 **stop** | **Number**| Stop Position | 
 **mapKey** | **Number**| A list of assembly map keys can be found using the lookup service | 

### Return type

[**[MappedSSLP]**](MappedSSLP.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

