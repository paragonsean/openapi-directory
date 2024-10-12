# IntegrationAccountSchemasApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**integrationAccountSchemasCreateOrUpdate**](IntegrationAccountSchemasApi.md#integrationAccountSchemasCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/integrationAccounts/{integrationAccountName}/schemas/{schemaName} |  |
| [**integrationAccountSchemasDelete**](IntegrationAccountSchemasApi.md#integrationAccountSchemasDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/integrationAccounts/{integrationAccountName}/schemas/{schemaName} |  |
| [**integrationAccountSchemasGet**](IntegrationAccountSchemasApi.md#integrationAccountSchemasGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/integrationAccounts/{integrationAccountName}/schemas/{schemaName} |  |
| [**integrationAccountSchemasList**](IntegrationAccountSchemasApi.md#integrationAccountSchemasList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/integrationAccounts/{integrationAccountName}/schemas |  |
| [**integrationAccountSchemasListContentCallbackUrl**](IntegrationAccountSchemasApi.md#integrationAccountSchemasListContentCallbackUrl) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/integrationAccounts/{integrationAccountName}/schemas/{schemaName}/listContentCallbackUrl |  |


<a id="integrationAccountSchemasCreateOrUpdate"></a>
# **integrationAccountSchemasCreateOrUpdate**
> IntegrationAccountSchema integrationAccountSchemasCreateOrUpdate(subscriptionId, resourceGroupName, integrationAccountName, schemaName, apiVersion, schema)



Creates or updates an integration account schema.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IntegrationAccountSchemasApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    IntegrationAccountSchemasApi apiInstance = new IntegrationAccountSchemasApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription id.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String integrationAccountName = "integrationAccountName_example"; // String | The integration account name.
    String schemaName = "schemaName_example"; // String | The integration account schema name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    IntegrationAccountSchema schema = new IntegrationAccountSchema(); // IntegrationAccountSchema | The integration account schema.
    try {
      IntegrationAccountSchema result = apiInstance.integrationAccountSchemasCreateOrUpdate(subscriptionId, resourceGroupName, integrationAccountName, schemaName, apiVersion, schema);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IntegrationAccountSchemasApi#integrationAccountSchemasCreateOrUpdate");
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
| **subscriptionId** | **String**| The subscription id. | |
| **resourceGroupName** | **String**| The resource group name. | |
| **integrationAccountName** | **String**| The integration account name. | |
| **schemaName** | **String**| The integration account schema name. | |
| **apiVersion** | **String**| The API version. | |
| **schema** | [**IntegrationAccountSchema**](IntegrationAccountSchema.md)| The integration account schema. | |

### Return type

[**IntegrationAccountSchema**](IntegrationAccountSchema.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **201** | Created |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="integrationAccountSchemasDelete"></a>
# **integrationAccountSchemasDelete**
> integrationAccountSchemasDelete(subscriptionId, resourceGroupName, integrationAccountName, schemaName, apiVersion)



Deletes an integration account schema.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IntegrationAccountSchemasApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    IntegrationAccountSchemasApi apiInstance = new IntegrationAccountSchemasApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription id.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String integrationAccountName = "integrationAccountName_example"; // String | The integration account name.
    String schemaName = "schemaName_example"; // String | The integration account schema name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    try {
      apiInstance.integrationAccountSchemasDelete(subscriptionId, resourceGroupName, integrationAccountName, schemaName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling IntegrationAccountSchemasApi#integrationAccountSchemasDelete");
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
| **subscriptionId** | **String**| The subscription id. | |
| **resourceGroupName** | **String**| The resource group name. | |
| **integrationAccountName** | **String**| The integration account name. | |
| **schemaName** | **String**| The integration account schema name. | |
| **apiVersion** | **String**| The API version. | |

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
| **200** | OK |  -  |
| **204** | No Content |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="integrationAccountSchemasGet"></a>
# **integrationAccountSchemasGet**
> IntegrationAccountSchema integrationAccountSchemasGet(subscriptionId, resourceGroupName, integrationAccountName, schemaName, apiVersion)



Gets an integration account schema.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IntegrationAccountSchemasApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    IntegrationAccountSchemasApi apiInstance = new IntegrationAccountSchemasApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription id.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String integrationAccountName = "integrationAccountName_example"; // String | The integration account name.
    String schemaName = "schemaName_example"; // String | The integration account schema name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    try {
      IntegrationAccountSchema result = apiInstance.integrationAccountSchemasGet(subscriptionId, resourceGroupName, integrationAccountName, schemaName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IntegrationAccountSchemasApi#integrationAccountSchemasGet");
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
| **subscriptionId** | **String**| The subscription id. | |
| **resourceGroupName** | **String**| The resource group name. | |
| **integrationAccountName** | **String**| The integration account name. | |
| **schemaName** | **String**| The integration account schema name. | |
| **apiVersion** | **String**| The API version. | |

### Return type

[**IntegrationAccountSchema**](IntegrationAccountSchema.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="integrationAccountSchemasList"></a>
# **integrationAccountSchemasList**
> IntegrationAccountSchemaListResult integrationAccountSchemasList(subscriptionId, resourceGroupName, integrationAccountName, apiVersion, $top, $filter)



Gets a list of integration account schemas.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IntegrationAccountSchemasApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    IntegrationAccountSchemasApi apiInstance = new IntegrationAccountSchemasApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription id.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String integrationAccountName = "integrationAccountName_example"; // String | The integration account name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    Integer $top = 56; // Integer | The number of items to be included in the result.
    String $filter = "$filter_example"; // String | The filter to apply on the operation. Options for filters include: SchemaType.
    try {
      IntegrationAccountSchemaListResult result = apiInstance.integrationAccountSchemasList(subscriptionId, resourceGroupName, integrationAccountName, apiVersion, $top, $filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IntegrationAccountSchemasApi#integrationAccountSchemasList");
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
| **subscriptionId** | **String**| The subscription id. | |
| **resourceGroupName** | **String**| The resource group name. | |
| **integrationAccountName** | **String**| The integration account name. | |
| **apiVersion** | **String**| The API version. | |
| **$top** | **Integer**| The number of items to be included in the result. | [optional] |
| **$filter** | **String**| The filter to apply on the operation. Options for filters include: SchemaType. | [optional] |

### Return type

[**IntegrationAccountSchemaListResult**](IntegrationAccountSchemaListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="integrationAccountSchemasListContentCallbackUrl"></a>
# **integrationAccountSchemasListContentCallbackUrl**
> WorkflowTriggerCallbackUrl integrationAccountSchemasListContentCallbackUrl(subscriptionId, resourceGroupName, integrationAccountName, schemaName, apiVersion, listContentCallbackUrl)



Get the content callback url.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IntegrationAccountSchemasApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    IntegrationAccountSchemasApi apiInstance = new IntegrationAccountSchemasApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription id.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String integrationAccountName = "integrationAccountName_example"; // String | The integration account name.
    String schemaName = "schemaName_example"; // String | The integration account schema name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    GetCallbackUrlParameters listContentCallbackUrl = new GetCallbackUrlParameters(); // GetCallbackUrlParameters | 
    try {
      WorkflowTriggerCallbackUrl result = apiInstance.integrationAccountSchemasListContentCallbackUrl(subscriptionId, resourceGroupName, integrationAccountName, schemaName, apiVersion, listContentCallbackUrl);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IntegrationAccountSchemasApi#integrationAccountSchemasListContentCallbackUrl");
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
| **subscriptionId** | **String**| The subscription id. | |
| **resourceGroupName** | **String**| The resource group name. | |
| **integrationAccountName** | **String**| The integration account name. | |
| **schemaName** | **String**| The integration account schema name. | |
| **apiVersion** | **String**| The API version. | |
| **listContentCallbackUrl** | [**GetCallbackUrlParameters**](GetCallbackUrlParameters.md)|  | |

### Return type

[**WorkflowTriggerCallbackUrl**](WorkflowTriggerCallbackUrl.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response describing why the operation failed. |  -  |

