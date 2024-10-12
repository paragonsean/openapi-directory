# ActionBatchesApi

All URIs are relative to *https://api.meraki.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createOrganizationActionBatch_1**](ActionBatchesApi.md#createOrganizationActionBatch_1) | **POST** /organizations/{organizationId}/actionBatches | Create an action batch |
| [**deleteOrganizationActionBatch_1**](ActionBatchesApi.md#deleteOrganizationActionBatch_1) | **DELETE** /organizations/{organizationId}/actionBatches/{actionBatchId} | Delete an action batch |
| [**getOrganizationActionBatch_1**](ActionBatchesApi.md#getOrganizationActionBatch_1) | **GET** /organizations/{organizationId}/actionBatches/{actionBatchId} | Return an action batch |
| [**getOrganizationActionBatches_1**](ActionBatchesApi.md#getOrganizationActionBatches_1) | **GET** /organizations/{organizationId}/actionBatches | Return the list of action batches in the organization |
| [**updateOrganizationActionBatch_1**](ActionBatchesApi.md#updateOrganizationActionBatch_1) | **PUT** /organizations/{organizationId}/actionBatches/{actionBatchId} | Update an action batch |


<a id="createOrganizationActionBatch_1"></a>
# **createOrganizationActionBatch_1**
> CreateOrganizationActionBatch201Response createOrganizationActionBatch_1(organizationId, createOrganizationActionBatchRequest)

Create an action batch

Create an action batch

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActionBatchesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    ActionBatchesApi apiInstance = new ActionBatchesApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    CreateOrganizationActionBatchRequest createOrganizationActionBatchRequest = new CreateOrganizationActionBatchRequest(); // CreateOrganizationActionBatchRequest | 
    try {
      CreateOrganizationActionBatch201Response result = apiInstance.createOrganizationActionBatch_1(organizationId, createOrganizationActionBatchRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActionBatchesApi#createOrganizationActionBatch_1");
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
| **organizationId** | **String**|  | |
| **createOrganizationActionBatchRequest** | [**CreateOrganizationActionBatchRequest**](CreateOrganizationActionBatchRequest.md)|  | |

### Return type

[**CreateOrganizationActionBatch201Response**](CreateOrganizationActionBatch201Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Successful operation |  -  |

<a id="deleteOrganizationActionBatch_1"></a>
# **deleteOrganizationActionBatch_1**
> deleteOrganizationActionBatch_1(organizationId, actionBatchId)

Delete an action batch

Delete an action batch

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActionBatchesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    ActionBatchesApi apiInstance = new ActionBatchesApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    String actionBatchId = "actionBatchId_example"; // String | 
    try {
      apiInstance.deleteOrganizationActionBatch_1(organizationId, actionBatchId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActionBatchesApi#deleteOrganizationActionBatch_1");
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
| **organizationId** | **String**|  | |
| **actionBatchId** | **String**|  | |

### Return type

null (empty response body)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Successful operation |  -  |

<a id="getOrganizationActionBatch_1"></a>
# **getOrganizationActionBatch_1**
> CreateOrganizationActionBatch201Response getOrganizationActionBatch_1(organizationId, actionBatchId)

Return an action batch

Return an action batch

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActionBatchesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    ActionBatchesApi apiInstance = new ActionBatchesApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    String actionBatchId = "actionBatchId_example"; // String | 
    try {
      CreateOrganizationActionBatch201Response result = apiInstance.getOrganizationActionBatch_1(organizationId, actionBatchId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActionBatchesApi#getOrganizationActionBatch_1");
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
| **organizationId** | **String**|  | |
| **actionBatchId** | **String**|  | |

### Return type

[**CreateOrganizationActionBatch201Response**](CreateOrganizationActionBatch201Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getOrganizationActionBatches_1"></a>
# **getOrganizationActionBatches_1**
> List&lt;Object&gt; getOrganizationActionBatches_1(organizationId, status)

Return the list of action batches in the organization

Return the list of action batches in the organization

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActionBatchesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    ActionBatchesApi apiInstance = new ActionBatchesApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    String status = "completed"; // String | Filter batches by status. Valid types are pending, completed, and failed.
    try {
      List<Object> result = apiInstance.getOrganizationActionBatches_1(organizationId, status);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActionBatchesApi#getOrganizationActionBatches_1");
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
| **organizationId** | **String**|  | |
| **status** | **String**| Filter batches by status. Valid types are pending, completed, and failed. | [optional] [enum: completed, failed, pending] |

### Return type

**List&lt;Object&gt;**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="updateOrganizationActionBatch_1"></a>
# **updateOrganizationActionBatch_1**
> Object updateOrganizationActionBatch_1(organizationId, actionBatchId, updateOrganizationActionBatchRequest)

Update an action batch

Update an action batch

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActionBatchesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    ActionBatchesApi apiInstance = new ActionBatchesApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    String actionBatchId = "actionBatchId_example"; // String | 
    UpdateOrganizationActionBatchRequest updateOrganizationActionBatchRequest = new UpdateOrganizationActionBatchRequest(); // UpdateOrganizationActionBatchRequest | 
    try {
      Object result = apiInstance.updateOrganizationActionBatch_1(organizationId, actionBatchId, updateOrganizationActionBatchRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActionBatchesApi#updateOrganizationActionBatch_1");
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
| **organizationId** | **String**|  | |
| **actionBatchId** | **String**|  | |
| **updateOrganizationActionBatchRequest** | [**UpdateOrganizationActionBatchRequest**](UpdateOrganizationActionBatchRequest.md)|  | [optional] |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

