# LegalEntitiesApi

All URIs are relative to *https://kyc-test.adyen.com/lem/v3*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getLegalEntitiesId**](LegalEntitiesApi.md#getLegalEntitiesId) | **GET** /legalEntities/{id} | Get a legal entity |
| [**getLegalEntitiesIdBusinessLines**](LegalEntitiesApi.md#getLegalEntitiesIdBusinessLines) | **GET** /legalEntities/{id}/businessLines | Get all business lines under a legal entity |
| [**patchLegalEntitiesId**](LegalEntitiesApi.md#patchLegalEntitiesId) | **PATCH** /legalEntities/{id} | Update a legal entity |
| [**postLegalEntities**](LegalEntitiesApi.md#postLegalEntities) | **POST** /legalEntities | Create a legal entity |
| [**postLegalEntitiesIdCheckVerificationErrors**](LegalEntitiesApi.md#postLegalEntitiesIdCheckVerificationErrors) | **POST** /legalEntities/{id}/checkVerificationErrors | Check a legal entity&#39;s verification errors |
| [**postLegalEntitiesIdConfirmDataReview**](LegalEntitiesApi.md#postLegalEntitiesIdConfirmDataReview) | **POST** /legalEntities/{id}/confirmDataReview | Confirm data review |


<a id="getLegalEntitiesId"></a>
# **getLegalEntitiesId**
> LegalEntity getLegalEntitiesId(id)

Get a legal entity

Returns a legal entity.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LegalEntitiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://kyc-test.adyen.com/lem/v3");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    LegalEntitiesApi apiInstance = new LegalEntitiesApi(defaultClient);
    String id = "id_example"; // String | The unique identifier of the legal entity.
    try {
      LegalEntity result = apiInstance.getLegalEntitiesId(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LegalEntitiesApi#getLegalEntitiesId");
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
| **id** | **String**| The unique identifier of the legal entity. | |

### Return type

[**LegalEntity**](LegalEntity.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - the request has succeeded. |  -  |
| **400** | Bad Request - a problem reading or understanding the request. |  -  |
| **401** | Unauthorized - authentication required. |  -  |
| **403** | Forbidden - insufficient permissions to process the request. |  -  |
| **422** | Unprocessable Entity - a request validation error. |  -  |
| **500** | Internal Server Error - the server could not process the request. |  -  |

<a id="getLegalEntitiesIdBusinessLines"></a>
# **getLegalEntitiesIdBusinessLines**
> BusinessLines getLegalEntitiesIdBusinessLines(id)

Get all business lines under a legal entity

Returns the business lines owned by a legal entity.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LegalEntitiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://kyc-test.adyen.com/lem/v3");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    LegalEntitiesApi apiInstance = new LegalEntitiesApi(defaultClient);
    String id = "id_example"; // String | The unique identifier of the legal entity.
    try {
      BusinessLines result = apiInstance.getLegalEntitiesIdBusinessLines(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LegalEntitiesApi#getLegalEntitiesIdBusinessLines");
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
| **id** | **String**| The unique identifier of the legal entity. | |

### Return type

[**BusinessLines**](BusinessLines.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - the request has succeeded. |  -  |
| **400** | Bad Request - a problem reading or understanding the request. |  -  |
| **401** | Unauthorized - authentication required. |  -  |
| **403** | Forbidden - insufficient permissions to process the request. |  -  |
| **422** | Unprocessable Entity - a request validation error. |  -  |
| **500** | Internal Server Error - the server could not process the request. |  -  |

<a id="patchLegalEntitiesId"></a>
# **patchLegalEntitiesId**
> LegalEntity patchLegalEntitiesId(id, xRequestedVerificationCode, legalEntityInfo)

Update a legal entity

Updates a legal entity.   &gt;To change the legal entity type, include only the new &#x60;type&#x60; in your request. To update the &#x60;entityAssociations&#x60; array, you need to replace the entire array. For example, if the array has 3 entries and you want to remove 1 entry, you need to PATCH the resource with the remaining 2 entries.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LegalEntitiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://kyc-test.adyen.com/lem/v3");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    LegalEntitiesApi apiInstance = new LegalEntitiesApi(defaultClient);
    String id = "id_example"; // String | The unique identifier of the legal entity.
    String xRequestedVerificationCode = "1"; // String | Use the requested verification code 0_0001 to resolve any suberrors associated with the legal entity. Requested verification codes can only be used in your test environment.
    LegalEntityInfo legalEntityInfo = new LegalEntityInfo(); // LegalEntityInfo | 
    try {
      LegalEntity result = apiInstance.patchLegalEntitiesId(id, xRequestedVerificationCode, legalEntityInfo);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LegalEntitiesApi#patchLegalEntitiesId");
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
| **id** | **String**| The unique identifier of the legal entity. | |
| **xRequestedVerificationCode** | **String**| Use the requested verification code 0_0001 to resolve any suberrors associated with the legal entity. Requested verification codes can only be used in your test environment. | [optional] |
| **legalEntityInfo** | [**LegalEntityInfo**](LegalEntityInfo.md)|  | [optional] |

### Return type

[**LegalEntity**](LegalEntity.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - the request has succeeded. |  -  |
| **400** | Bad Request - a problem reading or understanding the request. |  -  |
| **401** | Unauthorized - authentication required. |  -  |
| **403** | Forbidden - insufficient permissions to process the request. |  -  |
| **422** | Unprocessable Entity - a request validation error. |  -  |
| **500** | Internal Server Error - the server could not process the request. |  -  |

<a id="postLegalEntities"></a>
# **postLegalEntities**
> LegalEntity postLegalEntities(xRequestedVerificationCode, legalEntityInfoRequiredType)

Create a legal entity

Creates a legal entity.   This resource contains information about the user that will be onboarded in your platform. Adyen uses this information to perform verification checks as required by payment industry regulations. Adyen informs you of the verification results through webhooks or API responses.   &gt;If you are using hosted onboarding and just beginning your integration, use v3 for your API requests. Otherwise, use v2.  

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LegalEntitiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://kyc-test.adyen.com/lem/v3");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    LegalEntitiesApi apiInstance = new LegalEntitiesApi(defaultClient);
    String xRequestedVerificationCode = "13004"; // String | Use a suberror code as your requested verification code. You can include one code at a time in your request header. Requested verification codes can only be used in your test environment.
    LegalEntityInfoRequiredType legalEntityInfoRequiredType = new LegalEntityInfoRequiredType(); // LegalEntityInfoRequiredType | 
    try {
      LegalEntity result = apiInstance.postLegalEntities(xRequestedVerificationCode, legalEntityInfoRequiredType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LegalEntitiesApi#postLegalEntities");
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
| **xRequestedVerificationCode** | **String**| Use a suberror code as your requested verification code. You can include one code at a time in your request header. Requested verification codes can only be used in your test environment. | [optional] |
| **legalEntityInfoRequiredType** | [**LegalEntityInfoRequiredType**](LegalEntityInfoRequiredType.md)|  | [optional] |

### Return type

[**LegalEntity**](LegalEntity.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - the request has succeeded. |  -  |
| **400** | Bad Request - a problem reading or understanding the request. |  -  |
| **401** | Unauthorized - authentication required. |  -  |
| **403** | Forbidden - insufficient permissions to process the request. |  -  |
| **422** | Unprocessable Entity - a request validation error. |  -  |
| **500** | Internal Server Error - the server could not process the request. |  -  |

<a id="postLegalEntitiesIdCheckVerificationErrors"></a>
# **postLegalEntitiesIdCheckVerificationErrors**
> VerificationErrors postLegalEntitiesIdCheckVerificationErrors(id)

Check a legal entity&#39;s verification errors

Returns the verification errors for a legal entity and its supporting entities.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LegalEntitiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://kyc-test.adyen.com/lem/v3");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    LegalEntitiesApi apiInstance = new LegalEntitiesApi(defaultClient);
    String id = "id_example"; // String | The unique identifier of the legal entity.
    try {
      VerificationErrors result = apiInstance.postLegalEntitiesIdCheckVerificationErrors(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LegalEntitiesApi#postLegalEntitiesIdCheckVerificationErrors");
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
| **id** | **String**| The unique identifier of the legal entity. | |

### Return type

[**VerificationErrors**](VerificationErrors.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - the request has succeeded. |  -  |
| **400** | Bad Request - a problem reading or understanding the request. |  -  |
| **401** | Unauthorized - authentication required. |  -  |
| **403** | Forbidden - insufficient permissions to process the request. |  -  |
| **422** | Unprocessable Entity - a request validation error. |  -  |
| **500** | Internal Server Error - the server could not process the request. |  -  |

<a id="postLegalEntitiesIdConfirmDataReview"></a>
# **postLegalEntitiesIdConfirmDataReview**
> DataReviewConfirmationResponse postLegalEntitiesIdConfirmDataReview(id)

Confirm data review

Confirms that your user has reviewed the data for the legal entity specified in the path. Call this endpoint to inform Adyen that your user reviewed and verified that the data is up-to-date. The endpoint returns the timestamp of when Adyen received the request.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LegalEntitiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://kyc-test.adyen.com/lem/v3");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    LegalEntitiesApi apiInstance = new LegalEntitiesApi(defaultClient);
    String id = "id_example"; // String | The unique identifier of the legal entity.
    try {
      DataReviewConfirmationResponse result = apiInstance.postLegalEntitiesIdConfirmDataReview(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LegalEntitiesApi#postLegalEntitiesIdConfirmDataReview");
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
| **id** | **String**| The unique identifier of the legal entity. | |

### Return type

[**DataReviewConfirmationResponse**](DataReviewConfirmationResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - the request has succeeded. |  -  |
| **400** | Bad Request - a problem reading or understanding the request. |  -  |
| **401** | Unauthorized - authentication required. |  -  |
| **403** | Forbidden - insufficient permissions to process the request. |  -  |
| **422** | Unprocessable Entity - a request validation error. |  -  |
| **500** | Internal Server Error - the server could not process the request. |  -  |

