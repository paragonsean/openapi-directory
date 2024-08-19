# AssessmentGroupsApi

All URIs are relative to *https://api.iqualify.com/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**offeringsOfferingIdGroupsGet**](AssessmentGroupsApi.md#offeringsOfferingIdGroupsGet) | **GET** /offerings/{offeringId}/groups | Find assessment groups |
| [**offeringsOfferingIdGroupsGroupIdLearnersGet**](AssessmentGroupsApi.md#offeringsOfferingIdGroupsGroupIdLearnersGet) | **GET** /offerings/{offeringId}/groups/{groupId}/learners | Find learners in an assessment group |
| [**offeringsOfferingIdGroupsGroupIdLearnersPost**](AssessmentGroupsApi.md#offeringsOfferingIdGroupsGroupIdLearnersPost) | **POST** /offerings/{offeringId}/groups/{groupId}/learners | Add a learner to an assessment group |
| [**offeringsOfferingIdGroupsGroupIdLearnersUserEmailDelete**](AssessmentGroupsApi.md#offeringsOfferingIdGroupsGroupIdLearnersUserEmailDelete) | **DELETE** /offerings/{offeringId}/groups/{groupId}/learners/{userEmail} | Remove a learner from an assessment group |
| [**offeringsOfferingIdGroupsPost**](AssessmentGroupsApi.md#offeringsOfferingIdGroupsPost) | **POST** /offerings/{offeringId}/groups | Add an assessment group |


<a id="offeringsOfferingIdGroupsGet"></a>
# **offeringsOfferingIdGroupsGet**
> List&lt;AssessmentGroupResponse&gt; offeringsOfferingIdGroupsGet(offeringId)

Find assessment groups

Responds with a list of assessment groups in an offering.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AssessmentGroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.iqualify.com/v1");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    AssessmentGroupsApi apiInstance = new AssessmentGroupsApi(defaultClient);
    String offeringId = "offeringId_example"; // String | offering's id
    try {
      List<AssessmentGroupResponse> result = apiInstance.offeringsOfferingIdGroupsGet(offeringId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AssessmentGroupsApi#offeringsOfferingIdGroupsGet");
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

[**List&lt;AssessmentGroupResponse&gt;**](AssessmentGroupResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Succesful response |  -  |
| **401** | No authorization token was found. |  -  |
| **403** | You are not allowed to access this resource. |  -  |
| **404** | Not Found |  -  |

<a id="offeringsOfferingIdGroupsGroupIdLearnersGet"></a>
# **offeringsOfferingIdGroupsGroupIdLearnersGet**
> List&lt;UserResponse&gt; offeringsOfferingIdGroupsGroupIdLearnersGet(offeringId, groupId)

Find learners in an assessment group

Responds with a list of learners in a specified assessment group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AssessmentGroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.iqualify.com/v1");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    AssessmentGroupsApi apiInstance = new AssessmentGroupsApi(defaultClient);
    String offeringId = "offeringId_example"; // String | offering's id
    String groupId = "groupId_example"; // String | Assessment group id
    try {
      List<UserResponse> result = apiInstance.offeringsOfferingIdGroupsGroupIdLearnersGet(offeringId, groupId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AssessmentGroupsApi#offeringsOfferingIdGroupsGroupIdLearnersGet");
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
| **groupId** | **String**| Assessment group id | |

### Return type

[**List&lt;UserResponse&gt;**](UserResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Succesful response |  -  |
| **400** | Bad Request |  -  |
| **401** | No authorization token was found. |  -  |
| **403** | You are not allowed to access this resource. |  -  |
| **404** | Not Found |  -  |

<a id="offeringsOfferingIdGroupsGroupIdLearnersPost"></a>
# **offeringsOfferingIdGroupsGroupIdLearnersPost**
> UserResponse offeringsOfferingIdGroupsGroupIdLearnersPost(offeringId, groupId, offeringsOfferingIdGroupsGroupIdLearnersPostRequest)

Add a learner to an assessment group

Adds a learner into the specified assessment group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AssessmentGroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.iqualify.com/v1");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    AssessmentGroupsApi apiInstance = new AssessmentGroupsApi(defaultClient);
    String offeringId = "offeringId_example"; // String | offering's id
    String groupId = "groupId_example"; // String | Assessment group id
    OfferingsOfferingIdGroupsGroupIdLearnersPostRequest offeringsOfferingIdGroupsGroupIdLearnersPostRequest = new OfferingsOfferingIdGroupsGroupIdLearnersPostRequest(); // OfferingsOfferingIdGroupsGroupIdLearnersPostRequest | 
    try {
      UserResponse result = apiInstance.offeringsOfferingIdGroupsGroupIdLearnersPost(offeringId, groupId, offeringsOfferingIdGroupsGroupIdLearnersPostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AssessmentGroupsApi#offeringsOfferingIdGroupsGroupIdLearnersPost");
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
| **groupId** | **String**| Assessment group id | |
| **offeringsOfferingIdGroupsGroupIdLearnersPostRequest** | [**OfferingsOfferingIdGroupsGroupIdLearnersPostRequest**](OfferingsOfferingIdGroupsGroupIdLearnersPostRequest.md)|  | |

### Return type

[**UserResponse**](UserResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Succesful response |  -  |
| **400** | Bad Request |  -  |
| **401** | No authorization token was found. |  -  |
| **403** | You are not allowed to access this resource. |  -  |
| **404** | Not Found |  -  |

<a id="offeringsOfferingIdGroupsGroupIdLearnersUserEmailDelete"></a>
# **offeringsOfferingIdGroupsGroupIdLearnersUserEmailDelete**
> offeringsOfferingIdGroupsGroupIdLearnersUserEmailDelete(offeringId, groupId, userEmail)

Remove a learner from an assessment group

Removes a learner from the specified assessment group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AssessmentGroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.iqualify.com/v1");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    AssessmentGroupsApi apiInstance = new AssessmentGroupsApi(defaultClient);
    String offeringId = "offeringId_example"; // String | offering's id
    String groupId = "groupId_example"; // String | Assessment group id
    String userEmail = "userEmail_example"; // String | user's email
    try {
      apiInstance.offeringsOfferingIdGroupsGroupIdLearnersUserEmailDelete(offeringId, groupId, userEmail);
    } catch (ApiException e) {
      System.err.println("Exception when calling AssessmentGroupsApi#offeringsOfferingIdGroupsGroupIdLearnersUserEmailDelete");
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
| **groupId** | **String**| Assessment group id | |
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
| **204** | user successfully removed from the assessment group |  -  |
| **400** | Bad Request |  -  |
| **401** | No authorization token was found. |  -  |
| **403** | You are not allowed to access this resource. |  -  |
| **404** | Not Found |  -  |

<a id="offeringsOfferingIdGroupsPost"></a>
# **offeringsOfferingIdGroupsPost**
> AssessmentGroupResponse offeringsOfferingIdGroupsPost(offeringId, assessmentGroupRequired)

Add an assessment group

Creates a new assessment group in an offering.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AssessmentGroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.iqualify.com/v1");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    AssessmentGroupsApi apiInstance = new AssessmentGroupsApi(defaultClient);
    String offeringId = "offeringId_example"; // String | offering's id
    AssessmentGroupRequired assessmentGroupRequired = new AssessmentGroupRequired(); // AssessmentGroupRequired | 
    try {
      AssessmentGroupResponse result = apiInstance.offeringsOfferingIdGroupsPost(offeringId, assessmentGroupRequired);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AssessmentGroupsApi#offeringsOfferingIdGroupsPost");
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
| **assessmentGroupRequired** | [**AssessmentGroupRequired**](AssessmentGroupRequired.md)|  | |

### Return type

[**AssessmentGroupResponse**](AssessmentGroupResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | assessment group successfully added |  -  |
| **400** | Bad Request |  -  |
| **401** | No authorization token was found. |  -  |
| **403** | You are not allowed to access this resource. |  -  |
| **404** | Not Found |  -  |

