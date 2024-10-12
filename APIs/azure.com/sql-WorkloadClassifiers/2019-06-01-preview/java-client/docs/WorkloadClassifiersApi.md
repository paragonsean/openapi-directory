# WorkloadClassifiersApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**workloadClassifiersCreateOrUpdate**](WorkloadClassifiersApi.md#workloadClassifiersCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/databases/{databaseName}/workloadGroups/{workloadGroupName}/workloadClassifiers/{workloadClassifierName} |  |
| [**workloadClassifiersDelete**](WorkloadClassifiersApi.md#workloadClassifiersDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/databases/{databaseName}/workloadGroups/{workloadGroupName}/workloadClassifiers/{workloadClassifierName} |  |
| [**workloadClassifiersGet**](WorkloadClassifiersApi.md#workloadClassifiersGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/databases/{databaseName}/workloadGroups/{workloadGroupName}/workloadClassifiers/{workloadClassifierName} |  |
| [**workloadClassifiersListByWorkloadGroup**](WorkloadClassifiersApi.md#workloadClassifiersListByWorkloadGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/databases/{databaseName}/workloadGroups/{workloadGroupName}/workloadClassifiers |  |


<a id="workloadClassifiersCreateOrUpdate"></a>
# **workloadClassifiersCreateOrUpdate**
> WorkloadClassifier workloadClassifiersCreateOrUpdate(resourceGroupName, serverName, databaseName, workloadGroupName, workloadClassifierName, subscriptionId, apiVersion, parameters)



Creates or updates a workload classifier.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WorkloadClassifiersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    WorkloadClassifiersApi apiInstance = new WorkloadClassifiersApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String serverName = "serverName_example"; // String | The name of the server.
    String databaseName = "databaseName_example"; // String | The name of the database.
    String workloadGroupName = "workloadGroupName_example"; // String | The name of the workload group from which to receive the classifier from.
    String workloadClassifierName = "workloadClassifierName_example"; // String | The name of the workload classifier to create/update.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    WorkloadClassifier parameters = new WorkloadClassifier(); // WorkloadClassifier | The properties of the workload classifier.
    try {
      WorkloadClassifier result = apiInstance.workloadClassifiersCreateOrUpdate(resourceGroupName, serverName, databaseName, workloadGroupName, workloadClassifierName, subscriptionId, apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WorkloadClassifiersApi#workloadClassifiersCreateOrUpdate");
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
| **workloadGroupName** | **String**| The name of the workload group from which to receive the classifier from. | |
| **workloadClassifierName** | **String**| The name of the workload classifier to create/update. | |
| **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | |
| **apiVersion** | **String**| The API version to use for the request. | |
| **parameters** | [**WorkloadClassifier**](WorkloadClassifier.md)| The properties of the workload classifier. | |

### Return type

[**WorkloadClassifier**](WorkloadClassifier.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully updated the workload classifier. |  -  |
| **201** | Successfully created the workload classifier. |  -  |
| **202** | Create or update for the workload classifier is in progress. |  -  |
| **0** | *** Error Responses: ***   * 400 FeatureDisabledOnSelectedEdition - User attempted to use a feature which is disabled on current database edition.   * 400 OperationNotAllowedOnPausedDatabase - Operation is not allowed on a paused database.   * 400 InvalidMemberNameParameter - Invalid member name parameter for this workload classifier.   * 400 InvalidStartTimeAndEndTimeParameters - Invalid start time and end time parameters for the workload classifier.   * 400 InvalidImportanceParameter - Importance must be one of the following strings: Low, Below_Normal, Normal, Above_Normal, High.   * 400 InvalidResourceRequestBody - The resource or resource properties in the request body is empty or invalid.   * 404 ServerNotInSubscriptionResourceGroup - Specified server does not exist in the specified resource group and subscription.   * 404 SubscriptionDoesNotHaveServer - The requested server was not found   * 404 DatabaseDoesNotExist - User has specified a database name that does not exist on this server instance.   * 404 ResourceNotFound - The requested resource was not found.   * 404 OperationIdNotFound - The operation with Id does not exist.   * 409 ConflictingSystemOperationInProgress - A system maintenance operation is in progress on the database and further operations need to wait until it is completed.   * 409 ConflictingDatabaseOperation - There is already some operation on the database and the current operation should wait till it is done.   * 409 OperationCancelled - The operation has been cancelled by user.   * 409 OperationInterrupted - The operation on the resource could not be completed because it was interrupted by another operation on the same resource.   * 500 OperationTimedOut - The operation timed out and automatically rolled back. Please retry the operation.   * 503 DatabaseUnavailable - The operation failed because the database is unavailable.   * 503 TooManyRequests - Requests beyond max requests that can be processed by available resources.   * 504 RequestTimeout - Service request exceeded the allowed timeout. |  -  |

<a id="workloadClassifiersDelete"></a>
# **workloadClassifiersDelete**
> workloadClassifiersDelete(resourceGroupName, serverName, databaseName, workloadGroupName, workloadClassifierName, subscriptionId, apiVersion)



Deletes a workload classifier.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WorkloadClassifiersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    WorkloadClassifiersApi apiInstance = new WorkloadClassifiersApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String serverName = "serverName_example"; // String | The name of the server.
    String databaseName = "databaseName_example"; // String | The name of the database.
    String workloadGroupName = "workloadGroupName_example"; // String | The name of the workload group from which to receive the classifier from.
    String workloadClassifierName = "workloadClassifierName_example"; // String | The name of the workload classifier to delete.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    try {
      apiInstance.workloadClassifiersDelete(resourceGroupName, serverName, databaseName, workloadGroupName, workloadClassifierName, subscriptionId, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling WorkloadClassifiersApi#workloadClassifiersDelete");
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
| **workloadGroupName** | **String**| The name of the workload group from which to receive the classifier from. | |
| **workloadClassifierName** | **String**| The name of the workload classifier to delete. | |
| **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | |
| **apiVersion** | **String**| The API version to use for the request. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully deleted the workload classifier. |  -  |
| **202** | Deleting the workload classifier is in progress. |  -  |
| **204** | The specified workload classifier does not exist. |  -  |
| **0** | *** Error Responses: ***   * 400 FeatureDisabledOnSelectedEdition - User attempted to use a feature which is disabled on current database edition.   * 400 OperationNotAllowedOnPausedDatabase - Operation is not allowed on a paused database.   * 404 ServerNotInSubscriptionResourceGroup - Specified server does not exist in the specified resource group and subscription.   * 404 SubscriptionDoesNotHaveServer - The requested server was not found   * 404 DatabaseDoesNotExist - User has specified a database name that does not exist on this server instance.   * 404 ResourceNotFound - The requested resource was not found.   * 404 OperationIdNotFound - The operation with Id does not exist.   * 409 ConflictingSystemOperationInProgress - A system maintenance operation is in progress on the database and further operations need to wait until it is completed.   * 409 ConflictingDatabaseOperation - There is already some operation on the database and the current operation should wait till it is done.   * 409 OperationCancelled - The operation has been cancelled by user.   * 409 OperationInterrupted - The operation on the resource could not be completed because it was interrupted by another operation on the same resource.   * 500 OperationTimedOut - The operation timed out and automatically rolled back. Please retry the operation.   * 503 DatabaseUnavailable - The operation failed because the database is unavailable.   * 503 TooManyRequests - Requests beyond max requests that can be processed by available resources.   * 504 RequestTimeout - Service request exceeded the allowed timeout. |  -  |

<a id="workloadClassifiersGet"></a>
# **workloadClassifiersGet**
> WorkloadClassifier workloadClassifiersGet(resourceGroupName, serverName, databaseName, workloadGroupName, workloadClassifierName, subscriptionId, apiVersion)



Gets a workload classifier

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WorkloadClassifiersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    WorkloadClassifiersApi apiInstance = new WorkloadClassifiersApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String serverName = "serverName_example"; // String | The name of the server.
    String databaseName = "databaseName_example"; // String | The name of the database.
    String workloadGroupName = "workloadGroupName_example"; // String | The name of the workload group from which to receive the classifier from.
    String workloadClassifierName = "workloadClassifierName_example"; // String | The name of the workload classifier.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    try {
      WorkloadClassifier result = apiInstance.workloadClassifiersGet(resourceGroupName, serverName, databaseName, workloadGroupName, workloadClassifierName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WorkloadClassifiersApi#workloadClassifiersGet");
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
| **workloadGroupName** | **String**| The name of the workload group from which to receive the classifier from. | |
| **workloadClassifierName** | **String**| The name of the workload classifier. | |
| **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | |
| **apiVersion** | **String**| The API version to use for the request. | |

### Return type

[**WorkloadClassifier**](WorkloadClassifier.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully retrieved the specifies workload classifier. |  -  |
| **0** | *** Error Responses: ***   * 400 FeatureDisabledOnSelectedEdition - User attempted to use a feature which is disabled on current database edition.   * 400 OperationNotAllowedOnPausedDatabase - Operation is not allowed on a paused database.   * 404 ServerNotInSubscriptionResourceGroup - Specified server does not exist in the specified resource group and subscription.   * 404 SubscriptionDoesNotHaveServer - The requested server was not found   * 404 DatabaseDoesNotExist - User has specified a database name that does not exist on this server instance.   * 404 ResourceNotFound - The requested resource was not found.   * 409 ConflictingSystemOperationInProgress - A system maintenance operation is in progress on the database and further operations need to wait until it is completed.   * 409 ConflictingDatabaseOperation - There is already some operation on the database and the current operation should wait till it is done.   * 503 DatabaseUnavailable - The operation failed because the database is unavailable.   * 503 TooManyRequests - Requests beyond max requests that can be processed by available resources.   * 504 RequestTimeout - Service request exceeded the allowed timeout. |  -  |

<a id="workloadClassifiersListByWorkloadGroup"></a>
# **workloadClassifiersListByWorkloadGroup**
> WorkloadClassifierListResult workloadClassifiersListByWorkloadGroup(resourceGroupName, serverName, databaseName, workloadGroupName, subscriptionId, apiVersion)



Gets the list of workload classifiers for a workload group

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WorkloadClassifiersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    WorkloadClassifiersApi apiInstance = new WorkloadClassifiersApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String serverName = "serverName_example"; // String | The name of the server.
    String databaseName = "databaseName_example"; // String | The name of the database.
    String workloadGroupName = "workloadGroupName_example"; // String | The name of the workload group from which to receive the classifiers from.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    try {
      WorkloadClassifierListResult result = apiInstance.workloadClassifiersListByWorkloadGroup(resourceGroupName, serverName, databaseName, workloadGroupName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WorkloadClassifiersApi#workloadClassifiersListByWorkloadGroup");
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
| **workloadGroupName** | **String**| The name of the workload group from which to receive the classifiers from. | |
| **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | |
| **apiVersion** | **String**| The API version to use for the request. | |

### Return type

[**WorkloadClassifierListResult**](WorkloadClassifierListResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully retrieved the list of workload groups. |  -  |
| **0** | *** Error Responses: ***   * 400 FeatureDisabledOnSelectedEdition - User attempted to use a feature which is disabled on current database edition.   * 400 OperationNotAllowedOnPausedDatabase - Operation is not allowed on a paused database.   * 404 ServerNotInSubscriptionResourceGroup - Specified server does not exist in the specified resource group and subscription.   * 404 SubscriptionDoesNotHaveServer - The requested server was not found   * 404 DatabaseDoesNotExist - User has specified a database name that does not exist on this server instance.   * 404 ResourceNotFound - The requested resource was not found.   * 409 ConflictingSystemOperationInProgress - A system maintenance operation is in progress on the database and further operations need to wait until it is completed.   * 409 ConflictingDatabaseOperation - There is already some operation on the database and the current operation should wait till it is done.   * 503 DatabaseUnavailable - The operation failed because the database is unavailable.   * 503 TooManyRequests - Requests beyond max requests that can be processed by available resources.   * 504 RequestTimeout - Service request exceeded the allowed timeout. |  -  |

