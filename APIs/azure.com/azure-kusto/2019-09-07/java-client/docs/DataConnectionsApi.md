# DataConnectionsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**dataConnectionsCheckNameAvailability**](DataConnectionsApi.md#dataConnectionsCheckNameAvailability) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Kusto/clusters/{clusterName}/databases/{databaseName}/checkNameAvailability |  |
| [**dataConnectionsCreateOrUpdate**](DataConnectionsApi.md#dataConnectionsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Kusto/clusters/{clusterName}/databases/{databaseName}/dataConnections/{dataConnectionName} |  |
| [**dataConnectionsDataConnectionValidation**](DataConnectionsApi.md#dataConnectionsDataConnectionValidation) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Kusto/clusters/{clusterName}/databases/{databaseName}/dataConnectionValidation |  |
| [**dataConnectionsDelete**](DataConnectionsApi.md#dataConnectionsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Kusto/clusters/{clusterName}/databases/{databaseName}/dataConnections/{dataConnectionName} |  |
| [**dataConnectionsGet**](DataConnectionsApi.md#dataConnectionsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Kusto/clusters/{clusterName}/databases/{databaseName}/dataConnections/{dataConnectionName} |  |
| [**dataConnectionsListByDatabase**](DataConnectionsApi.md#dataConnectionsListByDatabase) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Kusto/clusters/{clusterName}/databases/{databaseName}/dataConnections |  |
| [**dataConnectionsUpdate**](DataConnectionsApi.md#dataConnectionsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Kusto/clusters/{clusterName}/databases/{databaseName}/dataConnections/{dataConnectionName} |  |


<a id="dataConnectionsCheckNameAvailability"></a>
# **dataConnectionsCheckNameAvailability**
> CheckNameResult dataConnectionsCheckNameAvailability(resourceGroupName, clusterName, databaseName, apiVersion, subscriptionId, dataConnectionName)



Checks that the data connection name is valid and is not already in use.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DataConnectionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    DataConnectionsApi apiInstance = new DataConnectionsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group containing the Kusto cluster.
    String clusterName = "clusterName_example"; // String | The name of the Kusto cluster.
    String databaseName = "databaseName_example"; // String | The name of the database in the Kusto cluster.
    String apiVersion = "apiVersion_example"; // String | Client API Version.
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    DataConnectionCheckNameRequest dataConnectionName = new DataConnectionCheckNameRequest(); // DataConnectionCheckNameRequest | The name of the data connection.
    try {
      CheckNameResult result = apiInstance.dataConnectionsCheckNameAvailability(resourceGroupName, clusterName, databaseName, apiVersion, subscriptionId, dataConnectionName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DataConnectionsApi#dataConnectionsCheckNameAvailability");
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
| **dataConnectionName** | [**DataConnectionCheckNameRequest**](DataConnectionCheckNameRequest.md)| The name of the data connection. | |

### Return type

[**CheckNameResult**](CheckNameResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK -- Operation to check the Kusto resource name availability was successful. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="dataConnectionsCreateOrUpdate"></a>
# **dataConnectionsCreateOrUpdate**
> DataConnection dataConnectionsCreateOrUpdate(resourceGroupName, clusterName, databaseName, dataConnectionName, subscriptionId, apiVersion, parameters)



Creates or updates a data connection.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DataConnectionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    DataConnectionsApi apiInstance = new DataConnectionsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group containing the Kusto cluster.
    String clusterName = "clusterName_example"; // String | The name of the Kusto cluster.
    String databaseName = "databaseName_example"; // String | The name of the database in the Kusto cluster.
    String dataConnectionName = "dataConnectionName_example"; // String | The name of the data connection.
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String apiVersion = "apiVersion_example"; // String | Client API Version.
    DataConnection parameters = new DataConnection(); // DataConnection | The data connection parameters supplied to the CreateOrUpdate operation.
    try {
      DataConnection result = apiInstance.dataConnectionsCreateOrUpdate(resourceGroupName, clusterName, databaseName, dataConnectionName, subscriptionId, apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DataConnectionsApi#dataConnectionsCreateOrUpdate");
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
| **dataConnectionName** | **String**| The name of the data connection. | |
| **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **apiVersion** | **String**| Client API Version. | |
| **parameters** | [**DataConnection**](DataConnection.md)| The data connection parameters supplied to the CreateOrUpdate operation. | |

### Return type

[**DataConnection**](DataConnection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully updated the data connection. |  -  |
| **201** | Successfully created the data connection. |  -  |
| **202** | Accepted the create data connection request. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="dataConnectionsDataConnectionValidation"></a>
# **dataConnectionsDataConnectionValidation**
> DataConnectionValidationListResult dataConnectionsDataConnectionValidation(resourceGroupName, clusterName, databaseName, apiVersion, subscriptionId, parameters)



Checks that the data connection parameters are valid.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DataConnectionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    DataConnectionsApi apiInstance = new DataConnectionsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group containing the Kusto cluster.
    String clusterName = "clusterName_example"; // String | The name of the Kusto cluster.
    String databaseName = "databaseName_example"; // String | The name of the database in the Kusto cluster.
    String apiVersion = "apiVersion_example"; // String | Client API Version.
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    DataConnectionValidation parameters = new DataConnectionValidation(); // DataConnectionValidation | The data connection parameters supplied to the CreateOrUpdate operation.
    try {
      DataConnectionValidationListResult result = apiInstance.dataConnectionsDataConnectionValidation(resourceGroupName, clusterName, databaseName, apiVersion, subscriptionId, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DataConnectionsApi#dataConnectionsDataConnectionValidation");
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
| **parameters** | [**DataConnectionValidation**](DataConnectionValidation.md)| The data connection parameters supplied to the CreateOrUpdate operation. | |

### Return type

[**DataConnectionValidationListResult**](DataConnectionValidationListResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK -- Operation to check the kusto resource name availability was successful. |  -  |

<a id="dataConnectionsDelete"></a>
# **dataConnectionsDelete**
> dataConnectionsDelete(resourceGroupName, clusterName, databaseName, dataConnectionName, subscriptionId, apiVersion)



Deletes the data connection with the given name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DataConnectionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    DataConnectionsApi apiInstance = new DataConnectionsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group containing the Kusto cluster.
    String clusterName = "clusterName_example"; // String | The name of the Kusto cluster.
    String databaseName = "databaseName_example"; // String | The name of the database in the Kusto cluster.
    String dataConnectionName = "dataConnectionName_example"; // String | The name of the data connection.
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String apiVersion = "apiVersion_example"; // String | Client API Version.
    try {
      apiInstance.dataConnectionsDelete(resourceGroupName, clusterName, databaseName, dataConnectionName, subscriptionId, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling DataConnectionsApi#dataConnectionsDelete");
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
| **dataConnectionName** | **String**| The name of the data connection. | |
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
| **200** | Successfully deleted the data connection. |  -  |
| **202** | Accepted. |  -  |
| **204** | The specified data connection does not exist. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="dataConnectionsGet"></a>
# **dataConnectionsGet**
> DataConnection dataConnectionsGet(resourceGroupName, clusterName, databaseName, dataConnectionName, subscriptionId, apiVersion)



Returns a data connection.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DataConnectionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    DataConnectionsApi apiInstance = new DataConnectionsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group containing the Kusto cluster.
    String clusterName = "clusterName_example"; // String | The name of the Kusto cluster.
    String databaseName = "databaseName_example"; // String | The name of the database in the Kusto cluster.
    String dataConnectionName = "dataConnectionName_example"; // String | The name of the data connection.
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String apiVersion = "apiVersion_example"; // String | Client API Version.
    try {
      DataConnection result = apiInstance.dataConnectionsGet(resourceGroupName, clusterName, databaseName, dataConnectionName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DataConnectionsApi#dataConnectionsGet");
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
| **dataConnectionName** | **String**| The name of the data connection. | |
| **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **apiVersion** | **String**| Client API Version. | |

### Return type

[**DataConnection**](DataConnection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully retrieved the specified data connection. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="dataConnectionsListByDatabase"></a>
# **dataConnectionsListByDatabase**
> DataConnectionListResult dataConnectionsListByDatabase(resourceGroupName, clusterName, databaseName, subscriptionId, apiVersion)



Returns the list of data connections of the given Kusto database.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DataConnectionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    DataConnectionsApi apiInstance = new DataConnectionsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group containing the Kusto cluster.
    String clusterName = "clusterName_example"; // String | The name of the Kusto cluster.
    String databaseName = "databaseName_example"; // String | The name of the database in the Kusto cluster.
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String apiVersion = "apiVersion_example"; // String | Client API Version.
    try {
      DataConnectionListResult result = apiInstance.dataConnectionsListByDatabase(resourceGroupName, clusterName, databaseName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DataConnectionsApi#dataConnectionsListByDatabase");
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

[**DataConnectionListResult**](DataConnectionListResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully retrieved the list of data connections. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="dataConnectionsUpdate"></a>
# **dataConnectionsUpdate**
> DataConnection dataConnectionsUpdate(resourceGroupName, clusterName, databaseName, dataConnectionName, subscriptionId, apiVersion, parameters)



Updates a data connection.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DataConnectionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    DataConnectionsApi apiInstance = new DataConnectionsApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group containing the Kusto cluster.
    String clusterName = "clusterName_example"; // String | The name of the Kusto cluster.
    String databaseName = "databaseName_example"; // String | The name of the database in the Kusto cluster.
    String dataConnectionName = "dataConnectionName_example"; // String | The name of the data connection.
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String apiVersion = "apiVersion_example"; // String | Client API Version.
    DataConnection parameters = new DataConnection(); // DataConnection | The data connection parameters supplied to the Update operation.
    try {
      DataConnection result = apiInstance.dataConnectionsUpdate(resourceGroupName, clusterName, databaseName, dataConnectionName, subscriptionId, apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DataConnectionsApi#dataConnectionsUpdate");
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
| **dataConnectionName** | **String**| The name of the data connection. | |
| **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **apiVersion** | **String**| Client API Version. | |
| **parameters** | [**DataConnection**](DataConnection.md)| The data connection parameters supplied to the Update operation. | |

### Return type

[**DataConnection**](DataConnection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully updated the data connection. |  -  |
| **201** | Successfully updated the data connection. |  -  |
| **202** | Accepted the update data connection request. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

