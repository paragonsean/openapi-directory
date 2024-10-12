# LetMcApiV2FreeTier1.StaffControllerApi

All URIs are relative to *https://live-api.letmc.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v2Tier1ShortNameStaffStaffApplicationStaffIDGet**](StaffControllerApi.md#v2Tier1ShortNameStaffStaffApplicationStaffIDGet) | **GET** /v2/tier1/{shortName}/staff/staff/{applicationStaffID} | Get a specific application staff given its unique Object ID (OID)
[**v2Tier1ShortNameStaffStaffGet**](StaffControllerApi.md#v2Tier1ShortNameStaffStaffGet) | **GET** /v2/tier1/{shortName}/staff/staff | A collection of all the staff members linked to a specific company



## v2Tier1ShortNameStaffStaffApplicationStaffIDGet

> ApplicationStaffModel v2Tier1ShortNameStaffStaffApplicationStaffIDGet(shortName, applicationStaffID)

Get a specific application staff given its unique Object ID (OID)

### Example

```javascript
import LetMcApiV2FreeTier1 from 'let_mc_api_v2_free__tier_1';

let apiInstance = new LetMcApiV2FreeTier1.StaffControllerApi();
let shortName = "shortName_example"; // String | The unique client short-name
let applicationStaffID = "applicationStaffID_example"; // String | The unique ID of the ApplicationStaff
apiInstance.v2Tier1ShortNameStaffStaffApplicationStaffIDGet(shortName, applicationStaffID, (error, data, response) => {
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
 **applicationStaffID** | **String**| The unique ID of the ApplicationStaff | 

### Return type

[**ApplicationStaffModel**](ApplicationStaffModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## v2Tier1ShortNameStaffStaffGet

> ApplicationStaffModelResults v2Tier1ShortNameStaffStaffGet(shortName, offset, count)

A collection of all the staff members linked to a specific company

### Example

```javascript
import LetMcApiV2FreeTier1 from 'let_mc_api_v2_free__tier_1';

let apiInstance = new LetMcApiV2FreeTier1.StaffControllerApi();
let shortName = "shortName_example"; // String | The unique client short-name
let offset = 56; // Number | The index of the first item to return
let count = 56; // Number | The maximum number of items to return (up to 1000 per request)
apiInstance.v2Tier1ShortNameStaffStaffGet(shortName, offset, count, (error, data, response) => {
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

[**ApplicationStaffModelResults**](ApplicationStaffModelResults.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml

