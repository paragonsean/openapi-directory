# DeploymentsApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deploymentsCreate**](DeploymentsApi.md#deploymentsCreate) | **POST** /v3/deployments | Create a new deployment. |
| [**deploymentsDelete**](DeploymentsApi.md#deploymentsDelete) | **DELETE** /v3/deployments/{id} | Delete a deployment by its ID. |
| [**deploymentsGet**](DeploymentsApi.md#deploymentsGet) | **GET** /v3/deployments/{id} | Fetch a deployment by its ID. |
| [**deploymentsGetAll**](DeploymentsApi.md#deploymentsGetAll) | **GET** /v3/deployments | Fetch a list of deployments. |


<a id="deploymentsCreate"></a>
# **deploymentsCreate**
> CreateDeploymentResult deploymentsCreate(createDeployment)

Create a new deployment.

Required permission: &#x60;deployments_write&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeploymentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    DeploymentsApi apiInstance = new DeploymentsApi(defaultClient);
    CreateDeployment createDeployment = new CreateDeployment(); // CreateDeployment | The deployment object to create.
    try {
      CreateDeploymentResult result = apiInstance.deploymentsCreate(createDeployment);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeploymentsApi#deploymentsCreate");
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
| **createDeployment** | [**CreateDeployment**](CreateDeployment.md)| The deployment object to create. | [optional] |

### Return type

[**CreateDeploymentResult**](CreateDeploymentResult.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Deployment was created. |  -  |
| **400** | Model not valid. |  -  |
| **401** | API key not valid or no access to resource. |  -  |
| **402** | Tried to call the deployment API without deployment tracking enabled or trial expired. |  -  |
| **404** | Specified log not found. |  -  |
| **429** | A maximum of 500 requests per minute and 3600 requests per hour are permitted |  -  |

<a id="deploymentsDelete"></a>
# **deploymentsDelete**
> deploymentsDelete(id)

Delete a deployment by its ID.

This endpoint doesn&#39;t clear the version number of messages already annotated with this deployment version.&lt;br/&gt;&lt;br/&gt;Required permission: &#x60;deployments_delete&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeploymentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    DeploymentsApi apiInstance = new DeploymentsApi(defaultClient);
    String id = "id_example"; // String | The ID of the deployment to delete.
    try {
      apiInstance.deploymentsDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeploymentsApi#deploymentsDelete");
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
| **id** | **String**| The ID of the deployment to delete. | |

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Deployment was deleted. |  -  |
| **400** | Id not specified. |  -  |
| **401** | API key not valid or no access to resource. |  -  |
| **402** | Tried to call the deployment API without deployment tracking enabled or trial expired. |  -  |
| **404** | Deployment with specified id not found. |  -  |
| **429** | A maximum of 500 requests per minute and 3600 requests per hour are permitted |  -  |

<a id="deploymentsGet"></a>
# **deploymentsGet**
> Deployment deploymentsGet(id)

Fetch a deployment by its ID.

Required permission: &#x60;deployments_read&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeploymentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    DeploymentsApi apiInstance = new DeploymentsApi(defaultClient);
    String id = "id_example"; // String | The ID of the deployment to fetch.
    try {
      Deployment result = apiInstance.deploymentsGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeploymentsApi#deploymentsGet");
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
| **id** | **String**| The ID of the deployment to fetch. | |

### Return type

[**Deployment**](Deployment.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Request for deployment successful. |  -  |
| **400** | Id not specified. |  -  |
| **401** | API key not valid or no access to resource. |  -  |
| **402** | Deployment with specified id not found. |  -  |
| **429** | A maximum of 500 requests per minute and 3600 requests per hour are permitted |  -  |

<a id="deploymentsGetAll"></a>
# **deploymentsGetAll**
> List&lt;Deployment&gt; deploymentsGetAll()

Fetch a list of deployments.

Required permission: &#x60;deployments_read&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeploymentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    DeploymentsApi apiInstance = new DeploymentsApi(defaultClient);
    try {
      List<Deployment> result = apiInstance.deploymentsGetAll();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeploymentsApi#deploymentsGetAll");
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

[**List&lt;Deployment&gt;**](Deployment.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Request for deployments successful. |  -  |
| **401** | API key not valid or no access to resource. |  -  |
| **402** | Tried to call the deployment API without deployment tracking enabled or trial expired. |  -  |
| **429** | A maximum of 500 requests per minute and 3600 requests per hour are permitted |  -  |

