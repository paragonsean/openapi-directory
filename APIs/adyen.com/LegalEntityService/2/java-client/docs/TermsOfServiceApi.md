# TermsOfServiceApi

All URIs are relative to *https://kyc-test.adyen.com/lem/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getLegalEntitiesIdTermsOfServiceAcceptanceInfos**](TermsOfServiceApi.md#getLegalEntitiesIdTermsOfServiceAcceptanceInfos) | **GET** /legalEntities/{id}/termsOfServiceAcceptanceInfos | Get Terms of Service information for a legal entity |
| [**getLegalEntitiesIdTermsOfServiceStatus**](TermsOfServiceApi.md#getLegalEntitiesIdTermsOfServiceStatus) | **GET** /legalEntities/{id}/termsOfServiceStatus | Get Terms of Service status |
| [**patchLegalEntitiesIdTermsOfServiceTermsofservicedocumentid**](TermsOfServiceApi.md#patchLegalEntitiesIdTermsOfServiceTermsofservicedocumentid) | **PATCH** /legalEntities/{id}/termsOfService/{termsofservicedocumentid} | Accept Terms of Service |
| [**postLegalEntitiesIdTermsOfService**](TermsOfServiceApi.md#postLegalEntitiesIdTermsOfService) | **POST** /legalEntities/{id}/termsOfService | Get Terms of Service document |


<a id="getLegalEntitiesIdTermsOfServiceAcceptanceInfos"></a>
# **getLegalEntitiesIdTermsOfServiceAcceptanceInfos**
> GetTermsOfServiceAcceptanceInfosResponse getLegalEntitiesIdTermsOfServiceAcceptanceInfos(id)

Get Terms of Service information for a legal entity

Returns Terms of Service information for a legal entity.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TermsOfServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://kyc-test.adyen.com/lem/v2");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    TermsOfServiceApi apiInstance = new TermsOfServiceApi(defaultClient);
    String id = "id_example"; // String | The unique identifier of the legal entity. For sole proprietorships, this is the individual legal entity ID of the owner.
    try {
      GetTermsOfServiceAcceptanceInfosResponse result = apiInstance.getLegalEntitiesIdTermsOfServiceAcceptanceInfos(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TermsOfServiceApi#getLegalEntitiesIdTermsOfServiceAcceptanceInfos");
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
| **id** | **String**| The unique identifier of the legal entity. For sole proprietorships, this is the individual legal entity ID of the owner. | |

### Return type

[**GetTermsOfServiceAcceptanceInfosResponse**](GetTermsOfServiceAcceptanceInfosResponse.md)

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

<a id="getLegalEntitiesIdTermsOfServiceStatus"></a>
# **getLegalEntitiesIdTermsOfServiceStatus**
> CalculateTermsOfServiceStatusResponse getLegalEntitiesIdTermsOfServiceStatus(id)

Get Terms of Service status

Returns the required types of Terms of Service that need to be accepted by a legal entity.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TermsOfServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://kyc-test.adyen.com/lem/v2");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    TermsOfServiceApi apiInstance = new TermsOfServiceApi(defaultClient);
    String id = "id_example"; // String | The unique identifier of the legal entity. For sole proprietorships, this is the individual legal entity ID of the owner.
    try {
      CalculateTermsOfServiceStatusResponse result = apiInstance.getLegalEntitiesIdTermsOfServiceStatus(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TermsOfServiceApi#getLegalEntitiesIdTermsOfServiceStatus");
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
| **id** | **String**| The unique identifier of the legal entity. For sole proprietorships, this is the individual legal entity ID of the owner. | |

### Return type

[**CalculateTermsOfServiceStatusResponse**](CalculateTermsOfServiceStatusResponse.md)

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

<a id="patchLegalEntitiesIdTermsOfServiceTermsofservicedocumentid"></a>
# **patchLegalEntitiesIdTermsOfServiceTermsofservicedocumentid**
> AcceptTermsOfServiceResponse patchLegalEntitiesIdTermsOfServiceTermsofservicedocumentid(id, termsofservicedocumentid, acceptTermsOfServiceRequest)

Accept Terms of Service

Accepts Terms of Service.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TermsOfServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://kyc-test.adyen.com/lem/v2");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    TermsOfServiceApi apiInstance = new TermsOfServiceApi(defaultClient);
    String id = "id_example"; // String | The unique identifier of the legal entity. For sole proprietorships, this is the individual legal entity ID of the owner.
    String termsofservicedocumentid = "termsofservicedocumentid_example"; // String | The unique identifier of the Terms of Service document.
    AcceptTermsOfServiceRequest acceptTermsOfServiceRequest = new AcceptTermsOfServiceRequest(); // AcceptTermsOfServiceRequest | 
    try {
      AcceptTermsOfServiceResponse result = apiInstance.patchLegalEntitiesIdTermsOfServiceTermsofservicedocumentid(id, termsofservicedocumentid, acceptTermsOfServiceRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TermsOfServiceApi#patchLegalEntitiesIdTermsOfServiceTermsofservicedocumentid");
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
| **id** | **String**| The unique identifier of the legal entity. For sole proprietorships, this is the individual legal entity ID of the owner. | |
| **termsofservicedocumentid** | **String**| The unique identifier of the Terms of Service document. | |
| **acceptTermsOfServiceRequest** | [**AcceptTermsOfServiceRequest**](AcceptTermsOfServiceRequest.md)|  | [optional] |

### Return type

[**AcceptTermsOfServiceResponse**](AcceptTermsOfServiceResponse.md)

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

<a id="postLegalEntitiesIdTermsOfService"></a>
# **postLegalEntitiesIdTermsOfService**
> GetTermsOfServiceDocumentResponse postLegalEntitiesIdTermsOfService(id, getTermsOfServiceDocumentRequest)

Get Terms of Service document

Returns the Terms of Service document for a legal entity.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TermsOfServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://kyc-test.adyen.com/lem/v2");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    TermsOfServiceApi apiInstance = new TermsOfServiceApi(defaultClient);
    String id = "id_example"; // String | The unique identifier of the legal entity. For sole proprietorships, this is the individual legal entity ID of the owner.
    GetTermsOfServiceDocumentRequest getTermsOfServiceDocumentRequest = new GetTermsOfServiceDocumentRequest(); // GetTermsOfServiceDocumentRequest | 
    try {
      GetTermsOfServiceDocumentResponse result = apiInstance.postLegalEntitiesIdTermsOfService(id, getTermsOfServiceDocumentRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TermsOfServiceApi#postLegalEntitiesIdTermsOfService");
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
| **id** | **String**| The unique identifier of the legal entity. For sole proprietorships, this is the individual legal entity ID of the owner. | |
| **getTermsOfServiceDocumentRequest** | [**GetTermsOfServiceDocumentRequest**](GetTermsOfServiceDocumentRequest.md)|  | [optional] |

### Return type

[**GetTermsOfServiceDocumentResponse**](GetTermsOfServiceDocumentResponse.md)

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

