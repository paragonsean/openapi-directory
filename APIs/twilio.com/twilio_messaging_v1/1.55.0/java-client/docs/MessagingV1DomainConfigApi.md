# MessagingV1DomainConfigApi

All URIs are relative to *https://messaging.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**fetchDomainConfig**](MessagingV1DomainConfigApi.md#fetchDomainConfig) | **GET** /v1/LinkShortening/Domains/{DomainSid}/Config |  |
| [**updateDomainConfig**](MessagingV1DomainConfigApi.md#updateDomainConfig) | **POST** /v1/LinkShortening/Domains/{DomainSid}/Config |  |


<a id="fetchDomainConfig"></a>
# **fetchDomainConfig**
> MessagingV1DomainConfig fetchDomainConfig(domainSid)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MessagingV1DomainConfigApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://messaging.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    MessagingV1DomainConfigApi apiInstance = new MessagingV1DomainConfigApi(defaultClient);
    String domainSid = "domainSid_example"; // String | Unique string used to identify the domain that this config should be associated with.
    try {
      MessagingV1DomainConfig result = apiInstance.fetchDomainConfig(domainSid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MessagingV1DomainConfigApi#fetchDomainConfig");
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
| **domainSid** | **String**| Unique string used to identify the domain that this config should be associated with. | |

### Return type

[**MessagingV1DomainConfig**](MessagingV1DomainConfig.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updateDomainConfig"></a>
# **updateDomainConfig**
> MessagingV1DomainConfig updateDomainConfig(domainSid, callbackUrl, continueOnFailure, disableHttps, fallbackUrl)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MessagingV1DomainConfigApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://messaging.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    MessagingV1DomainConfigApi apiInstance = new MessagingV1DomainConfigApi(defaultClient);
    String domainSid = "domainSid_example"; // String | Unique string used to identify the domain that this config should be associated with.
    URI callbackUrl = new URI(); // URI | URL to receive click events to your webhook whenever the recipients click on the shortened links
    Boolean continueOnFailure = true; // Boolean | Boolean field to set customer delivery preference when there is a failure in linkShortening service
    Boolean disableHttps = true; // Boolean | Customer's choice to send links with/without \\\"https://\\\" attached to shortened url. If true, messages will not be sent with https:// at the beginning of the url. If false, messages will be sent with https:// at the beginning of the url. False is the default behavior if it is not specified.
    URI fallbackUrl = new URI(); // URI | Any requests we receive to this domain that do not match an existing shortened message will be redirected to the fallback url. These will likely be either expired messages, random misdirected traffic, or intentional scraping.
    try {
      MessagingV1DomainConfig result = apiInstance.updateDomainConfig(domainSid, callbackUrl, continueOnFailure, disableHttps, fallbackUrl);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MessagingV1DomainConfigApi#updateDomainConfig");
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
| **domainSid** | **String**| Unique string used to identify the domain that this config should be associated with. | |
| **callbackUrl** | **URI**| URL to receive click events to your webhook whenever the recipients click on the shortened links | [optional] |
| **continueOnFailure** | **Boolean**| Boolean field to set customer delivery preference when there is a failure in linkShortening service | [optional] |
| **disableHttps** | **Boolean**| Customer&#39;s choice to send links with/without \\\&quot;https://\\\&quot; attached to shortened url. If true, messages will not be sent with https:// at the beginning of the url. If false, messages will be sent with https:// at the beginning of the url. False is the default behavior if it is not specified. | [optional] |
| **fallbackUrl** | **URI**| Any requests we receive to this domain that do not match an existing shortened message will be redirected to the fallback url. These will likely be either expired messages, random misdirected traffic, or intentional scraping. | [optional] |

### Return type

[**MessagingV1DomainConfig**](MessagingV1DomainConfig.md)

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

