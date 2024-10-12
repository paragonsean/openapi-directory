# IQualifyManagementApi.PulsesApi

All URIs are relative to *https://api.iqualify.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**offeringsOfferingIdAnalyticsPulsesGet**](PulsesApi.md#offeringsOfferingIdAnalyticsPulsesGet) | **GET** /offerings/{offeringId}/analytics/pulses | Find all pulse IDs in the specified offering
[**offeringsOfferingIdAnalyticsPulsesPulseIdResponsesGet**](PulsesApi.md#offeringsOfferingIdAnalyticsPulsesPulseIdResponsesGet) | **GET** /offerings/{offeringId}/analytics/pulses/{pulseId}/responses | Find pulses by offeringId and pulseId
[**offeringsOfferingIdAnalyticsPulsesResponsesGet**](PulsesApi.md#offeringsOfferingIdAnalyticsPulsesResponsesGet) | **GET** /offerings/{offeringId}/analytics/pulses/responses | Find pulses by offeringId



## offeringsOfferingIdAnalyticsPulsesGet

> [String] offeringsOfferingIdAnalyticsPulsesGet(offeringId)

Find all pulse IDs in the specified offering

Responds with the IDs of all pulses that learners have responded to in a specified offering.

### Example

```javascript
import IQualifyManagementApi from 'i_qualify_management_api';
let defaultClient = IQualifyManagementApi.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new IQualifyManagementApi.PulsesApi();
let offeringId = "offeringId_example"; // String | offering's id
apiInstance.offeringsOfferingIdAnalyticsPulsesGet(offeringId, (error, data, response) => {
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

### Return type

**[String]**

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## offeringsOfferingIdAnalyticsPulsesPulseIdResponsesGet

> [PulseResponse] offeringsOfferingIdAnalyticsPulsesPulseIdResponsesGet(offeringId, pulseId)

Find pulses by offeringId and pulseId

Responds with pulse&#39;s responses, matching the pulseId, in an offering matching the offeringId.

### Example

```javascript
import IQualifyManagementApi from 'i_qualify_management_api';
let defaultClient = IQualifyManagementApi.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new IQualifyManagementApi.PulsesApi();
let offeringId = "offeringId_example"; // String | offering's id
let pulseId = "pulseId_example"; // String | pulse's base id
apiInstance.offeringsOfferingIdAnalyticsPulsesPulseIdResponsesGet(offeringId, pulseId, (error, data, response) => {
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
 **pulseId** | **String**| pulse&#39;s base id | 

### Return type

[**[PulseResponse]**](PulseResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## offeringsOfferingIdAnalyticsPulsesResponsesGet

> [PulseResponse] offeringsOfferingIdAnalyticsPulsesResponsesGet(offeringId, opts)

Find pulses by offeringId

Responds with pulse&#39;s responses in an offering matching the offeringId.

### Example

```javascript
import IQualifyManagementApi from 'i_qualify_management_api';
let defaultClient = IQualifyManagementApi.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new IQualifyManagementApi.PulsesApi();
let offeringId = "offeringId_example"; // String | offering's id
let opts = {
  'pulseType': "pulseType_example", // String | Filter pulse responses by type.
  'responseTime': new IQualifyManagementApi.OfferingsOfferingIdAnalyticsPulsesResponsesGetResponseTimeParameter() // OfferingsOfferingIdAnalyticsPulsesResponsesGetResponseTimeParameter | Filter pulse responses by responseTime. Lower then (`lt`), lower then or equal (`lte`), greater then (`gt`) and greater then or equal (`gte`) operators are available. Example of filtering by time range __gte__2017-03-14T07:30:00Z__
};
apiInstance.offeringsOfferingIdAnalyticsPulsesResponsesGet(offeringId, opts, (error, data, response) => {
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
 **pulseType** | **String**| Filter pulse responses by type. | [optional] 
 **responseTime** | [**OfferingsOfferingIdAnalyticsPulsesResponsesGetResponseTimeParameter**](.md)| Filter pulse responses by responseTime. Lower then (&#x60;lt&#x60;), lower then or equal (&#x60;lte&#x60;), greater then (&#x60;gt&#x60;) and greater then or equal (&#x60;gte&#x60;) operators are available. Example of filtering by time range __gte__2017-03-14T07:30:00Z__ | [optional] 

### Return type

[**[PulseResponse]**](PulseResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

