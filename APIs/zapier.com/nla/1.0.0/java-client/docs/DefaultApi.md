# DefaultApi

All URIs are relative to *https://nla.zapier.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**check**](DefaultApi.md#check) | **GET** /api/v1/check/ | Check |
| [**executeAppActionEndpoint**](DefaultApi.md#executeAppActionEndpoint) | **POST** /api/v1/exposed/{exposed_app_action_id}/execute/ | Execute App Action Endpoint |
| [**getConfigurationLink**](DefaultApi.md#getConfigurationLink) | **GET** /api/v1/configuration-link/ | Get Configuration Link |
| [**getExecutionLogEndpoint**](DefaultApi.md#getExecutionLogEndpoint) | **GET** /api/v1/execution-log/{execution_log_id}/ | Get Execution Log Endpoint |
| [**listExposedActions**](DefaultApi.md#listExposedActions) | **GET** /api/v1/exposed/ | List Exposed Actions |


<a id="check"></a>
# **check**
> check()

Check

Test that the API and auth are working.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://nla.zapier.com");
    
    // Configure API key authorization: AccessPointApiKeyQuery
    ApiKeyAuth AccessPointApiKeyQuery = (ApiKeyAuth) defaultClient.getAuthentication("AccessPointApiKeyQuery");
    AccessPointApiKeyQuery.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //AccessPointApiKeyQuery.setApiKeyPrefix("Token");

    // Configure API key authorization: SessionAuth
    ApiKeyAuth SessionAuth = (ApiKeyAuth) defaultClient.getAuthentication("SessionAuth");
    SessionAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //SessionAuth.setApiKeyPrefix("Token");

    // Configure API key authorization: AccessPointApiKeyHeader
    ApiKeyAuth AccessPointApiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("AccessPointApiKeyHeader");
    AccessPointApiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //AccessPointApiKeyHeader.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: AccessPointOAuth
    OAuth AccessPointOAuth = (OAuth) defaultClient.getAuthentication("AccessPointOAuth");
    AccessPointOAuth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      apiInstance.check();
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#check");
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

[AccessPointApiKeyQuery](../README.md#AccessPointApiKeyQuery), [SessionAuth](../README.md#SessionAuth), [AccessPointApiKeyHeader](../README.md#AccessPointApiKeyHeader), [AccessPointOAuth](../README.md#AccessPointOAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="executeAppActionEndpoint"></a>
# **executeAppActionEndpoint**
> ExecuteResponse executeAppActionEndpoint(exposedAppActionId, executeRequest)

Execute App Action Endpoint

Give us a plain english description of exact action you want to do. There should be dynamically generated documentation for this endpoint for each action that is exposed.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://nla.zapier.com");
    
    // Configure API key authorization: AccessPointApiKeyQuery
    ApiKeyAuth AccessPointApiKeyQuery = (ApiKeyAuth) defaultClient.getAuthentication("AccessPointApiKeyQuery");
    AccessPointApiKeyQuery.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //AccessPointApiKeyQuery.setApiKeyPrefix("Token");

    // Configure API key authorization: SessionAuth
    ApiKeyAuth SessionAuth = (ApiKeyAuth) defaultClient.getAuthentication("SessionAuth");
    SessionAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //SessionAuth.setApiKeyPrefix("Token");

    // Configure API key authorization: AccessPointApiKeyHeader
    ApiKeyAuth AccessPointApiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("AccessPointApiKeyHeader");
    AccessPointApiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //AccessPointApiKeyHeader.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: AccessPointOAuth
    OAuth AccessPointOAuth = (OAuth) defaultClient.getAuthentication("AccessPointOAuth");
    AccessPointOAuth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String exposedAppActionId = "exposedAppActionId_example"; // String | 
    ExecuteRequest executeRequest = new ExecuteRequest(); // ExecuteRequest | 
    try {
      ExecuteResponse result = apiInstance.executeAppActionEndpoint(exposedAppActionId, executeRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#executeAppActionEndpoint");
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
| **exposedAppActionId** | **String**|  | |
| **executeRequest** | [**ExecuteRequest**](ExecuteRequest.md)|  | |

### Return type

[**ExecuteResponse**](ExecuteResponse.md)

### Authorization

[AccessPointApiKeyQuery](../README.md#AccessPointApiKeyQuery), [SessionAuth](../README.md#SessionAuth), [AccessPointApiKeyHeader](../README.md#AccessPointApiKeyHeader), [AccessPointOAuth](../README.md#AccessPointOAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |

<a id="getConfigurationLink"></a>
# **getConfigurationLink**
> getConfigurationLink()

Get Configuration Link

Provides a link to configure more actions. Alternatively, searching through apps and actions will provide more specific configuration links.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://nla.zapier.com");
    
    // Configure API key authorization: AccessPointApiKeyQuery
    ApiKeyAuth AccessPointApiKeyQuery = (ApiKeyAuth) defaultClient.getAuthentication("AccessPointApiKeyQuery");
    AccessPointApiKeyQuery.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //AccessPointApiKeyQuery.setApiKeyPrefix("Token");

    // Configure API key authorization: SessionAuth
    ApiKeyAuth SessionAuth = (ApiKeyAuth) defaultClient.getAuthentication("SessionAuth");
    SessionAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //SessionAuth.setApiKeyPrefix("Token");

    // Configure API key authorization: AccessPointApiKeyHeader
    ApiKeyAuth AccessPointApiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("AccessPointApiKeyHeader");
    AccessPointApiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //AccessPointApiKeyHeader.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: AccessPointOAuth
    OAuth AccessPointOAuth = (OAuth) defaultClient.getAuthentication("AccessPointOAuth");
    AccessPointOAuth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      apiInstance.getConfigurationLink();
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getConfigurationLink");
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

[AccessPointApiKeyQuery](../README.md#AccessPointApiKeyQuery), [SessionAuth](../README.md#SessionAuth), [AccessPointApiKeyHeader](../README.md#AccessPointApiKeyHeader), [AccessPointOAuth](../README.md#AccessPointOAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="getExecutionLogEndpoint"></a>
# **getExecutionLogEndpoint**
> ExecuteResponse getExecutionLogEndpoint(executionLogId)

Get Execution Log Endpoint

Get the execution log for a given execution log id.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://nla.zapier.com");
    
    // Configure API key authorization: AccessPointApiKeyQuery
    ApiKeyAuth AccessPointApiKeyQuery = (ApiKeyAuth) defaultClient.getAuthentication("AccessPointApiKeyQuery");
    AccessPointApiKeyQuery.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //AccessPointApiKeyQuery.setApiKeyPrefix("Token");

    // Configure API key authorization: SessionAuth
    ApiKeyAuth SessionAuth = (ApiKeyAuth) defaultClient.getAuthentication("SessionAuth");
    SessionAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //SessionAuth.setApiKeyPrefix("Token");

    // Configure API key authorization: AccessPointApiKeyHeader
    ApiKeyAuth AccessPointApiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("AccessPointApiKeyHeader");
    AccessPointApiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //AccessPointApiKeyHeader.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: AccessPointOAuth
    OAuth AccessPointOAuth = (OAuth) defaultClient.getAuthentication("AccessPointOAuth");
    AccessPointOAuth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String executionLogId = "executionLogId_example"; // String | 
    try {
      ExecuteResponse result = apiInstance.getExecutionLogEndpoint(executionLogId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getExecutionLogEndpoint");
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
| **executionLogId** | **String**|  | |

### Return type

[**ExecuteResponse**](ExecuteResponse.md)

### Authorization

[AccessPointApiKeyQuery](../README.md#AccessPointApiKeyQuery), [SessionAuth](../README.md#SessionAuth), [AccessPointApiKeyHeader](../README.md#AccessPointApiKeyHeader), [AccessPointOAuth](../README.md#AccessPointOAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |

<a id="listExposedActions"></a>
# **listExposedActions**
> ExposedActionResponseSchema listExposedActions()

List Exposed Actions

List all the currently exposed actions for the given account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://nla.zapier.com");
    
    // Configure API key authorization: AccessPointApiKeyQuery
    ApiKeyAuth AccessPointApiKeyQuery = (ApiKeyAuth) defaultClient.getAuthentication("AccessPointApiKeyQuery");
    AccessPointApiKeyQuery.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //AccessPointApiKeyQuery.setApiKeyPrefix("Token");

    // Configure API key authorization: SessionAuth
    ApiKeyAuth SessionAuth = (ApiKeyAuth) defaultClient.getAuthentication("SessionAuth");
    SessionAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //SessionAuth.setApiKeyPrefix("Token");

    // Configure API key authorization: AccessPointApiKeyHeader
    ApiKeyAuth AccessPointApiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("AccessPointApiKeyHeader");
    AccessPointApiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //AccessPointApiKeyHeader.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: AccessPointOAuth
    OAuth AccessPointOAuth = (OAuth) defaultClient.getAuthentication("AccessPointOAuth");
    AccessPointOAuth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      ExposedActionResponseSchema result = apiInstance.listExposedActions();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listExposedActions");
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

[**ExposedActionResponseSchema**](ExposedActionResponseSchema.md)

### Authorization

[AccessPointApiKeyQuery](../README.md#AccessPointApiKeyQuery), [SessionAuth](../README.md#SessionAuth), [AccessPointApiKeyHeader](../README.md#AccessPointApiKeyHeader), [AccessPointOAuth](../README.md#AccessPointOAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

