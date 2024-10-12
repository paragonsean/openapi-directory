# DefaultApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**marketplaceAgreementsCancel**](DefaultApi.md#marketplaceAgreementsCancel) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.MarketplaceOrdering/agreements/{publisherId}/offers/{offerId}/plans/{planId}/cancel |  |
| [**marketplaceAgreementsCreate**](DefaultApi.md#marketplaceAgreementsCreate) | **PUT** /subscriptions/{subscriptionId}/providers/Microsoft.MarketplaceOrdering/offerTypes/{offerType}/publishers/{publisherId}/offers/{offerId}/plans/{planId}/agreements/current |  |
| [**marketplaceAgreementsGet**](DefaultApi.md#marketplaceAgreementsGet) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.MarketplaceOrdering/offerTypes/{offerType}/publishers/{publisherId}/offers/{offerId}/plans/{planId}/agreements/current |  |
| [**marketplaceAgreementsGetAgreement**](DefaultApi.md#marketplaceAgreementsGetAgreement) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.MarketplaceOrdering/agreements/{publisherId}/offers/{offerId}/plans/{planId} |  |
| [**marketplaceAgreementsList**](DefaultApi.md#marketplaceAgreementsList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.MarketplaceOrdering/agreements |  |
| [**marketplaceAgreementsSign**](DefaultApi.md#marketplaceAgreementsSign) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.MarketplaceOrdering/agreements/{publisherId}/offers/{offerId}/plans/{planId}/sign |  |


<a id="marketplaceAgreementsCancel"></a>
# **marketplaceAgreementsCancel**
> AgreementTerms marketplaceAgreementsCancel(apiVersion, subscriptionId, publisherId, offerId, planId)



Cancel marketplace terms.

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
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String publisherId = "publisherId_example"; // String | Publisher identifier string of image being deployed.
    String offerId = "offerId_example"; // String | Offer identifier string of image being deployed.
    String planId = "planId_example"; // String | Plan identifier string of image being deployed.
    try {
      AgreementTerms result = apiInstance.marketplaceAgreementsCancel(apiVersion, subscriptionId, publisherId, offerId, planId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#marketplaceAgreementsCancel");
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
| **apiVersion** | **String**| The API version to use for the request. | |
| **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | |
| **publisherId** | **String**| Publisher identifier string of image being deployed. | |
| **offerId** | **String**| Offer identifier string of image being deployed. | |
| **planId** | **String**| Plan identifier string of image being deployed. | |

### Return type

[**AgreementTerms**](AgreementTerms.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. The request was successfully processed and the terms were rejected. |  -  |
| **0** | Microsoft.MarketplaceOrdering error response describing why the operation failed. |  -  |

<a id="marketplaceAgreementsCreate"></a>
# **marketplaceAgreementsCreate**
> AgreementTerms marketplaceAgreementsCreate(apiVersion, offerType, subscriptionId, publisherId, offerId, planId, parameters)



Save marketplace terms.

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
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    String offerType = "virtualmachine"; // String | Offer Type, currently only virtualmachine type is supported.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String publisherId = "publisherId_example"; // String | Publisher identifier string of image being deployed.
    String offerId = "offerId_example"; // String | Offer identifier string of image being deployed.
    String planId = "planId_example"; // String | Plan identifier string of image being deployed.
    AgreementTerms parameters = new AgreementTerms(); // AgreementTerms | Parameters supplied to the Create Marketplace Terms operation.
    try {
      AgreementTerms result = apiInstance.marketplaceAgreementsCreate(apiVersion, offerType, subscriptionId, publisherId, offerId, planId, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#marketplaceAgreementsCreate");
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
| **apiVersion** | **String**| The API version to use for the request. | |
| **offerType** | **String**| Offer Type, currently only virtualmachine type is supported. | [enum: virtualmachine] |
| **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | |
| **publisherId** | **String**| Publisher identifier string of image being deployed. | |
| **offerId** | **String**| Offer identifier string of image being deployed. | |
| **planId** | **String**| Plan identifier string of image being deployed. | |
| **parameters** | [**AgreementTerms**](AgreementTerms.md)| Parameters supplied to the Create Marketplace Terms operation. | |

### Return type

[**AgreementTerms**](AgreementTerms.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. The request was successfully processed and the terms were accepted or acceptance revoked as per the request body. |  -  |
| **0** | Microsoft.MarketplaceOrdering error response describing why the operation failed. |  -  |

<a id="marketplaceAgreementsGet"></a>
# **marketplaceAgreementsGet**
> AgreementTerms marketplaceAgreementsGet(apiVersion, subscriptionId, offerType, publisherId, offerId, planId)



Get marketplace terms.

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
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String offerType = "virtualmachine"; // String | Offer Type, currently only virtualmachine type is supported.
    String publisherId = "publisherId_example"; // String | Publisher identifier string of image being deployed.
    String offerId = "offerId_example"; // String | Offer identifier string of image being deployed.
    String planId = "planId_example"; // String | Plan identifier string of image being deployed.
    try {
      AgreementTerms result = apiInstance.marketplaceAgreementsGet(apiVersion, subscriptionId, offerType, publisherId, offerId, planId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#marketplaceAgreementsGet");
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
| **apiVersion** | **String**| The API version to use for the request. | |
| **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | |
| **offerType** | **String**| Offer Type, currently only virtualmachine type is supported. | [enum: virtualmachine] |
| **publisherId** | **String**| Publisher identifier string of image being deployed. | |
| **offerId** | **String**| Offer identifier string of image being deployed. | |
| **planId** | **String**| Plan identifier string of image being deployed. | |

### Return type

[**AgreementTerms**](AgreementTerms.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Terms returned successfully |  -  |

<a id="marketplaceAgreementsGetAgreement"></a>
# **marketplaceAgreementsGetAgreement**
> AgreementTerms marketplaceAgreementsGetAgreement(apiVersion, subscriptionId, publisherId, offerId, planId)



Get marketplace agreement.

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
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String publisherId = "publisherId_example"; // String | Publisher identifier string of image being deployed.
    String offerId = "offerId_example"; // String | Offer identifier string of image being deployed.
    String planId = "planId_example"; // String | Plan identifier string of image being deployed.
    try {
      AgreementTerms result = apiInstance.marketplaceAgreementsGetAgreement(apiVersion, subscriptionId, publisherId, offerId, planId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#marketplaceAgreementsGetAgreement");
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
| **apiVersion** | **String**| The API version to use for the request. | |
| **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | |
| **publisherId** | **String**| Publisher identifier string of image being deployed. | |
| **offerId** | **String**| Offer identifier string of image being deployed. | |
| **planId** | **String**| Plan identifier string of image being deployed. | |

### Return type

[**AgreementTerms**](AgreementTerms.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Terms returned successfully |  -  |

<a id="marketplaceAgreementsList"></a>
# **marketplaceAgreementsList**
> List&lt;AgreementTerms&gt; marketplaceAgreementsList(apiVersion, subscriptionId)



List marketplace agreements in the subscription.

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
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    try {
      List<AgreementTerms> result = apiInstance.marketplaceAgreementsList(apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#marketplaceAgreementsList");
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
| **apiVersion** | **String**| The API version to use for the request. | |
| **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | |

### Return type

[**List&lt;AgreementTerms&gt;**](AgreementTerms.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Terms returned successfully |  -  |

<a id="marketplaceAgreementsSign"></a>
# **marketplaceAgreementsSign**
> AgreementTerms marketplaceAgreementsSign(apiVersion, subscriptionId, publisherId, offerId, planId)



Sign marketplace terms.

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
    String apiVersion = "apiVersion_example"; // String | The API version to use for the request.
    String subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
    String publisherId = "publisherId_example"; // String | Publisher identifier string of image being deployed.
    String offerId = "offerId_example"; // String | Offer identifier string of image being deployed.
    String planId = "planId_example"; // String | Plan identifier string of image being deployed.
    try {
      AgreementTerms result = apiInstance.marketplaceAgreementsSign(apiVersion, subscriptionId, publisherId, offerId, planId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#marketplaceAgreementsSign");
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
| **apiVersion** | **String**| The API version to use for the request. | |
| **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | |
| **publisherId** | **String**| Publisher identifier string of image being deployed. | |
| **offerId** | **String**| Offer identifier string of image being deployed. | |
| **planId** | **String**| Plan identifier string of image being deployed. | |

### Return type

[**AgreementTerms**](AgreementTerms.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. The request was successfully processed and the terms were accepted. |  -  |
| **0** | Microsoft.MarketplaceOrdering error response describing why the operation failed. |  -  |

