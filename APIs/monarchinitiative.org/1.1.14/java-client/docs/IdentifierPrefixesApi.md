# IdentifierPrefixesApi

All URIs are relative to */api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getPrefixCollection**](IdentifierPrefixesApi.md#getPrefixCollection) | **GET** /identifier/prefixes/ | Returns list of prefixes |
| [**getPrefixContract**](IdentifierPrefixesApi.md#getPrefixContract) | **GET** /identifier/prefixes/contract/{uri} | Returns contracted URI |
| [**getPrefixExpand**](IdentifierPrefixesApi.md#getPrefixExpand) | **GET** /identifier/prefixes/expand/{id} | Returns expanded URI |


<a id="getPrefixCollection"></a>
# **getPrefixCollection**
> getPrefixCollection()

Returns list of prefixes

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IdentifierPrefixesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    IdentifierPrefixesApi apiInstance = new IdentifierPrefixesApi(defaultClient);
    try {
      apiInstance.getPrefixCollection();
    } catch (ApiException e) {
      System.err.println("Exception when calling IdentifierPrefixesApi#getPrefixCollection");
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

<a id="getPrefixContract"></a>
# **getPrefixContract**
> getPrefixContract(uri)

Returns contracted URI

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IdentifierPrefixesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    IdentifierPrefixesApi apiInstance = new IdentifierPrefixesApi(defaultClient);
    String uri = "uri_example"; // String | URI of entity to be contracted to identifier/CURIE, e.g \"http://www.informatics.jax.org/accession/MGI:1\"
    try {
      apiInstance.getPrefixContract(uri);
    } catch (ApiException e) {
      System.err.println("Exception when calling IdentifierPrefixesApi#getPrefixContract");
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
| **uri** | **String**| URI of entity to be contracted to identifier/CURIE, e.g \&quot;http://www.informatics.jax.org/accession/MGI:1\&quot; | |

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

<a id="getPrefixExpand"></a>
# **getPrefixExpand**
> getPrefixExpand(id)

Returns expanded URI

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IdentifierPrefixesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    IdentifierPrefixesApi apiInstance = new IdentifierPrefixesApi(defaultClient);
    String id = "id_example"; // String | ID of entity to be contracted to URI, e.g \"MGI:1\"
    try {
      apiInstance.getPrefixExpand(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling IdentifierPrefixesApi#getPrefixExpand");
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
| **id** | **String**| ID of entity to be contracted to URI, e.g \&quot;MGI:1\&quot; | |

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

