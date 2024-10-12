# ReviewApi

All URIs are relative to *https://api2.bigoven.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**recipeRecipeIdReviewGet**](ReviewApi.md#recipeRecipeIdReviewGet) | **GET** /recipe/{recipeId}/review | Get *my* review for the recipe {recipeId}, where \&quot;me\&quot; is determined by standard authentication headers |
| [**recipeReviewReviewIdGet**](ReviewApi.md#recipeReviewReviewIdGet) | **GET** /recipe/review/{reviewId} | Get a given review by string-style ID. This will return a payload with FeaturedReply, ReplyCount.              Recommended display is to list top-level reviews with one featured reply underneath.               Currently, the FeaturedReply is the most recent one for that rating. |
| [**reviewDelete**](ReviewApi.md#reviewDelete) | **DELETE** /recipe/{recipeId}/review/{reviewId} | DEPRECATED! - Deletes a review by recipeId and reviewId. Please use recipe/review/{reviewId} instead. |
| [**reviewDeleteReply**](ReviewApi.md#reviewDeleteReply) | **DELETE** /recipe/review/replies/{replyId} | DELETE a reply to a given review. Authenticated user must be the one who originally posted the reply. |
| [**reviewGet**](ReviewApi.md#reviewGet) | **GET** /recipe/{recipeId}/review/{reviewId} | Get a given review - DEPRECATED. See recipe/review/{reviewId} for the current usage.              Beginning in January 2017, BigOven moded from an integer-based ID system to a GUID-style string-based ID system for reviews and replies.              We are also supporting more of a \&quot;Google Play\&quot; style model for Reviews and Replies. That is, there are top-level Reviews and then              an unlimited list of replies (which do not carry star ratings) underneath existing reviews. Also, a given user can only have one review               per recipe. Existing legacy endpoints will continue to work, but we strongly recommend you migrate to using the newer endpoints listed              which do NOT carry the \&quot;DEPRECATED\&quot; flag. |
| [**reviewGetReplies**](ReviewApi.md#reviewGetReplies) | **GET** /recipe/review/{reviewId}/replies | Get a paged list of replies for a given review. |
| [**reviewGetReviews**](ReviewApi.md#reviewGetReviews) | **GET** /recipe/{recipeId}/reviews | Get paged list of reviews for a recipe. Each review will have at most one FeaturedReply, as well as a ReplyCount. |
| [**reviewPost**](ReviewApi.md#reviewPost) | **POST** /recipe/{recipeId}/review | Add a new review. Only one review can be provided per {userId, recipeId} pair. Otherwise your review will be updated. |
| [**reviewPostReply**](ReviewApi.md#reviewPostReply) | **POST** /recipe/review/{reviewId}/replies | POST a reply to a given review. The date will be set by server. Note that replies no longer have star ratings, only top-level reviews do. |
| [**reviewPut**](ReviewApi.md#reviewPut) | **PUT** /recipe/review/{reviewId} | Update a given top-level review. |
| [**reviewPutLegacy**](ReviewApi.md#reviewPutLegacy) | **PUT** /recipe/{recipeId}/review/{reviewId} | HTTP PUT (update) a recipe review. DEPRECATED. Please see recipe/review/{reviewId} PUT for the new endpoint.              We are moving to a string-based primary key system, no longer integers, for reviews and replies. |
| [**reviewPutReply**](ReviewApi.md#reviewPutReply) | **PUT** /recipe/review/replies/{replyId} | Update (PUT) a reply to a given review. Authenticated user must be the original one that posted the reply. |


<a id="recipeRecipeIdReviewGet"></a>
# **recipeRecipeIdReviewGet**
> BigOvenModelAPIReview recipeRecipeIdReviewGet(recipeId)

Get *my* review for the recipe {recipeId}, where \&quot;me\&quot; is determined by standard authentication headers

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReviewApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api2.bigoven.com");

    ReviewApi apiInstance = new ReviewApi(defaultClient);
    Integer recipeId = 56; // Integer | 
    try {
      BigOvenModelAPIReview result = apiInstance.recipeRecipeIdReviewGet(recipeId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReviewApi#recipeRecipeIdReviewGet");
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
| **recipeId** | **Integer**|  | |

### Return type

[**BigOvenModelAPIReview**](BigOvenModelAPIReview.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="recipeReviewReviewIdGet"></a>
# **recipeReviewReviewIdGet**
> BigOvenModelAPIReview recipeReviewReviewIdGet(reviewId)

Get a given review by string-style ID. This will return a payload with FeaturedReply, ReplyCount.              Recommended display is to list top-level reviews with one featured reply underneath.               Currently, the FeaturedReply is the most recent one for that rating.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReviewApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api2.bigoven.com");

    ReviewApi apiInstance = new ReviewApi(defaultClient);
    String reviewId = "reviewId_example"; // String | 
    try {
      BigOvenModelAPIReview result = apiInstance.recipeReviewReviewIdGet(reviewId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReviewApi#recipeReviewReviewIdGet");
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
| **reviewId** | **String**|  | |

### Return type

[**BigOvenModelAPIReview**](BigOvenModelAPIReview.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="reviewDelete"></a>
# **reviewDelete**
> Object reviewDelete(recipeId, reviewId)

DEPRECATED! - Deletes a review by recipeId and reviewId. Please use recipe/review/{reviewId} instead.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReviewApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api2.bigoven.com");

    ReviewApi apiInstance = new ReviewApi(defaultClient);
    Integer recipeId = 56; // Integer | 
    Long reviewId = 56L; // Long | 
    try {
      Object result = apiInstance.reviewDelete(recipeId, reviewId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReviewApi#reviewDelete");
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
| **recipeId** | **Integer**|  | |
| **reviewId** | **Long**|  | |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="reviewDeleteReply"></a>
# **reviewDeleteReply**
> Object reviewDeleteReply(replyId)

DELETE a reply to a given review. Authenticated user must be the one who originally posted the reply.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReviewApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api2.bigoven.com");

    ReviewApi apiInstance = new ReviewApi(defaultClient);
    String replyId = "replyId_example"; // String | 
    try {
      Object result = apiInstance.reviewDeleteReply(replyId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReviewApi#reviewDeleteReply");
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
| **replyId** | **String**|  | |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="reviewGet"></a>
# **reviewGet**
> BigOvenModelAPIReview reviewGet(reviewId, recipeId)

Get a given review - DEPRECATED. See recipe/review/{reviewId} for the current usage.              Beginning in January 2017, BigOven moded from an integer-based ID system to a GUID-style string-based ID system for reviews and replies.              We are also supporting more of a \&quot;Google Play\&quot; style model for Reviews and Replies. That is, there are top-level Reviews and then              an unlimited list of replies (which do not carry star ratings) underneath existing reviews. Also, a given user can only have one review               per recipe. Existing legacy endpoints will continue to work, but we strongly recommend you migrate to using the newer endpoints listed              which do NOT carry the \&quot;DEPRECATED\&quot; flag.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReviewApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api2.bigoven.com");

    ReviewApi apiInstance = new ReviewApi(defaultClient);
    Integer reviewId = 56; // Integer | int
    Integer recipeId = 56; // Integer | int
    try {
      BigOvenModelAPIReview result = apiInstance.reviewGet(reviewId, recipeId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReviewApi#reviewGet");
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
| **reviewId** | **Integer**| int | |
| **recipeId** | **Integer**| int | |

### Return type

[**BigOvenModelAPIReview**](BigOvenModelAPIReview.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="reviewGetReplies"></a>
# **reviewGetReplies**
> List&lt;BigOvenModelAPIReply&gt; reviewGetReplies(reviewId, pg, rpp)

Get a paged list of replies for a given review.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReviewApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api2.bigoven.com");

    ReviewApi apiInstance = new ReviewApi(defaultClient);
    String reviewId = "reviewId_example"; // String | 
    Integer pg = 56; // Integer | the page (int), starting with 1
    Integer rpp = 56; // Integer | results per page (int)
    try {
      List<BigOvenModelAPIReply> result = apiInstance.reviewGetReplies(reviewId, pg, rpp);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReviewApi#reviewGetReplies");
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
| **reviewId** | **String**|  | |
| **pg** | **Integer**| the page (int), starting with 1 | [optional] |
| **rpp** | **Integer**| results per page (int) | [optional] |

### Return type

[**List&lt;BigOvenModelAPIReply&gt;**](BigOvenModelAPIReply.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="reviewGetReviews"></a>
# **reviewGetReviews**
> List&lt;BigOvenModelAPIReview&gt; reviewGetReviews(recipeId, pg, rpp)

Get paged list of reviews for a recipe. Each review will have at most one FeaturedReply, as well as a ReplyCount.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReviewApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api2.bigoven.com");

    ReviewApi apiInstance = new ReviewApi(defaultClient);
    Integer recipeId = 56; // Integer | recipe id (int)
    Integer pg = 56; // Integer | the page (int), starting with 1
    Integer rpp = 56; // Integer | results per page (int)
    try {
      List<BigOvenModelAPIReview> result = apiInstance.reviewGetReviews(recipeId, pg, rpp);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReviewApi#reviewGetReviews");
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
| **recipeId** | **Integer**| recipe id (int) | |
| **pg** | **Integer**| the page (int), starting with 1 | [optional] |
| **rpp** | **Integer**| results per page (int) | [optional] |

### Return type

[**List&lt;BigOvenModelAPIReview&gt;**](BigOvenModelAPIReview.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="reviewPost"></a>
# **reviewPost**
> Object reviewPost(recipeId, apI2ControllersWebAPIReviewControllerReviewRequest)

Add a new review. Only one review can be provided per {userId, recipeId} pair. Otherwise your review will be updated.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReviewApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api2.bigoven.com");

    ReviewApi apiInstance = new ReviewApi(defaultClient);
    Integer recipeId = 56; // Integer | 
    API2ControllersWebAPIReviewControllerReviewRequest apI2ControllersWebAPIReviewControllerReviewRequest = new API2ControllersWebAPIReviewControllerReviewRequest(); // API2ControllersWebAPIReviewControllerReviewRequest | 
    try {
      Object result = apiInstance.reviewPost(recipeId, apI2ControllersWebAPIReviewControllerReviewRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReviewApi#reviewPost");
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
| **recipeId** | **Integer**|  | |
| **apI2ControllersWebAPIReviewControllerReviewRequest** | [**API2ControllersWebAPIReviewControllerReviewRequest**](API2ControllersWebAPIReviewControllerReviewRequest.md)|  | |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="reviewPostReply"></a>
# **reviewPostReply**
> BigOvenModelAPIReply reviewPostReply(reviewId, apI2ControllersWebAPIReviewControllerPostReplyReq)

POST a reply to a given review. The date will be set by server. Note that replies no longer have star ratings, only top-level reviews do.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReviewApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api2.bigoven.com");

    ReviewApi apiInstance = new ReviewApi(defaultClient);
    String reviewId = "reviewId_example"; // String | 
    API2ControllersWebAPIReviewControllerPostReplyReq apI2ControllersWebAPIReviewControllerPostReplyReq = new API2ControllersWebAPIReviewControllerPostReplyReq(); // API2ControllersWebAPIReviewControllerPostReplyReq | 
    try {
      BigOvenModelAPIReply result = apiInstance.reviewPostReply(reviewId, apI2ControllersWebAPIReviewControllerPostReplyReq);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReviewApi#reviewPostReply");
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
| **reviewId** | **String**|  | |
| **apI2ControllersWebAPIReviewControllerPostReplyReq** | [**API2ControllersWebAPIReviewControllerPostReplyReq**](API2ControllersWebAPIReviewControllerPostReplyReq.md)|  | |

### Return type

[**BigOvenModelAPIReply**](BigOvenModelAPIReply.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="reviewPut"></a>
# **reviewPut**
> BigOvenModelAPIReview reviewPut(reviewId, apI2ControllersWebAPIReviewControllerReviewRequest)

Update a given top-level review.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReviewApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api2.bigoven.com");

    ReviewApi apiInstance = new ReviewApi(defaultClient);
    String reviewId = "reviewId_example"; // String | 
    API2ControllersWebAPIReviewControllerReviewRequest apI2ControllersWebAPIReviewControllerReviewRequest = new API2ControllersWebAPIReviewControllerReviewRequest(); // API2ControllersWebAPIReviewControllerReviewRequest | 
    try {
      BigOvenModelAPIReview result = apiInstance.reviewPut(reviewId, apI2ControllersWebAPIReviewControllerReviewRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReviewApi#reviewPut");
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
| **reviewId** | **String**|  | |
| **apI2ControllersWebAPIReviewControllerReviewRequest** | [**API2ControllersWebAPIReviewControllerReviewRequest**](API2ControllersWebAPIReviewControllerReviewRequest.md)|  | |

### Return type

[**BigOvenModelAPIReview**](BigOvenModelAPIReview.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="reviewPutLegacy"></a>
# **reviewPutLegacy**
> BigOvenModelAPIReview reviewPutLegacy(reviewId, recipeId, apI2ControllersWebAPIReviewControllerReviewRequestLegacy)

HTTP PUT (update) a recipe review. DEPRECATED. Please see recipe/review/{reviewId} PUT for the new endpoint.              We are moving to a string-based primary key system, no longer integers, for reviews and replies.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReviewApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api2.bigoven.com");

    ReviewApi apiInstance = new ReviewApi(defaultClient);
    Integer reviewId = 56; // Integer | reviewId (int)
    Integer recipeId = 56; // Integer | recipeId (int)
    API2ControllersWebAPIReviewControllerReviewRequestLegacy apI2ControllersWebAPIReviewControllerReviewRequestLegacy = new API2ControllersWebAPIReviewControllerReviewRequestLegacy(); // API2ControllersWebAPIReviewControllerReviewRequestLegacy | 
    try {
      BigOvenModelAPIReview result = apiInstance.reviewPutLegacy(reviewId, recipeId, apI2ControllersWebAPIReviewControllerReviewRequestLegacy);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReviewApi#reviewPutLegacy");
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
| **reviewId** | **Integer**| reviewId (int) | |
| **recipeId** | **Integer**| recipeId (int) | |
| **apI2ControllersWebAPIReviewControllerReviewRequestLegacy** | [**API2ControllersWebAPIReviewControllerReviewRequestLegacy**](API2ControllersWebAPIReviewControllerReviewRequestLegacy.md)|  | |

### Return type

[**BigOvenModelAPIReview**](BigOvenModelAPIReview.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="reviewPutReply"></a>
# **reviewPutReply**
> BigOvenModelAPIReply reviewPutReply(replyId, apI2ControllersWebAPIReviewControllerPostReplyReq)

Update (PUT) a reply to a given review. Authenticated user must be the original one that posted the reply.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReviewApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api2.bigoven.com");

    ReviewApi apiInstance = new ReviewApi(defaultClient);
    String replyId = "replyId_example"; // String | 
    API2ControllersWebAPIReviewControllerPostReplyReq apI2ControllersWebAPIReviewControllerPostReplyReq = new API2ControllersWebAPIReviewControllerPostReplyReq(); // API2ControllersWebAPIReviewControllerPostReplyReq | 
    try {
      BigOvenModelAPIReply result = apiInstance.reviewPutReply(replyId, apI2ControllersWebAPIReviewControllerPostReplyReq);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReviewApi#reviewPutReply");
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
| **replyId** | **String**|  | |
| **apI2ControllersWebAPIReviewControllerPostReplyReq** | [**API2ControllersWebAPIReviewControllerPostReplyReq**](API2ControllersWebAPIReviewControllerPostReplyReq.md)|  | |

### Return type

[**BigOvenModelAPIReply**](BigOvenModelAPIReply.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

