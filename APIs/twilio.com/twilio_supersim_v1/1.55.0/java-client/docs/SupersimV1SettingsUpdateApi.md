# SupersimV1SettingsUpdateApi

All URIs are relative to *https://supersim.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**listSettingsUpdate**](SupersimV1SettingsUpdateApi.md#listSettingsUpdate) | **GET** /v1/SettingsUpdates |  |


<a id="listSettingsUpdate"></a>
# **listSettingsUpdate**
> ListSettingsUpdateResponse listSettingsUpdate(sim, status, pageSize, page, pageToken)



Retrieve a list of Settings Updates.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SupersimV1SettingsUpdateApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://supersim.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    SupersimV1SettingsUpdateApi apiInstance = new SupersimV1SettingsUpdateApi(defaultClient);
    String sim = "sim_example"; // String | Filter the Settings Updates by a Super SIM's SID or UniqueName.
    SettingsUpdateEnumStatus status = SettingsUpdateEnumStatus.fromValue("scheduled"); // SettingsUpdateEnumStatus | Filter the Settings Updates by status. Can be `scheduled`, `in-progress`, `successful`, or `failed`.
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListSettingsUpdateResponse result = apiInstance.listSettingsUpdate(sim, status, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SupersimV1SettingsUpdateApi#listSettingsUpdate");
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
| **sim** | **String**| Filter the Settings Updates by a Super SIM&#39;s SID or UniqueName. | [optional] |
| **status** | **SettingsUpdateEnumStatus**| Filter the Settings Updates by status. Can be &#x60;scheduled&#x60;, &#x60;in-progress&#x60;, &#x60;successful&#x60;, or &#x60;failed&#x60;. | [optional] [enum: scheduled, in-progress, successful, failed] |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListSettingsUpdateResponse**](ListSettingsUpdateResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

