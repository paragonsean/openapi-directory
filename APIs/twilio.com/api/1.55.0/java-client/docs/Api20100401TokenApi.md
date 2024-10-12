# Api20100401TokenApi

All URIs are relative to *https://api.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createToken**](Api20100401TokenApi.md#createToken) | **POST** /2010-04-01/Accounts/{AccountSid}/Tokens.json |  |


<a id="createToken"></a>
# **createToken**
> ApiV2010AccountToken createToken(accountSid, ttl)



Create a new token for ICE servers

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Api20100401TokenApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    Api20100401TokenApi apiInstance = new Api20100401TokenApi(defaultClient);
    String accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that will create the resource.
    Integer ttl = 56; // Integer | The duration in seconds for which the generated credentials are valid. The default value is 86400 (24 hours).
    try {
      ApiV2010AccountToken result = apiInstance.createToken(accountSid, ttl);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Api20100401TokenApi#createToken");
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
| **accountSid** | **String**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that will create the resource. | |
| **ttl** | **Integer**| The duration in seconds for which the generated credentials are valid. The default value is 86400 (24 hours). | [optional] |

### Return type

[**ApiV2010AccountToken**](ApiV2010AccountToken.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

