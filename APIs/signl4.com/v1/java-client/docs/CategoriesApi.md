# CategoriesApi

All URIs are relative to *https://connect.signl4.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**categoriesImagesGet**](CategoriesApi.md#categoriesImagesGet) | **GET** /categories/images | Gets the names of all alert category images.  You can get the image by going to account.signl4.com/images/alerts/categoryImageName.svg |
| [**categoriesTeamIdCategoryIdDelete**](CategoriesApi.md#categoriesTeamIdCategoryIdDelete) | **DELETE** /categories/{teamId}/{categoryId} | Delete an existing category |
| [**categoriesTeamIdCategoryIdGet**](CategoriesApi.md#categoriesTeamIdCategoryIdGet) | **GET** /categories/{teamId}/{categoryId} | Get a specific category |
| [**categoriesTeamIdCategoryIdMetricsGet**](CategoriesApi.md#categoriesTeamIdCategoryIdMetricsGet) | **GET** /categories/{teamId}/{categoryId}/metrics | Get metrics for a specific category |
| [**categoriesTeamIdCategoryIdPut**](CategoriesApi.md#categoriesTeamIdCategoryIdPut) | **PUT** /categories/{teamId}/{categoryId} | Update an existing category |
| [**categoriesTeamIdCategoryIdSubscriptionsGet**](CategoriesApi.md#categoriesTeamIdCategoryIdSubscriptionsGet) | **GET** /categories/{teamId}/{categoryId}/subscriptions | Get category subscriptions |
| [**categoriesTeamIdCategoryIdSubscriptionsPost**](CategoriesApi.md#categoriesTeamIdCategoryIdSubscriptionsPost) | **POST** /categories/{teamId}/{categoryId}/subscriptions | Set category subscriptions |
| [**categoriesTeamIdGet**](CategoriesApi.md#categoriesTeamIdGet) | **GET** /categories/{teamId} | Get all categories |
| [**categoriesTeamIdMetricsGet**](CategoriesApi.md#categoriesTeamIdMetricsGet) | **GET** /categories/{teamId}/metrics | Get metrics for all categories |
| [**categoriesTeamIdPost**](CategoriesApi.md#categoriesTeamIdPost) | **POST** /categories/{teamId} | Create a new category |


<a id="categoriesImagesGet"></a>
# **categoriesImagesGet**
> List&lt;String&gt; categoriesImagesGet()

Gets the names of all alert category images.  You can get the image by going to account.signl4.com/images/alerts/categoryImageName.svg

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CategoriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.signl4.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    CategoriesApi apiInstance = new CategoriesApi(defaultClient);
    try {
      List<String> result = apiInstance.categoriesImagesGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CategoriesApi#categoriesImagesGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

**List&lt;String&gt;**

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns the alert categories. |  -  |
| **204** | Request was canceled. |  -  |
| **403** | If you have no permission to access the resource. |  -  |
| **404** | No categories were found. |  -  |
| **500** | Internal general error occured. |  -  |

<a id="categoriesTeamIdCategoryIdDelete"></a>
# **categoriesTeamIdCategoryIdDelete**
> categoriesTeamIdCategoryIdDelete(teamId, categoryId)

Delete an existing category

Sample Request:                    DELETE /categories/cbb70402-1359-477f-ac92-0171cf2b5ff7/c0054336-cd89-4abf-882d-ba69b5adb25e

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CategoriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.signl4.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    CategoriesApi apiInstance = new CategoriesApi(defaultClient);
    String teamId = "teamId_example"; // String | ID of the team the category belongs to
    String categoryId = "categoryId_example"; // String | ID of the category to delete
    try {
      apiInstance.categoriesTeamIdCategoryIdDelete(teamId, categoryId);
    } catch (ApiException e) {
      System.err.println("Exception when calling CategoriesApi#categoriesTeamIdCategoryIdDelete");
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
| **teamId** | **String**| ID of the team the category belongs to | |
| **categoryId** | **String**| ID of the category to delete | |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | If the delete operation was successful |  -  |
| **204** | Success |  -  |
| **400** | If the input is not valid |  -  |
| **403** | If you have no permission to access this resource |  -  |
| **404** | If the resource was not found |  -  |
| **500** | If any server side errors occur |  -  |

<a id="categoriesTeamIdCategoryIdGet"></a>
# **categoriesTeamIdCategoryIdGet**
> CategoryInfo categoriesTeamIdCategoryIdGet(teamId, categoryId)

Get a specific category

Sample Request:                    GET /categories/cbb70402-1359-477f-ac92-0171cf2b5ff7/c0054336-cd89-4abf-882d-ba69b5adb25e

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CategoriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.signl4.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    CategoriesApi apiInstance = new CategoriesApi(defaultClient);
    String teamId = "teamId_example"; // String | ID of the team the category belongs to
    String categoryId = "categoryId_example"; // String | ID of the category to get
    try {
      CategoryInfo result = apiInstance.categoriesTeamIdCategoryIdGet(teamId, categoryId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CategoriesApi#categoriesTeamIdCategoryIdGet");
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
| **teamId** | **String**| ID of the team the category belongs to | |
| **categoryId** | **String**| ID of the category to get | |

### Return type

[**CategoryInfo**](CategoryInfo.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns the category details |  -  |
| **400** | If the input is not valid |  -  |
| **403** | If you have no permission to access this resource |  -  |
| **404** | If the resource was not found |  -  |
| **500** | If any server side errors occur |  -  |

<a id="categoriesTeamIdCategoryIdMetricsGet"></a>
# **categoriesTeamIdCategoryIdMetricsGet**
> CategoryMetrics categoriesTeamIdCategoryIdMetricsGet(teamId, categoryId)

Get metrics for a specific category

Sample Request:                    GET /categories/cbb70402-1359-477f-ac92-0171cf2b5ff7/c0054336-cd89-4abf-882d-ba69b5adb25e/metrics

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CategoriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.signl4.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    CategoriesApi apiInstance = new CategoriesApi(defaultClient);
    String teamId = "teamId_example"; // String | ID of the team the category belongs to
    String categoryId = "categoryId_example"; // String | ID of the category to get
    try {
      CategoryMetrics result = apiInstance.categoriesTeamIdCategoryIdMetricsGet(teamId, categoryId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CategoriesApi#categoriesTeamIdCategoryIdMetricsGet");
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
| **teamId** | **String**| ID of the team the category belongs to | |
| **categoryId** | **String**| ID of the category to get | |

### Return type

[**CategoryMetrics**](CategoryMetrics.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns the category metrics |  -  |
| **400** | If the input is not valid |  -  |
| **403** | If you have no permission to access this resource |  -  |
| **404** | If the resource was not found |  -  |
| **500** | If any server side errors occur |  -  |

<a id="categoriesTeamIdCategoryIdPut"></a>
# **categoriesTeamIdCategoryIdPut**
> CategoryInfo categoriesTeamIdCategoryIdPut(teamId, categoryId, categoryInfo)

Update an existing category

Sample Request:                    PUT /categories/cbb70402-1359-477f-ac92-0171cf2b5ff7/c0054336-cd89-4abf-882d-ba69b5adb25e      {          \&quot;name\&quot;: \&quot;Water-Updated\&quot;,          \&quot;imageName\&quot;: \&quot;water.svg\&quot;,          \&quot;color\&quot;: \&quot;#0000cc\&quot;,          \&quot;keywordMatching\&quot;: \&quot;All\&quot;,          \&quot;keywords\&quot;: [              {                  \&quot;value\&quot;: \&quot;H2O\&quot;              },              {                  \&quot;value\&quot;: \&quot;Water\&quot;              },              {                  \&quot;value\&quot;: \&quot;Wet\&quot;              }          ]      }

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CategoriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.signl4.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    CategoriesApi apiInstance = new CategoriesApi(defaultClient);
    String teamId = "teamId_example"; // String | ID of the team the category belongs to
    String categoryId = "categoryId_example"; // String | 
    CategoryInfo categoryInfo = new CategoryInfo(); // CategoryInfo | Category to be updated
    try {
      CategoryInfo result = apiInstance.categoriesTeamIdCategoryIdPut(teamId, categoryId, categoryInfo);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CategoriesApi#categoriesTeamIdCategoryIdPut");
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
| **teamId** | **String**| ID of the team the category belongs to | |
| **categoryId** | **String**|  | |
| **categoryInfo** | [**CategoryInfo**](CategoryInfo.md)| Category to be updated | [optional] |

### Return type

[**CategoryInfo**](CategoryInfo.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns the updated category |  -  |
| **400** | If the input is not valid |  -  |
| **403** | If you have no permission to access this resource |  -  |
| **404** | If the resource was not found |  -  |
| **500** | If any server side errors occur |  -  |

<a id="categoriesTeamIdCategoryIdSubscriptionsGet"></a>
# **categoriesTeamIdCategoryIdSubscriptionsGet**
> List&lt;CategorySubscriptionInfo&gt; categoriesTeamIdCategoryIdSubscriptionsGet(teamId, categoryId)

Get category subscriptions

Sample Request:                    GET /categories/cbb70402-1359-477f-ac92-0171cf2b5ff7/c0054336-cd89-4abf-882d-ba69b5adb25e/subscriptions      {      }

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CategoriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.signl4.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    CategoriesApi apiInstance = new CategoriesApi(defaultClient);
    String teamId = "teamId_example"; // String | ID of the team the category belongs to
    String categoryId = "categoryId_example"; // String | Category to get subscriptions for
    try {
      List<CategorySubscriptionInfo> result = apiInstance.categoriesTeamIdCategoryIdSubscriptionsGet(teamId, categoryId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CategoriesApi#categoriesTeamIdCategoryIdSubscriptionsGet");
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
| **teamId** | **String**| ID of the team the category belongs to | |
| **categoryId** | **String**| Category to get subscriptions for | |

### Return type

[**List&lt;CategorySubscriptionInfo&gt;**](CategorySubscriptionInfo.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns the category subscriptions |  -  |
| **400** | If the input is not valid |  -  |
| **403** | If you have no permission to access this resource |  -  |
| **404** | If the resource was not found |  -  |
| **500** | If any server side errors occur |  -  |

<a id="categoriesTeamIdCategoryIdSubscriptionsPost"></a>
# **categoriesTeamIdCategoryIdSubscriptionsPost**
> List&lt;CategorySubscriptionInfo&gt; categoriesTeamIdCategoryIdSubscriptionsPost(teamId, categoryId, categorySubscriptionInfo)

Set category subscriptions

Sample Request:                    POST /categories/cbb70402-1359-477f-ac92-0171cf2b5ff7/c0054336-cd89-4abf-882d-ba69b5adb25e/subscriptions      {      }

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CategoriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.signl4.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    CategoriesApi apiInstance = new CategoriesApi(defaultClient);
    String teamId = "teamId_example"; // String | ID of the team the category belongs to
    String categoryId = "categoryId_example"; // String | Category to be updated
    List<CategorySubscriptionInfo> categorySubscriptionInfo = Arrays.asList(); // List<CategorySubscriptionInfo> | 
    try {
      List<CategorySubscriptionInfo> result = apiInstance.categoriesTeamIdCategoryIdSubscriptionsPost(teamId, categoryId, categorySubscriptionInfo);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CategoriesApi#categoriesTeamIdCategoryIdSubscriptionsPost");
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
| **teamId** | **String**| ID of the team the category belongs to | |
| **categoryId** | **String**| Category to be updated | |
| **categorySubscriptionInfo** | [**List&lt;CategorySubscriptionInfo&gt;**](CategorySubscriptionInfo.md)|  | [optional] |

### Return type

[**List&lt;CategorySubscriptionInfo&gt;**](CategorySubscriptionInfo.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns the updated category subscriptions |  -  |
| **400** | If the input is not valid |  -  |
| **403** | If you have no permission to access this resource |  -  |
| **404** | If the resource was not found |  -  |
| **500** | If any server side errors occur |  -  |

<a id="categoriesTeamIdGet"></a>
# **categoriesTeamIdGet**
> List&lt;CategoryInfo&gt; categoriesTeamIdGet(teamId)

Get all categories

Sample Request:                    GET /categories/cbb70402-1359-477f-ac92-0171cf2b5ff7

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CategoriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.signl4.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    CategoriesApi apiInstance = new CategoriesApi(defaultClient);
    String teamId = "teamId_example"; // String | ID of the team the categories belong to
    try {
      List<CategoryInfo> result = apiInstance.categoriesTeamIdGet(teamId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CategoriesApi#categoriesTeamIdGet");
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
| **teamId** | **String**| ID of the team the categories belong to | |

### Return type

[**List&lt;CategoryInfo&gt;**](CategoryInfo.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns the category infos |  -  |
| **400** | If the input is not valid |  -  |
| **403** | If you have no permission to access this resource |  -  |
| **404** | If the resource was not found |  -  |
| **500** | If any server side errors occur |  -  |

<a id="categoriesTeamIdMetricsGet"></a>
# **categoriesTeamIdMetricsGet**
> List&lt;CategoryMetrics&gt; categoriesTeamIdMetricsGet(teamId)

Get metrics for all categories

Sample Request:                    GET /categories/cbb70402-1359-477f-ac92-0171cf2b5ff7/metrics

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CategoriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.signl4.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    CategoriesApi apiInstance = new CategoriesApi(defaultClient);
    String teamId = "teamId_example"; // String | ID of the team the categories belongs to
    try {
      List<CategoryMetrics> result = apiInstance.categoriesTeamIdMetricsGet(teamId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CategoriesApi#categoriesTeamIdMetricsGet");
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
| **teamId** | **String**| ID of the team the categories belongs to | |

### Return type

[**List&lt;CategoryMetrics&gt;**](CategoryMetrics.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns a list of category metrics |  -  |
| **400** | If the input is not valid |  -  |
| **403** | If you have no permission to access this resource |  -  |
| **404** | If the resource was not found |  -  |
| **500** | If any server side errors occur |  -  |

<a id="categoriesTeamIdPost"></a>
# **categoriesTeamIdPost**
> CategoryInfo categoriesTeamIdPost(teamId, categoryInfo)

Create a new category

Sample Request:                    POST /categories/cbb70402-1359-477f-ac92-0171cf2b5ff7      {          \&quot;name\&quot;: \&quot;Water\&quot;,          \&quot;imageName\&quot;: \&quot;water.svg\&quot;,          \&quot;color\&quot;: \&quot;#0000cc\&quot;,          \&quot;keywordMatching\&quot;: \&quot;Any\&quot;,          \&quot;keywords\&quot;: [              {                  \&quot;value\&quot;: \&quot;H2O\&quot;              },              {                  \&quot;value\&quot;: \&quot;Water\&quot;              }          ]      }

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CategoriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.signl4.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    CategoriesApi apiInstance = new CategoriesApi(defaultClient);
    String teamId = "teamId_example"; // String | ID of the team the category belongs to
    CategoryInfo categoryInfo = new CategoryInfo(); // CategoryInfo | Category to be created
    try {
      CategoryInfo result = apiInstance.categoriesTeamIdPost(teamId, categoryInfo);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CategoriesApi#categoriesTeamIdPost");
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
| **teamId** | **String**| ID of the team the category belongs to | |
| **categoryInfo** | [**CategoryInfo**](CategoryInfo.md)| Category to be created | [optional] |

### Return type

[**CategoryInfo**](CategoryInfo.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Returns the newly created category |  -  |
| **400** | If the input is not valid |  -  |
| **403** | If you have no permission to access this resource |  -  |
| **404** | If the resource was not found |  -  |
| **500** | If any server side errors occur |  -  |

