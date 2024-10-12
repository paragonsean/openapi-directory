# ServerAdvisorsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**serverAdvisorsGet**](ServerAdvisorsApi.md#serverAdvisorsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/advisors/{advisorName} |  |
| [**serverAdvisorsListByServer**](ServerAdvisorsApi.md#serverAdvisorsListByServer) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/advisors |  |
| [**serverAdvisorsUpdate**](ServerAdvisorsApi.md#serverAdvisorsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/advisors/{advisorName} |  |


<a id="serverAdvisorsGet"></a>
# **serverAdvisorsGet**
> Advisor serverAdvisorsGet(resourceGroupName, serverName, advisorName, subscriptionId, apiVersion)



Gets a server advisor.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServerAdvisorsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    ServerAdvisorsApi apiInstance = new ServerAdvisorsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String serverName = "serverName_example"; // String | The name of the server.
    String advisorName = "advisorName_example"; // String | The name of the Server Advisor.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    try {
      Advisor result = apiInstance.serverAdvisorsGet(resourceGroupName, serverName, advisorName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServerAdvisorsApi#serverAdvisorsGet");
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
| **resourceGroupName** | **String**| The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. | |
| **serverName** | **String**| The name of the server. | |
| **advisorName** | **String**| The name of the Server Advisor. | |
| **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | |
| **apiVersion** | **String**| The API version to use for the request. | |

### Return type

[**Advisor**](Advisor.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully retrieved details of specified server advisor. |  -  |
| **0** | *** Error Responses: ***   * 400 InvalidIdentifier - The identifier contains NULL or an invalid unicode character.   * 404 SubscriptionDoesNotHaveServer - The requested server was not found   * 404 DatabaseDoesNotExist - The requested database was not found   * 404 SubscriptionDoesNotHaveElasticPool - The requested elastic pool was not found   * 404 AdvisorNotFound - The requested advisor was not found.   * 405 NotSupported - This functionality is not supported.   * 409 Conflict - Request could not be processed because of conflict in the request.   * 503 ServiceTemporarilyUnavailable - Feature temporarily unavailable. |  -  |

<a id="serverAdvisorsListByServer"></a>
# **serverAdvisorsListByServer**
> List&lt;Advisor&gt; serverAdvisorsListByServer(resourceGroupName, serverName, subscriptionId, apiVersion)



Gets a list of server advisors.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServerAdvisorsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    ServerAdvisorsApi apiInstance = new ServerAdvisorsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String serverName = "serverName_example"; // String | The name of the server.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    try {
      List<Advisor> result = apiInstance.serverAdvisorsListByServer(resourceGroupName, serverName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServerAdvisorsApi#serverAdvisorsListByServer");
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
| **resourceGroupName** | **String**| The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. | |
| **serverName** | **String**| The name of the server. | |
| **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | |
| **apiVersion** | **String**| The API version to use for the request. | |

### Return type

[**List&lt;Advisor&gt;**](Advisor.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully retrieved the list of server advisors. |  -  |
| **0** | *** Error Responses: ***   * 400 InvalidIdentifier - The identifier contains NULL or an invalid unicode character.   * 404 SubscriptionDoesNotHaveServer - The requested server was not found   * 404 DatabaseDoesNotExist - The requested database was not found   * 404 SubscriptionDoesNotHaveElasticPool - The requested elastic pool was not found   * 404 AdvisorNotFound - The requested advisor was not found.   * 405 NotSupported - This functionality is not supported.   * 409 Conflict - Request could not be processed because of conflict in the request.   * 503 ServiceTemporarilyUnavailable - Feature temporarily unavailable. |  -  |

<a id="serverAdvisorsUpdate"></a>
# **serverAdvisorsUpdate**
> Advisor serverAdvisorsUpdate(resourceGroupName, serverName, advisorName, subscriptionId, apiVersion, parameters)



Updates a server advisor.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServerAdvisorsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    ServerAdvisorsApi apiInstance = new ServerAdvisorsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String serverName = "serverName_example"; // String | The name of the server.
    String advisorName = "advisorName_example"; // String | The name of the Server Advisor.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    Advisor parameters = new Advisor(); // Advisor | The requested advisor resource state.
    try {
      Advisor result = apiInstance.serverAdvisorsUpdate(resourceGroupName, serverName, advisorName, subscriptionId, apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServerAdvisorsApi#serverAdvisorsUpdate");
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
| **resourceGroupName** | **String**| The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. | |
| **serverName** | **String**| The name of the server. | |
| **advisorName** | **String**| The name of the Server Advisor. | |
| **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | |
| **apiVersion** | **String**| The API version to use for the request. | |
| **parameters** | [**Advisor**](Advisor.md)| The requested advisor resource state. | |

### Return type

[**Advisor**](Advisor.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully updated the specified server advisor. |  -  |
| **0** | *** Error Responses: ***   * 400 InvalidIdentifier - The identifier contains NULL or an invalid unicode character.   * 400 InvalidAdvisorUpsertRequest - The update advisor request body does not exist or has no properties object.   * 400 InvalidAdvisorAutoExecuteStatus - Specified auto-execute status for the advisor is not allowed.   * 404 SubscriptionDoesNotHaveServer - The requested server was not found   * 404 DatabaseDoesNotExist - The requested database was not found   * 404 SubscriptionDoesNotHaveElasticPool - The requested elastic pool was not found   * 404 AdvisorNotFound - The requested advisor was not found.   * 405 NotSupported - This functionality is not supported.   * 409 Conflict - Request could not be processed because of conflict in the request.   * 503 ServiceTemporarilyUnavailable - Feature temporarily unavailable. |  -  |

