# CustomerSubscriptionApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**customerSubscriptionsCreate**](CustomerSubscriptionApi.md#customerSubscriptionsCreate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroup}/providers/Microsoft.AzureStack/registrations/{registrationName}/customerSubscriptions/{customerSubscriptionName} |  |
| [**customerSubscriptionsDelete**](CustomerSubscriptionApi.md#customerSubscriptionsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroup}/providers/Microsoft.AzureStack/registrations/{registrationName}/customerSubscriptions/{customerSubscriptionName} |  |
| [**customerSubscriptionsGet**](CustomerSubscriptionApi.md#customerSubscriptionsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroup}/providers/Microsoft.AzureStack/registrations/{registrationName}/customerSubscriptions/{customerSubscriptionName} |  |
| [**customerSubscriptionsList**](CustomerSubscriptionApi.md#customerSubscriptionsList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroup}/providers/Microsoft.AzureStack/registrations/{registrationName}/customerSubscriptions |  |


<a id="customerSubscriptionsCreate"></a>
# **customerSubscriptionsCreate**
> CustomerSubscription customerSubscriptionsCreate(subscriptionId, resourceGroup, registrationName, customerSubscriptionName, apiVersion, customerCreationParameters)



Creates a new customer subscription under a registration.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomerSubscriptionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    CustomerSubscriptionApi apiInstance = new CustomerSubscriptionApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroup = "resourceGroup_example"; // String | Name of the resource group.
    String registrationName = "registrationName_example"; // String | Name of the Azure Stack registration.
    String customerSubscriptionName = "customerSubscriptionName_example"; // String | Name of the product.
    String apiVersion = "2017-06-01"; // String | Client API Version.
    CustomerSubscription customerCreationParameters = new CustomerSubscription(); // CustomerSubscription | Parameters use to create a customer subscription.
    try {
      CustomerSubscription result = apiInstance.customerSubscriptionsCreate(subscriptionId, resourceGroup, registrationName, customerSubscriptionName, apiVersion, customerCreationParameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomerSubscriptionApi#customerSubscriptionsCreate");
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
| **subscriptionId** | **String**| Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **resourceGroup** | **String**| Name of the resource group. | |
| **registrationName** | **String**| Name of the Azure Stack registration. | |
| **customerSubscriptionName** | **String**| Name of the product. | |
| **apiVersion** | **String**| Client API Version. | [default to 2017-06-01] |
| **customerCreationParameters** | [**CustomerSubscription**](CustomerSubscription.md)| Parameters use to create a customer subscription. | |

### Return type

[**CustomerSubscription**](CustomerSubscription.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="customerSubscriptionsDelete"></a>
# **customerSubscriptionsDelete**
> customerSubscriptionsDelete(subscriptionId, resourceGroup, registrationName, customerSubscriptionName, apiVersion)



Deletes a customer subscription under a registration.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomerSubscriptionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    CustomerSubscriptionApi apiInstance = new CustomerSubscriptionApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroup = "resourceGroup_example"; // String | Name of the resource group.
    String registrationName = "registrationName_example"; // String | Name of the Azure Stack registration.
    String customerSubscriptionName = "customerSubscriptionName_example"; // String | Name of the product.
    String apiVersion = "2017-06-01"; // String | Client API Version.
    try {
      apiInstance.customerSubscriptionsDelete(subscriptionId, resourceGroup, registrationName, customerSubscriptionName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomerSubscriptionApi#customerSubscriptionsDelete");
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
| **subscriptionId** | **String**| Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **resourceGroup** | **String**| Name of the resource group. | |
| **registrationName** | **String**| Name of the Azure Stack registration. | |
| **customerSubscriptionName** | **String**| Name of the product. | |
| **apiVersion** | **String**| Client API Version. | [default to 2017-06-01] |

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
| **200** | OK |  -  |
| **204** | NO CONTENT |  -  |

<a id="customerSubscriptionsGet"></a>
# **customerSubscriptionsGet**
> CustomerSubscription customerSubscriptionsGet(subscriptionId, resourceGroup, registrationName, customerSubscriptionName, apiVersion)



Returns the specified product.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomerSubscriptionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    CustomerSubscriptionApi apiInstance = new CustomerSubscriptionApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroup = "resourceGroup_example"; // String | Name of the resource group.
    String registrationName = "registrationName_example"; // String | Name of the Azure Stack registration.
    String customerSubscriptionName = "customerSubscriptionName_example"; // String | Name of the product.
    String apiVersion = "2017-06-01"; // String | Client API Version.
    try {
      CustomerSubscription result = apiInstance.customerSubscriptionsGet(subscriptionId, resourceGroup, registrationName, customerSubscriptionName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomerSubscriptionApi#customerSubscriptionsGet");
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
| **subscriptionId** | **String**| Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **resourceGroup** | **String**| Name of the resource group. | |
| **registrationName** | **String**| Name of the Azure Stack registration. | |
| **customerSubscriptionName** | **String**| Name of the product. | |
| **apiVersion** | **String**| Client API Version. | [default to 2017-06-01] |

### Return type

[**CustomerSubscription**](CustomerSubscription.md)

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

<a id="customerSubscriptionsList"></a>
# **customerSubscriptionsList**
> CustomerSubscriptionList customerSubscriptionsList(subscriptionId, resourceGroup, registrationName, apiVersion)



Returns a list of products.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomerSubscriptionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    CustomerSubscriptionApi apiInstance = new CustomerSubscriptionApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String resourceGroup = "resourceGroup_example"; // String | Name of the resource group.
    String registrationName = "registrationName_example"; // String | Name of the Azure Stack registration.
    String apiVersion = "2017-06-01"; // String | Client API Version.
    try {
      CustomerSubscriptionList result = apiInstance.customerSubscriptionsList(subscriptionId, resourceGroup, registrationName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomerSubscriptionApi#customerSubscriptionsList");
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
| **subscriptionId** | **String**| Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **resourceGroup** | **String**| Name of the resource group. | |
| **registrationName** | **String**| Name of the Azure Stack registration. | |
| **apiVersion** | **String**| Client API Version. | [default to 2017-06-01] |

### Return type

[**CustomerSubscriptionList**](CustomerSubscriptionList.md)

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

