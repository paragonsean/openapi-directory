# VariationSetApi

All URIs are relative to */api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deleteVariantSetItem**](VariationSetApi.md#deleteVariantSetItem) | **DELETE** /variation/set/{id} | Deletes variant set |
| [**getVariantAnalyze**](VariationSetApi.md#getVariantAnalyze) | **GET** /variation/set/analyze/{id} | Returns list of matches |
| [**getVariantSetItem**](VariationSetApi.md#getVariantSetItem) | **GET** /variation/set/{id} | Returns a variant set |
| [**getVariantSetsArchiveCollection**](VariationSetApi.md#getVariantSetsArchiveCollection) | **GET** /variation/set/archive/{year}/{month}/{day} | Returns list of variant sets from a specified time period |
| [**getVariantSetsCollection**](VariationSetApi.md#getVariantSetsCollection) | **GET** /variation/set/ | Returns list of variant sets |
| [**postVariantSetsCollection**](VariationSetApi.md#postVariantSetsCollection) | **POST** /variation/set/ | Creates a new variant set |
| [**putVariantSetItem**](VariationSetApi.md#putVariantSetItem) | **PUT** /variation/set/{id} | Updates a variant set |


<a id="deleteVariantSetItem"></a>
# **deleteVariantSetItem**
> deleteVariantSetItem(id)

Deletes variant set

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VariationSetApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    VariationSetApi apiInstance = new VariationSetApi(defaultClient);
    String id = "id_example"; // String | 
    try {
      apiInstance.deleteVariantSetItem(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling VariationSetApi#deleteVariantSetItem");
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
| **id** | **String**|  | |

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
| **204** | VariantSet successfully deleted. |  -  |
| **404** | VariantSet not found. |  -  |

<a id="getVariantAnalyze"></a>
# **getVariantAnalyze**
> List&lt;Association&gt; getVariantAnalyze(id)

Returns list of matches

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VariationSetApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    VariationSetApi apiInstance = new VariationSetApi(defaultClient);
    String id = "id_example"; // String | 
    try {
      List<Association> result = apiInstance.getVariantAnalyze(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VariationSetApi#getVariantAnalyze");
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
| **id** | **String**|  | |

### Return type

[**List&lt;Association&gt;**](Association.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="getVariantSetItem"></a>
# **getVariantSetItem**
> VariantSet getVariantSetItem(id)

Returns a variant set

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VariationSetApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    VariationSetApi apiInstance = new VariationSetApi(defaultClient);
    String id = "id_example"; // String | 
    try {
      VariantSet result = apiInstance.getVariantSetItem(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VariationSetApi#getVariantSetItem");
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
| **id** | **String**|  | |

### Return type

[**VariantSet**](VariantSet.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **404** | VariantSet not found. |  -  |

<a id="getVariantSetsArchiveCollection"></a>
# **getVariantSetsArchiveCollection**
> PageOfVariantSets getVariantSetsArchiveCollection(year, month, day, page, perPage)

Returns list of variant sets from a specified time period

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VariationSetApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    VariationSetApi apiInstance = new VariationSetApi(defaultClient);
    Integer year = 56; // Integer | 
    Integer month = 56; // Integer | 
    Integer day = 56; // Integer | 
    Integer page = 1; // Integer | Page number
    Integer perPage = 2; // Integer | Results per page {error_msg}
    try {
      PageOfVariantSets result = apiInstance.getVariantSetsArchiveCollection(year, month, day, page, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VariationSetApi#getVariantSetsArchiveCollection");
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
| **year** | **Integer**|  | |
| **month** | **Integer**|  | |
| **day** | **Integer**|  | |
| **page** | **Integer**| Page number | [optional] [default to 1] |
| **perPage** | **Integer**| Results per page {error_msg} | [optional] [default to 10] [enum: 2, 10, 20, 30, 40, 50] |

### Return type

[**PageOfVariantSets**](PageOfVariantSets.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="getVariantSetsCollection"></a>
# **getVariantSetsCollection**
> PageOfVariantSets getVariantSetsCollection(page, perPage)

Returns list of variant sets

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VariationSetApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    VariationSetApi apiInstance = new VariationSetApi(defaultClient);
    Integer page = 1; // Integer | Page number
    Integer perPage = 2; // Integer | Results per page {error_msg}
    try {
      PageOfVariantSets result = apiInstance.getVariantSetsCollection(page, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VariationSetApi#getVariantSetsCollection");
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
| **page** | **Integer**| Page number | [optional] [default to 1] |
| **perPage** | **Integer**| Results per page {error_msg} | [optional] [default to 10] [enum: 2, 10, 20, 30, 40, 50] |

### Return type

[**PageOfVariantSets**](PageOfVariantSets.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="postVariantSetsCollection"></a>
# **postVariantSetsCollection**
> postVariantSetsCollection(variantSet)

Creates a new variant set

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VariationSetApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    VariationSetApi apiInstance = new VariationSetApi(defaultClient);
    VariantSet variantSet = new VariantSet(); // VariantSet | 
    try {
      apiInstance.postVariantSetsCollection(variantSet);
    } catch (ApiException e) {
      System.err.println("Exception when calling VariationSetApi#postVariantSetsCollection");
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
| **variantSet** | [**VariantSet**](VariantSet.md)|  | |

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
| **200** | Success |  -  |

<a id="putVariantSetItem"></a>
# **putVariantSetItem**
> putVariantSetItem(id, variantSet)

Updates a variant set

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VariationSetApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    VariationSetApi apiInstance = new VariationSetApi(defaultClient);
    String id = "id_example"; // String | 
    VariantSet variantSet = new VariantSet(); // VariantSet | 
    try {
      apiInstance.putVariantSetItem(id, variantSet);
    } catch (ApiException e) {
      System.err.println("Exception when calling VariationSetApi#putVariantSetItem");
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
| **id** | **String**|  | |
| **variantSet** | [**VariantSet**](VariantSet.md)|  | |

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
| **204** | VariantSet successfully updated. |  -  |
| **404** | VariantSet not found. |  -  |

