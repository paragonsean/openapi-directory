# CatalogsAutoApi

All URIs are relative to *https://api.beezup.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**autoConfigureAutoImportInterval**](CatalogsAutoApi.md#autoConfigureAutoImportInterval) | **POST** /v2/user/catalogs/{storeId}/autoImport/scheduling/interval | Configure Auto Import Interval |
| [**autoDeleteAutoImport**](CatalogsAutoApi.md#autoDeleteAutoImport) | **DELETE** /v2/user/catalogs/{storeId}/autoImport | Delete Auto Import |
| [**autoGetAutoImportConfiguration**](CatalogsAutoApi.md#autoGetAutoImportConfiguration) | **GET** /v2/user/catalogs/{storeId}/autoImport | Get the auto import configuration |
| [**autoPauseAutoImport**](CatalogsAutoApi.md#autoPauseAutoImport) | **POST** /v2/user/catalogs/{storeId}/autoImport/pause | Pause Auto Import |
| [**autoResumeAutoImport**](CatalogsAutoApi.md#autoResumeAutoImport) | **POST** /v2/user/catalogs/{storeId}/autoImport/resume | Resume Auto Import |
| [**autoScheduleAutoImport**](CatalogsAutoApi.md#autoScheduleAutoImport) | **POST** /v2/user/catalogs/{storeId}/autoImport/scheduling/schedules | Configure Auto Import Schedules |
| [**autoStartAutoImport**](CatalogsAutoApi.md#autoStartAutoImport) | **POST** /v2/user/catalogs/{storeId}/autoImport/start | Start Auto Import Manually |
| [**importationActivateAutoImport**](CatalogsAutoApi.md#importationActivateAutoImport) | **POST** /v2/user/catalogs/{storeId}/autoImport/activate | Activate the auto importation of the last successful manual catalog importation. |


<a id="autoConfigureAutoImportInterval"></a>
# **autoConfigureAutoImportInterval**
> autoConfigureAutoImportInterval(storeId, configureAutoImportIntervalRequest)

Configure Auto Import Interval

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CatalogsAutoApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    CatalogsAutoApi apiInstance = new CatalogsAutoApi(defaultClient);
    String storeId = "storeId_example"; // String | Your store identifier
    ConfigureAutoImportIntervalRequest configureAutoImportIntervalRequest = new ConfigureAutoImportIntervalRequest(); // ConfigureAutoImportIntervalRequest | 
    try {
      apiInstance.autoConfigureAutoImportInterval(storeId, configureAutoImportIntervalRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling CatalogsAutoApi#autoConfigureAutoImportInterval");
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
| **storeId** | **String**| Your store identifier | |
| **configureAutoImportIntervalRequest** | [**ConfigureAutoImportIntervalRequest**](ConfigureAutoImportIntervalRequest.md)|  | |

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
| **204** | Auto import scheduling interval saved |  -  |
| **400** |  When the min catalog Auto Import scheduling interval delay has been reached. When the max catalog Auto Import count has been reached. |  -  |
| **404** | Occurs when a user tries to work on the wrong store. |  -  |
| **0** | Occurs when something goes wrong |  -  |

<a id="autoDeleteAutoImport"></a>
# **autoDeleteAutoImport**
> autoDeleteAutoImport(storeId)

Delete Auto Import

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CatalogsAutoApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    CatalogsAutoApi apiInstance = new CatalogsAutoApi(defaultClient);
    String storeId = "storeId_example"; // String | Your store identifier
    try {
      apiInstance.autoDeleteAutoImport(storeId);
    } catch (ApiException e) {
      System.err.println("Exception when calling CatalogsAutoApi#autoDeleteAutoImport");
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
| **storeId** | **String**| Your store identifier | |

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
| **204** | Auto import deleted |  -  |
| **400** | Occurs when the catalog auto import is not configured. |  -  |
| **404** | Occurs when a user tries to work on the wrong store. |  -  |
| **0** | Occurs when something goes wrong |  -  |

<a id="autoGetAutoImportConfiguration"></a>
# **autoGetAutoImportConfiguration**
> AutoImportConfiguration autoGetAutoImportConfiguration(storeId)

Get the auto import configuration

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CatalogsAutoApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    CatalogsAutoApi apiInstance = new CatalogsAutoApi(defaultClient);
    String storeId = "storeId_example"; // String | Your store identifier
    try {
      AutoImportConfiguration result = apiInstance.autoGetAutoImportConfiguration(storeId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CatalogsAutoApi#autoGetAutoImportConfiguration");
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
| **storeId** | **String**| Your store identifier | |

### Return type

[**AutoImportConfiguration**](AutoImportConfiguration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Auto import configuration |  -  |
| **404** | StoreId or Auto Import configuration not found |  -  |
| **0** | Occurs when something goes wrong |  -  |

<a id="autoPauseAutoImport"></a>
# **autoPauseAutoImport**
> autoPauseAutoImport(storeId)

Pause Auto Import

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CatalogsAutoApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    CatalogsAutoApi apiInstance = new CatalogsAutoApi(defaultClient);
    String storeId = "storeId_example"; // String | Your store identifier
    try {
      apiInstance.autoPauseAutoImport(storeId);
    } catch (ApiException e) {
      System.err.println("Exception when calling CatalogsAutoApi#autoPauseAutoImport");
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
| **storeId** | **String**| Your store identifier | |

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
| **204** | Auto import paused |  -  |
| **400** | Occurs when the catalog auto import is not configured. |  -  |
| **404** | Occurs when a user tries to work on the wrong store. |  -  |
| **0** | Occurs when something goes wrong |  -  |

<a id="autoResumeAutoImport"></a>
# **autoResumeAutoImport**
> autoResumeAutoImport(storeId)

Resume Auto Import

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CatalogsAutoApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    CatalogsAutoApi apiInstance = new CatalogsAutoApi(defaultClient);
    String storeId = "storeId_example"; // String | Your store identifier
    try {
      apiInstance.autoResumeAutoImport(storeId);
    } catch (ApiException e) {
      System.err.println("Exception when calling CatalogsAutoApi#autoResumeAutoImport");
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
| **storeId** | **String**| Your store identifier | |

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
| **204** | Auto import resumed |  -  |
| **400** | Occurs when the catalog auto import is not configured. |  -  |
| **404** | Occurs when a user tries to work on the wrong store. |  -  |
| **0** | Occurs when something goes wrong |  -  |

<a id="autoScheduleAutoImport"></a>
# **autoScheduleAutoImport**
> autoScheduleAutoImport(storeId, scheduleAutoImportRequest)

Configure Auto Import Schedules

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CatalogsAutoApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    CatalogsAutoApi apiInstance = new CatalogsAutoApi(defaultClient);
    String storeId = "storeId_example"; // String | Your store identifier
    ScheduleAutoImportRequest scheduleAutoImportRequest = new ScheduleAutoImportRequest(); // ScheduleAutoImportRequest | 
    try {
      apiInstance.autoScheduleAutoImport(storeId, scheduleAutoImportRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling CatalogsAutoApi#autoScheduleAutoImport");
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
| **storeId** | **String**| Your store identifier | |
| **scheduleAutoImportRequest** | [**ScheduleAutoImportRequest**](ScheduleAutoImportRequest.md)|  | |

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
| **204** | Auto import scheduling saved |  -  |
| **400** |  When the max catalog Auto Import count has been reached. When the min catalog Auto Import scheduling interval delay has been reached. When the max catalog Auto Import count has been reached. |  -  |
| **404** | Occurs when a user tries to work on the wrong store. |  -  |
| **0** | Occurs when something goes wrong |  -  |

<a id="autoStartAutoImport"></a>
# **autoStartAutoImport**
> LinksImportationGetImportationMonitoringLink autoStartAutoImport(storeId)

Start Auto Import Manually

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CatalogsAutoApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    CatalogsAutoApi apiInstance = new CatalogsAutoApi(defaultClient);
    String storeId = "storeId_example"; // String | Your store identifier
    try {
      LinksImportationGetImportationMonitoringLink result = apiInstance.autoStartAutoImport(storeId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CatalogsAutoApi#autoStartAutoImport");
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
| **storeId** | **String**| Your store identifier | |

### Return type

[**LinksImportationGetImportationMonitoringLink**](LinksImportationGetImportationMonitoringLink.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Catalog importation started |  * Location - The location of the generated invoice. Might take a few seconds to be available <br>  * Retry-After - The duration in second to wait before polling this resource <br>  |
| **400** | Occurs when the catalog auto import is not configured. When a user column name is duplicate. When the catalog column name are duplicate. When the BeezUP column have duplicate mapping. Occurs when the required beezup column is not mapped to any column. Occurs when the category hierarchy is not correctly mapped. Occurs when the duplicate strategy on {catalogColumnName} is not found. When the user tries to import to ofen the catalog file to download count max limit has been reached. |  -  |
| **404** | Occurs when a user tries to work on the wrong store. |  -  |
| **409** | An importation is already in progress |  -  |
| **0** | Occurs when something goes wrong |  -  |

<a id="importationActivateAutoImport"></a>
# **importationActivateAutoImport**
> importationActivateAutoImport(storeId)

Activate the auto importation of the last successful manual catalog importation.

Once you have made your fist manual catalog importation with success, you can call this operation to import it automatically. No parameter required, we know which one it is.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CatalogsAutoApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    CatalogsAutoApi apiInstance = new CatalogsAutoApi(defaultClient);
    String storeId = "storeId_example"; // String | Your store identifier
    try {
      apiInstance.importationActivateAutoImport(storeId);
    } catch (ApiException e) {
      System.err.println("Exception when calling CatalogsAutoApi#importationActivateAutoImport");
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
| **storeId** | **String**| Your store identifier | |

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
| **204** | Auto import activated |  -  |
| **400** | Occurs when the user tries to auto import a local file. |  -  |
| **404** | Occurs when a user tries to work on the wrong store. |  -  |
| **409** | When a catalog importation is already in progress! |  -  |
| **0** | Occurs when something goes wrong |  -  |

