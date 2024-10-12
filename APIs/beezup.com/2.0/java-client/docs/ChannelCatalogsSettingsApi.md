# ChannelCatalogsSettingsApi

All URIs are relative to *https://api.beezup.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**configureChannelCatalogCostSettings**](ChannelCatalogsSettingsApi.md#configureChannelCatalogCostSettings) | **PUT** /v2/user/channelCatalogs/{channelCatalogId}/settings/cost | Configure channel catalog cost settings |
| [**configureChannelCatalogGeneralSettings**](ChannelCatalogsSettingsApi.md#configureChannelCatalogGeneralSettings) | **PUT** /v2/user/channelCatalogs/{channelCatalogId}/settings/general | Configure channel catalog general settings |
| [**disableChannelCatalog**](ChannelCatalogsSettingsApi.md#disableChannelCatalog) | **POST** /v2/user/channelCatalogs/{channelCatalogId}/disable | Disable a channel catalog |
| [**enableChannelCatalog**](ChannelCatalogsSettingsApi.md#enableChannelCatalog) | **POST** /v2/user/channelCatalogs/{channelCatalogId}/enable | Enable a channel catalog |


<a id="configureChannelCatalogCostSettings"></a>
# **configureChannelCatalogCostSettings**
> configureChannelCatalogCostSettings(channelCatalogId, costSettings)

Configure channel catalog cost settings

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChannelCatalogsSettingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    ChannelCatalogsSettingsApi apiInstance = new ChannelCatalogsSettingsApi(defaultClient);
    String channelCatalogId = "6d6b04de-406b-4539-8e7e-bf3e8da5dfb0"; // String | The channel catalog identifier
    CostSettings costSettings = new CostSettings(); // CostSettings | 
    try {
      apiInstance.configureChannelCatalogCostSettings(channelCatalogId, costSettings);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChannelCatalogsSettingsApi#configureChannelCatalogCostSettings");
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
| **channelCatalogId** | **String**| The channel catalog identifier | |
| **costSettings** | [**CostSettings**](CostSettings.md)|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Channel catalog cost settings configured |  -  |
| **404** | Occurs when a user tries to work on the wrong ChanelCatalogId. |  -  |
| **0** | Occurs when something goes wrong |  -  |

<a id="configureChannelCatalogGeneralSettings"></a>
# **configureChannelCatalogGeneralSettings**
> configureChannelCatalogGeneralSettings(channelCatalogId, generalSettings)

Configure channel catalog general settings

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChannelCatalogsSettingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    ChannelCatalogsSettingsApi apiInstance = new ChannelCatalogsSettingsApi(defaultClient);
    String channelCatalogId = "6d6b04de-406b-4539-8e7e-bf3e8da5dfb0"; // String | The channel catalog identifier
    GeneralSettings generalSettings = new GeneralSettings(); // GeneralSettings | 
    try {
      apiInstance.configureChannelCatalogGeneralSettings(channelCatalogId, generalSettings);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChannelCatalogsSettingsApi#configureChannelCatalogGeneralSettings");
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
| **channelCatalogId** | **String**| The channel catalog identifier | |
| **generalSettings** | [**GeneralSettings**](GeneralSettings.md)|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Channel catalog general settings configured |  -  |
| **404** | Occurs when a user tries to work on the wrong ChanelCatalogId. |  -  |
| **0** | Occurs when something goes wrong |  -  |

<a id="disableChannelCatalog"></a>
# **disableChannelCatalog**
> disableChannelCatalog(channelCatalogId)

Disable a channel catalog

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChannelCatalogsSettingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    ChannelCatalogsSettingsApi apiInstance = new ChannelCatalogsSettingsApi(defaultClient);
    String channelCatalogId = "6d6b04de-406b-4539-8e7e-bf3e8da5dfb0"; // String | The channel catalog identifier
    try {
      apiInstance.disableChannelCatalog(channelCatalogId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChannelCatalogsSettingsApi#disableChannelCatalog");
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
| **channelCatalogId** | **String**| The channel catalog identifier | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Channel catalog disabled |  -  |
| **404** | Occurs when a user tries to work on the wrong ChanelCatalogId. |  -  |
| **0** | Occurs when something goes wrong |  -  |

<a id="enableChannelCatalog"></a>
# **enableChannelCatalog**
> enableChannelCatalog(channelCatalogId)

Enable a channel catalog

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChannelCatalogsSettingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    ChannelCatalogsSettingsApi apiInstance = new ChannelCatalogsSettingsApi(defaultClient);
    String channelCatalogId = "6d6b04de-406b-4539-8e7e-bf3e8da5dfb0"; // String | The channel catalog identifier
    try {
      apiInstance.enableChannelCatalog(channelCatalogId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChannelCatalogsSettingsApi#enableChannelCatalog");
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
| **channelCatalogId** | **String**| The channel catalog identifier | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Channel catalog enabled |  -  |
| **402** | You have to upgrade your offer to activate this channel catalog |  -  |
| **404** | Occurs when a user tries to work on the wrong ChanelCatalogId. |  -  |
| **0** | Occurs when something goes wrong |  -  |

