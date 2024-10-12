# CamApi

All URIs are relative to */api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getActivityCollection**](CamApi.md#getActivityCollection) | **GET** /cam/activity | Returns list of models |
| [**getInstanceObject**](CamApi.md#getInstanceObject) | **GET** /cam/instance/{id} | Returns list of matches |
| [**getModelCollection**](CamApi.md#getModelCollection) | **GET** /cam/model | Returns list of ALL models |
| [**getModelContributors**](CamApi.md#getModelContributors) | **GET** /cam/model/contributors | Returns list of all contributors across all models |
| [**getModelInstances**](CamApi.md#getModelInstances) | **GET** /cam/instances | Returns list of all instances |
| [**getModelObject**](CamApi.md#getModelObject) | **GET** /cam/model/{id} | Returns a complete model |
| [**getModelProperties**](CamApi.md#getModelProperties) | **GET** /cam/model/properties | Returns list of all properties used across all models |
| [**getModelPropertyValues**](CamApi.md#getModelPropertyValues) | **GET** /cam/model/property_values | Returns list property-values for all models |
| [**getModelQuery**](CamApi.md#getModelQuery) | **GET** /cam/model/query | Returns list of models matching query |
| [**getPhysicalInteraction**](CamApi.md#getPhysicalInteraction) | **GET** /cam/physical_interaction | Returns list of models |


<a id="getActivityCollection"></a>
# **getActivityCollection**
> getActivityCollection(title, contributor)

Returns list of models

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CamApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    CamApi apiInstance = new CamApi(defaultClient);
    String title = "title_example"; // String | string to search for in title of model
    String contributor = "contributor_example"; // String | string to search for in contributor of model
    try {
      apiInstance.getActivityCollection(title, contributor);
    } catch (ApiException e) {
      System.err.println("Exception when calling CamApi#getActivityCollection");
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
| **title** | **String**| string to search for in title of model | [optional] |
| **contributor** | **String**| string to search for in contributor of model | [optional] |

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
| **200** | Success |  -  |

<a id="getInstanceObject"></a>
# **getInstanceObject**
> List&lt;Association&gt; getInstanceObject(id, title, contributor)

Returns list of matches

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CamApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    CamApi apiInstance = new CamApi(defaultClient);
    String id = "id_example"; // String | 
    String title = "title_example"; // String | string to search for in title of model
    String contributor = "contributor_example"; // String | string to search for in contributor of model
    try {
      List<Association> result = apiInstance.getInstanceObject(id, title, contributor);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CamApi#getInstanceObject");
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
| **title** | **String**| string to search for in title of model | [optional] |
| **contributor** | **String**| string to search for in contributor of model | [optional] |

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

<a id="getModelCollection"></a>
# **getModelCollection**
> getModelCollection()

Returns list of ALL models

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CamApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    CamApi apiInstance = new CamApi(defaultClient);
    try {
      apiInstance.getModelCollection();
    } catch (ApiException e) {
      System.err.println("Exception when calling CamApi#getModelCollection");
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
| **200** | Success |  -  |

<a id="getModelContributors"></a>
# **getModelContributors**
> getModelContributors()

Returns list of all contributors across all models

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CamApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    CamApi apiInstance = new CamApi(defaultClient);
    try {
      apiInstance.getModelContributors();
    } catch (ApiException e) {
      System.err.println("Exception when calling CamApi#getModelContributors");
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
| **200** | Success |  -  |

<a id="getModelInstances"></a>
# **getModelInstances**
> getModelInstances()

Returns list of all instances

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CamApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    CamApi apiInstance = new CamApi(defaultClient);
    try {
      apiInstance.getModelInstances();
    } catch (ApiException e) {
      System.err.println("Exception when calling CamApi#getModelInstances");
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
| **200** | Success |  -  |

<a id="getModelObject"></a>
# **getModelObject**
> getModelObject(id)

Returns a complete model

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CamApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    CamApi apiInstance = new CamApi(defaultClient);
    String id = "id_example"; // String | 
    try {
      apiInstance.getModelObject(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling CamApi#getModelObject");
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
| **200** | Success |  -  |

<a id="getModelProperties"></a>
# **getModelProperties**
> getModelProperties(title, contributor)

Returns list of all properties used across all models

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CamApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    CamApi apiInstance = new CamApi(defaultClient);
    String title = "title_example"; // String | string to search for in title of model
    String contributor = "contributor_example"; // String | string to search for in contributor of model
    try {
      apiInstance.getModelProperties(title, contributor);
    } catch (ApiException e) {
      System.err.println("Exception when calling CamApi#getModelProperties");
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
| **title** | **String**| string to search for in title of model | [optional] |
| **contributor** | **String**| string to search for in contributor of model | [optional] |

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
| **200** | Success |  -  |

<a id="getModelPropertyValues"></a>
# **getModelPropertyValues**
> getModelPropertyValues(title, contributor)

Returns list property-values for all models

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CamApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    CamApi apiInstance = new CamApi(defaultClient);
    String title = "title_example"; // String | string to search for in title of model
    String contributor = "contributor_example"; // String | string to search for in contributor of model
    try {
      apiInstance.getModelPropertyValues(title, contributor);
    } catch (ApiException e) {
      System.err.println("Exception when calling CamApi#getModelPropertyValues");
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
| **title** | **String**| string to search for in title of model | [optional] |
| **contributor** | **String**| string to search for in contributor of model | [optional] |

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
| **200** | Success |  -  |

<a id="getModelQuery"></a>
# **getModelQuery**
> getModelQuery(title, contributor)

Returns list of models matching query

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CamApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    CamApi apiInstance = new CamApi(defaultClient);
    String title = "title_example"; // String | string to search for in title of model
    String contributor = "contributor_example"; // String | string to search for in contributor of model
    try {
      apiInstance.getModelQuery(title, contributor);
    } catch (ApiException e) {
      System.err.println("Exception when calling CamApi#getModelQuery");
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
| **title** | **String**| string to search for in title of model | [optional] |
| **contributor** | **String**| string to search for in contributor of model | [optional] |

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
| **200** | Success |  -  |

<a id="getPhysicalInteraction"></a>
# **getPhysicalInteraction**
> getPhysicalInteraction(title, contributor)

Returns list of models

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CamApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    CamApi apiInstance = new CamApi(defaultClient);
    String title = "title_example"; // String | string to search for in title of model
    String contributor = "contributor_example"; // String | string to search for in contributor of model
    try {
      apiInstance.getPhysicalInteraction(title, contributor);
    } catch (ApiException e) {
      System.err.println("Exception when calling CamApi#getPhysicalInteraction");
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
| **title** | **String**| string to search for in title of model | [optional] |
| **contributor** | **String**| string to search for in contributor of model | [optional] |

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
| **200** | Success |  -  |

