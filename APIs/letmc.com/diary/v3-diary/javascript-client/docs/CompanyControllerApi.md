# AgentOsApiV3DiaryCallGroup.CompanyControllerApi

All URIs are relative to *https://live-api.letmc.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**companyControllerGetBranches**](CompanyControllerApi.md#companyControllerGetBranches) | **GET** /v3/diary/{shortName}/company/branches | All branches defined for a company
[**v3DiaryShortNameCompanyBranchesBranchIDGet**](CompanyControllerApi.md#v3DiaryShortNameCompanyBranchesBranchIDGet) | **GET** /v3/diary/{shortName}/company/branches/{branchID} | Get a specific branch given its unique Object ID (OID)



## companyControllerGetBranches

> AdvertisingBranchModelResults companyControllerGetBranches(shortName, offset, count)

All branches defined for a company

### Example

```javascript
import AgentOsApiV3DiaryCallGroup from 'agent_os_api_v3_diary_call_group';

let apiInstance = new AgentOsApiV3DiaryCallGroup.CompanyControllerApi();
let shortName = "shortName_example"; // String | The unique client short-name
let offset = 56; // Number | The index of the first item to return
let count = 56; // Number | The maximum number of items to return (up to 1000 per request)
apiInstance.companyControllerGetBranches(shortName, offset, count, (error, data, response) => {
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

[**AdvertisingBranchModelResults**](AdvertisingBranchModelResults.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## v3DiaryShortNameCompanyBranchesBranchIDGet

> AdvertisingBranchModel v3DiaryShortNameCompanyBranchesBranchIDGet(shortName, branchID)

Get a specific branch given its unique Object ID (OID)

### Example

```javascript
import AgentOsApiV3DiaryCallGroup from 'agent_os_api_v3_diary_call_group';

let apiInstance = new AgentOsApiV3DiaryCallGroup.CompanyControllerApi();
let shortName = "shortName_example"; // String | The unique client short-name
let branchID = "branchID_example"; // String | The unique ID of the Branch
apiInstance.v3DiaryShortNameCompanyBranchesBranchIDGet(shortName, branchID, (error, data, response) => {
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
 **branchID** | **String**| The unique ID of the Branch | 

### Return type

[**AdvertisingBranchModel**](AdvertisingBranchModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml

