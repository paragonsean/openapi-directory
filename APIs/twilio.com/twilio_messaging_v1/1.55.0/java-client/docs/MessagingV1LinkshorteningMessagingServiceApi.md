# MessagingV1LinkshorteningMessagingServiceApi

All URIs are relative to *https://messaging.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createLinkshorteningMessagingService**](MessagingV1LinkshorteningMessagingServiceApi.md#createLinkshorteningMessagingService) | **POST** /v1/LinkShortening/Domains/{DomainSid}/MessagingServices/{MessagingServiceSid} |  |
| [**deleteLinkshorteningMessagingService**](MessagingV1LinkshorteningMessagingServiceApi.md#deleteLinkshorteningMessagingService) | **DELETE** /v1/LinkShortening/Domains/{DomainSid}/MessagingServices/{MessagingServiceSid} |  |


<a id="createLinkshorteningMessagingService"></a>
# **createLinkshorteningMessagingService**
> MessagingV1LinkshorteningMessagingService createLinkshorteningMessagingService(domainSid, messagingServiceSid)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MessagingV1LinkshorteningMessagingServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://messaging.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    MessagingV1LinkshorteningMessagingServiceApi apiInstance = new MessagingV1LinkshorteningMessagingServiceApi(defaultClient);
    String domainSid = "domainSid_example"; // String | The domain SID to associate with a messaging service. With URL shortening enabled, links in messages sent with the associated messaging service will be shortened to the provided domain
    String messagingServiceSid = "messagingServiceSid_example"; // String | A messaging service SID to associate with a domain. With URL shortening enabled, links in messages sent with the provided messaging service will be shortened to the associated domain
    try {
      MessagingV1LinkshorteningMessagingService result = apiInstance.createLinkshorteningMessagingService(domainSid, messagingServiceSid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MessagingV1LinkshorteningMessagingServiceApi#createLinkshorteningMessagingService");
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
| **domainSid** | **String**| The domain SID to associate with a messaging service. With URL shortening enabled, links in messages sent with the associated messaging service will be shortened to the provided domain | |
| **messagingServiceSid** | **String**| A messaging service SID to associate with a domain. With URL shortening enabled, links in messages sent with the provided messaging service will be shortened to the associated domain | |

### Return type

[**MessagingV1LinkshorteningMessagingService**](MessagingV1LinkshorteningMessagingService.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |

<a id="deleteLinkshorteningMessagingService"></a>
# **deleteLinkshorteningMessagingService**
> deleteLinkshorteningMessagingService(domainSid, messagingServiceSid)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MessagingV1LinkshorteningMessagingServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://messaging.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    MessagingV1LinkshorteningMessagingServiceApi apiInstance = new MessagingV1LinkshorteningMessagingServiceApi(defaultClient);
    String domainSid = "domainSid_example"; // String | The domain SID to dissociate from a messaging service. With URL shortening enabled, links in messages sent with the associated messaging service will be shortened to the provided domain
    String messagingServiceSid = "messagingServiceSid_example"; // String | A messaging service SID to dissociate from a domain. With URL shortening enabled, links in messages sent with the provided messaging service will be shortened to the associated domain
    try {
      apiInstance.deleteLinkshorteningMessagingService(domainSid, messagingServiceSid);
    } catch (ApiException e) {
      System.err.println("Exception when calling MessagingV1LinkshorteningMessagingServiceApi#deleteLinkshorteningMessagingService");
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
| **domainSid** | **String**| The domain SID to dissociate from a messaging service. With URL shortening enabled, links in messages sent with the associated messaging service will be shortened to the provided domain | |
| **messagingServiceSid** | **String**| A messaging service SID to dissociate from a domain. With URL shortening enabled, links in messages sent with the provided messaging service will be shortened to the associated domain | |

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

