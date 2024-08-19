# ProjectsApi

All URIs are relative to *https://apis.e-conomic.com/api/v20.0.0*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createProject**](ProjectsApi.md#createProject) | **POST** /projects | Create a single Project |
| [**deleteProjectById**](ProjectsApi.md#deleteProjectById) | **DELETE** /projects/{number} | Delete single Project |
| [**getAllProjects**](ProjectsApi.md#getAllProjects) | **GET** /projects | Retrieve all Projects |
| [**getNumberOfProjects**](ProjectsApi.md#getNumberOfProjects) | **GET** /projects/count | Retrieve the number of Projects |
| [**getPageOfProjects**](ProjectsApi.md#getPageOfProjects) | **GET** /projects/paged | Retrieve a page of Projects |
| [**getPagedListOfProjectUnderEmployee**](ProjectsApi.md#getPagedListOfProjectUnderEmployee) | **GET** /projects/allowed | Retrieve the allowed projects that employee can register an entry on. |
| [**getProjectById**](ProjectsApi.md#getProjectById) | **GET** /projects/{number} | Retrieve single Project |
| [**updateProject**](ProjectsApi.md#updateProject) | **PUT** /projects | Update a single Project |


<a id="createProject"></a>
# **createProject**
> CreatedResult createProject(project)

Create a single Project

Use this endpoint to create a single Project.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

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

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    Project project = new Project(); // Project | 
    try {
      CreatedResult result = apiInstance.createProject(project);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#createProject");
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
| **project** | [**Project**](Project.md)|  | [optional] |

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

<a id="deleteProjectById"></a>
# **deleteProjectById**
> deleteProjectById(number)

Delete single Project

Use this endpoint to delete a single Project by id/number.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

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

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    Integer number = 56; // Integer | 
    try {
      apiInstance.deleteProjectById(number);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#deleteProjectById");
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

<a id="getAllProjects"></a>
# **getAllProjects**
> ProjectCursorResults getAllProjects(cursor, filter)

Retrieve all Projects

Use this endpoint to retrieve all Projects in bulk.  Max number of items returned in a single call is 1000. Use the continuation cursor parameter to set the continuation cursor for retrieval of next set of data. [pagination instructions](#section/Retrieving-data/Pagination)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

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

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String cursor = "cursor_example"; // String | 
    String filter = "filter_example"; // String | 
    try {
      ProjectCursorResults result = apiInstance.getAllProjects(cursor, filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#getAllProjects");
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

[**ProjectCursorResults**](ProjectCursorResults.md)

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

<a id="getNumberOfProjects"></a>
# **getNumberOfProjects**
> Integer getNumberOfProjects(filter)

Retrieve the number of Projects

Call this endpoint to get the number of Projects. You can use a filtering as well.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

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

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String filter = "filter_example"; // String | 
    try {
      Integer result = apiInstance.getNumberOfProjects(filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#getNumberOfProjects");
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

<a id="getPageOfProjects"></a>
# **getPageOfProjects**
> List&lt;Project&gt; getPageOfProjects(filter, sort, pageSize, skipPages)

Retrieve a page of Projects

Use this endpoint to load a page of Projects.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

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

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String filter = "filter_example"; // String | 
    String sort = "sort_example"; // String | 
    Integer pageSize = 20; // Integer | 
    Integer skipPages = 0; // Integer | 
    try {
      List<Project> result = apiInstance.getPageOfProjects(filter, sort, pageSize, skipPages);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#getPageOfProjects");
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

[**List&lt;Project&gt;**](Project.md)

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

<a id="getPagedListOfProjectUnderEmployee"></a>
# **getPagedListOfProjectUnderEmployee**
> List&lt;Project&gt; getPagedListOfProjectUnderEmployee(employeeNumber)

Retrieve the allowed projects that employee can register an entry on.

Use this endpoint to get all the projects that the employee is allowed to register an entry on. Potential restrictions of registration are based on recording rules in the UI, which cannot be modified through the API. Add the employee number to your query parameter to obtain the allowed projects for registrations.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

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

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    Integer employeeNumber = 56; // Integer | The employee number.
    try {
      List<Project> result = apiInstance.getPagedListOfProjectUnderEmployee(employeeNumber);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#getPagedListOfProjectUnderEmployee");
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
| **employeeNumber** | **Integer**| The employee number. | |

### Return type

[**List&lt;Project&gt;**](Project.md)

### Authorization

[X-AgreementGrantToken](../README.md#X-AgreementGrantToken), [X-AppSecretToken](../README.md#X-AppSecretToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | **Bad request.** The data you are sending is not passing our verification logic. Since this can be due to various reasons, you can check the message for the actual reason. |  -  |
| **401** | **Unauthorized access.** Please take a look at https://apis.e-conomic.com and follow the links to help on authorization, or use the word demo for both tokens. |  -  |
| **403** | **Access forbidden.** You won’t necessarily have access to everything. So even though you were authorized we might still deny access to certain resources. This depends on the roles asked for when the grant was issued. |  -  |
| **404** | **Resource not found.** The resource you have been looking for does not exist. |  -  |
| **429** | **Too many requests.** You have made too many calls towards our API. You are over your quota. Need to wait a bit. Check info in the response headers. |  -  |
| **500** | **Internal server error.** Something went wrong but the error has been logged. If you continue to see errors here, please contact api@e-conomic.com. Remember to include log id and agreement number when contacting support. |  -  |

<a id="getProjectById"></a>
# **getProjectById**
> Project getProjectById(number)

Retrieve single Project

Use this endpoint to load a single Project by id/number.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

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

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    Integer number = 56; // Integer | 
    try {
      Project result = apiInstance.getProjectById(number);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#getProjectById");
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

[**Project**](Project.md)

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

<a id="updateProject"></a>
# **updateProject**
> updateProject(project)

Update a single Project

Use this endpoint to update a single Project.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

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

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    Project project = new Project(); // Project | 
    try {
      apiInstance.updateProject(project);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#updateProject");
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
| **project** | [**Project**](Project.md)|  | [optional] |

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

