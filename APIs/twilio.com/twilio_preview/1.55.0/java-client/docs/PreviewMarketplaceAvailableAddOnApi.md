# PreviewMarketplaceAvailableAddOnApi

All URIs are relative to *https://preview.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**fetchMarketplaceAvailableAddOn**](PreviewMarketplaceAvailableAddOnApi.md#fetchMarketplaceAvailableAddOn) | **GET** /marketplace/AvailableAddOns/{Sid} |  |
| [**listMarketplaceAvailableAddOn**](PreviewMarketplaceAvailableAddOnApi.md#listMarketplaceAvailableAddOn) | **GET** /marketplace/AvailableAddOns |  |


<a id="fetchMarketplaceAvailableAddOn"></a>
# **fetchMarketplaceAvailableAddOn**
> PreviewMarketplaceAvailableAddOn fetchMarketplaceAvailableAddOn(sid)



Fetch an instance of an Add-on currently available to be installed.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PreviewMarketplaceAvailableAddOnApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://preview.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    PreviewMarketplaceAvailableAddOnApi apiInstance = new PreviewMarketplaceAvailableAddOnApi(defaultClient);
    String sid = "sid_example"; // String | The SID of the AvailableAddOn resource to fetch.
    try {
      PreviewMarketplaceAvailableAddOn result = apiInstance.fetchMarketplaceAvailableAddOn(sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PreviewMarketplaceAvailableAddOnApi#fetchMarketplaceAvailableAddOn");
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
| **sid** | **String**| The SID of the AvailableAddOn resource to fetch. | |

### Return type

[**PreviewMarketplaceAvailableAddOn**](PreviewMarketplaceAvailableAddOn.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listMarketplaceAvailableAddOn"></a>
# **listMarketplaceAvailableAddOn**
> ListMarketplaceAvailableAddOnResponse listMarketplaceAvailableAddOn(pageSize, page, pageToken)



Retrieve a list of Add-ons currently available to be installed.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PreviewMarketplaceAvailableAddOnApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://preview.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    PreviewMarketplaceAvailableAddOnApi apiInstance = new PreviewMarketplaceAvailableAddOnApi(defaultClient);
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListMarketplaceAvailableAddOnResponse result = apiInstance.listMarketplaceAvailableAddOn(pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PreviewMarketplaceAvailableAddOnApi#listMarketplaceAvailableAddOn");
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
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListMarketplaceAvailableAddOnResponse**](ListMarketplaceAvailableAddOnResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

