# PayoutSettingsMerchantLevelApi

All URIs are relative to *https://management-test.adyen.com/v3*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deleteMerchantsMerchantIdPayoutSettingsPayoutSettingsId**](PayoutSettingsMerchantLevelApi.md#deleteMerchantsMerchantIdPayoutSettingsPayoutSettingsId) | **DELETE** /merchants/{merchantId}/payoutSettings/{payoutSettingsId} | Delete a payout setting |
| [**getMerchantsMerchantIdPayoutSettings**](PayoutSettingsMerchantLevelApi.md#getMerchantsMerchantIdPayoutSettings) | **GET** /merchants/{merchantId}/payoutSettings | Get a list of payout settings |
| [**getMerchantsMerchantIdPayoutSettingsPayoutSettingsId**](PayoutSettingsMerchantLevelApi.md#getMerchantsMerchantIdPayoutSettingsPayoutSettingsId) | **GET** /merchants/{merchantId}/payoutSettings/{payoutSettingsId} | Get a payout setting |
| [**patchMerchantsMerchantIdPayoutSettingsPayoutSettingsId**](PayoutSettingsMerchantLevelApi.md#patchMerchantsMerchantIdPayoutSettingsPayoutSettingsId) | **PATCH** /merchants/{merchantId}/payoutSettings/{payoutSettingsId} | Update a payout setting |
| [**postMerchantsMerchantIdPayoutSettings**](PayoutSettingsMerchantLevelApi.md#postMerchantsMerchantIdPayoutSettings) | **POST** /merchants/{merchantId}/payoutSettings | Add a payout setting |


<a id="deleteMerchantsMerchantIdPayoutSettingsPayoutSettingsId"></a>
# **deleteMerchantsMerchantIdPayoutSettingsPayoutSettingsId**
> deleteMerchantsMerchantIdPayoutSettingsPayoutSettingsId(merchantId, payoutSettingsId)

Delete a payout setting

Deletes the payout setting identified in the path.  Use this endpoint if your integration requires it, such as Adyen for Platforms Manage. Your Adyen contact will set up your access.  To make this request, your API credential must have the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions):  * Management API—Payout account settings read and write

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PayoutSettingsMerchantLevelApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management-test.adyen.com/v3");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    PayoutSettingsMerchantLevelApi apiInstance = new PayoutSettingsMerchantLevelApi(defaultClient);
    String merchantId = "merchantId_example"; // String | The unique identifier of the merchant account.
    String payoutSettingsId = "payoutSettingsId_example"; // String | The unique identifier of the payout setting.
    try {
      apiInstance.deleteMerchantsMerchantIdPayoutSettingsPayoutSettingsId(merchantId, payoutSettingsId);
    } catch (ApiException e) {
      System.err.println("Exception when calling PayoutSettingsMerchantLevelApi#deleteMerchantsMerchantIdPayoutSettingsPayoutSettingsId");
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
| **merchantId** | **String**| The unique identifier of the merchant account. | |
| **payoutSettingsId** | **String**| The unique identifier of the payout setting. | |

### Return type

null (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content - look at the actual response code for the status of the request.  |  -  |
| **400** | Bad Request - a problem reading or understanding the request. |  -  |
| **401** | Unauthorized - authentication required. |  -  |
| **403** | Forbidden - insufficient permissions to process the request. |  -  |
| **422** | Unprocessable Entity - a request validation error. |  -  |
| **500** | Internal Server Error - the server could not process the request. |  -  |

<a id="getMerchantsMerchantIdPayoutSettings"></a>
# **getMerchantsMerchantIdPayoutSettings**
> PayoutSettingsResponse getMerchantsMerchantIdPayoutSettings(merchantId)

Get a list of payout settings

Returns the list of payout settings for the merchant account identified in the path.  Use this endpoint if your integration requires it, such as Adyen for Platforms Manage. Your Adyen contact will set up your access.  To make this request, your API credential must have the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Payout account settings read

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PayoutSettingsMerchantLevelApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management-test.adyen.com/v3");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    PayoutSettingsMerchantLevelApi apiInstance = new PayoutSettingsMerchantLevelApi(defaultClient);
    String merchantId = "merchantId_example"; // String | The unique identifier of the merchant account.
    try {
      PayoutSettingsResponse result = apiInstance.getMerchantsMerchantIdPayoutSettings(merchantId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PayoutSettingsMerchantLevelApi#getMerchantsMerchantIdPayoutSettings");
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
| **merchantId** | **String**| The unique identifier of the merchant account. | |

### Return type

[**PayoutSettingsResponse**](PayoutSettingsResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - the request has succeeded. |  -  |
| **204** | No Content - the request has been successfully processed, but there is no additional content. |  -  |
| **400** | Bad Request - a problem reading or understanding the request. |  -  |
| **401** | Unauthorized - authentication required. |  -  |
| **403** | Forbidden - insufficient permissions to process the request. |  -  |
| **422** | Unprocessable Entity - a request validation error. |  -  |
| **500** | Internal Server Error - the server could not process the request. |  -  |

<a id="getMerchantsMerchantIdPayoutSettingsPayoutSettingsId"></a>
# **getMerchantsMerchantIdPayoutSettingsPayoutSettingsId**
> PayoutSettings getMerchantsMerchantIdPayoutSettingsPayoutSettingsId(merchantId, payoutSettingsId)

Get a payout setting

Returns the payout setting identified in the path.  Use this endpoint if your integration requires it, such as Adyen for Platforms Manage. Your Adyen contact will set up your access.  To make this request, your API credential must have the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Payout account settings read

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PayoutSettingsMerchantLevelApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management-test.adyen.com/v3");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    PayoutSettingsMerchantLevelApi apiInstance = new PayoutSettingsMerchantLevelApi(defaultClient);
    String merchantId = "merchantId_example"; // String | The unique identifier of the merchant account.
    String payoutSettingsId = "payoutSettingsId_example"; // String | The unique identifier of the payout setting.
    try {
      PayoutSettings result = apiInstance.getMerchantsMerchantIdPayoutSettingsPayoutSettingsId(merchantId, payoutSettingsId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PayoutSettingsMerchantLevelApi#getMerchantsMerchantIdPayoutSettingsPayoutSettingsId");
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
| **merchantId** | **String**| The unique identifier of the merchant account. | |
| **payoutSettingsId** | **String**| The unique identifier of the payout setting. | |

### Return type

[**PayoutSettings**](PayoutSettings.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - the request has succeeded. |  -  |
| **204** | No Content - the request has been successfully processed, but there is no additional content. |  -  |
| **400** | Bad Request - a problem reading or understanding the request. |  -  |
| **401** | Unauthorized - authentication required. |  -  |
| **403** | Forbidden - insufficient permissions to process the request. |  -  |
| **422** | Unprocessable Entity - a request validation error. |  -  |
| **500** | Internal Server Error - the server could not process the request. |  -  |

<a id="patchMerchantsMerchantIdPayoutSettingsPayoutSettingsId"></a>
# **patchMerchantsMerchantIdPayoutSettingsPayoutSettingsId**
> PayoutSettings patchMerchantsMerchantIdPayoutSettingsPayoutSettingsId(merchantId, payoutSettingsId, updatePayoutSettingsRequest)

Update a payout setting

Updates the payout setting identified in the path. You can enable or disable the payout setting.  Use this endpoint if your integration requires it, such as Adyen for Platforms Manage. Your Adyen contact will set up your access.  To make this request, your API credential must have the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions):  * Management API—Payout account settings read and write

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PayoutSettingsMerchantLevelApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management-test.adyen.com/v3");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    PayoutSettingsMerchantLevelApi apiInstance = new PayoutSettingsMerchantLevelApi(defaultClient);
    String merchantId = "merchantId_example"; // String | The unique identifier of the merchant account.
    String payoutSettingsId = "payoutSettingsId_example"; // String | The unique identifier of the payout setting.
    UpdatePayoutSettingsRequest updatePayoutSettingsRequest = new UpdatePayoutSettingsRequest(); // UpdatePayoutSettingsRequest | 
    try {
      PayoutSettings result = apiInstance.patchMerchantsMerchantIdPayoutSettingsPayoutSettingsId(merchantId, payoutSettingsId, updatePayoutSettingsRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PayoutSettingsMerchantLevelApi#patchMerchantsMerchantIdPayoutSettingsPayoutSettingsId");
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
| **merchantId** | **String**| The unique identifier of the merchant account. | |
| **payoutSettingsId** | **String**| The unique identifier of the payout setting. | |
| **updatePayoutSettingsRequest** | [**UpdatePayoutSettingsRequest**](UpdatePayoutSettingsRequest.md)|  | [optional] |

### Return type

[**PayoutSettings**](PayoutSettings.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - the request has succeeded. |  -  |
| **204** | No Content - the request has been successfully processed, but there is no additional content. |  -  |
| **400** | Bad Request - a problem reading or understanding the request. |  -  |
| **401** | Unauthorized - authentication required. |  -  |
| **403** | Forbidden - insufficient permissions to process the request. |  -  |
| **422** | Unprocessable Entity - a request validation error. |  -  |
| **500** | Internal Server Error - the server could not process the request. |  -  |

<a id="postMerchantsMerchantIdPayoutSettings"></a>
# **postMerchantsMerchantIdPayoutSettings**
> PayoutSettings postMerchantsMerchantIdPayoutSettings(merchantId, payoutSettingsRequest)

Add a payout setting

Sends a request to add a payout setting for the merchant account specified in the path. A payout setting links the merchant account to the [transfer instrument](https://docs.adyen.com/api-explorer/#/legalentity/latest/post/transferInstruments) that contains the details of the payout bank account. Adyen verifies the bank account before allowing and enabling the payout setting.  If you&#39;re accepting payments in multiple currencies, you may add multiple payout settings for the merchant account.  Use this endpoint if your integration requires it, such as Adyen for Platforms Manage. Your Adyen contact will set up your access.  To make this request, your API credential must have the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions):  * Management API—Payout account settings read and write

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PayoutSettingsMerchantLevelApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management-test.adyen.com/v3");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    PayoutSettingsMerchantLevelApi apiInstance = new PayoutSettingsMerchantLevelApi(defaultClient);
    String merchantId = "merchantId_example"; // String | The unique identifier of the merchant account.
    PayoutSettingsRequest payoutSettingsRequest = new PayoutSettingsRequest(); // PayoutSettingsRequest | 
    try {
      PayoutSettings result = apiInstance.postMerchantsMerchantIdPayoutSettings(merchantId, payoutSettingsRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PayoutSettingsMerchantLevelApi#postMerchantsMerchantIdPayoutSettings");
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
| **merchantId** | **String**| The unique identifier of the merchant account. | |
| **payoutSettingsRequest** | [**PayoutSettingsRequest**](PayoutSettingsRequest.md)|  | [optional] |

### Return type

[**PayoutSettings**](PayoutSettings.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - the request has succeeded. |  -  |
| **204** | No Content - the request has been successfully processed, but there is no additional content. |  -  |
| **400** | Bad Request - a problem reading or understanding the request. |  -  |
| **401** | Unauthorized - authentication required. |  -  |
| **403** | Forbidden - insufficient permissions to process the request. |  -  |
| **422** | Unprocessable Entity - a request validation error. |  -  |
| **500** | Internal Server Error - the server could not process the request. |  -  |

