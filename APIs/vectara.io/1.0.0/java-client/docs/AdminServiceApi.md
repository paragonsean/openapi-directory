# AdminServiceApi

All URIs are relative to *https://api.vectara.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createCorpus**](AdminServiceApi.md#createCorpus) | **POST** /v1/create-corpus |  |
| [**deleteCorpus**](AdminServiceApi.md#deleteCorpus) | **POST** /v1/delete-corpus |  |
| [**listCorpora**](AdminServiceApi.md#listCorpora) | **POST** /v1/list-corpora |  |
| [**resetCorpus**](AdminServiceApi.md#resetCorpus) | **POST** /v1/reset-corpus |  |


<a id="createCorpus"></a>
# **createCorpus**
> AdminCreateCorpusResponse createCorpus(customerId, adminCreateCorpusRequest)



Create Corpus

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AdminServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.vectara.io");
    
    // Configure OAuth2 access token for authorization: oAuth
    OAuth oAuth = (OAuth) defaultClient.getAuthentication("oAuth");
    oAuth.setAccessToken("YOUR ACCESS TOKEN");

    AdminServiceApi apiInstance = new AdminServiceApi(defaultClient);
    Integer customerId = 56; // Integer | The Customer ID to use for the request.
    AdminCreateCorpusRequest adminCreateCorpusRequest = new AdminCreateCorpusRequest(); // AdminCreateCorpusRequest | 
    try {
      AdminCreateCorpusResponse result = apiInstance.createCorpus(customerId, adminCreateCorpusRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AdminServiceApi#createCorpus");
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
| **customerId** | **Integer**| The Customer ID to use for the request. | |
| **adminCreateCorpusRequest** | [**AdminCreateCorpusRequest**](AdminCreateCorpusRequest.md)|  | |

### Return type

[**AdminCreateCorpusResponse**](AdminCreateCorpusResponse.md)

### Authorization

[oAuth](../README.md#oAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A successful response. |  -  |
| **0** | An unexpected error response. |  -  |

<a id="deleteCorpus"></a>
# **deleteCorpus**
> AdminDeleteCorpusResponse deleteCorpus(customerId, adminDeleteCorpusRequest)



Delete Corpus

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AdminServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.vectara.io");
    
    // Configure OAuth2 access token for authorization: oAuth
    OAuth oAuth = (OAuth) defaultClient.getAuthentication("oAuth");
    oAuth.setAccessToken("YOUR ACCESS TOKEN");

    AdminServiceApi apiInstance = new AdminServiceApi(defaultClient);
    Integer customerId = 56; // Integer | The Customer ID to use for the request.
    AdminDeleteCorpusRequest adminDeleteCorpusRequest = new AdminDeleteCorpusRequest(); // AdminDeleteCorpusRequest | 
    try {
      AdminDeleteCorpusResponse result = apiInstance.deleteCorpus(customerId, adminDeleteCorpusRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AdminServiceApi#deleteCorpus");
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
| **customerId** | **Integer**| The Customer ID to use for the request. | |
| **adminDeleteCorpusRequest** | [**AdminDeleteCorpusRequest**](AdminDeleteCorpusRequest.md)|  | |

### Return type

[**AdminDeleteCorpusResponse**](AdminDeleteCorpusResponse.md)

### Authorization

[oAuth](../README.md#oAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A successful response. |  -  |
| **0** | An unexpected error response. |  -  |

<a id="listCorpora"></a>
# **listCorpora**
> AdminListCorporaResponse listCorpora(customerId, adminListCorporaRequest)



List Corpora

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AdminServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.vectara.io");
    
    // Configure OAuth2 access token for authorization: oAuth
    OAuth oAuth = (OAuth) defaultClient.getAuthentication("oAuth");
    oAuth.setAccessToken("YOUR ACCESS TOKEN");

    AdminServiceApi apiInstance = new AdminServiceApi(defaultClient);
    Integer customerId = 56; // Integer | The Customer ID to use for the request.
    AdminListCorporaRequest adminListCorporaRequest = new AdminListCorporaRequest(); // AdminListCorporaRequest | 
    try {
      AdminListCorporaResponse result = apiInstance.listCorpora(customerId, adminListCorporaRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AdminServiceApi#listCorpora");
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
| **customerId** | **Integer**| The Customer ID to use for the request. | |
| **adminListCorporaRequest** | [**AdminListCorporaRequest**](AdminListCorporaRequest.md)|  | |

### Return type

[**AdminListCorporaResponse**](AdminListCorporaResponse.md)

### Authorization

[oAuth](../README.md#oAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A successful response. |  -  |
| **0** | An unexpected error response. |  -  |

<a id="resetCorpus"></a>
# **resetCorpus**
> AdminResetCorpusResponse resetCorpus(customerId, adminResetCorpusRequest)



Reset Corpus

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AdminServiceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.vectara.io");
    
    // Configure OAuth2 access token for authorization: oAuth
    OAuth oAuth = (OAuth) defaultClient.getAuthentication("oAuth");
    oAuth.setAccessToken("YOUR ACCESS TOKEN");

    AdminServiceApi apiInstance = new AdminServiceApi(defaultClient);
    Integer customerId = 56; // Integer | The Customer ID to use for the request.
    AdminResetCorpusRequest adminResetCorpusRequest = new AdminResetCorpusRequest(); // AdminResetCorpusRequest | 
    try {
      AdminResetCorpusResponse result = apiInstance.resetCorpus(customerId, adminResetCorpusRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AdminServiceApi#resetCorpus");
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
| **customerId** | **Integer**| The Customer ID to use for the request. | |
| **adminResetCorpusRequest** | [**AdminResetCorpusRequest**](AdminResetCorpusRequest.md)|  | |

### Return type

[**AdminResetCorpusResponse**](AdminResetCorpusResponse.md)

### Authorization

[oAuth](../README.md#oAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A successful response. |  -  |
| **0** | An unexpected error response. |  -  |

