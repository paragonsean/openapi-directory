# ImportExportApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**databasesCreateImportOperation**](ImportExportApi.md#databasesCreateImportOperation) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/databases/{databaseName}/extensions/{extensionName} |  |
| [**databasesExport**](ImportExportApi.md#databasesExport) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/databases/{databaseName}/export |  |
| [**databasesImport**](ImportExportApi.md#databasesImport) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/import |  |


<a id="databasesCreateImportOperation"></a>
# **databasesCreateImportOperation**
> ImportExportResponse databasesCreateImportOperation(apiVersion, subscriptionId, resourceGroupName, serverName, databaseName, extensionName, parameters)



Creates an import operation that imports a bacpac into an existing database. The existing database must be empty.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ImportExportApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    ImportExportApi apiInstance = new ImportExportApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String serverName = "serverName_example"; // String | The name of the server.
    String databaseName = "databaseName_example"; // String | The name of the database to import into
    String extensionName = "import"; // String | The name of the operation to perform
    ImportExtensionRequest parameters = new ImportExtensionRequest(); // ImportExtensionRequest | The required parameters for importing a Bacpac into a database.
    try {
      ImportExportResponse result = apiInstance.databasesCreateImportOperation(apiVersion, subscriptionId, resourceGroupName, serverName, databaseName, extensionName, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImportExportApi#databasesCreateImportOperation");
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
| **apiVersion** | **String**| The API version to use for the request. | |
| **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | |
| **resourceGroupName** | **String**| The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. | |
| **serverName** | **String**| The name of the server. | |
| **databaseName** | **String**| The name of the database to import into | |
| **extensionName** | **String**| The name of the operation to perform | [enum: import] |
| **parameters** | [**ImportExtensionRequest**](ImportExtensionRequest.md)| The required parameters for importing a Bacpac into a database. | |

### Return type

[**ImportExportResponse**](ImportExportResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | OK |  -  |
| **202** | Accepted |  -  |

<a id="databasesExport"></a>
# **databasesExport**
> ImportExportResponse databasesExport(apiVersion, subscriptionId, resourceGroupName, serverName, databaseName, parameters)



Exports a database to a bacpac.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ImportExportApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    ImportExportApi apiInstance = new ImportExportApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String serverName = "serverName_example"; // String | The name of the server.
    String databaseName = "databaseName_example"; // String | The name of the database to be exported.
    ExportRequest parameters = new ExportRequest(); // ExportRequest | The required parameters for exporting a database.
    try {
      ImportExportResponse result = apiInstance.databasesExport(apiVersion, subscriptionId, resourceGroupName, serverName, databaseName, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImportExportApi#databasesExport");
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
| **apiVersion** | **String**| The API version to use for the request. | |
| **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | |
| **resourceGroupName** | **String**| The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. | |
| **serverName** | **String**| The name of the server. | |
| **databaseName** | **String**| The name of the database to be exported. | |
| **parameters** | [**ExportRequest**](ExportRequest.md)| The required parameters for exporting a database. | |

### Return type

[**ImportExportResponse**](ImportExportResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **202** | Accepted |  -  |

<a id="databasesImport"></a>
# **databasesImport**
> ImportExportResponse databasesImport(apiVersion, subscriptionId, resourceGroupName, serverName, parameters)



Imports a bacpac into a new database. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ImportExportApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    ImportExportApi apiInstance = new ImportExportApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String serverName = "serverName_example"; // String | The name of the server.
    ImportRequest parameters = new ImportRequest(); // ImportRequest | The required parameters for importing a Bacpac into a database.
    try {
      ImportExportResponse result = apiInstance.databasesImport(apiVersion, subscriptionId, resourceGroupName, serverName, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImportExportApi#databasesImport");
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
| **apiVersion** | **String**| The API version to use for the request. | |
| **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | |
| **resourceGroupName** | **String**| The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. | |
| **serverName** | **String**| The name of the server. | |
| **parameters** | [**ImportRequest**](ImportRequest.md)| The required parameters for importing a Bacpac into a database. | |

### Return type

[**ImportExportResponse**](ImportExportResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **202** | Accepted |  -  |

