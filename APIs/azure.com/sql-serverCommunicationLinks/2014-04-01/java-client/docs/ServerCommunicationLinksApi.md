# ServerCommunicationLinksApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**serverCommunicationLinksCreateOrUpdate**](ServerCommunicationLinksApi.md#serverCommunicationLinksCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/communicationLinks/{communicationLinkName} |  |
| [**serverCommunicationLinksDelete**](ServerCommunicationLinksApi.md#serverCommunicationLinksDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/communicationLinks/{communicationLinkName} |  |
| [**serverCommunicationLinksGet**](ServerCommunicationLinksApi.md#serverCommunicationLinksGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/communicationLinks/{communicationLinkName} |  |
| [**serverCommunicationLinksListByServer**](ServerCommunicationLinksApi.md#serverCommunicationLinksListByServer) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/communicationLinks |  |


<a id="serverCommunicationLinksCreateOrUpdate"></a>
# **serverCommunicationLinksCreateOrUpdate**
> ServerCommunicationLink serverCommunicationLinksCreateOrUpdate(apiVersion, subscriptionId, resourceGroupName, serverName, communicationLinkName, parameters)



Creates a server communication link.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServerCommunicationLinksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    ServerCommunicationLinksApi apiInstance = new ServerCommunicationLinksApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String serverName = "serverName_example"; // String | The name of the server.
    String communicationLinkName = "communicationLinkName_example"; // String | The name of the server communication link.
    ServerCommunicationLink parameters = new ServerCommunicationLink(); // ServerCommunicationLink | The required parameters for creating a server communication link.
    try {
      ServerCommunicationLink result = apiInstance.serverCommunicationLinksCreateOrUpdate(apiVersion, subscriptionId, resourceGroupName, serverName, communicationLinkName, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServerCommunicationLinksApi#serverCommunicationLinksCreateOrUpdate");
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
| **communicationLinkName** | **String**| The name of the server communication link. | |
| **parameters** | [**ServerCommunicationLink**](ServerCommunicationLink.md)| The required parameters for creating a server communication link. | |

### Return type

[**ServerCommunicationLink**](ServerCommunicationLink.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |
| **202** | Accepted |  -  |

<a id="serverCommunicationLinksDelete"></a>
# **serverCommunicationLinksDelete**
> serverCommunicationLinksDelete(apiVersion, subscriptionId, resourceGroupName, serverName, communicationLinkName)



Deletes a server communication link.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServerCommunicationLinksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    ServerCommunicationLinksApi apiInstance = new ServerCommunicationLinksApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String serverName = "serverName_example"; // String | The name of the server.
    String communicationLinkName = "communicationLinkName_example"; // String | The name of the server communication link.
    try {
      apiInstance.serverCommunicationLinksDelete(apiVersion, subscriptionId, resourceGroupName, serverName, communicationLinkName);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServerCommunicationLinksApi#serverCommunicationLinksDelete");
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
| **communicationLinkName** | **String**| The name of the server communication link. | |

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
| **200** | OK |  -  |

<a id="serverCommunicationLinksGet"></a>
# **serverCommunicationLinksGet**
> ServerCommunicationLink serverCommunicationLinksGet(apiVersion, subscriptionId, resourceGroupName, serverName, communicationLinkName)



Returns a server communication link.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServerCommunicationLinksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    ServerCommunicationLinksApi apiInstance = new ServerCommunicationLinksApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String serverName = "serverName_example"; // String | The name of the server.
    String communicationLinkName = "communicationLinkName_example"; // String | The name of the server communication link.
    try {
      ServerCommunicationLink result = apiInstance.serverCommunicationLinksGet(apiVersion, subscriptionId, resourceGroupName, serverName, communicationLinkName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServerCommunicationLinksApi#serverCommunicationLinksGet");
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
| **communicationLinkName** | **String**| The name of the server communication link. | |

### Return type

[**ServerCommunicationLink**](ServerCommunicationLink.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="serverCommunicationLinksListByServer"></a>
# **serverCommunicationLinksListByServer**
> ServerCommunicationLinkListResult serverCommunicationLinksListByServer(apiVersion, subscriptionId, resourceGroupName, serverName)



Gets a list of server communication links.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ServerCommunicationLinksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    ServerCommunicationLinksApi apiInstance = new ServerCommunicationLinksApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    String serverName = "serverName_example"; // String | The name of the server.
    try {
      ServerCommunicationLinkListResult result = apiInstance.serverCommunicationLinksListByServer(apiVersion, subscriptionId, resourceGroupName, serverName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ServerCommunicationLinksApi#serverCommunicationLinksListByServer");
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

### Return type

[**ServerCommunicationLinkListResult**](ServerCommunicationLinkListResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

