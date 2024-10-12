# DataFlowDebugSessionApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**dataFlowDebugSessionAddDataFlow**](DataFlowDebugSessionApi.md#dataFlowDebugSessionAddDataFlow) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}/addDataFlowToDebugSession |  |
| [**dataFlowDebugSessionCreate**](DataFlowDebugSessionApi.md#dataFlowDebugSessionCreate) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}/createDataFlowDebugSession |  |
| [**dataFlowDebugSessionDelete**](DataFlowDebugSessionApi.md#dataFlowDebugSessionDelete) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}/deleteDataFlowDebugSession |  |
| [**dataFlowDebugSessionExecuteCommand**](DataFlowDebugSessionApi.md#dataFlowDebugSessionExecuteCommand) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}/executeDataFlowDebugCommand |  |
| [**dataFlowDebugSessionQueryByFactory**](DataFlowDebugSessionApi.md#dataFlowDebugSessionQueryByFactory) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}/queryDataFlowDebugSessions |  |


<a id="dataFlowDebugSessionAddDataFlow"></a>
# **dataFlowDebugSessionAddDataFlow**
> AddDataFlowToDebugSessionResponse dataFlowDebugSessionAddDataFlow(subscriptionId, resourceGroupName, factoryName, apiVersion, request)



Add a data flow into debug session.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DataFlowDebugSessionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DataFlowDebugSessionApi apiInstance = new DataFlowDebugSessionApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String factoryName = "factoryName_example"; // String | The factory name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    DataFlowDebugPackage request = new DataFlowDebugPackage(); // DataFlowDebugPackage | Data flow debug session definition with debug content.
    try {
      AddDataFlowToDebugSessionResponse result = apiInstance.dataFlowDebugSessionAddDataFlow(subscriptionId, resourceGroupName, factoryName, apiVersion, request);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DataFlowDebugSessionApi#dataFlowDebugSessionAddDataFlow");
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
| **subscriptionId** | **String**| The subscription identifier. | |
| **resourceGroupName** | **String**| The resource group name. | |
| **factoryName** | **String**| The factory name. | |
| **apiVersion** | **String**| The API version. | |
| **request** | [**DataFlowDebugPackage**](DataFlowDebugPackage.md)| Data flow debug session definition with debug content. | |

### Return type

[**AddDataFlowToDebugSessionResponse**](AddDataFlowToDebugSessionResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. |  -  |
| **0** | An error response received from the Azure Data Factory service. |  -  |

<a id="dataFlowDebugSessionCreate"></a>
# **dataFlowDebugSessionCreate**
> CreateDataFlowDebugSessionResponse dataFlowDebugSessionCreate(subscriptionId, resourceGroupName, factoryName, apiVersion, request)



Creates a data flow debug session.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DataFlowDebugSessionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DataFlowDebugSessionApi apiInstance = new DataFlowDebugSessionApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String factoryName = "factoryName_example"; // String | The factory name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    CreateDataFlowDebugSessionRequest request = new CreateDataFlowDebugSessionRequest(); // CreateDataFlowDebugSessionRequest | Data flow debug session definition
    try {
      CreateDataFlowDebugSessionResponse result = apiInstance.dataFlowDebugSessionCreate(subscriptionId, resourceGroupName, factoryName, apiVersion, request);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DataFlowDebugSessionApi#dataFlowDebugSessionCreate");
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
| **subscriptionId** | **String**| The subscription identifier. | |
| **resourceGroupName** | **String**| The resource group name. | |
| **factoryName** | **String**| The factory name. | |
| **apiVersion** | **String**| The API version. | |
| **request** | [**CreateDataFlowDebugSessionRequest**](CreateDataFlowDebugSessionRequest.md)| Data flow debug session definition | |

### Return type

[**CreateDataFlowDebugSessionResponse**](CreateDataFlowDebugSessionResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. |  -  |
| **202** | Accepted. |  * location - URI to poll for asynchronous operation status. <br>  |
| **0** | An error response received from the Azure Data Factory service. |  -  |

<a id="dataFlowDebugSessionDelete"></a>
# **dataFlowDebugSessionDelete**
> dataFlowDebugSessionDelete(subscriptionId, resourceGroupName, factoryName, apiVersion, request)



Deletes a data flow debug session.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DataFlowDebugSessionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DataFlowDebugSessionApi apiInstance = new DataFlowDebugSessionApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String factoryName = "factoryName_example"; // String | The factory name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    DeleteDataFlowDebugSessionRequest request = new DeleteDataFlowDebugSessionRequest(); // DeleteDataFlowDebugSessionRequest | Data flow debug session definition for deletion
    try {
      apiInstance.dataFlowDebugSessionDelete(subscriptionId, resourceGroupName, factoryName, apiVersion, request);
    } catch (ApiException e) {
      System.err.println("Exception when calling DataFlowDebugSessionApi#dataFlowDebugSessionDelete");
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
| **subscriptionId** | **String**| The subscription identifier. | |
| **resourceGroupName** | **String**| The resource group name. | |
| **factoryName** | **String**| The factory name. | |
| **apiVersion** | **String**| The API version. | |
| **request** | [**DeleteDataFlowDebugSessionRequest**](DeleteDataFlowDebugSessionRequest.md)| Data flow debug session definition for deletion | |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. |  -  |
| **0** | An error response received from the Azure Data Factory service. |  -  |

<a id="dataFlowDebugSessionExecuteCommand"></a>
# **dataFlowDebugSessionExecuteCommand**
> DataFlowDebugCommandResponse dataFlowDebugSessionExecuteCommand(subscriptionId, resourceGroupName, factoryName, apiVersion, request)



Execute a data flow debug command.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DataFlowDebugSessionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DataFlowDebugSessionApi apiInstance = new DataFlowDebugSessionApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String factoryName = "factoryName_example"; // String | The factory name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    DataFlowDebugCommandRequest request = new DataFlowDebugCommandRequest(); // DataFlowDebugCommandRequest | Data flow debug command definition.
    try {
      DataFlowDebugCommandResponse result = apiInstance.dataFlowDebugSessionExecuteCommand(subscriptionId, resourceGroupName, factoryName, apiVersion, request);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DataFlowDebugSessionApi#dataFlowDebugSessionExecuteCommand");
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
| **subscriptionId** | **String**| The subscription identifier. | |
| **resourceGroupName** | **String**| The resource group name. | |
| **factoryName** | **String**| The factory name. | |
| **apiVersion** | **String**| The API version. | |
| **request** | [**DataFlowDebugCommandRequest**](DataFlowDebugCommandRequest.md)| Data flow debug command definition. | |

### Return type

[**DataFlowDebugCommandResponse**](DataFlowDebugCommandResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. |  -  |
| **202** | Accepted. |  * location - URI to poll for asynchronous operation status. <br>  |
| **0** | An error response received from the Azure Data Factory service. |  -  |

<a id="dataFlowDebugSessionQueryByFactory"></a>
# **dataFlowDebugSessionQueryByFactory**
> QueryDataFlowDebugSessionsResponse dataFlowDebugSessionQueryByFactory(subscriptionId, resourceGroupName, factoryName, apiVersion)



Query all active data flow debug sessions.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DataFlowDebugSessionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DataFlowDebugSessionApi apiInstance = new DataFlowDebugSessionApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String factoryName = "factoryName_example"; // String | The factory name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    try {
      QueryDataFlowDebugSessionsResponse result = apiInstance.dataFlowDebugSessionQueryByFactory(subscriptionId, resourceGroupName, factoryName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DataFlowDebugSessionApi#dataFlowDebugSessionQueryByFactory");
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
| **subscriptionId** | **String**| The subscription identifier. | |
| **resourceGroupName** | **String**| The resource group name. | |
| **factoryName** | **String**| The factory name. | |
| **apiVersion** | **String**| The API version. | |

### Return type

[**QueryDataFlowDebugSessionsResponse**](QueryDataFlowDebugSessionsResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. |  -  |
| **0** | An error response received from the Azure Data Factory service. |  -  |

