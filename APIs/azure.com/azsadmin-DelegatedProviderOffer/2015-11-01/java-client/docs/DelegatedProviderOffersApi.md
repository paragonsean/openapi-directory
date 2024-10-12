# DelegatedProviderOffersApi

All URIs are relative to *https://adminmanagement.local.azurestack.external*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**delegatedProviderOffersGet**](DelegatedProviderOffersApi.md#delegatedProviderOffersGet) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Subscriptions.Admin/delegatedProviders/{delegatedProviderSubscriptionId}/offers/{offer} |  |
| [**delegatedProviderOffersList**](DelegatedProviderOffersApi.md#delegatedProviderOffersList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Subscriptions.Admin/delegatedProviders/{delegatedProviderSubscriptionId}/offers |  |


<a id="delegatedProviderOffersGet"></a>
# **delegatedProviderOffersGet**
> DelegatedProviderOffer delegatedProviderOffersGet(subscriptionId, delegatedProviderSubscriptionId, offer, apiVersion)



Get the specified delegated provider offer.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DelegatedProviderOffersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://adminmanagement.local.azurestack.external");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DelegatedProviderOffersApi apiInstance = new DelegatedProviderOffersApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription.The subscription ID forms part of the URI for every service call.
    String delegatedProviderSubscriptionId = "delegatedProviderSubscriptionId_example"; // String | Delegated provider subscription identifier.
    String offer = "offer_example"; // String | Name of an offer.
    String apiVersion = "2015-11-01"; // String | Client Api Version.
    try {
      DelegatedProviderOffer result = apiInstance.delegatedProviderOffersGet(subscriptionId, delegatedProviderSubscriptionId, offer, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DelegatedProviderOffersApi#delegatedProviderOffersGet");
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
| **delegatedProviderSubscriptionId** | **String**| Delegated provider subscription identifier. | |
| **offer** | **String**| Name of an offer. | |
| **apiVersion** | **String**| Client Api Version. | [default to 2015-11-01] |

### Return type

[**DelegatedProviderOffer**](DelegatedProviderOffer.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="delegatedProviderOffersList"></a>
# **delegatedProviderOffersList**
> DelegatedProviderOfferList delegatedProviderOffersList(subscriptionId, delegatedProviderSubscriptionId, apiVersion)



Get the list of delegated provider offers.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DelegatedProviderOffersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://adminmanagement.local.azurestack.external");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DelegatedProviderOffersApi apiInstance = new DelegatedProviderOffersApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription.The subscription ID forms part of the URI for every service call.
    String delegatedProviderSubscriptionId = "delegatedProviderSubscriptionId_example"; // String | Delegated provider subscription identifier.
    String apiVersion = "2015-11-01"; // String | Client Api Version.
    try {
      DelegatedProviderOfferList result = apiInstance.delegatedProviderOffersList(subscriptionId, delegatedProviderSubscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DelegatedProviderOffersApi#delegatedProviderOffersList");
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
| **delegatedProviderSubscriptionId** | **String**| Delegated provider subscription identifier. | |
| **apiVersion** | **String**| Client Api Version. | [default to 2015-11-01] |

### Return type

[**DelegatedProviderOfferList**](DelegatedProviderOfferList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

