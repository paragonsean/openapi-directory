# SkuApprovalSettingsApi

All URIs are relative to *https://vtex.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getaccountconfig**](SkuApprovalSettingsApi.md#getaccountconfig) | **GET** /suggestions/configuration | Get Account&#39;s Approval Settings |
| [**getautoApprovevaluefromconfig**](SkuApprovalSettingsApi.md#getautoApprovevaluefromconfig) | **GET** /suggestions/configuration/autoapproval/toggle | Get autoApprove Status in Account Settings |
| [**getselleraccountconfig**](SkuApprovalSettingsApi.md#getselleraccountconfig) | **GET** /suggestions/configuration/seller/{sellerId} | Get Seller&#39;s Approval Settings |
| [**putselleraccountconfig**](SkuApprovalSettingsApi.md#putselleraccountconfig) | **PUT** /suggestions/configuration/seller/{sellerId} | Save Seller&#39;s Approval Settings |
| [**saveaccountconfig**](SkuApprovalSettingsApi.md#saveaccountconfig) | **PUT** /suggestions/configuration | Save Account&#39;s Approval Settings |
| [**saveautoapproveforaccount**](SkuApprovalSettingsApi.md#saveautoapproveforaccount) | **PUT** /suggestions/configuration/autoapproval/toggle | Activate autoApprove in Marketplace&#39;s Account |
| [**saveautoapproveforaccountseller**](SkuApprovalSettingsApi.md#saveautoapproveforaccountseller) | **PUT** /suggestions/configuration/autoapproval/toggle/seller/{sellerId} | Activate autoApprove Setting for a Seller |


<a id="getaccountconfig"></a>
# **getaccountconfig**
> Getaccountconfig200Response getaccountconfig(accountName, accept, contentType)

Get Account&#39;s Approval Settings

This endpoint retrieves the current approval settings of a marketplace&#39;s Received SKUs module. Its response includes:   - &#x60;Score&#x60;: Matcher scores for approving and rejecting SKUs received from sellers.   - &#x60;Matchers&#x60;: All Matchers configured on the marketplace, and their respective details.   - &#x60;SpecificationsMapping&#x60;: Mapping of product and SKU specifications, per seller.   - &#x60;MatchFlux&#x60;: This field determines the type of approval configuration applied to SKUs received from a seller.   The possible values include:   -&#x60;default&#x60;, where the Matcher reviews the SKU, and approves it based on its score.   -&#x60;manual&#x60;, for manual approvals through the Received SKU UI, or Match API.   -&#x60;autoApprove&#x60;, for every SKU received from a given seller to be approved automatically, regardless of their Matcher Score.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SkuApprovalSettingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    SkuApprovalSettingsApi apiInstance = new SkuApprovalSettingsApi(defaultClient);
    String accountName = "apiexamples"; // String | Name of the VTEX account that belongs to the marketplace. All data extracted, and changes added will be posted into this account.
    String accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    String contentType = "application/json"; // String | Describes the type of the content being sent.
    try {
      Getaccountconfig200Response result = apiInstance.getaccountconfig(accountName, accept, contentType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SkuApprovalSettingsApi#getaccountconfig");
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
| **accountName** | **String**| Name of the VTEX account that belongs to the marketplace. All data extracted, and changes added will be posted into this account. | [default to apiexamples] |
| **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | [default to application/json] |
| **contentType** | **String**| Describes the type of the content being sent. | [default to application/json] |

### Return type

[**Getaccountconfig200Response**](Getaccountconfig200Response.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="getautoApprovevaluefromconfig"></a>
# **getautoApprovevaluefromconfig**
> GetautoApprovevaluefromconfig200Response getautoApprovevaluefromconfig(sellerId, accountName, accept, contentType)

Get autoApprove Status in Account Settings

This endpoint can be used to check whether the autoapprove setting is active or not, for a specific seller.   If the response is &#x60;true&#x60;, the autoapprove setting is active. If the response is &#x60;false&#x60;, it is inactive.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SkuApprovalSettingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    SkuApprovalSettingsApi apiInstance = new SkuApprovalSettingsApi(defaultClient);
    String sellerId = "seller123"; // String | A string that identifies the seller in the marketplace. This ID must be created by the marketplace.
    String accountName = "apiexamples"; // String | Name of the VTEX account that belongs to the marketplace. All data extracted, and changes added will be posted into this account.
    String accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    String contentType = "application/json"; // String | Describes the type of the content being sent.
    try {
      GetautoApprovevaluefromconfig200Response result = apiInstance.getautoApprovevaluefromconfig(sellerId, accountName, accept, contentType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SkuApprovalSettingsApi#getautoApprovevaluefromconfig");
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
| **sellerId** | **String**| A string that identifies the seller in the marketplace. This ID must be created by the marketplace. | [default to seller123] |
| **accountName** | **String**| Name of the VTEX account that belongs to the marketplace. All data extracted, and changes added will be posted into this account. | [default to apiexamples] |
| **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | [default to application/json] |
| **contentType** | **String**| Describes the type of the content being sent. | [default to application/json] |

### Return type

[**GetautoApprovevaluefromconfig200Response**](GetautoApprovevaluefromconfig200Response.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="getselleraccountconfig"></a>
# **getselleraccountconfig**
> getselleraccountconfig(accountName, sellerId, accept, contentType)

Get Seller&#39;s Approval Settings

This endpoint retrieves the current Received SKUs approval settings applied to a specific seller. Its response includes:   - &#x60;sellerId&#x60;: A string that identifies the seller in the marketplace.   - &#x60;accountId&#x60;: Marketplace’s account ID.   - &#x60;accountName&#x60;: Marketplace’s account name.   - &#x60;mapping&#x60;: Mapping of SKU and product Specifications.   - &#x60;matchFlux&#x60;: This field determines the type of approval configuration applied to SKUs received  from a seller.   The possible values include:    -&#x60;default&#x60;, where the Matcher reviews the SKU, and approves it based on its score.   -&#x60;manual&#x60;, for manual approvals through the Received SKU UI and Match API.   -&#x60;autoApprove&#x60;, for every SKU received from a given seller to be approved automatically, regardless of the Matcher Score.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SkuApprovalSettingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    SkuApprovalSettingsApi apiInstance = new SkuApprovalSettingsApi(defaultClient);
    String accountName = "apiexamples"; // String | Name of the VTEX account that belongs to the marketplace. All data extracted, and changes added will be posted into this account.
    String sellerId = "seller123"; // String | A string that identifies the seller in the marketplace. This ID must be created by the marketplace.
    String accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    String contentType = "application/json"; // String | Describes the type of the content being sent.
    try {
      apiInstance.getselleraccountconfig(accountName, sellerId, accept, contentType);
    } catch (ApiException e) {
      System.err.println("Exception when calling SkuApprovalSettingsApi#getselleraccountconfig");
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
| **accountName** | **String**| Name of the VTEX account that belongs to the marketplace. All data extracted, and changes added will be posted into this account. | [default to apiexamples] |
| **sellerId** | **String**| A string that identifies the seller in the marketplace. This ID must be created by the marketplace. | [default to seller123] |
| **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | [default to application/json] |
| **contentType** | **String**| Describes the type of the content being sent. | [default to application/json] |

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="putselleraccountconfig"></a>
# **putselleraccountconfig**
> putselleraccountconfig(accountName, sellerId, accept, contentType, putselleraccountconfigRequest)

Save Seller&#39;s Approval Settings

Marketplaces use this endpoint to create or update approval settings to a specific seller, on the Received SKUs module.   The request includes all the details necessary to implement the chosen approval settings.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SkuApprovalSettingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    SkuApprovalSettingsApi apiInstance = new SkuApprovalSettingsApi(defaultClient);
    String accountName = "apiexamples"; // String | Name of the VTEX account that belongs to the marketplace. All data extracted, and changes added will be posted into this account.
    String sellerId = "seller123"; // String | A string that identifies the seller in the marketplace. This ID must be created by the marketplace.
    String accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    String contentType = "application/json"; // String | Describes the type of the content being sent.
    PutselleraccountconfigRequest putselleraccountconfigRequest = new PutselleraccountconfigRequest(); // PutselleraccountconfigRequest | 
    try {
      apiInstance.putselleraccountconfig(accountName, sellerId, accept, contentType, putselleraccountconfigRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling SkuApprovalSettingsApi#putselleraccountconfig");
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
| **accountName** | **String**| Name of the VTEX account that belongs to the marketplace. All data extracted, and changes added will be posted into this account. | [default to apiexamples] |
| **sellerId** | **String**| A string that identifies the seller in the marketplace. This ID must be created by the marketplace. | [default to seller123] |
| **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | [default to application/json] |
| **contentType** | **String**| Describes the type of the content being sent. | [default to application/json] |
| **putselleraccountconfigRequest** | [**PutselleraccountconfigRequest**](PutselleraccountconfigRequest.md)|  | |

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="saveaccountconfig"></a>
# **saveaccountconfig**
> Saveaccountconfig200Response saveaccountconfig(accountName, accept, contentType, saveaccountconfigRequest)

Save Account&#39;s Approval Settings

Marketplaces use this endpoint to create or update approval settings on their Received SKUs module.   The request includes all the details necessary to implement the chosen approval settings.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SkuApprovalSettingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    SkuApprovalSettingsApi apiInstance = new SkuApprovalSettingsApi(defaultClient);
    String accountName = "apiexamples"; // String | Name of the VTEX account that belongs to the marketplace. All data extracted, and changes added will be posted into this account.
    String accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    String contentType = "application/json"; // String | Describes the type of the content being sent.
    SaveaccountconfigRequest saveaccountconfigRequest = new SaveaccountconfigRequest(); // SaveaccountconfigRequest | 
    try {
      Saveaccountconfig200Response result = apiInstance.saveaccountconfig(accountName, accept, contentType, saveaccountconfigRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SkuApprovalSettingsApi#saveaccountconfig");
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
| **accountName** | **String**| Name of the VTEX account that belongs to the marketplace. All data extracted, and changes added will be posted into this account. | [default to apiexamples] |
| **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | [default to application/json] |
| **contentType** | **String**| Describes the type of the content being sent. | [default to application/json] |
| **saveaccountconfigRequest** | [**SaveaccountconfigRequest**](SaveaccountconfigRequest.md)|  | |

### Return type

[**Saveaccountconfig200Response**](Saveaccountconfig200Response.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="saveautoapproveforaccount"></a>
# **saveautoapproveforaccount**
> Saveautoapproveforaccount200Response saveautoapproveforaccount(accountName, accept, contentType, saveautoapproveforaccountRequest)

Activate autoApprove in Marketplace&#39;s Account

This endpoint enables the autoapprove rule to a marketplace&#39;s whole Received SKUs module. Once enabling the rule, received SKUs will be automatically approved on your store, regardless of the seller.    For the autoapprove rule to work as expected, the approval [Matcher score](https://help.vtex.com/en/tutorial/entendendo-a-pontuacao-do-vtex-matcher--tutorials_424) should be set up as 80 (default value), but you can configure a different number through the field &#x60;Score&#x60; in [Save Account&#39;s Approval Settings](https://developers.vtex.com/vtex-rest-api/reference/saveaccountconfig).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SkuApprovalSettingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    SkuApprovalSettingsApi apiInstance = new SkuApprovalSettingsApi(defaultClient);
    String accountName = "apiexamples"; // String | Name of the VTEX account that belongs to the marketplace. All data extracted, and changes added will be posted into this account.
    String accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    String contentType = "application/json"; // String | Describes the type of the content being sent.
    SaveautoapproveforaccountRequest saveautoapproveforaccountRequest = new SaveautoapproveforaccountRequest(); // SaveautoapproveforaccountRequest | 
    try {
      Saveautoapproveforaccount200Response result = apiInstance.saveautoapproveforaccount(accountName, accept, contentType, saveautoapproveforaccountRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SkuApprovalSettingsApi#saveautoapproveforaccount");
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
| **accountName** | **String**| Name of the VTEX account that belongs to the marketplace. All data extracted, and changes added will be posted into this account. | [default to apiexamples] |
| **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | [default to application/json] |
| **contentType** | **String**| Describes the type of the content being sent. | [default to application/json] |
| **saveautoapproveforaccountRequest** | [**SaveautoapproveforaccountRequest**](SaveautoapproveforaccountRequest.md)|  | |

### Return type

[**Saveautoapproveforaccount200Response**](Saveautoapproveforaccount200Response.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="saveautoapproveforaccountseller"></a>
# **saveautoapproveforaccountseller**
> saveautoapproveforaccountseller(accountName, sellerId, accept, contentType, saveautoapproveforaccountsellerRequest)

Activate autoApprove Setting for a Seller

This endpoint enables the auto approve setting to received SKUs from a specific seller. Be aware that once enabling the rule through this request, all received SKUs from that seller will be automatically approved on your store, regardless of the Matcher Score.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SkuApprovalSettingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    SkuApprovalSettingsApi apiInstance = new SkuApprovalSettingsApi(defaultClient);
    String accountName = "apiexamples"; // String | Name of the VTEX account that belongs to the marketplace. All data extracted, and changes added will be posted into this account.
    String sellerId = "seller123"; // String | A string that identifies the seller in the marketplace. This ID must be created by the marketplace.
    String accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    String contentType = "application/json"; // String | Describes the type of the content being sent.
    SaveautoapproveforaccountsellerRequest saveautoapproveforaccountsellerRequest = new SaveautoapproveforaccountsellerRequest(); // SaveautoapproveforaccountsellerRequest | 
    try {
      apiInstance.saveautoapproveforaccountseller(accountName, sellerId, accept, contentType, saveautoapproveforaccountsellerRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling SkuApprovalSettingsApi#saveautoapproveforaccountseller");
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
| **accountName** | **String**| Name of the VTEX account that belongs to the marketplace. All data extracted, and changes added will be posted into this account. | [default to apiexamples] |
| **sellerId** | **String**| A string that identifies the seller in the marketplace. This ID must be created by the marketplace. | [default to seller123] |
| **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | [default to application/json] |
| **contentType** | **String**| Describes the type of the content being sent. | [default to application/json] |
| **saveautoapproveforaccountsellerRequest** | [**SaveautoapproveforaccountsellerRequest**](SaveautoapproveforaccountsellerRequest.md)|  | |

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

