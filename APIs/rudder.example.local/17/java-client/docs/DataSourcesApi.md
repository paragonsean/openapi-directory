# DataSourcesApi

All URIs are relative to *https://rudder.example.local/rudder/api/latest*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createDataSource**](DataSourcesApi.md#createDataSource) | **PUT** /datasources | Create a data source |
| [**deleteDataSource**](DataSourcesApi.md#deleteDataSource) | **DELETE** /datasources/{datasourceId} | Delete a data source |
| [**getAllDataSources**](DataSourcesApi.md#getAllDataSources) | **GET** /datasources | List all data sources |
| [**getDataSource**](DataSourcesApi.md#getDataSource) | **GET** /datasources/{datasourceId} | Get data source configuration |
| [**reloadAllDatasourcesAllNodes**](DataSourcesApi.md#reloadAllDatasourcesAllNodes) | **POST** /datasources/reload | Update properties from data sources |
| [**reloadAllDatasourcesOneNode**](DataSourcesApi.md#reloadAllDatasourcesOneNode) | **POST** /nodes/{nodeId}/fetchData | Update properties for one node from all data sources |
| [**reloadOneDatasourceAllNodes**](DataSourcesApi.md#reloadOneDatasourceAllNodes) | **POST** /datasources/reload/{datasourceId} | Update properties from data sources |
| [**reloadOneDatasourceOneNode**](DataSourcesApi.md#reloadOneDatasourceOneNode) | **POST** /nodes/{nodeId}/fetchData/{datasourceId} | Update properties for one node from a data source |
| [**updateDataSource**](DataSourcesApi.md#updateDataSource) | **POST** /datasources/{datasourceId} | Update a data source configuration |


<a id="createDataSource"></a>
# **createDataSource**
> CreateDataSource200Response createDataSource(datasource)

Create a data source

Create a new data source

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
    defaultClient.setBasePath("https://rudder.example.local/rudder/api/latest");
    
    // Configure API key authorization: API-Tokens
    ApiKeyAuth API-Tokens = (ApiKeyAuth) defaultClient.getAuthentication("API-Tokens");
    API-Tokens.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API-Tokens.setApiKeyPrefix("Token");

    DataSourcesApi apiInstance = new DataSourcesApi(defaultClient);
    Datasource datasource = new Datasource(); // Datasource | 
    try {
      CreateDataSource200Response result = apiInstance.createDataSource(datasource);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DataSourcesApi#createDataSource");
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
| **datasource** | [**Datasource**](Datasource.md)|  | [optional] |

### Return type

[**CreateDataSource200Response**](CreateDataSource200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Created |  -  |

<a id="deleteDataSource"></a>
# **deleteDataSource**
> DeleteDataSource200Response deleteDataSource(datasourceId)

Delete a data source

Delete a data source configuration

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
    defaultClient.setBasePath("https://rudder.example.local/rudder/api/latest");
    
    // Configure API key authorization: API-Tokens
    ApiKeyAuth API-Tokens = (ApiKeyAuth) defaultClient.getAuthentication("API-Tokens");
    API-Tokens.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API-Tokens.setApiKeyPrefix("Token");

    DataSourcesApi apiInstance = new DataSourcesApi(defaultClient);
    String datasourceId = "test-data-source"; // String | Id of the data source
    try {
      DeleteDataSource200Response result = apiInstance.deleteDataSource(datasourceId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DataSourcesApi#deleteDataSource");
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
| **datasourceId** | **String**| Id of the data source | |

### Return type

[**DeleteDataSource200Response**](DeleteDataSource200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Data source information |  -  |

<a id="getAllDataSources"></a>
# **getAllDataSources**
> GetAllDataSources200Response getAllDataSources()

List all data sources

Get the configuration of all present data sources

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
    defaultClient.setBasePath("https://rudder.example.local/rudder/api/latest");
    
    // Configure API key authorization: API-Tokens
    ApiKeyAuth API-Tokens = (ApiKeyAuth) defaultClient.getAuthentication("API-Tokens");
    API-Tokens.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API-Tokens.setApiKeyPrefix("Token");

    DataSourcesApi apiInstance = new DataSourcesApi(defaultClient);
    try {
      GetAllDataSources200Response result = apiInstance.getAllDataSources();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DataSourcesApi#getAllDataSources");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetAllDataSources200Response**](GetAllDataSources200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Data sources information |  -  |

<a id="getDataSource"></a>
# **getDataSource**
> GetDataSource200Response getDataSource(datasourceId)

Get data source configuration

Get the configuration of a data source

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
    defaultClient.setBasePath("https://rudder.example.local/rudder/api/latest");
    
    // Configure API key authorization: API-Tokens
    ApiKeyAuth API-Tokens = (ApiKeyAuth) defaultClient.getAuthentication("API-Tokens");
    API-Tokens.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API-Tokens.setApiKeyPrefix("Token");

    DataSourcesApi apiInstance = new DataSourcesApi(defaultClient);
    String datasourceId = "test-data-source"; // String | Id of the data source
    try {
      GetDataSource200Response result = apiInstance.getDataSource(datasourceId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DataSourcesApi#getDataSource");
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
| **datasourceId** | **String**| Id of the data source | |

### Return type

[**GetDataSource200Response**](GetDataSource200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Data source information |  -  |

<a id="reloadAllDatasourcesAllNodes"></a>
# **reloadAllDatasourcesAllNodes**
> ReloadAllDatasourcesAllNodes200Response reloadAllDatasourcesAllNodes()

Update properties from data sources

Update properties from all data source on all nodes. The call is asynchronous.

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
    defaultClient.setBasePath("https://rudder.example.local/rudder/api/latest");
    
    // Configure API key authorization: API-Tokens
    ApiKeyAuth API-Tokens = (ApiKeyAuth) defaultClient.getAuthentication("API-Tokens");
    API-Tokens.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API-Tokens.setApiKeyPrefix("Token");

    DataSourcesApi apiInstance = new DataSourcesApi(defaultClient);
    try {
      ReloadAllDatasourcesAllNodes200Response result = apiInstance.reloadAllDatasourcesAllNodes();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DataSourcesApi#reloadAllDatasourcesAllNodes");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ReloadAllDatasourcesAllNodes200Response**](ReloadAllDatasourcesAllNodes200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Data source reloaded |  -  |

<a id="reloadAllDatasourcesOneNode"></a>
# **reloadAllDatasourcesOneNode**
> ReloadAllDatasourcesOneNode200Response reloadAllDatasourcesOneNode(nodeId)

Update properties for one node from all data sources

Update properties from all data sources on one nodes. The call is asynchronous.

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
    defaultClient.setBasePath("https://rudder.example.local/rudder/api/latest");
    
    // Configure API key authorization: API-Tokens
    ApiKeyAuth API-Tokens = (ApiKeyAuth) defaultClient.getAuthentication("API-Tokens");
    API-Tokens.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API-Tokens.setApiKeyPrefix("Token");

    DataSourcesApi apiInstance = new DataSourcesApi(defaultClient);
    String nodeId = "9a1773c9-0889-40b6-be89-f6504443ac1b"; // String | Id of the target node
    try {
      ReloadAllDatasourcesOneNode200Response result = apiInstance.reloadAllDatasourcesOneNode(nodeId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DataSourcesApi#reloadAllDatasourcesOneNode");
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
| **nodeId** | **String**| Id of the target node | |

### Return type

[**ReloadAllDatasourcesOneNode200Response**](ReloadAllDatasourcesOneNode200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Data sources reloaded |  -  |

<a id="reloadOneDatasourceAllNodes"></a>
# **reloadOneDatasourceAllNodes**
> ReloadOneDatasourceAllNodes200Response reloadOneDatasourceAllNodes(datasourceId)

Update properties from data sources

Update properties from all data source on all nodes. The call is asynchronous.

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
    defaultClient.setBasePath("https://rudder.example.local/rudder/api/latest");
    
    // Configure API key authorization: API-Tokens
    ApiKeyAuth API-Tokens = (ApiKeyAuth) defaultClient.getAuthentication("API-Tokens");
    API-Tokens.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API-Tokens.setApiKeyPrefix("Token");

    DataSourcesApi apiInstance = new DataSourcesApi(defaultClient);
    String datasourceId = "test-data-source"; // String | Id of the data source
    try {
      ReloadOneDatasourceAllNodes200Response result = apiInstance.reloadOneDatasourceAllNodes(datasourceId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DataSourcesApi#reloadOneDatasourceAllNodes");
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
| **datasourceId** | **String**| Id of the data source | |

### Return type

[**ReloadOneDatasourceAllNodes200Response**](ReloadOneDatasourceAllNodes200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Data source reloaded |  -  |

<a id="reloadOneDatasourceOneNode"></a>
# **reloadOneDatasourceOneNode**
> ReloadOneDatasourceOneNode200Response reloadOneDatasourceOneNode(nodeId, datasourceId)

Update properties for one node from a data source

Update properties from a data source on one nodes. The call is asynchronous.

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
    defaultClient.setBasePath("https://rudder.example.local/rudder/api/latest");
    
    // Configure API key authorization: API-Tokens
    ApiKeyAuth API-Tokens = (ApiKeyAuth) defaultClient.getAuthentication("API-Tokens");
    API-Tokens.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API-Tokens.setApiKeyPrefix("Token");

    DataSourcesApi apiInstance = new DataSourcesApi(defaultClient);
    String nodeId = "9a1773c9-0889-40b6-be89-f6504443ac1b"; // String | Id of the target node
    String datasourceId = "test-data-source"; // String | Id of the data source
    try {
      ReloadOneDatasourceOneNode200Response result = apiInstance.reloadOneDatasourceOneNode(nodeId, datasourceId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DataSourcesApi#reloadOneDatasourceOneNode");
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
| **nodeId** | **String**| Id of the target node | |
| **datasourceId** | **String**| Id of the data source | |

### Return type

[**ReloadOneDatasourceOneNode200Response**](ReloadOneDatasourceOneNode200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Data sources reloaded |  -  |

<a id="updateDataSource"></a>
# **updateDataSource**
> UpdateDataSource200Response updateDataSource(datasourceId, datasource)

Update a data source configuration

Update the configuration of a data source

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
    defaultClient.setBasePath("https://rudder.example.local/rudder/api/latest");
    
    // Configure API key authorization: API-Tokens
    ApiKeyAuth API-Tokens = (ApiKeyAuth) defaultClient.getAuthentication("API-Tokens");
    API-Tokens.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API-Tokens.setApiKeyPrefix("Token");

    DataSourcesApi apiInstance = new DataSourcesApi(defaultClient);
    String datasourceId = "test-data-source"; // String | Id of the data source
    Datasource datasource = new Datasource(); // Datasource | 
    try {
      UpdateDataSource200Response result = apiInstance.updateDataSource(datasourceId, datasource);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DataSourcesApi#updateDataSource");
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
| **datasourceId** | **String**| Id of the data source | |
| **datasource** | [**Datasource**](Datasource.md)|  | [optional] |

### Return type

[**UpdateDataSource200Response**](UpdateDataSource200Response.md)

### Authorization

[API-Tokens](../README.md#API-Tokens)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Data source information |  -  |

