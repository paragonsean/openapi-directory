# PreviewMarketplaceInstalledAddOnExtensionApi

All URIs are relative to *https://preview.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**fetchMarketplaceInstalledAddOnExtension**](PreviewMarketplaceInstalledAddOnExtensionApi.md#fetchMarketplaceInstalledAddOnExtension) | **GET** /marketplace/InstalledAddOns/{InstalledAddOnSid}/Extensions/{Sid} |  |
| [**listMarketplaceInstalledAddOnExtension**](PreviewMarketplaceInstalledAddOnExtensionApi.md#listMarketplaceInstalledAddOnExtension) | **GET** /marketplace/InstalledAddOns/{InstalledAddOnSid}/Extensions |  |
| [**updateMarketplaceInstalledAddOnExtension**](PreviewMarketplaceInstalledAddOnExtensionApi.md#updateMarketplaceInstalledAddOnExtension) | **POST** /marketplace/InstalledAddOns/{InstalledAddOnSid}/Extensions/{Sid} |  |


<a id="fetchMarketplaceInstalledAddOnExtension"></a>
# **fetchMarketplaceInstalledAddOnExtension**
> PreviewMarketplaceInstalledAddOnInstalledAddOnExtension fetchMarketplaceInstalledAddOnExtension(installedAddOnSid, sid)



Fetch an instance of an Extension for the Installed Add-on.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PreviewMarketplaceInstalledAddOnExtensionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://preview.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    PreviewMarketplaceInstalledAddOnExtensionApi apiInstance = new PreviewMarketplaceInstalledAddOnExtensionApi(defaultClient);
    String installedAddOnSid = "installedAddOnSid_example"; // String | The SID of the InstalledAddOn resource with the extension to fetch.
    String sid = "sid_example"; // String | The SID of the InstalledAddOn Extension resource to fetch.
    try {
      PreviewMarketplaceInstalledAddOnInstalledAddOnExtension result = apiInstance.fetchMarketplaceInstalledAddOnExtension(installedAddOnSid, sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PreviewMarketplaceInstalledAddOnExtensionApi#fetchMarketplaceInstalledAddOnExtension");
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
| **installedAddOnSid** | **String**| The SID of the InstalledAddOn resource with the extension to fetch. | |
| **sid** | **String**| The SID of the InstalledAddOn Extension resource to fetch. | |

### Return type

[**PreviewMarketplaceInstalledAddOnInstalledAddOnExtension**](PreviewMarketplaceInstalledAddOnInstalledAddOnExtension.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listMarketplaceInstalledAddOnExtension"></a>
# **listMarketplaceInstalledAddOnExtension**
> ListMarketplaceInstalledAddOnExtensionResponse listMarketplaceInstalledAddOnExtension(installedAddOnSid, pageSize, page, pageToken)



Retrieve a list of Extensions for the Installed Add-on.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PreviewMarketplaceInstalledAddOnExtensionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://preview.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    PreviewMarketplaceInstalledAddOnExtensionApi apiInstance = new PreviewMarketplaceInstalledAddOnExtensionApi(defaultClient);
    String installedAddOnSid = "installedAddOnSid_example"; // String | The SID of the InstalledAddOn resource with the extensions to read.
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListMarketplaceInstalledAddOnExtensionResponse result = apiInstance.listMarketplaceInstalledAddOnExtension(installedAddOnSid, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PreviewMarketplaceInstalledAddOnExtensionApi#listMarketplaceInstalledAddOnExtension");
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
| **installedAddOnSid** | **String**| The SID of the InstalledAddOn resource with the extensions to read. | |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListMarketplaceInstalledAddOnExtensionResponse**](ListMarketplaceInstalledAddOnExtensionResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updateMarketplaceInstalledAddOnExtension"></a>
# **updateMarketplaceInstalledAddOnExtension**
> PreviewMarketplaceInstalledAddOnInstalledAddOnExtension updateMarketplaceInstalledAddOnExtension(installedAddOnSid, sid, enabled)



Update an Extension for an Add-on installation.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PreviewMarketplaceInstalledAddOnExtensionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://preview.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    PreviewMarketplaceInstalledAddOnExtensionApi apiInstance = new PreviewMarketplaceInstalledAddOnExtensionApi(defaultClient);
    String installedAddOnSid = "installedAddOnSid_example"; // String | The SID of the InstalledAddOn resource with the extension to update.
    String sid = "sid_example"; // String | The SID of the InstalledAddOn Extension resource to update.
    Boolean enabled = true; // Boolean | Whether the Extension should be invoked.
    try {
      PreviewMarketplaceInstalledAddOnInstalledAddOnExtension result = apiInstance.updateMarketplaceInstalledAddOnExtension(installedAddOnSid, sid, enabled);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PreviewMarketplaceInstalledAddOnExtensionApi#updateMarketplaceInstalledAddOnExtension");
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
| **installedAddOnSid** | **String**| The SID of the InstalledAddOn resource with the extension to update. | |
| **sid** | **String**| The SID of the InstalledAddOn Extension resource to update. | |
| **enabled** | **Boolean**| Whether the Extension should be invoked. | |

### Return type

[**PreviewMarketplaceInstalledAddOnInstalledAddOnExtension**](PreviewMarketplaceInstalledAddOnInstalledAddOnExtension.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

