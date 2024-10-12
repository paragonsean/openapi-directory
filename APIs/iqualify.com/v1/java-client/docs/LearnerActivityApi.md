# LearnerActivityApi

All URIs are relative to *https://api.iqualify.com/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**offeringsOfferingIdAnalyticsLearnersProgressGet**](LearnerActivityApi.md#offeringsOfferingIdAnalyticsLearnersProgressGet) | **GET** /offerings/{offeringId}/analytics/learners-progress | Find learner progress in a specified offering |
| [**offeringsOfferingIdAnalyticsSocialNotesGet**](LearnerActivityApi.md#offeringsOfferingIdAnalyticsSocialNotesGet) | **GET** /offerings/{offeringId}/analytics/social-notes | Find shared social notes in an offering |
| [**offeringsOfferingIdAnalyticsUnitReactionsGet**](LearnerActivityApi.md#offeringsOfferingIdAnalyticsUnitReactionsGet) | **GET** /offerings/{offeringId}/analytics/unit-reactions | Find unit reactions |
| [**usersAllProgressGet**](LearnerActivityApi.md#usersAllProgressGet) | **GET** /users/all/progress | Find learner progress in all offerings |
| [**usersUserEmailOfferingsOfferingIdProgressGet**](LearnerActivityApi.md#usersUserEmailOfferingsOfferingIdProgressGet) | **GET** /users/{userEmail}/offerings/{offeringId}/progress | Find learner&#39;s progress in a specified offering |
| [**usersUserEmailProgressGet**](LearnerActivityApi.md#usersUserEmailProgressGet) | **GET** /users/{userEmail}/progress | Find learner&#39;s progress in offerings |


<a id="offeringsOfferingIdAnalyticsLearnersProgressGet"></a>
# **offeringsOfferingIdAnalyticsLearnersProgressGet**
> List&lt;LearnerProgressResponse&gt; offeringsOfferingIdAnalyticsLearnersProgressGet(offeringId)

Find learner progress in a specified offering

Responds with all learner progress in the offering.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LearnerActivityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.iqualify.com/v1");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    LearnerActivityApi apiInstance = new LearnerActivityApi(defaultClient);
    String offeringId = "offeringId_example"; // String | offering's id
    try {
      List<LearnerProgressResponse> result = apiInstance.offeringsOfferingIdAnalyticsLearnersProgressGet(offeringId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LearnerActivityApi#offeringsOfferingIdAnalyticsLearnersProgressGet");
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
| **offeringId** | **String**| offering&#39;s id | |

### Return type

[**List&lt;LearnerProgressResponse&gt;**](LearnerProgressResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Learners progress |  -  |
| **401** | No authorization token was found. |  -  |
| **403** | You are not allowed to access this resource. |  -  |
| **404** | Not Found |  -  |

<a id="offeringsOfferingIdAnalyticsSocialNotesGet"></a>
# **offeringsOfferingIdAnalyticsSocialNotesGet**
> List&lt;SocialNotesResponse&gt; offeringsOfferingIdAnalyticsSocialNotesGet(offeringId)

Find shared social notes in an offering

Responds with all shared social notes in a specified offering.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LearnerActivityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.iqualify.com/v1");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    LearnerActivityApi apiInstance = new LearnerActivityApi(defaultClient);
    String offeringId = "offeringId_example"; // String | offering's id
    try {
      List<SocialNotesResponse> result = apiInstance.offeringsOfferingIdAnalyticsSocialNotesGet(offeringId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LearnerActivityApi#offeringsOfferingIdAnalyticsSocialNotesGet");
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
| **offeringId** | **String**| offering&#39;s id | |

### Return type

[**List&lt;SocialNotesResponse&gt;**](SocialNotesResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Offering social notes |  -  |
| **401** | No authorization token was found. |  -  |
| **403** | You are not allowed to access this resource. |  -  |
| **404** | Not Found |  -  |

<a id="offeringsOfferingIdAnalyticsUnitReactionsGet"></a>
# **offeringsOfferingIdAnalyticsUnitReactionsGet**
> List&lt;UnitReactionsAnalyticsResponse&gt; offeringsOfferingIdAnalyticsUnitReactionsGet(offeringId)

Find unit reactions

Responds with user reactions to units in a specified offering.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LearnerActivityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.iqualify.com/v1");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    LearnerActivityApi apiInstance = new LearnerActivityApi(defaultClient);
    String offeringId = "offeringId_example"; // String | offering's id
    try {
      List<UnitReactionsAnalyticsResponse> result = apiInstance.offeringsOfferingIdAnalyticsUnitReactionsGet(offeringId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LearnerActivityApi#offeringsOfferingIdAnalyticsUnitReactionsGet");
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
| **offeringId** | **String**| offering&#39;s id | |

### Return type

[**List&lt;UnitReactionsAnalyticsResponse&gt;**](UnitReactionsAnalyticsResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Unit Reactions |  -  |
| **401** | No authorization token was found. |  -  |
| **403** | You are not allowed to access this resource. |  -  |
| **404** | Not Found |  -  |

<a id="usersAllProgressGet"></a>
# **usersAllProgressGet**
> UsersAllProgressGet200Response usersAllProgressGet($top, $orderby, $filter)

Find learner progress in all offerings

Responds with all learners&#39; progress in all offerings.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LearnerActivityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.iqualify.com/v1");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    LearnerActivityApi apiInstance = new LearnerActivityApi(defaultClient);
    String $top = "50"; // String | Returns only the first n results.
    String $orderby = "$orderby_example"; // String | Sorts the results.
    String $filter = "$filter_example"; // String | Filters the results, based on a Boolean condition.
    try {
      UsersAllProgressGet200Response result = apiInstance.usersAllProgressGet($top, $orderby, $filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LearnerActivityApi#usersAllProgressGet");
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
| **$top** | **String**| Returns only the first n results. | [optional] [default to 50] |
| **$orderby** | **String**| Sorts the results. | [optional] |
| **$filter** | **String**| Filters the results, based on a Boolean condition. | [optional] |

### Return type

[**UsersAllProgressGet200Response**](UsersAllProgressGet200Response.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Learners progress |  -  |
| **400** | Bad Request |  -  |
| **401** | No authorization token was found. |  -  |
| **403** | You are not allowed to access this resource. |  -  |

<a id="usersUserEmailOfferingsOfferingIdProgressGet"></a>
# **usersUserEmailOfferingsOfferingIdProgressGet**
> UsersUserEmailOfferingsOfferingIdProgressGet200Response usersUserEmailOfferingsOfferingIdProgressGet(userEmail, offeringId)

Find learner&#39;s progress in a specified offering

Responds with the learner&#39;s progress in a specified offering.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LearnerActivityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.iqualify.com/v1");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    LearnerActivityApi apiInstance = new LearnerActivityApi(defaultClient);
    String userEmail = "userEmail_example"; // String | user's email
    String offeringId = "offeringId_example"; // String | offering's id
    try {
      UsersUserEmailOfferingsOfferingIdProgressGet200Response result = apiInstance.usersUserEmailOfferingsOfferingIdProgressGet(userEmail, offeringId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LearnerActivityApi#usersUserEmailOfferingsOfferingIdProgressGet");
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
| **userEmail** | **String**| user&#39;s email | |
| **offeringId** | **String**| offering&#39;s id | |

### Return type

[**UsersUserEmailOfferingsOfferingIdProgressGet200Response**](UsersUserEmailOfferingsOfferingIdProgressGet200Response.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | user&#39;s offerings |  -  |
| **400** | Bad Request |  -  |
| **401** | No authorization token was found. |  -  |
| **403** | You are not allowed to access this resource. |  -  |
| **404** | Not Found |  -  |

<a id="usersUserEmailProgressGet"></a>
# **usersUserEmailProgressGet**
> LearnerResponse usersUserEmailProgressGet(userEmail)

Find learner&#39;s progress in offerings

Responds with the specified learner&#39;s progress in all offerings.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LearnerActivityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.iqualify.com/v1");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    LearnerActivityApi apiInstance = new LearnerActivityApi(defaultClient);
    String userEmail = "userEmail_example"; // String | user's email
    try {
      LearnerResponse result = apiInstance.usersUserEmailProgressGet(userEmail);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LearnerActivityApi#usersUserEmailProgressGet");
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
| **userEmail** | **String**| user&#39;s email | |

### Return type

[**LearnerResponse**](LearnerResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Learner Progress |  -  |
| **400** | Bad Request |  -  |
| **401** | No authorization token was found. |  -  |
| **403** | You are not allowed to access this resource. |  -  |
| **404** | Not Found |  -  |

