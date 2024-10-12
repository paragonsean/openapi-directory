# BulkexportsV1ExportConfigurationApi

All URIs are relative to *https://bulkexports.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**fetchExportConfiguration**](BulkexportsV1ExportConfigurationApi.md#fetchExportConfiguration) | **GET** /v1/Exports/{ResourceType}/Configuration |  |
| [**updateExportConfiguration**](BulkexportsV1ExportConfigurationApi.md#updateExportConfiguration) | **POST** /v1/Exports/{ResourceType}/Configuration |  |


<a id="fetchExportConfiguration"></a>
# **fetchExportConfiguration**
> BulkexportsV1ExportConfiguration fetchExportConfiguration(resourceType)



Fetch a specific Export Configuration.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BulkexportsV1ExportConfigurationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://bulkexports.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    BulkexportsV1ExportConfigurationApi apiInstance = new BulkexportsV1ExportConfigurationApi(defaultClient);
    String resourceType = "resourceType_example"; // String | The type of communication – Messages, Calls, Conferences, and Participants
    try {
      BulkexportsV1ExportConfiguration result = apiInstance.fetchExportConfiguration(resourceType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BulkexportsV1ExportConfigurationApi#fetchExportConfiguration");
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

### Return type

[**BulkexportsV1ExportConfiguration**](BulkexportsV1ExportConfiguration.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updateExportConfiguration"></a>
# **updateExportConfiguration**
> BulkexportsV1ExportConfiguration updateExportConfiguration(resourceType, enabled, webhookMethod, webhookUrl)



Update a specific Export Configuration.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BulkexportsV1ExportConfigurationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://bulkexports.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    BulkexportsV1ExportConfigurationApi apiInstance = new BulkexportsV1ExportConfigurationApi(defaultClient);
    String resourceType = "resourceType_example"; // String | The type of communication – Messages, Calls, Conferences, and Participants
    Boolean enabled = true; // Boolean | If true, Twilio will automatically generate every day's file when the day is over.
    String webhookMethod = "webhookMethod_example"; // String | Sets whether Twilio should call a webhook URL when the automatic generation is complete, using GET or POST. The actual destination is set in the webhook_url
    URI webhookUrl = new URI(); // URI | Stores the URL destination for the method specified in webhook_method.
    try {
      BulkexportsV1ExportConfiguration result = apiInstance.updateExportConfiguration(resourceType, enabled, webhookMethod, webhookUrl);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BulkexportsV1ExportConfigurationApi#updateExportConfiguration");
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
| **enabled** | **Boolean**| If true, Twilio will automatically generate every day&#39;s file when the day is over. | [optional] |
| **webhookMethod** | **String**| Sets whether Twilio should call a webhook URL when the automatic generation is complete, using GET or POST. The actual destination is set in the webhook_url | [optional] |
| **webhookUrl** | **URI**| Stores the URL destination for the method specified in webhook_method. | [optional] |

### Return type

[**BulkexportsV1ExportConfiguration**](BulkexportsV1ExportConfiguration.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

