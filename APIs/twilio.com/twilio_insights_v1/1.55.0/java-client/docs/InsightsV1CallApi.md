# InsightsV1CallApi

All URIs are relative to *https://insights.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**fetchCall**](InsightsV1CallApi.md#fetchCall) | **GET** /v1/Voice/{Sid} |  |


<a id="fetchCall"></a>
# **fetchCall**
> InsightsV1Call fetchCall(sid)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InsightsV1CallApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://insights.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    InsightsV1CallApi apiInstance = new InsightsV1CallApi(defaultClient);
    String sid = "sid_example"; // String | 
    try {
      InsightsV1Call result = apiInstance.fetchCall(sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InsightsV1CallApi#fetchCall");
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
| **sid** | **String**|  | |

### Return type

[**InsightsV1Call**](InsightsV1Call.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

