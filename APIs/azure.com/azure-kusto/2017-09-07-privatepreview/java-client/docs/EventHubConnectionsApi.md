# EventHubConnectionsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**eventHubConnectionsCreateOrUpdate**](EventHubConnectionsApi.md#eventHubConnectionsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Kusto/clusters/{clusterName}/databases/{databaseName}/eventhubconnections/{eventHubConnectionName} |  |
| [**eventHubConnectionsDelete**](EventHubConnectionsApi.md#eventHubConnectionsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Kusto/clusters/{clusterName}/databases/{databaseName}/eventhubconnections/{eventHubConnectionName} |  |
| [**eventHubConnectionsEventhubConnectionValidation**](EventHubConnectionsApi.md#eventHubConnectionsEventhubConnectionValidation) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Kusto/clusters/{clusterName}/databases/{databaseName}/eventhubConnectionValidation |  |
| [**eventHubConnectionsGet**](EventHubConnectionsApi.md#eventHubConnectionsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Kusto/clusters/{clusterName}/databases/{databaseName}/eventhubconnections/{eventHubConnectionName} |  |
| [**eventHubConnectionsListByDatabase**](EventHubConnectionsApi.md#eventHubConnectionsListByDatabase) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Kusto/clusters/{clusterName}/databases/{databaseName}/eventhubconnections |  |
| [**eventHubConnectionsUpdate**](EventHubConnectionsApi.md#eventHubConnectionsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Kusto/clusters/{clusterName}/databases/{databaseName}/eventhubconnections/{eventHubConnectionName} |  |


<a id="eventHubConnectionsCreateOrUpdate"></a>
# **eventHubConnectionsCreateOrUpdate**
> EventHubConnection eventHubConnectionsCreateOrUpdate(resourceGroupName, clusterName, databaseName, eventHubConnectionName, subscriptionId, apiVersion, parameters)



Creates or updates a Event Hub connection.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventHubConnectionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    EventHubConnectionsApi apiInstance = new EventHubConnectionsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group containing the Kusto cluster.
    String clusterName = "clusterName_example"; // String | The name of the Kusto cluster.
    String databaseName = "databaseName_example"; // String | The name of the database in the Kusto cluster.
    String eventHubConnectionName = "eventHubConnectionName_example"; // String | The name of the event hub connection.
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String apiVersion = "apiVersion_example"; // String | Client API Version.
    EventHubConnection parameters = new EventHubConnection(); // EventHubConnection | The Event Hub connection parameters supplied to the CreateOrUpdate operation.
    try {
      EventHubConnection result = apiInstance.eventHubConnectionsCreateOrUpdate(resourceGroupName, clusterName, databaseName, eventHubConnectionName, subscriptionId, apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventHubConnectionsApi#eventHubConnectionsCreateOrUpdate");
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
| **resourceGroupName** | **String**| The name of the resource group containing the Kusto cluster. | |
| **clusterName** | **String**| The name of the Kusto cluster. | |
| **databaseName** | **String**| The name of the database in the Kusto cluster. | |
| **eventHubConnectionName** | **String**| The name of the event hub connection. | |
| **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **apiVersion** | **String**| Client API Version. | |
| **parameters** | [**EventHubConnection**](EventHubConnection.md)| The Event Hub connection parameters supplied to the CreateOrUpdate operation. | |

### Return type

[**EventHubConnection**](EventHubConnection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully updated the Event Hub connection. |  -  |
| **201** | Successfully created the Event Hub connection. |  -  |
| **202** | Accepted the create Event Hub connection request. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="eventHubConnectionsDelete"></a>
# **eventHubConnectionsDelete**
> eventHubConnectionsDelete(resourceGroupName, clusterName, databaseName, eventHubConnectionName, subscriptionId, apiVersion)



Deletes the Event Hub connection with the given name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventHubConnectionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    EventHubConnectionsApi apiInstance = new EventHubConnectionsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group containing the Kusto cluster.
    String clusterName = "clusterName_example"; // String | The name of the Kusto cluster.
    String databaseName = "databaseName_example"; // String | The name of the database in the Kusto cluster.
    String eventHubConnectionName = "eventHubConnectionName_example"; // String | The name of the event hub connection.
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String apiVersion = "apiVersion_example"; // String | Client API Version.
    try {
      apiInstance.eventHubConnectionsDelete(resourceGroupName, clusterName, databaseName, eventHubConnectionName, subscriptionId, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventHubConnectionsApi#eventHubConnectionsDelete");
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
| **resourceGroupName** | **String**| The name of the resource group containing the Kusto cluster. | |
| **clusterName** | **String**| The name of the Kusto cluster. | |
| **databaseName** | **String**| The name of the database in the Kusto cluster. | |
| **eventHubConnectionName** | **String**| The name of the event hub connection. | |
| **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **apiVersion** | **String**| Client API Version. | |

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
| **200** | Successfully deleted the Event Hub connection. |  -  |
| **202** | Accepted. |  -  |
| **204** | The specified Event Hub connection does not exist. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="eventHubConnectionsEventhubConnectionValidation"></a>
# **eventHubConnectionsEventhubConnectionValidation**
> EventHubConnectionValidationListResult eventHubConnectionsEventhubConnectionValidation(resourceGroupName, clusterName, databaseName, apiVersion, subscriptionId, parameters)



Checks that the Event Hub data connection parameters are valid.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventHubConnectionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    EventHubConnectionsApi apiInstance = new EventHubConnectionsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group containing the Kusto cluster.
    String clusterName = "clusterName_example"; // String | The name of the Kusto cluster.
    String databaseName = "databaseName_example"; // String | The name of the database in the Kusto cluster.
    String apiVersion = "apiVersion_example"; // String | Client API Version.
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    EventHubConnectionValidation parameters = new EventHubConnectionValidation(); // EventHubConnectionValidation | The Event Hub connection parameters supplied to the CreateOrUpdate operation.
    try {
      EventHubConnectionValidationListResult result = apiInstance.eventHubConnectionsEventhubConnectionValidation(resourceGroupName, clusterName, databaseName, apiVersion, subscriptionId, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventHubConnectionsApi#eventHubConnectionsEventhubConnectionValidation");
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
| **resourceGroupName** | **String**| The name of the resource group containing the Kusto cluster. | |
| **clusterName** | **String**| The name of the Kusto cluster. | |
| **databaseName** | **String**| The name of the database in the Kusto cluster. | |
| **apiVersion** | **String**| Client API Version. | |
| **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **parameters** | [**EventHubConnectionValidation**](EventHubConnectionValidation.md)| The Event Hub connection parameters supplied to the CreateOrUpdate operation. | |

### Return type

[**EventHubConnectionValidationListResult**](EventHubConnectionValidationListResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK -- Operation to check the kusto resource name availability was successful. |  -  |

<a id="eventHubConnectionsGet"></a>
# **eventHubConnectionsGet**
> EventHubConnection eventHubConnectionsGet(resourceGroupName, clusterName, databaseName, eventHubConnectionName, subscriptionId, apiVersion)



Returns an Event Hub connection.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventHubConnectionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    EventHubConnectionsApi apiInstance = new EventHubConnectionsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group containing the Kusto cluster.
    String clusterName = "clusterName_example"; // String | The name of the Kusto cluster.
    String databaseName = "databaseName_example"; // String | The name of the database in the Kusto cluster.
    String eventHubConnectionName = "eventHubConnectionName_example"; // String | The name of the event hub connection.
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String apiVersion = "apiVersion_example"; // String | Client API Version.
    try {
      EventHubConnection result = apiInstance.eventHubConnectionsGet(resourceGroupName, clusterName, databaseName, eventHubConnectionName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventHubConnectionsApi#eventHubConnectionsGet");
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
| **resourceGroupName** | **String**| The name of the resource group containing the Kusto cluster. | |
| **clusterName** | **String**| The name of the Kusto cluster. | |
| **databaseName** | **String**| The name of the database in the Kusto cluster. | |
| **eventHubConnectionName** | **String**| The name of the event hub connection. | |
| **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **apiVersion** | **String**| Client API Version. | |

### Return type

[**EventHubConnection**](EventHubConnection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully retrieved the specified Event Hub connection. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="eventHubConnectionsListByDatabase"></a>
# **eventHubConnectionsListByDatabase**
> EventHubConnectionListResult eventHubConnectionsListByDatabase(resourceGroupName, clusterName, databaseName, subscriptionId, apiVersion)



Returns the list of Event Hub connections of the given Kusto database.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventHubConnectionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    EventHubConnectionsApi apiInstance = new EventHubConnectionsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group containing the Kusto cluster.
    String clusterName = "clusterName_example"; // String | The name of the Kusto cluster.
    String databaseName = "databaseName_example"; // String | The name of the database in the Kusto cluster.
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String apiVersion = "apiVersion_example"; // String | Client API Version.
    try {
      EventHubConnectionListResult result = apiInstance.eventHubConnectionsListByDatabase(resourceGroupName, clusterName, databaseName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventHubConnectionsApi#eventHubConnectionsListByDatabase");
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
| **resourceGroupName** | **String**| The name of the resource group containing the Kusto cluster. | |
| **clusterName** | **String**| The name of the Kusto cluster. | |
| **databaseName** | **String**| The name of the database in the Kusto cluster. | |
| **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **apiVersion** | **String**| Client API Version. | |

### Return type

[**EventHubConnectionListResult**](EventHubConnectionListResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully retrieved the list of Event Hub connections. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="eventHubConnectionsUpdate"></a>
# **eventHubConnectionsUpdate**
> EventHubConnection eventHubConnectionsUpdate(resourceGroupName, clusterName, databaseName, eventHubConnectionName, subscriptionId, apiVersion, parameters)



Updates a Event Hub connection.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventHubConnectionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    EventHubConnectionsApi apiInstance = new EventHubConnectionsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group containing the Kusto cluster.
    String clusterName = "clusterName_example"; // String | The name of the Kusto cluster.
    String databaseName = "databaseName_example"; // String | The name of the database in the Kusto cluster.
    String eventHubConnectionName = "eventHubConnectionName_example"; // String | The name of the event hub connection.
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String apiVersion = "apiVersion_example"; // String | Client API Version.
    EventHubConnectionUpdate parameters = new EventHubConnectionUpdate(); // EventHubConnectionUpdate | The Event Hub connection parameters supplied to the Update operation.
    try {
      EventHubConnection result = apiInstance.eventHubConnectionsUpdate(resourceGroupName, clusterName, databaseName, eventHubConnectionName, subscriptionId, apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventHubConnectionsApi#eventHubConnectionsUpdate");
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
| **resourceGroupName** | **String**| The name of the resource group containing the Kusto cluster. | |
| **clusterName** | **String**| The name of the Kusto cluster. | |
| **databaseName** | **String**| The name of the database in the Kusto cluster. | |
| **eventHubConnectionName** | **String**| The name of the event hub connection. | |
| **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **apiVersion** | **String**| Client API Version. | |
| **parameters** | [**EventHubConnectionUpdate**](EventHubConnectionUpdate.md)| The Event Hub connection parameters supplied to the Update operation. | |

### Return type

[**EventHubConnection**](EventHubConnection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully updated the Event Hub connection. |  -  |
| **201** | Successfully updated the Event Hub connection. |  -  |
| **202** | Accepted the update Event Hub connection request. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

