# TrunkingV1PhoneNumberApi

All URIs are relative to *https://trunking.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createPhoneNumber**](TrunkingV1PhoneNumberApi.md#createPhoneNumber) | **POST** /v1/Trunks/{TrunkSid}/PhoneNumbers |  |
| [**deletePhoneNumber**](TrunkingV1PhoneNumberApi.md#deletePhoneNumber) | **DELETE** /v1/Trunks/{TrunkSid}/PhoneNumbers/{Sid} |  |
| [**fetchPhoneNumber**](TrunkingV1PhoneNumberApi.md#fetchPhoneNumber) | **GET** /v1/Trunks/{TrunkSid}/PhoneNumbers/{Sid} |  |
| [**listPhoneNumber**](TrunkingV1PhoneNumberApi.md#listPhoneNumber) | **GET** /v1/Trunks/{TrunkSid}/PhoneNumbers |  |


<a id="createPhoneNumber"></a>
# **createPhoneNumber**
> TrunkingV1TrunkPhoneNumber createPhoneNumber(trunkSid, phoneNumberSid)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TrunkingV1PhoneNumberApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://trunking.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    TrunkingV1PhoneNumberApi apiInstance = new TrunkingV1PhoneNumberApi(defaultClient);
    String trunkSid = "trunkSid_example"; // String | The SID of the Trunk to associate the phone number with.
    String phoneNumberSid = "phoneNumberSid_example"; // String | The SID of the [Incoming Phone Number](https://www.twilio.com/docs/phone-numbers/api/incomingphonenumber-resource) that you want to associate with the trunk.
    try {
      TrunkingV1TrunkPhoneNumber result = apiInstance.createPhoneNumber(trunkSid, phoneNumberSid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TrunkingV1PhoneNumberApi#createPhoneNumber");
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
| **trunkSid** | **String**| The SID of the Trunk to associate the phone number with. | |
| **phoneNumberSid** | **String**| The SID of the [Incoming Phone Number](https://www.twilio.com/docs/phone-numbers/api/incomingphonenumber-resource) that you want to associate with the trunk. | |

### Return type

[**TrunkingV1TrunkPhoneNumber**](TrunkingV1TrunkPhoneNumber.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="deletePhoneNumber"></a>
# **deletePhoneNumber**
> deletePhoneNumber(trunkSid, sid)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TrunkingV1PhoneNumberApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://trunking.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    TrunkingV1PhoneNumberApi apiInstance = new TrunkingV1PhoneNumberApi(defaultClient);
    String trunkSid = "trunkSid_example"; // String | The SID of the Trunk from which to delete the PhoneNumber resource.
    String sid = "sid_example"; // String | The unique string that we created to identify the PhoneNumber resource to delete.
    try {
      apiInstance.deletePhoneNumber(trunkSid, sid);
    } catch (ApiException e) {
      System.err.println("Exception when calling TrunkingV1PhoneNumberApi#deletePhoneNumber");
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
| **trunkSid** | **String**| The SID of the Trunk from which to delete the PhoneNumber resource. | |
| **sid** | **String**| The unique string that we created to identify the PhoneNumber resource to delete. | |

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

<a id="fetchPhoneNumber"></a>
# **fetchPhoneNumber**
> TrunkingV1TrunkPhoneNumber fetchPhoneNumber(trunkSid, sid)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TrunkingV1PhoneNumberApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://trunking.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    TrunkingV1PhoneNumberApi apiInstance = new TrunkingV1PhoneNumberApi(defaultClient);
    String trunkSid = "trunkSid_example"; // String | The SID of the Trunk from which to fetch the PhoneNumber resource.
    String sid = "sid_example"; // String | The unique string that we created to identify the PhoneNumber resource to fetch.
    try {
      TrunkingV1TrunkPhoneNumber result = apiInstance.fetchPhoneNumber(trunkSid, sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TrunkingV1PhoneNumberApi#fetchPhoneNumber");
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
| **trunkSid** | **String**| The SID of the Trunk from which to fetch the PhoneNumber resource. | |
| **sid** | **String**| The unique string that we created to identify the PhoneNumber resource to fetch. | |

### Return type

[**TrunkingV1TrunkPhoneNumber**](TrunkingV1TrunkPhoneNumber.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listPhoneNumber"></a>
# **listPhoneNumber**
> ListPhoneNumberResponse listPhoneNumber(trunkSid, pageSize, page, pageToken)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TrunkingV1PhoneNumberApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://trunking.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    TrunkingV1PhoneNumberApi apiInstance = new TrunkingV1PhoneNumberApi(defaultClient);
    String trunkSid = "trunkSid_example"; // String | The SID of the Trunk from which to read the PhoneNumber resources.
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListPhoneNumberResponse result = apiInstance.listPhoneNumber(trunkSid, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TrunkingV1PhoneNumberApi#listPhoneNumber");
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
| **trunkSid** | **String**| The SID of the Trunk from which to read the PhoneNumber resources. | |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListPhoneNumberResponse**](ListPhoneNumberResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

