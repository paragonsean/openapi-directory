# DefaultApi

All URIs are relative to *https://extendsclass.com/api/json-storage*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**binIdDelete**](DefaultApi.md#binIdDelete) | **DELETE** /bin/{id} | Delete a json bin |
| [**binIdGet**](DefaultApi.md#binIdGet) | **GET** /bin/{id} | Return a json bin |
| [**binIdPatch**](DefaultApi.md#binIdPatch) | **PATCH** /bin/{id} | Partially update a json bin with JSON Merge Patch |
| [**binIdPut**](DefaultApi.md#binIdPut) | **PUT** /bin/{id} | Update a json bin |
| [**binPost**](DefaultApi.md#binPost) | **POST** /bin | Create a json bin |


<a id="binIdDelete"></a>
# **binIdDelete**
> DeleteStatus binIdDelete(id)

Delete a json bin

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://extendsclass.com/api/json-storage");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | 
    try {
      DeleteStatus result = apiInstance.binIdDelete(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#binIdDelete");
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

[**DeleteStatus**](DeleteStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Status of the deletion |  -  |
| **401** | Wrong security key |  -  |
| **404** | Bin not found |  -  |
| **422** | Id must be specified |  -  |

<a id="binIdGet"></a>
# **binIdGet**
> Object binIdGet(id)

Return a json bin

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://extendsclass.com/api/json-storage");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | 
    try {
      Object result = apiInstance.binIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#binIdGet");
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

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Bin data |  -  |
| **404** | Bin not found |  -  |
| **422** | Id must be specified |  -  |

<a id="binIdPatch"></a>
# **binIdPatch**
> UpdateStatus binIdPatch(id)

Partially update a json bin with JSON Merge Patch

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://extendsclass.com/api/json-storage");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | 
    try {
      UpdateStatus result = apiInstance.binIdPatch(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#binIdPatch");
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

[**UpdateStatus**](UpdateStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Bin data updated |  -  |
| **401** | Wrong security key |  -  |
| **404** | Bin not found |  -  |
| **413** | JSON data too large |  -  |
| **422** | Id must be specified |  -  |

<a id="binIdPut"></a>
# **binIdPut**
> UpdateStatus binIdPut(id)

Update a json bin

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://extendsclass.com/api/json-storage");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | 
    try {
      UpdateStatus result = apiInstance.binIdPut(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#binIdPut");
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

[**UpdateStatus**](UpdateStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Bin data updated |  -  |
| **401** | Wrong security key |  -  |
| **404** | Bin not found |  -  |
| **413** | JSON data too large |  -  |
| **422** | Id must be specified |  -  |

<a id="binPost"></a>
# **binPost**
> CreateStatus binPost()

Create a json bin

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://extendsclass.com/api/json-storage");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      CreateStatus result = apiInstance.binPost();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#binPost");
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

[**CreateStatus**](CreateStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Bin information (id and URL) |  -  |
| **413** | &#39;JSON data too large&#39; or &#39;Security key is too large&#39; |  -  |
| **422** | Security key is required for private bin |  -  |

