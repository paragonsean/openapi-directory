# MessagingV1DomainCertsApi

All URIs are relative to *https://messaging.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deleteDomainCertV4**](MessagingV1DomainCertsApi.md#deleteDomainCertV4) | **DELETE** /v1/LinkShortening/Domains/{DomainSid}/Certificate |  |
| [**fetchDomainCertV4**](MessagingV1DomainCertsApi.md#fetchDomainCertV4) | **GET** /v1/LinkShortening/Domains/{DomainSid}/Certificate |  |
| [**updateDomainCertV4**](MessagingV1DomainCertsApi.md#updateDomainCertV4) | **POST** /v1/LinkShortening/Domains/{DomainSid}/Certificate |  |


<a id="deleteDomainCertV4"></a>
# **deleteDomainCertV4**
> deleteDomainCertV4(domainSid)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MessagingV1DomainCertsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://messaging.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    MessagingV1DomainCertsApi apiInstance = new MessagingV1DomainCertsApi(defaultClient);
    String domainSid = "domainSid_example"; // String | Unique string used to identify the domain that this certificate should be associated with.
    try {
      apiInstance.deleteDomainCertV4(domainSid);
    } catch (ApiException e) {
      System.err.println("Exception when calling MessagingV1DomainCertsApi#deleteDomainCertV4");
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
| **domainSid** | **String**| Unique string used to identify the domain that this certificate should be associated with. | |

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

<a id="fetchDomainCertV4"></a>
# **fetchDomainCertV4**
> MessagingV1DomainCertV4 fetchDomainCertV4(domainSid)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MessagingV1DomainCertsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://messaging.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    MessagingV1DomainCertsApi apiInstance = new MessagingV1DomainCertsApi(defaultClient);
    String domainSid = "domainSid_example"; // String | Unique string used to identify the domain that this certificate should be associated with.
    try {
      MessagingV1DomainCertV4 result = apiInstance.fetchDomainCertV4(domainSid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MessagingV1DomainCertsApi#fetchDomainCertV4");
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
| **domainSid** | **String**| Unique string used to identify the domain that this certificate should be associated with. | |

### Return type

[**MessagingV1DomainCertV4**](MessagingV1DomainCertV4.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updateDomainCertV4"></a>
# **updateDomainCertV4**
> MessagingV1DomainCertV4 updateDomainCertV4(domainSid, tlsCert)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MessagingV1DomainCertsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://messaging.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    MessagingV1DomainCertsApi apiInstance = new MessagingV1DomainCertsApi(defaultClient);
    String domainSid = "domainSid_example"; // String | Unique string used to identify the domain that this certificate should be associated with.
    String tlsCert = "tlsCert_example"; // String | Contains the full TLS certificate and private for this domain in PEM format: https://en.wikipedia.org/wiki/Privacy-Enhanced_Mail. Twilio uses this information to process HTTPS traffic sent to your domain.
    try {
      MessagingV1DomainCertV4 result = apiInstance.updateDomainCertV4(domainSid, tlsCert);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MessagingV1DomainCertsApi#updateDomainCertV4");
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
| **domainSid** | **String**| Unique string used to identify the domain that this certificate should be associated with. | |
| **tlsCert** | **String**| Contains the full TLS certificate and private for this domain in PEM format: https://en.wikipedia.org/wiki/Privacy-Enhanced_Mail. Twilio uses this information to process HTTPS traffic sent to your domain. | |

### Return type

[**MessagingV1DomainCertV4**](MessagingV1DomainCertV4.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **201** | Created |  -  |

