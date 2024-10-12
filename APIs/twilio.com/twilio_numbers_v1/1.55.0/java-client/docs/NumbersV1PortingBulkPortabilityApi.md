# NumbersV1PortingBulkPortabilityApi

All URIs are relative to *https://numbers.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createPortingBulkPortability**](NumbersV1PortingBulkPortabilityApi.md#createPortingBulkPortability) | **POST** /v1/Porting/Portability |  |
| [**fetchPortingBulkPortability**](NumbersV1PortingBulkPortabilityApi.md#fetchPortingBulkPortability) | **GET** /v1/Porting/Portability/{Sid} |  |


<a id="createPortingBulkPortability"></a>
# **createPortingBulkPortability**
> NumbersV1PortingBulkPortability createPortingBulkPortability(phoneNumbers)



Allows to check if a list of phone numbers can be ported to Twilio or not. This is done asynchronous for each phone number.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NumbersV1PortingBulkPortabilityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://numbers.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    NumbersV1PortingBulkPortabilityApi apiInstance = new NumbersV1PortingBulkPortabilityApi(defaultClient);
    List<String> phoneNumbers = Arrays.asList(); // List<String> | The phone numbers which portability is to be checked. This should be a list of strings. Phone numbers are in E.164 format (e.g. +16175551212). .
    try {
      NumbersV1PortingBulkPortability result = apiInstance.createPortingBulkPortability(phoneNumbers);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NumbersV1PortingBulkPortabilityApi#createPortingBulkPortability");
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
| **phoneNumbers** | [**List&lt;String&gt;**](String.md)| The phone numbers which portability is to be checked. This should be a list of strings. Phone numbers are in E.164 format (e.g. +16175551212). . | |

### Return type

[**NumbersV1PortingBulkPortability**](NumbersV1PortingBulkPortability.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Accepted |  -  |

<a id="fetchPortingBulkPortability"></a>
# **fetchPortingBulkPortability**
> NumbersV1PortingBulkPortability fetchPortingBulkPortability(sid)



Fetch a previous portability check. This should return the current status of the validation and the result for all the numbers provided, given that they have been validated (as this process is performed asynchronously).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NumbersV1PortingBulkPortabilityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://numbers.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    NumbersV1PortingBulkPortabilityApi apiInstance = new NumbersV1PortingBulkPortabilityApi(defaultClient);
    String sid = "sid_example"; // String | A 34 character string that uniquely identifies the Portability check.
    try {
      NumbersV1PortingBulkPortability result = apiInstance.fetchPortingBulkPortability(sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NumbersV1PortingBulkPortabilityApi#fetchPortingBulkPortability");
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
| **sid** | **String**| A 34 character string that uniquely identifies the Portability check. | |

### Return type

[**NumbersV1PortingBulkPortability**](NumbersV1PortingBulkPortability.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

