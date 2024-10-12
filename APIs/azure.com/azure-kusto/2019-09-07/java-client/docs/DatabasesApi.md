# DatabasesApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**databasesAddPrincipals**](DatabasesApi.md#databasesAddPrincipals) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Kusto/clusters/{clusterName}/databases/{databaseName}/addPrincipals |  |
| [**databasesCheckNameAvailability**](DatabasesApi.md#databasesCheckNameAvailability) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Kusto/clusters/{clusterName}/checkNameAvailability |  |
| [**databasesCreateOrUpdate**](DatabasesApi.md#databasesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Kusto/clusters/{clusterName}/databases/{databaseName} |  |
| [**databasesDelete**](DatabasesApi.md#databasesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Kusto/clusters/{clusterName}/databases/{databaseName} |  |
| [**databasesGet**](DatabasesApi.md#databasesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Kusto/clusters/{clusterName}/databases/{databaseName} |  |
| [**databasesListByCluster**](DatabasesApi.md#databasesListByCluster) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Kusto/clusters/{clusterName}/databases |  |
| [**databasesListPrincipals**](DatabasesApi.md#databasesListPrincipals) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Kusto/clusters/{clusterName}/databases/{databaseName}/listPrincipals |  |
| [**databasesRemovePrincipals**](DatabasesApi.md#databasesRemovePrincipals) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Kusto/clusters/{clusterName}/databases/{databaseName}/removePrincipals |  |
| [**databasesUpdate**](DatabasesApi.md#databasesUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Kusto/clusters/{clusterName}/databases/{databaseName} |  |


<a id="databasesAddPrincipals"></a>
# **databasesAddPrincipals**
> DatabasePrincipalListResult databasesAddPrincipals(resourceGroupName, clusterName, databaseName, subscriptionId, apiVersion, databasePrincipalsToAdd)



Add Database principals permissions.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DatabasesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    DatabasesApi apiInstance = new DatabasesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group containing the Kusto cluster.
    String clusterName = "clusterName_example"; // String | The name of the Kusto cluster.
    String databaseName = "databaseName_example"; // String | The name of the database in the Kusto cluster.
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String apiVersion = "apiVersion_example"; // String | Client API Version.
    DatabasePrincipalListRequest databasePrincipalsToAdd = new DatabasePrincipalListRequest(); // DatabasePrincipalListRequest | List of database principals to add.
    try {
      DatabasePrincipalListResult result = apiInstance.databasesAddPrincipals(resourceGroupName, clusterName, databaseName, subscriptionId, apiVersion, databasePrincipalsToAdd);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DatabasesApi#databasesAddPrincipals");
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
| **databasePrincipalsToAdd** | [**DatabasePrincipalListRequest**](DatabasePrincipalListRequest.md)| List of database principals to add. | |

### Return type

[**DatabasePrincipalListResult**](DatabasePrincipalListResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK -- Successfully added the list of database principals. Returns the updated list of principals. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="databasesCheckNameAvailability"></a>
# **databasesCheckNameAvailability**
> CheckNameResult databasesCheckNameAvailability(resourceGroupName, clusterName, apiVersion, subscriptionId, resourceName)



Checks that the database name is valid and is not already in use.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DatabasesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    DatabasesApi apiInstance = new DatabasesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group containing the Kusto cluster.
    String clusterName = "clusterName_example"; // String | The name of the Kusto cluster.
    String apiVersion = "apiVersion_example"; // String | Client API Version.
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    CheckNameRequest resourceName = new CheckNameRequest(); // CheckNameRequest | The name of the resource.
    try {
      CheckNameResult result = apiInstance.databasesCheckNameAvailability(resourceGroupName, clusterName, apiVersion, subscriptionId, resourceName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DatabasesApi#databasesCheckNameAvailability");
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
| **apiVersion** | **String**| Client API Version. | |
| **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **resourceName** | [**CheckNameRequest**](CheckNameRequest.md)| The name of the resource. | |

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
| **200** | OK -- Operation to check the kusto resource name availability was successful. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="databasesCreateOrUpdate"></a>
# **databasesCreateOrUpdate**
> Database databasesCreateOrUpdate(resourceGroupName, clusterName, databaseName, subscriptionId, apiVersion, parameters)



Creates or updates a database.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DatabasesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    DatabasesApi apiInstance = new DatabasesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group containing the Kusto cluster.
    String clusterName = "clusterName_example"; // String | The name of the Kusto cluster.
    String databaseName = "databaseName_example"; // String | The name of the database in the Kusto cluster.
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String apiVersion = "apiVersion_example"; // String | Client API Version.
    Database parameters = new Database(); // Database | The database parameters supplied to the CreateOrUpdate operation.
    try {
      Database result = apiInstance.databasesCreateOrUpdate(resourceGroupName, clusterName, databaseName, subscriptionId, apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DatabasesApi#databasesCreateOrUpdate");
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
| **parameters** | [**Database**](Database.md)| The database parameters supplied to the CreateOrUpdate operation. | |

### Return type

[**Database**](Database.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully updated the database. |  -  |
| **201** | Successfully created the database. |  -  |
| **202** | Accepted the create database request. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="databasesDelete"></a>
# **databasesDelete**
> databasesDelete(resourceGroupName, clusterName, databaseName, subscriptionId, apiVersion)



Deletes the database with the given name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DatabasesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    DatabasesApi apiInstance = new DatabasesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group containing the Kusto cluster.
    String clusterName = "clusterName_example"; // String | The name of the Kusto cluster.
    String databaseName = "databaseName_example"; // String | The name of the database in the Kusto cluster.
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String apiVersion = "apiVersion_example"; // String | Client API Version.
    try {
      apiInstance.databasesDelete(resourceGroupName, clusterName, databaseName, subscriptionId, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling DatabasesApi#databasesDelete");
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

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully deleted the database. |  -  |
| **202** | Accepted. |  -  |
| **204** | The specified database does not exist. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="databasesGet"></a>
# **databasesGet**
> Database databasesGet(resourceGroupName, clusterName, databaseName, subscriptionId, apiVersion)



Returns a database.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DatabasesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    DatabasesApi apiInstance = new DatabasesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group containing the Kusto cluster.
    String clusterName = "clusterName_example"; // String | The name of the Kusto cluster.
    String databaseName = "databaseName_example"; // String | The name of the database in the Kusto cluster.
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String apiVersion = "apiVersion_example"; // String | Client API Version.
    try {
      Database result = apiInstance.databasesGet(resourceGroupName, clusterName, databaseName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DatabasesApi#databasesGet");
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

[**Database**](Database.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully retrieved the specified database. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="databasesListByCluster"></a>
# **databasesListByCluster**
> DatabaseListResult databasesListByCluster(resourceGroupName, clusterName, subscriptionId, apiVersion)



Returns the list of databases of the given Kusto cluster.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DatabasesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    DatabasesApi apiInstance = new DatabasesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group containing the Kusto cluster.
    String clusterName = "clusterName_example"; // String | The name of the Kusto cluster.
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String apiVersion = "apiVersion_example"; // String | Client API Version.
    try {
      DatabaseListResult result = apiInstance.databasesListByCluster(resourceGroupName, clusterName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DatabasesApi#databasesListByCluster");
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
| **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **apiVersion** | **String**| Client API Version. | |

### Return type

[**DatabaseListResult**](DatabaseListResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully retrieved the list of databases. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="databasesListPrincipals"></a>
# **databasesListPrincipals**
> DatabasePrincipalListResult databasesListPrincipals(resourceGroupName, clusterName, databaseName, subscriptionId, apiVersion)



Returns a list of database principals of the given Kusto cluster and database.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DatabasesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    DatabasesApi apiInstance = new DatabasesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group containing the Kusto cluster.
    String clusterName = "clusterName_example"; // String | The name of the Kusto cluster.
    String databaseName = "databaseName_example"; // String | The name of the database in the Kusto cluster.
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String apiVersion = "apiVersion_example"; // String | Client API Version.
    try {
      DatabasePrincipalListResult result = apiInstance.databasesListPrincipals(resourceGroupName, clusterName, databaseName, subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DatabasesApi#databasesListPrincipals");
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

[**DatabasePrincipalListResult**](DatabasePrincipalListResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully retrieved the list of database principals. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="databasesRemovePrincipals"></a>
# **databasesRemovePrincipals**
> DatabasePrincipalListResult databasesRemovePrincipals(resourceGroupName, clusterName, databaseName, subscriptionId, apiVersion, databasePrincipalsToRemove)



Remove Database principals permissions.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DatabasesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    DatabasesApi apiInstance = new DatabasesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group containing the Kusto cluster.
    String clusterName = "clusterName_example"; // String | The name of the Kusto cluster.
    String databaseName = "databaseName_example"; // String | The name of the database in the Kusto cluster.
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String apiVersion = "apiVersion_example"; // String | Client API Version.
    DatabasePrincipalListRequest databasePrincipalsToRemove = new DatabasePrincipalListRequest(); // DatabasePrincipalListRequest | List of database principals to remove.
    try {
      DatabasePrincipalListResult result = apiInstance.databasesRemovePrincipals(resourceGroupName, clusterName, databaseName, subscriptionId, apiVersion, databasePrincipalsToRemove);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DatabasesApi#databasesRemovePrincipals");
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
| **databasePrincipalsToRemove** | [**DatabasePrincipalListRequest**](DatabasePrincipalListRequest.md)| List of database principals to remove. | |

### Return type

[**DatabasePrincipalListResult**](DatabasePrincipalListResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK -- Successfully removed the list of database principals. Returns the updated list of principals. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="databasesUpdate"></a>
# **databasesUpdate**
> Database databasesUpdate(resourceGroupName, clusterName, databaseName, subscriptionId, apiVersion, parameters)



Updates a database.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DatabasesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    DatabasesApi apiInstance = new DatabasesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group containing the Kusto cluster.
    String clusterName = "clusterName_example"; // String | The name of the Kusto cluster.
    String databaseName = "databaseName_example"; // String | The name of the database in the Kusto cluster.
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String apiVersion = "apiVersion_example"; // String | Client API Version.
    Database parameters = new Database(); // Database | The database parameters supplied to the Update operation.
    try {
      Database result = apiInstance.databasesUpdate(resourceGroupName, clusterName, databaseName, subscriptionId, apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DatabasesApi#databasesUpdate");
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
| **parameters** | [**Database**](Database.md)| The database parameters supplied to the Update operation. | |

### Return type

[**Database**](Database.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully updated the database. |  -  |
| **201** | Successfully updated the database. |  -  |
| **202** | Accepted the update database request. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

