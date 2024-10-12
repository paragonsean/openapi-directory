# TriggerApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**triggersCreate**](TriggerApi.md#triggersCreate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataShare/accounts/{accountName}/shareSubscriptions/{shareSubscriptionName}/triggers/{triggerName} | This method creates a trigger for a share subscription |
| [**triggersDelete**](TriggerApi.md#triggersDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataShare/accounts/{accountName}/shareSubscriptions/{shareSubscriptionName}/triggers/{triggerName} | Delete Trigger in a shareSubscription. |
| [**triggersGet**](TriggerApi.md#triggersGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataShare/accounts/{accountName}/shareSubscriptions/{shareSubscriptionName}/triggers/{triggerName} | Get Trigger in a shareSubscription. |
| [**triggersListByShareSubscription**](TriggerApi.md#triggersListByShareSubscription) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataShare/accounts/{accountName}/shareSubscriptions/{shareSubscriptionName}/triggers | List Triggers in a share subscription. |


<a id="triggersCreate"></a>
# **triggersCreate**
> Trigger triggersCreate(subscriptionId, resourceGroupName, accountName, shareSubscriptionName, triggerName, apiVersion, trigger)

This method creates a trigger for a share subscription

Create a Trigger 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TriggerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    TriggerApi apiInstance = new TriggerApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription identifier
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String accountName = "accountName_example"; // String | The name of the share account.
    String shareSubscriptionName = "shareSubscriptionName_example"; // String | The name of the share subscription which will hold the data set sink.
    String triggerName = "triggerName_example"; // String | The name of the trigger.
    String apiVersion = "apiVersion_example"; // String | The api version to use.
    Trigger trigger = new Trigger(); // Trigger | Trigger details.
    try {
      Trigger result = apiInstance.triggersCreate(subscriptionId, resourceGroupName, accountName, shareSubscriptionName, triggerName, apiVersion, trigger);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TriggerApi#triggersCreate");
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
| **shareSubscriptionName** | **String**| The name of the share subscription which will hold the data set sink. | |
| **triggerName** | **String**| The name of the trigger. | |
| **apiVersion** | **String**| The api version to use. | |
| **trigger** | [**Trigger**](Trigger.md)| Trigger details. | |

### Return type

[**Trigger**](Trigger.md)

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

<a id="triggersDelete"></a>
# **triggersDelete**
> OperationResponse triggersDelete(subscriptionId, resourceGroupName, accountName, shareSubscriptionName, triggerName, apiVersion)

Delete Trigger in a shareSubscription.

Delete a Trigger in a shareSubscription

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TriggerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    TriggerApi apiInstance = new TriggerApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription identifier
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String accountName = "accountName_example"; // String | The name of the share account.
    String shareSubscriptionName = "shareSubscriptionName_example"; // String | The name of the shareSubscription.
    String triggerName = "triggerName_example"; // String | The name of the trigger.
    String apiVersion = "apiVersion_example"; // String | The api version to use.
    try {
      OperationResponse result = apiInstance.triggersDelete(subscriptionId, resourceGroupName, accountName, shareSubscriptionName, triggerName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TriggerApi#triggersDelete");
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
| **triggerName** | **String**| The name of the trigger. | |
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

<a id="triggersGet"></a>
# **triggersGet**
> Trigger triggersGet(subscriptionId, resourceGroupName, accountName, shareSubscriptionName, triggerName, apiVersion)

Get Trigger in a shareSubscription.

Get a Trigger in a shareSubscription

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TriggerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    TriggerApi apiInstance = new TriggerApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription identifier
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String accountName = "accountName_example"; // String | The name of the share account.
    String shareSubscriptionName = "shareSubscriptionName_example"; // String | The name of the shareSubscription.
    String triggerName = "triggerName_example"; // String | The name of the trigger.
    String apiVersion = "apiVersion_example"; // String | The api version to use.
    try {
      Trigger result = apiInstance.triggersGet(subscriptionId, resourceGroupName, accountName, shareSubscriptionName, triggerName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TriggerApi#triggersGet");
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
| **triggerName** | **String**| The name of the trigger. | |
| **apiVersion** | **String**| The api version to use. | |

### Return type

[**Trigger**](Trigger.md)

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

<a id="triggersListByShareSubscription"></a>
# **triggersListByShareSubscription**
> TriggerList triggersListByShareSubscription(subscriptionId, resourceGroupName, accountName, shareSubscriptionName, apiVersion, $skipToken)

List Triggers in a share subscription.

List Triggers in a share subscription

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TriggerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    TriggerApi apiInstance = new TriggerApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | The subscription identifier
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
    String accountName = "accountName_example"; // String | The name of the share account.
    String shareSubscriptionName = "shareSubscriptionName_example"; // String | The name of the share subscription.
    String apiVersion = "apiVersion_example"; // String | The api version to use.
    String $skipToken = "$skipToken_example"; // String | Continuation token
    try {
      TriggerList result = apiInstance.triggersListByShareSubscription(subscriptionId, resourceGroupName, accountName, shareSubscriptionName, apiVersion, $skipToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TriggerApi#triggersListByShareSubscription");
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

[**TriggerList**](TriggerList.md)

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

