# TransparentDataEncryptionApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**transparentDataEncryptionActivitiesListByConfiguration**](TransparentDataEncryptionApi.md#transparentDataEncryptionActivitiesListByConfiguration) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/databases/{databaseName}/transparentDataEncryption/{transparentDataEncryptionName}/operationResults |  |
| [**transparentDataEncryptionsCreateOrUpdate**](TransparentDataEncryptionApi.md#transparentDataEncryptionsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/databases/{databaseName}/transparentDataEncryption/{transparentDataEncryptionName} |  |
| [**transparentDataEncryptionsGet**](TransparentDataEncryptionApi.md#transparentDataEncryptionsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/databases/{databaseName}/transparentDataEncryption/{transparentDataEncryptionName} |  |


<a id="transparentDataEncryptionActivitiesListByConfiguration"></a>
# **transparentDataEncryptionActivitiesListByConfiguration**
> TransparentDataEncryptionActivityListResult transparentDataEncryptionActivitiesListByConfiguration(apiVersion, subscriptionId, resourceGroupName, serverName, databaseName, transparentDataEncryptionName)



Returns a database&#39;s transparent data encryption operation result.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransparentDataEncryptionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    TransparentDataEncryptionApi apiInstance = new TransparentDataEncryptionApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String serverName = "serverName_example"; // String | The name of the server.
    String databaseName = "databaseName_example"; // String | The name of the database for which the transparent data encryption applies.
    String transparentDataEncryptionName = "current"; // String | The name of the transparent data encryption configuration.
    try {
      TransparentDataEncryptionActivityListResult result = apiInstance.transparentDataEncryptionActivitiesListByConfiguration(apiVersion, subscriptionId, resourceGroupName, serverName, databaseName, transparentDataEncryptionName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransparentDataEncryptionApi#transparentDataEncryptionActivitiesListByConfiguration");
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
| **databaseName** | **String**| The name of the database for which the transparent data encryption applies. | |
| **transparentDataEncryptionName** | **String**| The name of the transparent data encryption configuration. | [enum: current] |

### Return type

[**TransparentDataEncryptionActivityListResult**](TransparentDataEncryptionActivityListResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="transparentDataEncryptionsCreateOrUpdate"></a>
# **transparentDataEncryptionsCreateOrUpdate**
> TransparentDataEncryption transparentDataEncryptionsCreateOrUpdate(apiVersion, subscriptionId, resourceGroupName, serverName, databaseName, transparentDataEncryptionName, parameters)



Creates or updates a database&#39;s transparent data encryption configuration.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransparentDataEncryptionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    TransparentDataEncryptionApi apiInstance = new TransparentDataEncryptionApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String serverName = "serverName_example"; // String | The name of the server.
    String databaseName = "databaseName_example"; // String | The name of the database for which setting the transparent data encryption applies.
    String transparentDataEncryptionName = "current"; // String | The name of the transparent data encryption configuration.
    TransparentDataEncryption parameters = new TransparentDataEncryption(); // TransparentDataEncryption | The required parameters for creating or updating transparent data encryption.
    try {
      TransparentDataEncryption result = apiInstance.transparentDataEncryptionsCreateOrUpdate(apiVersion, subscriptionId, resourceGroupName, serverName, databaseName, transparentDataEncryptionName, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransparentDataEncryptionApi#transparentDataEncryptionsCreateOrUpdate");
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
| **databaseName** | **String**| The name of the database for which setting the transparent data encryption applies. | |
| **transparentDataEncryptionName** | **String**| The name of the transparent data encryption configuration. | [enum: current] |
| **parameters** | [**TransparentDataEncryption**](TransparentDataEncryption.md)| The required parameters for creating or updating transparent data encryption. | |

### Return type

[**TransparentDataEncryption**](TransparentDataEncryption.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **201** | Created |  -  |

<a id="transparentDataEncryptionsGet"></a>
# **transparentDataEncryptionsGet**
> TransparentDataEncryption transparentDataEncryptionsGet(apiVersion, subscriptionId, resourceGroupName, serverName, databaseName, transparentDataEncryptionName)



Gets a database&#39;s transparent data encryption configuration.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransparentDataEncryptionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    TransparentDataEncryptionApi apiInstance = new TransparentDataEncryptionApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String serverName = "serverName_example"; // String | The name of the server.
    String databaseName = "databaseName_example"; // String | The name of the database for which the transparent data encryption applies.
    String transparentDataEncryptionName = "current"; // String | The name of the transparent data encryption configuration.
    try {
      TransparentDataEncryption result = apiInstance.transparentDataEncryptionsGet(apiVersion, subscriptionId, resourceGroupName, serverName, databaseName, transparentDataEncryptionName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransparentDataEncryptionApi#transparentDataEncryptionsGet");
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
| **databaseName** | **String**| The name of the database for which the transparent data encryption applies. | |
| **transparentDataEncryptionName** | **String**| The name of the transparent data encryption configuration. | [enum: current] |

### Return type

[**TransparentDataEncryption**](TransparentDataEncryption.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

