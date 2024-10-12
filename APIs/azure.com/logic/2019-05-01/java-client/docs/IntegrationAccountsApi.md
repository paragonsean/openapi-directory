# IntegrationAccountsApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**integrationAccountsCreateOrUpdate**](IntegrationAccountsApi.md#integrationAccountsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/integrationAccounts/{integrationAccountName} |  |
| [**integrationAccountsDelete**](IntegrationAccountsApi.md#integrationAccountsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/integrationAccounts/{integrationAccountName} |  |
| [**integrationAccountsGet**](IntegrationAccountsApi.md#integrationAccountsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/integrationAccounts/{integrationAccountName} |  |
| [**integrationAccountsListByResourceGroup**](IntegrationAccountsApi.md#integrationAccountsListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/integrationAccounts |  |
| [**integrationAccountsListBySubscription**](IntegrationAccountsApi.md#integrationAccountsListBySubscription) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Logic/integrationAccounts |  |
| [**integrationAccountsListCallbackUrl**](IntegrationAccountsApi.md#integrationAccountsListCallbackUrl) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/integrationAccounts/{integrationAccountName}/listCallbackUrl |  |
| [**integrationAccountsListKeyVaultKeys**](IntegrationAccountsApi.md#integrationAccountsListKeyVaultKeys) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/integrationAccounts/{integrationAccountName}/listKeyVaultKeys |  |
| [**integrationAccountsLogTrackingEvents**](IntegrationAccountsApi.md#integrationAccountsLogTrackingEvents) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/integrationAccounts/{integrationAccountName}/logTrackingEvents |  |
| [**integrationAccountsRegenerateAccessKey**](IntegrationAccountsApi.md#integrationAccountsRegenerateAccessKey) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/integrationAccounts/{integrationAccountName}/regenerateAccessKey |  |
| [**integrationAccountsUpdate**](IntegrationAccountsApi.md#integrationAccountsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/integrationAccounts/{integrationAccountName} |  |


<a id="integrationAccountsCreateOrUpdate"></a>
# **integrationAccountsCreateOrUpdate**
> IntegrationAccount integrationAccountsCreateOrUpdate(subscriptionId, resourceGroupName, integrationAccountName, apiVersion, integrationAccount)



Creates or updates an integration account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IntegrationAccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    IntegrationAccountsApi apiInstance = new IntegrationAccountsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription id.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String integrationAccountName = "integrationAccountName_example"; // String | The integration account name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    IntegrationAccount integrationAccount = new IntegrationAccount(); // IntegrationAccount | The integration account.
    try {
      IntegrationAccount result = apiInstance.integrationAccountsCreateOrUpdate(subscriptionId, resourceGroupName, integrationAccountName, apiVersion, integrationAccount);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IntegrationAccountsApi#integrationAccountsCreateOrUpdate");
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
| **integrationAccount** | [**IntegrationAccount**](IntegrationAccount.md)| The integration account. | |

### Return type

[**IntegrationAccount**](IntegrationAccount.md)

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

<a id="integrationAccountsDelete"></a>
# **integrationAccountsDelete**
> integrationAccountsDelete(subscriptionId, resourceGroupName, integrationAccountName, apiVersion)



Deletes an integration account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IntegrationAccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    IntegrationAccountsApi apiInstance = new IntegrationAccountsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription id.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String integrationAccountName = "integrationAccountName_example"; // String | The integration account name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    try {
      apiInstance.integrationAccountsDelete(subscriptionId, resourceGroupName, integrationAccountName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling IntegrationAccountsApi#integrationAccountsDelete");
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

<a id="integrationAccountsGet"></a>
# **integrationAccountsGet**
> IntegrationAccount integrationAccountsGet(subscriptionId, resourceGroupName, integrationAccountName, apiVersion)



Gets an integration account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IntegrationAccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    IntegrationAccountsApi apiInstance = new IntegrationAccountsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription id.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String integrationAccountName = "integrationAccountName_example"; // String | The integration account name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    try {
      IntegrationAccount result = apiInstance.integrationAccountsGet(subscriptionId, resourceGroupName, integrationAccountName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IntegrationAccountsApi#integrationAccountsGet");
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

### Return type

[**IntegrationAccount**](IntegrationAccount.md)

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

<a id="integrationAccountsListByResourceGroup"></a>
# **integrationAccountsListByResourceGroup**
> IntegrationAccountListResult integrationAccountsListByResourceGroup(subscriptionId, resourceGroupName, apiVersion, $top)



Gets a list of integration accounts by resource group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IntegrationAccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    IntegrationAccountsApi apiInstance = new IntegrationAccountsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription id.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    Integer $top = 56; // Integer | The number of items to be included in the result.
    try {
      IntegrationAccountListResult result = apiInstance.integrationAccountsListByResourceGroup(subscriptionId, resourceGroupName, apiVersion, $top);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IntegrationAccountsApi#integrationAccountsListByResourceGroup");
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
| **apiVersion** | **String**| The API version. | |
| **$top** | **Integer**| The number of items to be included in the result. | [optional] |

### Return type

[**IntegrationAccountListResult**](IntegrationAccountListResult.md)

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

<a id="integrationAccountsListBySubscription"></a>
# **integrationAccountsListBySubscription**
> IntegrationAccountListResult integrationAccountsListBySubscription(subscriptionId, apiVersion, $top)



Gets a list of integration accounts by subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IntegrationAccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    IntegrationAccountsApi apiInstance = new IntegrationAccountsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription id.
    String apiVersion = "apiVersion_example"; // String | The API version.
    Integer $top = 56; // Integer | The number of items to be included in the result.
    try {
      IntegrationAccountListResult result = apiInstance.integrationAccountsListBySubscription(subscriptionId, apiVersion, $top);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IntegrationAccountsApi#integrationAccountsListBySubscription");
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
| **apiVersion** | **String**| The API version. | |
| **$top** | **Integer**| The number of items to be included in the result. | [optional] |

### Return type

[**IntegrationAccountListResult**](IntegrationAccountListResult.md)

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

<a id="integrationAccountsListCallbackUrl"></a>
# **integrationAccountsListCallbackUrl**
> CallbackUrl integrationAccountsListCallbackUrl(subscriptionId, resourceGroupName, integrationAccountName, apiVersion, parameters)



Gets the integration account callback URL.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IntegrationAccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    IntegrationAccountsApi apiInstance = new IntegrationAccountsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription id.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String integrationAccountName = "integrationAccountName_example"; // String | The integration account name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    GetCallbackUrlParameters parameters = new GetCallbackUrlParameters(); // GetCallbackUrlParameters | The callback URL parameters.
    try {
      CallbackUrl result = apiInstance.integrationAccountsListCallbackUrl(subscriptionId, resourceGroupName, integrationAccountName, apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IntegrationAccountsApi#integrationAccountsListCallbackUrl");
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
| **parameters** | [**GetCallbackUrlParameters**](GetCallbackUrlParameters.md)| The callback URL parameters. | |

### Return type

[**CallbackUrl**](CallbackUrl.md)

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

<a id="integrationAccountsListKeyVaultKeys"></a>
# **integrationAccountsListKeyVaultKeys**
> KeyVaultKeyCollection integrationAccountsListKeyVaultKeys(subscriptionId, resourceGroupName, integrationAccountName, apiVersion, listKeyVaultKeys)



Gets the integration account&#39;s Key Vault keys.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IntegrationAccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    IntegrationAccountsApi apiInstance = new IntegrationAccountsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription id.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String integrationAccountName = "integrationAccountName_example"; // String | The integration account name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    ListKeyVaultKeysDefinition listKeyVaultKeys = new ListKeyVaultKeysDefinition(); // ListKeyVaultKeysDefinition | The key vault parameters.
    try {
      KeyVaultKeyCollection result = apiInstance.integrationAccountsListKeyVaultKeys(subscriptionId, resourceGroupName, integrationAccountName, apiVersion, listKeyVaultKeys);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IntegrationAccountsApi#integrationAccountsListKeyVaultKeys");
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
| **listKeyVaultKeys** | [**ListKeyVaultKeysDefinition**](ListKeyVaultKeysDefinition.md)| The key vault parameters. | |

### Return type

[**KeyVaultKeyCollection**](KeyVaultKeyCollection.md)

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

<a id="integrationAccountsLogTrackingEvents"></a>
# **integrationAccountsLogTrackingEvents**
> integrationAccountsLogTrackingEvents(subscriptionId, resourceGroupName, integrationAccountName, apiVersion, logTrackingEvents)



Logs the integration account&#39;s tracking events.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IntegrationAccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    IntegrationAccountsApi apiInstance = new IntegrationAccountsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription id.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String integrationAccountName = "integrationAccountName_example"; // String | The integration account name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    TrackingEventsDefinition logTrackingEvents = new TrackingEventsDefinition(); // TrackingEventsDefinition | The callback URL parameters.
    try {
      apiInstance.integrationAccountsLogTrackingEvents(subscriptionId, resourceGroupName, integrationAccountName, apiVersion, logTrackingEvents);
    } catch (ApiException e) {
      System.err.println("Exception when calling IntegrationAccountsApi#integrationAccountsLogTrackingEvents");
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
| **logTrackingEvents** | [**TrackingEventsDefinition**](TrackingEventsDefinition.md)| The callback URL parameters. | |

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
| **200** | OK |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="integrationAccountsRegenerateAccessKey"></a>
# **integrationAccountsRegenerateAccessKey**
> IntegrationAccount integrationAccountsRegenerateAccessKey(subscriptionId, resourceGroupName, integrationAccountName, apiVersion, regenerateAccessKey)



Regenerates the integration account access key.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IntegrationAccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    IntegrationAccountsApi apiInstance = new IntegrationAccountsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription id.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String integrationAccountName = "integrationAccountName_example"; // String | The integration account name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    RegenerateActionParameter regenerateAccessKey = new RegenerateActionParameter(); // RegenerateActionParameter | The access key type.
    try {
      IntegrationAccount result = apiInstance.integrationAccountsRegenerateAccessKey(subscriptionId, resourceGroupName, integrationAccountName, apiVersion, regenerateAccessKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IntegrationAccountsApi#integrationAccountsRegenerateAccessKey");
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
| **regenerateAccessKey** | [**RegenerateActionParameter**](RegenerateActionParameter.md)| The access key type. | |

### Return type

[**IntegrationAccount**](IntegrationAccount.md)

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

<a id="integrationAccountsUpdate"></a>
# **integrationAccountsUpdate**
> IntegrationAccount integrationAccountsUpdate(subscriptionId, resourceGroupName, integrationAccountName, apiVersion, integrationAccount)



Updates an integration account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IntegrationAccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    IntegrationAccountsApi apiInstance = new IntegrationAccountsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription id.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String integrationAccountName = "integrationAccountName_example"; // String | The integration account name.
    String apiVersion = "apiVersion_example"; // String | The API version.
    IntegrationAccount integrationAccount = new IntegrationAccount(); // IntegrationAccount | The integration account.
    try {
      IntegrationAccount result = apiInstance.integrationAccountsUpdate(subscriptionId, resourceGroupName, integrationAccountName, apiVersion, integrationAccount);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IntegrationAccountsApi#integrationAccountsUpdate");
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
| **integrationAccount** | [**IntegrationAccount**](IntegrationAccount.md)| The integration account. | |

### Return type

[**IntegrationAccount**](IntegrationAccount.md)

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

