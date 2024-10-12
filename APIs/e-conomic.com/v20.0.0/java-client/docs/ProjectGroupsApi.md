# ProjectGroupsApi

All URIs are relative to *https://apis.e-conomic.com/api/v20.0.0*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createProjectGroup**](ProjectGroupsApi.md#createProjectGroup) | **POST** /projectgroups | Create a single Project Group |
| [**getAllProjectGroups**](ProjectGroupsApi.md#getAllProjectGroups) | **GET** /projectgroups | Retrieve all Project Groups |
| [**getNumberOfProjectGroups**](ProjectGroupsApi.md#getNumberOfProjectGroups) | **GET** /projectgroups/count | Retrieve the number of Project Groups |
| [**getPageOfProjectGroups**](ProjectGroupsApi.md#getPageOfProjectGroups) | **GET** /projectgroups/paged | Retrieve a page of Project Groups |
| [**getProjectGroupById**](ProjectGroupsApi.md#getProjectGroupById) | **GET** /projectgroups/{number} | Retrieve single Project Group |


<a id="createProjectGroup"></a>
# **createProjectGroup**
> CreatedResult createProjectGroup(projectGroup)

Create a single Project Group

Use this endpoint to create a single Project Group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectGroupsApi;

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

    ProjectGroupsApi apiInstance = new ProjectGroupsApi(defaultClient);
    ProjectGroup projectGroup = new ProjectGroup(); // ProjectGroup | 
    try {
      CreatedResult result = apiInstance.createProjectGroup(projectGroup);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectGroupsApi#createProjectGroup");
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
| **projectGroup** | [**ProjectGroup**](ProjectGroup.md)|  | [optional] |

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

<a id="getAllProjectGroups"></a>
# **getAllProjectGroups**
> ProjectGroupCursorResults getAllProjectGroups(cursor, filter)

Retrieve all Project Groups

Use this endpoint to retrieve all Project Groups in bulk.  Max number of items returned in a single call is 1000. Use the continuation cursor parameter to set the continuation cursor for retrieval of next set of data. [pagination instructions](#section/Retrieving-data/Pagination)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectGroupsApi;

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

    ProjectGroupsApi apiInstance = new ProjectGroupsApi(defaultClient);
    String cursor = "cursor_example"; // String | 
    String filter = "filter_example"; // String | 
    try {
      ProjectGroupCursorResults result = apiInstance.getAllProjectGroups(cursor, filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectGroupsApi#getAllProjectGroups");
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

[**ProjectGroupCursorResults**](ProjectGroupCursorResults.md)

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

<a id="getNumberOfProjectGroups"></a>
# **getNumberOfProjectGroups**
> Integer getNumberOfProjectGroups(filter)

Retrieve the number of Project Groups

Call this endpoint to get the number of Project Groups. You can use a filtering as well.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectGroupsApi;

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

    ProjectGroupsApi apiInstance = new ProjectGroupsApi(defaultClient);
    String filter = "filter_example"; // String | 
    try {
      Integer result = apiInstance.getNumberOfProjectGroups(filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectGroupsApi#getNumberOfProjectGroups");
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

<a id="getPageOfProjectGroups"></a>
# **getPageOfProjectGroups**
> List&lt;ProjectGroup&gt; getPageOfProjectGroups(filter, sort, pageSize, skipPages)

Retrieve a page of Project Groups

Use this endpoint to load a page of Project Groups.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectGroupsApi;

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

    ProjectGroupsApi apiInstance = new ProjectGroupsApi(defaultClient);
    String filter = "filter_example"; // String | 
    String sort = "sort_example"; // String | 
    Integer pageSize = 20; // Integer | 
    Integer skipPages = 0; // Integer | 
    try {
      List<ProjectGroup> result = apiInstance.getPageOfProjectGroups(filter, sort, pageSize, skipPages);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectGroupsApi#getPageOfProjectGroups");
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

[**List&lt;ProjectGroup&gt;**](ProjectGroup.md)

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

<a id="getProjectGroupById"></a>
# **getProjectGroupById**
> ProjectGroup getProjectGroupById(number)

Retrieve single Project Group

Use this endpoint to load a single Project Group by id/number.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectGroupsApi;

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

    ProjectGroupsApi apiInstance = new ProjectGroupsApi(defaultClient);
    Integer number = 56; // Integer | 
    try {
      ProjectGroup result = apiInstance.getProjectGroupById(number);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectGroupsApi#getProjectGroupById");
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

[**ProjectGroup**](ProjectGroup.md)

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

