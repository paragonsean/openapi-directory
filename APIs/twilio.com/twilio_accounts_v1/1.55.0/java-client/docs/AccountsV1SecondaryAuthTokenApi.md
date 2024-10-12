# AccountsV1SecondaryAuthTokenApi

All URIs are relative to *https://accounts.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createSecondaryAuthToken**](AccountsV1SecondaryAuthTokenApi.md#createSecondaryAuthToken) | **POST** /v1/AuthTokens/Secondary |  |
| [**deleteSecondaryAuthToken**](AccountsV1SecondaryAuthTokenApi.md#deleteSecondaryAuthToken) | **DELETE** /v1/AuthTokens/Secondary |  |


<a id="createSecondaryAuthToken"></a>
# **createSecondaryAuthToken**
> AccountsV1SecondaryAuthToken createSecondaryAuthToken()



Create a new secondary Auth Token

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountsV1SecondaryAuthTokenApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://accounts.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    AccountsV1SecondaryAuthTokenApi apiInstance = new AccountsV1SecondaryAuthTokenApi(defaultClient);
    try {
      AccountsV1SecondaryAuthToken result = apiInstance.createSecondaryAuthToken();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountsV1SecondaryAuthTokenApi#createSecondaryAuthToken");
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

[**AccountsV1SecondaryAuthToken**](AccountsV1SecondaryAuthToken.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="deleteSecondaryAuthToken"></a>
# **deleteSecondaryAuthToken**
> deleteSecondaryAuthToken()



Delete the secondary Auth Token from your account

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountsV1SecondaryAuthTokenApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://accounts.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    AccountsV1SecondaryAuthTokenApi apiInstance = new AccountsV1SecondaryAuthTokenApi(defaultClient);
    try {
      apiInstance.deleteSecondaryAuthToken();
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountsV1SecondaryAuthTokenApi#deleteSecondaryAuthToken");
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

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The resource was deleted successfully. |  -  |

