# ReimbursementApi

All URIs are relative to */v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createReimbursement**](ReimbursementApi.md#createReimbursement) | **POST** /reimbursement/{projectId} | Create Reimbursement |
| [**updateReimbursement**](ReimbursementApi.md#updateReimbursement) | **PATCH** /reimbursement/{projectId} | Update Reimbursement |


<a id="createReimbursement"></a>
# **createReimbursement**
> createReimbursement(projectId, body)

Create Reimbursement

Create a new Reimbursement policy

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReimbursementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/v1");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    ReimbursementApi apiInstance = new ReimbursementApi(defaultClient);
    String projectId = "projectId_example"; // String | 
    CreateReimbursementRequest body = new CreateReimbursementRequest(); // CreateReimbursementRequest | 
    try {
      apiInstance.createReimbursement(projectId, body);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReimbursementApi#createReimbursement");
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
| **projectId** | **String**|  | |
| **body** | [**CreateReimbursementRequest**](CreateReimbursementRequest.md)|  | |

### Return type

null (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Invalid Request |  -  |
| **401** | Unauthorized |  -  |
| **500** | Server Error |  -  |

<a id="updateReimbursement"></a>
# **updateReimbursement**
> updateReimbursement(projectId, body)

Update Reimbursement

Update an existing Reimbursement policy

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReimbursementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/v1");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    ReimbursementApi apiInstance = new ReimbursementApi(defaultClient);
    String projectId = "projectId_example"; // String | 
    PolicyUpdateInput body = new PolicyUpdateInput(); // PolicyUpdateInput | 
    try {
      apiInstance.updateReimbursement(projectId, body);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReimbursementApi#updateReimbursement");
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
| **projectId** | **String**|  | |
| **body** | [**PolicyUpdateInput**](PolicyUpdateInput.md)|  | |

### Return type

null (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Invalid Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |
| **500** | Server Error |  -  |

