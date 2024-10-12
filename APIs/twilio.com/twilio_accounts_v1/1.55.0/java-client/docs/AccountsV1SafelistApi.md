# AccountsV1SafelistApi

All URIs are relative to *https://accounts.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createSafelist**](AccountsV1SafelistApi.md#createSafelist) | **POST** /v1/SafeList/Numbers |  |
| [**deleteSafelist**](AccountsV1SafelistApi.md#deleteSafelist) | **DELETE** /v1/SafeList/Numbers |  |
| [**fetchSafelist**](AccountsV1SafelistApi.md#fetchSafelist) | **GET** /v1/SafeList/Numbers |  |


<a id="createSafelist"></a>
# **createSafelist**
> AccountsV1Safelist createSafelist(phoneNumber)



Add a new phone number to SafeList.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountsV1SafelistApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://accounts.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    AccountsV1SafelistApi apiInstance = new AccountsV1SafelistApi(defaultClient);
    String phoneNumber = "phoneNumber_example"; // String | The phone number to be added in SafeList. Phone numbers must be in [E.164 format](https://www.twilio.com/docs/glossary/what-e164).
    try {
      AccountsV1Safelist result = apiInstance.createSafelist(phoneNumber);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountsV1SafelistApi#createSafelist");
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
| **phoneNumber** | **String**| The phone number to be added in SafeList. Phone numbers must be in [E.164 format](https://www.twilio.com/docs/glossary/what-e164). | |

### Return type

[**AccountsV1Safelist**](AccountsV1Safelist.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="deleteSafelist"></a>
# **deleteSafelist**
> deleteSafelist(phoneNumber)



Remove a phone number from SafeList.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountsV1SafelistApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://accounts.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    AccountsV1SafelistApi apiInstance = new AccountsV1SafelistApi(defaultClient);
    String phoneNumber = "phoneNumber_example"; // String | The phone number to be removed from SafeList. Phone numbers must be in [E.164 format](https://www.twilio.com/docs/glossary/what-e164).
    try {
      apiInstance.deleteSafelist(phoneNumber);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountsV1SafelistApi#deleteSafelist");
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
| **phoneNumber** | **String**| The phone number to be removed from SafeList. Phone numbers must be in [E.164 format](https://www.twilio.com/docs/glossary/what-e164). | [optional] |

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

<a id="fetchSafelist"></a>
# **fetchSafelist**
> AccountsV1Safelist fetchSafelist(phoneNumber)



Check if a phone number exists in SafeList.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountsV1SafelistApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://accounts.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    AccountsV1SafelistApi apiInstance = new AccountsV1SafelistApi(defaultClient);
    String phoneNumber = "phoneNumber_example"; // String | The phone number to be fetched from SafeList. Phone numbers must be in [E.164 format](https://www.twilio.com/docs/glossary/what-e164).
    try {
      AccountsV1Safelist result = apiInstance.fetchSafelist(phoneNumber);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountsV1SafelistApi#fetchSafelist");
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
| **phoneNumber** | **String**| The phone number to be fetched from SafeList. Phone numbers must be in [E.164 format](https://www.twilio.com/docs/glossary/what-e164). | [optional] |

### Return type

[**AccountsV1Safelist**](AccountsV1Safelist.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

