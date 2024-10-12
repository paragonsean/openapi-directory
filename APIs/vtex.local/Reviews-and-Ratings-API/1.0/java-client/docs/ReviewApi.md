# ReviewApi

All URIs are relative to *https://vtex.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deleteMultipleReviews**](ReviewApi.md#deleteMultipleReviews) | **DELETE** /reviews | Delete Multiple Reviews |
| [**deleteReview**](ReviewApi.md#deleteReview) | **DELETE** /review/{reviewId} | Delete Review |
| [**editReview**](ReviewApi.md#editReview) | **PATCH** /review/{reviewId} | Update a Review |
| [**getReviewbyReviewId**](ReviewApi.md#getReviewbyReviewId) | **GET** /review/{reviewId} | Get Review by Review ID |
| [**getalistofReviews**](ReviewApi.md#getalistofReviews) | **GET** /reviews | Get a list of Reviews |
| [**saveMultipleReviews**](ReviewApi.md#saveMultipleReviews) | **POST** /reviews | Create Multiple Reviews |
| [**saveReview**](ReviewApi.md#saveReview) | **POST** /review | Create a Review |


<a id="deleteMultipleReviews"></a>
# **deleteMultipleReviews**
> Boolean deleteMultipleReviews(contentType, accept, requestBody)

Delete Multiple Reviews

Deletes multiple reviews at once.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReviewApi;

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

    ReviewApi apiInstance = new ReviewApi(defaultClient);
    String contentType = "application/json"; // String | Describes the type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    List<String> requestBody = ["babefcf4-e0f7-11ec-835d-16c4e59c4351","qweqweee-e0f7-11ec-835d-16c4e59c4351","asdffggg-e0f7-11ec-835d-16c4e59c4351"]; // List<String> | 
    try {
      Boolean result = apiInstance.deleteMultipleReviews(contentType, accept, requestBody);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReviewApi#deleteMultipleReviews");
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
| **contentType** | **String**| Describes the type of the content being sent. | [default to application/json] |
| **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | [default to application/json] |
| **requestBody** | [**List&lt;String&gt;**](String.md)|  | [optional] |

### Return type

**Boolean**

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="deleteReview"></a>
# **deleteReview**
> Boolean deleteReview(reviewId, contentType, accept)

Delete Review

Deletes an existing review.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReviewApi;

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

    ReviewApi apiInstance = new ReviewApi(defaultClient);
    String reviewId = "1"; // String | Review ID.
    String contentType = "application/json"; // String | Describes the type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    try {
      Boolean result = apiInstance.deleteReview(reviewId, contentType, accept);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReviewApi#deleteReview");
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
| **reviewId** | **String**| Review ID. | |
| **contentType** | **String**| Describes the type of the content being sent. | [default to application/json] |
| **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | [default to application/json] |

### Return type

**Boolean**

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="editReview"></a>
# **editReview**
> GetReviewbyReviewId200Response editReview(reviewId, contentType, accept, editReviewRequest)

Update a Review

Updates the information of a review.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReviewApi;

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

    ReviewApi apiInstance = new ReviewApi(defaultClient);
    String reviewId = "5323fdaa-c012-11ec-835d-0ebee58edbb3"; // String | Review ID.
    String contentType = "application/json"; // String | Describes the type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    EditReviewRequest editReviewRequest = new EditReviewRequest(); // EditReviewRequest | 
    try {
      GetReviewbyReviewId200Response result = apiInstance.editReview(reviewId, contentType, accept, editReviewRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReviewApi#editReview");
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
| **reviewId** | **String**| Review ID. | |
| **contentType** | **String**| Describes the type of the content being sent. | [default to application/json] |
| **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | [default to application/json] |
| **editReviewRequest** | [**EditReviewRequest**](EditReviewRequest.md)|  | |

### Return type

[**GetReviewbyReviewId200Response**](GetReviewbyReviewId200Response.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="getReviewbyReviewId"></a>
# **getReviewbyReviewId**
> GetReviewbyReviewId200Response getReviewbyReviewId(reviewId, contentType, accept)

Get Review by Review ID

Retrieves information of a product review by its ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReviewApi;

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

    ReviewApi apiInstance = new ReviewApi(defaultClient);
    String reviewId = "1"; // String | Review ID.
    String contentType = "application/json"; // String | Describes the type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    try {
      GetReviewbyReviewId200Response result = apiInstance.getReviewbyReviewId(reviewId, contentType, accept);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReviewApi#getReviewbyReviewId");
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
| **reviewId** | **String**| Review ID. | |
| **contentType** | **String**| Describes the type of the content being sent. | [default to application/json] |
| **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | [default to application/json] |

### Return type

[**GetReviewbyReviewId200Response**](GetReviewbyReviewId200Response.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="getalistofReviews"></a>
# **getalistofReviews**
> GetalistofReviews200Response getalistofReviews(searchTerm, from, to, orderBy, status, productId, contentType, accept)

Get a list of Reviews

Retrieves a list of reviews.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReviewApi;

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

    ReviewApi apiInstance = new ReviewApi(defaultClient);
    String searchTerm = "search_term"; // String | Returns Reviews that contain the search term in `productId`, `sku`, `shopperId`, or `reviewerName`.
    String from = "0"; // String | Zero base starting record number, `0` is the default value.
    String to = "3"; // String | Zero base ending record number, `3` is the default value.
    String orderBy = ":asc"; // String | Case-sensitive fieldName to order records (optionally add `:asc` or `:desc`).
    Boolean status = true; // Boolean | Status of the review, approved (`true`) or not (`false`).
    String productId = "1"; // String | Filter the reviews by product ID.
    String contentType = "application/json"; // String | Describes the type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    try {
      GetalistofReviews200Response result = apiInstance.getalistofReviews(searchTerm, from, to, orderBy, status, productId, contentType, accept);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReviewApi#getalistofReviews");
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
| **searchTerm** | **String**| Returns Reviews that contain the search term in &#x60;productId&#x60;, &#x60;sku&#x60;, &#x60;shopperId&#x60;, or &#x60;reviewerName&#x60;. | |
| **from** | **String**| Zero base starting record number, &#x60;0&#x60; is the default value. | |
| **to** | **String**| Zero base ending record number, &#x60;3&#x60; is the default value. | |
| **orderBy** | **String**| Case-sensitive fieldName to order records (optionally add &#x60;:asc&#x60; or &#x60;:desc&#x60;). | |
| **status** | **Boolean**| Status of the review, approved (&#x60;true&#x60;) or not (&#x60;false&#x60;). | |
| **productId** | **String**| Filter the reviews by product ID. | |
| **contentType** | **String**| Describes the type of the content being sent. | [default to application/json] |
| **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | [default to application/json] |

### Return type

[**GetalistofReviews200Response**](GetalistofReviews200Response.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="saveMultipleReviews"></a>
# **saveMultipleReviews**
> List&lt;String&gt; saveMultipleReviews(contentType, accept, saveMultipleReviewsRequest)

Create Multiple Reviews

Creates multiple reviews.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReviewApi;

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

    ReviewApi apiInstance = new ReviewApi(defaultClient);
    String contentType = "application/json"; // String | Describes the type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    List<SaveMultipleReviewsRequest> saveMultipleReviewsRequest = Arrays.asList(); // List<SaveMultipleReviewsRequest> | 
    try {
      List<String> result = apiInstance.saveMultipleReviews(contentType, accept, saveMultipleReviewsRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReviewApi#saveMultipleReviews");
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
| **contentType** | **String**| Describes the type of the content being sent. | [default to application/json] |
| **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | [default to application/json] |
| **saveMultipleReviewsRequest** | [**List&lt;SaveMultipleReviewsRequest&gt;**](SaveMultipleReviewsRequest.md)|  | |

### Return type

**List&lt;String&gt;**

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="saveReview"></a>
# **saveReview**
> SaveReview200Response saveReview(contentType, accept, saveReviewRequest)

Create a Review

Creates a single review

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReviewApi;

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

    ReviewApi apiInstance = new ReviewApi(defaultClient);
    String contentType = "application/json"; // String | Describes the type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    SaveReviewRequest saveReviewRequest = new SaveReviewRequest(); // SaveReviewRequest | 
    try {
      SaveReview200Response result = apiInstance.saveReview(contentType, accept, saveReviewRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReviewApi#saveReview");
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
| **contentType** | **String**| Describes the type of the content being sent. | [default to application/json] |
| **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | [default to application/json] |
| **saveReviewRequest** | [**SaveReviewRequest**](SaveReviewRequest.md)|  | |

### Return type

[**SaveReview200Response**](SaveReview200Response.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

