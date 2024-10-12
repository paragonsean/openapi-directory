# PreflightApi

All URIs are relative to *https://api.lufthansa.com/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**autoCheckIn**](PreflightApi.md#autoCheckIn) | **PUT** /preflight/autocheckin/{ticketnumber} | Auto Check-In |


<a id="autoCheckIn"></a>
# **autoCheckIn**
> String autoCheckIn(ticketnumber, emailAddress, accept)

Auto Check-In

Trigger an automatic check-in given a ticket number. This service is only accessible for LH privileged partners

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PreflightApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.lufthansa.com/v1");
    
    // Configure OAuth2 access token for authorization: auth
    OAuth auth = (OAuth) defaultClient.getAuthentication("auth");
    auth.setAccessToken("YOUR ACCESS TOKEN");

    PreflightApi apiInstance = new PreflightApi(defaultClient);
    String ticketnumber = "ticketnumber_example"; // String | Ticket number
    String emailAddress = "emailAddress_example"; // String | Email address
    String accept = "accept_example"; // String | http header: application/json or application/xml (Acceptable values are: \"application/json\", \"application/xml\")
    try {
      String result = apiInstance.autoCheckIn(ticketnumber, emailAddress, accept);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PreflightApi#autoCheckIn");
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
| **ticketnumber** | **String**| Ticket number | |
| **emailAddress** | **String**| Email address | |
| **accept** | **String**| http header: application/json or application/xml (Acceptable values are: \&quot;application/json\&quot;, \&quot;application/xml\&quot;) | |

### Return type

**String**

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

