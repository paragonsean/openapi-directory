# ActivityApi

All URIs are relative to *https://accountname.exavault.com/api/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getSessionLogs**](ActivityApi.md#getSessionLogs) | **GET** /activity/session | Get activity logs |
| [**getWebhookLogs**](ActivityApi.md#getWebhookLogs) | **GET** /activity/webhooks | Get webhook logs |


<a id="getSessionLogs"></a>
# **getSessionLogs**
> SessionActivityResponse getSessionLogs(evApiKey, evAccessToken, startDate, endDate, ipAddress, username, path, type, offset, limit, sort)

Get activity logs

Returns the detailed activity logs for your account. Optional query paramaters will filter the returned results based on a number of options including usernames, activity types, or date ranges.   **NOTE:** Total Results will always return as 0 to avoid quering data you&#39;re not using and stay as performant as possible.     **Operation Types** Session activity is logged with an operation type that is different from what is visible through the [activity log interface in the web file manager](/docs/account/10-activity-logs/00-activity-logs). Consult the table below to compare the two:  | File Manager Value | API Value | Notes | |-----|----|---| | Connect | PASS | | | Disconnect | EXIT | | | Upload | STOR | | | Download | RETR | | | Delete | DELE | | | Create Folder | MKD | | | Rename | RNTO | | | Move | MOVE | | | Copy | COPY | | | Compress | COMPR | | | Extract | EXTRACT | | | Shared Folders | SHARE | | | Send Files | SEND | | | Receive Files | RECV | | | _N/A_ | EDIT\\_SEND | Update send. Not shown in file manager | | Update Share | EDIT\\_SHARE| |  | Update Receive | EDIT\\_RECV | | | Delete Send | DELE\\_SEND | | | Delete Receive | DELE\\_RECV | | | Delete Share | DELE\\_SHARE | | | Create Notification | NOTIFY | | | Update Notification | EDIT\\_NTFY| | | Delete Notification | DELE\\_NTFY | | | Create User | USER | | | Update User | EDIT\\_USER | | | Delete User | DELE\\_USER | | | _N/A_ | DFA | Create direct link. Not shown in file manager | | _N/A_ | EDIT\\_DFA | Update direct link options. Not shown in file manager | | _N/A_ | DELE\\_DFA | Deactivate direct link. Not shown in file manager| 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActivityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://accountname.exavault.com/api/v2");

    ActivityApi apiInstance = new ActivityApi(defaultClient);
    String evApiKey = "exampleaccount-zwSuWUZ8S38h33qPS8v0s"; // String | API Key
    String evAccessToken = "19853ef63a0bc348024a9e4cfd4a92520d2dfd04e88d8679fb1ed6bc551593d1"; // String | Access Token
    OffsetDateTime startDate = OffsetDateTime.parse("2019-10-18T06:48:40Z"); // OffsetDateTime | Start date of the filter data range
    OffsetDateTime endDate = OffsetDateTime.parse("2019-10-18T06:48:40Z"); // OffsetDateTime | End date of the filter data range
    String ipAddress = "127.0.0.1"; // String | Used to filter session logs by ip address.
    String username = "jdoe"; // String | Username used for filtering a list
    String path = "/folder*"; // String | Path used to filter records
    String type = "EDIT_SHARE"; // String | Filter session logs for operation type (see table above for acceptable values)
    Integer offset = 100; // Integer | Offset of the records list
    Integer limit = 10; // Integer | Limit of the records list
    String sort = "-date"; // String | Comma separated list sort params
    try {
      SessionActivityResponse result = apiInstance.getSessionLogs(evApiKey, evAccessToken, startDate, endDate, ipAddress, username, path, type, offset, limit, sort);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActivityApi#getSessionLogs");
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
| **evApiKey** | **String**| API Key | |
| **evAccessToken** | **String**| Access Token | |
| **startDate** | **OffsetDateTime**| Start date of the filter data range | [optional] |
| **endDate** | **OffsetDateTime**| End date of the filter data range | [optional] |
| **ipAddress** | **String**| Used to filter session logs by ip address. | [optional] |
| **username** | **String**| Username used for filtering a list | [optional] |
| **path** | **String**| Path used to filter records | [optional] |
| **type** | **String**| Filter session logs for operation type (see table above for acceptable values) | [optional] |
| **offset** | **Integer**| Offset of the records list | [optional] |
| **limit** | **Integer**| Limit of the records list | [optional] |
| **sort** | **String**| Comma separated list sort params | [optional] |

### Return type

[**SessionActivityResponse**](SessionActivityResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getWebhookLogs"></a>
# **getWebhookLogs**
> WebhookActivityResponse getWebhookLogs(evApiKey, evAccessToken, startDate, endDate, endpointUrl, event, statusCode, resourcePath, username, offset, limit, sort)

Get webhook logs

Returns the webhook logs for your account. Use the available query parameters to filter the listing of activity that is returned.  **NOTE:** Total Results will always return as 0 to avoid querying data you&#39;re not using and stay as performant as possible.   **Event Types**  Webhooks are triggered by enabled event types for your account, which are configured on the [developer settings page](/docs/account/09-settings/06-developer-settings). Not all event types may be allowed for your account type. These are the valid options for event types:  - resources.upload - resources.download - resources.delete - resources.createFolder - resources.rename - resources.move - resources.copy - resources.compress - resources.extract - shares.formSubmit 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActivityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://accountname.exavault.com/api/v2");

    ActivityApi apiInstance = new ActivityApi(defaultClient);
    String evApiKey = "exampleaccount-zwSuWUZ8S38h33qPS8v0s"; // String | API Key
    String evAccessToken = "19853ef63a0bc348024a9e4cfd4a92520d2dfd04e88d8679fb1ed6bc551593d1"; // String | Access Token
    OffsetDateTime startDate = OffsetDateTime.now(); // OffsetDateTime | Earliest date of entries to include in list
    OffsetDateTime endDate = OffsetDateTime.now(); // OffsetDateTime | Latest date of entries to include in list
    URI endpointUrl = new URI(); // URI | Webhook listener endpoint
    String event = "resources.upload"; // String | Type of activity that triggered the webhook attempt
    Integer statusCode = 200; // Integer | Response code from the webhook endpoint
    String resourcePath = "/Production"; // String | Path of the resource that triggered the webhook attempt
    String username = "exampleuser"; // String | Filter by triggering username.
    Integer offset = 100; // Integer | Records to skip before returning results.
    Integer limit = 100; // Integer | Limit of the records list
    String sort = "-date,event"; // String | Comma separated list sort params
    try {
      WebhookActivityResponse result = apiInstance.getWebhookLogs(evApiKey, evAccessToken, startDate, endDate, endpointUrl, event, statusCode, resourcePath, username, offset, limit, sort);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActivityApi#getWebhookLogs");
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
| **evApiKey** | **String**| API Key | |
| **evAccessToken** | **String**| Access Token | |
| **startDate** | **OffsetDateTime**| Earliest date of entries to include in list | [optional] |
| **endDate** | **OffsetDateTime**| Latest date of entries to include in list | [optional] |
| **endpointUrl** | **URI**| Webhook listener endpoint | [optional] |
| **event** | **String**| Type of activity that triggered the webhook attempt | [optional] |
| **statusCode** | **Integer**| Response code from the webhook endpoint | [optional] |
| **resourcePath** | **String**| Path of the resource that triggered the webhook attempt | [optional] |
| **username** | **String**| Filter by triggering username. | [optional] |
| **offset** | **Integer**| Records to skip before returning results. | [optional] |
| **limit** | **Integer**| Limit of the records list | [optional] |
| **sort** | **String**| Comma separated list sort params | [optional] |

### Return type

[**WebhookActivityResponse**](WebhookActivityResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

