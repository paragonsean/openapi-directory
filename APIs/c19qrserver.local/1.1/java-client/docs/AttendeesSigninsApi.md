# AttendeesSigninsApi

All URIs are relative to *http://c19qrserver.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**signinPost**](AttendeesSigninsApi.md#signinPost) | **POST** /signin |  |
| [**signinSigninIdDelete**](AttendeesSigninsApi.md#signinSigninIdDelete) | **DELETE** /signin/{signinId} | Delete a signin record |
| [**signinSigninIdGet**](AttendeesSigninsApi.md#signinSigninIdGet) | **GET** /signin/{signinId} | Retrieve the information associated with a signin record |
| [**signinSigninIdPut**](AttendeesSigninsApi.md#signinSigninIdPut) | **PUT** /signin/{signinId} | Update a signin record |
| [**signinsGet**](AttendeesSigninsApi.md#signinsGet) | **GET** /signins | Get signin info |


<a id="signinPost"></a>
# **signinPost**
> SigninResponse signinPost(signin)



Create a new signin record

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AttendeesSigninsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://c19qrserver.local");
    
    // Configure API key authorization: TokenHeader
    ApiKeyAuth TokenHeader = (ApiKeyAuth) defaultClient.getAuthentication("TokenHeader");
    TokenHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //TokenHeader.setApiKeyPrefix("Token");

    AttendeesSigninsApi apiInstance = new AttendeesSigninsApi(defaultClient);
    Signin signin = new Signin(); // Signin | 
    try {
      SigninResponse result = apiInstance.signinPost(signin);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AttendeesSigninsApi#signinPost");
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
| **signin** | [**Signin**](Signin.md)|  | [optional] |

### Return type

[**SigninResponse**](SigninResponse.md)

### Authorization

[TokenHeader](../README.md#TokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **401** | Unauthorized |  -  |
| **503** | Key Failure |  -  |

<a id="signinSigninIdDelete"></a>
# **signinSigninIdDelete**
> signinSigninIdDelete(signinId)

Delete a signin record

Delete a signin record       

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AttendeesSigninsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://c19qrserver.local");
    
    // Configure API key authorization: TokenHeader
    ApiKeyAuth TokenHeader = (ApiKeyAuth) defaultClient.getAuthentication("TokenHeader");
    TokenHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //TokenHeader.setApiKeyPrefix("Token");

    AttendeesSigninsApi apiInstance = new AttendeesSigninsApi(defaultClient);
    Integer signinId = 1; // Integer | The ID of the signin record to be deleted.
    try {
      apiInstance.signinSigninIdDelete(signinId);
    } catch (ApiException e) {
      System.err.println("Exception when calling AttendeesSigninsApi#signinSigninIdDelete");
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
| **signinId** | **Integer**| The ID of the signin record to be deleted. | |

### Return type

null (empty response body)

### Authorization

[TokenHeader](../README.md#TokenHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **401** | Unauthorized |  -  |

<a id="signinSigninIdGet"></a>
# **signinSigninIdGet**
> Signin signinSigninIdGet(signinId)

Retrieve the information associated with a signin record

Retrieve the information associated with a signin record 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AttendeesSigninsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://c19qrserver.local");
    
    // Configure API key authorization: TokenHeader
    ApiKeyAuth TokenHeader = (ApiKeyAuth) defaultClient.getAuthentication("TokenHeader");
    TokenHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //TokenHeader.setApiKeyPrefix("Token");

    AttendeesSigninsApi apiInstance = new AttendeesSigninsApi(defaultClient);
    Integer signinId = 1; // Integer | The ID of the signin record to be retrieved.
    try {
      Signin result = apiInstance.signinSigninIdGet(signinId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AttendeesSigninsApi#signinSigninIdGet");
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
| **signinId** | **Integer**| The ID of the signin record to be retrieved. | |

### Return type

[**Signin**](Signin.md)

### Authorization

[TokenHeader](../README.md#TokenHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **401** | Unauthorized |  -  |

<a id="signinSigninIdPut"></a>
# **signinSigninIdPut**
> UserRecord signinSigninIdPut(signinId, signin)

Update a signin record

Update a signin record 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AttendeesSigninsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://c19qrserver.local");
    
    // Configure API key authorization: TokenHeader
    ApiKeyAuth TokenHeader = (ApiKeyAuth) defaultClient.getAuthentication("TokenHeader");
    TokenHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //TokenHeader.setApiKeyPrefix("Token");

    AttendeesSigninsApi apiInstance = new AttendeesSigninsApi(defaultClient);
    Integer signinId = 1; // Integer | The ID of the signin record to be retrieved.
    Signin signin = new Signin(); // Signin | 
    try {
      UserRecord result = apiInstance.signinSigninIdPut(signinId, signin);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AttendeesSigninsApi#signinSigninIdPut");
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
| **signinId** | **Integer**| The ID of the signin record to be retrieved. | |
| **signin** | [**Signin**](Signin.md)|  | [optional] |

### Return type

[**UserRecord**](UserRecord.md)

### Authorization

[TokenHeader](../README.md#TokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **401** | Unauthorized |  -  |

<a id="signinsGet"></a>
# **signinsGet**
> List&lt;Signin&gt; signinsGet(lessThan, returnCount)

Get signin info

Returns a list of signin objects sorted by signin ID descending.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AttendeesSigninsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://c19qrserver.local");
    
    // Configure API key authorization: TokenHeader
    ApiKeyAuth TokenHeader = (ApiKeyAuth) defaultClient.getAuthentication("TokenHeader");
    TokenHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //TokenHeader.setApiKeyPrefix("Token");

    AttendeesSigninsApi apiInstance = new AttendeesSigninsApi(defaultClient);
    Integer lessThan = 56; // Integer | Return signins with IDs less than this value.
    Integer returnCount = 100; // Integer | Return this many objects
    try {
      List<Signin> result = apiInstance.signinsGet(lessThan, returnCount);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AttendeesSigninsApi#signinsGet");
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
| **lessThan** | **Integer**| Return signins with IDs less than this value. | [optional] |
| **returnCount** | **Integer**| Return this many objects | [optional] [default to 100] |

### Return type

[**List&lt;Signin&gt;**](Signin.md)

### Authorization

[TokenHeader](../README.md#TokenHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |
| **401** | Unauthorized |  -  |
| **503** | Key Failure |  -  |

