# RatGenomeDatabaseRestApi.MapApi

All URIs are relative to *http://rest.rgd.mcw.edu/rgdws*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getChromosomeByAssemblyUsingGET_0**](MapApi.md#getChromosomeByAssemblyUsingGET_0) | **GET** /maps/chr/{chromosome}/{mapKey} | Return a list of chromosomes
[**getChromosomesByAssemblyUsingGET_0**](MapApi.md#getChromosomesByAssemblyUsingGET_0) | **GET** /maps/chr/{mapKey} | Return a list of chromosomes
[**getMapsBySpeciesUsingGET**](MapApi.md#getMapsBySpeciesUsingGET) | **GET** /maps/{speciesTypeKey} | Return a list of assemblies



## getChromosomeByAssemblyUsingGET_0

> Chromosome getChromosomeByAssemblyUsingGET_0(chromosome, mapKey)

Return a list of chromosomes

### Example

```javascript
import RatGenomeDatabaseRestApi from 'rat_genome_database_rest_api';

let apiInstance = new RatGenomeDatabaseRestApi.MapApi();
let chromosome = "chromosome_example"; // String | chromosome
let mapKey = 56; // Number | mapKey
apiInstance.getChromosomeByAssemblyUsingGET_0(chromosome, mapKey, (error, data, response) => {
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


## getChromosomesByAssemblyUsingGET_0

> [String] getChromosomesByAssemblyUsingGET_0(mapKey)

Return a list of chromosomes

### Example

```javascript
import RatGenomeDatabaseRestApi from 'rat_genome_database_rest_api';

let apiInstance = new RatGenomeDatabaseRestApi.MapApi();
let mapKey = 56; // Number | mapKey
apiInstance.getChromosomesByAssemblyUsingGET_0(mapKey, (error, data, response) => {
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


## getMapsBySpeciesUsingGET

> [Map] getMapsBySpeciesUsingGET(speciesTypeKey)

Return a list of assemblies

### Example

```javascript
import RatGenomeDatabaseRestApi from 'rat_genome_database_rest_api';

let apiInstance = new RatGenomeDatabaseRestApi.MapApi();
let speciesTypeKey = 56; // Number | species Key
apiInstance.getMapsBySpeciesUsingGET(speciesTypeKey, (error, data, response) => {
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
 **speciesTypeKey** | **Number**| species Key | 

### Return type

[**[Map]**](Map.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

