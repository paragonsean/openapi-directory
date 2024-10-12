# ProjectActivitiesApi

All URIs are relative to *https://apis.e-conomic.com/api/v20.0.0*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createProjectActivity**](ProjectActivitiesApi.md#createProjectActivity) | **POST** /project-activities | Create a single Project Activity |
| [**deleteProjectActivityById**](ProjectActivitiesApi.md#deleteProjectActivityById) | **DELETE** /project-activities/{number} | Delete single Project Activity |
| [**getAllProjectActivities**](ProjectActivitiesApi.md#getAllProjectActivities) | **GET** /project-activities | Retrieve all Project Activities |
| [**getNumberOfProjectActivities**](ProjectActivitiesApi.md#getNumberOfProjectActivities) | **GET** /project-activities/count | Retrieve the number of Project Activities |
| [**getPageOfProjectActivities**](ProjectActivitiesApi.md#getPageOfProjectActivities) | **GET** /project-activities/paged | Retrieve a page of Project Activities |
| [**getProjectActivityById**](ProjectActivitiesApi.md#getProjectActivityById) | **GET** /project-activities/{number} | Retrieve single Project Activity |
| [**updateProjectActivity**](ProjectActivitiesApi.md#updateProjectActivity) | **PUT** /project-activities | Update a single Project Activity |


<a id="createProjectActivity"></a>
# **createProjectActivity**
> CreatedResult createProjectActivity(projectActivity)

Create a single Project Activity

Use this endpoint to create a single Project Activity.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectActivitiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://apis.e-conomic.com/api/v20.0.0");
    
    // Configure API key authorization: X-AgreementGrantToken
    ApiKeyAuth X-AgreementGrantToken = (ApiKeyAuth) defaultClient.getAuthentication("X-AgreementGrantToken");
    X-AgreementGrantToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AgreementGrantToken.setApiKeyPrefix("Token");

    // Configure API key authorization: X-AppSecretToken
    ApiKeyAuth X-AppSecretToken = (ApiKeyAuth) defaultClient.getAuthentication("X-AppSecretToken");
    X-AppSecretToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AppSecretToken.setApiKeyPrefix("Token");

    ProjectActivitiesApi apiInstance = new ProjectActivitiesApi(defaultClient);
    ProjectActivity projectActivity = new ProjectActivity(); // ProjectActivity | 
    try {
      CreatedResult result = apiInstance.createProjectActivity(projectActivity);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectActivitiesApi#createProjectActivity");
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
| **projectActivity** | [**ProjectActivity**](ProjectActivity.md)|  | [optional] |

### Return type

[**CreatedResult**](CreatedResult.md)

### Authorization

[X-AgreementGrantToken](../README.md#X-AgreementGrantToken), [X-AppSecretToken](../README.md#X-AppSecretToken)

### HTTP request headers

 - **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Success |  -  |
| **400** | **Bad request.** Your request does not pass our validation. See the message for more details. |  -  |
| **401** | **Unauthorized access.** Please take a look at https://apis.e-conomic.com and follow the links to help on authorization, or use the word demo for both tokens. |  -  |
| **403** | **Access forbidden.** You won’t necessarily have access to everything. So even though you were authorized we might still deny access to certain resources. This depends on the roles asked for when the grant was issued. |  -  |
| **429** | **Too many requests.** You have made too many calls towards our API. You are over your quota. Need to wait a bit. Check info in the response headers. |  -  |
| **500** | **Internal server error.** Something went wrong but the error has been logged. If you continue to see errors here, please contact api@e-conomic.com. Remember to include log id and agreement number when contacting support. |  -  |

<a id="deleteProjectActivityById"></a>
# **deleteProjectActivityById**
> deleteProjectActivityById(number)

Delete single Project Activity

Use this endpoint to delete a single Project Activity by id/number.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectActivitiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://apis.e-conomic.com/api/v20.0.0");
    
    // Configure API key authorization: X-AgreementGrantToken
    ApiKeyAuth X-AgreementGrantToken = (ApiKeyAuth) defaultClient.getAuthentication("X-AgreementGrantToken");
    X-AgreementGrantToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AgreementGrantToken.setApiKeyPrefix("Token");

    // Configure API key authorization: X-AppSecretToken
    ApiKeyAuth X-AppSecretToken = (ApiKeyAuth) defaultClient.getAuthentication("X-AppSecretToken");
    X-AppSecretToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AppSecretToken.setApiKeyPrefix("Token");

    ProjectActivitiesApi apiInstance = new ProjectActivitiesApi(defaultClient);
    Integer number = 56; // Integer | 
    try {
      apiInstance.deleteProjectActivityById(number);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectActivitiesApi#deleteProjectActivityById");
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
| **number** | **Integer**|  | |

### Return type

null (empty response body)

### Authorization

[X-AgreementGrantToken](../README.md#X-AgreementGrantToken), [X-AppSecretToken](../README.md#X-AppSecretToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **400** | **Bad request.** Your request does not pass our validation. See the message for more details. |  -  |
| **401** | **Unauthorized access.** Please take a look at https://apis.e-conomic.com and follow the links to help on authorization, or use the word demo for both tokens. |  -  |
| **403** | **Access forbidden.** You won’t necessarily have access to everything. So even though you were authorized we might still deny access to certain resources. This depends on the roles asked for when the grant was issued. |  -  |
| **404** | **Resource not found.** The resource you have been looking for does not exist. |  -  |
| **429** | **Too many requests.** You have made too many calls towards our API. You are over your quota. Need to wait a bit. Check info in the response headers. |  -  |
| **500** | **Internal server error.** Something went wrong but the error has been logged. If you continue to see errors here, please contact api@e-conomic.com. Remember to include log id and agreement number when contacting support. |  -  |

<a id="getAllProjectActivities"></a>
# **getAllProjectActivities**
> ProjectActivityCursorResults getAllProjectActivities(cursor, filter)

Retrieve all Project Activities

Use this endpoint to retrieve all Project Activities in bulk.  Max number of items returned in a single call is 1000. Use the continuation cursor parameter to set the continuation cursor for retrieval of next set of data. [pagination instructions](#section/Retrieving-data/Pagination)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectActivitiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://apis.e-conomic.com/api/v20.0.0");
    
    // Configure API key authorization: X-AgreementGrantToken
    ApiKeyAuth X-AgreementGrantToken = (ApiKeyAuth) defaultClient.getAuthentication("X-AgreementGrantToken");
    X-AgreementGrantToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AgreementGrantToken.setApiKeyPrefix("Token");

    // Configure API key authorization: X-AppSecretToken
    ApiKeyAuth X-AppSecretToken = (ApiKeyAuth) defaultClient.getAuthentication("X-AppSecretToken");
    X-AppSecretToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AppSecretToken.setApiKeyPrefix("Token");

    ProjectActivitiesApi apiInstance = new ProjectActivitiesApi(defaultClient);
    String cursor = "cursor_example"; // String | 
    String filter = "filter_example"; // String | 
    try {
      ProjectActivityCursorResults result = apiInstance.getAllProjectActivities(cursor, filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectActivitiesApi#getAllProjectActivities");
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
| **cursor** | **String**|  | [optional] |
| **filter** | **String**|  | [optional] |

### Return type

[**ProjectActivityCursorResults**](ProjectActivityCursorResults.md)

### Authorization

[X-AgreementGrantToken](../README.md#X-AgreementGrantToken), [X-AppSecretToken](../README.md#X-AppSecretToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | **Bad request.** Your request does not pass our validation. See the message for more details. |  -  |
| **401** | **Unauthorized access.** Please take a look at https://apis.e-conomic.com and follow the links to help on authorization, or use the word demo for both tokens. |  -  |
| **403** | **Access forbidden.** You won’t necessarily have access to everything. So even though you were authorized we might still deny access to certain resources. This depends on the roles asked for when the grant was issued. |  -  |
| **429** | **Too many requests.** You have made too many calls towards our API. You are over your quota. Need to wait a bit. Check info in the response headers. |  -  |
| **500** | **Internal server error.** Something went wrong but the error has been logged. If you continue to see errors here, please contact api@e-conomic.com. Remember to include log id and agreement number when contacting support. |  -  |

<a id="getNumberOfProjectActivities"></a>
# **getNumberOfProjectActivities**
> Integer getNumberOfProjectActivities(filter)

Retrieve the number of Project Activities

Call this endpoint to get the number of Project Activities. You can use a filtering as well.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectActivitiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://apis.e-conomic.com/api/v20.0.0");
    
    // Configure API key authorization: X-AgreementGrantToken
    ApiKeyAuth X-AgreementGrantToken = (ApiKeyAuth) defaultClient.getAuthentication("X-AgreementGrantToken");
    X-AgreementGrantToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AgreementGrantToken.setApiKeyPrefix("Token");

    // Configure API key authorization: X-AppSecretToken
    ApiKeyAuth X-AppSecretToken = (ApiKeyAuth) defaultClient.getAuthentication("X-AppSecretToken");
    X-AppSecretToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AppSecretToken.setApiKeyPrefix("Token");

    ProjectActivitiesApi apiInstance = new ProjectActivitiesApi(defaultClient);
    String filter = "filter_example"; // String | 
    try {
      Integer result = apiInstance.getNumberOfProjectActivities(filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectActivitiesApi#getNumberOfProjectActivities");
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
| **filter** | **String**|  | [optional] |

### Return type

**Integer**

### Authorization

[X-AgreementGrantToken](../README.md#X-AgreementGrantToken), [X-AppSecretToken](../README.md#X-AppSecretToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | **Bad request.** Your request does not pass our validation. See the message for more details. |  -  |
| **401** | **Unauthorized access.** Please take a look at https://apis.e-conomic.com and follow the links to help on authorization, or use the word demo for both tokens. |  -  |
| **403** | **Access forbidden.** You won’t necessarily have access to everything. So even though you were authorized we might still deny access to certain resources. This depends on the roles asked for when the grant was issued. |  -  |
| **429** | **Too many requests.** You have made too many calls towards our API. You are over your quota. Need to wait a bit. Check info in the response headers. |  -  |
| **500** | **Internal server error.** Something went wrong but the error has been logged. If you continue to see errors here, please contact api@e-conomic.com. Remember to include log id and agreement number when contacting support. |  -  |

<a id="getPageOfProjectActivities"></a>
# **getPageOfProjectActivities**
> List&lt;ProjectActivity&gt; getPageOfProjectActivities(filter, sort, pageSize, skipPages)

Retrieve a page of Project Activities

Use this endpoint to load a page of Project Activities.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectActivitiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://apis.e-conomic.com/api/v20.0.0");
    
    // Configure API key authorization: X-AgreementGrantToken
    ApiKeyAuth X-AgreementGrantToken = (ApiKeyAuth) defaultClient.getAuthentication("X-AgreementGrantToken");
    X-AgreementGrantToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AgreementGrantToken.setApiKeyPrefix("Token");

    // Configure API key authorization: X-AppSecretToken
    ApiKeyAuth X-AppSecretToken = (ApiKeyAuth) defaultClient.getAuthentication("X-AppSecretToken");
    X-AppSecretToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AppSecretToken.setApiKeyPrefix("Token");

    ProjectActivitiesApi apiInstance = new ProjectActivitiesApi(defaultClient);
    String filter = "filter_example"; // String | 
    String sort = "sort_example"; // String | 
    Integer pageSize = 20; // Integer | 
    Integer skipPages = 0; // Integer | 
    try {
      List<ProjectActivity> result = apiInstance.getPageOfProjectActivities(filter, sort, pageSize, skipPages);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectActivitiesApi#getPageOfProjectActivities");
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
| **filter** | **String**|  | [optional] |
| **sort** | **String**|  | [optional] |
| **pageSize** | **Integer**|  | [optional] [default to 20] |
| **skipPages** | **Integer**|  | [optional] [default to 0] |

### Return type

[**List&lt;ProjectActivity&gt;**](ProjectActivity.md)

### Authorization

[X-AgreementGrantToken](../README.md#X-AgreementGrantToken), [X-AppSecretToken](../README.md#X-AppSecretToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | **Bad request.** Your request does not pass our validation. See the message for more details. |  -  |
| **401** | **Unauthorized access.** Please take a look at https://apis.e-conomic.com and follow the links to help on authorization, or use the word demo for both tokens. |  -  |
| **403** | **Access forbidden.** You won’t necessarily have access to everything. So even though you were authorized we might still deny access to certain resources. This depends on the roles asked for when the grant was issued. |  -  |
| **429** | **Too many requests.** You have made too many calls towards our API. You are over your quota. Need to wait a bit. Check info in the response headers. |  -  |
| **500** | **Internal server error.** Something went wrong but the error has been logged. If you continue to see errors here, please contact api@e-conomic.com. Remember to include log id and agreement number when contacting support. |  -  |

<a id="getProjectActivityById"></a>
# **getProjectActivityById**
> ProjectActivity getProjectActivityById(number)

Retrieve single Project Activity

Use this endpoint to load a single Project Activity by id/number.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectActivitiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://apis.e-conomic.com/api/v20.0.0");
    
    // Configure API key authorization: X-AgreementGrantToken
    ApiKeyAuth X-AgreementGrantToken = (ApiKeyAuth) defaultClient.getAuthentication("X-AgreementGrantToken");
    X-AgreementGrantToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AgreementGrantToken.setApiKeyPrefix("Token");

    // Configure API key authorization: X-AppSecretToken
    ApiKeyAuth X-AppSecretToken = (ApiKeyAuth) defaultClient.getAuthentication("X-AppSecretToken");
    X-AppSecretToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AppSecretToken.setApiKeyPrefix("Token");

    ProjectActivitiesApi apiInstance = new ProjectActivitiesApi(defaultClient);
    Integer number = 56; // Integer | 
    try {
      ProjectActivity result = apiInstance.getProjectActivityById(number);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectActivitiesApi#getProjectActivityById");
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
| **number** | **Integer**|  | |

### Return type

[**ProjectActivity**](ProjectActivity.md)

### Authorization

[X-AgreementGrantToken](../README.md#X-AgreementGrantToken), [X-AppSecretToken](../README.md#X-AppSecretToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | **Bad request.** Your request does not pass our validation. See the message for more details. |  -  |
| **401** | **Unauthorized access.** Please take a look at https://apis.e-conomic.com and follow the links to help on authorization, or use the word demo for both tokens. |  -  |
| **403** | **Access forbidden.** You won’t necessarily have access to everything. So even though you were authorized we might still deny access to certain resources. This depends on the roles asked for when the grant was issued. |  -  |
| **404** | **Resource not found.** The resource you have been looking for does not exist. |  -  |
| **429** | **Too many requests.** You have made too many calls towards our API. You are over your quota. Need to wait a bit. Check info in the response headers. |  -  |
| **500** | **Internal server error.** Something went wrong but the error has been logged. If you continue to see errors here, please contact api@e-conomic.com. Remember to include log id and agreement number when contacting support. |  -  |

<a id="updateProjectActivity"></a>
# **updateProjectActivity**
> updateProjectActivity(projectActivity)

Update a single Project Activity

Use this endpoint to update a single Project Activity.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectActivitiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://apis.e-conomic.com/api/v20.0.0");
    
    // Configure API key authorization: X-AgreementGrantToken
    ApiKeyAuth X-AgreementGrantToken = (ApiKeyAuth) defaultClient.getAuthentication("X-AgreementGrantToken");
    X-AgreementGrantToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AgreementGrantToken.setApiKeyPrefix("Token");

    // Configure API key authorization: X-AppSecretToken
    ApiKeyAuth X-AppSecretToken = (ApiKeyAuth) defaultClient.getAuthentication("X-AppSecretToken");
    X-AppSecretToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-AppSecretToken.setApiKeyPrefix("Token");

    ProjectActivitiesApi apiInstance = new ProjectActivitiesApi(defaultClient);
    ProjectActivity projectActivity = new ProjectActivity(); // ProjectActivity | 
    try {
      apiInstance.updateProjectActivity(projectActivity);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectActivitiesApi#updateProjectActivity");
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
| **projectActivity** | [**ProjectActivity**](ProjectActivity.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

[X-AgreementGrantToken](../README.md#X-AgreementGrantToken), [X-AppSecretToken](../README.md#X-AppSecretToken)

### HTTP request headers

 - **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **400** | **Bad request.** Your request does not pass our validation. See the message for more details. |  -  |
| **401** | **Unauthorized access.** Please take a look at https://apis.e-conomic.com and follow the links to help on authorization, or use the word demo for both tokens. |  -  |
| **403** | **Access forbidden.** You won’t necessarily have access to everything. So even though you were authorized we might still deny access to certain resources. This depends on the roles asked for when the grant was issued. |  -  |
| **404** | **Resource not found.** The resource you have been looking for does not exist. |  -  |
| **409** | **Update conflict. Object version does not match.** The resource has been updated by another user. Retrieve the resource again to get the latest object version and then try to update. |  -  |
| **429** | **Too many requests.** You have made too many calls towards our API. You are over your quota. Need to wait a bit. Check info in the response headers. |  -  |
| **500** | **Internal server error.** Something went wrong but the error has been logged. If you continue to see errors here, please contact api@e-conomic.com. Remember to include log id and agreement number when contacting support. |  -  |

