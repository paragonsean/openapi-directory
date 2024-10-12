# NumbersV1BulkEligibilityApi

All URIs are relative to *https://numbers.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**fetchBulkEligibility**](NumbersV1BulkEligibilityApi.md#fetchBulkEligibility) | **GET** /v1/HostedNumber/Eligibility/Bulk/{RequestId} |  |


<a id="fetchBulkEligibility"></a>
# **fetchBulkEligibility**
> NumbersV1BulkEligibility fetchBulkEligibility(requestId)



Fetch an eligibility bulk check that you requested to host in Twilio.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NumbersV1BulkEligibilityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://numbers.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    NumbersV1BulkEligibilityApi apiInstance = new NumbersV1BulkEligibilityApi(defaultClient);
    String requestId = "requestId_example"; // String | The SID of the bulk eligibility check that you want to know about.
    try {
      NumbersV1BulkEligibility result = apiInstance.fetchBulkEligibility(requestId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NumbersV1BulkEligibilityApi#fetchBulkEligibility");
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
| **requestId** | **String**| The SID of the bulk eligibility check that you want to know about. | |

### Return type

[**NumbersV1BulkEligibility**](NumbersV1BulkEligibility.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

