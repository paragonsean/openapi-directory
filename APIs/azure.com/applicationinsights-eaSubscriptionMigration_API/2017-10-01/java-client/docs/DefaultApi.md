# DefaultApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**eASubscriptionListMigrationDatePost**](DefaultApi.md#eASubscriptionListMigrationDatePost) | **POST** /subscriptions/{subscriptionId}/providers/microsoft.insights/listMigrationdate |  |
| [**eASubscriptionMigrateToNewPricingModelPost**](DefaultApi.md#eASubscriptionMigrateToNewPricingModelPost) | **POST** /subscriptions/{subscriptionId}/providers/microsoft.insights/migrateToNewPricingModel |  |
| [**eASubscriptionRollbackToLegacyPricingModelPost**](DefaultApi.md#eASubscriptionRollbackToLegacyPricingModelPost) | **POST** /subscriptions/{subscriptionId}/providers/microsoft.insights/rollbackToLegacyPricingModel |  |


<a id="eASubscriptionListMigrationDatePost"></a>
# **eASubscriptionListMigrationDatePost**
> EASubscriptionMigrationDate eASubscriptionListMigrationDatePost(apiVersion, subscriptionId)



list date to migrate to new pricing model.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    try {
      EASubscriptionMigrationDate result = apiInstance.eASubscriptionListMigrationDatePost(apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#eASubscriptionListMigrationDatePost");
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
| **apiVersion** | **String**| The API version to use for this operation. | |
| **subscriptionId** | **String**| The ID of the target subscription. | |

### Return type

[**EASubscriptionMigrationDate**](EASubscriptionMigrationDate.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success list migrate date information for this subscription. |  -  |

<a id="eASubscriptionMigrateToNewPricingModelPost"></a>
# **eASubscriptionMigrateToNewPricingModelPost**
> eASubscriptionMigrateToNewPricingModelPost(apiVersion, subscriptionId)



Enterprise Agreement Customer opted to use new pricing model.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    try {
      apiInstance.eASubscriptionMigrateToNewPricingModelPost(apiVersion, subscriptionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#eASubscriptionMigrateToNewPricingModelPost");
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
| **apiVersion** | **String**| The API version to use for this operation. | |
| **subscriptionId** | **String**| The ID of the target subscription. | |

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
| **204** | Success migrate to new pricing model for this subscription. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

<a id="eASubscriptionRollbackToLegacyPricingModelPost"></a>
# **eASubscriptionRollbackToLegacyPricingModelPost**
> eASubscriptionRollbackToLegacyPricingModelPost(apiVersion, subscriptionId)



Enterprise Agreement Customer roll back to use legacy pricing model.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    try {
      apiInstance.eASubscriptionRollbackToLegacyPricingModelPost(apiVersion, subscriptionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#eASubscriptionRollbackToLegacyPricingModelPost");
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
| **apiVersion** | **String**| The API version to use for this operation. | |
| **subscriptionId** | **String**| The ID of the target subscription. | |

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
| **204** | Success roll back to legacy pricing model for this subscription. |  -  |
| **0** | Error response describing why the operation failed. |  -  |

