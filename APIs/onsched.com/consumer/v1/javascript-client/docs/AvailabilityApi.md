# OnSchedConsumerApi.AvailabilityApi

All URIs are relative to *https://sandbox-api.onsched.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**consumerV1AvailabilityServiceIdStartDateEndDateDaysGet**](AvailabilityApi.md#consumerV1AvailabilityServiceIdStartDateEndDateDaysGet) | **GET** /consumer/v1/availability/{serviceId}/{startDate}/{endDate}/days | Get Available Days
[**consumerV1AvailabilityServiceIdStartDateEndDateGet**](AvailabilityApi.md#consumerV1AvailabilityServiceIdStartDateEndDateGet) | **GET** /consumer/v1/availability/{serviceId}/{startDate}/{endDate} | Get Available Times
[**consumerV1AvailabilityServiceIdStartDateEndDateUnavailableGet**](AvailabilityApi.md#consumerV1AvailabilityServiceIdStartDateEndDateUnavailableGet) | **GET** /consumer/v1/availability/{serviceId}/{startDate}/{endDate}/unavailable | Get Unavailable Times



## consumerV1AvailabilityServiceIdStartDateEndDateDaysGet

> AvailabilityDayViewModel consumerV1AvailabilityServiceIdStartDateEndDateDaysGet(serviceId, startDate, endDate, opts)

Get Available Days

&lt;p&gt;This endpoint will return &lt;b&gt;Day Level Availability&lt;/b&gt; for the range of dates requested. For example, if the business is closed, or there is a public holiday this endpoint will return that the \&quot;Day is unavailable\&quot;.&lt;/p&gt;  &lt;p&gt;Day Availability is a high-level check for Holidays and Open/Available hours of a location, service and/or resource and should be used to restrict your choices of days available in your application to improve usability and performance.&lt;/p&gt;  &lt;p&gt;A &lt;b&gt;serviceId&lt;/b&gt; is required. The &lt;b&gt;startDate&lt;/b&gt; and &lt;b&gt;endDate&lt;/b&gt; are required and are formatted as: &lt;b&gt;YYYY-MM-DD&lt;/b&gt;&lt;/p&gt;  &lt;p&gt;The locationId is optional, however if not supplied it defaults to the Primary Business Location for open/closed hours information. It is recommended you always provide the locationId.&lt;/p&gt;  &lt;p&gt;A &lt;b&gt;resourceId&lt;/b&gt; is optional. If used the available days will be return day availability for the resource specified.&lt;/p&gt;  &lt;p&gt;The &lt;b&gt;tzOffset&lt;/b&gt; parameter should be used if the appointment requester, the end user, is in a different timezone than the location or resource.&lt;/p&gt;

### Example

```javascript
import OnSchedConsumerApi from 'on_sched_consumer_api';
let defaultClient = OnSchedConsumerApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new OnSchedConsumerApi.AvailabilityApi();
let serviceId = "serviceId_example"; // String | Service Id for day availability search
let startDate = new Date("2013-10-20T19:20:30+01:00"); // Date | Format YYYY-MM-DD: Start Date for availability search
let endDate = new Date("2013-10-20T19:20:30+01:00"); // Date | Format YYYY-MM-DD: End Date for availability search
let opts = {
  'locationId': "locationId_example", // String | Id of business location, defaults to primary business location
  'resourceId': "resourceId_example", // String | Resource Id to filter on
  'tzOffset': 56 // Number | Timezone offset to view availability for
};
apiInstance.consumerV1AvailabilityServiceIdStartDateEndDateDaysGet(serviceId, startDate, endDate, opts, (error, data, response) => {
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
 **serviceId** | **String**| Service Id for day availability search | 
 **startDate** | **Date**| Format YYYY-MM-DD: Start Date for availability search | 
 **endDate** | **Date**| Format YYYY-MM-DD: End Date for availability search | 
 **locationId** | **String**| Id of business location, defaults to primary business location | [optional] 
 **resourceId** | **String**| Resource Id to filter on | [optional] 
 **tzOffset** | **Number**| Timezone offset to view availability for | [optional] 

### Return type

[**AvailabilityDayViewModel**](AvailabilityDayViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## consumerV1AvailabilityServiceIdStartDateEndDateGet

> AvailabilityViewModel consumerV1AvailabilityServiceIdStartDateEndDateGet(serviceId, startDate, endDate, opts)

Get Available Times

&lt;p&gt;    &lt;b&gt;Choose your search criteria carefully. Availability is an expensive call.&lt;/b&gt; If you search availability for all resources, you should only do so for a single date. If you search availability for multiple dates, you should only do so for a specific resource by specifying the optional resourceId parameter.&lt;/p&gt;  &lt;p&gt;A &lt;b&gt;serviceId&lt;/b&gt; is required. The &lt;b&gt;startDate&lt;/b&gt; and &lt;b&gt;endDate&lt;/b&gt; are required and are formatted as: &lt;b&gt;YYYY-MM-DD&lt;/b&gt;&lt;/p&gt;  &lt;p&gt;A &lt;b&gt;resourceId&lt;/b&gt; is optional, it is recommended if known at the time of availability call.&lt;/p&gt;  &lt;p&gt;    &lt;b&gt;timezoneName&lt;/b&gt; is optional, it allows you to specify the IANA formatted name for the end user&#39;s timezone to view availability. e.g., &lt;i&gt;America/New_York&lt;/i&gt;. &lt;b&gt;NOTE: This is the recommended approach for your implementation.&lt;/b&gt;  The \&quot;tzOffset\&quot; parameter remains for backward compatibility.  For JavaScript, use moment.js in your client for ease of timezone detection and selection. For iOS, use the name property of the NSTimeZone returned from the localTimeZone method. For .NET, consider NodaTime or TimeZoneConverter via NuGet. &lt;/p&gt;  &lt;p&gt;    &lt;b&gt;duration&lt;/b&gt; should only be populated if you allow the end user to select a duration, otherwise the service&#39;s duration will be used.&lt;/p&gt;  &lt;p&gt;    &lt;b&gt;startTime&lt;/b&gt; and &lt;b&gt;endTime&lt;/b&gt; are optional and are specified in &lt;b&gt;military time e.g., 800 &#x3D; 8:00am, 2230 &#x3D; 10:30pm&lt;/b&gt;. Note: You will only see availability within the boundary of your business location start and end times.&lt;/p&gt;  &lt;p&gt;    &lt;b&gt;dayAvailability&lt;/b&gt; will return day level availability for the number of days requested from the start date. See &lt;i&gt;GET /consumer/v1/availability/{serviceId}/{startDate}/{endDate}/days&lt;/i&gt; for details.&lt;/p&gt;  &lt;p&gt;    &lt;b&gt;firstDayAvailable&lt;/b&gt; only works with day availability. If set to true it will look for the first day available within the range specified by the dayAvailability parameter. The two parameters together can be a clever way to display availability for a week or month. Tip - pass in the beginning of the week or month, and available times are displayed for the first available date if exists.&lt;/p&gt;  &lt;p&gt;    &lt;b&gt;tzOffset&lt;/b&gt; allows you to pass in the timezone offset for the end user&#39;s timezone of choice, e.g., (-240) for EST. If you use this option, your application should be timezone aware. The requested timezone is specified as an offset (plus or minus) from GMT time.&lt;/p&gt;  &lt;p&gt;Availability can be complex. For further troubleshooting refer to the: &lt;i&gt;&lt;b&gt;GET /consumer/v1/availability/{serviceId}/{startDate}/{endDate}/unavailable&lt;/b&gt;&lt;/i&gt; endpoint. This endpoint will show you all unavailable times for a given date range. Available times are created from any unblocked time periods. For more information: &lt;a href&#x3D;\&quot;https://onsched.readme.io/docs/availability-overview\&quot;&gt;Availability Overview&lt;/a&gt;&lt;/p&gt;

### Example

```javascript
import OnSchedConsumerApi from 'on_sched_consumer_api';
let defaultClient = OnSchedConsumerApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new OnSchedConsumerApi.AvailabilityApi();
let serviceId = "serviceId_example"; // String | Service Id for availability search
let startDate = new Date("2013-10-20T19:20:30+01:00"); // Date | Format YYYY-MM-DD: Start Date for availability search
let endDate = new Date("2013-10-20T19:20:30+01:00"); // Date | Format YYYY-MM-DD: End Date for availability search
let opts = {
  'startTime': 56, // Number | Format Military Time Start Time for availability search. Defaults to Business Hours Start
  'endTime': 56, // Number | Format Military Time. End Time for availability search. Defaults to Business Hours End
  'locationId': "locationId_example", // String | Id of business location, defaults to primary business location
  'resourceId': "resourceId_example", // String | Resource Id for availability search
  'resourceGroupId': "resourceGroupId_example", // String | Resource Group Id for availability search
  'resourceIds': "resourceIds_example", // String | Comma separated Resource Id's for availability search
  'roundRobin': "roundRobin_example", // String | Round robin choice 0=none, 1=random, 2=balanced
  'duration': 56, // Number | Duration of the service if different from default
  'interval': 56, // Number | Booking Interval if different than the default
  'timezoneName': "timezoneName_example", // String | Requested IANA timezone Id to view availability
  'tzOffset': 56, // Number | Request timezone offset to view availability
  'destination': "destination_example", // String | For calculating travel based availability, requires distance scope
  'dayAvailabilityStartDate': new Date("2013-10-20T19:20:30+01:00"), // Date | Format YYYY-DD-YY: Start date for day availability, defaults to startDate
  'dayAvailability': 56, // Number | Number of days of day availability to return
  'firstDayAvailable': true // Boolean | Return available times for the first available day
};
apiInstance.consumerV1AvailabilityServiceIdStartDateEndDateGet(serviceId, startDate, endDate, opts, (error, data, response) => {
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
 **serviceId** | **String**| Service Id for availability search | 
 **startDate** | **Date**| Format YYYY-MM-DD: Start Date for availability search | 
 **endDate** | **Date**| Format YYYY-MM-DD: End Date for availability search | 
 **startTime** | **Number**| Format Military Time Start Time for availability search. Defaults to Business Hours Start | [optional] 
 **endTime** | **Number**| Format Military Time. End Time for availability search. Defaults to Business Hours End | [optional] 
 **locationId** | **String**| Id of business location, defaults to primary business location | [optional] 
 **resourceId** | **String**| Resource Id for availability search | [optional] 
 **resourceGroupId** | **String**| Resource Group Id for availability search | [optional] 
 **resourceIds** | **String**| Comma separated Resource Id&#39;s for availability search | [optional] 
 **roundRobin** | **String**| Round robin choice 0&#x3D;none, 1&#x3D;random, 2&#x3D;balanced | [optional] 
 **duration** | **Number**| Duration of the service if different from default | [optional] 
 **interval** | **Number**| Booking Interval if different than the default | [optional] 
 **timezoneName** | **String**| Requested IANA timezone Id to view availability | [optional] 
 **tzOffset** | **Number**| Request timezone offset to view availability | [optional] 
 **destination** | **String**| For calculating travel based availability, requires distance scope | [optional] 
 **dayAvailabilityStartDate** | **Date**| Format YYYY-DD-YY: Start date for day availability, defaults to startDate | [optional] 
 **dayAvailability** | **Number**| Number of days of day availability to return | [optional] 
 **firstDayAvailable** | **Boolean**| Return available times for the first available day | [optional] 

### Return type

[**AvailabilityViewModel**](AvailabilityViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## consumerV1AvailabilityServiceIdStartDateEndDateUnavailableGet

> UnavailableTimeListViewModel consumerV1AvailabilityServiceIdStartDateEndDateUnavailableGet(serviceId, startDate, endDate, opts)

Get Unavailable Times

&lt;p&gt;This endpoint is used to show &lt;b&gt;Unavailable&lt;/b&gt; times and provides valuable information as to why a time slot is unavailable. If you question your availability results, populate the same parameters to this endpoint to find out why.&lt;/p&gt;  &lt;p&gt;A &lt;b&gt;serviceId&lt;/b&gt; is required. The &lt;b&gt;startDate&lt;/b&gt; and &lt;b&gt;endDate&lt;/b&gt; are required and are formatted as: &lt;b&gt;YYYY-MM-DD&lt;/b&gt;&lt;/p&gt;  &lt;p&gt;Location hours, holidays, services, resources, blocks, allocations, and appointments are just some of variables that may cause time slots to become unavailable. Use this endpoint to understand why you don&#39;t see availability.&lt;/p&gt;

### Example

```javascript
import OnSchedConsumerApi from 'on_sched_consumer_api';
let defaultClient = OnSchedConsumerApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new OnSchedConsumerApi.AvailabilityApi();
let serviceId = "serviceId_example"; // String | Service Id for availability search
let startDate = new Date("2013-10-20T19:20:30+01:00"); // Date | Format YYYY-MM-DD: Start Date for unavailable time search
let endDate = new Date("2013-10-20T19:20:30+01:00"); // Date | Format YYYY-MM-DD: End Date for unavailable time search
let opts = {
  'locationId': "locationId_example", // String | Id of business location, defaults to primary business location
  'resourceId': "resourceId_example", // String | Resource Id to filter on
  'duration': 56, // Number | Duration of the service if different from default
  'tzOffset': 56, // Number | Request timezone offset to view unavailable times
  'skipTimePastUnavailability': true // Boolean | Set as true to remove Time Past (TP) blocks in the response
};
apiInstance.consumerV1AvailabilityServiceIdStartDateEndDateUnavailableGet(serviceId, startDate, endDate, opts, (error, data, response) => {
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
 **serviceId** | **String**| Service Id for availability search | 
 **startDate** | **Date**| Format YYYY-MM-DD: Start Date for unavailable time search | 
 **endDate** | **Date**| Format YYYY-MM-DD: End Date for unavailable time search | 
 **locationId** | **String**| Id of business location, defaults to primary business location | [optional] 
 **resourceId** | **String**| Resource Id to filter on | [optional] 
 **duration** | **Number**| Duration of the service if different from default | [optional] 
 **tzOffset** | **Number**| Request timezone offset to view unavailable times | [optional] 
 **skipTimePastUnavailability** | **Boolean**| Set as true to remove Time Past (TP) blocks in the response | [optional] 

### Return type

[**UnavailableTimeListViewModel**](UnavailableTimeListViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

