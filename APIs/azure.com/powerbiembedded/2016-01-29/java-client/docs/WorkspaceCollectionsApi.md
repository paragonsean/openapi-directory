# WorkspaceCollectionsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**workspaceCollectionsCheckNameAvailability**](WorkspaceCollectionsApi.md#workspaceCollectionsCheckNameAvailability) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.PowerBI/locations/{location}/checkNameAvailability |  |
| [**workspaceCollectionsCreate**](WorkspaceCollectionsApi.md#workspaceCollectionsCreate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.PowerBI/workspaceCollections/{workspaceCollectionName} |  |
| [**workspaceCollectionsDelete**](WorkspaceCollectionsApi.md#workspaceCollectionsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.PowerBI/workspaceCollections/{workspaceCollectionName} |  |
| [**workspaceCollectionsGetAccessKeys**](WorkspaceCollectionsApi.md#workspaceCollectionsGetAccessKeys) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.PowerBI/workspaceCollections/{workspaceCollectionName}/listKeys |  |
| [**workspaceCollectionsGetByName**](WorkspaceCollectionsApi.md#workspaceCollectionsGetByName) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.PowerBI/workspaceCollections/{workspaceCollectionName} |  |
| [**workspaceCollectionsListByResourceGroup**](WorkspaceCollectionsApi.md#workspaceCollectionsListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.PowerBI/workspaceCollections |  |
| [**workspaceCollectionsListBySubscription**](WorkspaceCollectionsApi.md#workspaceCollectionsListBySubscription) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.PowerBI/workspaceCollections |  |
| [**workspaceCollectionsMigrate**](WorkspaceCollectionsApi.md#workspaceCollectionsMigrate) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/moveResources |  |
| [**workspaceCollectionsRegenerateKey**](WorkspaceCollectionsApi.md#workspaceCollectionsRegenerateKey) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.PowerBI/workspaceCollections/{workspaceCollectionName}/regenerateKey |  |
| [**workspaceCollectionsUpdate**](WorkspaceCollectionsApi.md#workspaceCollectionsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.PowerBI/workspaceCollections/{workspaceCollectionName} |  |


<a id="workspaceCollectionsCheckNameAvailability"></a>
# **workspaceCollectionsCheckNameAvailability**
> CheckNameResponse workspaceCollectionsCheckNameAvailability(subscriptionId, location, apiVersion, body)



Verify the specified Power BI Workspace Collection name is valid and not already in use.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WorkspaceCollectionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    WorkspaceCollectionsApi apiInstance = new WorkspaceCollectionsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String location = "location_example"; // String | Azure location
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    CheckNameRequest body = new CheckNameRequest(); // CheckNameRequest | Check name availability request
    try {
      CheckNameResponse result = apiInstance.workspaceCollectionsCheckNameAvailability(subscriptionId, location, apiVersion, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WorkspaceCollectionsApi#workspaceCollectionsCheckNameAvailability");
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
| **subscriptionId** | **String**| Gets subscription credentials which uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **location** | **String**| Azure location | |
| **apiVersion** | **String**| Client Api Version. | |
| **body** | [**CheckNameRequest**](CheckNameRequest.md)| Check name availability request | |

### Return type

[**CheckNameResponse**](CheckNameResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Request completed successfully |  -  |
| **0** | Default Response. It will be deserialized as per the Error definition specified in the schema. Exception will be thrown. |  -  |

<a id="workspaceCollectionsCreate"></a>
# **workspaceCollectionsCreate**
> WorkspaceCollection workspaceCollectionsCreate(subscriptionId, resourceGroupName, workspaceCollectionName, apiVersion, body)



Creates a new Power BI Workspace Collection with the specified properties. A Power BI Workspace Collection contains one or more workspaces, and can be used to provision keys that provide API access to those workspaces.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WorkspaceCollectionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    WorkspaceCollectionsApi apiInstance = new WorkspaceCollectionsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | Azure resource group
    String workspaceCollectionName = "workspaceCollectionName_example"; // String | Power BI Embedded Workspace Collection name
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    CreateWorkspaceCollectionRequest body = new CreateWorkspaceCollectionRequest(); // CreateWorkspaceCollectionRequest | Create workspace collection request
    try {
      WorkspaceCollection result = apiInstance.workspaceCollectionsCreate(subscriptionId, resourceGroupName, workspaceCollectionName, apiVersion, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WorkspaceCollectionsApi#workspaceCollectionsCreate");
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
| **subscriptionId** | **String**| Gets subscription credentials which uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| Azure resource group | |
| **workspaceCollectionName** | **String**| Power BI Embedded Workspace Collection name | |
| **apiVersion** | **String**| Client Api Version. | |
| **body** | [**CreateWorkspaceCollectionRequest**](CreateWorkspaceCollectionRequest.md)| Create workspace collection request | |

### Return type

[**WorkspaceCollection**](WorkspaceCollection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Workspace collection created successfully |  -  |
| **0** | Default Response. It will be deserialized as per the Error definition specified in the schema. Exception will be thrown. |  -  |

<a id="workspaceCollectionsDelete"></a>
# **workspaceCollectionsDelete**
> workspaceCollectionsDelete(subscriptionId, resourceGroupName, workspaceCollectionName, apiVersion)



Delete a Power BI Workspace Collection.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WorkspaceCollectionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    WorkspaceCollectionsApi apiInstance = new WorkspaceCollectionsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | Azure resource group
    String workspaceCollectionName = "workspaceCollectionName_example"; // String | Power BI Embedded Workspace Collection name
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    try {
      apiInstance.workspaceCollectionsDelete(subscriptionId, resourceGroupName, workspaceCollectionName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling WorkspaceCollectionsApi#workspaceCollectionsDelete");
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
| **subscriptionId** | **String**| Gets subscription credentials which uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| Azure resource group | |
| **workspaceCollectionName** | **String**| Power BI Embedded Workspace Collection name | |
| **apiVersion** | **String**| Client Api Version. | |

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
| **202** | Workspace collection deleted successfully |  -  |
| **0** | Default Response. It will be deserialized as per the Error definition specified in the schema. Exception will be thrown. |  -  |

<a id="workspaceCollectionsGetAccessKeys"></a>
# **workspaceCollectionsGetAccessKeys**
> WorkspaceCollectionAccessKeys workspaceCollectionsGetAccessKeys(subscriptionId, resourceGroupName, workspaceCollectionName, apiVersion)



Retrieves the primary and secondary access keys for the specified Power BI Workspace Collection.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WorkspaceCollectionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    WorkspaceCollectionsApi apiInstance = new WorkspaceCollectionsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | Azure resource group
    String workspaceCollectionName = "workspaceCollectionName_example"; // String | Power BI Embedded Workspace Collection name
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    try {
      WorkspaceCollectionAccessKeys result = apiInstance.workspaceCollectionsGetAccessKeys(subscriptionId, resourceGroupName, workspaceCollectionName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WorkspaceCollectionsApi#workspaceCollectionsGetAccessKeys");
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
| **subscriptionId** | **String**| Gets subscription credentials which uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| Azure resource group | |
| **workspaceCollectionName** | **String**| Power BI Embedded Workspace Collection name | |
| **apiVersion** | **String**| Client Api Version. | |

### Return type

[**WorkspaceCollectionAccessKeys**](WorkspaceCollectionAccessKeys.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get access keys completed successfully |  -  |
| **0** | Default Response. It will be deserialized as per the Error definition specified in the schema. Exception will be thrown. |  -  |

<a id="workspaceCollectionsGetByName"></a>
# **workspaceCollectionsGetByName**
> WorkspaceCollection workspaceCollectionsGetByName(subscriptionId, resourceGroupName, workspaceCollectionName, apiVersion)



Retrieves an existing Power BI Workspace Collection.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WorkspaceCollectionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    WorkspaceCollectionsApi apiInstance = new WorkspaceCollectionsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | Azure resource group
    String workspaceCollectionName = "workspaceCollectionName_example"; // String | Power BI Embedded Workspace Collection name
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    try {
      WorkspaceCollection result = apiInstance.workspaceCollectionsGetByName(subscriptionId, resourceGroupName, workspaceCollectionName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WorkspaceCollectionsApi#workspaceCollectionsGetByName");
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
| **subscriptionId** | **String**| Gets subscription credentials which uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| Azure resource group | |
| **workspaceCollectionName** | **String**| Power BI Embedded Workspace Collection name | |
| **apiVersion** | **String**| Client Api Version. | |

### Return type

[**WorkspaceCollection**](WorkspaceCollection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Workspace collection created successfully |  -  |
| **0** | Default Response. It will be deserialized as per the Error definition specified in the schema. Exception will be thrown. |  -  |

<a id="workspaceCollectionsListByResourceGroup"></a>
# **workspaceCollectionsListByResourceGroup**
> WorkspaceCollectionList workspaceCollectionsListByResourceGroup(subscriptionId, resourceGroupName, apiVersion)



Retrieves all existing Power BI workspace collections in the specified resource group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WorkspaceCollectionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    WorkspaceCollectionsApi apiInstance = new WorkspaceCollectionsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | Azure resource group
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    try {
      WorkspaceCollectionList result = apiInstance.workspaceCollectionsListByResourceGroup(subscriptionId, resourceGroupName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WorkspaceCollectionsApi#workspaceCollectionsListByResourceGroup");
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
| **subscriptionId** | **String**| Gets subscription credentials which uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| Azure resource group | |
| **apiVersion** | **String**| Client Api Version. | |

### Return type

[**WorkspaceCollectionList**](WorkspaceCollectionList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get workspaces response |  -  |
| **0** | Default Response. It will be deserialized as per the Error definition specified in the schema. Exception will be thrown. |  -  |

<a id="workspaceCollectionsListBySubscription"></a>
# **workspaceCollectionsListBySubscription**
> WorkspaceCollectionList workspaceCollectionsListBySubscription(subscriptionId, apiVersion)



Retrieves all existing Power BI workspace collections in the specified subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WorkspaceCollectionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    WorkspaceCollectionsApi apiInstance = new WorkspaceCollectionsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    try {
      WorkspaceCollectionList result = apiInstance.workspaceCollectionsListBySubscription(subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WorkspaceCollectionsApi#workspaceCollectionsListBySubscription");
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
| **subscriptionId** | **String**| Gets subscription credentials which uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **apiVersion** | **String**| Client Api Version. | |

### Return type

[**WorkspaceCollectionList**](WorkspaceCollectionList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get workspaces response |  -  |
| **0** | Default Response. It will be deserialized as per the Error definition specified in the schema. Exception will be thrown. |  -  |

<a id="workspaceCollectionsMigrate"></a>
# **workspaceCollectionsMigrate**
> workspaceCollectionsMigrate(subscriptionId, resourceGroupName, apiVersion, body)



Migrates an existing Power BI Workspace Collection to a different resource group and/or subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WorkspaceCollectionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    WorkspaceCollectionsApi apiInstance = new WorkspaceCollectionsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | Azure resource group
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    MigrateWorkspaceCollectionRequest body = new MigrateWorkspaceCollectionRequest(); // MigrateWorkspaceCollectionRequest | Workspace migration request
    try {
      apiInstance.workspaceCollectionsMigrate(subscriptionId, resourceGroupName, apiVersion, body);
    } catch (ApiException e) {
      System.err.println("Exception when calling WorkspaceCollectionsApi#workspaceCollectionsMigrate");
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
| **subscriptionId** | **String**| Gets subscription credentials which uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| Azure resource group | |
| **apiVersion** | **String**| Client Api Version. | |
| **body** | [**MigrateWorkspaceCollectionRequest**](MigrateWorkspaceCollectionRequest.md)| Workspace migration request | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Migration completed successfully |  -  |
| **0** | Default Response. It will be deserialized as per the Error definition specified in the schema. Exception will be thrown. |  -  |

<a id="workspaceCollectionsRegenerateKey"></a>
# **workspaceCollectionsRegenerateKey**
> WorkspaceCollectionAccessKeys workspaceCollectionsRegenerateKey(subscriptionId, resourceGroupName, workspaceCollectionName, apiVersion, body)



Regenerates the primary or secondary access key for the specified Power BI Workspace Collection.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WorkspaceCollectionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    WorkspaceCollectionsApi apiInstance = new WorkspaceCollectionsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | Azure resource group
    String workspaceCollectionName = "workspaceCollectionName_example"; // String | Power BI Embedded Workspace Collection name
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    WorkspaceCollectionAccessKey body = new WorkspaceCollectionAccessKey(); // WorkspaceCollectionAccessKey | Access key to regenerate
    try {
      WorkspaceCollectionAccessKeys result = apiInstance.workspaceCollectionsRegenerateKey(subscriptionId, resourceGroupName, workspaceCollectionName, apiVersion, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WorkspaceCollectionsApi#workspaceCollectionsRegenerateKey");
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
| **subscriptionId** | **String**| Gets subscription credentials which uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| Azure resource group | |
| **workspaceCollectionName** | **String**| Power BI Embedded Workspace Collection name | |
| **apiVersion** | **String**| Client Api Version. | |
| **body** | [**WorkspaceCollectionAccessKey**](WorkspaceCollectionAccessKey.md)| Access key to regenerate | |

### Return type

[**WorkspaceCollectionAccessKeys**](WorkspaceCollectionAccessKeys.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get access keys completed successfully |  -  |
| **0** | Default Response. It will be deserialized as per the Error definition specified in the schema. Exception will be thrown. |  -  |

<a id="workspaceCollectionsUpdate"></a>
# **workspaceCollectionsUpdate**
> WorkspaceCollection workspaceCollectionsUpdate(subscriptionId, resourceGroupName, workspaceCollectionName, apiVersion, body)



Update an existing Power BI Workspace Collection with the specified properties.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WorkspaceCollectionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    WorkspaceCollectionsApi apiInstance = new WorkspaceCollectionsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | Azure resource group
    String workspaceCollectionName = "workspaceCollectionName_example"; // String | Power BI Embedded Workspace Collection name
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    UpdateWorkspaceCollectionRequest body = new UpdateWorkspaceCollectionRequest(); // UpdateWorkspaceCollectionRequest | Update workspace collection request
    try {
      WorkspaceCollection result = apiInstance.workspaceCollectionsUpdate(subscriptionId, resourceGroupName, workspaceCollectionName, apiVersion, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WorkspaceCollectionsApi#workspaceCollectionsUpdate");
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
| **subscriptionId** | **String**| Gets subscription credentials which uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| Azure resource group | |
| **workspaceCollectionName** | **String**| Power BI Embedded Workspace Collection name | |
| **apiVersion** | **String**| Client Api Version. | |
| **body** | [**UpdateWorkspaceCollectionRequest**](UpdateWorkspaceCollectionRequest.md)| Update workspace collection request | |

### Return type

[**WorkspaceCollection**](WorkspaceCollection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Workspace collection updated successfully |  -  |
| **0** | Default Response. It will be deserialized as per the Error definition specified in the schema. Exception will be thrown. |  -  |

