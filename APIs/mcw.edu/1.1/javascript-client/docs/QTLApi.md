# RatGenomeDatabaseRestApi.QTLApi

All URIs are relative to *http://rest.rgd.mcw.edu/rgdws*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getMappedQTLByPositionUsingGET**](QTLApi.md#getMappedQTLByPositionUsingGET) | **GET** /qtls/mapped/{chr}/{start}/{stop}/{mapKey} | Returns a list QTL for given position and assembly map
[**getQTLByRgdIdUsingGET**](QTLApi.md#getQTLByRgdIdUsingGET) | **GET** /qtls/{rgdId} | Return a QTL for provided RGD ID
[**getQtlListByPositionUsingGET**](QTLApi.md#getQtlListByPositionUsingGET) | **GET** /qtls/{chr}/{start}/{stop}/{mapKey} | Returns a list QTL for given position and assembly map



## getMappedQTLByPositionUsingGET

> [MappedQTL] getMappedQTLByPositionUsingGET(chr, start, stop, mapKey)

Returns a list QTL for given position and assembly map

### Example

```javascript
import RatGenomeDatabaseRestApi from 'rat_genome_database_rest_api';

let apiInstance = new RatGenomeDatabaseRestApi.QTLApi();
let chr = "chr_example"; // String | Chromosome
let start = 789; // Number | Start Position
let stop = 789; // Number | Stop Position
let mapKey = 56; // Number | A list of assembly map keys can be found using the lookup service
apiInstance.getMappedQTLByPositionUsingGET(chr, start, stop, mapKey, (error, data, response) => {
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

[**[MappedQTL]**](MappedQTL.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getQTLByRgdIdUsingGET

> QTL getQTLByRgdIdUsingGET(rgdId)

Return a QTL for provided RGD ID

### Example

```javascript
import RatGenomeDatabaseRestApi from 'rat_genome_database_rest_api';

let apiInstance = new RatGenomeDatabaseRestApi.QTLApi();
let rgdId = 56; // Number | RGD ID
apiInstance.getQTLByRgdIdUsingGET(rgdId, (error, data, response) => {
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
 **rgdId** | **Number**| RGD ID | 

### Return type

[**QTL**](QTL.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getQtlListByPositionUsingGET

> [QTL] getQtlListByPositionUsingGET(chr, start, stop, mapKey)

Returns a list QTL for given position and assembly map

### Example

```javascript
import RatGenomeDatabaseRestApi from 'rat_genome_database_rest_api';

let apiInstance = new RatGenomeDatabaseRestApi.QTLApi();
let chr = "chr_example"; // String | Chromosome
let start = 789; // Number | Start Position
let stop = 789; // Number | Stop Position
let mapKey = 56; // Number | A list of assembly map keys can be found using the lookup service
apiInstance.getQtlListByPositionUsingGET(chr, start, stop, mapKey, (error, data, response) => {
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

[**[QTL]**](QTL.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

