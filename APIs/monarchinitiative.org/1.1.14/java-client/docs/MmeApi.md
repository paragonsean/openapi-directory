# MmeApi

All URIs are relative to */api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**postDiseaseMme**](MmeApi.md#postDiseaseMme) | **POST** /mme/disease | Match a patient to diseases based on their phenotypes |
| [**postFlyMme**](MmeApi.md#postFlyMme) | **POST** /mme/fly | Match a patient to fruit fly genes based on similar phenotypes |
| [**postMouseMme**](MmeApi.md#postMouseMme) | **POST** /mme/mouse | Match a patient to mouse genes based on similar phenotypes |
| [**postNematodeMme**](MmeApi.md#postNematodeMme) | **POST** /mme/nematode | Match a patient to nematode genes based on similar phenotypes |
| [**postZebrafishMme**](MmeApi.md#postZebrafishMme) | **POST** /mme/zebrafish | Match a patient to zebrafish genes based on similar phenotypes |


<a id="postDiseaseMme"></a>
# **postDiseaseMme**
> postDiseaseMme(body)

Match a patient to diseases based on their phenotypes

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MmeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    MmeApi apiInstance = new MmeApi(defaultClient);
    Object body = null; // Object | 
    try {
      apiInstance.postDiseaseMme(body);
    } catch (ApiException e) {
      System.err.println("Exception when calling MmeApi#postDiseaseMme");
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
| **body** | **Object**|  | |

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

<a id="postFlyMme"></a>
# **postFlyMme**
> postFlyMme(body)

Match a patient to fruit fly genes based on similar phenotypes

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MmeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    MmeApi apiInstance = new MmeApi(defaultClient);
    Object body = null; // Object | 
    try {
      apiInstance.postFlyMme(body);
    } catch (ApiException e) {
      System.err.println("Exception when calling MmeApi#postFlyMme");
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
| **body** | **Object**|  | |

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

<a id="postMouseMme"></a>
# **postMouseMme**
> postMouseMme(body)

Match a patient to mouse genes based on similar phenotypes

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MmeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    MmeApi apiInstance = new MmeApi(defaultClient);
    Object body = null; // Object | 
    try {
      apiInstance.postMouseMme(body);
    } catch (ApiException e) {
      System.err.println("Exception when calling MmeApi#postMouseMme");
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
| **body** | **Object**|  | |

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

<a id="postNematodeMme"></a>
# **postNematodeMme**
> postNematodeMme(body)

Match a patient to nematode genes based on similar phenotypes

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MmeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    MmeApi apiInstance = new MmeApi(defaultClient);
    Object body = null; // Object | 
    try {
      apiInstance.postNematodeMme(body);
    } catch (ApiException e) {
      System.err.println("Exception when calling MmeApi#postNematodeMme");
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
| **body** | **Object**|  | |

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

<a id="postZebrafishMme"></a>
# **postZebrafishMme**
> postZebrafishMme(body)

Match a patient to zebrafish genes based on similar phenotypes

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MmeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    MmeApi apiInstance = new MmeApi(defaultClient);
    Object body = null; // Object | 
    try {
      apiInstance.postZebrafishMme(body);
    } catch (ApiException e) {
      System.err.println("Exception when calling MmeApi#postZebrafishMme");
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
| **body** | **Object**|  | |

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

