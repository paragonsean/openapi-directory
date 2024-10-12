# OauthV1DeviceCodeApi

All URIs are relative to *https://oauth.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createDeviceCode**](OauthV1DeviceCodeApi.md#createDeviceCode) | **POST** /v1/device/code |  |


<a id="createDeviceCode"></a>
# **createDeviceCode**
> OauthV1DeviceCode createDeviceCode(clientSid, scopes, audiences)



Issues a new Access token (optionally identity_token &amp; refresh_token) in exchange of Oauth grant

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OauthV1DeviceCodeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://oauth.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    OauthV1DeviceCodeApi apiInstance = new OauthV1DeviceCodeApi(defaultClient);
    String clientSid = "clientSid_example"; // String | A 34 character string that uniquely identifies this OAuth App.
    List<String> scopes = Arrays.asList(); // List<String> | An Array of scopes for authorization request
    List<String> audiences = Arrays.asList(); // List<String> | An array of intended audiences for token requests
    try {
      OauthV1DeviceCode result = apiInstance.createDeviceCode(clientSid, scopes, audiences);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OauthV1DeviceCodeApi#createDeviceCode");
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
| **clientSid** | **String**| A 34 character string that uniquely identifies this OAuth App. | |
| **scopes** | [**List&lt;String&gt;**](String.md)| An Array of scopes for authorization request | |
| **audiences** | [**List&lt;String&gt;**](String.md)| An array of intended audiences for token requests | [optional] |

### Return type

[**OauthV1DeviceCode**](OauthV1DeviceCode.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

