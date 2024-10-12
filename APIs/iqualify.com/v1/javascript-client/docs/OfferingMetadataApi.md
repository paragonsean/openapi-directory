# IQualifyManagementApi.OfferingMetadataApi

All URIs are relative to *https://api.iqualify.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**offeringsOfferingIdMetadataCategoryPut**](OfferingMetadataApi.md#offeringsOfferingIdMetadataCategoryPut) | **PUT** /offerings/{offeringId}/metadata/category | Update offering category metadata
[**offeringsOfferingIdMetadataLevelPut**](OfferingMetadataApi.md#offeringsOfferingIdMetadataLevelPut) | **PUT** /offerings/{offeringId}/metadata/level | Update offering level metadata
[**offeringsOfferingIdMetadataTagsPut**](OfferingMetadataApi.md#offeringsOfferingIdMetadataTagsPut) | **PUT** /offerings/{offeringId}/metadata/tags | Update offering tags metadata
[**offeringsOfferingIdMetadataTopicPut**](OfferingMetadataApi.md#offeringsOfferingIdMetadataTopicPut) | **PUT** /offerings/{offeringId}/metadata/topic | Update offering topic metadata



## offeringsOfferingIdMetadataCategoryPut

> OfferingMetadataResponse offeringsOfferingIdMetadataCategoryPut(offeringId, coursesContentIdMetadataCategoryPutRequest)

Update offering category metadata

Updates the offering category metadata.

### Example

```javascript
import IQualifyManagementApi from 'i_qualify_management_api';
let defaultClient = IQualifyManagementApi.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new IQualifyManagementApi.OfferingMetadataApi();
let offeringId = "offeringId_example"; // String | offering's id
let coursesContentIdMetadataCategoryPutRequest = new IQualifyManagementApi.CoursesContentIdMetadataCategoryPutRequest(); // CoursesContentIdMetadataCategoryPutRequest | 
apiInstance.offeringsOfferingIdMetadataCategoryPut(offeringId, coursesContentIdMetadataCategoryPutRequest, (error, data, response) => {
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
 **offeringId** | **String**| offering&#39;s id | 
 **coursesContentIdMetadataCategoryPutRequest** | [**CoursesContentIdMetadataCategoryPutRequest**](CoursesContentIdMetadataCategoryPutRequest.md)|  | 

### Return type

[**OfferingMetadataResponse**](OfferingMetadataResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## offeringsOfferingIdMetadataLevelPut

> OfferingMetadataResponse offeringsOfferingIdMetadataLevelPut(offeringId, coursesContentIdMetadataLevelPutRequest)

Update offering level metadata

Updates the offering level metadata.

### Example

```javascript
import IQualifyManagementApi from 'i_qualify_management_api';
let defaultClient = IQualifyManagementApi.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new IQualifyManagementApi.OfferingMetadataApi();
let offeringId = "offeringId_example"; // String | offering's id
let coursesContentIdMetadataLevelPutRequest = new IQualifyManagementApi.CoursesContentIdMetadataLevelPutRequest(); // CoursesContentIdMetadataLevelPutRequest | 
apiInstance.offeringsOfferingIdMetadataLevelPut(offeringId, coursesContentIdMetadataLevelPutRequest, (error, data, response) => {
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
 **offeringId** | **String**| offering&#39;s id | 
 **coursesContentIdMetadataLevelPutRequest** | [**CoursesContentIdMetadataLevelPutRequest**](CoursesContentIdMetadataLevelPutRequest.md)|  | 

### Return type

[**OfferingMetadataResponse**](OfferingMetadataResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## offeringsOfferingIdMetadataTagsPut

> OfferingMetadataResponse offeringsOfferingIdMetadataTagsPut(offeringId, coursesContentIdMetadataTagsPutRequest)

Update offering tags metadata

Updates the offering tags metadata.

### Example

```javascript
import IQualifyManagementApi from 'i_qualify_management_api';
let defaultClient = IQualifyManagementApi.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new IQualifyManagementApi.OfferingMetadataApi();
let offeringId = "offeringId_example"; // String | offering's id
let coursesContentIdMetadataTagsPutRequest = new IQualifyManagementApi.CoursesContentIdMetadataTagsPutRequest(); // CoursesContentIdMetadataTagsPutRequest | 
apiInstance.offeringsOfferingIdMetadataTagsPut(offeringId, coursesContentIdMetadataTagsPutRequest, (error, data, response) => {
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
 **offeringId** | **String**| offering&#39;s id | 
 **coursesContentIdMetadataTagsPutRequest** | [**CoursesContentIdMetadataTagsPutRequest**](CoursesContentIdMetadataTagsPutRequest.md)|  | 

### Return type

[**OfferingMetadataResponse**](OfferingMetadataResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## offeringsOfferingIdMetadataTopicPut

> OfferingMetadataResponse offeringsOfferingIdMetadataTopicPut(offeringId, coursesContentIdMetadataTopicPutRequest)

Update offering topic metadata

Updates the offering topic metadata.

### Example

```javascript
import IQualifyManagementApi from 'i_qualify_management_api';
let defaultClient = IQualifyManagementApi.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new IQualifyManagementApi.OfferingMetadataApi();
let offeringId = "offeringId_example"; // String | offering's id
let coursesContentIdMetadataTopicPutRequest = new IQualifyManagementApi.CoursesContentIdMetadataTopicPutRequest(); // CoursesContentIdMetadataTopicPutRequest | 
apiInstance.offeringsOfferingIdMetadataTopicPut(offeringId, coursesContentIdMetadataTopicPutRequest, (error, data, response) => {
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
 **offeringId** | **String**| offering&#39;s id | 
 **coursesContentIdMetadataTopicPutRequest** | [**CoursesContentIdMetadataTopicPutRequest**](CoursesContentIdMetadataTopicPutRequest.md)|  | 

### Return type

[**OfferingMetadataResponse**](OfferingMetadataResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

