# DatabaseRecommendedActionsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**databaseRecommendedActionsGet**](DatabaseRecommendedActionsApi.md#databaseRecommendedActionsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/databases/{databaseName}/advisors/{advisorName}/recommendedActions/{recommendedActionName} |  |
| [**databaseRecommendedActionsListByDatabaseAdvisor**](DatabaseRecommendedActionsApi.md#databaseRecommendedActionsListByDatabaseAdvisor) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/databases/{databaseName}/advisors/{advisorName}/recommendedActions |  |
| [**databaseRecommendedActionsUpdate**](DatabaseRecommendedActionsApi.md#databaseRecommendedActionsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/databases/{databaseName}/advisors/{advisorName}/recommendedActions/{recommendedActionName} |  |


<a id="databaseRecommendedActionsGet"></a>
# **databaseRecommendedActionsGet**
> RecommendedAction databaseRecommendedActionsGet(resourceGroupName, serverName, databaseName, advisorName, recommendedActionName, subscriptionId, apiVersion)



Gets a database recommended action.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DatabaseRecommendedActionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    DatabaseRecommendedActionsApi apiInstance = new DatabaseRecommendedActionsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String serverName = "serverName_example"; // String | The name of the server.
    String databaseName = "databaseName_example"; // String | The name of the database.
    String advisorName = "advisorName_example"; // String | The name of the Database Advisor.
    String recommendedActionName = "recommendedActionName_example"; // String | The name of Database Recommended Action.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    try {
      RecommendedAction result = apiInstance.databaseRecommendedActionsGet(resourceGroupName, serverName, databaseName, advisorName, recommendedActionName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DatabaseRecommendedActionsApi#databaseRecommendedActionsGet");
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
| **databaseName** | **String**| The name of the database. | |
| **advisorName** | **String**| The name of the Database Advisor. | |
| **recommendedActionName** | **String**| The name of Database Recommended Action. | |
| **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | |
| **apiVersion** | **String**| The API version to use for the request. | |

### Return type

[**RecommendedAction**](RecommendedAction.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully retrieved details of specified database recommended action. |  -  |
| **0** | *** Error Responses: ***   * 400 InvalidIdentifier - The identifier contains NULL or an invalid unicode character.   * 404 SubscriptionDoesNotHaveServer - The requested server was not found   * 404 DatabaseDoesNotExist - The requested database was not found   * 404 SubscriptionDoesNotHaveElasticPool - The requested elastic pool was not found   * 404 AdvisorNotFound - The requested advisor was not found.   * 404 RecommendedActionNotFound - The requested recommended action was not found.   * 404 AdvisorNotFound - The requested advisor was not found.   * 404 RecommendedActionNotFound - The requested recommended action was not found.   * 405 NotSupported - This functionality is not supported.   * 409 Conflict - Request could not be processed because of conflict in the request.   * 503 ServiceTemporarilyUnavailable - Feature temporarily unavailable. |  -  |

<a id="databaseRecommendedActionsListByDatabaseAdvisor"></a>
# **databaseRecommendedActionsListByDatabaseAdvisor**
> List&lt;RecommendedAction&gt; databaseRecommendedActionsListByDatabaseAdvisor(resourceGroupName, serverName, databaseName, advisorName, subscriptionId, apiVersion)



Gets list of Database Recommended Actions.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DatabaseRecommendedActionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    DatabaseRecommendedActionsApi apiInstance = new DatabaseRecommendedActionsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String serverName = "serverName_example"; // String | The name of the server.
    String databaseName = "databaseName_example"; // String | The name of the database.
    String advisorName = "advisorName_example"; // String | The name of the Database Advisor.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    try {
      List<RecommendedAction> result = apiInstance.databaseRecommendedActionsListByDatabaseAdvisor(resourceGroupName, serverName, databaseName, advisorName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DatabaseRecommendedActionsApi#databaseRecommendedActionsListByDatabaseAdvisor");
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
| **databaseName** | **String**| The name of the database. | |
| **advisorName** | **String**| The name of the Database Advisor. | |
| **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | |
| **apiVersion** | **String**| The API version to use for the request. | |

### Return type

[**List&lt;RecommendedAction&gt;**](RecommendedAction.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully retrieved the list of database recommended actions. |  -  |
| **0** | *** Error Responses: ***   * 400 InvalidIdentifier - The identifier contains NULL or an invalid unicode character.   * 404 SubscriptionDoesNotHaveServer - The requested server was not found   * 404 DatabaseDoesNotExist - The requested database was not found   * 404 SubscriptionDoesNotHaveElasticPool - The requested elastic pool was not found   * 404 AdvisorNotFound - The requested advisor was not found.   * 404 RecommendedActionNotFound - The requested recommended action was not found.   * 404 AdvisorNotFound - The requested advisor was not found.   * 404 RecommendedActionNotFound - The requested recommended action was not found.   * 405 NotSupported - This functionality is not supported.   * 409 Conflict - Request could not be processed because of conflict in the request.   * 503 ServiceTemporarilyUnavailable - Feature temporarily unavailable. |  -  |

<a id="databaseRecommendedActionsUpdate"></a>
# **databaseRecommendedActionsUpdate**
> RecommendedAction databaseRecommendedActionsUpdate(resourceGroupName, serverName, databaseName, advisorName, recommendedActionName, subscriptionId, apiVersion, parameters)



Updates a database recommended action.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DatabaseRecommendedActionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    DatabaseRecommendedActionsApi apiInstance = new DatabaseRecommendedActionsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String serverName = "serverName_example"; // String | The name of the server.
    String databaseName = "databaseName_example"; // String | The name of the database.
    String advisorName = "advisorName_example"; // String | The name of the Database Advisor.
    String recommendedActionName = "recommendedActionName_example"; // String | The name of Database Recommended Action.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    RecommendedAction parameters = new RecommendedAction(); // RecommendedAction | The requested recommended action resource state.
    try {
      RecommendedAction result = apiInstance.databaseRecommendedActionsUpdate(resourceGroupName, serverName, databaseName, advisorName, recommendedActionName, subscriptionId, apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DatabaseRecommendedActionsApi#databaseRecommendedActionsUpdate");
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
| **databaseName** | **String**| The name of the database. | |
| **advisorName** | **String**| The name of the Database Advisor. | |
| **recommendedActionName** | **String**| The name of Database Recommended Action. | |
| **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | |
| **apiVersion** | **String**| The API version to use for the request. | |
| **parameters** | [**RecommendedAction**](RecommendedAction.md)| The requested recommended action resource state. | |

### Return type

[**RecommendedAction**](RecommendedAction.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully updated the specified database recommended action. |  -  |
| **0** | *** Error Responses: ***   * 400 InvalidIdentifier - The identifier contains NULL or an invalid unicode character.   * 400 InvalidRecommendedActionUpsertRequest - The update recommended action request body does not exist or has no properties or state object.   * 400 InvalidRecommendedActionState - The specified state for recommended action is invalid   * 404 SubscriptionDoesNotHaveServer - The requested server was not found   * 404 DatabaseDoesNotExist - The requested database was not found   * 404 SubscriptionDoesNotHaveElasticPool - The requested elastic pool was not found   * 404 AdvisorNotFound - The requested advisor was not found.   * 404 RecommendedActionNotFound - The requested recommended action was not found.   * 404 AdvisorNotFound - The requested advisor was not found.   * 404 RecommendedActionNotFound - The requested recommended action was not found.   * 405 NotSupported - This functionality is not supported.   * 409 Conflict - Request could not be processed because of conflict in the request.   * 503 ServiceTemporarilyUnavailable - Feature temporarily unavailable. |  -  |

