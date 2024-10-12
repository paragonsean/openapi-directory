# BulkexportsV1ExportCustomJobApi

All URIs are relative to *https://bulkexports.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createExportCustomJob**](BulkexportsV1ExportCustomJobApi.md#createExportCustomJob) | **POST** /v1/Exports/{ResourceType}/Jobs |  |
| [**listExportCustomJob**](BulkexportsV1ExportCustomJobApi.md#listExportCustomJob) | **GET** /v1/Exports/{ResourceType}/Jobs |  |


<a id="createExportCustomJob"></a>
# **createExportCustomJob**
> BulkexportsV1ExportExportCustomJob createExportCustomJob(resourceType, endDay, friendlyName, startDay, email, webhookMethod, webhookUrl)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BulkexportsV1ExportCustomJobApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://bulkexports.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    BulkexportsV1ExportCustomJobApi apiInstance = new BulkexportsV1ExportCustomJobApi(defaultClient);
    String resourceType = "resourceType_example"; // String | The type of communication – Messages or Calls, Conferences, and Participants
    String endDay = "endDay_example"; // String | The end day for the custom export specified as a string in the format of yyyy-mm-dd. End day is inclusive and must be 2 days earlier than the current UTC day.
    String friendlyName = "friendlyName_example"; // String | The friendly name specified when creating the job
    String startDay = "startDay_example"; // String | The start day for the custom export specified as a string in the format of yyyy-mm-dd
    String email = "email_example"; // String | The optional email to send the completion notification to. You can set both webhook, and email, or one or the other. If you set neither, the job will run but you will have to query to determine your job's status.
    String webhookMethod = "webhookMethod_example"; // String | This is the method used to call the webhook on completion of the job. If this is supplied, `WebhookUrl` must also be supplied.
    String webhookUrl = "webhookUrl_example"; // String | The optional webhook url called on completion of the job. If this is supplied, `WebhookMethod` must also be supplied. If you set neither webhook nor email, you will have to check your job's status manually.
    try {
      BulkexportsV1ExportExportCustomJob result = apiInstance.createExportCustomJob(resourceType, endDay, friendlyName, startDay, email, webhookMethod, webhookUrl);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BulkexportsV1ExportCustomJobApi#createExportCustomJob");
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
| **resourceType** | **String**| The type of communication – Messages or Calls, Conferences, and Participants | |
| **endDay** | **String**| The end day for the custom export specified as a string in the format of yyyy-mm-dd. End day is inclusive and must be 2 days earlier than the current UTC day. | |
| **friendlyName** | **String**| The friendly name specified when creating the job | |
| **startDay** | **String**| The start day for the custom export specified as a string in the format of yyyy-mm-dd | |
| **email** | **String**| The optional email to send the completion notification to. You can set both webhook, and email, or one or the other. If you set neither, the job will run but you will have to query to determine your job&#39;s status. | [optional] |
| **webhookMethod** | **String**| This is the method used to call the webhook on completion of the job. If this is supplied, &#x60;WebhookUrl&#x60; must also be supplied. | [optional] |
| **webhookUrl** | **String**| The optional webhook url called on completion of the job. If this is supplied, &#x60;WebhookMethod&#x60; must also be supplied. If you set neither webhook nor email, you will have to check your job&#39;s status manually. | [optional] |

### Return type

[**BulkexportsV1ExportExportCustomJob**](BulkexportsV1ExportExportCustomJob.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="listExportCustomJob"></a>
# **listExportCustomJob**
> ListExportCustomJobResponse listExportCustomJob(resourceType, pageSize, page, pageToken)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BulkexportsV1ExportCustomJobApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://bulkexports.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    BulkexportsV1ExportCustomJobApi apiInstance = new BulkexportsV1ExportCustomJobApi(defaultClient);
    String resourceType = "resourceType_example"; // String | The type of communication – Messages, Calls, Conferences, and Participants
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListExportCustomJobResponse result = apiInstance.listExportCustomJob(resourceType, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BulkexportsV1ExportCustomJobApi#listExportCustomJob");
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
| **resourceType** | **String**| The type of communication – Messages, Calls, Conferences, and Participants | |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListExportCustomJobResponse**](ListExportCustomJobResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

