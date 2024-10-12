# OauthV1UserInfoApi

All URIs are relative to *https://oauth.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**fetchUserInfo**](OauthV1UserInfoApi.md#fetchUserInfo) | **GET** /v1/userinfo |  |


<a id="fetchUserInfo"></a>
# **fetchUserInfo**
> OauthV1UserInfo fetchUserInfo()



Retrieves the consented UserInfo and other claims about the logged-in subject (end-user).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OauthV1UserInfoApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://oauth.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    OauthV1UserInfoApi apiInstance = new OauthV1UserInfoApi(defaultClient);
    try {
      OauthV1UserInfo result = apiInstance.fetchUserInfo();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OauthV1UserInfoApi#fetchUserInfo");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**OauthV1UserInfo**](OauthV1UserInfo.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

