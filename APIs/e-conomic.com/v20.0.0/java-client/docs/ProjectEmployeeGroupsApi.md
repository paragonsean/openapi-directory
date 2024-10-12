# ProjectEmployeeGroupsApi

All URIs are relative to *https://apis.e-conomic.com/api/v20.0.0*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createProjectEmployeeGroup**](ProjectEmployeeGroupsApi.md#createProjectEmployeeGroup) | **POST** /project-employeegroups | Create a single Project employee group |
| [**deleteProjectEmployeeGroupById**](ProjectEmployeeGroupsApi.md#deleteProjectEmployeeGroupById) | **DELETE** /project-employeegroups/{number} | Delete single Project employee group |
| [**getAllProjectEmployeeGroups**](ProjectEmployeeGroupsApi.md#getAllProjectEmployeeGroups) | **GET** /project-employeegroups | Retrieve all Project employee groups |
| [**getNumberOfProjectEmployeeGroups**](ProjectEmployeeGroupsApi.md#getNumberOfProjectEmployeeGroups) | **GET** /project-employeegroups/count | Retrieve the number of Project employee groups |
| [**getPageOfProjectEmployeeGroups**](ProjectEmployeeGroupsApi.md#getPageOfProjectEmployeeGroups) | **GET** /project-employeegroups/paged | Retrieve a page of Project employee groups |
| [**getProjectEmployeeGroupById**](ProjectEmployeeGroupsApi.md#getProjectEmployeeGroupById) | **GET** /project-employeegroups/{number} | Retrieve single Project employee group |
| [**updateProjectEmployeeGroup**](ProjectEmployeeGroupsApi.md#updateProjectEmployeeGroup) | **PUT** /project-employeegroups | Update a single Project employee group |


<a id="createProjectEmployeeGroup"></a>
# **createProjectEmployeeGroup**
> CreatedResult createProjectEmployeeGroup(projectEmployeeGroup)

Create a single Project employee group

Use this endpoint to create a single Project employee group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectEmployeeGroupsApi;

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

    ProjectEmployeeGroupsApi apiInstance = new ProjectEmployeeGroupsApi(defaultClient);
    ProjectEmployeeGroup projectEmployeeGroup = new ProjectEmployeeGroup(); // ProjectEmployeeGroup | 
    try {
      CreatedResult result = apiInstance.createProjectEmployeeGroup(projectEmployeeGroup);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectEmployeeGroupsApi#createProjectEmployeeGroup");
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
| **projectEmployeeGroup** | [**ProjectEmployeeGroup**](ProjectEmployeeGroup.md)|  | [optional] |

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

<a id="deleteProjectEmployeeGroupById"></a>
# **deleteProjectEmployeeGroupById**
> deleteProjectEmployeeGroupById(number)

Delete single Project employee group

Use this endpoint to delete a single Project employee group by id/number.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectEmployeeGroupsApi;

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

    ProjectEmployeeGroupsApi apiInstance = new ProjectEmployeeGroupsApi(defaultClient);
    Integer number = 56; // Integer | 
    try {
      apiInstance.deleteProjectEmployeeGroupById(number);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectEmployeeGroupsApi#deleteProjectEmployeeGroupById");
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

<a id="getAllProjectEmployeeGroups"></a>
# **getAllProjectEmployeeGroups**
> ProjectEmployeeGroupCursorResults getAllProjectEmployeeGroups(cursor, filter)

Retrieve all Project employee groups

Use this endpoint to retrieve all Project employee groups in bulk.  Max number of items returned in a single call is 1000. Use the continuation cursor parameter to set the continuation cursor for retrieval of next set of data. [pagination instructions](#section/Retrieving-data/Pagination)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectEmployeeGroupsApi;

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

    ProjectEmployeeGroupsApi apiInstance = new ProjectEmployeeGroupsApi(defaultClient);
    String cursor = "cursor_example"; // String | 
    String filter = "filter_example"; // String | 
    try {
      ProjectEmployeeGroupCursorResults result = apiInstance.getAllProjectEmployeeGroups(cursor, filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectEmployeeGroupsApi#getAllProjectEmployeeGroups");
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

[**ProjectEmployeeGroupCursorResults**](ProjectEmployeeGroupCursorResults.md)

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

<a id="getNumberOfProjectEmployeeGroups"></a>
# **getNumberOfProjectEmployeeGroups**
> Integer getNumberOfProjectEmployeeGroups(filter)

Retrieve the number of Project employee groups

Call this endpoint to get the number of Project employee groups. You can use a filtering as well.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectEmployeeGroupsApi;

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

    ProjectEmployeeGroupsApi apiInstance = new ProjectEmployeeGroupsApi(defaultClient);
    String filter = "filter_example"; // String | 
    try {
      Integer result = apiInstance.getNumberOfProjectEmployeeGroups(filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectEmployeeGroupsApi#getNumberOfProjectEmployeeGroups");
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

<a id="getPageOfProjectEmployeeGroups"></a>
# **getPageOfProjectEmployeeGroups**
> List&lt;ProjectEmployeeGroup&gt; getPageOfProjectEmployeeGroups(filter, sort, pageSize, skipPages)

Retrieve a page of Project employee groups

Use this endpoint to load a page of Project employee groups.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectEmployeeGroupsApi;

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

    ProjectEmployeeGroupsApi apiInstance = new ProjectEmployeeGroupsApi(defaultClient);
    String filter = "filter_example"; // String | 
    String sort = "sort_example"; // String | 
    Integer pageSize = 20; // Integer | 
    Integer skipPages = 0; // Integer | 
    try {
      List<ProjectEmployeeGroup> result = apiInstance.getPageOfProjectEmployeeGroups(filter, sort, pageSize, skipPages);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectEmployeeGroupsApi#getPageOfProjectEmployeeGroups");
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

[**List&lt;ProjectEmployeeGroup&gt;**](ProjectEmployeeGroup.md)

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

<a id="getProjectEmployeeGroupById"></a>
# **getProjectEmployeeGroupById**
> ProjectEmployeeGroup getProjectEmployeeGroupById(number)

Retrieve single Project employee group

Use this endpoint to load a single Project employee group by id/number.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectEmployeeGroupsApi;

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

    ProjectEmployeeGroupsApi apiInstance = new ProjectEmployeeGroupsApi(defaultClient);
    Integer number = 56; // Integer | 
    try {
      ProjectEmployeeGroup result = apiInstance.getProjectEmployeeGroupById(number);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectEmployeeGroupsApi#getProjectEmployeeGroupById");
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

[**ProjectEmployeeGroup**](ProjectEmployeeGroup.md)

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

<a id="updateProjectEmployeeGroup"></a>
# **updateProjectEmployeeGroup**
> updateProjectEmployeeGroup(projectEmployeeGroup)

Update a single Project employee group

Use this endpoint to update a single Project employee group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectEmployeeGroupsApi;

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

    ProjectEmployeeGroupsApi apiInstance = new ProjectEmployeeGroupsApi(defaultClient);
    ProjectEmployeeGroup projectEmployeeGroup = new ProjectEmployeeGroup(); // ProjectEmployeeGroup | 
    try {
      apiInstance.updateProjectEmployeeGroup(projectEmployeeGroup);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectEmployeeGroupsApi#updateProjectEmployeeGroup");
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
| **projectEmployeeGroup** | [**ProjectEmployeeGroup**](ProjectEmployeeGroup.md)|  | [optional] |

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

