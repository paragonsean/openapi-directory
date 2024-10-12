# RoutesV2SipDomainApi

All URIs are relative to *https://routes.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**fetchSipDomain**](RoutesV2SipDomainApi.md#fetchSipDomain) | **GET** /v2/SipDomains/{SipDomain} |  |
| [**updateSipDomain**](RoutesV2SipDomainApi.md#updateSipDomain) | **POST** /v2/SipDomains/{SipDomain} |  |


<a id="fetchSipDomain"></a>
# **fetchSipDomain**
> RoutesV2SipDomain fetchSipDomain(sipDomain)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RoutesV2SipDomainApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://routes.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    RoutesV2SipDomainApi apiInstance = new RoutesV2SipDomainApi(defaultClient);
    String sipDomain = "sipDomain_example"; // String | 
    try {
      RoutesV2SipDomain result = apiInstance.fetchSipDomain(sipDomain);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RoutesV2SipDomainApi#fetchSipDomain");
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
| **sipDomain** | **String**|  | |

### Return type

[**RoutesV2SipDomain**](RoutesV2SipDomain.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updateSipDomain"></a>
# **updateSipDomain**
> RoutesV2SipDomain updateSipDomain(sipDomain, friendlyName, voiceRegion)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RoutesV2SipDomainApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://routes.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    RoutesV2SipDomainApi apiInstance = new RoutesV2SipDomainApi(defaultClient);
    String sipDomain = "sipDomain_example"; // String | 
    String friendlyName = "friendlyName_example"; // String | 
    String voiceRegion = "voiceRegion_example"; // String | 
    try {
      RoutesV2SipDomain result = apiInstance.updateSipDomain(sipDomain, friendlyName, voiceRegion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RoutesV2SipDomainApi#updateSipDomain");
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
| **sipDomain** | **String**|  | |
| **friendlyName** | **String**|  | [optional] |
| **voiceRegion** | **String**|  | [optional] |

### Return type

[**RoutesV2SipDomain**](RoutesV2SipDomain.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

