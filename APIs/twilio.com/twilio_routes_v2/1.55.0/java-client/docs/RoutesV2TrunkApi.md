# RoutesV2TrunkApi

All URIs are relative to *https://routes.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**fetchTrunks**](RoutesV2TrunkApi.md#fetchTrunks) | **GET** /v2/Trunks/{SipTrunkDomain} |  |
| [**updateTrunks**](RoutesV2TrunkApi.md#updateTrunks) | **POST** /v2/Trunks/{SipTrunkDomain} |  |


<a id="fetchTrunks"></a>
# **fetchTrunks**
> RoutesV2Trunks fetchTrunks(sipTrunkDomain)



Fetch the Inbound Processing Region assigned to a SIP Trunk.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RoutesV2TrunkApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://routes.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    RoutesV2TrunkApi apiInstance = new RoutesV2TrunkApi(defaultClient);
    String sipTrunkDomain = "sipTrunkDomain_example"; // String | The absolute URL of the SIP Trunk
    try {
      RoutesV2Trunks result = apiInstance.fetchTrunks(sipTrunkDomain);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RoutesV2TrunkApi#fetchTrunks");
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
| **sipTrunkDomain** | **String**| The absolute URL of the SIP Trunk | |

### Return type

[**RoutesV2Trunks**](RoutesV2Trunks.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updateTrunks"></a>
# **updateTrunks**
> RoutesV2Trunks updateTrunks(sipTrunkDomain, friendlyName, voiceRegion)



Assign an Inbound Processing Region to a SIP Trunk

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RoutesV2TrunkApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://routes.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    RoutesV2TrunkApi apiInstance = new RoutesV2TrunkApi(defaultClient);
    String sipTrunkDomain = "sipTrunkDomain_example"; // String | The absolute URL of the SIP Trunk
    String friendlyName = "friendlyName_example"; // String | A human readable description of this resource, up to 64 characters.
    String voiceRegion = "voiceRegion_example"; // String | The Inbound Processing Region used for this SIP Trunk for voice
    try {
      RoutesV2Trunks result = apiInstance.updateTrunks(sipTrunkDomain, friendlyName, voiceRegion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RoutesV2TrunkApi#updateTrunks");
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
| **sipTrunkDomain** | **String**| The absolute URL of the SIP Trunk | |
| **friendlyName** | **String**| A human readable description of this resource, up to 64 characters. | [optional] |
| **voiceRegion** | **String**| The Inbound Processing Region used for this SIP Trunk for voice | [optional] |

### Return type

[**RoutesV2Trunks**](RoutesV2Trunks.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

