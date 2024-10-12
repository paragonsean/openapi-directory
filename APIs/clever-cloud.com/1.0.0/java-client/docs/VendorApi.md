# VendorApi

All URIs are relative to *https://api.clever-cloud.com/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getVendorAppsAddonId_0**](VendorApi.md#getVendorAppsAddonId_0) | **GET** /vendor/apps/{addonId} |  |
| [**getVendorApps_0**](VendorApi.md#getVendorApps_0) | **GET** /vendor/apps |  |
| [**postVendorBillingOwnerId_0**](VendorApi.md#postVendorBillingOwnerId_0) | **POST** /vendor/apps/{addonId}/consumptions |  |
| [**putVendorAppsAddonId_0**](VendorApi.md#putVendorAppsAddonId_0) | **PUT** /vendor/apps/{addonId} |  |
| [**vendorAddonsPost_1**](VendorApi.md#vendorAddonsPost_1) | **POST** /vendor//addons |  |
| [**vendorAppsAddonIdLogscollectorGet_0**](VendorApi.md#vendorAppsAddonIdLogscollectorGet_0) | **GET** /vendor//apps/{addonId}/logscollector |  |
| [**vendorAppsAddonIdMigrationCallbackPut_0**](VendorApi.md#vendorAppsAddonIdMigrationCallbackPut_0) | **PUT** /vendor/apps/{addonId}/migration_callback |  |


<a id="getVendorAppsAddonId_0"></a>
# **getVendorAppsAddonId_0**
> getVendorAppsAddonId_0(addonId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VendorApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    VendorApi apiInstance = new VendorApi(defaultClient);
    String addonId = "addonId_example"; // String | 
    try {
      apiInstance.getVendorAppsAddonId_0(addonId);
    } catch (ApiException e) {
      System.err.println("Exception when calling VendorApi#getVendorAppsAddonId_0");
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
| **addonId** | **String**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | getApplicationInfo |  -  |

<a id="getVendorApps_0"></a>
# **getVendorApps_0**
> List&lt;Application&gt; getVendorApps_0(offset)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VendorApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    VendorApi apiInstance = new VendorApi(defaultClient);
    Integer offset = 56; // Integer | 
    try {
      List<Application> result = apiInstance.getVendorApps_0(offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VendorApi#getVendorApps_0");
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
| **offset** | **Integer**|  | [optional] |

### Return type

[**List&lt;Application&gt;**](Application.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | listApps |  -  |

<a id="postVendorBillingOwnerId_0"></a>
# **postVendorBillingOwnerId_0**
> postVendorBillingOwnerId_0(addonId, wannabeAddonBilling)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VendorApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    VendorApi apiInstance = new VendorApi(defaultClient);
    String addonId = "addonId_example"; // String | 
    WannabeAddonBilling wannabeAddonBilling = new WannabeAddonBilling(); // WannabeAddonBilling | 
    try {
      apiInstance.postVendorBillingOwnerId_0(addonId, wannabeAddonBilling);
    } catch (ApiException e) {
      System.err.println("Exception when calling VendorApi#postVendorBillingOwnerId_0");
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
| **addonId** | **String**|  | |
| **wannabeAddonBilling** | [**WannabeAddonBilling**](WannabeAddonBilling.md)|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Status 200 |  -  |

<a id="putVendorAppsAddonId_0"></a>
# **putVendorAppsAddonId_0**
> putVendorAppsAddonId_0(addonId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VendorApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    VendorApi apiInstance = new VendorApi(defaultClient);
    String addonId = "addonId_example"; // String | 
    try {
      apiInstance.putVendorAppsAddonId_0(addonId);
    } catch (ApiException e) {
      System.err.println("Exception when calling VendorApi#putVendorAppsAddonId_0");
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
| **addonId** | **String**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | editApplicationConfiguration |  -  |

<a id="vendorAddonsPost_1"></a>
# **vendorAddonsPost_1**
> vendorAddonsPost_1()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VendorApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    VendorApi apiInstance = new VendorApi(defaultClient);
    try {
      apiInstance.vendorAddonsPost_1();
    } catch (ApiException e) {
      System.err.println("Exception when calling VendorApi#vendorAddonsPost_1");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Status 200 |  -  |

<a id="vendorAppsAddonIdLogscollectorGet_0"></a>
# **vendorAppsAddonIdLogscollectorGet_0**
> vendorAppsAddonIdLogscollectorGet_0(addonId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VendorApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    VendorApi apiInstance = new VendorApi(defaultClient);
    String addonId = "addonId_example"; // String | 
    try {
      apiInstance.vendorAppsAddonIdLogscollectorGet_0(addonId);
    } catch (ApiException e) {
      System.err.println("Exception when calling VendorApi#vendorAppsAddonIdLogscollectorGet_0");
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
| **addonId** | **String**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Status 200 |  -  |

<a id="vendorAppsAddonIdMigrationCallbackPut_0"></a>
# **vendorAppsAddonIdMigrationCallbackPut_0**
> vendorAppsAddonIdMigrationCallbackPut_0(addonId, planId, region)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VendorApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.clever-cloud.com/v2");

    VendorApi apiInstance = new VendorApi(defaultClient);
    String addonId = "addonId_example"; // String | 
    String planId = "planId_example"; // String | 
    String region = "region_example"; // String | 
    try {
      apiInstance.vendorAppsAddonIdMigrationCallbackPut_0(addonId, planId, region);
    } catch (ApiException e) {
      System.err.println("Exception when calling VendorApi#vendorAppsAddonIdMigrationCallbackPut_0");
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
| **addonId** | **String**|  | |
| **planId** | **String**|  | [optional] |
| **region** | **String**|  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Status 200 |  -  |

