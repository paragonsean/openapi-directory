# VendorsApi

All URIs are relative to *http://api.cambase.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiV1VendorsCreate**](VendorsApi.md#apiV1VendorsCreate) | **POST** /api/v1/vendors.json | Creates a new Vendor |
| [**apiV1VendorsIdJsonPatch**](VendorsApi.md#apiV1VendorsIdJsonPatch) | **PATCH** /api/v1/vendors/{id}.json | Updates an existing Vendor |
| [**apiV1VendorsIdJsonPut**](VendorsApi.md#apiV1VendorsIdJsonPut) | **PUT** /api/v1/vendors/{id}.json | Updates an existing Vendor |
| [**apiV1VendorsIndex**](VendorsApi.md#apiV1VendorsIndex) | **GET** /api/v1/vendors.json | Fetches all Vendors |
| [**apiV1VendorsShow**](VendorsApi.md#apiV1VendorsShow) | **GET** /api/v1/vendors/{id}.json | Fetches a single Vendor |


<a id="apiV1VendorsCreate"></a>
# **apiV1VendorsCreate**
> apiV1VendorsCreate(vendorName, vendorInfo, vendorUrl, vendorMac)

Creates a new Vendor

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VendorsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.cambase.io");

    VendorsApi apiInstance = new VendorsApi(defaultClient);
    String vendorName = "vendorName_example"; // String | Name
    String vendorInfo = "vendorInfo_example"; // String | Info.
    String vendorUrl = "vendorUrl_example"; // String | Website
    String vendorMac = "vendorMac_example"; // String | MAC
    try {
      apiInstance.apiV1VendorsCreate(vendorName, vendorInfo, vendorUrl, vendorMac);
    } catch (ApiException e) {
      System.err.println("Exception when calling VendorsApi#apiV1VendorsCreate");
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
| **vendorName** | **String**| Name | |
| **vendorInfo** | **String**| Info. | [optional] |
| **vendorUrl** | **String**| Website | [optional] |
| **vendorMac** | **String**| MAC | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |
| **401** | Unauthorized |  -  |
| **406** | Not Acceptable |  -  |

<a id="apiV1VendorsIdJsonPatch"></a>
# **apiV1VendorsIdJsonPatch**
> apiV1VendorsIdJsonPatch(id, vendorName, vendorInfo, vendorUrl, vendorMac)

Updates an existing Vendor

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VendorsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.cambase.io");

    VendorsApi apiInstance = new VendorsApi(defaultClient);
    String id = "id_example"; // String | Vendor ID
    String vendorName = "vendorName_example"; // String | Name
    String vendorInfo = "vendorInfo_example"; // String | Info.
    String vendorUrl = "vendorUrl_example"; // String | Website
    String vendorMac = "vendorMac_example"; // String | MAC
    try {
      apiInstance.apiV1VendorsIdJsonPatch(id, vendorName, vendorInfo, vendorUrl, vendorMac);
    } catch (ApiException e) {
      System.err.println("Exception when calling VendorsApi#apiV1VendorsIdJsonPatch");
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
| **id** | **String**| Vendor ID | |
| **vendorName** | **String**| Name | [optional] |
| **vendorInfo** | **String**| Info. | [optional] |
| **vendorUrl** | **String**| Website | [optional] |
| **vendorMac** | **String**| MAC | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |
| **406** | Not Acceptable |  -  |

<a id="apiV1VendorsIdJsonPut"></a>
# **apiV1VendorsIdJsonPut**
> apiV1VendorsIdJsonPut(id, vendorName, vendorInfo, vendorUrl, vendorMac)

Updates an existing Vendor

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VendorsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.cambase.io");

    VendorsApi apiInstance = new VendorsApi(defaultClient);
    String id = "id_example"; // String | Vendor ID
    String vendorName = "vendorName_example"; // String | Name
    String vendorInfo = "vendorInfo_example"; // String | Info.
    String vendorUrl = "vendorUrl_example"; // String | Website
    String vendorMac = "vendorMac_example"; // String | MAC
    try {
      apiInstance.apiV1VendorsIdJsonPut(id, vendorName, vendorInfo, vendorUrl, vendorMac);
    } catch (ApiException e) {
      System.err.println("Exception when calling VendorsApi#apiV1VendorsIdJsonPut");
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
| **id** | **String**| Vendor ID | |
| **vendorName** | **String**| Name | [optional] |
| **vendorInfo** | **String**| Info. | [optional] |
| **vendorUrl** | **String**| Website | [optional] |
| **vendorMac** | **String**| MAC | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |
| **406** | Not Acceptable |  -  |

<a id="apiV1VendorsIndex"></a>
# **apiV1VendorsIndex**
> apiV1VendorsIndex(page, order)

Fetches all Vendors

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VendorsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.cambase.io");

    VendorsApi apiInstance = new VendorsApi(defaultClient);
    Integer page = 56; // Integer | Page number
    String order = "order_example"; // String | Sort order
    try {
      apiInstance.apiV1VendorsIndex(page, order);
    } catch (ApiException e) {
      System.err.println("Exception when calling VendorsApi#apiV1VendorsIndex");
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
| **page** | **Integer**| Page number | [optional] |
| **order** | **String**| Sort order | [optional] |

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
| **200** | No response was specified |  -  |
| **401** | Unauthorized |  -  |
| **406** | The request you made is not acceptable |  -  |
| **416** | Requested Range Not Satisfiable |  -  |

<a id="apiV1VendorsShow"></a>
# **apiV1VendorsShow**
> apiV1VendorsShow(id, order)

Fetches a single Vendor

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VendorsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.cambase.io");

    VendorsApi apiInstance = new VendorsApi(defaultClient);
    String id = "id_example"; // String | Vendor ID
    String order = "order_example"; // String | Sort order
    try {
      apiInstance.apiV1VendorsShow(id, order);
    } catch (ApiException e) {
      System.err.println("Exception when calling VendorsApi#apiV1VendorsShow");
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
| **id** | **String**| Vendor ID | |
| **order** | **String**| Sort order | [optional] |

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
| **200** | No response was specified |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |
| **406** | Not Acceptable |  -  |

