# LetMcApiV2BasicTier2.StaffControllerApi

All URIs are relative to *https://live-api.letmc.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v2Tier2ShortNameStaffStaffApplicationStaffIDGet**](StaffControllerApi.md#v2Tier2ShortNameStaffStaffApplicationStaffIDGet) | **GET** /v2/tier2/{shortName}/staff/staff/{applicationStaffID} | Get a specific application staff given its unique Object ID (OID)
[**v2Tier2ShortNameStaffStaffGet**](StaffControllerApi.md#v2Tier2ShortNameStaffStaffGet) | **GET** /v2/tier2/{shortName}/staff/staff | A collection of all the staff members linked to a specific company



## v2Tier2ShortNameStaffStaffApplicationStaffIDGet

> ApplicationStaffModel v2Tier2ShortNameStaffStaffApplicationStaffIDGet(shortName, applicationStaffID)

Get a specific application staff given its unique Object ID (OID)

### Example

```javascript
import LetMcApiV2BasicTier2 from 'let_mc_api_v2_basic__tier_2';

let apiInstance = new LetMcApiV2BasicTier2.StaffControllerApi();
let shortName = "shortName_example"; // String | The unique client short-name
let applicationStaffID = "applicationStaffID_example"; // String | The unique ID of the ApplicationStaff
apiInstance.v2Tier2ShortNameStaffStaffApplicationStaffIDGet(shortName, applicationStaffID, (error, data, response) => {
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


## v2Tier2ShortNameStaffStaffGet

> ApplicationStaffModelResults v2Tier2ShortNameStaffStaffGet(shortName, offset, count)

A collection of all the staff members linked to a specific company

### Example

```javascript
import LetMcApiV2BasicTier2 from 'let_mc_api_v2_basic__tier_2';

let apiInstance = new LetMcApiV2BasicTier2.StaffControllerApi();
let shortName = "shortName_example"; // String | The unique client short-name
let offset = 56; // Number | The index of the first item to return
let count = 56; // Number | The maximum number of items to return (up to 1000 per request)
apiInstance.v2Tier2ShortNameStaffStaffGet(shortName, offset, count, (error, data, response) => {
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

