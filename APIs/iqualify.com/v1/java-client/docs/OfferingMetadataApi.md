# OfferingMetadataApi

All URIs are relative to *https://api.iqualify.com/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**offeringsOfferingIdMetadataCategoryPut**](OfferingMetadataApi.md#offeringsOfferingIdMetadataCategoryPut) | **PUT** /offerings/{offeringId}/metadata/category | Update offering category metadata |
| [**offeringsOfferingIdMetadataLevelPut**](OfferingMetadataApi.md#offeringsOfferingIdMetadataLevelPut) | **PUT** /offerings/{offeringId}/metadata/level | Update offering level metadata |
| [**offeringsOfferingIdMetadataTagsPut**](OfferingMetadataApi.md#offeringsOfferingIdMetadataTagsPut) | **PUT** /offerings/{offeringId}/metadata/tags | Update offering tags metadata |
| [**offeringsOfferingIdMetadataTopicPut**](OfferingMetadataApi.md#offeringsOfferingIdMetadataTopicPut) | **PUT** /offerings/{offeringId}/metadata/topic | Update offering topic metadata |


<a id="offeringsOfferingIdMetadataCategoryPut"></a>
# **offeringsOfferingIdMetadataCategoryPut**
> OfferingMetadataResponse offeringsOfferingIdMetadataCategoryPut(offeringId, coursesContentIdMetadataCategoryPutRequest)

Update offering category metadata

Updates the offering category metadata.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OfferingMetadataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.iqualify.com/v1");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    OfferingMetadataApi apiInstance = new OfferingMetadataApi(defaultClient);
    String offeringId = "offeringId_example"; // String | offering's id
    CoursesContentIdMetadataCategoryPutRequest coursesContentIdMetadataCategoryPutRequest = new CoursesContentIdMetadataCategoryPutRequest(); // CoursesContentIdMetadataCategoryPutRequest | 
    try {
      OfferingMetadataResponse result = apiInstance.offeringsOfferingIdMetadataCategoryPut(offeringId, coursesContentIdMetadataCategoryPutRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OfferingMetadataApi#offeringsOfferingIdMetadataCategoryPut");
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
| **coursesContentIdMetadataCategoryPutRequest** | [**CoursesContentIdMetadataCategoryPutRequest**](CoursesContentIdMetadataCategoryPutRequest.md)|  | |

### Return type

[**OfferingMetadataResponse**](OfferingMetadataResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | offering updated |  -  |
| **400** | Bad Request |  -  |
| **401** | No authorization token was found. |  -  |
| **403** | You are not allowed to access this resource. |  -  |
| **404** | Not Found |  -  |

<a id="offeringsOfferingIdMetadataLevelPut"></a>
# **offeringsOfferingIdMetadataLevelPut**
> OfferingMetadataResponse offeringsOfferingIdMetadataLevelPut(offeringId, coursesContentIdMetadataLevelPutRequest)

Update offering level metadata

Updates the offering level metadata.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OfferingMetadataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.iqualify.com/v1");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    OfferingMetadataApi apiInstance = new OfferingMetadataApi(defaultClient);
    String offeringId = "offeringId_example"; // String | offering's id
    CoursesContentIdMetadataLevelPutRequest coursesContentIdMetadataLevelPutRequest = new CoursesContentIdMetadataLevelPutRequest(); // CoursesContentIdMetadataLevelPutRequest | 
    try {
      OfferingMetadataResponse result = apiInstance.offeringsOfferingIdMetadataLevelPut(offeringId, coursesContentIdMetadataLevelPutRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OfferingMetadataApi#offeringsOfferingIdMetadataLevelPut");
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
| **coursesContentIdMetadataLevelPutRequest** | [**CoursesContentIdMetadataLevelPutRequest**](CoursesContentIdMetadataLevelPutRequest.md)|  | |

### Return type

[**OfferingMetadataResponse**](OfferingMetadataResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | offering updated |  -  |
| **400** | Bad Request |  -  |
| **401** | No authorization token was found. |  -  |
| **403** | You are not allowed to access this resource. |  -  |
| **404** | Not Found |  -  |

<a id="offeringsOfferingIdMetadataTagsPut"></a>
# **offeringsOfferingIdMetadataTagsPut**
> OfferingMetadataResponse offeringsOfferingIdMetadataTagsPut(offeringId, coursesContentIdMetadataTagsPutRequest)

Update offering tags metadata

Updates the offering tags metadata.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OfferingMetadataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.iqualify.com/v1");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    OfferingMetadataApi apiInstance = new OfferingMetadataApi(defaultClient);
    String offeringId = "offeringId_example"; // String | offering's id
    CoursesContentIdMetadataTagsPutRequest coursesContentIdMetadataTagsPutRequest = new CoursesContentIdMetadataTagsPutRequest(); // CoursesContentIdMetadataTagsPutRequest | 
    try {
      OfferingMetadataResponse result = apiInstance.offeringsOfferingIdMetadataTagsPut(offeringId, coursesContentIdMetadataTagsPutRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OfferingMetadataApi#offeringsOfferingIdMetadataTagsPut");
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
| **coursesContentIdMetadataTagsPutRequest** | [**CoursesContentIdMetadataTagsPutRequest**](CoursesContentIdMetadataTagsPutRequest.md)|  | |

### Return type

[**OfferingMetadataResponse**](OfferingMetadataResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | offering updated |  -  |
| **400** | Bad Request |  -  |
| **401** | No authorization token was found. |  -  |
| **403** | You are not allowed to access this resource. |  -  |
| **404** | Not Found |  -  |

<a id="offeringsOfferingIdMetadataTopicPut"></a>
# **offeringsOfferingIdMetadataTopicPut**
> OfferingMetadataResponse offeringsOfferingIdMetadataTopicPut(offeringId, coursesContentIdMetadataTopicPutRequest)

Update offering topic metadata

Updates the offering topic metadata.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OfferingMetadataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.iqualify.com/v1");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    OfferingMetadataApi apiInstance = new OfferingMetadataApi(defaultClient);
    String offeringId = "offeringId_example"; // String | offering's id
    CoursesContentIdMetadataTopicPutRequest coursesContentIdMetadataTopicPutRequest = new CoursesContentIdMetadataTopicPutRequest(); // CoursesContentIdMetadataTopicPutRequest | 
    try {
      OfferingMetadataResponse result = apiInstance.offeringsOfferingIdMetadataTopicPut(offeringId, coursesContentIdMetadataTopicPutRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OfferingMetadataApi#offeringsOfferingIdMetadataTopicPut");
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
| **coursesContentIdMetadataTopicPutRequest** | [**CoursesContentIdMetadataTopicPutRequest**](CoursesContentIdMetadataTopicPutRequest.md)|  | |

### Return type

[**OfferingMetadataResponse**](OfferingMetadataResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | offering updated |  -  |
| **400** | Bad Request |  -  |
| **401** | No authorization token was found. |  -  |
| **403** | You are not allowed to access this resource. |  -  |
| **404** | Not Found |  -  |

