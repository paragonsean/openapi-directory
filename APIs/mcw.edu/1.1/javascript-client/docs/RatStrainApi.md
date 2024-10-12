# RatGenomeDatabaseRestApi.RatStrainApi

All URIs are relative to *http://rest.rgd.mcw.edu/rgdws*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getAllStrainsUsingGET**](RatStrainApi.md#getAllStrainsUsingGET) | **GET** /strains/all | Return all active strains in RGD
[**getStrainByRgdIdUsingGET**](RatStrainApi.md#getStrainByRgdIdUsingGET) | **GET** /strains/{rgdId} | Return a strain by RGD ID
[**getStrainsByPositionUsingGET**](RatStrainApi.md#getStrainsByPositionUsingGET) | **GET** /strains/{chr}/{start}/{stop}/{mapKey} | Return all active strains by position



## getAllStrainsUsingGET

> [Strain] getAllStrainsUsingGET()

Return all active strains in RGD

### Example

```javascript
import RatGenomeDatabaseRestApi from 'rat_genome_database_rest_api';

let apiInstance = new RatGenomeDatabaseRestApi.RatStrainApi();
apiInstance.getAllStrainsUsingGET((error, data, response) => {
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

[**[Strain]**](Strain.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getStrainByRgdIdUsingGET

> Strain getStrainByRgdIdUsingGET(rgdId)

Return a strain by RGD ID

### Example

```javascript
import RatGenomeDatabaseRestApi from 'rat_genome_database_rest_api';

let apiInstance = new RatGenomeDatabaseRestApi.RatStrainApi();
let rgdId = 56; // Number | RGD ID of the strain
apiInstance.getStrainByRgdIdUsingGET(rgdId, (error, data, response) => {
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
 **rgdId** | **Number**| RGD ID of the strain | 

### Return type

[**Strain**](Strain.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getStrainsByPositionUsingGET

> [Strain] getStrainsByPositionUsingGET(chr, start, stop, mapKey)

Return all active strains by position

### Example

```javascript
import RatGenomeDatabaseRestApi from 'rat_genome_database_rest_api';

let apiInstance = new RatGenomeDatabaseRestApi.RatStrainApi();
let chr = "chr_example"; // String | Chromosome
let start = 789; // Number | Start Position
let stop = 789; // Number | Stop Position
let mapKey = 56; // Number | RGD Map Key (available through lookup service)
apiInstance.getStrainsByPositionUsingGET(chr, start, stop, mapKey, (error, data, response) => {
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
 **mapKey** | **Number**| RGD Map Key (available through lookup service) | 

### Return type

[**[Strain]**](Strain.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

