# WirelessV1DataSessionApi

All URIs are relative to *https://wireless.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**listDataSession**](WirelessV1DataSessionApi.md#listDataSession) | **GET** /v1/Sims/{SimSid}/DataSessions |  |


<a id="listDataSession"></a>
# **listDataSession**
> ListDataSessionResponse listDataSession(simSid, pageSize, page, pageToken)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WirelessV1DataSessionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://wireless.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    WirelessV1DataSessionApi apiInstance = new WirelessV1DataSessionApi(defaultClient);
    String simSid = "simSid_example"; // String | The SID of the [Sim resource](https://www.twilio.com/docs/iot/wireless/api/sim-resource) with the Data Sessions to read.
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListDataSessionResponse result = apiInstance.listDataSession(simSid, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WirelessV1DataSessionApi#listDataSession");
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
| **simSid** | **String**| The SID of the [Sim resource](https://www.twilio.com/docs/iot/wireless/api/sim-resource) with the Data Sessions to read. | |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListDataSessionResponse**](ListDataSessionResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

