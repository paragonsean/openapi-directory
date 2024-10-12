# BotConnectionApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**botConnectionCreate**](BotConnectionApi.md#botConnectionCreate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.BotService/botServices/{resourceName}/Connections/{connectionName} |  |
| [**botConnectionDelete**](BotConnectionApi.md#botConnectionDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.BotService/botServices/{resourceName}/Connections/{connectionName} |  |
| [**botConnectionGet**](BotConnectionApi.md#botConnectionGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.BotService/botServices/{resourceName}/Connections/{connectionName} |  |
| [**botConnectionListByBotService**](BotConnectionApi.md#botConnectionListByBotService) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.BotService/botServices/{resourceName}/connections |  |
| [**botConnectionListWithSecrets**](BotConnectionApi.md#botConnectionListWithSecrets) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.BotService/botServices/{resourceName}/Connections/{connectionName}/listWithSecrets |  |
| [**botConnectionUpdate**](BotConnectionApi.md#botConnectionUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.BotService/botServices/{resourceName}/Connections/{connectionName} |  |


<a id="botConnectionCreate"></a>
# **botConnectionCreate**
> ConnectionSetting botConnectionCreate(resourceGroupName, resourceName, connectionName, apiVersion, subscriptionId, parameters)



Register a new Auth Connection for a Bot Service

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BotConnectionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    BotConnectionApi apiInstance = new BotConnectionApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the Bot resource group in the user subscription.
    String resourceName = "resourceName_example"; // String | The name of the Bot resource.
    String connectionName = "connectionName_example"; // String | The name of the Bot Service Connection Setting resource
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
    ConnectionSetting parameters = new ConnectionSetting(); // ConnectionSetting | The parameters to provide for creating the Connection Setting.
    try {
      ConnectionSetting result = apiInstance.botConnectionCreate(resourceGroupName, resourceName, connectionName, apiVersion, subscriptionId, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BotConnectionApi#botConnectionCreate");
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
| **resourceGroupName** | **String**| The name of the Bot resource group in the user subscription. | |
| **resourceName** | **String**| The name of the Bot resource. | |
| **connectionName** | **String**| The name of the Bot Service Connection Setting resource | |
| **apiVersion** | **String**| Version of the API to be used with the client request. | |
| **subscriptionId** | **String**| Azure Subscription ID. | |
| **parameters** | [**ConnectionSetting**](ConnectionSetting.md)| The parameters to provide for creating the Connection Setting. | |

### Return type

[**ConnectionSetting**](ConnectionSetting.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | If resource is created successfully or already existed, the service should return 200 (OK). |  -  |
| **201** | If resource is created successfully, the service should return 201 (Created). Execution to continue asynchronously. |  -  |
| **0** | Error response describing why the operation failed |  -  |

<a id="botConnectionDelete"></a>
# **botConnectionDelete**
> botConnectionDelete(resourceGroupName, resourceName, connectionName, apiVersion, subscriptionId)



Deletes a Connection Setting registration for a Bot Service

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BotConnectionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    BotConnectionApi apiInstance = new BotConnectionApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the Bot resource group in the user subscription.
    String resourceName = "resourceName_example"; // String | The name of the Bot resource.
    String connectionName = "connectionName_example"; // String | The name of the Bot Service Connection Setting resource
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
    try {
      apiInstance.botConnectionDelete(resourceGroupName, resourceName, connectionName, apiVersion, subscriptionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling BotConnectionApi#botConnectionDelete");
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
| **resourceGroupName** | **String**| The name of the Bot resource group in the user subscription. | |
| **resourceName** | **String**| The name of the Bot resource. | |
| **connectionName** | **String**| The name of the Bot Service Connection Setting resource | |
| **apiVersion** | **String**| Version of the API to be used with the client request. | |
| **subscriptionId** | **String**| Azure Subscription ID. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A 200 (OK) should be returned if the object exists and was deleted successfully; |  -  |
| **204** | a 204 (NoContent) should be used if the resource does not exist and the request is well formed. |  -  |
| **0** | Error response describing why the operation failed |  -  |

<a id="botConnectionGet"></a>
# **botConnectionGet**
> ConnectionSetting botConnectionGet(resourceGroupName, resourceName, connectionName, apiVersion, subscriptionId)



Get a Connection Setting registration for a Bot Service

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BotConnectionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    BotConnectionApi apiInstance = new BotConnectionApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the Bot resource group in the user subscription.
    String resourceName = "resourceName_example"; // String | The name of the Bot resource.
    String connectionName = "connectionName_example"; // String | The name of the Bot Service Connection Setting resource
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
    try {
      ConnectionSetting result = apiInstance.botConnectionGet(resourceGroupName, resourceName, connectionName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BotConnectionApi#botConnectionGet");
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
| **resourceGroupName** | **String**| The name of the Bot resource group in the user subscription. | |
| **resourceName** | **String**| The name of the Bot resource. | |
| **connectionName** | **String**| The name of the Bot Service Connection Setting resource | |
| **apiVersion** | **String**| Version of the API to be used with the client request. | |
| **subscriptionId** | **String**| Azure Subscription ID. | |

### Return type

[**ConnectionSetting**](ConnectionSetting.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The resource provider should return 200 (OK) to indicate that the operation completed successfully.  |  -  |
| **0** | Error response describing why the operation failed. If the resource group *or* resource does not exist, 404 (NotFound) should be returned. |  -  |

<a id="botConnectionListByBotService"></a>
# **botConnectionListByBotService**
> ConnectionSettingResponseList botConnectionListByBotService(resourceGroupName, resourceName, subscriptionId, apiVersion)



Returns all the Connection Settings registered to a particular BotService resource

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BotConnectionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    BotConnectionApi apiInstance = new BotConnectionApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the Bot resource group in the user subscription.
    String resourceName = "resourceName_example"; // String | The name of the Bot resource.
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    try {
      ConnectionSettingResponseList result = apiInstance.botConnectionListByBotService(resourceGroupName, resourceName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BotConnectionApi#botConnectionListByBotService");
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
| **resourceGroupName** | **String**| The name of the Bot resource group in the user subscription. | |
| **resourceName** | **String**| The name of the Bot resource. | |
| **subscriptionId** | **String**| Azure Subscription ID. | |
| **apiVersion** | **String**| Version of the API to be used with the client request. | |

### Return type

[**ConnectionSettingResponseList**](ConnectionSettingResponseList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The resource provider should return 200 (OK) to indicate that the operation completed successfully. For other errors (e.g. internal errors) use the appropriate HTTP error code. The nextLink field is expected to point to the URL the client should use to fetch the next page (per server side paging). This matches the OData guidelines for paged responses here. If a resource provider does not support paging, it should return the same body (JSON object with “value” property) but omit nextLink entirely (or set to null, *not* empty string) for future compatibility. The nextLink should be implemented using following query parameters: · skipToken: opaque token that allows the resource provider to skip resources already enumerated. This value is defined and returned by the RP after first request via nextLink. · top: the optional client query parameter which defines the maximum number of records to be returned by the server. Implementation details: · NextLink may include all the query parameters (specifically OData $filter) used by the client in the first query.  · Server may return less records than requested with nextLink. Returning zero records with NextLink is an acceptable response.  Clients must fetch records until the nextLink is not returned back / null. Clients should never rely on number of returned records to determinate if pagination is completed. |  -  |
| **0** | Error response describing why the operation failed. If the resource group does not exist, 404 (NotFound) will be returned. |  -  |

<a id="botConnectionListWithSecrets"></a>
# **botConnectionListWithSecrets**
> ConnectionSetting botConnectionListWithSecrets(resourceGroupName, resourceName, connectionName, apiVersion, subscriptionId)



Get a Connection Setting registration for a Bot Service

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BotConnectionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    BotConnectionApi apiInstance = new BotConnectionApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the Bot resource group in the user subscription.
    String resourceName = "resourceName_example"; // String | The name of the Bot resource.
    String connectionName = "connectionName_example"; // String | The name of the Bot Service Connection Setting resource
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
    try {
      ConnectionSetting result = apiInstance.botConnectionListWithSecrets(resourceGroupName, resourceName, connectionName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BotConnectionApi#botConnectionListWithSecrets");
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
| **resourceGroupName** | **String**| The name of the Bot resource group in the user subscription. | |
| **resourceName** | **String**| The name of the Bot resource. | |
| **connectionName** | **String**| The name of the Bot Service Connection Setting resource | |
| **apiVersion** | **String**| Version of the API to be used with the client request. | |
| **subscriptionId** | **String**| Azure Subscription ID. | |

### Return type

[**ConnectionSetting**](ConnectionSetting.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The resource provider should return 200 (OK) to indicate that the operation completed successfully.  |  -  |
| **0** | Error response describing why the operation failed. If the resource group *or* resource does not exist, 404 (NotFound) should be returned. |  -  |

<a id="botConnectionUpdate"></a>
# **botConnectionUpdate**
> ConnectionSetting botConnectionUpdate(resourceGroupName, resourceName, connectionName, apiVersion, subscriptionId, parameters)



Updates a Connection Setting registration for a Bot Service

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BotConnectionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    BotConnectionApi apiInstance = new BotConnectionApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the Bot resource group in the user subscription.
    String resourceName = "resourceName_example"; // String | The name of the Bot resource.
    String connectionName = "connectionName_example"; // String | The name of the Bot Service Connection Setting resource
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
    String subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
    ConnectionSetting parameters = new ConnectionSetting(); // ConnectionSetting | The parameters to provide for updating the Connection Setting.
    try {
      ConnectionSetting result = apiInstance.botConnectionUpdate(resourceGroupName, resourceName, connectionName, apiVersion, subscriptionId, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BotConnectionApi#botConnectionUpdate");
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
| **resourceGroupName** | **String**| The name of the Bot resource group in the user subscription. | |
| **resourceName** | **String**| The name of the Bot resource. | |
| **connectionName** | **String**| The name of the Bot Service Connection Setting resource | |
| **apiVersion** | **String**| Version of the API to be used with the client request. | |
| **subscriptionId** | **String**| Azure Subscription ID. | |
| **parameters** | [**ConnectionSetting**](ConnectionSetting.md)| The parameters to provide for updating the Connection Setting. | |

### Return type

[**ConnectionSetting**](ConnectionSetting.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | If resource is created successfully or already existed, the service should return 200 (OK). |  -  |
| **201** | If resource is created successfully, the service should return 201 (Created). Execution to continue asynchronously. |  -  |
| **0** | Error response describing why the operation failed |  -  |

