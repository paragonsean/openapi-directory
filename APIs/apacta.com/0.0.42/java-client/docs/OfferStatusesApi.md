# OfferStatusesApi

All URIs are relative to *https://app.apacta.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**offerStatusesBulkDeleteDelete**](OfferStatusesApi.md#offerStatusesBulkDeleteDelete) | **DELETE** /offer_statuses/bulkDelete | Bulk delete offer statuses |
| [**offerStatusesGet**](OfferStatusesApi.md#offerStatusesGet) | **GET** /offer_statuses | Get list of offer statuses |
| [**offerStatusesOfferStatusIdDelete**](OfferStatusesApi.md#offerStatusesOfferStatusIdDelete) | **DELETE** /offer_statuses/{offer_status_id} | Delete a offer status |
| [**offerStatusesOfferStatusIdGet**](OfferStatusesApi.md#offerStatusesOfferStatusIdGet) | **GET** /offer_statuses/{offer_status_id} | Get a single offer status |
| [**offerStatusesOfferStatusIdPut**](OfferStatusesApi.md#offerStatusesOfferStatusIdPut) | **PUT** /offer_statuses/{offer_status_id} | Edit a offer status |
| [**offerStatusesPost**](OfferStatusesApi.md#offerStatusesPost) | **POST** /offer_statuses | Create a new offer status |


<a id="offerStatusesBulkDeleteDelete"></a>
# **offerStatusesBulkDeleteDelete**
> EmptySuccessResponse offerStatusesBulkDeleteDelete(bulkActionRequestBody)

Bulk delete offer statuses

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OfferStatusesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.apacta.com/api/v1");

    OfferStatusesApi apiInstance = new OfferStatusesApi(defaultClient);
    BulkActionRequestBody bulkActionRequestBody = new BulkActionRequestBody(); // BulkActionRequestBody | Offer statuses ids
    try {
      EmptySuccessResponse result = apiInstance.offerStatusesBulkDeleteDelete(bulkActionRequestBody);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OfferStatusesApi#offerStatusesBulkDeleteDelete");
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
| **bulkActionRequestBody** | [**BulkActionRequestBody**](BulkActionRequestBody.md)| Offer statuses ids | |

### Return type

[**EmptySuccessResponse**](EmptySuccessResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **403** | Forbidden |  -  |

<a id="offerStatusesGet"></a>
# **offerStatusesGet**
> OfferStatusesGet200Response offerStatusesGet()

Get list of offer statuses

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OfferStatusesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.apacta.com/api/v1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: X-Auth-Token
    ApiKeyAuth X-Auth-Token = (ApiKeyAuth) defaultClient.getAuthentication("X-Auth-Token");
    X-Auth-Token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-Auth-Token.setApiKeyPrefix("Token");

    OfferStatusesApi apiInstance = new OfferStatusesApi(defaultClient);
    try {
      OfferStatusesGet200Response result = apiInstance.offerStatusesGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OfferStatusesApi#offerStatusesGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**OfferStatusesGet200Response**](OfferStatusesGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="offerStatusesOfferStatusIdDelete"></a>
# **offerStatusesOfferStatusIdDelete**
> EmptySuccessResponse offerStatusesOfferStatusIdDelete(offerStatusId)

Delete a offer status

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OfferStatusesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.apacta.com/api/v1");

    OfferStatusesApi apiInstance = new OfferStatusesApi(defaultClient);
    UUID offerStatusId = UUID.randomUUID(); // UUID | 
    try {
      EmptySuccessResponse result = apiInstance.offerStatusesOfferStatusIdDelete(offerStatusId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OfferStatusesApi#offerStatusesOfferStatusIdDelete");
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
| **offerStatusId** | **UUID**|  | |

### Return type

[**EmptySuccessResponse**](EmptySuccessResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **403** | Forbidden |  -  |
| **404** | Record not found |  -  |

<a id="offerStatusesOfferStatusIdGet"></a>
# **offerStatusesOfferStatusIdGet**
> OfferStatusesOfferStatusIdGet200Response offerStatusesOfferStatusIdGet(offerStatusId)

Get a single offer status

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OfferStatusesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.apacta.com/api/v1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: X-Auth-Token
    ApiKeyAuth X-Auth-Token = (ApiKeyAuth) defaultClient.getAuthentication("X-Auth-Token");
    X-Auth-Token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-Auth-Token.setApiKeyPrefix("Token");

    OfferStatusesApi apiInstance = new OfferStatusesApi(defaultClient);
    String offerStatusId = "offerStatusId_example"; // String | 
    try {
      OfferStatusesOfferStatusIdGet200Response result = apiInstance.offerStatusesOfferStatusIdGet(offerStatusId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OfferStatusesApi#offerStatusesOfferStatusIdGet");
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
| **offerStatusId** | **String**|  | |

### Return type

[**OfferStatusesOfferStatusIdGet200Response**](OfferStatusesOfferStatusIdGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | Not found |  -  |

<a id="offerStatusesOfferStatusIdPut"></a>
# **offerStatusesOfferStatusIdPut**
> EmptySuccessResponse offerStatusesOfferStatusIdPut(offerStatusId)

Edit a offer status

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OfferStatusesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.apacta.com/api/v1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: X-Auth-Token
    ApiKeyAuth X-Auth-Token = (ApiKeyAuth) defaultClient.getAuthentication("X-Auth-Token");
    X-Auth-Token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-Auth-Token.setApiKeyPrefix("Token");

    OfferStatusesApi apiInstance = new OfferStatusesApi(defaultClient);
    String offerStatusId = "offerStatusId_example"; // String | 
    try {
      EmptySuccessResponse result = apiInstance.offerStatusesOfferStatusIdPut(offerStatusId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OfferStatusesApi#offerStatusesOfferStatusIdPut");
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
| **offerStatusId** | **String**|  | |

### Return type

[**EmptySuccessResponse**](EmptySuccessResponse.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **403** | Forbidden |  -  |
| **404** | Record Not Found |  -  |
| **422** | Validation error |  -  |

<a id="offerStatusesPost"></a>
# **offerStatusesPost**
> EmptySuccessResponse offerStatusesPost(offerStatusesPostRequest)

Create a new offer status

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OfferStatusesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.apacta.com/api/v1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: X-Auth-Token
    ApiKeyAuth X-Auth-Token = (ApiKeyAuth) defaultClient.getAuthentication("X-Auth-Token");
    X-Auth-Token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-Auth-Token.setApiKeyPrefix("Token");

    OfferStatusesApi apiInstance = new OfferStatusesApi(defaultClient);
    OfferStatusesPostRequest offerStatusesPostRequest = new OfferStatusesPostRequest(); // OfferStatusesPostRequest | 
    try {
      EmptySuccessResponse result = apiInstance.offerStatusesPost(offerStatusesPostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OfferStatusesApi#offerStatusesPost");
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
| **offerStatusesPostRequest** | [**OfferStatusesPostRequest**](OfferStatusesPostRequest.md)|  | |

### Return type

[**EmptySuccessResponse**](EmptySuccessResponse.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **403** | Forbidden |  -  |
| **422** | Validation error |  -  |

