# RatGenomeDatabaseRestApi.ChromosomeApi

All URIs are relative to *http://rest.rgd.mcw.edu/rgdws*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getChromosomeByAssemblyUsingGET**](ChromosomeApi.md#getChromosomeByAssemblyUsingGET) | **GET** /maps/chr/{chromosome}/{mapKey} | Return a list of chromosomes
[**getChromosomesByAssemblyUsingGET**](ChromosomeApi.md#getChromosomesByAssemblyUsingGET) | **GET** /maps/chr/{mapKey} | Return a list of chromosomes



## getChromosomeByAssemblyUsingGET

> Chromosome getChromosomeByAssemblyUsingGET(chromosome, mapKey)

Return a list of chromosomes

### Example

```javascript
import RatGenomeDatabaseRestApi from 'rat_genome_database_rest_api';

let apiInstance = new RatGenomeDatabaseRestApi.ChromosomeApi();
let chromosome = "chromosome_example"; // String | chromosome
let mapKey = 56; // Number | mapKey
apiInstance.getChromosomeByAssemblyUsingGET(chromosome, mapKey, (error, data, response) => {
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
 **chromosome** | **String**| chromosome | 
 **mapKey** | **Number**| mapKey | 

### Return type

[**Chromosome**](Chromosome.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getChromosomesByAssemblyUsingGET

> [String] getChromosomesByAssemblyUsingGET(mapKey)

Return a list of chromosomes

### Example

```javascript
import RatGenomeDatabaseRestApi from 'rat_genome_database_rest_api';

let apiInstance = new RatGenomeDatabaseRestApi.ChromosomeApi();
let mapKey = 56; // Number | mapKey
apiInstance.getChromosomesByAssemblyUsingGET(mapKey, (error, data, response) => {
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
 **mapKey** | **Number**| mapKey | 

### Return type

**[String]**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

