# DataSourcesApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**dataSourcesCreateOrUpdate**](DataSourcesApi.md#dataSourcesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.OperationalInsights/workspaces/{workspaceName}/dataSources/{dataSourceName} |  |
| [**dataSourcesDelete**](DataSourcesApi.md#dataSourcesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.OperationalInsights/workspaces/{workspaceName}/dataSources/{dataSourceName} |  |
| [**dataSourcesGet**](DataSourcesApi.md#dataSourcesGet) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.OperationalInsights/workspaces/{workspaceName}/dataSources/{dataSourceName} |  |
| [**dataSourcesListByWorkspace**](DataSourcesApi.md#dataSourcesListByWorkspace) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.OperationalInsights/workspaces/{workspaceName}/dataSources |  |


<a id="dataSourcesCreateOrUpdate"></a>
# **dataSourcesCreateOrUpdate**
> DataSource dataSourcesCreateOrUpdate(resourceGroupName, workspaceName, dataSourceName, apiVersion, subscriptionId, parameters)



Create or update a data source.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DataSourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DataSourcesApi apiInstance = new DataSourcesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to get. The name is case insensitive.
    String workspaceName = "workspaceName_example"; // String | Name of the Log Analytics Workspace that will contain the datasource
    String dataSourceName = "dataSourceName_example"; // String | The name of the datasource resource.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    DataSource parameters = new DataSource(); // DataSource | The parameters required to create or update a datasource.
    try {
      DataSource result = apiInstance.dataSourcesCreateOrUpdate(resourceGroupName, workspaceName, dataSourceName, apiVersion, subscriptionId, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DataSourcesApi#dataSourcesCreateOrUpdate");
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
| **resourceGroupName** | **String**| The name of the resource group to get. The name is case insensitive. | |
| **workspaceName** | **String**| Name of the Log Analytics Workspace that will contain the datasource | |
| **dataSourceName** | **String**| The name of the datasource resource. | |
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **parameters** | [**DataSource**](DataSource.md)| The parameters required to create or update a datasource. | |

### Return type

[**DataSource**](DataSource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK response definition. |  -  |
| **201** | Created response definition. |  -  |

<a id="dataSourcesDelete"></a>
# **dataSourcesDelete**
> dataSourcesDelete(resourceGroupName, workspaceName, dataSourceName, apiVersion, subscriptionId)



Deletes a data source instance.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DataSourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DataSourcesApi apiInstance = new DataSourcesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to get. The name is case insensitive.
    String workspaceName = "workspaceName_example"; // String | Name of the Log Analytics Workspace that contains the datasource.
    String dataSourceName = "dataSourceName_example"; // String | Name of the datasource.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      apiInstance.dataSourcesDelete(resourceGroupName, workspaceName, dataSourceName, apiVersion, subscriptionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling DataSourcesApi#dataSourcesDelete");
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
| **resourceGroupName** | **String**| The name of the resource group to get. The name is case insensitive. | |
| **workspaceName** | **String**| Name of the Log Analytics Workspace that contains the datasource. | |
| **dataSourceName** | **String**| Name of the datasource. | |
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK response definition. |  -  |
| **204** | NoContent response definition. |  -  |

<a id="dataSourcesGet"></a>
# **dataSourcesGet**
> DataSource dataSourcesGet(resourceGroupName, workspaceName, dataSourceName, apiVersion, subscriptionId)



Gets a datasource instance.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DataSourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DataSourcesApi apiInstance = new DataSourcesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to get. The name is case insensitive.
    String workspaceName = "workspaceName_example"; // String | Name of the Log Analytics Workspace that contains the datasource.
    String dataSourceName = "dataSourceName_example"; // String | Name of the datasource
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      DataSource result = apiInstance.dataSourcesGet(resourceGroupName, workspaceName, dataSourceName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DataSourcesApi#dataSourcesGet");
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
| **resourceGroupName** | **String**| The name of the resource group to get. The name is case insensitive. | |
| **workspaceName** | **String**| Name of the Log Analytics Workspace that contains the datasource. | |
| **dataSourceName** | **String**| Name of the datasource | |
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**DataSource**](DataSource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK response definition. |  -  |

<a id="dataSourcesListByWorkspace"></a>
# **dataSourcesListByWorkspace**
> DataSourceListResult dataSourcesListByWorkspace(resourceGroupName, workspaceName, $filter, apiVersion, subscriptionId, $skiptoken)



Gets the first page of data source instances in a workspace with the link to the next page.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DataSourcesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DataSourcesApi apiInstance = new DataSourcesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to get. The name is case insensitive.
    String workspaceName = "workspaceName_example"; // String | The workspace that contains the data sources.
    String $filter = "$filter_example"; // String | The filter to apply on the operation.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String $skiptoken = "$skiptoken_example"; // String | Starting point of the collection of data source instances.
    try {
      DataSourceListResult result = apiInstance.dataSourcesListByWorkspace(resourceGroupName, workspaceName, $filter, apiVersion, subscriptionId, $skiptoken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DataSourcesApi#dataSourcesListByWorkspace");
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
| **resourceGroupName** | **String**| The name of the resource group to get. The name is case insensitive. | |
| **workspaceName** | **String**| The workspace that contains the data sources. | |
| **$filter** | **String**| The filter to apply on the operation. | |
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **$skiptoken** | **String**| Starting point of the collection of data source instances. | [optional] |

### Return type

[**DataSourceListResult**](DataSourceListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK response definition. |  -  |

