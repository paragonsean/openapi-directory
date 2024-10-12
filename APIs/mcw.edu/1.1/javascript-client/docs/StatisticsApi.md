# RatGenomeDatabaseRestApi.StatisticsApi

All URIs are relative to *http://rest.rgd.mcw.edu/rgdws*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getActiveObjectCountUsingGET**](StatisticsApi.md#getActiveObjectCountUsingGET) | **GET** /stats/count/activeObject/{speciesTypeKey}/{dateYYYYMMDD} | Count of active objects by type, for specified species and date
[**getActiveObjectDiffUsingGET**](StatisticsApi.md#getActiveObjectDiffUsingGET) | **GET** /stats/diff/activeObject/{speciesTypeKey}/{dateFromYYYYMMDD}/{dateToYYYYMMDD} | Count difference of active objects, by type, for specified species and date range
[**getGeneTypeCountUsingGET**](StatisticsApi.md#getGeneTypeCountUsingGET) | **GET** /stats/count/geneType/{speciesTypeKey}/{dateYYYYMMDD} | Count of gene types, for specified species and date
[**getGeneTypeDiffUsingGET**](StatisticsApi.md#getGeneTypeDiffUsingGET) | **GET** /stats/diff/geneType/{speciesTypeKey}/{dateFromYYYYMMDD}/{dateToYYYYMMDD} | Count difference of gene types, for specified species and date range
[**getObjectStatusCountUsingGET**](StatisticsApi.md#getObjectStatusCountUsingGET) | **GET** /stats/count/objectStatus/{speciesTypeKey}/{dateYYYYMMDD} | Count of objects with given status, for specified species and date
[**getObjectStatusDiffUsingGET**](StatisticsApi.md#getObjectStatusDiffUsingGET) | **GET** /stats/diff/objectStatus/{speciesTypeKey}/{dateFromYYYYMMDD}/{dateToYYYYMMDD} | Count difference of objects with given status, for specified species and date range
[**getObjectsWithRefSeqCountUsingGET**](StatisticsApi.md#getObjectsWithRefSeqCountUsingGET) | **GET** /stats/count/objectWithRefSeq/{speciesTypeKey}/{dateYYYYMMDD} | Count of objects with reference sequence(s), by object type, for specified species and date
[**getObjectsWithRefSeqDiffUsingGET**](StatisticsApi.md#getObjectsWithRefSeqDiffUsingGET) | **GET** /stats/diff/objectWithRefSeq/{speciesTypeKey}/{dateFromYYYYMMDD}/{dateToYYYYMMDD} | Count difference of objects with reference sequence(s), by object type, for specified species and date range
[**getObjectsWithReferenceCountUsingGET**](StatisticsApi.md#getObjectsWithReferenceCountUsingGET) | **GET** /stats/count/objectWithReference/{speciesTypeKey}/{dateYYYYMMDD} | Count of objects with reference, by object type, for specified species and date
[**getObjectsWithReferenceDiffUsingGET**](StatisticsApi.md#getObjectsWithReferenceDiffUsingGET) | **GET** /stats/diff/objectWithReference/{speciesTypeKey}/{dateFromYYYYMMDD}/{dateToYYYYMMDD} | Count difference of objects with reference, by object type, for specified species and date range
[**getObjectsWithXDBsCountUsingGET**](StatisticsApi.md#getObjectsWithXDBsCountUsingGET) | **GET** /stats/count/objectWithXdb/{speciesTypeKey}/{objectKey}/{dateYYYYMMDD} | Count of objects with external database ids, by database id, for specified species, object type and date
[**getObjectsWithXDBsDiffUsingGET**](StatisticsApi.md#getObjectsWithXDBsDiffUsingGET) | **GET** /stats/diff/objectWithXdb/{speciesTypeKey}/{objectKey}/{dateFromYYYYMMDD}/{dateToYYYYMMDD} | Count difference of objects with external database ids, by database id, for specified species, object type and date range
[**getProteinInteractionCountUsingGET**](StatisticsApi.md#getProteinInteractionCountUsingGET) | **GET** /stats/count/proteinInteraction/{speciesTypeKey}/{dateYYYYMMDD} | Count of protein interactions, for specified species and date
[**getProteinInteractionDiffUsingGET**](StatisticsApi.md#getProteinInteractionDiffUsingGET) | **GET** /stats/diff/proteinInteraction/{speciesTypeKey}/{dateFromYYYYMMDD}/{dateToYYYYMMDD} | Count difference of protein interactions, for specified species and date range
[**getQtlInheritanceTypeCountUsingGET**](StatisticsApi.md#getQtlInheritanceTypeCountUsingGET) | **GET** /stats/count/qtlInheritanceType/{speciesTypeKey}/{dateYYYYMMDD} | Count of strains, by qtl inheritance type, for specified species and date
[**getQtlInheritanceTypeDiffUsingGET**](StatisticsApi.md#getQtlInheritanceTypeDiffUsingGET) | **GET** /stats/diff/qtlInheritanceType/{speciesTypeKey}/{dateFromYYYYMMDD}/{dateToYYYYMMDD} | Count difference of strains, by qtl inheritance type, for specified species and date range
[**getRetiredObjectCountUsingGET**](StatisticsApi.md#getRetiredObjectCountUsingGET) | **GET** /stats/count/retiredObject/{speciesTypeKey}/{dateYYYYMMDD} | Count of retired objects by type, for specified species and date
[**getRetiredObjectDiffUsingGET**](StatisticsApi.md#getRetiredObjectDiffUsingGET) | **GET** /stats/diff/retiredObject/{speciesTypeKey}/{dateFromYYYYMMDD}/{dateToYYYYMMDD} | Count difference of retired objects, by type, for specified species and date range
[**getStrainTypeCountUsingGET**](StatisticsApi.md#getStrainTypeCountUsingGET) | **GET** /stats/count/strainType/{speciesTypeKey}/{dateYYYYMMDD} | Count of strain types, for specified species and date
[**getStrainTypeDiffUsingGET**](StatisticsApi.md#getStrainTypeDiffUsingGET) | **GET** /stats/diff/strainType/{speciesTypeKey}/{dateFromYYYYMMDD}/{dateToYYYYMMDD} | Count difference of strain types, for specified species and date range
[**getTermStatsUsingGET**](StatisticsApi.md#getTermStatsUsingGET) | **GET** /stats/term/{accId}/{filterAccId} | getTermStats
[**getWithdrawnObjectCountUsingGET**](StatisticsApi.md#getWithdrawnObjectCountUsingGET) | **GET** /stats/count/withdrawnObject/{speciesTypeKey}/{dateYYYYMMDD} | Count of withdrawn objects by type, for specified species and date
[**getWithdrawnObjectDiffUsingGET**](StatisticsApi.md#getWithdrawnObjectDiffUsingGET) | **GET** /stats/diff/withdrawnObject/{speciesTypeKey}/{dateFromYYYYMMDD}/{dateToYYYYMMDD} | Count difference of withdrawn objects, by type, for specified species and date range
[**getXdbsCountUsingGET**](StatisticsApi.md#getXdbsCountUsingGET) | **GET** /stats/count/xdb/{speciesTypeKey}/{dateYYYYMMDD} | Count of external database ids, for specied species and date
[**getXdbsDiffUsingGET**](StatisticsApi.md#getXdbsDiffUsingGET) | **GET** /stats/diff/xdb/{speciesTypeKey}/{dateFromYYYYMMDD}/{dateToYYYYMMDD} | Count difference of external database ids, for specified species and date range



## getActiveObjectCountUsingGET

> {String: String} getActiveObjectCountUsingGET(speciesTypeKey, dateYYYYMMDD)

Count of active objects by type, for specified species and date

### Example

```javascript
import RatGenomeDatabaseRestApi from 'rat_genome_database_rest_api';

let apiInstance = new RatGenomeDatabaseRestApi.StatisticsApi();
let speciesTypeKey = 56; // Number | speciesTypeKey
let dateYYYYMMDD = "dateYYYYMMDD_example"; // String | dateYYYYMMDD
apiInstance.getActiveObjectCountUsingGET(speciesTypeKey, dateYYYYMMDD, (error, data, response) => {
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
 **speciesTypeKey** | **Number**| speciesTypeKey | 
 **dateYYYYMMDD** | **String**| dateYYYYMMDD | 

### Return type

**{String: String}**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getActiveObjectDiffUsingGET

> {String: String} getActiveObjectDiffUsingGET(speciesTypeKey, dateFromYYYYMMDD, dateToYYYYMMDD)

Count difference of active objects, by type, for specified species and date range

### Example

```javascript
import RatGenomeDatabaseRestApi from 'rat_genome_database_rest_api';

let apiInstance = new RatGenomeDatabaseRestApi.StatisticsApi();
let speciesTypeKey = 56; // Number | speciesTypeKey
let dateFromYYYYMMDD = "dateFromYYYYMMDD_example"; // String | dateFromYYYYMMDD
let dateToYYYYMMDD = "dateToYYYYMMDD_example"; // String | dateToYYYYMMDD
apiInstance.getActiveObjectDiffUsingGET(speciesTypeKey, dateFromYYYYMMDD, dateToYYYYMMDD, (error, data, response) => {
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
 **speciesTypeKey** | **Number**| speciesTypeKey | 
 **dateFromYYYYMMDD** | **String**| dateFromYYYYMMDD | 
 **dateToYYYYMMDD** | **String**| dateToYYYYMMDD | 

### Return type

**{String: String}**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getGeneTypeCountUsingGET

> {String: String} getGeneTypeCountUsingGET(speciesTypeKey, dateYYYYMMDD)

Count of gene types, for specified species and date

### Example

```javascript
import RatGenomeDatabaseRestApi from 'rat_genome_database_rest_api';

let apiInstance = new RatGenomeDatabaseRestApi.StatisticsApi();
let speciesTypeKey = 56; // Number | speciesTypeKey
let dateYYYYMMDD = "dateYYYYMMDD_example"; // String | dateYYYYMMDD
apiInstance.getGeneTypeCountUsingGET(speciesTypeKey, dateYYYYMMDD, (error, data, response) => {
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
 **speciesTypeKey** | **Number**| speciesTypeKey | 
 **dateYYYYMMDD** | **String**| dateYYYYMMDD | 

### Return type

**{String: String}**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getGeneTypeDiffUsingGET

> {String: String} getGeneTypeDiffUsingGET(speciesTypeKey, dateFromYYYYMMDD, dateToYYYYMMDD)

Count difference of gene types, for specified species and date range

### Example

```javascript
import RatGenomeDatabaseRestApi from 'rat_genome_database_rest_api';

let apiInstance = new RatGenomeDatabaseRestApi.StatisticsApi();
let speciesTypeKey = 56; // Number | speciesTypeKey
let dateFromYYYYMMDD = "dateFromYYYYMMDD_example"; // String | dateFromYYYYMMDD
let dateToYYYYMMDD = "dateToYYYYMMDD_example"; // String | dateToYYYYMMDD
apiInstance.getGeneTypeDiffUsingGET(speciesTypeKey, dateFromYYYYMMDD, dateToYYYYMMDD, (error, data, response) => {
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
 **speciesTypeKey** | **Number**| speciesTypeKey | 
 **dateFromYYYYMMDD** | **String**| dateFromYYYYMMDD | 
 **dateToYYYYMMDD** | **String**| dateToYYYYMMDD | 

### Return type

**{String: String}**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getObjectStatusCountUsingGET

> {String: String} getObjectStatusCountUsingGET(speciesTypeKey, dateYYYYMMDD)

Count of objects with given status, for specified species and date

### Example

```javascript
import RatGenomeDatabaseRestApi from 'rat_genome_database_rest_api';

let apiInstance = new RatGenomeDatabaseRestApi.StatisticsApi();
let speciesTypeKey = 56; // Number | speciesTypeKey
let dateYYYYMMDD = "dateYYYYMMDD_example"; // String | dateYYYYMMDD
apiInstance.getObjectStatusCountUsingGET(speciesTypeKey, dateYYYYMMDD, (error, data, response) => {
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
 **speciesTypeKey** | **Number**| speciesTypeKey | 
 **dateYYYYMMDD** | **String**| dateYYYYMMDD | 

### Return type

**{String: String}**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getObjectStatusDiffUsingGET

> {String: String} getObjectStatusDiffUsingGET(speciesTypeKey, dateFromYYYYMMDD, dateToYYYYMMDD)

Count difference of objects with given status, for specified species and date range

### Example

```javascript
import RatGenomeDatabaseRestApi from 'rat_genome_database_rest_api';

let apiInstance = new RatGenomeDatabaseRestApi.StatisticsApi();
let speciesTypeKey = 56; // Number | speciesTypeKey
let dateFromYYYYMMDD = "dateFromYYYYMMDD_example"; // String | dateFromYYYYMMDD
let dateToYYYYMMDD = "dateToYYYYMMDD_example"; // String | dateToYYYYMMDD
apiInstance.getObjectStatusDiffUsingGET(speciesTypeKey, dateFromYYYYMMDD, dateToYYYYMMDD, (error, data, response) => {
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
 **speciesTypeKey** | **Number**| speciesTypeKey | 
 **dateFromYYYYMMDD** | **String**| dateFromYYYYMMDD | 
 **dateToYYYYMMDD** | **String**| dateToYYYYMMDD | 

### Return type

**{String: String}**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getObjectsWithRefSeqCountUsingGET

> {String: String} getObjectsWithRefSeqCountUsingGET(speciesTypeKey, dateYYYYMMDD)

Count of objects with reference sequence(s), by object type, for specified species and date

### Example

```javascript
import RatGenomeDatabaseRestApi from 'rat_genome_database_rest_api';

let apiInstance = new RatGenomeDatabaseRestApi.StatisticsApi();
let speciesTypeKey = 56; // Number | speciesTypeKey
let dateYYYYMMDD = "dateYYYYMMDD_example"; // String | dateYYYYMMDD
apiInstance.getObjectsWithRefSeqCountUsingGET(speciesTypeKey, dateYYYYMMDD, (error, data, response) => {
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
 **speciesTypeKey** | **Number**| speciesTypeKey | 
 **dateYYYYMMDD** | **String**| dateYYYYMMDD | 

### Return type

**{String: String}**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getObjectsWithRefSeqDiffUsingGET

> {String: String} getObjectsWithRefSeqDiffUsingGET(speciesTypeKey, dateFromYYYYMMDD, dateToYYYYMMDD)

Count difference of objects with reference sequence(s), by object type, for specified species and date range

### Example

```javascript
import RatGenomeDatabaseRestApi from 'rat_genome_database_rest_api';

let apiInstance = new RatGenomeDatabaseRestApi.StatisticsApi();
let speciesTypeKey = 56; // Number | speciesTypeKey
let dateFromYYYYMMDD = "dateFromYYYYMMDD_example"; // String | dateFromYYYYMMDD
let dateToYYYYMMDD = "dateToYYYYMMDD_example"; // String | dateToYYYYMMDD
apiInstance.getObjectsWithRefSeqDiffUsingGET(speciesTypeKey, dateFromYYYYMMDD, dateToYYYYMMDD, (error, data, response) => {
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
 **speciesTypeKey** | **Number**| speciesTypeKey | 
 **dateFromYYYYMMDD** | **String**| dateFromYYYYMMDD | 
 **dateToYYYYMMDD** | **String**| dateToYYYYMMDD | 

### Return type

**{String: String}**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getObjectsWithReferenceCountUsingGET

> {String: String} getObjectsWithReferenceCountUsingGET(speciesTypeKey, dateYYYYMMDD)

Count of objects with reference, by object type, for specified species and date

### Example

```javascript
import RatGenomeDatabaseRestApi from 'rat_genome_database_rest_api';

let apiInstance = new RatGenomeDatabaseRestApi.StatisticsApi();
let speciesTypeKey = 56; // Number | speciesTypeKey
let dateYYYYMMDD = "dateYYYYMMDD_example"; // String | dateYYYYMMDD
apiInstance.getObjectsWithReferenceCountUsingGET(speciesTypeKey, dateYYYYMMDD, (error, data, response) => {
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
 **speciesTypeKey** | **Number**| speciesTypeKey | 
 **dateYYYYMMDD** | **String**| dateYYYYMMDD | 

### Return type

**{String: String}**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getObjectsWithReferenceDiffUsingGET

> {String: String} getObjectsWithReferenceDiffUsingGET(speciesTypeKey, dateFromYYYYMMDD, dateToYYYYMMDD)

Count difference of objects with reference, by object type, for specified species and date range

### Example

```javascript
import RatGenomeDatabaseRestApi from 'rat_genome_database_rest_api';

let apiInstance = new RatGenomeDatabaseRestApi.StatisticsApi();
let speciesTypeKey = 56; // Number | speciesTypeKey
let dateFromYYYYMMDD = "dateFromYYYYMMDD_example"; // String | dateFromYYYYMMDD
let dateToYYYYMMDD = "dateToYYYYMMDD_example"; // String | dateToYYYYMMDD
apiInstance.getObjectsWithReferenceDiffUsingGET(speciesTypeKey, dateFromYYYYMMDD, dateToYYYYMMDD, (error, data, response) => {
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
 **speciesTypeKey** | **Number**| speciesTypeKey | 
 **dateFromYYYYMMDD** | **String**| dateFromYYYYMMDD | 
 **dateToYYYYMMDD** | **String**| dateToYYYYMMDD | 

### Return type

**{String: String}**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getObjectsWithXDBsCountUsingGET

> {String: String} getObjectsWithXDBsCountUsingGET(speciesTypeKey, objectKey, dateYYYYMMDD)

Count of objects with external database ids, by database id, for specified species, object type and date

### Example

```javascript
import RatGenomeDatabaseRestApi from 'rat_genome_database_rest_api';

let apiInstance = new RatGenomeDatabaseRestApi.StatisticsApi();
let speciesTypeKey = 56; // Number | speciesTypeKey
let objectKey = 56; // Number | objectKey
let dateYYYYMMDD = "dateYYYYMMDD_example"; // String | dateYYYYMMDD
apiInstance.getObjectsWithXDBsCountUsingGET(speciesTypeKey, objectKey, dateYYYYMMDD, (error, data, response) => {
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
 **speciesTypeKey** | **Number**| speciesTypeKey | 
 **objectKey** | **Number**| objectKey | 
 **dateYYYYMMDD** | **String**| dateYYYYMMDD | 

### Return type

**{String: String}**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getObjectsWithXDBsDiffUsingGET

> {String: String} getObjectsWithXDBsDiffUsingGET(speciesTypeKey, objectKey, dateFromYYYYMMDD, dateToYYYYMMDD)

Count difference of objects with external database ids, by database id, for specified species, object type and date range

### Example

```javascript
import RatGenomeDatabaseRestApi from 'rat_genome_database_rest_api';

let apiInstance = new RatGenomeDatabaseRestApi.StatisticsApi();
let speciesTypeKey = 56; // Number | speciesTypeKey
let objectKey = 56; // Number | objectKey
let dateFromYYYYMMDD = "dateFromYYYYMMDD_example"; // String | dateFromYYYYMMDD
let dateToYYYYMMDD = "dateToYYYYMMDD_example"; // String | dateToYYYYMMDD
apiInstance.getObjectsWithXDBsDiffUsingGET(speciesTypeKey, objectKey, dateFromYYYYMMDD, dateToYYYYMMDD, (error, data, response) => {
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
 **speciesTypeKey** | **Number**| speciesTypeKey | 
 **objectKey** | **Number**| objectKey | 
 **dateFromYYYYMMDD** | **String**| dateFromYYYYMMDD | 
 **dateToYYYYMMDD** | **String**| dateToYYYYMMDD | 

### Return type

**{String: String}**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getProteinInteractionCountUsingGET

> {String: String} getProteinInteractionCountUsingGET(speciesTypeKey, dateYYYYMMDD)

Count of protein interactions, for specified species and date

### Example

```javascript
import RatGenomeDatabaseRestApi from 'rat_genome_database_rest_api';

let apiInstance = new RatGenomeDatabaseRestApi.StatisticsApi();
let speciesTypeKey = 56; // Number | speciesTypeKey
let dateYYYYMMDD = "dateYYYYMMDD_example"; // String | dateYYYYMMDD
apiInstance.getProteinInteractionCountUsingGET(speciesTypeKey, dateYYYYMMDD, (error, data, response) => {
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
 **speciesTypeKey** | **Number**| speciesTypeKey | 
 **dateYYYYMMDD** | **String**| dateYYYYMMDD | 

### Return type

**{String: String}**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getProteinInteractionDiffUsingGET

> {String: String} getProteinInteractionDiffUsingGET(speciesTypeKey, dateFromYYYYMMDD, dateToYYYYMMDD)

Count difference of protein interactions, for specified species and date range

### Example

```javascript
import RatGenomeDatabaseRestApi from 'rat_genome_database_rest_api';

let apiInstance = new RatGenomeDatabaseRestApi.StatisticsApi();
let speciesTypeKey = 56; // Number | speciesTypeKey
let dateFromYYYYMMDD = "dateFromYYYYMMDD_example"; // String | dateFromYYYYMMDD
let dateToYYYYMMDD = "dateToYYYYMMDD_example"; // String | dateToYYYYMMDD
apiInstance.getProteinInteractionDiffUsingGET(speciesTypeKey, dateFromYYYYMMDD, dateToYYYYMMDD, (error, data, response) => {
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
 **speciesTypeKey** | **Number**| speciesTypeKey | 
 **dateFromYYYYMMDD** | **String**| dateFromYYYYMMDD | 
 **dateToYYYYMMDD** | **String**| dateToYYYYMMDD | 

### Return type

**{String: String}**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getQtlInheritanceTypeCountUsingGET

> {String: String} getQtlInheritanceTypeCountUsingGET(speciesTypeKey, dateYYYYMMDD)

Count of strains, by qtl inheritance type, for specified species and date

### Example

```javascript
import RatGenomeDatabaseRestApi from 'rat_genome_database_rest_api';

let apiInstance = new RatGenomeDatabaseRestApi.StatisticsApi();
let speciesTypeKey = 56; // Number | speciesTypeKey
let dateYYYYMMDD = "dateYYYYMMDD_example"; // String | dateYYYYMMDD
apiInstance.getQtlInheritanceTypeCountUsingGET(speciesTypeKey, dateYYYYMMDD, (error, data, response) => {
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
 **speciesTypeKey** | **Number**| speciesTypeKey | 
 **dateYYYYMMDD** | **String**| dateYYYYMMDD | 

### Return type

**{String: String}**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getQtlInheritanceTypeDiffUsingGET

> {String: String} getQtlInheritanceTypeDiffUsingGET(speciesTypeKey, dateFromYYYYMMDD, dateToYYYYMMDD)

Count difference of strains, by qtl inheritance type, for specified species and date range

### Example

```javascript
import RatGenomeDatabaseRestApi from 'rat_genome_database_rest_api';

let apiInstance = new RatGenomeDatabaseRestApi.StatisticsApi();
let speciesTypeKey = 56; // Number | speciesTypeKey
let dateFromYYYYMMDD = "dateFromYYYYMMDD_example"; // String | dateFromYYYYMMDD
let dateToYYYYMMDD = "dateToYYYYMMDD_example"; // String | dateToYYYYMMDD
apiInstance.getQtlInheritanceTypeDiffUsingGET(speciesTypeKey, dateFromYYYYMMDD, dateToYYYYMMDD, (error, data, response) => {
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
 **speciesTypeKey** | **Number**| speciesTypeKey | 
 **dateFromYYYYMMDD** | **String**| dateFromYYYYMMDD | 
 **dateToYYYYMMDD** | **String**| dateToYYYYMMDD | 

### Return type

**{String: String}**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getRetiredObjectCountUsingGET

> {String: String} getRetiredObjectCountUsingGET(speciesTypeKey, dateYYYYMMDD)

Count of retired objects by type, for specified species and date

### Example

```javascript
import RatGenomeDatabaseRestApi from 'rat_genome_database_rest_api';

let apiInstance = new RatGenomeDatabaseRestApi.StatisticsApi();
let speciesTypeKey = 56; // Number | speciesTypeKey
let dateYYYYMMDD = "dateYYYYMMDD_example"; // String | dateYYYYMMDD
apiInstance.getRetiredObjectCountUsingGET(speciesTypeKey, dateYYYYMMDD, (error, data, response) => {
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
 **speciesTypeKey** | **Number**| speciesTypeKey | 
 **dateYYYYMMDD** | **String**| dateYYYYMMDD | 

### Return type

**{String: String}**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getRetiredObjectDiffUsingGET

> {String: String} getRetiredObjectDiffUsingGET(speciesTypeKey, dateFromYYYYMMDD, dateToYYYYMMDD)

Count difference of retired objects, by type, for specified species and date range

### Example

```javascript
import RatGenomeDatabaseRestApi from 'rat_genome_database_rest_api';

let apiInstance = new RatGenomeDatabaseRestApi.StatisticsApi();
let speciesTypeKey = 56; // Number | speciesTypeKey
let dateFromYYYYMMDD = "dateFromYYYYMMDD_example"; // String | dateFromYYYYMMDD
let dateToYYYYMMDD = "dateToYYYYMMDD_example"; // String | dateToYYYYMMDD
apiInstance.getRetiredObjectDiffUsingGET(speciesTypeKey, dateFromYYYYMMDD, dateToYYYYMMDD, (error, data, response) => {
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
 **speciesTypeKey** | **Number**| speciesTypeKey | 
 **dateFromYYYYMMDD** | **String**| dateFromYYYYMMDD | 
 **dateToYYYYMMDD** | **String**| dateToYYYYMMDD | 

### Return type

**{String: String}**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getStrainTypeCountUsingGET

> {String: String} getStrainTypeCountUsingGET(speciesTypeKey, dateYYYYMMDD)

Count of strain types, for specified species and date

### Example

```javascript
import RatGenomeDatabaseRestApi from 'rat_genome_database_rest_api';

let apiInstance = new RatGenomeDatabaseRestApi.StatisticsApi();
let speciesTypeKey = 56; // Number | speciesTypeKey
let dateYYYYMMDD = "dateYYYYMMDD_example"; // String | dateYYYYMMDD
apiInstance.getStrainTypeCountUsingGET(speciesTypeKey, dateYYYYMMDD, (error, data, response) => {
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
 **speciesTypeKey** | **Number**| speciesTypeKey | 
 **dateYYYYMMDD** | **String**| dateYYYYMMDD | 

### Return type

**{String: String}**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getStrainTypeDiffUsingGET

> {String: String} getStrainTypeDiffUsingGET(speciesTypeKey, dateFromYYYYMMDD, dateToYYYYMMDD)

Count difference of strain types, for specified species and date range

### Example

```javascript
import RatGenomeDatabaseRestApi from 'rat_genome_database_rest_api';

let apiInstance = new RatGenomeDatabaseRestApi.StatisticsApi();
let speciesTypeKey = 56; // Number | speciesTypeKey
let dateFromYYYYMMDD = "dateFromYYYYMMDD_example"; // String | dateFromYYYYMMDD
let dateToYYYYMMDD = "dateToYYYYMMDD_example"; // String | dateToYYYYMMDD
apiInstance.getStrainTypeDiffUsingGET(speciesTypeKey, dateFromYYYYMMDD, dateToYYYYMMDD, (error, data, response) => {
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
 **speciesTypeKey** | **Number**| speciesTypeKey | 
 **dateFromYYYYMMDD** | **String**| dateFromYYYYMMDD | 
 **dateToYYYYMMDD** | **String**| dateToYYYYMMDD | 

### Return type

**{String: String}**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getTermStatsUsingGET

> {String: Number} getTermStatsUsingGET(accId, filterAccId)

getTermStats

### Example

```javascript
import RatGenomeDatabaseRestApi from 'rat_genome_database_rest_api';

let apiInstance = new RatGenomeDatabaseRestApi.StatisticsApi();
let accId = "accId_example"; // String | accId
let filterAccId = "filterAccId_example"; // String | filterAccId
apiInstance.getTermStatsUsingGET(accId, filterAccId, (error, data, response) => {
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
 **accId** | **String**| accId | 
 **filterAccId** | **String**| filterAccId | 

### Return type

**{String: Number}**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getWithdrawnObjectCountUsingGET

> {String: String} getWithdrawnObjectCountUsingGET(speciesTypeKey, dateYYYYMMDD)

Count of withdrawn objects by type, for specified species and date

### Example

```javascript
import RatGenomeDatabaseRestApi from 'rat_genome_database_rest_api';

let apiInstance = new RatGenomeDatabaseRestApi.StatisticsApi();
let speciesTypeKey = 56; // Number | speciesTypeKey
let dateYYYYMMDD = "dateYYYYMMDD_example"; // String | dateYYYYMMDD
apiInstance.getWithdrawnObjectCountUsingGET(speciesTypeKey, dateYYYYMMDD, (error, data, response) => {
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
 **speciesTypeKey** | **Number**| speciesTypeKey | 
 **dateYYYYMMDD** | **String**| dateYYYYMMDD | 

### Return type

**{String: String}**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getWithdrawnObjectDiffUsingGET

> {String: String} getWithdrawnObjectDiffUsingGET(speciesTypeKey, dateFromYYYYMMDD, dateToYYYYMMDD)

Count difference of withdrawn objects, by type, for specified species and date range

### Example

```javascript
import RatGenomeDatabaseRestApi from 'rat_genome_database_rest_api';

let apiInstance = new RatGenomeDatabaseRestApi.StatisticsApi();
let speciesTypeKey = 56; // Number | speciesTypeKey
let dateFromYYYYMMDD = "dateFromYYYYMMDD_example"; // String | dateFromYYYYMMDD
let dateToYYYYMMDD = "dateToYYYYMMDD_example"; // String | dateToYYYYMMDD
apiInstance.getWithdrawnObjectDiffUsingGET(speciesTypeKey, dateFromYYYYMMDD, dateToYYYYMMDD, (error, data, response) => {
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
 **speciesTypeKey** | **Number**| speciesTypeKey | 
 **dateFromYYYYMMDD** | **String**| dateFromYYYYMMDD | 
 **dateToYYYYMMDD** | **String**| dateToYYYYMMDD | 

### Return type

**{String: String}**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getXdbsCountUsingGET

> {String: String} getXdbsCountUsingGET(speciesTypeKey, dateYYYYMMDD)

Count of external database ids, for specied species and date

### Example

```javascript
import RatGenomeDatabaseRestApi from 'rat_genome_database_rest_api';

let apiInstance = new RatGenomeDatabaseRestApi.StatisticsApi();
let speciesTypeKey = 56; // Number | speciesTypeKey
let dateYYYYMMDD = "dateYYYYMMDD_example"; // String | dateYYYYMMDD
apiInstance.getXdbsCountUsingGET(speciesTypeKey, dateYYYYMMDD, (error, data, response) => {
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
 **speciesTypeKey** | **Number**| speciesTypeKey | 
 **dateYYYYMMDD** | **String**| dateYYYYMMDD | 

### Return type

**{String: String}**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getXdbsDiffUsingGET

> {String: String} getXdbsDiffUsingGET(speciesTypeKey, dateFromYYYYMMDD, dateToYYYYMMDD)

Count difference of external database ids, for specified species and date range

### Example

```javascript
import RatGenomeDatabaseRestApi from 'rat_genome_database_rest_api';

let apiInstance = new RatGenomeDatabaseRestApi.StatisticsApi();
let speciesTypeKey = 56; // Number | speciesTypeKey
let dateFromYYYYMMDD = "dateFromYYYYMMDD_example"; // String | dateFromYYYYMMDD
let dateToYYYYMMDD = "dateToYYYYMMDD_example"; // String | dateToYYYYMMDD
apiInstance.getXdbsDiffUsingGET(speciesTypeKey, dateFromYYYYMMDD, dateToYYYYMMDD, (error, data, response) => {
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
 **speciesTypeKey** | **Number**| speciesTypeKey | 
 **dateFromYYYYMMDD** | **String**| dateFromYYYYMMDD | 
 **dateToYYYYMMDD** | **String**| dateToYYYYMMDD | 

### Return type

**{String: String}**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

