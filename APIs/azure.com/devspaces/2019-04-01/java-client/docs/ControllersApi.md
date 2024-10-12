# ControllersApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**controllersCreate**](ControllersApi.md#controllersCreate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevSpaces/controllers/{name} | Creates an Azure Dev Spaces Controller. |
| [**controllersDelete**](ControllersApi.md#controllersDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevSpaces/controllers/{name} | Deletes an Azure Dev Spaces Controller. |
| [**controllersGet**](ControllersApi.md#controllersGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevSpaces/controllers/{name} | Gets an Azure Dev Spaces Controller. |
| [**controllersList**](ControllersApi.md#controllersList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.DevSpaces/controllers | Lists the Azure Dev Spaces Controllers in a subscription. |
| [**controllersListByResourceGroup**](ControllersApi.md#controllersListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevSpaces/controllers | Lists the Azure Dev Spaces Controllers in a resource group. |
| [**controllersListConnectionDetails**](ControllersApi.md#controllersListConnectionDetails) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevSpaces/controllers/{name}/listConnectionDetails | Lists connection details for an Azure Dev Spaces Controller. |
| [**controllersUpdate**](ControllersApi.md#controllersUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevSpaces/controllers/{name} | Updates an Azure Dev Spaces Controller. |


<a id="controllersCreate"></a>
# **controllersCreate**
> Controller controllersCreate(apiVersion, subscriptionId, resourceGroupName, name, controller)

Creates an Azure Dev Spaces Controller.

Creates an Azure Dev Spaces Controller with the specified create parameters.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ControllersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    ControllersApi apiInstance = new ControllersApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Resource group to which the resource belongs.
    String name = "name_example"; // String | Name of the resource.
    Controller controller = new Controller(); // Controller | Controller create parameters.
    try {
      Controller result = apiInstance.controllersCreate(apiVersion, subscriptionId, resourceGroupName, name, controller);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ControllersApi#controllersCreate");
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
| **apiVersion** | **String**| Client API version. | |
| **subscriptionId** | **String**| Azure subscription ID. | |
| **resourceGroupName** | **String**| Resource group to which the resource belongs. | |
| **name** | **String**| Name of the resource. | |
| **controller** | [**Controller**](Controller.md)| Controller create parameters. | |

### Return type

[**Controller**](Controller.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The request was successful; response contains the created Azure Dev Spaces Controller . |  -  |
| **201** | The request was successful; Azure Dev Spaces Controller is being created. |  -  |
| **0** | Error response describing the reason for operation failure. 400 - BadRequest(One or more creation parameters are invalid.), 409 - Conflict(Target container host is not in a supported state.) |  -  |

<a id="controllersDelete"></a>
# **controllersDelete**
> controllersDelete(apiVersion, subscriptionId, resourceGroupName, name)

Deletes an Azure Dev Spaces Controller.

Deletes an existing Azure Dev Spaces Controller.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ControllersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    ControllersApi apiInstance = new ControllersApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Resource group to which the resource belongs.
    String name = "name_example"; // String | Name of the resource.
    try {
      apiInstance.controllersDelete(apiVersion, subscriptionId, resourceGroupName, name);
    } catch (ApiException e) {
      System.err.println("Exception when calling ControllersApi#controllersDelete");
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
| **apiVersion** | **String**| Client API version. | |
| **subscriptionId** | **String**| Azure subscription ID. | |
| **resourceGroupName** | **String**| Resource group to which the resource belongs. | |
| **name** | **String**| Name of the resource. | |

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
| **200** | The request was successful; the Azure Dev Spaces Controller is deleted. |  -  |
| **202** | The request was successful; Azure Dev Spaces Controller is being deleted. |  -  |
| **204** | The request was successful; Azure Dev Spaces Controller does not exist. |  -  |
| **0** | Error response describing the reason for operation failure. 409 - Conflict(Azure Dev Spaces Controller is in a non-terminal state due to an ongoing operation.) |  -  |

<a id="controllersGet"></a>
# **controllersGet**
> Controller controllersGet(apiVersion, subscriptionId, resourceGroupName, name)

Gets an Azure Dev Spaces Controller.

Gets the properties for an Azure Dev Spaces Controller.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ControllersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    ControllersApi apiInstance = new ControllersApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Resource group to which the resource belongs.
    String name = "name_example"; // String | Name of the resource.
    try {
      Controller result = apiInstance.controllersGet(apiVersion, subscriptionId, resourceGroupName, name);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ControllersApi#controllersGet");
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
| **apiVersion** | **String**| Client API version. | |
| **subscriptionId** | **String**| Azure subscription ID. | |
| **resourceGroupName** | **String**| Resource group to which the resource belongs. | |
| **name** | **String**| Name of the resource. | |

### Return type

[**Controller**](Controller.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The request was successful; response contains the Azure Dev Spaces Controller. |  -  |
| **0** | Error response describing the reason for operation failure. 404 - NotFound(Azure Dev Spaces Controller doesn&#39;t exist.) |  -  |

<a id="controllersList"></a>
# **controllersList**
> ControllerList controllersList(apiVersion, subscriptionId)

Lists the Azure Dev Spaces Controllers in a subscription.

Lists all the Azure Dev Spaces Controllers with their properties in the subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ControllersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    ControllersApi apiInstance = new ControllersApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
    try {
      ControllerList result = apiInstance.controllersList(apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ControllersApi#controllersList");
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
| **apiVersion** | **String**| Client API version. | |
| **subscriptionId** | **String**| Azure subscription ID. | |

### Return type

[**ControllerList**](ControllerList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The request was successful; response contains the list of Azure Dev Spaces Controllers in the subscription. |  -  |
| **0** | Error response describing the reason for operation failure. |  -  |

<a id="controllersListByResourceGroup"></a>
# **controllersListByResourceGroup**
> ControllerList controllersListByResourceGroup(apiVersion, subscriptionId, resourceGroupName)

Lists the Azure Dev Spaces Controllers in a resource group.

Lists all the Azure Dev Spaces Controllers with their properties in the specified resource group and subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ControllersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    ControllersApi apiInstance = new ControllersApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Resource group to which the resource belongs.
    try {
      ControllerList result = apiInstance.controllersListByResourceGroup(apiVersion, subscriptionId, resourceGroupName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ControllersApi#controllersListByResourceGroup");
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
| **apiVersion** | **String**| Client API version. | |
| **subscriptionId** | **String**| Azure subscription ID. | |
| **resourceGroupName** | **String**| Resource group to which the resource belongs. | |

### Return type

[**ControllerList**](ControllerList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The request was successful; response contains the list of Azure Dev Spaces Controllers in the resource group. |  -  |
| **0** | Error response describing the reason for operation failure. |  -  |

<a id="controllersListConnectionDetails"></a>
# **controllersListConnectionDetails**
> ControllerConnectionDetailsList controllersListConnectionDetails(apiVersion, subscriptionId, resourceGroupName, name, listConnectionDetailsParameters)

Lists connection details for an Azure Dev Spaces Controller.

Lists connection details for the underlying container resources of an Azure Dev Spaces Controller.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ControllersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    ControllersApi apiInstance = new ControllersApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Resource group to which the resource belongs.
    String name = "name_example"; // String | Name of the resource.
    ListConnectionDetailsParameters listConnectionDetailsParameters = new ListConnectionDetailsParameters(); // ListConnectionDetailsParameters | Parameters for listing connection details of Azure Dev Spaces Controller.
    try {
      ControllerConnectionDetailsList result = apiInstance.controllersListConnectionDetails(apiVersion, subscriptionId, resourceGroupName, name, listConnectionDetailsParameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ControllersApi#controllersListConnectionDetails");
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
| **apiVersion** | **String**| Client API version. | |
| **subscriptionId** | **String**| Azure subscription ID. | |
| **resourceGroupName** | **String**| Resource group to which the resource belongs. | |
| **name** | **String**| Name of the resource. | |
| **listConnectionDetailsParameters** | [**ListConnectionDetailsParameters**](ListConnectionDetailsParameters.md)| Parameters for listing connection details of Azure Dev Spaces Controller. | |

### Return type

[**ControllerConnectionDetailsList**](ControllerConnectionDetailsList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The request was successful; response contains the list of connection details for the Azure Dev Spaces Controller . |  -  |
| **0** | Error response describing the reason for operation failure. 404 - NotFound(Azure Dev Spaces Controller doesn&#39;t exist.) |  -  |

<a id="controllersUpdate"></a>
# **controllersUpdate**
> Controller controllersUpdate(apiVersion, subscriptionId, resourceGroupName, name, controllerUpdateParameters)

Updates an Azure Dev Spaces Controller.

Updates the properties of an existing Azure Dev Spaces Controller with the specified update parameters.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ControllersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    ControllersApi apiInstance = new ControllersApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client API version.
    String subscriptionId = "subscriptionId_example"; // String | Azure subscription ID.
    String resourceGroupName = "resourceGroupName_example"; // String | Resource group to which the resource belongs.
    String name = "name_example"; // String | Name of the resource.
    ControllerUpdateParameters controllerUpdateParameters = new ControllerUpdateParameters(); // ControllerUpdateParameters | Parameters for updating the Azure Dev Spaces Controller.
    try {
      Controller result = apiInstance.controllersUpdate(apiVersion, subscriptionId, resourceGroupName, name, controllerUpdateParameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ControllersApi#controllersUpdate");
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
| **apiVersion** | **String**| Client API version. | |
| **subscriptionId** | **String**| Azure subscription ID. | |
| **resourceGroupName** | **String**| Resource group to which the resource belongs. | |
| **name** | **String**| Name of the resource. | |
| **controllerUpdateParameters** | [**ControllerUpdateParameters**](ControllerUpdateParameters.md)| Parameters for updating the Azure Dev Spaces Controller. | |

### Return type

[**Controller**](Controller.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The request was successful; response contains the updated Azure Dev Spaces Controller . |  -  |
| **201** | The request was successful; Azure Dev Spaces Controller is being updated. |  -  |
| **0** | Error response describing the reason for operation failure. 404 - NotFound(Azure Dev Spaces Controller doesn&#39;t exist.), 400 - BadRequest(One or more update parameters are invalid.) |  -  |

