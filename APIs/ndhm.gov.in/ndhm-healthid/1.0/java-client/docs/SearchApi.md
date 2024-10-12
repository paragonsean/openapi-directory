# SearchApi

All URIs are relative to *https://healthidsbx.ndhm.gov.in/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**searchUserByAccountUsingPOST**](SearchApi.md#searchUserByAccountUsingPOST) | **POST** /v1/search/searchByHealthId | Search a user by Health ID Number. |
| [**searchUserByMobileUsingPOST**](SearchApi.md#searchUserByMobileUsingPOST) | **POST** /v1/search/searchByMobile | Search users with a mobile number. |
| [**searchUserByUseridUsingPOST**](SearchApi.md#searchUserByUseridUsingPOST) | **POST** /v1/search/existsByHealthId | Search a user by Health IDs. |


<a id="searchUserByAccountUsingPOST"></a>
# **searchUserByAccountUsingPOST**
> SearchResponseSingle searchUserByAccountUsingPOST(searchRequest, acceptLanguage)

Search a user by Health ID Number.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SearchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://healthidsbx.ndhm.gov.in/api");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    // Configure API key authorization: X-HIP-ID
    ApiKeyAuth X-HIP-ID = (ApiKeyAuth) defaultClient.getAuthentication("X-HIP-ID");
    X-HIP-ID.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-HIP-ID.setApiKeyPrefix("Token");

    SearchApi apiInstance = new SearchApi(defaultClient);
    SearchByHealthIdRequest searchRequest = new SearchByHealthIdRequest(); // SearchByHealthIdRequest | searchRequest
    String acceptLanguage = "en-US"; // String | 
    try {
      SearchResponseSingle result = apiInstance.searchUserByAccountUsingPOST(searchRequest, acceptLanguage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SearchApi#searchUserByAccountUsingPOST");
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
| **searchRequest** | [**SearchByHealthIdRequest**](SearchByHealthIdRequest.md)| searchRequest | |
| **acceptLanguage** | **String**|  | [optional] [default to en-US] |

### Return type

[**SearchResponseSingle**](SearchResponseSingle.md)

### Authorization

[Authorization](../README.md#Authorization), [X-HIP-ID](../README.md#X-HIP-ID)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **201** | Created |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

<a id="searchUserByMobileUsingPOST"></a>
# **searchUserByMobileUsingPOST**
> SearchResponseSingle searchUserByMobileUsingPOST(searchRequest, acceptLanguage)

Search users with a mobile number.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SearchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://healthidsbx.ndhm.gov.in/api");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    // Configure API key authorization: X-HIP-ID
    ApiKeyAuth X-HIP-ID = (ApiKeyAuth) defaultClient.getAuthentication("X-HIP-ID");
    X-HIP-ID.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-HIP-ID.setApiKeyPrefix("Token");

    SearchApi apiInstance = new SearchApi(defaultClient);
    SearchByMobileRequest searchRequest = new SearchByMobileRequest(); // SearchByMobileRequest | searchRequest
    String acceptLanguage = "en-US"; // String | 
    try {
      SearchResponseSingle result = apiInstance.searchUserByMobileUsingPOST(searchRequest, acceptLanguage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SearchApi#searchUserByMobileUsingPOST");
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
| **searchRequest** | [**SearchByMobileRequest**](SearchByMobileRequest.md)| searchRequest | |
| **acceptLanguage** | **String**|  | [optional] [default to en-US] |

### Return type

[**SearchResponseSingle**](SearchResponseSingle.md)

### Authorization

[Authorization](../README.md#Authorization), [X-HIP-ID](../README.md#X-HIP-ID)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **201** | Created |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

<a id="searchUserByUseridUsingPOST"></a>
# **searchUserByUseridUsingPOST**
> Object searchUserByUseridUsingPOST(searchDTO, acceptLanguage)

Search a user by Health IDs.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SearchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://healthidsbx.ndhm.gov.in/api");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    // Configure API key authorization: X-HIP-ID
    ApiKeyAuth X-HIP-ID = (ApiKeyAuth) defaultClient.getAuthentication("X-HIP-ID");
    X-HIP-ID.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-HIP-ID.setApiKeyPrefix("Token");

    SearchApi apiInstance = new SearchApi(defaultClient);
    SearchByHealthIdRequest searchDTO = new SearchByHealthIdRequest(); // SearchByHealthIdRequest | searchDTO
    String acceptLanguage = "en-US"; // String | 
    try {
      Object result = apiInstance.searchUserByUseridUsingPOST(searchDTO, acceptLanguage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SearchApi#searchUserByUseridUsingPOST");
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
| **searchDTO** | [**SearchByHealthIdRequest**](SearchByHealthIdRequest.md)| searchDTO | |
| **acceptLanguage** | **String**|  | [optional] [default to en-US] |

### Return type

**Object**

### Authorization

[Authorization](../README.md#Authorization), [X-HIP-ID](../README.md#X-HIP-ID)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **201** | Created |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

