# LetMcApiV2FreeTier1.DiaryControllerApi

All URIs are relative to *https://live-api.letmc.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v2Tier1ShortNameDiaryAllocationsDiaryAllocationIDGet**](DiaryControllerApi.md#v2Tier1ShortNameDiaryAllocationsDiaryAllocationIDGet) | **GET** /v2/tier1/{shortName}/diary/allocations/{diaryAllocationID} | Get a specific diary allocation given its unique Object ID (OID)
[**v2Tier1ShortNameDiaryAllocationsGet**](DiaryControllerApi.md#v2Tier1ShortNameDiaryAllocationsGet) | **GET** /v2/tier1/{shortName}/diary/allocations | A collection of all diary allocations
[**v2Tier1ShortNameDiaryAppointmentsDiaryAppointmentIDGet**](DiaryControllerApi.md#v2Tier1ShortNameDiaryAppointmentsDiaryAppointmentIDGet) | **GET** /v2/tier1/{shortName}/diary/appointments/{diaryAppointmentID} | Get a specific diary appointment given its unique Object ID (OID)
[**v2Tier1ShortNameDiaryAppointmentsGet**](DiaryControllerApi.md#v2Tier1ShortNameDiaryAppointmentsGet) | **GET** /v2/tier1/{shortName}/diary/appointments | A collection of all diary appointments
[**v2Tier1ShortNameDiaryAppointmenttypesDiaryAppointmentTypeIDGet**](DiaryControllerApi.md#v2Tier1ShortNameDiaryAppointmenttypesDiaryAppointmentTypeIDGet) | **GET** /v2/tier1/{shortName}/diary/appointmenttypes/{diaryAppointmentTypeID} | Get a specific diary appointment type given its unique Object ID (OID)
[**v2Tier1ShortNameDiaryAppointmenttypesGet**](DiaryControllerApi.md#v2Tier1ShortNameDiaryAppointmenttypesGet) | **GET** /v2/tier1/{shortName}/diary/appointmenttypes | A collection of all diary appointment types



## v2Tier1ShortNameDiaryAllocationsDiaryAllocationIDGet

> DiaryAllocationModel v2Tier1ShortNameDiaryAllocationsDiaryAllocationIDGet(shortName, diaryAllocationID)

Get a specific diary allocation given its unique Object ID (OID)

### Example

```javascript
import LetMcApiV2FreeTier1 from 'let_mc_api_v2_free__tier_1';

let apiInstance = new LetMcApiV2FreeTier1.DiaryControllerApi();
let shortName = "shortName_example"; // String | The unique client short-name
let diaryAllocationID = "diaryAllocationID_example"; // String | The unique ID of the DiaryAllocation
apiInstance.v2Tier1ShortNameDiaryAllocationsDiaryAllocationIDGet(shortName, diaryAllocationID, (error, data, response) => {
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
 **shortName** | **String**| The unique client short-name | 
 **diaryAllocationID** | **String**| The unique ID of the DiaryAllocation | 

### Return type

[**DiaryAllocationModel**](DiaryAllocationModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## v2Tier1ShortNameDiaryAllocationsGet

> DiaryAllocationModelResults v2Tier1ShortNameDiaryAllocationsGet(shortName, offset, count)

A collection of all diary allocations

### Example

```javascript
import LetMcApiV2FreeTier1 from 'let_mc_api_v2_free__tier_1';

let apiInstance = new LetMcApiV2FreeTier1.DiaryControllerApi();
let shortName = "shortName_example"; // String | The unique client short-name
let offset = 56; // Number | The index of the first item to return
let count = 56; // Number | The maximum number of items to return (up to 1000 per request)
apiInstance.v2Tier1ShortNameDiaryAllocationsGet(shortName, offset, count, (error, data, response) => {
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
 **shortName** | **String**| The unique client short-name | 
 **offset** | **Number**| The index of the first item to return | 
 **count** | **Number**| The maximum number of items to return (up to 1000 per request) | 

### Return type

[**DiaryAllocationModelResults**](DiaryAllocationModelResults.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## v2Tier1ShortNameDiaryAppointmentsDiaryAppointmentIDGet

> DiaryAppointmentModel v2Tier1ShortNameDiaryAppointmentsDiaryAppointmentIDGet(shortName, diaryAppointmentID)

Get a specific diary appointment given its unique Object ID (OID)

### Example

```javascript
import LetMcApiV2FreeTier1 from 'let_mc_api_v2_free__tier_1';

let apiInstance = new LetMcApiV2FreeTier1.DiaryControllerApi();
let shortName = "shortName_example"; // String | The unique client short-name
let diaryAppointmentID = "diaryAppointmentID_example"; // String | The unique ID of the DiaryAppointment
apiInstance.v2Tier1ShortNameDiaryAppointmentsDiaryAppointmentIDGet(shortName, diaryAppointmentID, (error, data, response) => {
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
 **shortName** | **String**| The unique client short-name | 
 **diaryAppointmentID** | **String**| The unique ID of the DiaryAppointment | 

### Return type

[**DiaryAppointmentModel**](DiaryAppointmentModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## v2Tier1ShortNameDiaryAppointmentsGet

> DiaryAppointmentModelResults v2Tier1ShortNameDiaryAppointmentsGet(shortName, offset, count)

A collection of all diary appointments

### Example

```javascript
import LetMcApiV2FreeTier1 from 'let_mc_api_v2_free__tier_1';

let apiInstance = new LetMcApiV2FreeTier1.DiaryControllerApi();
let shortName = "shortName_example"; // String | The unique client short-name
let offset = 56; // Number | The index of the first item to return
let count = 56; // Number | The maximum number of items to return (up to 1000 per request)
apiInstance.v2Tier1ShortNameDiaryAppointmentsGet(shortName, offset, count, (error, data, response) => {
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
 **shortName** | **String**| The unique client short-name | 
 **offset** | **Number**| The index of the first item to return | 
 **count** | **Number**| The maximum number of items to return (up to 1000 per request) | 

### Return type

[**DiaryAppointmentModelResults**](DiaryAppointmentModelResults.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## v2Tier1ShortNameDiaryAppointmenttypesDiaryAppointmentTypeIDGet

> DiaryAppointmentTypeModel v2Tier1ShortNameDiaryAppointmenttypesDiaryAppointmentTypeIDGet(shortName, diaryAppointmentTypeID)

Get a specific diary appointment type given its unique Object ID (OID)

### Example

```javascript
import LetMcApiV2FreeTier1 from 'let_mc_api_v2_free__tier_1';

let apiInstance = new LetMcApiV2FreeTier1.DiaryControllerApi();
let shortName = "shortName_example"; // String | The unique client short-name
let diaryAppointmentTypeID = "diaryAppointmentTypeID_example"; // String | The unique ID of the DiaryAppointmentType
apiInstance.v2Tier1ShortNameDiaryAppointmenttypesDiaryAppointmentTypeIDGet(shortName, diaryAppointmentTypeID, (error, data, response) => {
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
 **shortName** | **String**| The unique client short-name | 
 **diaryAppointmentTypeID** | **String**| The unique ID of the DiaryAppointmentType | 

### Return type

[**DiaryAppointmentTypeModel**](DiaryAppointmentTypeModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## v2Tier1ShortNameDiaryAppointmenttypesGet

> DiaryAppointmentTypeModelResults v2Tier1ShortNameDiaryAppointmenttypesGet(shortName, offset, count)

A collection of all diary appointment types

### Example

```javascript
import LetMcApiV2FreeTier1 from 'let_mc_api_v2_free__tier_1';

let apiInstance = new LetMcApiV2FreeTier1.DiaryControllerApi();
let shortName = "shortName_example"; // String | The unique client short-name
let offset = 56; // Number | The index of the first item to return
let count = 56; // Number | The maximum number of items to return (up to 1000 per request)
apiInstance.v2Tier1ShortNameDiaryAppointmenttypesGet(shortName, offset, count, (error, data, response) => {
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
 **shortName** | **String**| The unique client short-name | 
 **offset** | **Number**| The index of the first item to return | 
 **count** | **Number**| The maximum number of items to return (up to 1000 per request) | 

### Return type

[**DiaryAppointmentTypeModelResults**](DiaryAppointmentTypeModelResults.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml

