# TaxonomyApi

All URIs are relative to *https://api.semantria.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addTaxonomy**](TaxonomyApi.md#addTaxonomy) | **POST** /taxonomy.{content_type} | Add taxonomy nodes |
| [**deleteTaxonomy**](TaxonomyApi.md#deleteTaxonomy) | **DELETE** /taxonomy.{content_type} | Remove taxonomy nodes |
| [**getTaxonomy**](TaxonomyApi.md#getTaxonomy) | **GET** /taxonomy.{content_type} | Retrieve taxonomy |
| [**updateTaxonomy**](TaxonomyApi.md#updateTaxonomy) | **PUT** /taxonomy.{content_type} | Update taxonomy nodes |


<a id="addTaxonomy"></a>
# **addTaxonomy**
> List&lt;TaxonomyNodeResponseVersion&gt; addTaxonomy(contentType, taxonomy, configId)

Add taxonomy nodes

This method adds taxonomy nodes on Semantria side.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TaxonomyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.semantria.com");

    TaxonomyApi apiInstance = new TaxonomyApi(defaultClient);
    String contentType = "contentType_example"; // String | 
    Object taxonomy = null; // Object | List of parametrized JSON or XML objects.
    String configId = "configId_example"; // String | Identifier of configuration queries linked to.
    try {
      List<TaxonomyNodeResponseVersion> result = apiInstance.addTaxonomy(contentType, taxonomy, configId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TaxonomyApi#addTaxonomy");
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
| **contentType** | **String**|  | |
| **taxonomy** | **Object**| List of parametrized JSON or XML objects. | |
| **configId** | **String**| Identifier of configuration queries linked to. | [optional] |

### Return type

[**List&lt;TaxonomyNodeResponseVersion&gt;**](TaxonomyNodeResponseVersion.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |
| **202** | Client request accepted and queued. |  -  |
| **400** | Incoming request body is incorrect. Server responds with details. |  -  |
| **401** | Authentication failed. |  -  |
| **402** | Unauthorized. Limit of system calls is reached or subscription is expired. |  -  |
| **406** | Number of allowed queries per configuration achieved. |  -  |
| **500** | Server side issue. Server may respond with the details in response body. |  -  |

<a id="deleteTaxonomy"></a>
# **deleteTaxonomy**
> deleteTaxonomy(contentType, taxonomyNodeIDs, configId)

Remove taxonomy nodes

This method removes certain taxonomy nodes by their IDs on Semantria side.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TaxonomyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.semantria.com");

    TaxonomyApi apiInstance = new TaxonomyApi(defaultClient);
    String contentType = "contentType_example"; // String | 
    List<String> taxonomyNodeIDs = Arrays.asList(); // List<String> | List of taxonomy node identifiers.
    String configId = "configId_example"; // String | Identifier of configuration queries linked to.
    try {
      apiInstance.deleteTaxonomy(contentType, taxonomyNodeIDs, configId);
    } catch (ApiException e) {
      System.err.println("Exception when calling TaxonomyApi#deleteTaxonomy");
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
| **contentType** | **String**|  | |
| **taxonomyNodeIDs** | [**List&lt;String&gt;**](String.md)| List of taxonomy node identifiers. | |
| **configId** | **String**| Identifier of configuration queries linked to. | [optional] |

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
| **202** | Client request accepted and queued. |  -  |
| **400** | Incoming request body is incorrect. Server responds with details. |  -  |
| **401** | Authentication failed. |  -  |
| **402** | Unauthorized. Limit of system calls is reached or subscription is expired. |  -  |
| **403** | Forbidden. Server responds if client tries to remove primary configuration. |  -  |
| **500** | Server side issue. Server may respond with the details in response body. |  -  |

<a id="getTaxonomy"></a>
# **getTaxonomy**
> List&lt;TaxonomyNodeResponseVersion&gt; getTaxonomy(contentType, configId)

Retrieve taxonomy

This method retrieves list of taxonomy available on Semantria side.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TaxonomyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.semantria.com");

    TaxonomyApi apiInstance = new TaxonomyApi(defaultClient);
    String contentType = "contentType_example"; // String | 
    String configId = "configId_example"; // String | Identifier of configuration taxonomy linked to.
    try {
      List<TaxonomyNodeResponseVersion> result = apiInstance.getTaxonomy(contentType, configId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TaxonomyApi#getTaxonomy");
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
| **contentType** | **String**|  | |
| **configId** | **String**| Identifier of configuration taxonomy linked to. | [optional] |

### Return type

[**List&lt;TaxonomyNodeResponseVersion&gt;**](TaxonomyNodeResponseVersion.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Client request accepted and queued. Server responds with the taxonomy list. |  -  |
| **202** | Client request accepted and no taxonomy found. Server responds with empty body. |  -  |
| **401** | Authentication failed. |  -  |
| **402** | Unauthorized. Limit of system calls is reached or subscription is expired. |  -  |
| **500** | Server side issue. Server may respond with the details in response body. |  -  |

<a id="updateTaxonomy"></a>
# **updateTaxonomy**
> List&lt;TaxonomyNodeResponseVersion&gt; updateTaxonomy(contentType, taxonomy, configId)

Update taxonomy nodes

This method updates taxonomy nodes on Semantria side.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TaxonomyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.semantria.com");

    TaxonomyApi apiInstance = new TaxonomyApi(defaultClient);
    String contentType = "contentType_example"; // String | 
    Object taxonomy = null; // Object | List of parametrized JSON or XML objects.
    String configId = "configId_example"; // String | Identifier of configuration queries linked to.
    try {
      List<TaxonomyNodeResponseVersion> result = apiInstance.updateTaxonomy(contentType, taxonomy, configId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TaxonomyApi#updateTaxonomy");
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
| **contentType** | **String**|  | |
| **taxonomy** | **Object**| List of parametrized JSON or XML objects. | |
| **configId** | **String**| Identifier of configuration queries linked to. | [optional] |

### Return type

[**List&lt;TaxonomyNodeResponseVersion&gt;**](TaxonomyNodeResponseVersion.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |
| **202** | Client request accepted and queued. |  -  |
| **400** | Incoming request body is incorrect. Server responds with details. |  -  |
| **401** | Authentication failed. |  -  |
| **402** | Unauthorized. Limit of system calls is reached or subscription is expired. |  -  |
| **406** | Number of allowed queries per configuration achieved. |  -  |
| **500** | Server side issue. Server may respond with the details in response body. |  -  |

