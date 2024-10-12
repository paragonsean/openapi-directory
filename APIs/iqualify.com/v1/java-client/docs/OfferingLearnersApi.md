# OfferingLearnersApi

All URIs are relative to *https://api.iqualify.com/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**offeringsOfferingIdUsersGet**](OfferingLearnersApi.md#offeringsOfferingIdUsersGet) | **GET** /offerings/{offeringId}/users | Find offering&#39;s users |
| [**offeringsOfferingIdUsersMarkerEmailMarksDelete**](OfferingLearnersApi.md#offeringsOfferingIdUsersMarkerEmailMarksDelete) | **DELETE** /offerings/{offeringId}/users/{markerEmail}/marks | Remove learners from coach&#39;s marking list |
| [**offeringsOfferingIdUsersMarkerEmailMarksGet**](OfferingLearnersApi.md#offeringsOfferingIdUsersMarkerEmailMarksGet) | **GET** /offerings/{offeringId}/users/{markerEmail}/marks | Find Learners marked by a coach |
| [**offeringsOfferingIdUsersMarkerEmailMarksPost**](OfferingLearnersApi.md#offeringsOfferingIdUsersMarkerEmailMarksPost) | **POST** /offerings/{offeringId}/users/{markerEmail}/marks | Add learners to be marked by a coach |
| [**offeringsOfferingIdUsersPost**](OfferingLearnersApi.md#offeringsOfferingIdUsersPost) | **POST** /offerings/{offeringId}/users | Adds user to the offering |
| [**offeringsOfferingIdUsersUserEmailDelete**](OfferingLearnersApi.md#offeringsOfferingIdUsersUserEmailDelete) | **DELETE** /offerings/{offeringId}/users/{userEmail} | Removes user from the offering |
| [**usersUserEmailTransferPatch**](OfferingLearnersApi.md#usersUserEmailTransferPatch) | **PATCH** /users/{userEmail}/transfer | Transfer a user between offerings |


<a id="offeringsOfferingIdUsersGet"></a>
# **offeringsOfferingIdUsersGet**
> List&lt;OfferingUserResponse&gt; offeringsOfferingIdUsersGet(offeringId, facilitators, learners, markers)

Find offering&#39;s users

Responds with a list of users in the offering (facilitators, learners and markers.).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OfferingLearnersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.iqualify.com/v1");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    OfferingLearnersApi apiInstance = new OfferingLearnersApi(defaultClient);
    String offeringId = "offeringId_example"; // String | offering's id
    String facilitators = "true"; // String | If true, facilitators are included in the results.
    String learners = "true"; // String | If true, learners are included in the results.
    String markers = "true"; // String | If true, markers are included in the results.
    try {
      List<OfferingUserResponse> result = apiInstance.offeringsOfferingIdUsersGet(offeringId, facilitators, learners, markers);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OfferingLearnersApi#offeringsOfferingIdUsersGet");
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
| **facilitators** | **String**| If true, facilitators are included in the results. | [optional] [default to true] [enum: true, false] |
| **learners** | **String**| If true, learners are included in the results. | [optional] [default to true] [enum: true, false] |
| **markers** | **String**| If true, markers are included in the results. | [optional] [default to true] [enum: true, false] |

### Return type

[**List&lt;OfferingUserResponse&gt;**](OfferingUserResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | offering&#39;s users |  -  |
| **400** | Bad Request |  -  |
| **401** | No authorization token was found. |  -  |
| **403** | You are not allowed to access this resource. |  -  |
| **404** | Not Found |  -  |

<a id="offeringsOfferingIdUsersMarkerEmailMarksDelete"></a>
# **offeringsOfferingIdUsersMarkerEmailMarksDelete**
> List&lt;OfferingUser&gt; offeringsOfferingIdUsersMarkerEmailMarksDelete(offeringId, markerEmail, requestBody)

Remove learners from coach&#39;s marking list

Removes an array of learners from coach&#39;s marking list.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OfferingLearnersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.iqualify.com/v1");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    OfferingLearnersApi apiInstance = new OfferingLearnersApi(defaultClient);
    String offeringId = "offeringId_example"; // String | offering's id
    String markerEmail = "markerEmail_example"; // String | marker's email
    List<String> requestBody = Arrays.asList(); // List<String> | array of learners e-mails
    try {
      List<OfferingUser> result = apiInstance.offeringsOfferingIdUsersMarkerEmailMarksDelete(offeringId, markerEmail, requestBody);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OfferingLearnersApi#offeringsOfferingIdUsersMarkerEmailMarksDelete");
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
| **markerEmail** | **String**| marker&#39;s email | |
| **requestBody** | [**List&lt;String&gt;**](String.md)| array of learners e-mails | |

### Return type

[**List&lt;OfferingUser&gt;**](OfferingUser.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | learners marked by the marker |  -  |
| **400** | Bad Request |  -  |
| **401** | No authorization token was found. |  -  |
| **403** | You are not allowed to access this resource. |  -  |
| **404** | Not Found |  -  |

<a id="offeringsOfferingIdUsersMarkerEmailMarksGet"></a>
# **offeringsOfferingIdUsersMarkerEmailMarksGet**
> List&lt;OfferingUser&gt; offeringsOfferingIdUsersMarkerEmailMarksGet(offeringId, markerEmail)

Find Learners marked by a coach

Responds with all learners marked by the specified coach.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OfferingLearnersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.iqualify.com/v1");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    OfferingLearnersApi apiInstance = new OfferingLearnersApi(defaultClient);
    String offeringId = "offeringId_example"; // String | offering's id
    String markerEmail = "markerEmail_example"; // String | marker's email
    try {
      List<OfferingUser> result = apiInstance.offeringsOfferingIdUsersMarkerEmailMarksGet(offeringId, markerEmail);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OfferingLearnersApi#offeringsOfferingIdUsersMarkerEmailMarksGet");
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
| **markerEmail** | **String**| marker&#39;s email | |

### Return type

[**List&lt;OfferingUser&gt;**](OfferingUser.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | learners marked by the marker |  -  |
| **401** | No authorization token was found. |  -  |
| **403** | You are not allowed to access this resource. |  -  |
| **404** | Not Found |  -  |

<a id="offeringsOfferingIdUsersMarkerEmailMarksPost"></a>
# **offeringsOfferingIdUsersMarkerEmailMarksPost**
> List&lt;OfferingUser&gt; offeringsOfferingIdUsersMarkerEmailMarksPost(offeringId, markerEmail, requestBody)

Add learners to be marked by a coach

Adds an array of learners to be marked by the specified coach.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OfferingLearnersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.iqualify.com/v1");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    OfferingLearnersApi apiInstance = new OfferingLearnersApi(defaultClient);
    String offeringId = "offeringId_example"; // String | offering's id
    String markerEmail = "markerEmail_example"; // String | marker's email
    List<String> requestBody = Arrays.asList(); // List<String> | array of learners e-mails
    try {
      List<OfferingUser> result = apiInstance.offeringsOfferingIdUsersMarkerEmailMarksPost(offeringId, markerEmail, requestBody);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OfferingLearnersApi#offeringsOfferingIdUsersMarkerEmailMarksPost");
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
| **markerEmail** | **String**| marker&#39;s email | |
| **requestBody** | [**List&lt;String&gt;**](String.md)| array of learners e-mails | |

### Return type

[**List&lt;OfferingUser&gt;**](OfferingUser.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | learners marked by the marker |  -  |
| **400** | Bad Request |  -  |
| **401** | No authorization token was found. |  -  |
| **403** | You are not allowed to access this resource. |  -  |
| **404** | Not Found |  -  |

<a id="offeringsOfferingIdUsersPost"></a>
# **offeringsOfferingIdUsersPost**
> List&lt;OfferingUserAddResponse&gt; offeringsOfferingIdUsersPost(offeringId, offeringUser)

Adds user to the offering

Adds one or more users to the offering.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OfferingLearnersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.iqualify.com/v1");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    OfferingLearnersApi apiInstance = new OfferingLearnersApi(defaultClient);
    String offeringId = "offeringId_example"; // String | offering's id
    List<OfferingUser> offeringUser = Arrays.asList(); // List<OfferingUser> | 
    try {
      List<OfferingUserAddResponse> result = apiInstance.offeringsOfferingIdUsersPost(offeringId, offeringUser);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OfferingLearnersApi#offeringsOfferingIdUsersPost");
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
| **offeringUser** | [**List&lt;OfferingUser&gt;**](OfferingUser.md)|  | |

### Return type

[**List&lt;OfferingUserAddResponse&gt;**](OfferingUserAddResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | user successfully added to the offering |  -  |
| **207** | Partially successful response |  -  |
| **400** | Bad Request |  -  |
| **401** | No authorization token was found. |  -  |
| **403** | You are not allowed to access this resource. |  -  |
| **404** | Not Found |  -  |

<a id="offeringsOfferingIdUsersUserEmailDelete"></a>
# **offeringsOfferingIdUsersUserEmailDelete**
> offeringsOfferingIdUsersUserEmailDelete(offeringId, userEmail)

Removes user from the offering

Removes a user from the offering.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OfferingLearnersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.iqualify.com/v1");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    OfferingLearnersApi apiInstance = new OfferingLearnersApi(defaultClient);
    String offeringId = "offeringId_example"; // String | offering's id
    String userEmail = "userEmail_example"; // String | user's email
    try {
      apiInstance.offeringsOfferingIdUsersUserEmailDelete(offeringId, userEmail);
    } catch (ApiException e) {
      System.err.println("Exception when calling OfferingLearnersApi#offeringsOfferingIdUsersUserEmailDelete");
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

null (empty response body)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | user successfully removed from the offering |  -  |
| **400** | Bad Request |  -  |
| **401** | No authorization token was found. |  -  |
| **403** | You are not allowed to access this resource. |  -  |
| **404** | Not Found |  -  |

<a id="usersUserEmailTransferPatch"></a>
# **usersUserEmailTransferPatch**
> usersUserEmailTransferPatch(userEmail, transferRequest)

Transfer a user between offerings

Moves the user&#39;s access and progress from one offering to another.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OfferingLearnersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.iqualify.com/v1");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    OfferingLearnersApi apiInstance = new OfferingLearnersApi(defaultClient);
    String userEmail = "userEmail_example"; // String | user's email
    TransferRequest transferRequest = new TransferRequest(); // TransferRequest | transfer_data
    try {
      apiInstance.usersUserEmailTransferPatch(userEmail, transferRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling OfferingLearnersApi#usersUserEmailTransferPatch");
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
| **transferRequest** | [**TransferRequest**](TransferRequest.md)| transfer_data | |

### Return type

null (empty response body)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Updated user information |  -  |
| **400** | Bad Request |  -  |
| **401** | No authorization token was found. |  -  |
| **403** | You are not allowed to access this resource. |  -  |
| **404** | Not Found |  -  |

