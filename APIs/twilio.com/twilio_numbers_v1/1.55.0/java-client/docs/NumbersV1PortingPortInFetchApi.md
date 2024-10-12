# NumbersV1PortingPortInFetchApi

All URIs are relative to *https://numbers.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**fetchPortingPortInFetch**](NumbersV1PortingPortInFetchApi.md#fetchPortingPortInFetch) | **GET** /v1/Porting/PortIn/{PortInRequestSid} |  |


<a id="fetchPortingPortInFetch"></a>
# **fetchPortingPortInFetch**
> NumbersV1PortingPortInFetch fetchPortingPortInFetch(portInRequestSid)



Fetch a port in request by SID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NumbersV1PortingPortInFetchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://numbers.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    NumbersV1PortingPortInFetchApi apiInstance = new NumbersV1PortingPortInFetchApi(defaultClient);
    String portInRequestSid = "portInRequestSid_example"; // String | The SID of the Port In request. This is a unique identifier of the port in request.
    try {
      NumbersV1PortingPortInFetch result = apiInstance.fetchPortingPortInFetch(portInRequestSid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NumbersV1PortingPortInFetchApi#fetchPortingPortInFetch");
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
| **portInRequestSid** | **String**| The SID of the Port In request. This is a unique identifier of the port in request. | |

### Return type

[**NumbersV1PortingPortInFetch**](NumbersV1PortingPortInFetch.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

