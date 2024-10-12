# VoiceV1ArchivedCallApi

All URIs are relative to *https://voice.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deleteArchivedCall**](VoiceV1ArchivedCallApi.md#deleteArchivedCall) | **DELETE** /v1/Archives/{Date}/Calls/{Sid} |  |


<a id="deleteArchivedCall"></a>
# **deleteArchivedCall**
> deleteArchivedCall(date, sid)



Delete an archived call record from Bulk Export. Note: this does not also delete the record from the Voice API.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VoiceV1ArchivedCallApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://voice.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    VoiceV1ArchivedCallApi apiInstance = new VoiceV1ArchivedCallApi(defaultClient);
    LocalDate date = LocalDate.now(); // LocalDate | The date of the Call in UTC.
    String sid = "sid_example"; // String | The Twilio-provided Call SID that uniquely identifies the Call resource to delete
    try {
      apiInstance.deleteArchivedCall(date, sid);
    } catch (ApiException e) {
      System.err.println("Exception when calling VoiceV1ArchivedCallApi#deleteArchivedCall");
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
| **date** | **LocalDate**| The date of the Call in UTC. | |
| **sid** | **String**| The Twilio-provided Call SID that uniquely identifies the Call resource to delete | |

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The resource was deleted successfully. |  -  |

