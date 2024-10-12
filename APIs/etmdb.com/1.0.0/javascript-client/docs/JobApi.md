# EtMdbRestApiV1.JobApi

All URIs are relative to *https://etmdb.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**jobSearchRead**](JobApi.md#jobSearchRead) | **GET** /api/v1/job/search/{job_title} | Return job details search result
[**jobSearchallRead**](JobApi.md#jobSearchallRead) | **GET** /api/v1/job/searchall/{company_name} | Return job details search result



## jobSearchRead

> jobSearchRead(jobTitle)

Return job details search result

Return job details search result  ### Response Class (Status 200)  * __{job_title}__: Used as a key word to search jobs,  For more details on how job are listed [see here][ref]. [ref]: https://etmdb.com/en/job-list/-updated_date

### Example

```javascript
import EtMdbRestApiV1 from 'et_mdb_rest_api_v1';

let apiInstance = new EtMdbRestApiV1.JobApi();
let jobTitle = "jobTitle_example"; // String | 
apiInstance.jobSearchRead(jobTitle, (error, data, response) => {
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
 **jobTitle** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## jobSearchallRead

> jobSearchallRead(companyName)

Return job details search result

Return job details search result  ### Response Class (Status 200)  * __{company_name}__: Used as a key word to search jobs,  For more details on how job are listed [see here][ref]. [ref]: https://etmdb.com/en/job-list/-updated_date

### Example

```javascript
import EtMdbRestApiV1 from 'et_mdb_rest_api_v1';

let apiInstance = new EtMdbRestApiV1.JobApi();
let companyName = "companyName_example"; // String | 
apiInstance.jobSearchallRead(companyName, (error, data, response) => {
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
 **companyName** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

