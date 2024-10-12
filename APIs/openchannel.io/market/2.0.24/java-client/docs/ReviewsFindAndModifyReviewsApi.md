# ReviewsFindAndModifyReviewsApi

All URIs are relative to *https://market.openchannel.io/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**reviewsGet**](ReviewsFindAndModifyReviewsApi.md#reviewsGet) | **GET** /reviews | Find reviews for a particular App and marketplace. Results are automatically paginated when limit is set |
| [**reviewsPost**](ReviewsFindAndModifyReviewsApi.md#reviewsPost) | **POST** /reviews | Post a review from a User and returns the new post |
| [**reviewsReviewIdDelete**](ReviewsFindAndModifyReviewsApi.md#reviewsReviewIdDelete) | **DELETE** /reviews/{reviewId} | Remove a review |
| [**reviewsReviewIdGet**](ReviewsFindAndModifyReviewsApi.md#reviewsReviewIdGet) | **GET** /reviews/{reviewId} | Find a Review within a particular App and marketplace |
| [**reviewsReviewIdPatch**](ReviewsFindAndModifyReviewsApi.md#reviewsReviewIdPatch) | **PATCH** /reviews/{reviewId} | Update a review fields |
| [**reviewsReviewIdPost**](ReviewsFindAndModifyReviewsApi.md#reviewsReviewIdPost) | **POST** /reviews/{reviewId} | Update a review from a User and returns the new post |


<a id="reviewsGet"></a>
# **reviewsGet**
> ReviewPages reviewsGet(query, sort, pageNumber, limit)

Find reviews for a particular App and marketplace. Results are automatically paginated when limit is set

- Results are paginated and the default is value is 100 if no limit is provided 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReviewsFindAndModifyReviewsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://market.openchannel.io/v2");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    ReviewsFindAndModifyReviewsApi apiInstance = new ReviewsFindAndModifyReviewsApi(defaultClient);
    String query = "query_example"; // String | A query document. Example: {'rating': 500} matches all the reviews that have a rating of 500. 
    String sort = "sort_example"; // String | A sort document. Example: {'rating':1} sorts the results by rating in ascending order
    Integer pageNumber = 56; // Integer | The result set page number to be returned
    Integer limit = 56; // Integer | The maximum number of results to return per page
    try {
      ReviewPages result = apiInstance.reviewsGet(query, sort, pageNumber, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReviewsFindAndModifyReviewsApi#reviewsGet");
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
| **query** | **String**| A query document. Example: {&#39;rating&#39;: 500} matches all the reviews that have a rating of 500.  | [optional] |
| **sort** | **String**| A sort document. Example: {&#39;rating&#39;:1} sorts the results by rating in ascending order | [optional] |
| **pageNumber** | **Integer**| The result set page number to be returned | [optional] |
| **limit** | **Integer**| The maximum number of results to return per page | [optional] |

### Return type

[**ReviewPages**](ReviewPages.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **400** | Bad Request - Required parameters are missing, malformed or invalid |  -  |
| **0** | OK |  -  |

<a id="reviewsPost"></a>
# **reviewsPost**
> Review reviewsPost(appId, userId, headline, rating, description, userAccountId, type, mustOwnApp, autoApprove, customData)

Post a review from a User and returns the new post

- Only authenticated users are able to post reviews - Returns the newly created review 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReviewsFindAndModifyReviewsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://market.openchannel.io/v2");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    ReviewsFindAndModifyReviewsApi apiInstance = new ReviewsFindAndModifyReviewsApi(defaultClient);
    String appId = "appId_example"; // String | The id of the App that will own this review
    String userId = "userId_example"; // String | The id of the User that is posting this review
    String headline = "headline_example"; // String | The review's headline. Limited to 50 characters.
    Integer rating = 56; // Integer | The rating given within this review. The rating is represented as an integer between 0 and 500 (0 - 5 stars)
    String description = "description_example"; // String | The review's description. Limited to 2000 characters.
    String userAccountId = "userAccountId_example"; // String | The id of the User account that is posting this review
    String type = "type_example"; // String | The type for this review
    Boolean mustOwnApp = true; // Boolean | True if a review can be created only by a user that has owned the app. The default is True.
    Boolean autoApprove = true; // Boolean | True if the review should be automatically approved. The default is False.
    String customData = "customData_example"; // String | A custom JSON object that you can create and attach to this record
    try {
      Review result = apiInstance.reviewsPost(appId, userId, headline, rating, description, userAccountId, type, mustOwnApp, autoApprove, customData);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReviewsFindAndModifyReviewsApi#reviewsPost");
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
| **appId** | **String**| The id of the App that will own this review | |
| **userId** | **String**| The id of the User that is posting this review | |
| **headline** | **String**| The review&#39;s headline. Limited to 50 characters. | |
| **rating** | **Integer**| The rating given within this review. The rating is represented as an integer between 0 and 500 (0 - 5 stars) | |
| **description** | **String**| The review&#39;s description. Limited to 2000 characters. | |
| **userAccountId** | **String**| The id of the User account that is posting this review | [optional] |
| **type** | **String**| The type for this review | [optional] |
| **mustOwnApp** | **Boolean**| True if a review can be created only by a user that has owned the app. The default is True. | [optional] |
| **autoApprove** | **Boolean**| True if the review should be automatically approved. The default is False. | [optional] |
| **customData** | **String**| A custom JSON object that you can create and attach to this record | [optional] |

### Return type

[**Review**](Review.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **400** | Bad Request - Required parameters are missing, malformed or invalid |  -  |
| **403** | Forbidden - Users must have owned the app before they can post a review; Anonymous users cannot post reviews |  -  |
| **409** | Already Exists - The User has already reviewed this app |  -  |
| **0** | OK |  -  |

<a id="reviewsReviewIdDelete"></a>
# **reviewsReviewIdDelete**
> reviewsReviewIdDelete(reviewId, userId, userAccountId)

Remove a review

- Only the review author is able to remove their review 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReviewsFindAndModifyReviewsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://market.openchannel.io/v2");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    ReviewsFindAndModifyReviewsApi apiInstance = new ReviewsFindAndModifyReviewsApi(defaultClient);
    String reviewId = "reviewId_example"; // String | The id of the Review to be updated
    String userId = "userId_example"; // String | The id of the User that is removing this review
    String userAccountId = "userAccountId_example"; // String | The id of the User account that is emoving this review
    try {
      apiInstance.reviewsReviewIdDelete(reviewId, userId, userAccountId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReviewsFindAndModifyReviewsApi#reviewsReviewIdDelete");
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
| **reviewId** | **String**| The id of the Review to be updated | |
| **userId** | **String**| The id of the User that is removing this review | |
| **userAccountId** | **String**| The id of the User account that is emoving this review | [optional] |

### Return type

null (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **400** | Bad Request - Required parameters are missing, malformed or invalid |  -  |

<a id="reviewsReviewIdGet"></a>
# **reviewsReviewIdGet**
> Review reviewsReviewIdGet(reviewId)

Find a Review within a particular App and marketplace

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReviewsFindAndModifyReviewsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://market.openchannel.io/v2");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    ReviewsFindAndModifyReviewsApi apiInstance = new ReviewsFindAndModifyReviewsApi(defaultClient);
    String reviewId = "reviewId_example"; // String | The id of the review to be located
    try {
      Review result = apiInstance.reviewsReviewIdGet(reviewId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReviewsFindAndModifyReviewsApi#reviewsReviewIdGet");
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
| **reviewId** | **String**| The id of the review to be located | |

### Return type

[**Review**](Review.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **400** | Bad Request - Required parameters are missing, malformed or invalid |  -  |
| **404** | Not Found - Review is not found |  -  |
| **0** | OK |  -  |

<a id="reviewsReviewIdPatch"></a>
# **reviewsReviewIdPatch**
> Review reviewsReviewIdPatch(reviewId, userId, userAccountId, headline, rating, description, customData)

Update a review fields

- Only the review author is able to update their review - Returns the newly updated review 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReviewsFindAndModifyReviewsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://market.openchannel.io/v2");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    ReviewsFindAndModifyReviewsApi apiInstance = new ReviewsFindAndModifyReviewsApi(defaultClient);
    String reviewId = "reviewId_example"; // String | The id of the Review to be updated
    String userId = "userId_example"; // String | The id of the User that is updating this review
    String userAccountId = "userAccountId_example"; // String | The id of the User account that is posting this review
    String headline = "headline_example"; // String | The review's headline. Limited to 50 characters.
    Integer rating = 56; // Integer | The rating given within this review. The rating is represented as an integer between 0 and 500 (0 - 5 stars)
    String description = "description_example"; // String | The review's description. Limited to 2000 characters.
    String customData = "customData_example"; // String | A custom JSON object that you can create and attach to this record
    try {
      Review result = apiInstance.reviewsReviewIdPatch(reviewId, userId, userAccountId, headline, rating, description, customData);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReviewsFindAndModifyReviewsApi#reviewsReviewIdPatch");
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
| **reviewId** | **String**| The id of the Review to be updated | |
| **userId** | **String**| The id of the User that is updating this review | |
| **userAccountId** | **String**| The id of the User account that is posting this review | [optional] |
| **headline** | **String**| The review&#39;s headline. Limited to 50 characters. | [optional] |
| **rating** | **Integer**| The rating given within this review. The rating is represented as an integer between 0 and 500 (0 - 5 stars) | [optional] |
| **description** | **String**| The review&#39;s description. Limited to 2000 characters. | [optional] |
| **customData** | **String**| A custom JSON object that you can create and attach to this record | [optional] |

### Return type

[**Review**](Review.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **400** | Bad Request - Required parameters are missing, malformed or invalid |  -  |
| **403** | Forbidden - Anonymous users cannot update reviews |  -  |
| **404** | Not Found - This review was not found |  -  |
| **0** | OK |  -  |

<a id="reviewsReviewIdPost"></a>
# **reviewsReviewIdPost**
> Review reviewsReviewIdPost(reviewId, userId, userAccountId, headline, rating, description, customData)

Update a review from a User and returns the new post

- Only the review author is able to update their review - Returns the newly updated review 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReviewsFindAndModifyReviewsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://market.openchannel.io/v2");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    ReviewsFindAndModifyReviewsApi apiInstance = new ReviewsFindAndModifyReviewsApi(defaultClient);
    String reviewId = "reviewId_example"; // String | The id of the Review to be updated
    String userId = "userId_example"; // String | The id of the User that is updating this review
    String userAccountId = "userAccountId_example"; // String | The id of the User account that is posting this review
    String headline = "headline_example"; // String | The review's headline. Limited to 50 characters.
    Integer rating = 56; // Integer | The rating given within this review. The rating is represented as an integer between 0 and 500 (0 - 5 stars)
    String description = "description_example"; // String | The review's description. Limited to 2000 characters.
    String customData = "customData_example"; // String | A custom JSON object that you can create and attach to this record
    try {
      Review result = apiInstance.reviewsReviewIdPost(reviewId, userId, userAccountId, headline, rating, description, customData);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReviewsFindAndModifyReviewsApi#reviewsReviewIdPost");
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
| **reviewId** | **String**| The id of the Review to be updated | |
| **userId** | **String**| The id of the User that is updating this review | |
| **userAccountId** | **String**| The id of the User account that is posting this review | |
| **headline** | **String**| The review&#39;s headline. Limited to 50 characters. | |
| **rating** | **Integer**| The rating given within this review. The rating is represented as an integer between 0 and 500 (0 - 5 stars) | |
| **description** | **String**| The review&#39;s description. Limited to 2000 characters. | |
| **customData** | **String**| A custom JSON object that you can create and attach to this record | [optional] |

### Return type

[**Review**](Review.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **400** | Bad Request - Required parameters are missing, malformed or invalid |  -  |
| **403** | Forbidden - Anonymous users cannot update reviews |  -  |
| **404** | Not Found - This review was not found |  -  |
| **0** | OK |  -  |

