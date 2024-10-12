# FeatureApi

All URIs are relative to *https://api.feedback.eu.pendo.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**featuresGet**](FeatureApi.md#featuresGet) | **GET** /features | Query features |
| [**featuresIdGet**](FeatureApi.md#featuresIdGet) | **GET** /features/{id} | Get a Feature by ID |
| [**featuresIdTagsDelete**](FeatureApi.md#featuresIdTagsDelete) | **DELETE** /features/{id}/tags | Delete custom Feature tags |
| [**featuresIdTagsGet**](FeatureApi.md#featuresIdTagsGet) | **GET** /features/{id}/tags | Get custom Feature tags |
| [**featuresIdTagsPost**](FeatureApi.md#featuresIdTagsPost) | **POST** /features/{id}/tags | Overwrite current custom Feature tags with the given tags |
| [**searchGet**](FeatureApi.md#searchGet) | **GET** /search | Search features |


<a id="featuresGet"></a>
# **featuresGet**
> List&lt;Feature&gt; featuresGet(limit, start, orderDir, isPrivate, wantedBy, orderBy, tags, products)

Query features

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FeatureApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.feedback.eu.pendo.io");
    
    // Configure API key authorization: userApiKey (request header)
    ApiKeyAuth userApiKey (request header) = (ApiKeyAuth) defaultClient.getAuthentication("userApiKey (request header)");
    userApiKey (request header).setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //userApiKey (request header).setApiKeyPrefix("Token");

    // Configure API key authorization: userApiKey (query parameter)
    ApiKeyAuth userApiKey (query parameter) = (ApiKeyAuth) defaultClient.getAuthentication("userApiKey (query parameter)");
    userApiKey (query parameter).setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //userApiKey (query parameter).setApiKeyPrefix("Token");

    FeatureApi apiInstance = new FeatureApi(defaultClient);
    BigDecimal limit = new BigDecimal(78); // BigDecimal | Limit the number of records returned
    BigDecimal start = new BigDecimal(78); // BigDecimal | Offset to start at
    String orderDir = "asc"; // String | The sort direction
    Boolean isPrivate = true; // Boolean | Filter by whether the features are shown/hidden from customer, if supplied.
    Integer wantedBy = 56; // Integer | Filter by User ID, if supplied.
    String orderBy = "title"; // String | The field to use for sort
    String tags = "tags_example"; // String | Tags to limit results by. Multiple tags can be provided via comma delimeted string. Tags with contexts can be used. E.g. \"....&tags=TagExample,Multi:TagThis,Multi:TagThat\".
    String products = "products_example"; // String | Products to limit results by. Comma delimeted string of either ids or names. E.g. \"...&products=1,2,3\" or \"...products=Product1,Product2\".
    try {
      List<Feature> result = apiInstance.featuresGet(limit, start, orderDir, isPrivate, wantedBy, orderBy, tags, products);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FeatureApi#featuresGet");
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
| **limit** | **BigDecimal**| Limit the number of records returned | [optional] |
| **start** | **BigDecimal**| Offset to start at | [optional] |
| **orderDir** | **String**| The sort direction | [optional] [enum: asc, desc] |
| **isPrivate** | **Boolean**| Filter by whether the features are shown/hidden from customer, if supplied. | [optional] |
| **wantedBy** | **Integer**| Filter by User ID, if supplied. | [optional] |
| **orderBy** | **String**| The field to use for sort | [optional] [enum: title, created_at, updated_at, declined_at, developing_at, planned_at, released_at, waiting_at, deleted_at] |
| **tags** | **String**| Tags to limit results by. Multiple tags can be provided via comma delimeted string. Tags with contexts can be used. E.g. \&quot;....&amp;tags&#x3D;TagExample,Multi:TagThis,Multi:TagThat\&quot;. | [optional] |
| **products** | **String**| Products to limit results by. Comma delimeted string of either ids or names. E.g. \&quot;...&amp;products&#x3D;1,2,3\&quot; or \&quot;...products&#x3D;Product1,Product2\&quot;. | [optional] |

### Return type

[**List&lt;Feature&gt;**](Feature.md)

### Authorization

[userApiKey (request header)](../README.md#userApiKey (request header)), [userApiKey (query parameter)](../README.md#userApiKey (query parameter))

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="featuresIdGet"></a>
# **featuresIdGet**
> Feature featuresIdGet(id)

Get a Feature by ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FeatureApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.feedback.eu.pendo.io");
    
    // Configure API key authorization: userApiKey (request header)
    ApiKeyAuth userApiKey (request header) = (ApiKeyAuth) defaultClient.getAuthentication("userApiKey (request header)");
    userApiKey (request header).setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //userApiKey (request header).setApiKeyPrefix("Token");

    // Configure API key authorization: userApiKey (query parameter)
    ApiKeyAuth userApiKey (query parameter) = (ApiKeyAuth) defaultClient.getAuthentication("userApiKey (query parameter)");
    userApiKey (query parameter).setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //userApiKey (query parameter).setApiKeyPrefix("Token");

    FeatureApi apiInstance = new FeatureApi(defaultClient);
    Integer id = 56; // Integer | ID of the feature
    try {
      Feature result = apiInstance.featuresIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FeatureApi#featuresIdGet");
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
| **id** | **Integer**| ID of the feature | |

### Return type

[**Feature**](Feature.md)

### Authorization

[userApiKey (request header)](../README.md#userApiKey (request header)), [userApiKey (query parameter)](../README.md#userApiKey (query parameter))

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | ok |  -  |

<a id="featuresIdTagsDelete"></a>
# **featuresIdTagsDelete**
> featuresIdTagsDelete(id)

Delete custom Feature tags

Removes all custom tags associated with the Feature

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FeatureApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.feedback.eu.pendo.io");
    
    // Configure API key authorization: userApiKey (request header)
    ApiKeyAuth userApiKey (request header) = (ApiKeyAuth) defaultClient.getAuthentication("userApiKey (request header)");
    userApiKey (request header).setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //userApiKey (request header).setApiKeyPrefix("Token");

    // Configure API key authorization: userApiKey (query parameter)
    ApiKeyAuth userApiKey (query parameter) = (ApiKeyAuth) defaultClient.getAuthentication("userApiKey (query parameter)");
    userApiKey (query parameter).setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //userApiKey (query parameter).setApiKeyPrefix("Token");

    FeatureApi apiInstance = new FeatureApi(defaultClient);
    BigDecimal id = new BigDecimal(78); // BigDecimal | Feedback's Feature ID
    try {
      apiInstance.featuresIdTagsDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling FeatureApi#featuresIdTagsDelete");
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
| **id** | **BigDecimal**| Feedback&#39;s Feature ID | |

### Return type

null (empty response body)

### Authorization

[userApiKey (request header)](../README.md#userApiKey (request header)), [userApiKey (query parameter)](../README.md#userApiKey (query parameter))

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | success |  -  |

<a id="featuresIdTagsGet"></a>
# **featuresIdTagsGet**
> featuresIdTagsGet(id)

Get custom Feature tags

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FeatureApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.feedback.eu.pendo.io");
    
    // Configure API key authorization: userApiKey (request header)
    ApiKeyAuth userApiKey (request header) = (ApiKeyAuth) defaultClient.getAuthentication("userApiKey (request header)");
    userApiKey (request header).setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //userApiKey (request header).setApiKeyPrefix("Token");

    // Configure API key authorization: userApiKey (query parameter)
    ApiKeyAuth userApiKey (query parameter) = (ApiKeyAuth) defaultClient.getAuthentication("userApiKey (query parameter)");
    userApiKey (query parameter).setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //userApiKey (query parameter).setApiKeyPrefix("Token");

    FeatureApi apiInstance = new FeatureApi(defaultClient);
    BigDecimal id = new BigDecimal(78); // BigDecimal | Account ID (generated by Feedback)
    try {
      apiInstance.featuresIdTagsGet(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling FeatureApi#featuresIdTagsGet");
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
| **id** | **BigDecimal**| Account ID (generated by Feedback) | |

### Return type

null (empty response body)

### Authorization

[userApiKey (request header)](../README.md#userApiKey (request header)), [userApiKey (query parameter)](../README.md#userApiKey (query parameter))

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns an array of maps specifying tags under each tag group, for example:  [  {&#39;impacts&#39; &#x3D;&gt; [&#39;sales&#39;]},  {&#39;resources&#39; &#x3D;&gt; [&#39;dev&#39;, &#39;test&#39;, &#39;support&#39;]}  ] |  -  |
| **404** | Feature not found |  -  |

<a id="featuresIdTagsPost"></a>
# **featuresIdTagsPost**
> featuresIdTagsPost(id, tags)

Overwrite current custom Feature tags with the given tags

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FeatureApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.feedback.eu.pendo.io");
    
    // Configure API key authorization: userApiKey (request header)
    ApiKeyAuth userApiKey (request header) = (ApiKeyAuth) defaultClient.getAuthentication("userApiKey (request header)");
    userApiKey (request header).setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //userApiKey (request header).setApiKeyPrefix("Token");

    // Configure API key authorization: userApiKey (query parameter)
    ApiKeyAuth userApiKey (query parameter) = (ApiKeyAuth) defaultClient.getAuthentication("userApiKey (query parameter)");
    userApiKey (query parameter).setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //userApiKey (query parameter).setApiKeyPrefix("Token");

    FeatureApi apiInstance = new FeatureApi(defaultClient);
    BigDecimal id = new BigDecimal(78); // BigDecimal | Feedback's Feature ID
    Object tags = null; // Object | 
    try {
      apiInstance.featuresIdTagsPost(id, tags);
    } catch (ApiException e) {
      System.err.println("Exception when calling FeatureApi#featuresIdTagsPost");
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
| **id** | **BigDecimal**| Feedback&#39;s Feature ID | |
| **tags** | **Object**|  | |

### Return type

null (empty response body)

### Authorization

[userApiKey (request header)](../README.md#userApiKey (request header)), [userApiKey (query parameter)](../README.md#userApiKey (query parameter))

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Updated Feature tags |  -  |
| **404** | Feature not found |  -  |

<a id="searchGet"></a>
# **searchGet**
> List&lt;Feature&gt; searchGet(scope, q, status, tags, products)

Search features

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FeatureApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.feedback.eu.pendo.io");
    
    // Configure API key authorization: userApiKey (request header)
    ApiKeyAuth userApiKey (request header) = (ApiKeyAuth) defaultClient.getAuthentication("userApiKey (request header)");
    userApiKey (request header).setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //userApiKey (request header).setApiKeyPrefix("Token");

    // Configure API key authorization: userApiKey (query parameter)
    ApiKeyAuth userApiKey (query parameter) = (ApiKeyAuth) defaultClient.getAuthentication("userApiKey (query parameter)");
    userApiKey (query parameter).setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //userApiKey (query parameter).setApiKeyPrefix("Token");

    FeatureApi apiInstance = new FeatureApi(defaultClient);
    String scope = "feature"; // String | Specifies the type of entity being searched for. Must be set to 'feature'
    String q = "q_example"; // String | The search term.
    String status = "new"; // String | A comma seperated list of status values to filter by, if required. Valid values: 'new', 'waiting', 'planned', 'developing', 'released', 'declined'.
    String tags = "tags_example"; // String | Tags to limit results by - only applies when scope is 'case' or 'feature'. Multiple tags can be provided via comma delimeted string. Tags with contexts can be used. E.g. \"....&tags=TagExample,Multi:TagThis,Multi:TagThat\".
    String products = "products_example"; // String | Products to limit results by. Comma delimeted string of either ids or names. E.g. \"...&products=1,2,3\" or \"...products=Product1,Product2\".
    try {
      List<Feature> result = apiInstance.searchGet(scope, q, status, tags, products);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FeatureApi#searchGet");
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
| **scope** | **String**| Specifies the type of entity being searched for. Must be set to &#39;feature&#39; | [enum: feature] |
| **q** | **String**| The search term. | |
| **status** | **String**| A comma seperated list of status values to filter by, if required. Valid values: &#39;new&#39;, &#39;waiting&#39;, &#39;planned&#39;, &#39;developing&#39;, &#39;released&#39;, &#39;declined&#39;. | [optional] [enum: new, waiting, planned, developing, released, declined] |
| **tags** | **String**| Tags to limit results by - only applies when scope is &#39;case&#39; or &#39;feature&#39;. Multiple tags can be provided via comma delimeted string. Tags with contexts can be used. E.g. \&quot;....&amp;tags&#x3D;TagExample,Multi:TagThis,Multi:TagThat\&quot;. | [optional] |
| **products** | **String**| Products to limit results by. Comma delimeted string of either ids or names. E.g. \&quot;...&amp;products&#x3D;1,2,3\&quot; or \&quot;...products&#x3D;Product1,Product2\&quot;. | [optional] |

### Return type

[**List&lt;Feature&gt;**](Feature.md)

### Authorization

[userApiKey (request header)](../README.md#userApiKey (request header)), [userApiKey (query parameter)](../README.md#userApiKey (query parameter))

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

