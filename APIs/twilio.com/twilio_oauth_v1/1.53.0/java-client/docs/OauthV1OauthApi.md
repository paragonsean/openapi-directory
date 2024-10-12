# OauthV1OauthApi

All URIs are relative to *https://oauth.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**fetchCerts**](OauthV1OauthApi.md#fetchCerts) | **GET** /v1/certs |  |


<a id="fetchCerts"></a>
# **fetchCerts**
> OauthV1Certs fetchCerts()



Fetches public JWKs

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OauthV1OauthApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://oauth.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    OauthV1OauthApi apiInstance = new OauthV1OauthApi(defaultClient);
    try {
      OauthV1Certs result = apiInstance.fetchCerts();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OauthV1OauthApi#fetchCerts");
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

[**OauthV1Certs**](OauthV1Certs.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

