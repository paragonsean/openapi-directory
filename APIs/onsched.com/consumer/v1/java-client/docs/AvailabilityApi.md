# AvailabilityApi

All URIs are relative to *https://sandbox-api.onsched.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**consumerV1AvailabilityServiceIdStartDateEndDateDaysGet**](AvailabilityApi.md#consumerV1AvailabilityServiceIdStartDateEndDateDaysGet) | **GET** /consumer/v1/availability/{serviceId}/{startDate}/{endDate}/days | Get Available Days |
| [**consumerV1AvailabilityServiceIdStartDateEndDateGet**](AvailabilityApi.md#consumerV1AvailabilityServiceIdStartDateEndDateGet) | **GET** /consumer/v1/availability/{serviceId}/{startDate}/{endDate} | Get Available Times |
| [**consumerV1AvailabilityServiceIdStartDateEndDateUnavailableGet**](AvailabilityApi.md#consumerV1AvailabilityServiceIdStartDateEndDateUnavailableGet) | **GET** /consumer/v1/availability/{serviceId}/{startDate}/{endDate}/unavailable | Get Unavailable Times |


<a id="consumerV1AvailabilityServiceIdStartDateEndDateDaysGet"></a>
# **consumerV1AvailabilityServiceIdStartDateEndDateDaysGet**
> AvailabilityDayViewModel consumerV1AvailabilityServiceIdStartDateEndDateDaysGet(serviceId, startDate, endDate, locationId, resourceId, tzOffset)

Get Available Days

&lt;p&gt;This endpoint will return &lt;b&gt;Day Level Availability&lt;/b&gt; for the range of dates requested. For example, if the business is closed, or there is a public holiday this endpoint will return that the \&quot;Day is unavailable\&quot;.&lt;/p&gt;  &lt;p&gt;Day Availability is a high-level check for Holidays and Open/Available hours of a location, service and/or resource and should be used to restrict your choices of days available in your application to improve usability and performance.&lt;/p&gt;  &lt;p&gt;A &lt;b&gt;serviceId&lt;/b&gt; is required. The &lt;b&gt;startDate&lt;/b&gt; and &lt;b&gt;endDate&lt;/b&gt; are required and are formatted as: &lt;b&gt;YYYY-MM-DD&lt;/b&gt;&lt;/p&gt;  &lt;p&gt;The locationId is optional, however if not supplied it defaults to the Primary Business Location for open/closed hours information. It is recommended you always provide the locationId.&lt;/p&gt;  &lt;p&gt;A &lt;b&gt;resourceId&lt;/b&gt; is optional. If used the available days will be return day availability for the resource specified.&lt;/p&gt;  &lt;p&gt;The &lt;b&gt;tzOffset&lt;/b&gt; parameter should be used if the appointment requester, the end user, is in a different timezone than the location or resource.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AvailabilityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sandbox-api.onsched.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    AvailabilityApi apiInstance = new AvailabilityApi(defaultClient);
    String serviceId = "serviceId_example"; // String | Service Id for day availability search
    OffsetDateTime startDate = OffsetDateTime.now(); // OffsetDateTime | Format YYYY-MM-DD: Start Date for availability search
    OffsetDateTime endDate = OffsetDateTime.now(); // OffsetDateTime | Format YYYY-MM-DD: End Date for availability search
    String locationId = "locationId_example"; // String | Id of business location, defaults to primary business location
    String resourceId = "resourceId_example"; // String | Resource Id to filter on
    Integer tzOffset = 56; // Integer | Timezone offset to view availability for
    try {
      AvailabilityDayViewModel result = apiInstance.consumerV1AvailabilityServiceIdStartDateEndDateDaysGet(serviceId, startDate, endDate, locationId, resourceId, tzOffset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AvailabilityApi#consumerV1AvailabilityServiceIdStartDateEndDateDaysGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **serviceId** | **String**| Service Id for day availability search | |
| **startDate** | **OffsetDateTime**| Format YYYY-MM-DD: Start Date for availability search | |
| **endDate** | **OffsetDateTime**| Format YYYY-MM-DD: End Date for availability search | |
| **locationId** | **String**| Id of business location, defaults to primary business location | [optional] |
| **resourceId** | **String**| Resource Id to filter on | [optional] |
| **tzOffset** | **Integer**| Timezone offset to view availability for | [optional] |

### Return type

[**AvailabilityDayViewModel**](AvailabilityDayViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="consumerV1AvailabilityServiceIdStartDateEndDateGet"></a>
# **consumerV1AvailabilityServiceIdStartDateEndDateGet**
> AvailabilityViewModel consumerV1AvailabilityServiceIdStartDateEndDateGet(serviceId, startDate, endDate, startTime, endTime, locationId, resourceId, resourceGroupId, resourceIds, roundRobin, duration, interval, timezoneName, tzOffset, destination, dayAvailabilityStartDate, dayAvailability, firstDayAvailable)

Get Available Times

&lt;p&gt;    &lt;b&gt;Choose your search criteria carefully. Availability is an expensive call.&lt;/b&gt; If you search availability for all resources, you should only do so for a single date. If you search availability for multiple dates, you should only do so for a specific resource by specifying the optional resourceId parameter.&lt;/p&gt;  &lt;p&gt;A &lt;b&gt;serviceId&lt;/b&gt; is required. The &lt;b&gt;startDate&lt;/b&gt; and &lt;b&gt;endDate&lt;/b&gt; are required and are formatted as: &lt;b&gt;YYYY-MM-DD&lt;/b&gt;&lt;/p&gt;  &lt;p&gt;A &lt;b&gt;resourceId&lt;/b&gt; is optional, it is recommended if known at the time of availability call.&lt;/p&gt;  &lt;p&gt;    &lt;b&gt;timezoneName&lt;/b&gt; is optional, it allows you to specify the IANA formatted name for the end user&#39;s timezone to view availability. e.g., &lt;i&gt;America/New_York&lt;/i&gt;. &lt;b&gt;NOTE: This is the recommended approach for your implementation.&lt;/b&gt;  The \&quot;tzOffset\&quot; parameter remains for backward compatibility.  For JavaScript, use moment.js in your client for ease of timezone detection and selection. For iOS, use the name property of the NSTimeZone returned from the localTimeZone method. For .NET, consider NodaTime or TimeZoneConverter via NuGet. &lt;/p&gt;  &lt;p&gt;    &lt;b&gt;duration&lt;/b&gt; should only be populated if you allow the end user to select a duration, otherwise the service&#39;s duration will be used.&lt;/p&gt;  &lt;p&gt;    &lt;b&gt;startTime&lt;/b&gt; and &lt;b&gt;endTime&lt;/b&gt; are optional and are specified in &lt;b&gt;military time e.g., 800 &#x3D; 8:00am, 2230 &#x3D; 10:30pm&lt;/b&gt;. Note: You will only see availability within the boundary of your business location start and end times.&lt;/p&gt;  &lt;p&gt;    &lt;b&gt;dayAvailability&lt;/b&gt; will return day level availability for the number of days requested from the start date. See &lt;i&gt;GET /consumer/v1/availability/{serviceId}/{startDate}/{endDate}/days&lt;/i&gt; for details.&lt;/p&gt;  &lt;p&gt;    &lt;b&gt;firstDayAvailable&lt;/b&gt; only works with day availability. If set to true it will look for the first day available within the range specified by the dayAvailability parameter. The two parameters together can be a clever way to display availability for a week or month. Tip - pass in the beginning of the week or month, and available times are displayed for the first available date if exists.&lt;/p&gt;  &lt;p&gt;    &lt;b&gt;tzOffset&lt;/b&gt; allows you to pass in the timezone offset for the end user&#39;s timezone of choice, e.g., (-240) for EST. If you use this option, your application should be timezone aware. The requested timezone is specified as an offset (plus or minus) from GMT time.&lt;/p&gt;  &lt;p&gt;Availability can be complex. For further troubleshooting refer to the: &lt;i&gt;&lt;b&gt;GET /consumer/v1/availability/{serviceId}/{startDate}/{endDate}/unavailable&lt;/b&gt;&lt;/i&gt; endpoint. This endpoint will show you all unavailable times for a given date range. Available times are created from any unblocked time periods. For more information: &lt;a href&#x3D;\&quot;https://onsched.readme.io/docs/availability-overview\&quot;&gt;Availability Overview&lt;/a&gt;&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AvailabilityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sandbox-api.onsched.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    AvailabilityApi apiInstance = new AvailabilityApi(defaultClient);
    String serviceId = "serviceId_example"; // String | Service Id for availability search
    OffsetDateTime startDate = OffsetDateTime.now(); // OffsetDateTime | Format YYYY-MM-DD: Start Date for availability search
    OffsetDateTime endDate = OffsetDateTime.now(); // OffsetDateTime | Format YYYY-MM-DD: End Date for availability search
    Integer startTime = 56; // Integer | Format Military Time Start Time for availability search. Defaults to Business Hours Start
    Integer endTime = 56; // Integer | Format Military Time. End Time for availability search. Defaults to Business Hours End
    String locationId = "locationId_example"; // String | Id of business location, defaults to primary business location
    String resourceId = "resourceId_example"; // String | Resource Id for availability search
    String resourceGroupId = "resourceGroupId_example"; // String | Resource Group Id for availability search
    String resourceIds = "resourceIds_example"; // String | Comma separated Resource Id's for availability search
    String roundRobin = "roundRobin_example"; // String | Round robin choice 0=none, 1=random, 2=balanced
    Integer duration = 56; // Integer | Duration of the service if different from default
    Integer interval = 56; // Integer | Booking Interval if different than the default
    String timezoneName = "timezoneName_example"; // String | Requested IANA timezone Id to view availability
    Integer tzOffset = 56; // Integer | Request timezone offset to view availability
    String destination = "destination_example"; // String | For calculating travel based availability, requires distance scope
    OffsetDateTime dayAvailabilityStartDate = OffsetDateTime.now(); // OffsetDateTime | Format YYYY-DD-YY: Start date for day availability, defaults to startDate
    Integer dayAvailability = 56; // Integer | Number of days of day availability to return
    Boolean firstDayAvailable = true; // Boolean | Return available times for the first available day
    try {
      AvailabilityViewModel result = apiInstance.consumerV1AvailabilityServiceIdStartDateEndDateGet(serviceId, startDate, endDate, startTime, endTime, locationId, resourceId, resourceGroupId, resourceIds, roundRobin, duration, interval, timezoneName, tzOffset, destination, dayAvailabilityStartDate, dayAvailability, firstDayAvailable);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AvailabilityApi#consumerV1AvailabilityServiceIdStartDateEndDateGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **serviceId** | **String**| Service Id for availability search | |
| **startDate** | **OffsetDateTime**| Format YYYY-MM-DD: Start Date for availability search | |
| **endDate** | **OffsetDateTime**| Format YYYY-MM-DD: End Date for availability search | |
| **startTime** | **Integer**| Format Military Time Start Time for availability search. Defaults to Business Hours Start | [optional] |
| **endTime** | **Integer**| Format Military Time. End Time for availability search. Defaults to Business Hours End | [optional] |
| **locationId** | **String**| Id of business location, defaults to primary business location | [optional] |
| **resourceId** | **String**| Resource Id for availability search | [optional] |
| **resourceGroupId** | **String**| Resource Group Id for availability search | [optional] |
| **resourceIds** | **String**| Comma separated Resource Id&#39;s for availability search | [optional] |
| **roundRobin** | **String**| Round robin choice 0&#x3D;none, 1&#x3D;random, 2&#x3D;balanced | [optional] |
| **duration** | **Integer**| Duration of the service if different from default | [optional] |
| **interval** | **Integer**| Booking Interval if different than the default | [optional] |
| **timezoneName** | **String**| Requested IANA timezone Id to view availability | [optional] |
| **tzOffset** | **Integer**| Request timezone offset to view availability | [optional] |
| **destination** | **String**| For calculating travel based availability, requires distance scope | [optional] |
| **dayAvailabilityStartDate** | **OffsetDateTime**| Format YYYY-DD-YY: Start date for day availability, defaults to startDate | [optional] |
| **dayAvailability** | **Integer**| Number of days of day availability to return | [optional] |
| **firstDayAvailable** | **Boolean**| Return available times for the first available day | [optional] |

### Return type

[**AvailabilityViewModel**](AvailabilityViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="consumerV1AvailabilityServiceIdStartDateEndDateUnavailableGet"></a>
# **consumerV1AvailabilityServiceIdStartDateEndDateUnavailableGet**
> UnavailableTimeListViewModel consumerV1AvailabilityServiceIdStartDateEndDateUnavailableGet(serviceId, startDate, endDate, locationId, resourceId, duration, tzOffset, skipTimePastUnavailability)

Get Unavailable Times

&lt;p&gt;This endpoint is used to show &lt;b&gt;Unavailable&lt;/b&gt; times and provides valuable information as to why a time slot is unavailable. If you question your availability results, populate the same parameters to this endpoint to find out why.&lt;/p&gt;  &lt;p&gt;A &lt;b&gt;serviceId&lt;/b&gt; is required. The &lt;b&gt;startDate&lt;/b&gt; and &lt;b&gt;endDate&lt;/b&gt; are required and are formatted as: &lt;b&gt;YYYY-MM-DD&lt;/b&gt;&lt;/p&gt;  &lt;p&gt;Location hours, holidays, services, resources, blocks, allocations, and appointments are just some of variables that may cause time slots to become unavailable. Use this endpoint to understand why you don&#39;t see availability.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AvailabilityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sandbox-api.onsched.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    AvailabilityApi apiInstance = new AvailabilityApi(defaultClient);
    String serviceId = "serviceId_example"; // String | Service Id for availability search
    OffsetDateTime startDate = OffsetDateTime.now(); // OffsetDateTime | Format YYYY-MM-DD: Start Date for unavailable time search
    OffsetDateTime endDate = OffsetDateTime.now(); // OffsetDateTime | Format YYYY-MM-DD: End Date for unavailable time search
    String locationId = "locationId_example"; // String | Id of business location, defaults to primary business location
    String resourceId = "resourceId_example"; // String | Resource Id to filter on
    Integer duration = 56; // Integer | Duration of the service if different from default
    Integer tzOffset = 56; // Integer | Request timezone offset to view unavailable times
    Boolean skipTimePastUnavailability = true; // Boolean | Set as true to remove Time Past (TP) blocks in the response
    try {
      UnavailableTimeListViewModel result = apiInstance.consumerV1AvailabilityServiceIdStartDateEndDateUnavailableGet(serviceId, startDate, endDate, locationId, resourceId, duration, tzOffset, skipTimePastUnavailability);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AvailabilityApi#consumerV1AvailabilityServiceIdStartDateEndDateUnavailableGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **serviceId** | **String**| Service Id for availability search | |
| **startDate** | **OffsetDateTime**| Format YYYY-MM-DD: Start Date for unavailable time search | |
| **endDate** | **OffsetDateTime**| Format YYYY-MM-DD: End Date for unavailable time search | |
| **locationId** | **String**| Id of business location, defaults to primary business location | [optional] |
| **resourceId** | **String**| Resource Id to filter on | [optional] |
| **duration** | **Integer**| Duration of the service if different from default | [optional] |
| **tzOffset** | **Integer**| Request timezone offset to view unavailable times | [optional] |
| **skipTimePastUnavailability** | **Boolean**| Set as true to remove Time Past (TP) blocks in the response | [optional] |

### Return type

[**UnavailableTimeListViewModel**](UnavailableTimeListViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

