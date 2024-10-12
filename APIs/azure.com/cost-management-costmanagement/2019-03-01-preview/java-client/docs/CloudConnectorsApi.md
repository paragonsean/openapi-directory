# CloudConnectorsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**cloudConnectorCreateOrUpdate**](CloudConnectorsApi.md#cloudConnectorCreateOrUpdate) | **PUT** /providers/Microsoft.CostManagement/cloudConnectors/{connectorName} |  |
| [**cloudConnectorDelete**](CloudConnectorsApi.md#cloudConnectorDelete) | **DELETE** /providers/Microsoft.CostManagement/cloudConnectors/{connectorName} |  |
| [**cloudConnectorGet**](CloudConnectorsApi.md#cloudConnectorGet) | **GET** /providers/Microsoft.CostManagement/cloudConnectors/{connectorName} |  |
| [**cloudConnectorList**](CloudConnectorsApi.md#cloudConnectorList) | **GET** /providers/Microsoft.CostManagement/cloudConnectors |  |
| [**cloudConnectorUpdate**](CloudConnectorsApi.md#cloudConnectorUpdate) | **PATCH** /providers/Microsoft.CostManagement/cloudConnectors/{connectorName} |  |


<a id="cloudConnectorCreateOrUpdate"></a>
# **cloudConnectorCreateOrUpdate**
> ConnectorDefinition cloudConnectorCreateOrUpdate(apiVersion, connectorName, connector)



Create or update a cloud connector definition

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CloudConnectorsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    CloudConnectorsApi apiInstance = new CloudConnectorsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-03-01-preview
    String connectorName = "connectorName_example"; // String | Connector Name.
    ConnectorDefinition connector = new ConnectorDefinition(); // ConnectorDefinition | Connector details
    try {
      ConnectorDefinition result = apiInstance.cloudConnectorCreateOrUpdate(apiVersion, connectorName, connector);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CloudConnectorsApi#cloudConnectorCreateOrUpdate");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-03-01-preview | |
| **connectorName** | **String**| Connector Name. | |
| **connector** | [**ConnectorDefinition**](ConnectorDefinition.md)| Connector details | |

### Return type

[**ConnectorDefinition**](ConnectorDefinition.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. The request has succeeded. |  -  |
| **201** | Created. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="cloudConnectorDelete"></a>
# **cloudConnectorDelete**
> cloudConnectorDelete(apiVersion, connectorName)



Delete a cloud connector definition

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CloudConnectorsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    CloudConnectorsApi apiInstance = new CloudConnectorsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-03-01-preview
    String connectorName = "connectorName_example"; // String | Connector Name.
    try {
      apiInstance.cloudConnectorDelete(apiVersion, connectorName);
    } catch (ApiException e) {
      System.err.println("Exception when calling CloudConnectorsApi#cloudConnectorDelete");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-03-01-preview | |
| **connectorName** | **String**| Connector Name. | |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. The request has succeeded. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="cloudConnectorGet"></a>
# **cloudConnectorGet**
> ConnectorDefinition cloudConnectorGet(apiVersion, connectorName, $expand)



Get a cloud connector definition

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CloudConnectorsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    CloudConnectorsApi apiInstance = new CloudConnectorsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-03-01-preview
    String connectorName = "connectorName_example"; // String | Connector Name.
    String $expand = "$expand_example"; // String | May be used to expand the collectionInfo property. By default, collectionInfo is not included.
    try {
      ConnectorDefinition result = apiInstance.cloudConnectorGet(apiVersion, connectorName, $expand);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CloudConnectorsApi#cloudConnectorGet");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-03-01-preview | |
| **connectorName** | **String**| Connector Name. | |
| **$expand** | **String**| May be used to expand the collectionInfo property. By default, collectionInfo is not included. | [optional] |

### Return type

[**ConnectorDefinition**](ConnectorDefinition.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. The request has succeeded. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="cloudConnectorList"></a>
# **cloudConnectorList**
> ConnectorDefinitionListResult cloudConnectorList(apiVersion)



List all cloud connector definitions

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CloudConnectorsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    CloudConnectorsApi apiInstance = new CloudConnectorsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-03-01-preview
    try {
      ConnectorDefinitionListResult result = apiInstance.cloudConnectorList(apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CloudConnectorsApi#cloudConnectorList");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-03-01-preview | |

### Return type

[**ConnectorDefinitionListResult**](ConnectorDefinitionListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. The request has succeeded. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="cloudConnectorUpdate"></a>
# **cloudConnectorUpdate**
> ConnectorDefinition cloudConnectorUpdate(apiVersion, connectorName, connector)



Update a cloud connector definition

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CloudConnectorsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    CloudConnectorsApi apiInstance = new CloudConnectorsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-03-01-preview
    String connectorName = "connectorName_example"; // String | Connector Name.
    ConnectorDefinition connector = new ConnectorDefinition(); // ConnectorDefinition | Connector details
    try {
      ConnectorDefinition result = apiInstance.cloudConnectorUpdate(apiVersion, connectorName, connector);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CloudConnectorsApi#cloudConnectorUpdate");
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
| **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-03-01-preview | |
| **connectorName** | **String**| Connector Name. | |
| **connector** | [**ConnectorDefinition**](ConnectorDefinition.md)| Connector details | |

### Return type

[**ConnectorDefinition**](ConnectorDefinition.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. The request has succeeded. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

