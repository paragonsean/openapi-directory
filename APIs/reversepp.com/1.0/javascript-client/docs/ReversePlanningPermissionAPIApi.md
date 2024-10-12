# ReversePlanningPermissionApi.ReversePlanningPermissionAPIApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**postApplicantSingleApplicantMulti**](ReversePlanningPermissionAPIApi.md#postApplicantSingleApplicantMulti) | **POST** /applicant_multi | 
[**postApplicantSingleApplicantSingle**](ReversePlanningPermissionAPIApi.md#postApplicantSingleApplicantSingle) | **POST** /applicant_single | 
[**postFreeEndPointFree**](ReversePlanningPermissionAPIApi.md#postFreeEndPointFree) | **POST** /free | 
[**postPartialAddresSinglePartialAddressSingle**](ReversePlanningPermissionAPIApi.md#postPartialAddresSinglePartialAddressSingle) | **POST** /partial_address_single | 
[**postPartialAddressMultiPartialAddressMulti**](ReversePlanningPermissionAPIApi.md#postPartialAddressMultiPartialAddressMulti) | **POST** /partial_address_multi | 
[**postPostcodeMultiPostcodeMulti**](ReversePlanningPermissionAPIApi.md#postPostcodeMultiPostcodeMulti) | **POST** /postcode_multi | 
[**postPostcodeSinglePostcodeSingle**](ReversePlanningPermissionAPIApi.md#postPostcodeSinglePostcodeSingle) | **POST** /postcode_single | 
[**postProposalMultiProposal**](ReversePlanningPermissionAPIApi.md#postProposalMultiProposal) | **POST** /proposal | 



## postApplicantSingleApplicantMulti

> postApplicantSingleApplicantMulti(payload)



Retrieve 50 planning applications for an applicant name (example: John Smith). Rate limit is 100/day;10/minute

### Example

```javascript
import ReversePlanningPermissionApi from 'reverse_planning_permission_api';

let apiInstance = new ReversePlanningPermissionApi.ReversePlanningPermissionAPIApi();
let payload = new ReversePlanningPermissionApi.PostApplicantSingleApplicantMultiRequest(); // PostApplicantSingleApplicantMultiRequest | 
apiInstance.postApplicantSingleApplicantMulti(payload, (error, data, response) => {
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
 **payload** | [**PostApplicantSingleApplicantMultiRequest**](PostApplicantSingleApplicantMultiRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## postApplicantSingleApplicantSingle

> postApplicantSingleApplicantSingle(payload)



Retrieve a single planning application for an applicant (example: John Smith). Rate limit is 100/day;10/minute

### Example

```javascript
import ReversePlanningPermissionApi from 'reverse_planning_permission_api';

let apiInstance = new ReversePlanningPermissionApi.ReversePlanningPermissionAPIApi();
let payload = new ReversePlanningPermissionApi.PostApplicantSingleApplicantMultiRequest(); // PostApplicantSingleApplicantMultiRequest | 
apiInstance.postApplicantSingleApplicantSingle(payload, (error, data, response) => {
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
 **payload** | [**PostApplicantSingleApplicantMultiRequest**](PostApplicantSingleApplicantMultiRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## postFreeEndPointFree

> postFreeEndPointFree(payload)



Retrieve 1 planning application for proposal key word (example: Swimming Pool). Rate limit is 100/day;10/minute

### Example

```javascript
import ReversePlanningPermissionApi from 'reverse_planning_permission_api';

let apiInstance = new ReversePlanningPermissionApi.ReversePlanningPermissionAPIApi();
let payload = new ReversePlanningPermissionApi.PostFreeEndPointFreeRequest(); // PostFreeEndPointFreeRequest | 
apiInstance.postFreeEndPointFree(payload, (error, data, response) => {
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
 **payload** | [**PostFreeEndPointFreeRequest**](PostFreeEndPointFreeRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## postPartialAddresSinglePartialAddressSingle

> postPartialAddresSinglePartialAddressSingle(payload)



Retrieve a single planning application for a partial address (example: Station Road). Rate limit is 100/day;10/minute

### Example

```javascript
import ReversePlanningPermissionApi from 'reverse_planning_permission_api';

let apiInstance = new ReversePlanningPermissionApi.ReversePlanningPermissionAPIApi();
let payload = new ReversePlanningPermissionApi.PostPartialAddressMultiPartialAddressMultiRequest(); // PostPartialAddressMultiPartialAddressMultiRequest | 
apiInstance.postPartialAddresSinglePartialAddressSingle(payload, (error, data, response) => {
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
 **payload** | [**PostPartialAddressMultiPartialAddressMultiRequest**](PostPartialAddressMultiPartialAddressMultiRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## postPartialAddressMultiPartialAddressMulti

> postPartialAddressMultiPartialAddressMulti(payload)



Retrieve 50 planning applications for a partial address (example: Station Road). Rate limit is 100/day;10/minute

### Example

```javascript
import ReversePlanningPermissionApi from 'reverse_planning_permission_api';

let apiInstance = new ReversePlanningPermissionApi.ReversePlanningPermissionAPIApi();
let payload = new ReversePlanningPermissionApi.PostPartialAddressMultiPartialAddressMultiRequest(); // PostPartialAddressMultiPartialAddressMultiRequest | 
apiInstance.postPartialAddressMultiPartialAddressMulti(payload, (error, data, response) => {
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
 **payload** | [**PostPartialAddressMultiPartialAddressMultiRequest**](PostPartialAddressMultiPartialAddressMultiRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## postPostcodeMultiPostcodeMulti

> postPostcodeMultiPostcodeMulti(payload)



Retrieve 50 planning applications for a postcode. Rate limit is 100/day;10/minute

### Example

```javascript
import ReversePlanningPermissionApi from 'reverse_planning_permission_api';

let apiInstance = new ReversePlanningPermissionApi.ReversePlanningPermissionAPIApi();
let payload = new ReversePlanningPermissionApi.PostPostcodeMultiPostcodeMultiRequest(); // PostPostcodeMultiPostcodeMultiRequest | 
apiInstance.postPostcodeMultiPostcodeMulti(payload, (error, data, response) => {
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
 **payload** | [**PostPostcodeMultiPostcodeMultiRequest**](PostPostcodeMultiPostcodeMultiRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## postPostcodeSinglePostcodeSingle

> postPostcodeSinglePostcodeSingle(payload)



Retrieve a single planning application for a postcode. Rate limit is 100/day;10/minute

### Example

```javascript
import ReversePlanningPermissionApi from 'reverse_planning_permission_api';

let apiInstance = new ReversePlanningPermissionApi.ReversePlanningPermissionAPIApi();
let payload = new ReversePlanningPermissionApi.PostPostcodeMultiPostcodeMultiRequest(); // PostPostcodeMultiPostcodeMultiRequest | 
apiInstance.postPostcodeSinglePostcodeSingle(payload, (error, data, response) => {
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
 **payload** | [**PostPostcodeMultiPostcodeMultiRequest**](PostPostcodeMultiPostcodeMultiRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## postProposalMultiProposal

> postProposalMultiProposal(payload)



Retrieve 50 planning applications for proposal key word (example: Swimming Pool). Rate limit is 100/day;10/minute

### Example

```javascript
import ReversePlanningPermissionApi from 'reverse_planning_permission_api';

let apiInstance = new ReversePlanningPermissionApi.ReversePlanningPermissionAPIApi();
let payload = new ReversePlanningPermissionApi.PostProposalMultiProposalRequest(); // PostProposalMultiProposalRequest | 
apiInstance.postProposalMultiProposal(payload, (error, data, response) => {
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
 **payload** | [**PostProposalMultiProposalRequest**](PostProposalMultiProposalRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

