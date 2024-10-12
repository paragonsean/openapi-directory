# RatGenomeDatabaseRestApi.OntologyApi

All URIs are relative to *http://rest.rgd.mcw.edu/rgdws*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getOntDagsUsingGET**](OntologyApi.md#getOntDagsUsingGET) | **GET** /ontology/ont/{accId} | Returns child and parent terms for Accession ID
[**getTermUsingGET**](OntologyApi.md#getTermUsingGET) | **GET** /ontology/term/{accId} | Returns term for Accession ID
[**isDescendantOfUsingGET**](OntologyApi.md#isDescendantOfUsingGET) | **GET** /ontology/term/{accId1}/{accId2} | Returns true or false for terms



## getOntDagsUsingGET

> {String: [String]} getOntDagsUsingGET(accId)

Returns child and parent terms for Accession ID

### Example

```javascript
import RatGenomeDatabaseRestApi from 'rat_genome_database_rest_api';

let apiInstance = new RatGenomeDatabaseRestApi.OntologyApi();
let accId = "accId_example"; // String | Accession ID
apiInstance.getOntDagsUsingGET(accId, (error, data, response) => {
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
 **accId** | **String**| Accession ID | 

### Return type

**{String: [String]}**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getTermUsingGET

> Term getTermUsingGET(accId)

Returns term for Accession ID

### Example

```javascript
import RatGenomeDatabaseRestApi from 'rat_genome_database_rest_api';

let apiInstance = new RatGenomeDatabaseRestApi.OntologyApi();
let accId = "accId_example"; // String | Term Accession ID
apiInstance.getTermUsingGET(accId, (error, data, response) => {
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
 **accId** | **String**| Term Accession ID | 

### Return type

[**Term**](Term.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## isDescendantOfUsingGET

> Boolean isDescendantOfUsingGET(accId1, accId2)

Returns true or false for terms

### Example

```javascript
import RatGenomeDatabaseRestApi from 'rat_genome_database_rest_api';

let apiInstance = new RatGenomeDatabaseRestApi.OntologyApi();
let accId1 = "accId1_example"; // String | Child Term Accession ID
let accId2 = "accId2_example"; // String | Parent Term Accession ID
apiInstance.isDescendantOfUsingGET(accId1, accId2, (error, data, response) => {
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
 **accId1** | **String**| Child Term Accession ID | 
 **accId2** | **String**| Parent Term Accession ID | 

### Return type

**Boolean**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

