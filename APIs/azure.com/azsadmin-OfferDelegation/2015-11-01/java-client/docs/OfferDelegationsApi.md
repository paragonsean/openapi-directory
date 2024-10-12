# OfferDelegationsApi

All URIs are relative to *https://adminmanagement.local.azurestack.external*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**offerDelegationsCreateOrUpdate**](OfferDelegationsApi.md#offerDelegationsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Subscriptions.Admin/offers/{offer}/offerDelegations/{offerDelegationName} |  |
| [**offerDelegationsDelete**](OfferDelegationsApi.md#offerDelegationsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Subscriptions.Admin/offers/{offer}/offerDelegations/{offerDelegationName} |  |
| [**offerDelegationsGet**](OfferDelegationsApi.md#offerDelegationsGet) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Subscriptions.Admin/offers/{offer}/offerDelegations/{offerDelegationName} |  |
| [**offerDelegationsList**](OfferDelegationsApi.md#offerDelegationsList) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Subscriptions.Admin/offers/{offer}/offerDelegations |  |


<a id="offerDelegationsCreateOrUpdate"></a>
# **offerDelegationsCreateOrUpdate**
> OfferDelegation offerDelegationsCreateOrUpdate(subscriptionId, resourceGroupName, offer, offerDelegationName, apiVersion, newOfferDelegation)



Create or update the offer delegation.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OfferDelegationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://adminmanagement.local.azurestack.external");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    OfferDelegationsApi apiInstance = new OfferDelegationsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription.The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group the resource is located under.
    String offer = "offer_example"; // String | Name of an offer.
    String offerDelegationName = "offerDelegationName_example"; // String | Name of a offer delegation.
    String apiVersion = "2015-11-01"; // String | Client Api Version.
    OfferDelegation newOfferDelegation = new OfferDelegation(); // OfferDelegation | New offer delegation parameter.
    try {
      OfferDelegation result = apiInstance.offerDelegationsCreateOrUpdate(subscriptionId, resourceGroupName, offer, offerDelegationName, apiVersion, newOfferDelegation);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OfferDelegationsApi#offerDelegationsCreateOrUpdate");
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
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription.The subscription ID forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| The resource group the resource is located under. | |
| **offer** | **String**| Name of an offer. | |
| **offerDelegationName** | **String**| Name of a offer delegation. | |
| **apiVersion** | **String**| Client Api Version. | [default to 2015-11-01] |
| **newOfferDelegation** | [**OfferDelegation**](OfferDelegation.md)| New offer delegation parameter. | |

### Return type

[**OfferDelegation**](OfferDelegation.md)

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

<a id="offerDelegationsDelete"></a>
# **offerDelegationsDelete**
> offerDelegationsDelete(subscriptionId, resourceGroupName, offer, offerDelegationName, apiVersion)



Delete the specified offer delegation.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OfferDelegationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://adminmanagement.local.azurestack.external");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    OfferDelegationsApi apiInstance = new OfferDelegationsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription.The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group the resource is located under.
    String offer = "offer_example"; // String | Name of an offer.
    String offerDelegationName = "offerDelegationName_example"; // String | Name of a offer delegation.
    String apiVersion = "2015-11-01"; // String | Client Api Version.
    try {
      apiInstance.offerDelegationsDelete(subscriptionId, resourceGroupName, offer, offerDelegationName, apiVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling OfferDelegationsApi#offerDelegationsDelete");
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
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription.The subscription ID forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| The resource group the resource is located under. | |
| **offer** | **String**| Name of an offer. | |
| **offerDelegationName** | **String**| Name of a offer delegation. | |
| **apiVersion** | **String**| Client Api Version. | [default to 2015-11-01] |

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
| **204** | No Content |  -  |

<a id="offerDelegationsGet"></a>
# **offerDelegationsGet**
> OfferDelegation offerDelegationsGet(subscriptionId, resourceGroupName, offer, offerDelegationName, apiVersion)



Get the specified offer delegation.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OfferDelegationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://adminmanagement.local.azurestack.external");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    OfferDelegationsApi apiInstance = new OfferDelegationsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription.The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group the resource is located under.
    String offer = "offer_example"; // String | Name of an offer.
    String offerDelegationName = "offerDelegationName_example"; // String | Name of a offer delegation.
    String apiVersion = "2015-11-01"; // String | Client Api Version.
    try {
      OfferDelegation result = apiInstance.offerDelegationsGet(subscriptionId, resourceGroupName, offer, offerDelegationName, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OfferDelegationsApi#offerDelegationsGet");
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
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription.The subscription ID forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| The resource group the resource is located under. | |
| **offer** | **String**| Name of an offer. | |
| **offerDelegationName** | **String**| Name of a offer delegation. | |
| **apiVersion** | **String**| Client Api Version. | [default to 2015-11-01] |

### Return type

[**OfferDelegation**](OfferDelegation.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="offerDelegationsList"></a>
# **offerDelegationsList**
> OfferDelegationList offerDelegationsList(subscriptionId, resourceGroupName, offer, apiVersion)



Get the list of offer delegations.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OfferDelegationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://adminmanagement.local.azurestack.external");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    OfferDelegationsApi apiInstance = new OfferDelegationsApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription.The subscription ID forms part of the URI for every service call.
    String resourceGroupName = "resourceGroupName_example"; // String | The resource group the resource is located under.
    String offer = "offer_example"; // String | Name of an offer.
    String apiVersion = "2015-11-01"; // String | Client Api Version.
    try {
      OfferDelegationList result = apiInstance.offerDelegationsList(subscriptionId, resourceGroupName, offer, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OfferDelegationsApi#offerDelegationsList");
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
| **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription.The subscription ID forms part of the URI for every service call. | |
| **resourceGroupName** | **String**| The resource group the resource is located under. | |
| **offer** | **String**| Name of an offer. | |
| **apiVersion** | **String**| Client Api Version. | [default to 2015-11-01] |

### Return type

[**OfferDelegationList**](OfferDelegationList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

