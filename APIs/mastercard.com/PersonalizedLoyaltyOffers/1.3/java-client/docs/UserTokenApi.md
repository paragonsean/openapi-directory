# UserTokenApi

All URIs are relative to *https://api.mastercard.com/plo/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**usertokenGet**](UserTokenApi.md#usertokenGet) | **GET** /usertoken | Returns User Session Token |


<a id="usertokenGet"></a>
# **usertokenGet**
> UserTokenResponse usertokenGet(fid, authInfo)

Returns User Session Token

This resource creates the user session. It must be called prior to any other API calls for the specified user. The Token value does not expire. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserTokenApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.mastercard.com/plo/v1");

    UserTokenApi apiInstance = new UserTokenApi(defaultClient);
    String fid = "999999"; // String | Financial Institution Identifier. Code that specifies the platform and configuration instance, provided by Mastercard during implementation.
    String authInfo = "authInfo_example"; // String | Authorization Information. AES 128-bit encrypted concatenation of \"User ID as specified in enrollment:FI ID as provided by Mastercard:current Unix time\". Key exchange and establishment of maintenance procedures occur during implementation.
    try {
      UserTokenResponse result = apiInstance.usertokenGet(fid, authInfo);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserTokenApi#usertokenGet");
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
| **fid** | **String**| Financial Institution Identifier. Code that specifies the platform and configuration instance, provided by Mastercard during implementation. | |
| **authInfo** | **String**| Authorization Information. AES 128-bit encrypted concatenation of \&quot;User ID as specified in enrollment:FI ID as provided by Mastercard:current Unix time\&quot;. Key exchange and establishment of maintenance procedures occur during implementation. | |

### Return type

[**UserTokenResponse**](UserTokenResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | This resource returns the user session token (UserToken), which is a required input to all other API resources. |  -  |
| **0** | Unexpected error |  -  |

