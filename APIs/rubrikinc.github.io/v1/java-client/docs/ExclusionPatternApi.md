# ExclusionPatternApi

All URIs are relative to */api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**bulkCreateExclusionPattern**](ExclusionPatternApi.md#bulkCreateExclusionPattern) | **POST** /exclusion_pattern/bulk | Bulk create exclusion patterns |
| [**bulkDeleteExclusionPattern**](ExclusionPatternApi.md#bulkDeleteExclusionPattern) | **DELETE** /exclusion_pattern/bulk | Bulk delete the provided mutable exclusion patterns |
| [**createExclusionPattern**](ExclusionPatternApi.md#createExclusionPattern) | **POST** /exclusion_pattern | Create an exclusion pattern |
| [**deleteExclusionPattern**](ExclusionPatternApi.md#deleteExclusionPattern) | **DELETE** /exclusion_pattern/{id} | Delete a mutable exclusion pattern |
| [**getExclusionPattern**](ExclusionPatternApi.md#getExclusionPattern) | **GET** /exclusion_pattern/{id} | Get details of a exclusion pattern |
| [**queryExclusionPattern**](ExclusionPatternApi.md#queryExclusionPattern) | **GET** /exclusion_pattern | Get a summary of all exclusion patterns |
| [**updateExclusionPattern**](ExclusionPatternApi.md#updateExclusionPattern) | **POST** /exclusion_pattern/{id} | Update a mutable exclusion pattern |


<a id="bulkCreateExclusionPattern"></a>
# **bulkCreateExclusionPattern**
> ExclusionPatternDetailList bulkCreateExclusionPattern(exclusionPatternCreateConfig)

Bulk create exclusion patterns

Bulk create exclusion patterns.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExclusionPatternApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    ExclusionPatternApi apiInstance = new ExclusionPatternApi(defaultClient);
    List<ExclusionPatternCreateConfig> exclusionPatternCreateConfig = Arrays.asList(); // List<ExclusionPatternCreateConfig> | Create configuration parameters for a exclusion pattern.
    try {
      ExclusionPatternDetailList result = apiInstance.bulkCreateExclusionPattern(exclusionPatternCreateConfig);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExclusionPatternApi#bulkCreateExclusionPattern");
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
| **exclusionPatternCreateConfig** | [**List&lt;ExclusionPatternCreateConfig&gt;**](ExclusionPatternCreateConfig.md)| Create configuration parameters for a exclusion pattern. | |

### Return type

[**ExclusionPatternDetailList**](ExclusionPatternDetailList.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Details of new exclusion patterns. |  -  |
| **404** | Failed to create exclusion pattern. |  -  |
| **422** | Failed to create exclusion pattern on replication target cluster. |  -  |

<a id="bulkDeleteExclusionPattern"></a>
# **bulkDeleteExclusionPattern**
> bulkDeleteExclusionPattern(ids)

Bulk delete the provided mutable exclusion patterns

Bulk deletes the mutable patterns in a specified set of exclusion patterns.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExclusionPatternApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    ExclusionPatternApi apiInstance = new ExclusionPatternApi(defaultClient);
    List<String> ids = Arrays.asList(); // List<String> | The ID of each exclusion pattern to delete.
    try {
      apiInstance.bulkDeleteExclusionPattern(ids);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExclusionPatternApi#bulkDeleteExclusionPattern");
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
| **ids** | [**List&lt;String&gt;**](String.md)| The ID of each exclusion pattern to delete. | |

### Return type

null (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Successfully deleted all the specified exclusion patterns. |  -  |
| **404** | The exclusion pattern deletion failed for at least one exclusion pattern. |  -  |

<a id="createExclusionPattern"></a>
# **createExclusionPattern**
> ExclusionPatternDetail createExclusionPattern(exclusionPatternCreateConfig)

Create an exclusion pattern

Create a exclusion pattern.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExclusionPatternApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    ExclusionPatternApi apiInstance = new ExclusionPatternApi(defaultClient);
    ExclusionPatternCreateConfig exclusionPatternCreateConfig = new ExclusionPatternCreateConfig(); // ExclusionPatternCreateConfig | Create configuration parameters for a exclusion pattern.
    try {
      ExclusionPatternDetail result = apiInstance.createExclusionPattern(exclusionPatternCreateConfig);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExclusionPatternApi#createExclusionPattern");
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
| **exclusionPatternCreateConfig** | [**ExclusionPatternCreateConfig**](ExclusionPatternCreateConfig.md)| Create configuration parameters for a exclusion pattern. | |

### Return type

[**ExclusionPatternDetail**](ExclusionPatternDetail.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Details of the new exclusion pattern. |  -  |
| **404** | Failed to create exclusion pattern. |  -  |
| **422** | Failed to create exclusion pattern on replication target cluster. |  -  |

<a id="deleteExclusionPattern"></a>
# **deleteExclusionPattern**
> deleteExclusionPattern(id)

Delete a mutable exclusion pattern

Deletes an exclusion pattern if that pattern is mutable.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExclusionPatternApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    ExclusionPatternApi apiInstance = new ExclusionPatternApi(defaultClient);
    String id = "id_example"; // String | ID of the exclusion pattern.
    try {
      apiInstance.deleteExclusionPattern(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExclusionPatternApi#deleteExclusionPattern");
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
| **id** | **String**| ID of the exclusion pattern. | |

### Return type

null (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Successfully deleted the specified exclusion pattern. |  -  |
| **403** | Failed to delete a immutable exclusion pattern. |  -  |
| **404** | Failed to delete exclusion pattern. |  -  |

<a id="getExclusionPattern"></a>
# **getExclusionPattern**
> ExclusionPatternDetail getExclusionPattern(id)

Get details of a exclusion pattern

Get details of a exclusion pattern.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExclusionPatternApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    ExclusionPatternApi apiInstance = new ExclusionPatternApi(defaultClient);
    String id = "id_example"; // String | ID of the exclusion pattern.
    try {
      ExclusionPatternDetail result = apiInstance.getExclusionPattern(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExclusionPatternApi#getExclusionPattern");
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
| **id** | **String**| ID of the exclusion pattern. | |

### Return type

[**ExclusionPatternDetail**](ExclusionPatternDetail.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Details about the exclusion pattern. |  -  |
| **404** | Failed to get exclusion pattern. |  -  |

<a id="queryExclusionPattern"></a>
# **queryExclusionPattern**
> ExclusionPatternDetailListResponse queryExclusionPattern(pattern, isMutable, sourceId, primaryClusterId, limit, offset, sortBy, sortOrder)

Get a summary of all exclusion patterns

Get a summary of all exclusion patterns.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExclusionPatternApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    ExclusionPatternApi apiInstance = new ExclusionPatternApi(defaultClient);
    String pattern = "pattern_example"; // String | Filter a response by making an infix comparison of the exclusion patttern in the response with the specified value.
    Boolean isMutable = true; // Boolean | Filter a response based on the mutability of the pattern.
    String sourceId = "sourceId_example"; // String | Filter a response based on the protectable object to which the exclusion pattern applies.
    String primaryClusterId = "primaryClusterId_example"; // String | Limit a response to the results that have the specified primary cluster value.
    Integer limit = 56; // Integer | Limit the summary information to a specified maximum number of matches. Optionally, use with offset to start the count at a specified point. Optionally, use with sort_by to perform sort on given attributes. Include sort_order to determine the ascending or descending direction of the sort.
    Integer offset = 56; // Integer | Starting position in the list of matches. The response includes the specified numbered entry and all higher numbered entries. Use with limit to retrieve the response as smaller groups of entries, for example for paging of results.
    String sortBy = "pattern"; // String | Specifies a comma-separated list of attributes to use in sorting the matches. Performs an ASCII sort of the values in the response using each specified attribute, in the order specified.
    String sortOrder = "asc"; // String | Sort order, either ascending or descending.
    try {
      ExclusionPatternDetailListResponse result = apiInstance.queryExclusionPattern(pattern, isMutable, sourceId, primaryClusterId, limit, offset, sortBy, sortOrder);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExclusionPatternApi#queryExclusionPattern");
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
| **pattern** | **String**| Filter a response by making an infix comparison of the exclusion patttern in the response with the specified value. | [optional] |
| **isMutable** | **Boolean**| Filter a response based on the mutability of the pattern. | [optional] |
| **sourceId** | **String**| Filter a response based on the protectable object to which the exclusion pattern applies. | [optional] |
| **primaryClusterId** | **String**| Limit a response to the results that have the specified primary cluster value. | [optional] |
| **limit** | **Integer**| Limit the summary information to a specified maximum number of matches. Optionally, use with offset to start the count at a specified point. Optionally, use with sort_by to perform sort on given attributes. Include sort_order to determine the ascending or descending direction of the sort. | [optional] |
| **offset** | **Integer**| Starting position in the list of matches. The response includes the specified numbered entry and all higher numbered entries. Use with limit to retrieve the response as smaller groups of entries, for example for paging of results. | [optional] |
| **sortBy** | **String**| Specifies a comma-separated list of attributes to use in sorting the matches. Performs an ASCII sort of the values in the response using each specified attribute, in the order specified. | [optional] [enum: pattern] |
| **sortOrder** | **String**| Sort order, either ascending or descending. | [optional] [default to asc] [enum: asc, desc] |

### Return type

[**ExclusionPatternDetailListResponse**](ExclusionPatternDetailListResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful query results for exclusion pattern. |  -  |

<a id="updateExclusionPattern"></a>
# **updateExclusionPattern**
> ExclusionPatternDetail updateExclusionPattern(id, exclusionPatternUpdateConfig)

Update a mutable exclusion pattern

Update mutable exclusion pattern with specified properties. The exclusion pattern which is mutable can be modified.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExclusionPatternApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    ExclusionPatternApi apiInstance = new ExclusionPatternApi(defaultClient);
    String id = "id_example"; // String | ID of exclusion pattern.
    ExclusionPatternUpdateConfig exclusionPatternUpdateConfig = new ExclusionPatternUpdateConfig(); // ExclusionPatternUpdateConfig | Properties to update.
    try {
      ExclusionPatternDetail result = apiInstance.updateExclusionPattern(id, exclusionPatternUpdateConfig);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExclusionPatternApi#updateExclusionPattern");
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
| **id** | **String**| ID of exclusion pattern. | |
| **exclusionPatternUpdateConfig** | [**ExclusionPatternUpdateConfig**](ExclusionPatternUpdateConfig.md)| Properties to update. | |

### Return type

[**ExclusionPatternDetail**](ExclusionPatternDetail.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Return details about the exclusion pattern. |  -  |
| **403** | Failed to update a immutable exclusion pattern. |  -  |
| **404** | Failed to update exclusion pattern. |  -  |

