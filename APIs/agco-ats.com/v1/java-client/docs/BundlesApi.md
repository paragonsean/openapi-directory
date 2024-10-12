# BundlesApi

All URIs are relative to *https://secure.agco-ats.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**bundlesDeleteBundle**](BundlesApi.md#bundlesDeleteBundle) | **DELETE** /api/v2/Bundles/{ID} | Delete a Bundle. |
| [**bundlesGetBundle**](BundlesApi.md#bundlesGetBundle) | **GET** /api/v2/Bundles/{ID} | Get a specific Bundle by ID. |
| [**bundlesGetBundles**](BundlesApi.md#bundlesGetBundles) | **GET** /api/v2/Bundles | Get the list of bundles. |
| [**bundlesPostBundle**](BundlesApi.md#bundlesPostBundle) | **POST** /api/v2/Bundles | Add a Bundle to the Update System. |
| [**bundlesPutBundle**](BundlesApi.md#bundlesPutBundle) | **PUT** /api/v2/Bundles/{ID} | Modify a Bundle in the Update System. |


<a id="bundlesDeleteBundle"></a>
# **bundlesDeleteBundle**
> bundlesDeleteBundle(ID)

Delete a Bundle.

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BundlesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    BundlesApi apiInstance = new BundlesApi(defaultClient);
    String ID = "ID_example"; // String | The Bundle ID to Delete
    try {
      apiInstance.bundlesDeleteBundle(ID);
    } catch (ApiException e) {
      System.err.println("Exception when calling BundlesApi#bundlesDeleteBundle");
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
| **ID** | **String**| The Bundle ID to Delete | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |
| **0** | API Error Response |  -  |

<a id="bundlesGetBundle"></a>
# **bundlesGetBundle**
> UpdateSystemModelsBundle bundlesGetBundle(ID)

Get a specific Bundle by ID.

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BundlesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    BundlesApi apiInstance = new BundlesApi(defaultClient);
    String ID = "ID_example"; // String | The Bundle ID
    try {
      UpdateSystemModelsBundle result = apiInstance.bundlesGetBundle(ID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BundlesApi#bundlesGetBundle");
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
| **ID** | **String**| The Bundle ID | |

### Return type

[**UpdateSystemModelsBundle**](UpdateSystemModelsBundle.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | API Error Response |  -  |

<a id="bundlesGetBundles"></a>
# **bundlesGetBundles**
> APIPagedResponseUpdateSystemModelsBundle bundlesGetBundles(updateGroupID, active, limit, offset, bundleNumber)

Get the list of bundles.

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BundlesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    BundlesApi apiInstance = new BundlesApi(defaultClient);
    String updateGroupID = "updateGroupID_example"; // String | Optional. Filter by UpdateGroup ID.
    Boolean active = true; // Boolean | Optional. Filter by active status.
    Integer limit = 56; // Integer | Optional. The page limit. The default page limit is 10.
    Integer offset = 56; // Integer | Optional. The page offset. The default page offset is 0.
    Integer bundleNumber = 56; // Integer | Optional. If provided, filters by BundleNumber.
    try {
      APIPagedResponseUpdateSystemModelsBundle result = apiInstance.bundlesGetBundles(updateGroupID, active, limit, offset, bundleNumber);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BundlesApi#bundlesGetBundles");
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
| **updateGroupID** | **String**| Optional. Filter by UpdateGroup ID. | [optional] |
| **active** | **Boolean**| Optional. Filter by active status. | [optional] |
| **limit** | **Integer**| Optional. The page limit. The default page limit is 10. | [optional] |
| **offset** | **Integer**| Optional. The page offset. The default page offset is 0. | [optional] |
| **bundleNumber** | **Integer**| Optional. If provided, filters by BundleNumber. | [optional] |

### Return type

[**APIPagedResponseUpdateSystemModelsBundle**](APIPagedResponseUpdateSystemModelsBundle.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | API Error Response |  -  |

<a id="bundlesPostBundle"></a>
# **bundlesPostBundle**
> String bundlesPostBundle(updateSystemModelsBundle)

Add a Bundle to the Update System.

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BundlesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    BundlesApi apiInstance = new BundlesApi(defaultClient);
    UpdateSystemModelsBundle updateSystemModelsBundle = new UpdateSystemModelsBundle(); // UpdateSystemModelsBundle | The bundle to add
    try {
      String result = apiInstance.bundlesPostBundle(updateSystemModelsBundle);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BundlesApi#bundlesPostBundle");
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
| **updateSystemModelsBundle** | [**UpdateSystemModelsBundle**](UpdateSystemModelsBundle.md)| The bundle to add | |

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | API Error Response |  -  |

<a id="bundlesPutBundle"></a>
# **bundlesPutBundle**
> bundlesPutBundle(ID, updateSystemModelsBundle)

Modify a Bundle in the Update System.

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BundlesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    BundlesApi apiInstance = new BundlesApi(defaultClient);
    String ID = "ID_example"; // String | The unique ID of the Bundle
    UpdateSystemModelsBundle updateSystemModelsBundle = new UpdateSystemModelsBundle(); // UpdateSystemModelsBundle | The bundle to modify
    try {
      apiInstance.bundlesPutBundle(ID, updateSystemModelsBundle);
    } catch (ApiException e) {
      System.err.println("Exception when calling BundlesApi#bundlesPutBundle");
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
| **ID** | **String**| The unique ID of the Bundle | |
| **updateSystemModelsBundle** | [**UpdateSystemModelsBundle**](UpdateSystemModelsBundle.md)| The bundle to modify | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |
| **0** | API Error Response |  -  |

