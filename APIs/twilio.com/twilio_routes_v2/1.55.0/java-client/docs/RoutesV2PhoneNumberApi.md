# RoutesV2PhoneNumberApi

All URIs are relative to *https://routes.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**fetchPhoneNumber**](RoutesV2PhoneNumberApi.md#fetchPhoneNumber) | **GET** /v2/PhoneNumbers/{PhoneNumber} |  |
| [**updatePhoneNumber**](RoutesV2PhoneNumberApi.md#updatePhoneNumber) | **POST** /v2/PhoneNumbers/{PhoneNumber} |  |


<a id="fetchPhoneNumber"></a>
# **fetchPhoneNumber**
> RoutesV2PhoneNumber fetchPhoneNumber(phoneNumber)



Fetch the Inbound Processing Region assigned to a phone number.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RoutesV2PhoneNumberApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://routes.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    RoutesV2PhoneNumberApi apiInstance = new RoutesV2PhoneNumberApi(defaultClient);
    String phoneNumber = "phoneNumber_example"; // String | The phone number in E.164 format
    try {
      RoutesV2PhoneNumber result = apiInstance.fetchPhoneNumber(phoneNumber);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RoutesV2PhoneNumberApi#fetchPhoneNumber");
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
| **phoneNumber** | **String**| The phone number in E.164 format | |

### Return type

[**RoutesV2PhoneNumber**](RoutesV2PhoneNumber.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updatePhoneNumber"></a>
# **updatePhoneNumber**
> RoutesV2PhoneNumber updatePhoneNumber(phoneNumber, friendlyName, voiceRegion)



Assign an Inbound Processing Region to a phone number.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RoutesV2PhoneNumberApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://routes.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    RoutesV2PhoneNumberApi apiInstance = new RoutesV2PhoneNumberApi(defaultClient);
    String phoneNumber = "phoneNumber_example"; // String | The phone number in E.164 format
    String friendlyName = "friendlyName_example"; // String | A human readable description of this resource, up to 64 characters.
    String voiceRegion = "voiceRegion_example"; // String | The Inbound Processing Region used for this phone number for voice
    try {
      RoutesV2PhoneNumber result = apiInstance.updatePhoneNumber(phoneNumber, friendlyName, voiceRegion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RoutesV2PhoneNumberApi#updatePhoneNumber");
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
| **phoneNumber** | **String**| The phone number in E.164 format | |
| **friendlyName** | **String**| A human readable description of this resource, up to 64 characters. | [optional] |
| **voiceRegion** | **String**| The Inbound Processing Region used for this phone number for voice | [optional] |

### Return type

[**RoutesV2PhoneNumber**](RoutesV2PhoneNumber.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

