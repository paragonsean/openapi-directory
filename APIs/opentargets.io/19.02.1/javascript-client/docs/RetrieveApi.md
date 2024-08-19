# OpenTargetsPlatformRestApi.RetrieveApi

All URIs are relative to *http://platform-api.opentargets.io/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getAssociationById_0**](RetrieveApi.md#getAssociationById_0) | **GET** /platform/public/association | Get association by id
[**getEvidenceById_0**](RetrieveApi.md#getEvidenceById_0) | **GET** /platform/public/evidence | Get evidence by ID
[**postEvidenceById_0**](RetrieveApi.md#postEvidenceById_0) | **POST** /platform/public/evidence | Get evidence for a list of IDs



## getAssociationById_0

> getAssociationById_0(id)

Get association by id

Once we integrate all evidence connecting a target to a specific disease, we  compute an association score by the means of an harmonic sum. This *association score* provides  an indication of how strong the evidence behind each connection is and can be  used to rank genes in order of likelihood as drug targets.  The association ID is constructed by using the Ensembl ID of the gene and the  EFO ID for the disease (e.g. ENSG00000073756-EFO_0003767).  The method returns an association object, which contains the data and summary  on each evidence type included in the calculation of the score, as well as the score itself. 

### Example

```javascript
import OpenTargetsPlatformRestApi from 'open_targets_platform_rest_api';

let apiInstance = new OpenTargetsPlatformRestApi.RetrieveApi();
let id = "id_example"; // String | An association ID usually in the form of `TARGET_ID-DISEASE_ID`.
apiInstance.getAssociationById_0(id, (error, data, response) => {
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
 **id** | **String**| An association ID usually in the form of &#x60;TARGET_ID-DISEASE_ID&#x60;. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getEvidenceById_0

> getEvidenceById_0(id)

Get evidence by ID

We call **evidence** a unit of data that support a connection between a target and a disease. The Open Targets Platform integrates multiple types of evidence including genetic associations, somatic mutations, RNA expression and target-disease associations mined from the literature. This method allows you to retrieve a single evidence item or a list of pieces of evidence by using their targetvalidation.org ID.  Evidence IDs are unique within each data release (e.g. &#x60;8ed3d7568a8c6cac9c95cfb869bac762&#x60; for release 1.2). You can obtain a list of evidence and their IDs from other API calls such as [/public/evidence/filter](#!/public/get_public_evidence_filter).  **Please note** that a specific evidence ID may change between data releases. We can not guarantee that a specific evidence ID will refer to the same piece of evidence connecting a target and its diseases. 

### Example

```javascript
import OpenTargetsPlatformRestApi from 'open_targets_platform_rest_api';

let apiInstance = new OpenTargetsPlatformRestApi.RetrieveApi();
let id = "id_example"; // String | Internal unique ID of the evidence string to retrieve.
apiInstance.getEvidenceById_0(id, (error, data, response) => {
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
 **id** | **String**| Internal unique ID of the evidence string to retrieve. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## postEvidenceById_0

> postEvidenceById_0(body)

Get evidence for a list of IDs

This is the POST version of [/public/evidence](#!/public/get_public_evidence). It allows to query for a list of evidence strings encoded in a &#x60;json&#x60; object to be passed in the body. 

### Example

```javascript
import OpenTargetsPlatformRestApi from 'open_targets_platform_rest_api';

let apiInstance = new OpenTargetsPlatformRestApi.RetrieveApi();
let body = "body_example"; // String | IDs of the evidence string to retrieve.
apiInstance.postEvidenceById_0(body, (error, data, response) => {
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
 **body** | **String**| IDs of the evidence string to retrieve. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

