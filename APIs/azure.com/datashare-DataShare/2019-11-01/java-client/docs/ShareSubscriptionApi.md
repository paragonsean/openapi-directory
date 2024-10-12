# ShareSubscriptionApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**consumerSourceDataSetsListByShareSubscription**](ShareSubscriptionApi.md#consumerSourceDataSetsListByShareSubscription) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataShare/accounts/{accountName}/shareSubscriptions/{shareSubscriptionName}/ConsumerSourceDataSets | Get source dataSets of a shareSubscription. |
| [**shareSubscriptionsCancelSynchronization**](ShareSubscriptionApi.md#shareSubscriptionsCancelSynchronization) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataShare/accounts/{accountName}/shareSubscriptions/{shareSubscriptionName}/cancelSynchronization | Request cancellation of a data share snapshot |
| [**shareSubscriptionsCreate**](ShareSubscriptionApi.md#shareSubscriptionsCreate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataShare/accounts/{accountName}/shareSubscriptions/{shareSubscriptionName} | Create shareSubscription in an account. |
| [**shareSubscriptionsDelete**](ShareSubscriptionApi.md#shareSubscriptionsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataShare/accounts/{accountName}/shareSubscriptions/{shareSubscriptionName} | Delete shareSubscription in an account. |
| [**shareSubscriptionsGet**](ShareSubscriptionApi.md#shareSubscriptionsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataShare/accounts/{accountName}/shareSubscriptions/{shareSubscriptionName} | Get shareSubscription in an account. |
| [**shareSubscriptionsListByAccount**](ShareSubscriptionApi.md#shareSubscriptionsListByAccount) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataShare/accounts/{accountName}/shareSubscriptions | List of available share subscriptions under an account. |
| [**shareSubscriptionsListSourceShareSynchronizationSettings**](ShareSubscriptionApi.md#shareSubscriptionsListSourceShareSynchronizationSettings) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataShare/accounts/{accountName}/shareSubscriptions/{shareSubscriptionName}/listSourceShareSynchronizationSettings | Get source share synchronization settings for a shareSubscription. |
| [**shareSubscriptionsListSynchronizationDetails**](ShareSubscriptionApi.md#shareSubscriptionsListSynchronizationDetails) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataShare/accounts/{accountName}/shareSubscriptions/{shareSubscriptionName}/listSynchronizationDetails | List data set level details for a share subscription synchronization |
| [**shareSubscriptionsListSynchronizations**](ShareSubscriptionApi.md#shareSubscriptionsListSynchronizations) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataShare/accounts/{accountName}/shareSubscriptions/{shareSubscriptionName}/listSynchronizations | List Synchronizations in a share subscription. |
| [**shareSubscriptionsSynchronize**](ShareSubscriptionApi.md#shareSubscriptionsSynchronize) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataShare/accounts/{accountName}/shareSubscriptions/{shareSubscriptionName}/Synchronize | Initiate an asynchronous data share job |


<a id="consumerSourceDataSetsListByShareSubscription"></a>
# **consumerSourceDataSetsListByShareSubscription**
> ConsumerSourceDataSetList consumerSourceDataSetsListByShareSubscription(subscriptionId, resourceGroupName, accountName, shareSubscriptionName, apiVersion, $skipToken)

Get source dataSets of a shareSubscription.

Get source dataSets of a shareSubscription

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ShareSubscriptionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ShareSubscriptionApi apiInstance = new ShareSubscriptionApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription identifier
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String accountName = "accountName_example"; // String | The name of the share account.
    String shareSubscriptionName = "shareSubscriptionName_example"; // String | The name of the shareSubscription.
    String apiVersion = "apiVersion_example"; // String | The api version to use.
    String $skipToken = "$skipToken_example"; // String | Continuation token
    try {
      ConsumerSourceDataSetList result = apiInstance.consumerSourceDataSetsListByShareSubscription(subscriptionId, resourceGroupName, accountName, shareSubscriptionName, apiVersion, $skipToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ShareSubscriptionApi#consumerSourceDataSetsListByShareSubscription");
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
| **shareSubscriptionName** | **String**| The name of the shareSubscription. | |
| **apiVersion** | **String**| The api version to use. | |
| **$skipToken** | **String**| Continuation token | [optional] |

### Return type

[**ConsumerSourceDataSetList**](ConsumerSourceDataSetList.md)

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

<a id="shareSubscriptionsCancelSynchronization"></a>
# **shareSubscriptionsCancelSynchronization**
> ShareSubscriptionSynchronization shareSubscriptionsCancelSynchronization(subscriptionId, resourceGroupName, accountName, shareSubscriptionName, apiVersion, shareSubscriptionSynchronization)

Request cancellation of a data share snapshot

Request to cancel a synchronization.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ShareSubscriptionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ShareSubscriptionApi apiInstance = new ShareSubscriptionApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription identifier
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String accountName = "accountName_example"; // String | The name of the share account.
    String shareSubscriptionName = "shareSubscriptionName_example"; // String | The name of the shareSubscription.
    String apiVersion = "apiVersion_example"; // String | The api version to use.
    ShareSubscriptionSynchronization shareSubscriptionSynchronization = new ShareSubscriptionSynchronization(); // ShareSubscriptionSynchronization | Share Subscription Synchronization payload.
    try {
      ShareSubscriptionSynchronization result = apiInstance.shareSubscriptionsCancelSynchronization(subscriptionId, resourceGroupName, accountName, shareSubscriptionName, apiVersion, shareSubscriptionSynchronization);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ShareSubscriptionApi#shareSubscriptionsCancelSynchronization");
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
| **shareSubscriptionName** | **String**| The name of the shareSubscription. | |
| **apiVersion** | **String**| The api version to use. | |
| **shareSubscriptionSynchronization** | [**ShareSubscriptionSynchronization**](ShareSubscriptionSynchronization.md)| Share Subscription Synchronization payload. | |

### Return type

[**ShareSubscriptionSynchronization**](ShareSubscriptionSynchronization.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **202** | Accepted |  -  |
| **0** | An error response received from the Microsoft.DataShare resource provider. |  -  |

<a id="shareSubscriptionsCreate"></a>
# **shareSubscriptionsCreate**
> ShareSubscription shareSubscriptionsCreate(subscriptionId, resourceGroupName, accountName, shareSubscriptionName, apiVersion, shareSubscription)

Create shareSubscription in an account.

Create a shareSubscription in an account

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ShareSubscriptionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ShareSubscriptionApi apiInstance = new ShareSubscriptionApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription identifier
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String accountName = "accountName_example"; // String | The name of the share account.
    String shareSubscriptionName = "shareSubscriptionName_example"; // String | The name of the shareSubscription.
    String apiVersion = "apiVersion_example"; // String | The api version to use.
    ShareSubscription shareSubscription = new ShareSubscription(); // ShareSubscription | create parameters for shareSubscription
    try {
      ShareSubscription result = apiInstance.shareSubscriptionsCreate(subscriptionId, resourceGroupName, accountName, shareSubscriptionName, apiVersion, shareSubscription);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ShareSubscriptionApi#shareSubscriptionsCreate");
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
| **shareSubscriptionName** | **String**| The name of the shareSubscription. | |
| **apiVersion** | **String**| The api version to use. | |
| **shareSubscription** | [**ShareSubscription**](ShareSubscription.md)| create parameters for shareSubscription | |

### Return type

[**ShareSubscription**](ShareSubscription.md)

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

<a id="shareSubscriptionsDelete"></a>
# **shareSubscriptionsDelete**
> OperationResponse shareSubscriptionsDelete(subscriptionId, resourceGroupName, accountName, shareSubscriptionName, apiVersion)

Delete shareSubscription in an account.

Delete a shareSubscription in an account

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ShareSubscriptionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ShareSubscriptionApi apiInstance = new ShareSubscriptionApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription identifier
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String accountName = "accountName_example"; // String | The name of the share account.
    String shareSubscriptionName = "shareSubscriptionName_example"; // String | The name of the shareSubscription.
    String apiVersion = "apiVersion_example"; // String | The api version to use.
    try {
      OperationResponse result = apiInstance.shareSubscriptionsDelete(subscriptionId, resourceGroupName, accountName, shareSubscriptionName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ShareSubscriptionApi#shareSubscriptionsDelete");
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
| **shareSubscriptionName** | **String**| The name of the shareSubscription. | |
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

<a id="shareSubscriptionsGet"></a>
# **shareSubscriptionsGet**
> ShareSubscription shareSubscriptionsGet(subscriptionId, resourceGroupName, accountName, shareSubscriptionName, apiVersion)

Get shareSubscription in an account.

Get a shareSubscription in an account

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ShareSubscriptionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ShareSubscriptionApi apiInstance = new ShareSubscriptionApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription identifier
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String accountName = "accountName_example"; // String | The name of the share account.
    String shareSubscriptionName = "shareSubscriptionName_example"; // String | The name of the shareSubscription.
    String apiVersion = "apiVersion_example"; // String | The api version to use.
    try {
      ShareSubscription result = apiInstance.shareSubscriptionsGet(subscriptionId, resourceGroupName, accountName, shareSubscriptionName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ShareSubscriptionApi#shareSubscriptionsGet");
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
| **shareSubscriptionName** | **String**| The name of the shareSubscription. | |
| **apiVersion** | **String**| The api version to use. | |

### Return type

[**ShareSubscription**](ShareSubscription.md)

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

<a id="shareSubscriptionsListByAccount"></a>
# **shareSubscriptionsListByAccount**
> ShareSubscriptionList shareSubscriptionsListByAccount(subscriptionId, resourceGroupName, accountName, apiVersion, $skipToken)

List of available share subscriptions under an account.

List share subscriptions in an account

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ShareSubscriptionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ShareSubscriptionApi apiInstance = new ShareSubscriptionApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription identifier
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String accountName = "accountName_example"; // String | The name of the share account.
    String apiVersion = "apiVersion_example"; // String | The api version to use.
    String $skipToken = "$skipToken_example"; // String | Continuation Token
    try {
      ShareSubscriptionList result = apiInstance.shareSubscriptionsListByAccount(subscriptionId, resourceGroupName, accountName, apiVersion, $skipToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ShareSubscriptionApi#shareSubscriptionsListByAccount");
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

[**ShareSubscriptionList**](ShareSubscriptionList.md)

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

<a id="shareSubscriptionsListSourceShareSynchronizationSettings"></a>
# **shareSubscriptionsListSourceShareSynchronizationSettings**
> SourceShareSynchronizationSettingList shareSubscriptionsListSourceShareSynchronizationSettings(subscriptionId, resourceGroupName, accountName, shareSubscriptionName, apiVersion, $skipToken)

Get source share synchronization settings for a shareSubscription.

Get synchronization settings set on a share

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ShareSubscriptionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ShareSubscriptionApi apiInstance = new ShareSubscriptionApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription identifier
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String accountName = "accountName_example"; // String | The name of the share account.
    String shareSubscriptionName = "shareSubscriptionName_example"; // String | The name of the shareSubscription.
    String apiVersion = "apiVersion_example"; // String | The api version to use.
    String $skipToken = "$skipToken_example"; // String | Continuation token
    try {
      SourceShareSynchronizationSettingList result = apiInstance.shareSubscriptionsListSourceShareSynchronizationSettings(subscriptionId, resourceGroupName, accountName, shareSubscriptionName, apiVersion, $skipToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ShareSubscriptionApi#shareSubscriptionsListSourceShareSynchronizationSettings");
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
| **shareSubscriptionName** | **String**| The name of the shareSubscription. | |
| **apiVersion** | **String**| The api version to use. | |
| **$skipToken** | **String**| Continuation token | [optional] |

### Return type

[**SourceShareSynchronizationSettingList**](SourceShareSynchronizationSettingList.md)

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

<a id="shareSubscriptionsListSynchronizationDetails"></a>
# **shareSubscriptionsListSynchronizationDetails**
> SynchronizationDetailsList shareSubscriptionsListSynchronizationDetails(subscriptionId, resourceGroupName, accountName, shareSubscriptionName, apiVersion, shareSubscriptionSynchronization, $skipToken)

List data set level details for a share subscription synchronization

List synchronization details

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ShareSubscriptionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ShareSubscriptionApi apiInstance = new ShareSubscriptionApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription identifier
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String accountName = "accountName_example"; // String | The name of the share account.
    String shareSubscriptionName = "shareSubscriptionName_example"; // String | The name of the share subscription.
    String apiVersion = "apiVersion_example"; // String | The api version to use.
    ShareSubscriptionSynchronization shareSubscriptionSynchronization = new ShareSubscriptionSynchronization(); // ShareSubscriptionSynchronization | Share Subscription Synchronization payload.
    String $skipToken = "$skipToken_example"; // String | Continuation token
    try {
      SynchronizationDetailsList result = apiInstance.shareSubscriptionsListSynchronizationDetails(subscriptionId, resourceGroupName, accountName, shareSubscriptionName, apiVersion, shareSubscriptionSynchronization, $skipToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ShareSubscriptionApi#shareSubscriptionsListSynchronizationDetails");
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
| **shareSubscriptionName** | **String**| The name of the share subscription. | |
| **apiVersion** | **String**| The api version to use. | |
| **shareSubscriptionSynchronization** | [**ShareSubscriptionSynchronization**](ShareSubscriptionSynchronization.md)| Share Subscription Synchronization payload. | |
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

<a id="shareSubscriptionsListSynchronizations"></a>
# **shareSubscriptionsListSynchronizations**
> ShareSubscriptionSynchronizationList shareSubscriptionsListSynchronizations(subscriptionId, resourceGroupName, accountName, shareSubscriptionName, apiVersion, $skipToken)

List Synchronizations in a share subscription.

List synchronizations of a share subscription

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ShareSubscriptionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ShareSubscriptionApi apiInstance = new ShareSubscriptionApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription identifier
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String accountName = "accountName_example"; // String | The name of the share account.
    String shareSubscriptionName = "shareSubscriptionName_example"; // String | The name of the share subscription.
    String apiVersion = "apiVersion_example"; // String | The api version to use.
    String $skipToken = "$skipToken_example"; // String | Continuation token
    try {
      ShareSubscriptionSynchronizationList result = apiInstance.shareSubscriptionsListSynchronizations(subscriptionId, resourceGroupName, accountName, shareSubscriptionName, apiVersion, $skipToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ShareSubscriptionApi#shareSubscriptionsListSynchronizations");
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
| **shareSubscriptionName** | **String**| The name of the share subscription. | |
| **apiVersion** | **String**| The api version to use. | |
| **$skipToken** | **String**| Continuation token | [optional] |

### Return type

[**ShareSubscriptionSynchronizationList**](ShareSubscriptionSynchronizationList.md)

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

<a id="shareSubscriptionsSynchronize"></a>
# **shareSubscriptionsSynchronize**
> ShareSubscriptionSynchronization shareSubscriptionsSynchronize(subscriptionId, resourceGroupName, accountName, shareSubscriptionName, apiVersion, synchronize)

Initiate an asynchronous data share job

Initiate a copy

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ShareSubscriptionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    ShareSubscriptionApi apiInstance = new ShareSubscriptionApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription identifier
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String accountName = "accountName_example"; // String | The name of the share account.
    String shareSubscriptionName = "shareSubscriptionName_example"; // String | The name of share subscription
    String apiVersion = "apiVersion_example"; // String | The api version to use.
    Synchronize synchronize = new Synchronize(); // Synchronize | Synchronize payload
    try {
      ShareSubscriptionSynchronization result = apiInstance.shareSubscriptionsSynchronize(subscriptionId, resourceGroupName, accountName, shareSubscriptionName, apiVersion, synchronize);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ShareSubscriptionApi#shareSubscriptionsSynchronize");
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
| **shareSubscriptionName** | **String**| The name of share subscription | |
| **apiVersion** | **String**| The api version to use. | |
| **synchronize** | [**Synchronize**](Synchronize.md)| Synchronize payload | |

### Return type

[**ShareSubscriptionSynchronization**](ShareSubscriptionSynchronization.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **202** | Accepted |  -  |
| **0** | An error response received from the Microsoft.DataShare resource provider. |  -  |

