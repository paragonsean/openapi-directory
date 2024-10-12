# OrganizationApi

All URIs are relative to */api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**bulkCreateEnvoys**](OrganizationApi.md#bulkCreateEnvoys) | **POST** /organization/{id}/envoy/bulk | Create a list of Rubrik Envoy objects |
| [**bulkDeleteEnvoys**](OrganizationApi.md#bulkDeleteEnvoys) | **DELETE** /organization/{id}/envoy/bulk | Remove a list of Rubrik Envoy objects |
| [**bulkUpdateEnvoys**](OrganizationApi.md#bulkUpdateEnvoys) | **PATCH** /organization/{id}/envoy/bulk | Update a list of Rubrik Envoy objects |


<a id="bulkCreateEnvoys"></a>
# **bulkCreateEnvoys**
> EnvoyDetailList bulkCreateEnvoys(id, envoyCreate)

Create a list of Rubrik Envoy objects

Create a list of Rubrik Envoy objects for a specified organization and specify the properties to assign to the Rubrik Envoy objects.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganizationApi;

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

    OrganizationApi apiInstance = new OrganizationApi(defaultClient);
    String id = "id_example"; // String | ID assigned to an organization object.
    List<EnvoyCreate> envoyCreate = Arrays.asList(); // List<EnvoyCreate> | Properties to assign to the Rubrik Envoy objects.
    try {
      EnvoyDetailList result = apiInstance.bulkCreateEnvoys(id, envoyCreate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganizationApi#bulkCreateEnvoys");
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
| **id** | **String**| ID assigned to an organization object. | |
| **envoyCreate** | [**List&lt;EnvoyCreate&gt;**](EnvoyCreate.md)| Properties to assign to the Rubrik Envoy objects. | |

### Return type

[**EnvoyDetailList**](EnvoyDetailList.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns a detailed view of all created Rubrik Envoy objects. |  -  |

<a id="bulkDeleteEnvoys"></a>
# **bulkDeleteEnvoys**
> bulkDeleteEnvoys(id, envoyIdList)

Remove a list of Rubrik Envoy objects

Remove a list of Rubrik Envoy objects from an organization and delete the objects from the Rubrik cluster.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganizationApi;

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

    OrganizationApi apiInstance = new OrganizationApi(defaultClient);
    String id = "id_example"; // String | ID assigned to an organization object.
    EnvoyIdList envoyIdList = new EnvoyIdList(); // EnvoyIdList | A list of Rubrik Envoy objects IDs.
    try {
      apiInstance.bulkDeleteEnvoys(id, envoyIdList);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganizationApi#bulkDeleteEnvoys");
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
| **id** | **String**| ID assigned to an organization object. | |
| **envoyIdList** | [**EnvoyIdList**](EnvoyIdList.md)| A list of Rubrik Envoy objects IDs. | |

### Return type

null (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Successfully deleted a list of Rubrik Envoy objects. |  -  |

<a id="bulkUpdateEnvoys"></a>
# **bulkUpdateEnvoys**
> EnvoyDetailList bulkUpdateEnvoys(id, envoyBulkUpdate)

Update a list of Rubrik Envoy objects

Change one or more of the properties of a list of Rubrik Envoy objects.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganizationApi;

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

    OrganizationApi apiInstance = new OrganizationApi(defaultClient);
    String id = "id_example"; // String | ID assigned to an organization object.
    List<EnvoyBulkUpdate> envoyBulkUpdate = Arrays.asList(); // List<EnvoyBulkUpdate> | Properties to assign to the Rubrik Envoy objects.
    try {
      EnvoyDetailList result = apiInstance.bulkUpdateEnvoys(id, envoyBulkUpdate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganizationApi#bulkUpdateEnvoys");
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
| **id** | **String**| ID assigned to an organization object. | |
| **envoyBulkUpdate** | [**List&lt;EnvoyBulkUpdate&gt;**](EnvoyBulkUpdate.md)| Properties to assign to the Rubrik Envoy objects. | |

### Return type

[**EnvoyDetailList**](EnvoyDetailList.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns a detailed view of all updated Rubrik Envoy objects. |  -  |

