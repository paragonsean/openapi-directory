# ProxyV1PhoneNumberApi

All URIs are relative to *https://proxy.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createPhoneNumber**](ProxyV1PhoneNumberApi.md#createPhoneNumber) | **POST** /v1/Services/{ServiceSid}/PhoneNumbers |  |
| [**deletePhoneNumber**](ProxyV1PhoneNumberApi.md#deletePhoneNumber) | **DELETE** /v1/Services/{ServiceSid}/PhoneNumbers/{Sid} |  |
| [**fetchPhoneNumber**](ProxyV1PhoneNumberApi.md#fetchPhoneNumber) | **GET** /v1/Services/{ServiceSid}/PhoneNumbers/{Sid} |  |
| [**listPhoneNumber**](ProxyV1PhoneNumberApi.md#listPhoneNumber) | **GET** /v1/Services/{ServiceSid}/PhoneNumbers |  |
| [**updatePhoneNumber**](ProxyV1PhoneNumberApi.md#updatePhoneNumber) | **POST** /v1/Services/{ServiceSid}/PhoneNumbers/{Sid} |  |


<a id="createPhoneNumber"></a>
# **createPhoneNumber**
> ProxyV1ServicePhoneNumber createPhoneNumber(serviceSid, isReserved, phoneNumber, sid)



Add a Phone Number to a Service&#39;s Proxy Number Pool.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProxyV1PhoneNumberApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://proxy.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ProxyV1PhoneNumberApi apiInstance = new ProxyV1PhoneNumberApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | The SID parent [Service](https://www.twilio.com/docs/proxy/api/service) resource of the new PhoneNumber resource.
    Boolean isReserved = true; // Boolean | Whether the new phone number should be reserved and not be assigned to a participant using proxy pool logic. See [Reserved Phone Numbers](https://www.twilio.com/docs/proxy/reserved-phone-numbers) for more information.
    String phoneNumber = "phoneNumber_example"; // String | The phone number in [E.164](https://www.twilio.com/docs/glossary/what-e164) format.  E.164 phone numbers consist of a + followed by the country code and subscriber number without punctuation characters. For example, +14155551234.
    String sid = "sid_example"; // String | The SID of a Twilio [IncomingPhoneNumber](https://www.twilio.com/docs/phone-numbers/api/incomingphonenumber-resource) resource that represents the Twilio Number you would like to assign to your Proxy Service.
    try {
      ProxyV1ServicePhoneNumber result = apiInstance.createPhoneNumber(serviceSid, isReserved, phoneNumber, sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProxyV1PhoneNumberApi#createPhoneNumber");
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
| **serviceSid** | **String**| The SID parent [Service](https://www.twilio.com/docs/proxy/api/service) resource of the new PhoneNumber resource. | |
| **isReserved** | **Boolean**| Whether the new phone number should be reserved and not be assigned to a participant using proxy pool logic. See [Reserved Phone Numbers](https://www.twilio.com/docs/proxy/reserved-phone-numbers) for more information. | [optional] |
| **phoneNumber** | **String**| The phone number in [E.164](https://www.twilio.com/docs/glossary/what-e164) format.  E.164 phone numbers consist of a + followed by the country code and subscriber number without punctuation characters. For example, +14155551234. | [optional] |
| **sid** | **String**| The SID of a Twilio [IncomingPhoneNumber](https://www.twilio.com/docs/phone-numbers/api/incomingphonenumber-resource) resource that represents the Twilio Number you would like to assign to your Proxy Service. | [optional] |

### Return type

[**ProxyV1ServicePhoneNumber**](ProxyV1ServicePhoneNumber.md)

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
> deletePhoneNumber(serviceSid, sid)



Delete a specific Phone Number from a Service.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProxyV1PhoneNumberApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://proxy.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ProxyV1PhoneNumberApi apiInstance = new ProxyV1PhoneNumberApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | The SID of the parent [Service](https://www.twilio.com/docs/proxy/api/service) of the PhoneNumber resource to delete.
    String sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the PhoneNumber resource to delete.
    try {
      apiInstance.deletePhoneNumber(serviceSid, sid);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProxyV1PhoneNumberApi#deletePhoneNumber");
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
| **serviceSid** | **String**| The SID of the parent [Service](https://www.twilio.com/docs/proxy/api/service) of the PhoneNumber resource to delete. | |
| **sid** | **String**| The Twilio-provided string that uniquely identifies the PhoneNumber resource to delete. | |

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
> ProxyV1ServicePhoneNumber fetchPhoneNumber(serviceSid, sid)



Fetch a specific Phone Number.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProxyV1PhoneNumberApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://proxy.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ProxyV1PhoneNumberApi apiInstance = new ProxyV1PhoneNumberApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | The SID of the parent [Service](https://www.twilio.com/docs/proxy/api/service) of the PhoneNumber resource to fetch.
    String sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the PhoneNumber resource to fetch.
    try {
      ProxyV1ServicePhoneNumber result = apiInstance.fetchPhoneNumber(serviceSid, sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProxyV1PhoneNumberApi#fetchPhoneNumber");
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
| **serviceSid** | **String**| The SID of the parent [Service](https://www.twilio.com/docs/proxy/api/service) of the PhoneNumber resource to fetch. | |
| **sid** | **String**| The Twilio-provided string that uniquely identifies the PhoneNumber resource to fetch. | |

### Return type

[**ProxyV1ServicePhoneNumber**](ProxyV1ServicePhoneNumber.md)

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
> ListPhoneNumberResponse listPhoneNumber(serviceSid, pageSize, page, pageToken)



Retrieve a list of all Phone Numbers in the Proxy Number Pool for a Service. A maximum of 100 records will be returned per page.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProxyV1PhoneNumberApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://proxy.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ProxyV1PhoneNumberApi apiInstance = new ProxyV1PhoneNumberApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | The SID of the parent [Service](https://www.twilio.com/docs/proxy/api/service) of the PhoneNumber resources to read.
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListPhoneNumberResponse result = apiInstance.listPhoneNumber(serviceSid, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProxyV1PhoneNumberApi#listPhoneNumber");
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
| **serviceSid** | **String**| The SID of the parent [Service](https://www.twilio.com/docs/proxy/api/service) of the PhoneNumber resources to read. | |
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

<a id="updatePhoneNumber"></a>
# **updatePhoneNumber**
> ProxyV1ServicePhoneNumber updatePhoneNumber(serviceSid, sid, isReserved)



Update a specific Proxy Number.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProxyV1PhoneNumberApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://proxy.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    ProxyV1PhoneNumberApi apiInstance = new ProxyV1PhoneNumberApi(defaultClient);
    String serviceSid = "serviceSid_example"; // String | The SID of the parent [Service](https://www.twilio.com/docs/proxy/api/service) of the PhoneNumber resource to update.
    String sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the PhoneNumber resource to update.
    Boolean isReserved = true; // Boolean | Whether the phone number should be reserved and not be assigned to a participant using proxy pool logic. See [Reserved Phone Numbers](https://www.twilio.com/docs/proxy/reserved-phone-numbers) for more information.
    try {
      ProxyV1ServicePhoneNumber result = apiInstance.updatePhoneNumber(serviceSid, sid, isReserved);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProxyV1PhoneNumberApi#updatePhoneNumber");
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
| **serviceSid** | **String**| The SID of the parent [Service](https://www.twilio.com/docs/proxy/api/service) of the PhoneNumber resource to update. | |
| **sid** | **String**| The Twilio-provided string that uniquely identifies the PhoneNumber resource to update. | |
| **isReserved** | **Boolean**| Whether the phone number should be reserved and not be assigned to a participant using proxy pool logic. See [Reserved Phone Numbers](https://www.twilio.com/docs/proxy/reserved-phone-numbers) for more information. | [optional] |

### Return type

[**ProxyV1ServicePhoneNumber**](ProxyV1ServicePhoneNumber.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

