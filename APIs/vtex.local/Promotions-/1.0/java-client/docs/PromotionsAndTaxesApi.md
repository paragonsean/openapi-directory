# PromotionsAndTaxesApi

All URIs are relative to *https://vtex.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiRnbPvtImportCalculatorConfigurationPost**](PromotionsAndTaxesApi.md#apiRnbPvtImportCalculatorConfigurationPost) | **POST** /api/rnb/pvt/import/calculatorConfiguration | Create Multiple SKU Promotion |
| [**apiRnbPvtImportCalculatorConfigurationPromotionIdPut**](PromotionsAndTaxesApi.md#apiRnbPvtImportCalculatorConfigurationPromotionIdPut) | **PUT** /api/rnb/pvt/import/calculatorConfiguration/{promotionId} | Update Multiple SKU Promotion |
| [**archivePromotion**](PromotionsAndTaxesApi.md#archivePromotion) | **POST** /api/rnb/pvt/archive/calculatorConfiguration/{idCalculatorConfiguration} | Archive Promotion or Tax |
| [**createOrUpdateCalculatorConfiguration**](PromotionsAndTaxesApi.md#createOrUpdateCalculatorConfiguration) | **POST** /api/rnb/pvt/calculatorconfiguration | Create or Update Promotion or Tax |
| [**getAllBenefits**](PromotionsAndTaxesApi.md#getAllBenefits) | **GET** /api/rnb/pvt/benefits/calculatorconfiguration | Get All Promotions |
| [**getAllTaxes**](PromotionsAndTaxesApi.md#getAllTaxes) | **GET** /api/rnb/pvt/taxes/calculatorconfiguration | Get All Taxes |
| [**getArchivedPromotions**](PromotionsAndTaxesApi.md#getArchivedPromotions) | **GET** /api/rnb/pvt/archive/benefits/calculatorConfiguration | List Archived Promotions |
| [**getArchivedTaxes**](PromotionsAndTaxesApi.md#getArchivedTaxes) | **GET** /api/rnb/pvt/archive/taxes/calculatorConfiguration | List Archived Taxes |
| [**getCalculatorConfigurationById**](PromotionsAndTaxesApi.md#getCalculatorConfigurationById) | **GET** /api/rnb/pvt/calculatorconfiguration/{idCalculatorConfiguration} | Get Promotion or Tax by ID |
| [**unarchivePromotion**](PromotionsAndTaxesApi.md#unarchivePromotion) | **POST** /api/rnb/pvt/unarchive/calculatorConfiguration/{idCalculatorConfiguration} | Unarchive Promotion or Tax |


<a id="apiRnbPvtImportCalculatorConfigurationPost"></a>
# **apiRnbPvtImportCalculatorConfigurationPost**
> apiRnbPvtImportCalculatorConfigurationPost(contentType, accept, xVTEXCalculatorName, xVTEXStartDate, xVTEXEndDate, xVTEXAccumulateWithManualPrices, xVTEXCumulative, xVTEXClusterOperator, xVTEXClusterExpression, body)

Create Multiple SKU Promotion

Creates a Multiple SKU Promotion. This scenario allows to create a single promotion for multiples SKUs with the Percentage Effect.   &gt; ⚠️   &gt;  &gt; The limit of SKUs on a Multiple Effects promotion is 400.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PromotionsAndTaxesApi;

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

    PromotionsAndTaxesApi apiInstance = new PromotionsAndTaxesApi(defaultClient);
    String contentType = "text/csv"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    String xVTEXCalculatorName = "Test"; // String | Promotion Name.
    String xVTEXStartDate = "2020-08-18T16:00:00+3:00"; // String | Promotion start date.
    String xVTEXEndDate = "2020-08-18T16:30:00+3:00"; // String | Promotion end date.
    Boolean xVTEXAccumulateWithManualPrices = false; // Boolean | Condition that will accumulate the Promotion with manual prices or not.
    Boolean xVTEXCumulative = false; // Boolean | Defines if the Promotion is cumulative with other promotions.
    String xVTEXClusterOperator = "any"; // String | This header allows implementing the Promotion in multiples client clusters. You can set the value as `all` - the Promotion will be valid to all the clusters - or `any` - the Promotion will be valid to any of the clusters.
    String xVTEXClusterExpression = "cluster_name=true"; // String | Cluster that will be included in the Promotion. To add multiple clusters, create a header for each one of them.
    File body = new File("/path/to/file"); // File | 
    try {
      apiInstance.apiRnbPvtImportCalculatorConfigurationPost(contentType, accept, xVTEXCalculatorName, xVTEXStartDate, xVTEXEndDate, xVTEXAccumulateWithManualPrices, xVTEXCumulative, xVTEXClusterOperator, xVTEXClusterExpression, body);
    } catch (ApiException e) {
      System.err.println("Exception when calling PromotionsAndTaxesApi#apiRnbPvtImportCalculatorConfigurationPost");
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
| **contentType** | **String**| Type of the content being sent. | |
| **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | [default to application/json] |
| **xVTEXCalculatorName** | **String**| Promotion Name. | |
| **xVTEXStartDate** | **String**| Promotion start date. | |
| **xVTEXEndDate** | **String**| Promotion end date. | |
| **xVTEXAccumulateWithManualPrices** | **Boolean**| Condition that will accumulate the Promotion with manual prices or not. | |
| **xVTEXCumulative** | **Boolean**| Defines if the Promotion is cumulative with other promotions. | [optional] |
| **xVTEXClusterOperator** | **String**| This header allows implementing the Promotion in multiples client clusters. You can set the value as &#x60;all&#x60; - the Promotion will be valid to all the clusters - or &#x60;any&#x60; - the Promotion will be valid to any of the clusters. | [optional] |
| **xVTEXClusterExpression** | **String**| Cluster that will be included in the Promotion. To add multiple clusters, create a header for each one of them. | [optional] |
| **body** | **File**|  | [optional] |

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: text/csv
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="apiRnbPvtImportCalculatorConfigurationPromotionIdPut"></a>
# **apiRnbPvtImportCalculatorConfigurationPromotionIdPut**
> apiRnbPvtImportCalculatorConfigurationPromotionIdPut(contentType, accept, xVTEXCalculatorName, xVTEXStartDate, xVTEXEndDate, xVTEXAccumulateWithManualPrices, promotionId, xVTEXCumulative, xVTEXClusterOperator, xVTEXClusterExpression, body)

Update Multiple SKU Promotion

Updates information from a Multiple SKU Promotion. This scenario allows to create a single promotion for multiples SKUs with the Percentage Effect.    &gt; ⚠️   &gt;  &gt; The limit of SKUs on a Multiple Effects promotion is 400.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PromotionsAndTaxesApi;

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

    PromotionsAndTaxesApi apiInstance = new PromotionsAndTaxesApi(defaultClient);
    String contentType = "text/csv"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    String xVTEXCalculatorName = "Test"; // String | Promotion Name.
    String xVTEXStartDate = "2020-08-18T16:00:00+3:00"; // String | Promotion start date.
    String xVTEXEndDate = "2020-08-18T16:30:00+3:00"; // String | Promotion end date.
    Boolean xVTEXAccumulateWithManualPrices = false; // Boolean | Condition that will accumulate the Promotion with manual prices or not.
    String promotionId = "dc6b6f59-ec2b-4a13-8490-0d1e0c53ddf9"; // String | Promotion unique identifier.
    Boolean xVTEXCumulative = false; // Boolean | Defines if the Promotion is cumulative with other promotions.
    String xVTEXClusterOperator = "any"; // String | This header allows implementing the Promotion in multiples client clusters. You can set the value as `all` - the Promotion will be valid to all the clusters - or `any` - the Promotion will be valid to any of the clusters.
    String xVTEXClusterExpression = "cluster_name=true"; // String | Cluster that will be included in the Promotion. To add multiple clusters, create a header for each one of them.
    File body = new File("/path/to/file"); // File | 
    try {
      apiInstance.apiRnbPvtImportCalculatorConfigurationPromotionIdPut(contentType, accept, xVTEXCalculatorName, xVTEXStartDate, xVTEXEndDate, xVTEXAccumulateWithManualPrices, promotionId, xVTEXCumulative, xVTEXClusterOperator, xVTEXClusterExpression, body);
    } catch (ApiException e) {
      System.err.println("Exception when calling PromotionsAndTaxesApi#apiRnbPvtImportCalculatorConfigurationPromotionIdPut");
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
| **contentType** | **String**| Type of the content being sent. | |
| **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | [default to application/json] |
| **xVTEXCalculatorName** | **String**| Promotion Name. | |
| **xVTEXStartDate** | **String**| Promotion start date. | |
| **xVTEXEndDate** | **String**| Promotion end date. | |
| **xVTEXAccumulateWithManualPrices** | **Boolean**| Condition that will accumulate the Promotion with manual prices or not. | |
| **promotionId** | **String**| Promotion unique identifier. | |
| **xVTEXCumulative** | **Boolean**| Defines if the Promotion is cumulative with other promotions. | [optional] |
| **xVTEXClusterOperator** | **String**| This header allows implementing the Promotion in multiples client clusters. You can set the value as &#x60;all&#x60; - the Promotion will be valid to all the clusters - or &#x60;any&#x60; - the Promotion will be valid to any of the clusters. | [optional] |
| **xVTEXClusterExpression** | **String**| Cluster that will be included in the Promotion. To add multiple clusters, create a header for each one of them. | [optional] |
| **body** | **File**|  | [optional] |

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: text/csv
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Accepted |  -  |

<a id="archivePromotion"></a>
# **archivePromotion**
> archivePromotion(contentType, accept, idCalculatorConfiguration)

Archive Promotion or Tax

Archives a Promotion or Tax by its ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PromotionsAndTaxesApi;

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

    PromotionsAndTaxesApi apiInstance = new PromotionsAndTaxesApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    String idCalculatorConfiguration = "d8a1cd2e-b667-4054-b3ae-b79124c7218e"; // String | Promotion ID or tax ID.
    try {
      apiInstance.archivePromotion(contentType, accept, idCalculatorConfiguration);
    } catch (ApiException e) {
      System.err.println("Exception when calling PromotionsAndTaxesApi#archivePromotion");
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
| **contentType** | **String**| Type of the content being sent. | [default to application/json] |
| **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | [default to application/json] |
| **idCalculatorConfiguration** | **String**| Promotion ID or tax ID. | |

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
| **204** | No Content |  -  |

<a id="createOrUpdateCalculatorConfiguration"></a>
# **createOrUpdateCalculatorConfiguration**
> CreateOrUpdateCalculatorConfiguration200Response createOrUpdateCalculatorConfiguration(contentType, accept, createOrUpdateCalculatorConfigurationRequest)

Create or Update Promotion or Tax

Creates or updates a specific Promotion by its Promotion ID or a specific Tax by its Tax ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PromotionsAndTaxesApi;

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

    PromotionsAndTaxesApi apiInstance = new PromotionsAndTaxesApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    CreateOrUpdateCalculatorConfigurationRequest createOrUpdateCalculatorConfigurationRequest = new CreateOrUpdateCalculatorConfigurationRequest(); // CreateOrUpdateCalculatorConfigurationRequest | 
    try {
      CreateOrUpdateCalculatorConfiguration200Response result = apiInstance.createOrUpdateCalculatorConfiguration(contentType, accept, createOrUpdateCalculatorConfigurationRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PromotionsAndTaxesApi#createOrUpdateCalculatorConfiguration");
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
| **contentType** | **String**| Type of the content being sent. | [default to application/json] |
| **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | [default to application/json] |
| **createOrUpdateCalculatorConfigurationRequest** | [**CreateOrUpdateCalculatorConfigurationRequest**](CreateOrUpdateCalculatorConfigurationRequest.md)|  | |

### Return type

[**CreateOrUpdateCalculatorConfiguration200Response**](CreateOrUpdateCalculatorConfiguration200Response.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="getAllBenefits"></a>
# **getAllBenefits**
> GetAllBenefits200Response getAllBenefits(contentType, accept)

Get All Promotions

Retrieves all promotions from an account.     &gt; 📘 Onboarding guide   &gt;  &gt; Check the new [Promotions onboarding guide](https://developers.vtex.com/vtex-rest-api/docs/promotions-overview). We created this guide to improve the onboarding experience for developers at VTEX. It assembles all documentation on our Developer Portal about the Promotions and is organized by focusing on the developer&#39;s journey.    

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PromotionsAndTaxesApi;

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

    PromotionsAndTaxesApi apiInstance = new PromotionsAndTaxesApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    try {
      GetAllBenefits200Response result = apiInstance.getAllBenefits(contentType, accept);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PromotionsAndTaxesApi#getAllBenefits");
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
| **contentType** | **String**| Type of the content being sent. | [default to application/json] |
| **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | [default to application/json] |

### Return type

[**GetAllBenefits200Response**](GetAllBenefits200Response.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="getAllTaxes"></a>
# **getAllTaxes**
> GetAllTaxes200Response getAllTaxes(contentType, accept)

Get All Taxes

Retrieves all taxes from an account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PromotionsAndTaxesApi;

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

    PromotionsAndTaxesApi apiInstance = new PromotionsAndTaxesApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    try {
      GetAllTaxes200Response result = apiInstance.getAllTaxes(contentType, accept);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PromotionsAndTaxesApi#getAllTaxes");
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
| **contentType** | **String**| Type of the content being sent. | [default to application/json] |
| **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | [default to application/json] |

### Return type

[**GetAllTaxes200Response**](GetAllTaxes200Response.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="getArchivedPromotions"></a>
# **getArchivedPromotions**
> GetArchivedPromotions200Response getArchivedPromotions(contentType, accept)

List Archived Promotions

Lists all archived promotions.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PromotionsAndTaxesApi;

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

    PromotionsAndTaxesApi apiInstance = new PromotionsAndTaxesApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    try {
      GetArchivedPromotions200Response result = apiInstance.getArchivedPromotions(contentType, accept);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PromotionsAndTaxesApi#getArchivedPromotions");
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
| **contentType** | **String**| Type of the content being sent. | [default to application/json] |
| **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | [default to application/json] |

### Return type

[**GetArchivedPromotions200Response**](GetArchivedPromotions200Response.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="getArchivedTaxes"></a>
# **getArchivedTaxes**
> GetArchivedTaxes200Response getArchivedTaxes(contentType, accept)

List Archived Taxes

Lists all archived taxes.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PromotionsAndTaxesApi;

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

    PromotionsAndTaxesApi apiInstance = new PromotionsAndTaxesApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    try {
      GetArchivedTaxes200Response result = apiInstance.getArchivedTaxes(contentType, accept);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PromotionsAndTaxesApi#getArchivedTaxes");
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
| **contentType** | **String**| Type of the content being sent. | [default to application/json] |
| **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | [default to application/json] |

### Return type

[**GetArchivedTaxes200Response**](GetArchivedTaxes200Response.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="getCalculatorConfigurationById"></a>
# **getCalculatorConfigurationById**
> GetCalculatorConfigurationById200Response getCalculatorConfigurationById(contentType, accept, idCalculatorConfiguration)

Get Promotion or Tax by ID

Retrieves a specific promotion by its Promotion ID or a specific tax by its Tax ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PromotionsAndTaxesApi;

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

    PromotionsAndTaxesApi apiInstance = new PromotionsAndTaxesApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    String idCalculatorConfiguration = "d8a1cd2e-b667-4054-b3ae-b79124c7218e"; // String | Promotion ID or tax ID.
    try {
      GetCalculatorConfigurationById200Response result = apiInstance.getCalculatorConfigurationById(contentType, accept, idCalculatorConfiguration);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PromotionsAndTaxesApi#getCalculatorConfigurationById");
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
| **contentType** | **String**| Type of the content being sent. | [default to application/json] |
| **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | [default to application/json] |
| **idCalculatorConfiguration** | **String**| Promotion ID or tax ID. | |

### Return type

[**GetCalculatorConfigurationById200Response**](GetCalculatorConfigurationById200Response.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Promotion, Tax

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="unarchivePromotion"></a>
# **unarchivePromotion**
> unarchivePromotion(contentType, accept, idCalculatorConfiguration)

Unarchive Promotion or Tax

Unarchives a Promotion or Tax by its ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PromotionsAndTaxesApi;

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

    PromotionsAndTaxesApi apiInstance = new PromotionsAndTaxesApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    String idCalculatorConfiguration = "d8a1cd2e-b667-4054-b3ae-b79124c7218e"; // String | Promotion ID or tax ID.
    try {
      apiInstance.unarchivePromotion(contentType, accept, idCalculatorConfiguration);
    } catch (ApiException e) {
      System.err.println("Exception when calling PromotionsAndTaxesApi#unarchivePromotion");
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
| **contentType** | **String**| Type of the content being sent. | [default to application/json] |
| **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | [default to application/json] |
| **idCalculatorConfiguration** | **String**| Promotion ID or tax ID. | |

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
| **204** | No Content |  -  |

