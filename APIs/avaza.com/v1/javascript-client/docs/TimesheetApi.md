# AvazaApiDocumentation.TimesheetApi

All URIs are relative to *https://api.avaza.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**timesheetDelete**](TimesheetApi.md#timesheetDelete) | **DELETE** /api/Timesheet/{id} | Delete a Timesheet Entry
[**timesheetGet**](TimesheetApi.md#timesheetGet) | **GET** /api/Timesheet | Gets list of Timsheets
[**timesheetGetByID**](TimesheetApi.md#timesheetGetByID) | **GET** /api/Timesheet/{id} | Gets a Timesheet Entry by Timesheet ID
[**timesheetPost**](TimesheetApi.md#timesheetPost) | **POST** /api/Timesheet | Create a new Timesheet Entry
[**timesheetPut**](TimesheetApi.md#timesheetPut) | **PUT** /api/Timesheet | Update a Timesheet



## timesheetDelete

> Object timesheetDelete(id)

Delete a Timesheet Entry

### Example

```javascript
import AvazaApiDocumentation from 'avaza_api_documentation';
let defaultClient = AvazaApiDocumentation.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AvazaApiDocumentation.TimesheetApi();
let id = 789; // Number | The id of the timesheet entry to be deleted
apiInstance.timesheetDelete(id, (error, data, response) => {
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
 **id** | **Number**| The id of the timesheet entry to be deleted | 

### Return type

**Object**

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## timesheetGet

> TimesheetList timesheetGet(opts)

Gets list of Timsheets

### Example

```javascript
import AvazaApiDocumentation from 'avaza_api_documentation';
let defaultClient = AvazaApiDocumentation.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AvazaApiDocumentation.TimesheetApi();
let opts = {
  'updatedAfter': new Date("2013-10-20T19:20:30+01:00"), // Date | 
  'entryDateFrom': new Date("2013-10-20T19:20:30+01:00"), // Date | 
  'entryDateTo': new Date("2013-10-20T19:20:30+01:00"), // Date | 
  'userID': 56, // Number | The UserID of a timesheet user to filter timesheets for. Only api users with certain higher roles can see timesheets across multiple users.
  'userEmail': "userEmail_example", // String | 
  'categoryName': "categoryName_example", // String | 
  'projectID': 56, // Number | 
  'isBillable': true, // Boolean | 
  'isInvoiced': true, // Boolean | 
  'isTimerRunning': true, // Boolean | 
  'pageSize': 56, // Number | Number of items per page (max 1000)
  'pageNumber': 56, // Number | Page to display. Starts from 1.
  'includeInvoiceDetails': true, // Boolean | Defaults to false. When true, the InvoiceIDFK value will be included in the response.
  'sort': "sort_example" // String | Optional sorting instruction. Currently possible values: \"DateUpdated\", \"DateCreated\", \"DateUpdated desc\", \"DateCreated desc\",\"EntryDate\", \"EntryDate desc\", \"StartTimeLocal\",\"StartTimeLocal desc\", \"TimeSheetEntryID\", \"TimeSheetEntryID desc\"
};
apiInstance.timesheetGet(opts, (error, data, response) => {
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
 **userID** | **Number**| The UserID of a timesheet user to filter timesheets for. Only api users with certain higher roles can see timesheets across multiple users. | [optional] 
 **userEmail** | **String**|  | [optional] 
 **categoryName** | **String**|  | [optional] 
 **projectID** | **Number**|  | [optional] 
 **isBillable** | **Boolean**|  | [optional] 
 **isInvoiced** | **Boolean**|  | [optional] 
 **isTimerRunning** | **Boolean**|  | [optional] 
 **pageSize** | **Number**| Number of items per page (max 1000) | [optional] 
 **pageNumber** | **Number**| Page to display. Starts from 1. | [optional] 
 **includeInvoiceDetails** | **Boolean**| Defaults to false. When true, the InvoiceIDFK value will be included in the response. | [optional] 
 **sort** | **String**| Optional sorting instruction. Currently possible values: \&quot;DateUpdated\&quot;, \&quot;DateCreated\&quot;, \&quot;DateUpdated desc\&quot;, \&quot;DateCreated desc\&quot;,\&quot;EntryDate\&quot;, \&quot;EntryDate desc\&quot;, \&quot;StartTimeLocal\&quot;,\&quot;StartTimeLocal desc\&quot;, \&quot;TimeSheetEntryID\&quot;, \&quot;TimeSheetEntryID desc\&quot; | [optional] 

### Return type

[**TimesheetList**](TimesheetList.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## timesheetGetByID

> TimesheetDetails timesheetGetByID(id)

Gets a Timesheet Entry by Timesheet ID

### Example

```javascript
import AvazaApiDocumentation from 'avaza_api_documentation';
let defaultClient = AvazaApiDocumentation.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AvazaApiDocumentation.TimesheetApi();
let id = 789; // Number | Timesheet ID number
apiInstance.timesheetGetByID(id, (error, data, response) => {
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
 **id** | **Number**| Timesheet ID number | 

### Return type

[**TimesheetDetails**](TimesheetDetails.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## timesheetPost

> TimesheetDetails timesheetPost(model)

Create a new Timesheet Entry

### Example

```javascript
import AvazaApiDocumentation from 'avaza_api_documentation';
let defaultClient = AvazaApiDocumentation.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AvazaApiDocumentation.TimesheetApi();
let model = new AvazaApiDocumentation.NewTimesheet(); // NewTimesheet | 
apiInstance.timesheetPost(model, (error, data, response) => {
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
 **model** | [**NewTimesheet**](NewTimesheet.md)|  | 

### Return type

[**TimesheetDetails**](TimesheetDetails.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
- **Accept**: application/json, text/json, application/xml, text/xml


## timesheetPut

> TimesheetDetails timesheetPut(model)

Update a Timesheet

The FieldsToUpdate field expects a string array collection of the field names you would like updated. Valid fields to update inlcude \&quot;ProjectIDFK\&quot;, \&quot;TimeSheetCategoryIDFK\&quot;, \&quot;TaskIDFK\&quot;, \&quot;Duration\&quot;, \&quot;EntryDate\&quot;, \&quot;Notes\&quot;, \&quot;hasStartEndTime\&quot;, \&quot;CustomMetadata\&quot;. If you intend to provide start/end times on timesheets, this is achieved by including the start time in the EntryDate field (Iso date format), along with a Duration (decimal format).

### Example

```javascript
import AvazaApiDocumentation from 'avaza_api_documentation';
let defaultClient = AvazaApiDocumentation.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AvazaApiDocumentation.TimesheetApi();
let model = new AvazaApiDocumentation.UpdateTimesheetModel(); // UpdateTimesheetModel | 
apiInstance.timesheetPut(model, (error, data, response) => {
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
 **model** | [**UpdateTimesheetModel**](UpdateTimesheetModel.md)|  | 

### Return type

[**TimesheetDetails**](TimesheetDetails.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
- **Accept**: application/json, text/json, application/xml, text/xml

