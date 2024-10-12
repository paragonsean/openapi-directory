# ReferenceApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiReferenceAnsweringBodiesGet**](ReferenceApi.md#apiReferenceAnsweringBodiesGet) | **GET** /api/Reference/AnsweringBodies | Returns a list of answering bodies. |
| [**apiReferenceDepartmentsGet**](ReferenceApi.md#apiReferenceDepartmentsGet) | **GET** /api/Reference/Departments | Returns a list of departments. |
| [**apiReferenceDepartmentsIdLogoGet**](ReferenceApi.md#apiReferenceDepartmentsIdLogoGet) | **GET** /api/Reference/Departments/{id}/Logo | Returns department logo. |
| [**apiReferencePolicyInterestsGet**](ReferenceApi.md#apiReferencePolicyInterestsGet) | **GET** /api/Reference/PolicyInterests | Returns a list of policy interest. |


<a id="apiReferenceAnsweringBodiesGet"></a>
# **apiReferenceAnsweringBodiesGet**
> List&lt;AnsweringBody&gt; apiReferenceAnsweringBodiesGet(id, nameContains)

Returns a list of answering bodies.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReferenceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    ReferenceApi apiInstance = new ReferenceApi(defaultClient);
    Integer id = 56; // Integer | 
    String nameContains = "nameContains_example"; // String | 
    try {
      List<AnsweringBody> result = apiInstance.apiReferenceAnsweringBodiesGet(id, nameContains);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReferenceApi#apiReferenceAnsweringBodiesGet");
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
| **id** | **Integer**|  | [optional] |
| **nameContains** | **String**|  | [optional] |

### Return type

[**List&lt;AnsweringBody&gt;**](AnsweringBody.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |

<a id="apiReferenceDepartmentsGet"></a>
# **apiReferenceDepartmentsGet**
> List&lt;GovernmentDepartment&gt; apiReferenceDepartmentsGet(id, nameContains)

Returns a list of departments.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReferenceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    ReferenceApi apiInstance = new ReferenceApi(defaultClient);
    Integer id = 56; // Integer | 
    String nameContains = "nameContains_example"; // String | 
    try {
      List<GovernmentDepartment> result = apiInstance.apiReferenceDepartmentsGet(id, nameContains);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReferenceApi#apiReferenceDepartmentsGet");
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
| **id** | **Integer**|  | [optional] |
| **nameContains** | **String**|  | [optional] |

### Return type

[**List&lt;GovernmentDepartment&gt;**](GovernmentDepartment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |

<a id="apiReferenceDepartmentsIdLogoGet"></a>
# **apiReferenceDepartmentsIdLogoGet**
> apiReferenceDepartmentsIdLogoGet(id)

Returns department logo.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReferenceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    ReferenceApi apiInstance = new ReferenceApi(defaultClient);
    Integer id = 56; // Integer | Logo by department ID
    try {
      apiInstance.apiReferenceDepartmentsIdLogoGet(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReferenceApi#apiReferenceDepartmentsIdLogoGet");
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
| **id** | **Integer**| Logo by department ID | |

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
| **400** | Bad Request |  -  |
| **404** | Not Found |  -  |

<a id="apiReferencePolicyInterestsGet"></a>
# **apiReferencePolicyInterestsGet**
> List&lt;GenericReferenceData&gt; apiReferencePolicyInterestsGet()

Returns a list of policy interest.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReferenceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    ReferenceApi apiInstance = new ReferenceApi(defaultClient);
    try {
      List<GenericReferenceData> result = apiInstance.apiReferencePolicyInterestsGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReferenceApi#apiReferencePolicyInterestsGet");
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

[**List&lt;GenericReferenceData&gt;**](GenericReferenceData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

