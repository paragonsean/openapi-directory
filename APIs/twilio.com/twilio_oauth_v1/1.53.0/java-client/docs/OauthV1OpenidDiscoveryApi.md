# OauthV1OpenidDiscoveryApi

All URIs are relative to *https://oauth.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**fetchOpenidDiscovery**](OauthV1OpenidDiscoveryApi.md#fetchOpenidDiscovery) | **GET** /v1/.well-known/openid-configuration |  |


<a id="fetchOpenidDiscovery"></a>
# **fetchOpenidDiscovery**
> OauthV1OpenidDiscovery fetchOpenidDiscovery()



Fetch configuration details about the OpenID Connect Authorization Server

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OauthV1OpenidDiscoveryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://oauth.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    OauthV1OpenidDiscoveryApi apiInstance = new OauthV1OpenidDiscoveryApi(defaultClient);
    try {
      OauthV1OpenidDiscovery result = apiInstance.fetchOpenidDiscovery();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OauthV1OpenidDiscoveryApi#fetchOpenidDiscovery");
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

[**OauthV1OpenidDiscovery**](OauthV1OpenidDiscovery.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

