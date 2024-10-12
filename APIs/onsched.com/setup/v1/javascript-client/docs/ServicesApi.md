# OnSchedSetupApi.ServicesApi

All URIs are relative to *https://sandbox-api.onsched.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**setupV1ServicesAllocationsIdDelete**](ServicesApi.md#setupV1ServicesAllocationsIdDelete) | **DELETE** /setup/v1/services/allocations/{id} | Delete Allocation
[**setupV1ServicesAllocationsIdGet**](ServicesApi.md#setupV1ServicesAllocationsIdGet) | **GET** /setup/v1/services/allocations/{id} | Get Allocation
[**setupV1ServicesAllocationsIdPut**](ServicesApi.md#setupV1ServicesAllocationsIdPut) | **PUT** /setup/v1/services/allocations/{id} | Update Allocation
[**setupV1ServicesBlockIdDelete**](ServicesApi.md#setupV1ServicesBlockIdDelete) | **DELETE** /setup/v1/services/block/{id} | Delete Block
[**setupV1ServicesBlockIdPut**](ServicesApi.md#setupV1ServicesBlockIdPut) | **PUT** /setup/v1/services/block/{id} | Update Block
[**setupV1ServicesBlocksIdGet**](ServicesApi.md#setupV1ServicesBlocksIdGet) | **GET** /setup/v1/services/blocks/{id} | Get Block
[**setupV1ServicesCalendarIdDelete**](ServicesApi.md#setupV1ServicesCalendarIdDelete) | **DELETE** /setup/v1/services/calendar/{id} | Delete Service Links
[**setupV1ServicesCalendarPost**](ServicesApi.md#setupV1ServicesCalendarPost) | **POST** /setup/v1/services/calendar | Link Service to Calendar
[**setupV1ServicesGet**](ServicesApi.md#setupV1ServicesGet) | **GET** /setup/v1/services | List Services
[**setupV1ServicesIdAllocationsBulkPost**](ServicesApi.md#setupV1ServicesIdAllocationsBulkPost) | **POST** /setup/v1/services/{id}/allocations/bulk | Create Allocations Bulk
[**setupV1ServicesIdAllocationsGet**](ServicesApi.md#setupV1ServicesIdAllocationsGet) | **GET** /setup/v1/services/{id}/allocations | List Service Allocations
[**setupV1ServicesIdAllocationsPost**](ServicesApi.md#setupV1ServicesIdAllocationsPost) | **POST** /setup/v1/services/{id}/allocations | Create Allocation
[**setupV1ServicesIdAvailabilityGet**](ServicesApi.md#setupV1ServicesIdAvailabilityGet) | **GET** /setup/v1/services/{id}/availability | Get Weekly Availability
[**setupV1ServicesIdAvailabilityPut**](ServicesApi.md#setupV1ServicesIdAvailabilityPut) | **PUT** /setup/v1/services/{id}/availability | Update Weekly Availability
[**setupV1ServicesIdBlockPost**](ServicesApi.md#setupV1ServicesIdBlockPost) | **POST** /setup/v1/services/{id}/block | Create Block
[**setupV1ServicesIdBlocksGet**](ServicesApi.md#setupV1ServicesIdBlocksGet) | **GET** /setup/v1/services/{id}/blocks | List Service Blocks
[**setupV1ServicesIdCalendarGet**](ServicesApi.md#setupV1ServicesIdCalendarGet) | **GET** /setup/v1/services/{id}/calendar | Get Linked Calendar
[**setupV1ServicesIdDelete**](ServicesApi.md#setupV1ServicesIdDelete) | **DELETE** /setup/v1/services/{id} | Delete Service
[**setupV1ServicesIdDeleteimageDelete**](ServicesApi.md#setupV1ServicesIdDeleteimageDelete) | **DELETE** /setup/v1/services/{id}/deleteimage | Delete Service Image
[**setupV1ServicesIdGet**](ServicesApi.md#setupV1ServicesIdGet) | **GET** /setup/v1/services/{id} | Get Service
[**setupV1ServicesIdPut**](ServicesApi.md#setupV1ServicesIdPut) | **PUT** /setup/v1/services/{id} | Update Service
[**setupV1ServicesIdRecoverPut**](ServicesApi.md#setupV1ServicesIdRecoverPut) | **PUT** /setup/v1/services/{id}/recover | Recover Service
[**setupV1ServicesIdResourcesGet**](ServicesApi.md#setupV1ServicesIdResourcesGet) | **GET** /setup/v1/services/{id}/resources | List Resources for Service
[**setupV1ServicesIdUploadimagePost**](ServicesApi.md#setupV1ServicesIdUploadimagePost) | **POST** /setup/v1/services/{id}/uploadimage | Upload Service Image
[**setupV1ServicesPost**](ServicesApi.md#setupV1ServicesPost) | **POST** /setup/v1/services | Create Service



## setupV1ServicesAllocationsIdDelete

> ServiceAllocationViewModel setupV1ServicesAllocationsIdDelete(id)

Delete Allocation

&lt;p&gt;Use this endpoint to permanently &lt;b&gt;Delete&lt;/b&gt; a service allocation. A valid &lt;b&gt;serviceAllocation id&lt;/b&gt; is required.&lt;/p&gt;

### Example

```javascript
import OnSchedSetupApi from 'on_sched_setup_api';
let defaultClient = OnSchedSetupApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new OnSchedSetupApi.ServicesApi();
let id = "id_example"; // String | id of serviceAllocation object
apiInstance.setupV1ServicesAllocationsIdDelete(id, (error, data, response) => {
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
 **id** | **String**| id of serviceAllocation object | 

### Return type

[**ServiceAllocationViewModel**](ServiceAllocationViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## setupV1ServicesAllocationsIdGet

> ServiceAllocationViewModel setupV1ServicesAllocationsIdGet(id)

Get Allocation

&lt;p&gt;Use this endpoint to &lt;b&gt;Get a Service Allocation&lt;/b&gt;. A valid &lt;b&gt;serviceAllocation id&lt;/b&gt; is required.&lt;/p&gt;

### Example

```javascript
import OnSchedSetupApi from 'on_sched_setup_api';
let defaultClient = OnSchedSetupApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new OnSchedSetupApi.ServicesApi();
let id = "id_example"; // String | id of serviceAllocation object
apiInstance.setupV1ServicesAllocationsIdGet(id, (error, data, response) => {
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
 **id** | **String**| id of serviceAllocation object | 

### Return type

[**ServiceAllocationViewModel**](ServiceAllocationViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## setupV1ServicesAllocationsIdPut

> ServiceAllocationViewModel setupV1ServicesAllocationsIdPut(id, opts)

Update Allocation

&lt;p&gt;Use this endpoint to &lt;b&gt;Update&lt;/b&gt; a service allocation. A valid &lt;b&gt;serviceAllocation id&lt;/b&gt; is required. Refer to the &lt;i&gt;POST /setup/v1/services/{id}/allocations&lt;/i&gt; endpoint for fields names and details.&lt;/p&gt;

### Example

```javascript
import OnSchedSetupApi from 'on_sched_setup_api';
let defaultClient = OnSchedSetupApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new OnSchedSetupApi.ServicesApi();
let id = "id_example"; // String | id of serviceAllocation object
let opts = {
  'serviceAllocationUpdateModel': new OnSchedSetupApi.ServiceAllocationUpdateModel() // ServiceAllocationUpdateModel | Service allocation update model
};
apiInstance.setupV1ServicesAllocationsIdPut(id, opts, (error, data, response) => {
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
 **id** | **String**| id of serviceAllocation object | 
 **serviceAllocationUpdateModel** | [**ServiceAllocationUpdateModel**](ServiceAllocationUpdateModel.md)| Service allocation update model | [optional] 

### Return type

[**ServiceAllocationViewModel**](ServiceAllocationViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
- **Accept**: application/json


## setupV1ServicesBlockIdDelete

> ResourceBlockViewModel setupV1ServicesBlockIdDelete(id)

Delete Block

&lt;p&gt;Use this endpoint to permanently &lt;b&gt;Delete&lt;/b&gt; a Service Block. A valid &lt;b&gt;serviceBlock id&lt;/b&gt; is required.&lt;/p&gt;

### Example

```javascript
import OnSchedSetupApi from 'on_sched_setup_api';
let defaultClient = OnSchedSetupApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new OnSchedSetupApi.ServicesApi();
let id = "id_example"; // String | id of serviceBlock object
apiInstance.setupV1ServicesBlockIdDelete(id, (error, data, response) => {
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
 **id** | **String**| id of serviceBlock object | 

### Return type

[**ResourceBlockViewModel**](ResourceBlockViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## setupV1ServicesBlockIdPut

> ServiceBlockViewModel setupV1ServicesBlockIdPut(id, opts)

Update Block

&lt;p&gt;Use this endpoint to &lt;b&gt;Update&lt;/b&gt; a Service Block. A valid &lt;b&gt;serviceBlock id&lt;/b&gt; is required.&lt;/p&gt;

### Example

```javascript
import OnSchedSetupApi from 'on_sched_setup_api';
let defaultClient = OnSchedSetupApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new OnSchedSetupApi.ServicesApi();
let id = "id_example"; // String | id of serviceBlock object
let opts = {
  'serviceBlockUpdateModel': new OnSchedSetupApi.ServiceBlockUpdateModel() // ServiceBlockUpdateModel | Service Block update model
};
apiInstance.setupV1ServicesBlockIdPut(id, opts, (error, data, response) => {
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
 **id** | **String**| id of serviceBlock object | 
 **serviceBlockUpdateModel** | [**ServiceBlockUpdateModel**](ServiceBlockUpdateModel.md)| Service Block update model | [optional] 

### Return type

[**ServiceBlockViewModel**](ServiceBlockViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
- **Accept**: application/json


## setupV1ServicesBlocksIdGet

> ResourceBlockViewModel setupV1ServicesBlocksIdGet(id)

Get Block

&lt;p&gt;Use this endpoint to &lt;b&gt;Get a Service Block&lt;/b&gt;. A valid &lt;b&gt;serviceBlock id&lt;/b&gt; is required.&lt;/p&gt;

### Example

```javascript
import OnSchedSetupApi from 'on_sched_setup_api';
let defaultClient = OnSchedSetupApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new OnSchedSetupApi.ServicesApi();
let id = "id_example"; // String | id of serviceBlock object
apiInstance.setupV1ServicesBlocksIdGet(id, (error, data, response) => {
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
 **id** | **String**| id of serviceBlock object | 

### Return type

[**ResourceBlockViewModel**](ResourceBlockViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## setupV1ServicesCalendarIdDelete

> ServiceCalendarViewModel setupV1ServicesCalendarIdDelete(id)

Delete Service Links

&lt;p&gt;Use this endpoint to &lt;b&gt;Delete&lt;/b&gt; service links from the calendar specified. A valid &lt;b&gt;calendar id&lt;/b&gt; is required.&lt;/p&gt;

### Example

```javascript
import OnSchedSetupApi from 'on_sched_setup_api';
let defaultClient = OnSchedSetupApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new OnSchedSetupApi.ServicesApi();
let id = "id_example"; // String | id of calender to delete service links from
apiInstance.setupV1ServicesCalendarIdDelete(id, (error, data, response) => {
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
 **id** | **String**| id of calender to delete service links from | 

### Return type

[**ServiceCalendarViewModel**](ServiceCalendarViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## setupV1ServicesCalendarPost

> ServiceCalendarViewModel setupV1ServicesCalendarPost(opts)

Link Service to Calendar

&lt;p&gt;Use this endpoint to &lt;b&gt;Link a Service&lt;/b&gt; to a calendar. &lt;/p&gt;

### Example

```javascript
import OnSchedSetupApi from 'on_sched_setup_api';
let defaultClient = OnSchedSetupApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new OnSchedSetupApi.ServicesApi();
let opts = {
  'serviceCalendarInputModel': new OnSchedSetupApi.ServiceCalendarInputModel() // ServiceCalendarInputModel | 
};
apiInstance.setupV1ServicesCalendarPost(opts, (error, data, response) => {
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
 **serviceCalendarInputModel** | [**ServiceCalendarInputModel**](ServiceCalendarInputModel.md)|  | [optional] 

### Return type

[**ServiceCalendarViewModel**](ServiceCalendarViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
- **Accept**: application/json


## setupV1ServicesGet

> ServiceListViewModel setupV1ServicesGet(opts)

List Services

&lt;p&gt;Use this endpoint to return a &lt;b&gt;List of Service&lt;/b&gt;. The results are returned in pages. Use the offset and limit parameters to control the page start and number of results. Default offset is 0, limit is 20, max is 100. Use the query parameters to filter the results further.&lt;/p&gt;

### Example

```javascript
import OnSchedSetupApi from 'on_sched_setup_api';
let defaultClient = OnSchedSetupApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new OnSchedSetupApi.ServicesApi();
let opts = {
  'locationId': "locationId_example", // String | id of business location, defaults to primary business location
  'serviceGroupId': 56, // Number | Filter services by groupId
  'deleted': true, // Boolean | Filter by deleted status
  'offset': 56, // Number | Starting row of page, default 0
  'limit': 56 // Number | Page limit default 20, max 100
};
apiInstance.setupV1ServicesGet(opts, (error, data, response) => {
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
 **locationId** | **String**| id of business location, defaults to primary business location | [optional] 
 **serviceGroupId** | **Number**| Filter services by groupId | [optional] 
 **deleted** | **Boolean**| Filter by deleted status | [optional] 
 **offset** | **Number**| Starting row of page, default 0 | [optional] 
 **limit** | **Number**| Page limit default 20, max 100 | [optional] 

### Return type

[**ServiceListViewModel**](ServiceListViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## setupV1ServicesIdAllocationsBulkPost

> [ServiceAllocationViewModel] setupV1ServicesIdAllocationsBulkPost(id, opts)

Create Allocations Bulk

&lt;p&gt;Use this endpoint to &lt;b&gt;Create&lt;/b&gt; bulk service allocations. A valid &lt;b&gt;service id&lt;/b&gt; is required. Use this endpoint only if you need to POST multiple service allocations in one transaction. For details refer to: &lt;a href&#x3D;\&quot;POST ​/setup​/v1​/services​/{id}​/allocations\&quot;&gt;Post Service Allocation&lt;/a&gt;&lt;/p&gt;

### Example

```javascript
import OnSchedSetupApi from 'on_sched_setup_api';
let defaultClient = OnSchedSetupApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new OnSchedSetupApi.ServicesApi();
let id = "id_example"; // String | id of service object
let opts = {
  'serviceAllocationsInputModel': new OnSchedSetupApi.ServiceAllocationsInputModel() // ServiceAllocationsInputModel | 
};
apiInstance.setupV1ServicesIdAllocationsBulkPost(id, opts, (error, data, response) => {
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
 **id** | **String**| id of service object | 
 **serviceAllocationsInputModel** | [**ServiceAllocationsInputModel**](ServiceAllocationsInputModel.md)|  | [optional] 

### Return type

[**[ServiceAllocationViewModel]**](ServiceAllocationViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
- **Accept**: application/json


## setupV1ServicesIdAllocationsGet

> ServiceAllocationListViewModel setupV1ServicesIdAllocationsGet(id, opts)

List Service Allocations

&lt;p&gt;Use this endpoint to return a &lt;b&gt;List of Service Allocations&lt;/b&gt; for a specified service. A valid &lt;b&gt;service id&lt;/b&gt; is required. Service allocations are used for &lt;b&gt;Event type services only&lt;/b&gt; where the events are offered on specific dates and times. Retrieve all allocations for a location by passing in 0 as the service id.&lt;/p&gt;  &lt;p&gt;The results are returned in pages. Use the offset and limit parameters to control the page start and number of results. Default offset is 0, limit is 20, max is 100. Use the query parameters to filter the results further.&lt;/p&gt;

### Example

```javascript
import OnSchedSetupApi from 'on_sched_setup_api';
let defaultClient = OnSchedSetupApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new OnSchedSetupApi.ServicesApi();
let id = "id_example"; // String | id of  service to list allocations for, 0 for all
let opts = {
  'locationId': "locationId_example", // String | The id of the location. Defaults to the primary location
  'resourceId': "resourceId_example", // String | The id of the resource to filter on
  'startDate': new Date("2013-10-20T19:20:30+01:00"), // Date | Format YYYY-MM-DD. Filter appointments by on/after startDate
  'endDate': new Date("2013-10-20T19:20:30+01:00"), // Date | Format YYYY-MM-DD. Filter appointments on/before endDate
  'offset': 56, // Number | Starting row of page, default 0
  'limit': 56 // Number | Page limit default 20, max 100
};
apiInstance.setupV1ServicesIdAllocationsGet(id, opts, (error, data, response) => {
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
 **id** | **String**| id of  service to list allocations for, 0 for all | 
 **locationId** | **String**| The id of the location. Defaults to the primary location | [optional] 
 **resourceId** | **String**| The id of the resource to filter on | [optional] 
 **startDate** | **Date**| Format YYYY-MM-DD. Filter appointments by on/after startDate | [optional] 
 **endDate** | **Date**| Format YYYY-MM-DD. Filter appointments on/before endDate | [optional] 
 **offset** | **Number**| Starting row of page, default 0 | [optional] 
 **limit** | **Number**| Page limit default 20, max 100 | [optional] 

### Return type

[**ServiceAllocationListViewModel**](ServiceAllocationListViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## setupV1ServicesIdAllocationsPost

> ServiceAllocationViewModel setupV1ServicesIdAllocationsPost(id, opts)

Create Allocation

&lt;p&gt;Use this endpoint to &lt;b&gt;Create&lt;/b&gt; a service allocation for a service. A valid &lt;b&gt;service id&lt;/b&gt; is required. Service allocations are used for &lt;b&gt;Event type services only&lt;/b&gt;. Service allocations allow you to specify the time(s) a service is available as opposed to using weekly availability which represents a weekly schedule, ie: Mon-Fri 9am-5pm.&lt;/p&gt;  &lt;p&gt;Required fields: &lt;b&gt;startDate, endDate, startTime, endTime&lt;/b&gt; and &lt;b&gt;reason&lt;/b&gt;. Service allocations can be set to specific time ranges or for the whole day by setting startTime&#x3D;0 and endTime&#x3D;2400. Service allocations can repeat for a specific date range instance or set to repeat at a specified frequency.&lt;/p&gt;  &lt;p&gt;    &lt;b&gt;Repeat object: (repeats &#x3D; true)&lt;/b&gt;  &lt;/p&gt;  &lt;p&gt;The &lt;b&gt;frequency&lt;/b&gt; can be set to a value of &lt;b&gt;D, W or M&lt;/b&gt; for &lt;b&gt;Day, Week&lt;/b&gt; or &lt;b&gt;Month&lt;/b&gt; respectively.&lt;/p&gt;  &lt;p&gt;Use the &lt;b&gt;interval&lt;/b&gt; property to specify the interval that the allocation repeats. For example, an interval of 2 for a weekly allocation means that the allocation will repeat every 2nd week beginning at the day specified. A daily allocation with an interval of 10 means the allocation will repeat every 10 days. The interval property applies to all repeat frequencies.  &lt;b&gt;If using the repeat functionality an interval value is required&lt;/b&gt;.&lt;/p&gt;  &lt;p&gt;    &lt;b&gt;DAILY ALLOCATIONS&lt;/b&gt;: Will repeat for each day of the week for the date range specified for the interval specified.  An interval value of “1” repeats every day, and an interval value of “3” is every 3rd day.&lt;/p&gt;  &lt;p&gt;    &lt;b&gt;WEEKLY ALLOCATIONS&lt;/b&gt;: Will repeat only on the specified days of the week for the date range specified. For weekly the &lt;b&gt;frequency&lt;/b&gt; is required and should be set to &lt;b&gt;“W”&lt;/b&gt;. You must specify the &lt;b&gt;“weekdays”&lt;/b&gt; parameter. Weekdays are expressed as a string of digits with each single digit in the string representing a day of the week. The possible values are &lt;b&gt;0,1,2,3,4,5,6&lt;/b&gt; where &lt;b&gt;0&#x3D;Sunday, 1&#x3D;Monday, 2&#x3D;Tuesday, 3&#x3D;Wednesday, 4&#x3D;Thursday, 5&#x3D;Friday, 6&#x3D;Saturday&lt;/b&gt;.  For example, a weekly frequency with an interval of “1”, and an entry of weekdays &#x3D; “24”, will repeat each week on Tuesday and Thursday for the duration of the allocation date range.&lt;/p&gt;  &lt;p&gt;    &lt;b&gt;MONTHLY ALLOCATIONS&lt;/b&gt;: Will repeat either on the day of the month specified in the &lt;b&gt;monthDay&lt;/b&gt; property or on the day of the week and week of the month specified by the &lt;b&gt;monthType&lt;/b&gt; property.  In both cases &lt;b&gt;frequency&lt;/b&gt; is required and should be set to &lt;b&gt;“M”&lt;/b&gt;, monthly. &lt;b&gt;monthDay&lt;/b&gt; is the day of the month you want allocated.  If monthDay&#x3D;’15’ this means to allocate the 15th of every month in the date range requested. Using monthDay in conjunction with monthType addresses “day of the week and week of the month” scenario.  There are two possible values for monthType: &lt;b&gt;D for Day of Month&lt;/b&gt; or &lt;b&gt;W for Week of Month.&lt;/b&gt; For &lt;b&gt;monthType D&lt;/b&gt;, monthDay value must be between 1 and 31. It is the day of the month to repeat on.  For &lt;b&gt;monthType M&lt;/b&gt;, monthDay value contains 2 digits:  day of week (0-6), (0,1,2,3,4,5,6 where 0&#x3D;Sunday, 1&#x3D;Monday, 2&#x3D;Tuesday, 3&#x3D;Wednesday, 4&#x3D;Thursday, 5&#x3D;Friday, 6&#x3D;Saturday) and week of month (1-5). 1 being the first week, 2 being the second. The third Thursday of the month is depicted as a monthType&#x3D;”M” and monthDay&#x3D;”43”.&lt;/p&gt;  &lt;p&gt;    &lt;b&gt;Repeats will end on the date specified by the end date.&lt;/b&gt;  &lt;/p&gt;

### Example

```javascript
import OnSchedSetupApi from 'on_sched_setup_api';
let defaultClient = OnSchedSetupApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new OnSchedSetupApi.ServicesApi();
let id = "id_example"; // String | id of service object
let opts = {
  'serviceAllocationInputModel': new OnSchedSetupApi.ServiceAllocationInputModel() // ServiceAllocationInputModel | 
};
apiInstance.setupV1ServicesIdAllocationsPost(id, opts, (error, data, response) => {
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
 **id** | **String**| id of service object | 
 **serviceAllocationInputModel** | [**ServiceAllocationInputModel**](ServiceAllocationInputModel.md)|  | [optional] 

### Return type

[**ServiceAllocationViewModel**](ServiceAllocationViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
- **Accept**: application/json


## setupV1ServicesIdAvailabilityGet

> ServiceAvailabilityViewModel setupV1ServicesIdAvailabilityGet(id)

Get Weekly Availability

&lt;p&gt;Use this endpoint to return the &lt;b&gt;Weekly Service Availability&lt;/b&gt; for an appointment service. A valid &lt;b&gt;service id&lt;/b&gt; is required. Weekly availability is returned for services where the Type &#x3D; 1. For event type services, where service Type &#x3D; 2, refer to the &lt;i&gt;GET ​/setup​/v1​/services​/{id}​/allocations&lt;/i&gt; endpoint.&lt;/p&gt;

### Example

```javascript
import OnSchedSetupApi from 'on_sched_setup_api';
let defaultClient = OnSchedSetupApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new OnSchedSetupApi.ServicesApi();
let id = "id_example"; // String | id of service object
apiInstance.setupV1ServicesIdAvailabilityGet(id, (error, data, response) => {
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
 **id** | **String**| id of service object | 

### Return type

[**ServiceAvailabilityViewModel**](ServiceAvailabilityViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## setupV1ServicesIdAvailabilityPut

> ServiceAvailabilityViewModel setupV1ServicesIdAvailabilityPut(id, opts)

Update Weekly Availability

&lt;p&gt;Use this endpoint to &lt;b&gt;Update&lt;/b&gt; service weekly availability. A valid &lt;b&gt;service id&lt;/b&gt; is required. The availability day entries are created when a service object is created.&lt;/p&gt;  &lt;p&gt;To update weekly availability hours, all days of the week must be provided. Days are defined as &lt;b&gt;sun, mon, tue, wed, thu, fri&lt;/b&gt; and &lt;b&gt;sat&lt;/b&gt;. The &lt;b&gt;startTime&lt;/b&gt; and &lt;b&gt;endTime&lt;/b&gt; fields are entered in &lt;b&gt;military format. e.g., 800 is 8:00am, 2230 is 10:30pm&lt;/b&gt;. We support 24-hour availability, set startTime&#x3D;0 and endTime&#x3D;2400. To set a whole day as unavailable, set both the startTime and endTime to 0.&lt;/p&gt;  &lt;p&gt;If you require times in between specified hours to be unavailable, use the resource blocks endpoints. Times entered represent the timezone of the business location.&lt;/p&gt;

### Example

```javascript
import OnSchedSetupApi from 'on_sched_setup_api';
let defaultClient = OnSchedSetupApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new OnSchedSetupApi.ServicesApi();
let id = "id_example"; // String | id of service object
let opts = {
  'availabilityInputModel': new OnSchedSetupApi.AvailabilityInputModel() // AvailabilityInputModel | Service Availability Input Model
};
apiInstance.setupV1ServicesIdAvailabilityPut(id, opts, (error, data, response) => {
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
 **id** | **String**| id of service object | 
 **availabilityInputModel** | [**AvailabilityInputModel**](AvailabilityInputModel.md)| Service Availability Input Model | [optional] 

### Return type

[**ServiceAvailabilityViewModel**](ServiceAvailabilityViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
- **Accept**: application/json


## setupV1ServicesIdBlockPost

> ServiceBlockViewModel setupV1ServicesIdBlockPost(id, opts)

Create Block

&lt;p&gt;Use this endpoint to &lt;b&gt;Create&lt;/b&gt; a Service Block. A valid &lt;b&gt;service id&lt;/b&gt; is required.&lt;/p&gt;  &lt;p&gt;Required fields: &lt;b&gt;startDate, endDate, startTime, endTime&lt;/b&gt; and &lt;b&gt;reason&lt;/b&gt;.&lt;/p&gt;  &lt;p&gt;Service blocks can be set to specific time ranges or for the whole day. To block a whole day set startTime to 0 and endTime to 2400.&lt;/p&gt;  &lt;p&gt;Service blocks can be for a specific date range instance or set to repeat at a specified frequency. &lt;/p&gt;  &lt;p&gt;    &lt;b&gt;Repeat object: (repeats &#x3D; true)&lt;/b&gt;  &lt;/p&gt;  &lt;p&gt;The &lt;b&gt;frequency&lt;/b&gt; can be set to a value of &lt;b&gt;D, W or M&lt;/b&gt; for &lt;b&gt;Day, Week&lt;/b&gt; or &lt;b&gt;Month&lt;/b&gt; respectively.&lt;/p&gt;  &lt;p&gt;Use the &lt;b&gt;interval&lt;/b&gt; property to specify the interval that the block repeats. For example, an interval of 2 for a weekly block means that the block will repeat every 2nd week beginning at the day specified. A daily block with an interval of 10 means the block will repeat every 10 days. The interval property applies to all repeat frequencies. &lt;b&gt;If using the repeat functionality an interval value is required&lt;/b&gt;.&lt;/p&gt;  &lt;p&gt;    &lt;b&gt;DAILY BLOCKS&lt;/b&gt;: Will repeat for each day of the week for the date range specified for the interval specified.  An interval value of “1” repeats every day, and an interval value of “3” is every 3rd day.&lt;/p&gt;  &lt;p&gt;    &lt;b&gt;WEEKLY BLOCKS&lt;/b&gt;: Will repeat only on the specified days of the week for the date range specified. For weekly the &lt;b&gt;frequency&lt;/b&gt; is required and should be set to &lt;b&gt;“W”&lt;/b&gt;.  You must specify the &lt;b&gt;weekdays&lt;/b&gt; parameter. Weekdays are expressed as a string of digits with each single digit in the string representing a day of the week. The possible values are &lt;b&gt;0,1,2,3,4,5,6&lt;/b&gt; where &lt;b&gt;0&#x3D;Sunday, 1&#x3D;Monday, 2&#x3D;Tuesday, 3&#x3D;Wednesday, 4&#x3D;Thursday, 5&#x3D;Friday, 6&#x3D;Saturday&lt;/b&gt;. For example, a weekly frequency with an interval of “1”, and an entry of weekdays &#x3D; “24”, will repeat each week on Tuesday and Thursday for the duration of the block date range.&lt;/p&gt;  &lt;p&gt;    &lt;b&gt;MONTHLY BLOCKS&lt;/b&gt;: Will repeat either on the day of the month specified in the &lt;b&gt;monthDay&lt;/b&gt; property or on the day of the week and week of the month specified by the &lt;b&gt;monthType&lt;/b&gt; property.  In both cases &lt;b&gt;frequency&lt;/b&gt; is required and should be set to &lt;b&gt;“M”&lt;/b&gt;, monthly, &lt;b&gt;monthDay&lt;/b&gt; is the day of the month you want blocked.  If monthDay&#x3D;’15’ this means to block the 15th of every month in the date range requested. Using monthDay in conjunction with monthType addresses “day of the week and week of the month” scenario.  There are two possible values for monthType: &lt;b&gt;D for Day of Month&lt;/b&gt; or &lt;b&gt;W for Week of Month.&lt;/b&gt; For &lt;b&gt;monthType D&lt;/b&gt;, monthDay value must be between 1 and 31. It is the day of the month to repeat on. For &lt;b&gt;monthType M&lt;/b&gt;, monthDay value contains 2 digits: day of week (0-6), (0,1,2,3,4,5,6 where 0&#x3D;Sunday, 1&#x3D;Monday, 2&#x3D;Tuesday, 3&#x3D;Wednesday, 4&#x3D;Thursday, 5&#x3D;Friday, 6&#x3D;Saturday) and week of month (1-5). 1 being the first week, 2 being the second. The third Thursday of the month is depicted as a monthType&#x3D;”M” and monthDay&#x3D;”43”.&lt;/p&gt;  &lt;p&gt;    &lt;b&gt;Repeats will end on the date specified by the end date.&lt;/b&gt;  &lt;/p&gt;

### Example

```javascript
import OnSchedSetupApi from 'on_sched_setup_api';
let defaultClient = OnSchedSetupApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new OnSchedSetupApi.ServicesApi();
let id = "id_example"; // String | id of service object
let opts = {
  'serviceBlockInputModel': new OnSchedSetupApi.ServiceBlockInputModel() // ServiceBlockInputModel | 
};
apiInstance.setupV1ServicesIdBlockPost(id, opts, (error, data, response) => {
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
 **id** | **String**| id of service object | 
 **serviceBlockInputModel** | [**ServiceBlockInputModel**](ServiceBlockInputModel.md)|  | [optional] 

### Return type

[**ServiceBlockViewModel**](ServiceBlockViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
- **Accept**: application/json


## setupV1ServicesIdBlocksGet

> ServiceBlockListViewModel setupV1ServicesIdBlocksGet(id, opts)

List Service Blocks

&lt;p&gt;Use this endpoint to return a list of &lt;b&gt;Service Blocks&lt;/b&gt;. The results are returned in pages. Use the offset and limit parameters to control the page start and number of results. Default offset is 0, limit is 20, max is 100. Use the query parameters to filter the results further.&lt;/p&gt;

### Example

```javascript
import OnSchedSetupApi from 'on_sched_setup_api';
let defaultClient = OnSchedSetupApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new OnSchedSetupApi.ServicesApi();
let id = "id_example"; // String | id of service to list blocks for
let opts = {
  'startDate': new Date("2013-10-20T19:20:30+01:00"), // Date | Format YYYY-MM-DD. Filter blocks on/after startDate
  'endDate': new Date("2013-10-20T19:20:30+01:00"), // Date | Format YYYY-MM-DD. Filter on/before endDate
  'offset': 56, // Number | Starting row of page, default 0
  'limit': 56 // Number | Page limit default 20, max 100
};
apiInstance.setupV1ServicesIdBlocksGet(id, opts, (error, data, response) => {
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
 **id** | **String**| id of service to list blocks for | 
 **startDate** | **Date**| Format YYYY-MM-DD. Filter blocks on/after startDate | [optional] 
 **endDate** | **Date**| Format YYYY-MM-DD. Filter on/before endDate | [optional] 
 **offset** | **Number**| Starting row of page, default 0 | [optional] 
 **limit** | **Number**| Page limit default 20, max 100 | [optional] 

### Return type

[**ServiceBlockListViewModel**](ServiceBlockListViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## setupV1ServicesIdCalendarGet

> ServiceCalendarViewModel setupV1ServicesIdCalendarGet(id, opts)

Get Linked Calendar

&lt;p&gt;Use this endpoint to &lt;b&gt;Get the Linked Calendar&lt;/b&gt; for the service requested. A valid &lt;b&gt;service id&lt;/b&gt; is required. A service can only be linked to one calendar in a location.&lt;/p&gt;

### Example

```javascript
import OnSchedSetupApi from 'on_sched_setup_api';
let defaultClient = OnSchedSetupApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new OnSchedSetupApi.ServicesApi();
let id = "id_example"; // String | id of service object
let opts = {
  'locationId': "locationId_example" // String | id of business location, defaults to primary business location
};
apiInstance.setupV1ServicesIdCalendarGet(id, opts, (error, data, response) => {
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
 **id** | **String**| id of service object | 
 **locationId** | **String**| id of business location, defaults to primary business location | [optional] 

### Return type

[**ServiceCalendarViewModel**](ServiceCalendarViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## setupV1ServicesIdDelete

> ServiceViewModel setupV1ServicesIdDelete(id)

Delete Service

&lt;p&gt;Use this endpoint to &lt;b&gt;Delete&lt;/b&gt; a service object. A valid &lt;b&gt;service id&lt;/b&gt; is required. The service is not permanently deleted and can be recovered by using the &lt;i&gt;PUT /setup​/v1​/services​/{id}​/recover&lt;/i&gt; endpoint.&lt;/p&gt;

### Example

```javascript
import OnSchedSetupApi from 'on_sched_setup_api';
let defaultClient = OnSchedSetupApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new OnSchedSetupApi.ServicesApi();
let id = "id_example"; // String | id of service object
apiInstance.setupV1ServicesIdDelete(id, (error, data, response) => {
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
 **id** | **String**| id of service object | 

### Return type

[**ServiceViewModel**](ServiceViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## setupV1ServicesIdDeleteimageDelete

> ServiceViewModel setupV1ServicesIdDeleteimageDelete(id)

Delete Service Image

&lt;p&gt;Use this endpoint to permanently &lt;b&gt;Delete&lt;/b&gt; a previously uploaded service image. A valid &lt;b&gt;service id&lt;/b&gt; is required.&lt;/p&gt;

### Example

```javascript
import OnSchedSetupApi from 'on_sched_setup_api';
let defaultClient = OnSchedSetupApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new OnSchedSetupApi.ServicesApi();
let id = "id_example"; // String | id of service object
apiInstance.setupV1ServicesIdDeleteimageDelete(id, (error, data, response) => {
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
 **id** | **String**| id of service object | 

### Return type

[**ServiceViewModel**](ServiceViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## setupV1ServicesIdGet

> ServiceViewModel setupV1ServicesIdGet(id)

Get Service

&lt;p&gt;Use this endpoint to return a &lt;b&gt;Service&lt;/b&gt; object. A valid &lt;b&gt;service id&lt;/b&gt; is required. Find service id&#39;s by using the &lt;i&gt;GET /setup/v1/services&lt;/i&gt; endpoint.&lt;/p&gt;

### Example

```javascript
import OnSchedSetupApi from 'on_sched_setup_api';
let defaultClient = OnSchedSetupApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new OnSchedSetupApi.ServicesApi();
let id = 56; // Number | id of service object
apiInstance.setupV1ServicesIdGet(id, (error, data, response) => {
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
 **id** | **Number**| id of service object | 

### Return type

[**ServiceViewModel**](ServiceViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## setupV1ServicesIdPut

> ServiceViewModel setupV1ServicesIdPut(id, opts)

Update Service

&lt;p&gt;Use this endpoint to &lt;b&gt;Update&lt;/b&gt; a service object. A valid &lt;b&gt;service id&lt;/b&gt; is required.&lt;/p&gt;

### Example

```javascript
import OnSchedSetupApi from 'on_sched_setup_api';
let defaultClient = OnSchedSetupApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new OnSchedSetupApi.ServicesApi();
let id = "id_example"; // String | 
let opts = {
  'serviceUpdateModel': new OnSchedSetupApi.ServiceUpdateModel() // ServiceUpdateModel | 
};
apiInstance.setupV1ServicesIdPut(id, opts, (error, data, response) => {
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
 **id** | **String**|  | 
 **serviceUpdateModel** | [**ServiceUpdateModel**](ServiceUpdateModel.md)|  | [optional] 

### Return type

[**ServiceViewModel**](ServiceViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
- **Accept**: application/json


## setupV1ServicesIdRecoverPut

> ServiceViewModel setupV1ServicesIdRecoverPut(id)

Recover Service

&lt;p&gt;Use this endpoint to &lt;b&gt;Recover&lt;/b&gt; a deleted service object. A valid &lt;b&gt;service id&lt;/b&gt; is required.&lt;/p&gt;

### Example

```javascript
import OnSchedSetupApi from 'on_sched_setup_api';
let defaultClient = OnSchedSetupApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new OnSchedSetupApi.ServicesApi();
let id = "id_example"; // String | 
apiInstance.setupV1ServicesIdRecoverPut(id, (error, data, response) => {
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
 **id** | **String**|  | 

### Return type

[**ServiceViewModel**](ServiceViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## setupV1ServicesIdResourcesGet

> ResourceListViewModel setupV1ServicesIdResourcesGet(id, opts)

List Resources for Service

&lt;p&gt;Use this endpoint to return a list of &lt;b&gt;Resources&lt;/b&gt; that provide the requested service. A valid &lt;b&gt;service id&lt;/b&gt; is required. Use the offset and limit parameters to control the page start and number of results. Default offset is 0, limit is 20, max is 100. Use the query parameters to filter the results further.&lt;/p&gt;

### Example

```javascript
import OnSchedSetupApi from 'on_sched_setup_api';
let defaultClient = OnSchedSetupApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new OnSchedSetupApi.ServicesApi();
let id = "id_example"; // String | id of service object
let opts = {
  'offset': 56, // Number | Starting row of page, default 0
  'limit': 56, // Number | Page limit default 20, max 100
  'googleAuthReturnUrl': "googleAuthReturnUrl_example", // String | Google calendar authorization return url
  'outlookAuthReturnUrl': "outlookAuthReturnUrl_example" // String | Outlook calendar authorization return url
};
apiInstance.setupV1ServicesIdResourcesGet(id, opts, (error, data, response) => {
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
 **id** | **String**| id of service object | 
 **offset** | **Number**| Starting row of page, default 0 | [optional] 
 **limit** | **Number**| Page limit default 20, max 100 | [optional] 
 **googleAuthReturnUrl** | **String**| Google calendar authorization return url | [optional] 
 **outlookAuthReturnUrl** | **String**| Outlook calendar authorization return url | [optional] 

### Return type

[**ResourceListViewModel**](ResourceListViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## setupV1ServicesIdUploadimagePost

> ServiceViewModel setupV1ServicesIdUploadimagePost(id, opts)

Upload Service Image

&lt;p&gt;Use this endpoint to &lt;b&gt;Upload&lt;/b&gt; an image to the service. A valid &lt;b&gt;service id&lt;/b&gt; is required. You must convert the image to a &lt;b&gt;base64 encoded string&lt;/b&gt; and pass that string as input along with your &lt;b&gt;filename&lt;/b&gt;.&lt;/p&gt;

### Example

```javascript
import OnSchedSetupApi from 'on_sched_setup_api';
let defaultClient = OnSchedSetupApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new OnSchedSetupApi.ServicesApi();
let id = "id_example"; // String | id of service object
let opts = {
  'serviceImageInputModel': new OnSchedSetupApi.ServiceImageInputModel() // ServiceImageInputModel | Input model for image upload
};
apiInstance.setupV1ServicesIdUploadimagePost(id, opts, (error, data, response) => {
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
 **id** | **String**| id of service object | 
 **serviceImageInputModel** | [**ServiceImageInputModel**](ServiceImageInputModel.md)| Input model for image upload | [optional] 

### Return type

[**ServiceViewModel**](ServiceViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
- **Accept**: application/json


## setupV1ServicesPost

> ServiceViewModel setupV1ServicesPost(opts)

Create Service

&lt;p&gt;Use this endpoint to &lt;b&gt;Create&lt;/b&gt; a new service. If not specified, the business location defaults to the primary business location. Note: Posting a service to the Primary Business Location will scope as company scoped and make the service available to all locations. If you want a service to only be available from a specific location, include the business location id.&lt;/p&gt;  &lt;p&gt;Required fields: &lt;b&gt;Name&lt;/b&gt; and &lt;b&gt;Duration&lt;/b&gt;&lt;/p&gt;  &lt;p&gt;The service &lt;b&gt;Type&lt;/b&gt; is either, &lt;b&gt;1 &#x3D; Appointment&lt;/b&gt; or &lt;b&gt;2 &#x3D; Event&lt;/b&gt;. Default is 1 if not specified.&lt;/p&gt;  &lt;p&gt;For type &#x3D; 1, Appointments - Create an availability entry for each weekday to provide the service for. &lt;b&gt;All days of the week must be provided when adding service availability.&lt;/b&gt; Days are defined as &lt;b&gt;sun, mon, tue, wed, thu, fri&lt;/b&gt; and &lt;b&gt;sat&lt;/b&gt;. Start and End Times are entered in military format. e.g., 800 is 8:00am, 2230 is 10:30pm. If not provided, it defaults to the primary location business hours.&lt;/p&gt;  &lt;p&gt;We support 24-hour availability, set startTime&#x3D;0 and endTime&#x3D;2400. To set a whole day as unavailable, set both the startTime and endTime to 0. If you require times in between specified hours to be unavailable, use the service block endpoint at: &lt;i&gt;POST ​/setup​/v1​/services​/{id}​/block&lt;/i&gt;.&lt;/p&gt;  &lt;p&gt;For type &#x3D; 2, Events - Create service allocations for their availability. Refer to the: &lt;i&gt;POST /setup​/v1​/services​/{id}​/allocations&lt;/i&gt; to set up service allocations for the event.&lt;/p&gt;  &lt;p&gt;Options are available for customer selected durations, for details: &lt;a href&#x3D;\&quot;https://docs.onsched.com/docs/services-overview#variable-duration\&quot;&gt;Variable Duration Overview&lt;/a&gt;&lt;/p&gt;  &lt;p&gt;Additional parameters include but are not limited to bookingLimit, maxCapacity and maxGroupSize. For details: &lt;a href&#x3D;\&quot;https://docs.onsched.com/docs/service-max-capacity\&quot;&gt;Service Limits Overview&lt;/a&gt;&lt;/p&gt;

### Example

```javascript
import OnSchedSetupApi from 'on_sched_setup_api';
let defaultClient = OnSchedSetupApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new OnSchedSetupApi.ServicesApi();
let opts = {
  'serviceInputModel': new OnSchedSetupApi.ServiceInputModel() // ServiceInputModel | 
};
apiInstance.setupV1ServicesPost(opts, (error, data, response) => {
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
 **serviceInputModel** | [**ServiceInputModel**](ServiceInputModel.md)|  | [optional] 

### Return type

[**ServiceViewModel**](ServiceViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
- **Accept**: application/json

