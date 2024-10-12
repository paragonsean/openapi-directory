# ShareApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**providerShareSubscriptionsGetByShare**](ShareApi.md#providerShareSubscriptionsGetByShare) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataShare/accounts/{accountName}/shares/{shareName}/providerShareSubscriptions/{providerShareSubscriptionId} | Get share subscription in a provider share. |
| [**providerShareSubscriptionsListByShare**](ShareApi.md#providerShareSubscriptionsListByShare) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataShare/accounts/{accountName}/shares/{shareName}/providerShareSubscriptions | List of available share subscriptions to a provider share. |
| [**providerShareSubscriptionsReinstate**](ShareApi.md#providerShareSubscriptionsReinstate) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataShare/accounts/{accountName}/shares/{shareName}/providerShareSubscriptions/{providerShareSubscriptionId}/reinstate | Reinstate share subscription in a provider share. |
| [**providerShareSubscriptionsRevoke**](ShareApi.md#providerShareSubscriptionsRevoke) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataShare/accounts/{accountName}/shares/{shareName}/providerShareSubscriptions/{providerShareSubscriptionId}/revoke | Revoke share subscription in a provider share. |
| [**sharesCreate**](ShareApi.md#sharesCreate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataShare/accounts/{accountName}/shares/{shareName} | Create a share in the given account. |
| [**sharesDelete**](ShareApi.md#sharesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataShare/accounts/{accountName}/shares/{shareName} | Deletes a share |
| [**sharesGet**](ShareApi.md#sharesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataShare/accounts/{accountName}/shares/{shareName} | Get a specified share |
| [**sharesListByAccount**](ShareApi.md#sharesListByAccount) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataShare/accounts/{accountName}/shares | List of available shares under an account. |
| [**sharesListSynchronizationDetails**](ShareApi.md#sharesListSynchronizationDetails) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataShare/accounts/{accountName}/shares/{shareName}/listSynchronizationDetails | List data set level details for a share synchronization |
| [**sharesListSynchronizations**](ShareApi.md#sharesListSynchronizations) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataShare/accounts/{accountName}/shares/{shareName}/listSynchronizations | List Synchronizations in a share |


<a id="providerShareSubscriptionsGetByShare"></a>
# **providerShareSubscriptionsGetByShare**
> ProviderShareSubscription providerShareSubscriptionsGetByShare(subscriptionId, resourceGroupName, accountName, shareName, providerShareSubscriptionId, apiVersion)

Get share subscription in a provider share.

Get share subscription in a provider share

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ShareApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ShareApi apiInstance = new ShareApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription identifier
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String accountName = "accountName_example"; // String | The name of the share account.
    String shareName = "shareName_example"; // String | The name of the share.
    String providerShareSubscriptionId = "providerShareSubscriptionId_example"; // String | To locate shareSubscription
    String apiVersion = "apiVersion_example"; // String | The api version to use.
    try {
      ProviderShareSubscription result = apiInstance.providerShareSubscriptionsGetByShare(subscriptionId, resourceGroupName, accountName, shareName, providerShareSubscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ShareApi#providerShareSubscriptionsGetByShare");
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
| **subscriptionId** | **String**| The subscription identifier | |
| **resourceGroupName** | **String**| The resource group name. | |
| **accountName** | **String**| The name of the share account. | |
| **shareName** | **String**| The name of the share. | |
| **providerShareSubscriptionId** | **String**| To locate shareSubscription | |
| **apiVersion** | **String**| The api version to use. | |

### Return type

[**ProviderShareSubscription**](ProviderShareSubscription.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **0** | An error response received from the Microsoft.DataShare resource provider. |  -  |

<a id="providerShareSubscriptionsListByShare"></a>
# **providerShareSubscriptionsListByShare**
> ProviderShareSubscriptionList providerShareSubscriptionsListByShare(subscriptionId, resourceGroupName, accountName, shareName, apiVersion, $skipToken)

List of available share subscriptions to a provider share.

List share subscriptions in a provider share

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ShareApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ShareApi apiInstance = new ShareApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription identifier
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String accountName = "accountName_example"; // String | The name of the share account.
    String shareName = "shareName_example"; // String | The name of the share.
    String apiVersion = "apiVersion_example"; // String | The api version to use.
    String $skipToken = "$skipToken_example"; // String | Continuation Token
    try {
      ProviderShareSubscriptionList result = apiInstance.providerShareSubscriptionsListByShare(subscriptionId, resourceGroupName, accountName, shareName, apiVersion, $skipToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ShareApi#providerShareSubscriptionsListByShare");
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
| **subscriptionId** | **String**| The subscription identifier | |
| **resourceGroupName** | **String**| The resource group name. | |
| **accountName** | **String**| The name of the share account. | |
| **shareName** | **String**| The name of the share. | |
| **apiVersion** | **String**| The api version to use. | |
| **$skipToken** | **String**| Continuation Token | [optional] |

### Return type

[**ProviderShareSubscriptionList**](ProviderShareSubscriptionList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **0** | An error response received from the Microsoft.DataShare resource provider. |  -  |

<a id="providerShareSubscriptionsReinstate"></a>
# **providerShareSubscriptionsReinstate**
> ProviderShareSubscription providerShareSubscriptionsReinstate(subscriptionId, resourceGroupName, accountName, shareName, providerShareSubscriptionId, apiVersion)

Reinstate share subscription in a provider share.

Reinstate share subscription in a provider share

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ShareApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ShareApi apiInstance = new ShareApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription identifier
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String accountName = "accountName_example"; // String | The name of the share account.
    String shareName = "shareName_example"; // String | The name of the share.
    String providerShareSubscriptionId = "providerShareSubscriptionId_example"; // String | To locate shareSubscription
    String apiVersion = "apiVersion_example"; // String | The api version to use.
    try {
      ProviderShareSubscription result = apiInstance.providerShareSubscriptionsReinstate(subscriptionId, resourceGroupName, accountName, shareName, providerShareSubscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ShareApi#providerShareSubscriptionsReinstate");
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
| **subscriptionId** | **String**| The subscription identifier | |
| **resourceGroupName** | **String**| The resource group name. | |
| **accountName** | **String**| The name of the share account. | |
| **shareName** | **String**| The name of the share. | |
| **providerShareSubscriptionId** | **String**| To locate shareSubscription | |
| **apiVersion** | **String**| The api version to use. | |

### Return type

[**ProviderShareSubscription**](ProviderShareSubscription.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **0** | An error response received from the Microsoft.DataShare resource provider. |  -  |

<a id="providerShareSubscriptionsRevoke"></a>
# **providerShareSubscriptionsRevoke**
> ProviderShareSubscription providerShareSubscriptionsRevoke(subscriptionId, resourceGroupName, accountName, shareName, providerShareSubscriptionId, apiVersion)

Revoke share subscription in a provider share.

Revoke share subscription in a provider share

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ShareApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ShareApi apiInstance = new ShareApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription identifier
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String accountName = "accountName_example"; // String | The name of the share account.
    String shareName = "shareName_example"; // String | The name of the share.
    String providerShareSubscriptionId = "providerShareSubscriptionId_example"; // String | To locate shareSubscription
    String apiVersion = "apiVersion_example"; // String | The api version to use.
    try {
      ProviderShareSubscription result = apiInstance.providerShareSubscriptionsRevoke(subscriptionId, resourceGroupName, accountName, shareName, providerShareSubscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ShareApi#providerShareSubscriptionsRevoke");
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
| **subscriptionId** | **String**| The subscription identifier | |
| **resourceGroupName** | **String**| The resource group name. | |
| **accountName** | **String**| The name of the share account. | |
| **shareName** | **String**| The name of the share. | |
| **providerShareSubscriptionId** | **String**| To locate shareSubscription | |
| **apiVersion** | **String**| The api version to use. | |

### Return type

[**ProviderShareSubscription**](ProviderShareSubscription.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **202** | Accepted |  -  |
| **0** | An error response received from the Microsoft.DataShare resource provider. |  -  |

<a id="sharesCreate"></a>
# **sharesCreate**
> Share sharesCreate(subscriptionId, resourceGroupName, accountName, shareName, apiVersion, share)

Create a share in the given account.

Create a share 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ShareApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ShareApi apiInstance = new ShareApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription identifier
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String accountName = "accountName_example"; // String | The name of the share account.
    String shareName = "shareName_example"; // String | The name of the share.
    String apiVersion = "apiVersion_example"; // String | The api version to use.
    Share share = new Share(); // Share | The share payload
    try {
      Share result = apiInstance.sharesCreate(subscriptionId, resourceGroupName, accountName, shareName, apiVersion, share);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ShareApi#sharesCreate");
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
| **subscriptionId** | **String**| The subscription identifier | |
| **resourceGroupName** | **String**| The resource group name. | |
| **accountName** | **String**| The name of the share account. | |
| **shareName** | **String**| The name of the share. | |
| **apiVersion** | **String**| The api version to use. | |
| **share** | [**Share**](Share.md)| The share payload | |

### Return type

[**Share**](Share.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **201** | Success |  -  |
| **0** | An error response received from the Microsoft.DataShare resource provider. |  -  |

<a id="sharesDelete"></a>
# **sharesDelete**
> OperationResponse sharesDelete(subscriptionId, resourceGroupName, accountName, shareName, apiVersion)

Deletes a share

Delete a share 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ShareApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ShareApi apiInstance = new ShareApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription identifier
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String accountName = "accountName_example"; // String | The name of the share account.
    String shareName = "shareName_example"; // String | The name of the share.
    String apiVersion = "apiVersion_example"; // String | The api version to use.
    try {
      OperationResponse result = apiInstance.sharesDelete(subscriptionId, resourceGroupName, accountName, shareName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ShareApi#sharesDelete");
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
| **subscriptionId** | **String**| The subscription identifier | |
| **resourceGroupName** | **String**| The resource group name. | |
| **accountName** | **String**| The name of the share account. | |
| **shareName** | **String**| The name of the share. | |
| **apiVersion** | **String**| The api version to use. | |

### Return type

[**OperationResponse**](OperationResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **202** | Accepted |  -  |
| **204** | Success |  -  |
| **0** | An error response received from the Microsoft.DataShare resource provider. |  -  |

<a id="sharesGet"></a>
# **sharesGet**
> Share sharesGet(subscriptionId, resourceGroupName, accountName, shareName, apiVersion)

Get a specified share

Get a share 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ShareApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ShareApi apiInstance = new ShareApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription identifier
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String accountName = "accountName_example"; // String | The name of the share account.
    String shareName = "shareName_example"; // String | The name of the share to retrieve.
    String apiVersion = "apiVersion_example"; // String | The api version to use.
    try {
      Share result = apiInstance.sharesGet(subscriptionId, resourceGroupName, accountName, shareName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ShareApi#sharesGet");
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
| **subscriptionId** | **String**| The subscription identifier | |
| **resourceGroupName** | **String**| The resource group name. | |
| **accountName** | **String**| The name of the share account. | |
| **shareName** | **String**| The name of the share to retrieve. | |
| **apiVersion** | **String**| The api version to use. | |

### Return type

[**Share**](Share.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **0** | An error response received from the Microsoft.DataShare resource provider. |  -  |

<a id="sharesListByAccount"></a>
# **sharesListByAccount**
> ShareList sharesListByAccount(subscriptionId, resourceGroupName, accountName, apiVersion, $skipToken)

List of available shares under an account.

List shares in an account

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ShareApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ShareApi apiInstance = new ShareApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription identifier
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String accountName = "accountName_example"; // String | The name of the share account.
    String apiVersion = "apiVersion_example"; // String | The api version to use.
    String $skipToken = "$skipToken_example"; // String | Continuation Token
    try {
      ShareList result = apiInstance.sharesListByAccount(subscriptionId, resourceGroupName, accountName, apiVersion, $skipToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ShareApi#sharesListByAccount");
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
| **subscriptionId** | **String**| The subscription identifier | |
| **resourceGroupName** | **String**| The resource group name. | |
| **accountName** | **String**| The name of the share account. | |
| **apiVersion** | **String**| The api version to use. | |
| **$skipToken** | **String**| Continuation Token | [optional] |

### Return type

[**ShareList**](ShareList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **0** | An error response received from the Microsoft.DataShare resource provider. |  -  |

<a id="sharesListSynchronizationDetails"></a>
# **sharesListSynchronizationDetails**
> SynchronizationDetailsList sharesListSynchronizationDetails(subscriptionId, resourceGroupName, accountName, shareName, apiVersion, shareSynchronization, $skipToken)

List data set level details for a share synchronization

List synchronization details

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ShareApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ShareApi apiInstance = new ShareApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription identifier
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String accountName = "accountName_example"; // String | The name of the share account.
    String shareName = "shareName_example"; // String | The name of the share.
    String apiVersion = "apiVersion_example"; // String | The api version to use.
    ShareSynchronization shareSynchronization = new ShareSynchronization(); // ShareSynchronization | Share Synchronization payload.
    String $skipToken = "$skipToken_example"; // String | Continuation token
    try {
      SynchronizationDetailsList result = apiInstance.sharesListSynchronizationDetails(subscriptionId, resourceGroupName, accountName, shareName, apiVersion, shareSynchronization, $skipToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ShareApi#sharesListSynchronizationDetails");
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
| **subscriptionId** | **String**| The subscription identifier | |
| **resourceGroupName** | **String**| The resource group name. | |
| **accountName** | **String**| The name of the share account. | |
| **shareName** | **String**| The name of the share. | |
| **apiVersion** | **String**| The api version to use. | |
| **shareSynchronization** | [**ShareSynchronization**](ShareSynchronization.md)| Share Synchronization payload. | |
| **$skipToken** | **String**| Continuation token | [optional] |

### Return type

[**SynchronizationDetailsList**](SynchronizationDetailsList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **0** | An error response received from the Microsoft.DataShare resource provider. |  -  |

<a id="sharesListSynchronizations"></a>
# **sharesListSynchronizations**
> ShareSynchronizationList sharesListSynchronizations(subscriptionId, resourceGroupName, accountName, shareName, apiVersion, $skipToken)

List Synchronizations in a share

List synchronizations of a share

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ShareApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ShareApi apiInstance = new ShareApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription identifier
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String accountName = "accountName_example"; // String | The name of the share account.
    String shareName = "shareName_example"; // String | The name of the share.
    String apiVersion = "apiVersion_example"; // String | The api version to use.
    String $skipToken = "$skipToken_example"; // String | Continuation token
    try {
      ShareSynchronizationList result = apiInstance.sharesListSynchronizations(subscriptionId, resourceGroupName, accountName, shareName, apiVersion, $skipToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ShareApi#sharesListSynchronizations");
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
| **subscriptionId** | **String**| The subscription identifier | |
| **resourceGroupName** | **String**| The resource group name. | |
| **accountName** | **String**| The name of the share account. | |
| **shareName** | **String**| The name of the share. | |
| **apiVersion** | **String**| The api version to use. | |
| **$skipToken** | **String**| Continuation token | [optional] |

### Return type

[**ShareSynchronizationList**](ShareSynchronizationList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **0** | An error response received from the Microsoft.DataShare resource provider. |  -  |

