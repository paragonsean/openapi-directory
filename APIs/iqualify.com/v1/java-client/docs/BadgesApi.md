# BadgesApi

All URIs are relative to *https://api.iqualify.com/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**offeringsOfferingIdBadgesGet**](BadgesApi.md#offeringsOfferingIdBadgesGet) | **GET** /offerings/{offeringId}/badges | Find offering badges |
| [**offeringsOfferingIdUsersUserEmailBadgesAwardPost**](BadgesApi.md#offeringsOfferingIdUsersUserEmailBadgesAwardPost) | **POST** /offerings/{offeringId}/users/{userEmail}/badges/award | Award badge |
| [**usersUserEmailBadgesGet**](BadgesApi.md#usersUserEmailBadgesGet) | **GET** /users/{userEmail}/badges | Find user&#39;s badges |


<a id="offeringsOfferingIdBadgesGet"></a>
# **offeringsOfferingIdBadgesGet**
> Badge offeringsOfferingIdBadgesGet(offeringId)

Find offering badges

Responds with the badge for an offering matching the offeringId.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BadgesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.iqualify.com/v1");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    BadgesApi apiInstance = new BadgesApi(defaultClient);
    String offeringId = "offeringId_example"; // String | offering's id
    try {
      Badge result = apiInstance.offeringsOfferingIdBadgesGet(offeringId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BadgesApi#offeringsOfferingIdBadgesGet");
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

[**Badge**](Badge.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | badges |  -  |
| **401** | No authorization token was found. |  -  |
| **403** | You are not allowed to access this resource. |  -  |
| **404** | Not Found |  -  |

<a id="offeringsOfferingIdUsersUserEmailBadgesAwardPost"></a>
# **offeringsOfferingIdUsersUserEmailBadgesAwardPost**
> AwardedResponse offeringsOfferingIdUsersUserEmailBadgesAwardPost(offeringId, userEmail)

Award badge

Awards a badge to a user in the offering.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BadgesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.iqualify.com/v1");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    BadgesApi apiInstance = new BadgesApi(defaultClient);
    String offeringId = "offeringId_example"; // String | offering's id
    String userEmail = "userEmail_example"; // String | user's email
    try {
      AwardedResponse result = apiInstance.offeringsOfferingIdUsersUserEmailBadgesAwardPost(offeringId, userEmail);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BadgesApi#offeringsOfferingIdUsersUserEmailBadgesAwardPost");
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
| **userEmail** | **String**| user&#39;s email | |

### Return type

[**AwardedResponse**](AwardedResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Awarded badge response |  -  |
| **400** | Bad Request |  -  |
| **401** | No authorization token was found. |  -  |
| **403** | You are not allowed to access this resource. |  -  |
| **404** | Not Found |  -  |

<a id="usersUserEmailBadgesGet"></a>
# **usersUserEmailBadgesGet**
> List&lt;UserBadge&gt; usersUserEmailBadgesGet(userEmail)

Find user&#39;s badges

Responds with all badges that the specified user has been awarded.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BadgesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.iqualify.com/v1");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    BadgesApi apiInstance = new BadgesApi(defaultClient);
    String userEmail = "userEmail_example"; // String | user's email
    try {
      List<UserBadge> result = apiInstance.usersUserEmailBadgesGet(userEmail);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BadgesApi#usersUserEmailBadgesGet");
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

[**List&lt;UserBadge&gt;**](UserBadge.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | user&#39;s badges |  -  |
| **400** | Bad Request |  -  |
| **401** | No authorization token was found. |  -  |
| **403** | You are not allowed to access this resource. |  -  |
| **404** | Not Found |  -  |

