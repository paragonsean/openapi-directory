# PreviewMarketplaceAvailableAddOnExtensionApi

All URIs are relative to *https://preview.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**fetchMarketplaceAvailableAddOnExtension**](PreviewMarketplaceAvailableAddOnExtensionApi.md#fetchMarketplaceAvailableAddOnExtension) | **GET** /marketplace/AvailableAddOns/{AvailableAddOnSid}/Extensions/{Sid} |  |
| [**listMarketplaceAvailableAddOnExtension**](PreviewMarketplaceAvailableAddOnExtensionApi.md#listMarketplaceAvailableAddOnExtension) | **GET** /marketplace/AvailableAddOns/{AvailableAddOnSid}/Extensions |  |


<a id="fetchMarketplaceAvailableAddOnExtension"></a>
# **fetchMarketplaceAvailableAddOnExtension**
> PreviewMarketplaceAvailableAddOnAvailableAddOnExtension fetchMarketplaceAvailableAddOnExtension(availableAddOnSid, sid)



Fetch an instance of an Extension for the Available Add-on.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PreviewMarketplaceAvailableAddOnExtensionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://preview.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    PreviewMarketplaceAvailableAddOnExtensionApi apiInstance = new PreviewMarketplaceAvailableAddOnExtensionApi(defaultClient);
    String availableAddOnSid = "availableAddOnSid_example"; // String | The SID of the AvailableAddOn resource with the extension to fetch.
    String sid = "sid_example"; // String | The SID of the AvailableAddOn Extension resource to fetch.
    try {
      PreviewMarketplaceAvailableAddOnAvailableAddOnExtension result = apiInstance.fetchMarketplaceAvailableAddOnExtension(availableAddOnSid, sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PreviewMarketplaceAvailableAddOnExtensionApi#fetchMarketplaceAvailableAddOnExtension");
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
| **availableAddOnSid** | **String**| The SID of the AvailableAddOn resource with the extension to fetch. | |
| **sid** | **String**| The SID of the AvailableAddOn Extension resource to fetch. | |

### Return type

[**PreviewMarketplaceAvailableAddOnAvailableAddOnExtension**](PreviewMarketplaceAvailableAddOnAvailableAddOnExtension.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listMarketplaceAvailableAddOnExtension"></a>
# **listMarketplaceAvailableAddOnExtension**
> ListMarketplaceAvailableAddOnExtensionResponse listMarketplaceAvailableAddOnExtension(availableAddOnSid, pageSize, page, pageToken)



Retrieve a list of Extensions for the Available Add-on.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PreviewMarketplaceAvailableAddOnExtensionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://preview.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    PreviewMarketplaceAvailableAddOnExtensionApi apiInstance = new PreviewMarketplaceAvailableAddOnExtensionApi(defaultClient);
    String availableAddOnSid = "availableAddOnSid_example"; // String | The SID of the AvailableAddOn resource with the extensions to read.
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListMarketplaceAvailableAddOnExtensionResponse result = apiInstance.listMarketplaceAvailableAddOnExtension(availableAddOnSid, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PreviewMarketplaceAvailableAddOnExtensionApi#listMarketplaceAvailableAddOnExtension");
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
| **availableAddOnSid** | **String**| The SID of the AvailableAddOn resource with the extensions to read. | |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListMarketplaceAvailableAddOnExtensionResponse**](ListMarketplaceAvailableAddOnExtensionResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

