# WorkflowsApi

All URIs are relative to *https://api.mailscript.com/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addWorkflow**](WorkflowsApi.md#addWorkflow) | **POST** /workflows | Setup workflow |
| [**deleteWorkflow**](WorkflowsApi.md#deleteWorkflow) | **DELETE** /workflows/{workflow} | Delete a workflow |
| [**getAllWorkflows**](WorkflowsApi.md#getAllWorkflows) | **GET** /workflows | Get all workflows you have access to |
| [**setWorkflow**](WorkflowsApi.md#setWorkflow) | **POST** /workflows/set | Set a property on a workflow |
| [**updateWorkflow**](WorkflowsApi.md#updateWorkflow) | **PUT** /workflows/{workflow} | Update an workflow |


<a id="addWorkflow"></a>
# **addWorkflow**
> addWorkflow(addWorkflowRequest)

Setup workflow



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WorkflowsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.mailscript.com/v2");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    WorkflowsApi apiInstance = new WorkflowsApi(defaultClient);
    AddWorkflowRequest addWorkflowRequest = new AddWorkflowRequest(); // AddWorkflowRequest | Workflow body
    try {
      apiInstance.addWorkflow(addWorkflowRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling WorkflowsApi#addWorkflow");
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
| **addWorkflowRequest** | [**AddWorkflowRequest**](AddWorkflowRequest.md)| Workflow body | |

### Return type

null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | successful operation |  -  |
| **400** | Internal error |  -  |
| **403** | Bad credentials |  -  |
| **405** | Invalid input |  -  |

<a id="deleteWorkflow"></a>
# **deleteWorkflow**
> deleteWorkflow(workflow)

Delete a workflow

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WorkflowsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.mailscript.com/v2");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    WorkflowsApi apiInstance = new WorkflowsApi(defaultClient);
    String workflow = "workflow_example"; // String | ID of the workflow
    try {
      apiInstance.deleteWorkflow(workflow);
    } catch (ApiException e) {
      System.err.println("Exception when calling WorkflowsApi#deleteWorkflow");
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
| **workflow** | **String**| ID of the workflow | |

### Return type

null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Successful delete operation |  -  |
| **400** | Failure |  -  |
| **403** | Bad credentials |  -  |
| **404** | Key not found |  -  |

<a id="getAllWorkflows"></a>
# **getAllWorkflows**
> GetAllWorkflowsResponse getAllWorkflows()

Get all workflows you have access to



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WorkflowsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.mailscript.com/v2");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    WorkflowsApi apiInstance = new WorkflowsApi(defaultClient);
    try {
      GetAllWorkflowsResponse result = apiInstance.getAllWorkflows();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WorkflowsApi#getAllWorkflows");
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

[**GetAllWorkflowsResponse**](GetAllWorkflowsResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **403** | Bad credentials |  -  |
| **405** | Invalid input |  -  |

<a id="setWorkflow"></a>
# **setWorkflow**
> setWorkflow(setWorkflowRequest)

Set a property on a workflow

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WorkflowsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.mailscript.com/v2");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    WorkflowsApi apiInstance = new WorkflowsApi(defaultClient);
    SetWorkflowRequest setWorkflowRequest = new SetWorkflowRequest(); // SetWorkflowRequest | Set Workflow body
    try {
      apiInstance.setWorkflow(setWorkflowRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling WorkflowsApi#setWorkflow");
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
| **setWorkflowRequest** | [**SetWorkflowRequest**](SetWorkflowRequest.md)| Set Workflow body | |

### Return type

null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Successful update operation |  -  |
| **400** | Failure |  -  |
| **403** | Bad credentials |  -  |
| **404** | Key not found |  -  |

<a id="updateWorkflow"></a>
# **updateWorkflow**
> updateWorkflow(workflow, addWorkflowRequest)

Update an workflow

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WorkflowsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.mailscript.com/v2");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    WorkflowsApi apiInstance = new WorkflowsApi(defaultClient);
    String workflow = "workflow_example"; // String | ID of the workflow
    AddWorkflowRequest addWorkflowRequest = new AddWorkflowRequest(); // AddWorkflowRequest | Workflow body
    try {
      apiInstance.updateWorkflow(workflow, addWorkflowRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling WorkflowsApi#updateWorkflow");
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
| **workflow** | **String**| ID of the workflow | |
| **addWorkflowRequest** | [**AddWorkflowRequest**](AddWorkflowRequest.md)| Workflow body | |

### Return type

null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful update operation |  -  |
| **400** | Failure |  -  |
| **403** | Bad credentials |  -  |
| **404** | Key not found |  -  |

