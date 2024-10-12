# AvazaApiDocumentation.FixedAmountApi

All URIs are relative to *https://api.avaza.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fixedAmountGet**](FixedAmountApi.md#fixedAmountGet) | **GET** /api/FixedAmount | Gets list of Fixed Amounts



## fixedAmountGet

> FixedAmountList fixedAmountGet(opts)

Gets list of Fixed Amounts

### Example

```javascript
import AvazaApiDocumentation from 'avaza_api_documentation';
let defaultClient = AvazaApiDocumentation.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AvazaApiDocumentation.FixedAmountApi();
let opts = {
  'updatedAfter': new Date("2013-10-20T19:20:30+01:00"), // Date | 
  'entryDateFrom': new Date("2013-10-20T19:20:30+01:00"), // Date | 
  'entryDateTo': new Date("2013-10-20T19:20:30+01:00"), // Date | 
  'projectID': 56, // Number | (Optional) The ProjectID of a Project to filter Fixed Amounts for
  'taskID': 56, // Number | (Optional) The TaskID of a Task to filter Fixed Amounts for
  'isInvoiced': true, // Boolean | 
  'pageSize': 56, // Number | Number of items per page (max 1000)
  'pageNumber': 56, // Number | Page to display. Starts from 1.
  'sort': "sort_example" // String | Optional sorting instruction. Currently possible values: \"DateUpdated\", \"DateCreated\", \"DateUpdated desc\", \"DateCreated desc\",\"EntryDate\", \"EntryDate desc\", \"StartTimeLocal\",\"StartTimeLocal desc\", \"TimeSheetEntryID\", \"TimeSheetEntryID desc\"
};
apiInstance.fixedAmountGet(opts, (error, data, response) => {
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
 **updatedAfter** | **Date**|  | [optional] 
 **entryDateFrom** | **Date**|  | [optional] 
 **entryDateTo** | **Date**|  | [optional] 
 **projectID** | **Number**| (Optional) The ProjectID of a Project to filter Fixed Amounts for | [optional] 
 **taskID** | **Number**| (Optional) The TaskID of a Task to filter Fixed Amounts for | [optional] 
 **isInvoiced** | **Boolean**|  | [optional] 
 **pageSize** | **Number**| Number of items per page (max 1000) | [optional] 
 **pageNumber** | **Number**| Page to display. Starts from 1. | [optional] 
 **sort** | **String**| Optional sorting instruction. Currently possible values: \&quot;DateUpdated\&quot;, \&quot;DateCreated\&quot;, \&quot;DateUpdated desc\&quot;, \&quot;DateCreated desc\&quot;,\&quot;EntryDate\&quot;, \&quot;EntryDate desc\&quot;, \&quot;StartTimeLocal\&quot;,\&quot;StartTimeLocal desc\&quot;, \&quot;TimeSheetEntryID\&quot;, \&quot;TimeSheetEntryID desc\&quot; | [optional] 

### Return type

[**FixedAmountList**](FixedAmountList.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml

