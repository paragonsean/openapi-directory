# ScheduleMesagesApi

All URIs are relative to *https://rest.iad-01.braze.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getUpcomingScheduledCampaignsAndCanvases_0**](ScheduleMesagesApi.md#getUpcomingScheduledCampaignsAndCanvases_0) | **GET** /messages/scheduled_broadcasts | Get Upcoming Scheduled Campaigns and Canvases |
| [**scheduleApiTriggeredCanvases_0**](ScheduleMesagesApi.md#scheduleApiTriggeredCanvases_0) | **POST** /canvas/trigger/schedule/create | Schedule API Triggered Canvases |


<a id="getUpcomingScheduledCampaignsAndCanvases_0"></a>
# **getUpcomingScheduledCampaignsAndCanvases_0**
> getUpcomingScheduledCampaignsAndCanvases_0(endTime)

Get Upcoming Scheduled Campaigns and Canvases

You can view a JSON list of upcoming and scheduled Campaigns and Canvases using the following information and parameters. The endpoint will return information about scheduled Campaigns and entry Canvases between now and the designated end_time (ISO 8601 format) specified in the request. Daily, recurring messages will only appear once with their next occurrence. Results returned in this endpoint are only for Campaigns and Canvases created and scheduled in Braze.  ## Response  &#x60;&#x60;&#x60;json Content-Type: application/json Authorization: Bearer YOUR-REST-API-KEY {     \&quot;scheduled_broadcasts\&quot;: [       # Example Canvas       {         \&quot;name\&quot; &#x3D;&gt; String,         \&quot;id\&quot; &#x3D;&gt; String,         \&quot;type\&quot; &#x3D;&gt; \&quot;Canvas\&quot;,         \&quot;tags\&quot; &#x3D;&gt; [String tag names],         \&quot;next_send_time\&quot; &#x3D;&gt; \&quot;YYYY-MM-DD HH:mm:ss\&quot; (may also include time zone if not local/intelligent delivery)         \&quot;schedule_type\&quot; &#x3D;&gt; one of \&quot;local_time_zones\&quot;, \&quot;intelligent_delivery\&quot;, or the name of your company&#39;s time zone       },       # Example Campaign       {         \&quot;name\&quot; &#x3D;&gt; String,         \&quot;id\&quot; &#x3D;&gt; String,         \&quot;type\&quot; &#x3D;&gt; \&quot;Campaign\&quot;,         \&quot;tags\&quot; &#x3D;&gt; [String tag names],         \&quot;next_send_time\&quot; &#x3D;&gt; \&quot;YYYY-MM-DD HH:mm:ss\&quot; (may also include time zone if not local/intelligent delivery)         \&quot;schedule_type\&quot; &#x3D;&gt; one of \&quot;local_time_zones\&quot;, \&quot;intelligent_delivery\&quot;, or the name of your company&#39;s time zone       },     ] } &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScheduleMesagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rest.iad-01.braze.com");

    ScheduleMesagesApi apiInstance = new ScheduleMesagesApi(defaultClient);
    String endTime = "2018-09-01T00:00:00-04:00"; // String | (Required) String in ISO 8601 format  End date of the range to retrieve upcoming scheduled Campaigns and Canvases. This is treated as midnight in UTC time by the API.
    try {
      apiInstance.getUpcomingScheduledCampaignsAndCanvases_0(endTime);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScheduleMesagesApi#getUpcomingScheduledCampaignsAndCanvases_0");
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
| **endTime** | **String**| (Required) String in ISO 8601 format  End date of the range to retrieve upcoming scheduled Campaigns and Canvases. This is treated as midnight in UTC time by the API. | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="scheduleApiTriggeredCanvases_0"></a>
# **scheduleApiTriggeredCanvases_0**
> scheduleApiTriggeredCanvases_0(scheduleApiTriggeredCanvasesRequest)

Schedule API Triggered Canvases

Use this endpoint to trigger API Triggered Canvases, which are created on the Dashboard and initiated via the API. You can pass in &#x60;canvas_entry_properties&#x60; that will be templated into the messages sent by the first steps of the Canvas.  This endpoint allows you to schedule Canvas messages (up to 90 days in advance) via API Triggered delivery, allowing you to decide what action should trigger the message to be sent. Please note that to send messages with this endpoint, you must have a Canvas ID, created when you build a Canvas.  ### Request Parameters  | Parameter | Required | Data Type | Description | | --------- | ---------| --------- | ----------- | |&#x60;canvas_id&#x60;|Required|String| See canvas identifier| |&#x60;send_id&#x60; | Optional | String | See send identifier | |&#x60;recipients&#x60; | Optional | Array of recipient objects | See recipients object | |&#x60;audience&#x60; | Optional | Connected audience object | See connected audience | |&#x60;broadcast&#x60; | Optional | Boolean | See broadcast -- defaults to false on 8/31/17, must be set to true if \&quot;recipients\&quot; object is omitted | | &#x60;trigger_properties&#x60; | Optional | Object | Personalization key value pairs for all users in this send; see trigger properties | | &#x60;schedule&#x60; | Required | Schedule object | See schedule object |  ## Request Components - [Canvas Identifier](https://www.braze.com/docs/api/identifier_types/) - [Recipients](https://www.braze.com/docs/api/objects_filters/recipient_object/) - [Connected Audience](https://www.braze.com/docs/api/objects_filters/connected_audience/) - [Broadcast](https://www.braze.com/docs/api/parameters/#broadcast) - [Trigger Properties](https://www.braze.com/docs/api/objects_filters/trigger_properties_object/) - [Schedule Object](https://www.braze.com/docs/api/objects_filters/schedule_object/)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScheduleMesagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rest.iad-01.braze.com");

    ScheduleMesagesApi apiInstance = new ScheduleMesagesApi(defaultClient);
    ScheduleApiTriggeredCanvasesRequest scheduleApiTriggeredCanvasesRequest = new ScheduleApiTriggeredCanvasesRequest(); // ScheduleApiTriggeredCanvasesRequest | 
    try {
      apiInstance.scheduleApiTriggeredCanvases_0(scheduleApiTriggeredCanvasesRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScheduleMesagesApi#scheduleApiTriggeredCanvases_0");
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
| **scheduleApiTriggeredCanvasesRequest** | [**ScheduleApiTriggeredCanvasesRequest**](ScheduleApiTriggeredCanvasesRequest.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

