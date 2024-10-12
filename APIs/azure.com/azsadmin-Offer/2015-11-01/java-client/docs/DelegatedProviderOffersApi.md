# DelegatedProviderOffersApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**delegatedProviderOffersGet**](DelegatedProviderOffersApi.md#delegatedProviderOffersGet) | **GET** /delegatedProviders/{delegatedProviderId}/offers/{offerName} |  |
| [**delegatedProviderOffersList**](DelegatedProviderOffersApi.md#delegatedProviderOffersList) | **GET** /delegatedProviders/{delegatedProviderId}/offers |  |


<a id="delegatedProviderOffersGet"></a>
# **delegatedProviderOffersGet**
> Offer delegatedProviderOffersGet(delegatedProviderId, offerName, apiVersion)



Get the specified offer for the delegated provider.

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
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DelegatedProviderOffersApi apiInstance = new DelegatedProviderOffersApi(defaultClient);
    String delegatedProviderId = "delegatedProviderId_example"; // String | Id of the delegated provider.
    String offerName = "offerName_example"; // String | Name of the offer.
    String apiVersion = "2015-11-01"; // String | Client Api Version.
    try {
      Offer result = apiInstance.delegatedProviderOffersGet(delegatedProviderId, offerName, apiVersion);
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
| **delegatedProviderId** | **String**| Id of the delegated provider. | |
| **offerName** | **String**| Name of the offer. | |
| **apiVersion** | **String**| Client Api Version. | [default to 2015-11-01] |

### Return type

[**Offer**](Offer.md)

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
> OfferList delegatedProviderOffersList(delegatedProviderId, apiVersion)



Get the list of offers for the specified delegated provider.

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
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DelegatedProviderOffersApi apiInstance = new DelegatedProviderOffersApi(defaultClient);
    String delegatedProviderId = "delegatedProviderId_example"; // String | Id of the delegated provider.
    String apiVersion = "2015-11-01"; // String | Client Api Version.
    try {
      OfferList result = apiInstance.delegatedProviderOffersList(delegatedProviderId, apiVersion);
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
| **delegatedProviderId** | **String**| Id of the delegated provider. | |
| **apiVersion** | **String**| Client Api Version. | [default to 2015-11-01] |

### Return type

[**OfferList**](OfferList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

