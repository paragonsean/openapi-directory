# OnSchedSetupApi.AppointmentsApi

All URIs are relative to *https://sandbox-api.onsched.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**setupV1AppointmentsGet**](AppointmentsApi.md#setupV1AppointmentsGet) | **GET** /setup/v1/appointments | List Appointments
[**setupV1AppointmentsIdGet**](AppointmentsApi.md#setupV1AppointmentsIdGet) | **GET** /setup/v1/appointments/{id} | Get Appointment
[**setupV1AppointmentsIdReassignResourceResourceIdPut**](AppointmentsApi.md#setupV1AppointmentsIdReassignResourceResourceIdPut) | **PUT** /setup/v1/appointments/{id}/reassign/resource/{resourceId} | Reassign Appointment



## setupV1AppointmentsGet

> AppointmentListViewModel setupV1AppointmentsGet(opts)

List Appointments

&lt;p&gt;Use this endpoint to return a &lt;b&gt;List of Appointments&lt;/b&gt;. Use the offset and limit parameters to control the page start and number of results. Default offset is 0, limit is 20, max is 100. Use the query parameters to filter the results further. For more information: &lt;a href&#x3D;\&quot;https://onsched.readme.io/docs/appointments-overview\&quot;&gt;Appointments Overview&lt;/a&gt;&lt;/p&gt;

### Example

```javascript
import OnSchedSetupApi from 'on_sched_setup_api';
let defaultClient = OnSchedSetupApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new OnSchedSetupApi.AppointmentsApi();
let opts = {
  'locationId': "locationId_example", // String | id of business location, defaults to primary business location
  'email': "email_example", // String | Filter appointments by email address
  'lastname': "lastname_example", // String | Filter appointments by lastname or part of
  'serviceId': "serviceId_example", // String | Filter appointments by service
  'calendarId': "calendarId_example", // String | Filter appointments by calendar
  'resourceId': "resourceId_example", // String | Filter appointments by resource
  'customerId': "customerId_example", // String | Filter appointments by customer
  'serviceAllocationId': "serviceAllocationId_example", // String | Filter appointments by service allocation
  'startDate': new Date("2013-10-20T19:20:30+01:00"), // Date | Format YYYY-MM-DD: Filter appointments by on/after startDate
  'endDate': new Date("2013-10-20T19:20:30+01:00"), // Date | Format YYYY-MM-DD: Filter appointments on/before endDate
  'status': "status_example", // String | Filter appointments by status: IN, BK, CN, RE, RS
  'bookedBy': "bookedBy_example", // String | Filter appointments by user email who booked
  'offset': 56, // Number | Starting row of page, default 0
  'limit': 56 // Number | Page limit default 20, max 100
};
apiInstance.setupV1AppointmentsGet(opts, (error, data, response) => {
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
 **email** | **String**| Filter appointments by email address | [optional] 
 **lastname** | **String**| Filter appointments by lastname or part of | [optional] 
 **serviceId** | **String**| Filter appointments by service | [optional] 
 **calendarId** | **String**| Filter appointments by calendar | [optional] 
 **resourceId** | **String**| Filter appointments by resource | [optional] 
 **customerId** | **String**| Filter appointments by customer | [optional] 
 **serviceAllocationId** | **String**| Filter appointments by service allocation | [optional] 
 **startDate** | **Date**| Format YYYY-MM-DD: Filter appointments by on/after startDate | [optional] 
 **endDate** | **Date**| Format YYYY-MM-DD: Filter appointments on/before endDate | [optional] 
 **status** | **String**| Filter appointments by status: IN, BK, CN, RE, RS | [optional] 
 **bookedBy** | **String**| Filter appointments by user email who booked | [optional] 
 **offset** | **Number**| Starting row of page, default 0 | [optional] 
 **limit** | **Number**| Page limit default 20, max 100 | [optional] 

### Return type

[**AppointmentListViewModel**](AppointmentListViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## setupV1AppointmentsIdGet

> AppointmentViewModel setupV1AppointmentsIdGet(id)

Get Appointment

&lt;p&gt;Use this endpoint to return an &lt;b&gt;Appointment&lt;/b&gt; object. A valid &lt;b&gt;appointment id&lt;/b&gt; is required. Find appointment id&#39;s by using the &lt;i&gt;GET​/setup​/v1​/appointments&lt;/i&gt; endpoint.&lt;/p&gt;

### Example

```javascript
import OnSchedSetupApi from 'on_sched_setup_api';
let defaultClient = OnSchedSetupApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new OnSchedSetupApi.AppointmentsApi();
let id = "id_example"; // String | id of appointment object
apiInstance.setupV1AppointmentsIdGet(id, (error, data, response) => {
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
 **id** | **String**| id of appointment object | 

### Return type

[**AppointmentViewModel**](AppointmentViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## setupV1AppointmentsIdReassignResourceResourceIdPut

> AppointmentViewModel setupV1AppointmentsIdReassignResourceResourceIdPut(id, resourceId)

Reassign Appointment

&lt;p&gt;Use this endpoint to &lt;b&gt;Reassign&lt;/b&gt; an appointment from one resource to another. The result returned is a single appointment that was reassigned to the target resource. A valid &lt;b&gt;appointment id&lt;/b&gt; and &lt;b&gt;resource id&lt;/b&gt; is required. Find appointment id&#39;s by using the &lt;i&gt;GET /setup/v1/appointments&lt;/i&gt; endpoint, find resource id&#39;s by using the &lt;i&gt;GET ​/setup​/v1​/resources&lt;/i&gt; endpoint.&lt;/p&gt;

### Example

```javascript
import OnSchedSetupApi from 'on_sched_setup_api';
let defaultClient = OnSchedSetupApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new OnSchedSetupApi.AppointmentsApi();
let id = "id_example"; // String | id of appointment object
let resourceId = "resourceId_example"; // String | id of target resource
apiInstance.setupV1AppointmentsIdReassignResourceResourceIdPut(id, resourceId, (error, data, response) => {
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
 **id** | **String**| id of appointment object | 
 **resourceId** | **String**| id of target resource | 

### Return type

[**AppointmentViewModel**](AppointmentViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

