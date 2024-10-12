# ProjectBriefsApi

All URIs are relative to *https://app.asana.com/api/1.0*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createProjectBrief**](ProjectBriefsApi.md#createProjectBrief) | **POST** /projects/{project_gid}/project_briefs | Create a project brief |
| [**deleteProjectBrief**](ProjectBriefsApi.md#deleteProjectBrief) | **DELETE** /project_briefs/{project_brief_gid} | Delete a project brief |
| [**getProjectBrief**](ProjectBriefsApi.md#getProjectBrief) | **GET** /project_briefs/{project_brief_gid} | Get a project brief |
| [**updateProjectBrief**](ProjectBriefsApi.md#updateProjectBrief) | **PUT** /project_briefs/{project_brief_gid} | Update a project brief |


<a id="createProjectBrief"></a>
# **createProjectBrief**
> GetProjectBrief200Response createProjectBrief(projectGid, updateProjectBriefRequest, optPretty, optFields)

Create a project brief

Creates a new project brief.  Returns the full record of the newly created project brief.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectBriefsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.asana.com/api/1.0");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ProjectBriefsApi apiInstance = new ProjectBriefsApi(defaultClient);
    String projectGid = "1331"; // String | Globally unique identifier for the project.
    UpdateProjectBriefRequest updateProjectBriefRequest = new UpdateProjectBriefRequest(); // UpdateProjectBriefRequest | The project brief to create.
    Boolean optPretty = true; // Boolean | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
    List<String> optFields = Arrays.asList(); // List<String> | Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options.
    try {
      GetProjectBrief200Response result = apiInstance.createProjectBrief(projectGid, updateProjectBriefRequest, optPretty, optFields);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectBriefsApi#createProjectBrief");
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
| **projectGid** | **String**| Globally unique identifier for the project. | |
| **updateProjectBriefRequest** | [**UpdateProjectBriefRequest**](UpdateProjectBriefRequest.md)| The project brief to create. | |
| **optPretty** | **Boolean**| Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. | [optional] |
| **optFields** | [**List&lt;String&gt;**](String.md)| Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options. | [optional] |

### Return type

[**GetProjectBrief200Response**](GetProjectBrief200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Successfully created a new project brief. |  -  |
| **400** | This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again. |  -  |
| **401** | A valid authentication token was not provided with the request, so the API could not associate a user with the request. |  -  |
| **402** | The request was valid, but the queried object or object mutation specified in the request is above your current premium level. |  -  |
| **403** | The authentication and request syntax was valid but the server is refusing to complete the request. This can happen if you try to read or write to objects or properties that the user does not have access to. |  -  |
| **404** | Either the request method and path supplied do not specify a known action in the API, or the object specified by the request does not exist. |  -  |
| **500** | There was a problem on Asana’s end. In the event of a server error the response body should contain an error phrase. These phrases can be used by Asana support to quickly look up the incident that caused the server error. Some errors are due to server load, and will not supply an error phrase. |  -  |

<a id="deleteProjectBrief"></a>
# **deleteProjectBrief**
> DeleteAttachment200Response deleteProjectBrief(projectBriefGid, optPretty, optFields)

Delete a project brief

Deletes a specific, existing project brief.  Returns an empty data record.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectBriefsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.asana.com/api/1.0");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ProjectBriefsApi apiInstance = new ProjectBriefsApi(defaultClient);
    String projectBriefGid = "12345"; // String | Globally unique identifier for the project brief.
    Boolean optPretty = true; // Boolean | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
    List<String> optFields = Arrays.asList(); // List<String> | Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options.
    try {
      DeleteAttachment200Response result = apiInstance.deleteProjectBrief(projectBriefGid, optPretty, optFields);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectBriefsApi#deleteProjectBrief");
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
| **projectBriefGid** | **String**| Globally unique identifier for the project brief. | |
| **optPretty** | **Boolean**| Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. | [optional] |
| **optFields** | [**List&lt;String&gt;**](String.md)| Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options. | [optional] |

### Return type

[**DeleteAttachment200Response**](DeleteAttachment200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully deleted the specified project brief. |  -  |
| **400** | This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again. |  -  |
| **401** | A valid authentication token was not provided with the request, so the API could not associate a user with the request. |  -  |
| **403** | The authentication and request syntax was valid but the server is refusing to complete the request. This can happen if you try to read or write to objects or properties that the user does not have access to. |  -  |
| **404** | Either the request method and path supplied do not specify a known action in the API, or the object specified by the request does not exist. |  -  |
| **500** | There was a problem on Asana’s end. In the event of a server error the response body should contain an error phrase. These phrases can be used by Asana support to quickly look up the incident that caused the server error. Some errors are due to server load, and will not supply an error phrase. |  -  |

<a id="getProjectBrief"></a>
# **getProjectBrief**
> GetProjectBrief200Response getProjectBrief(projectBriefGid, optPretty, optFields)

Get a project brief

Get the full record for a project brief.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectBriefsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.asana.com/api/1.0");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ProjectBriefsApi apiInstance = new ProjectBriefsApi(defaultClient);
    String projectBriefGid = "12345"; // String | Globally unique identifier for the project brief.
    Boolean optPretty = true; // Boolean | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
    List<String> optFields = Arrays.asList(); // List<String> | Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options.
    try {
      GetProjectBrief200Response result = apiInstance.getProjectBrief(projectBriefGid, optPretty, optFields);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectBriefsApi#getProjectBrief");
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
| **projectBriefGid** | **String**| Globally unique identifier for the project brief. | |
| **optPretty** | **Boolean**| Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. | [optional] |
| **optFields** | [**List&lt;String&gt;**](String.md)| Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options. | [optional] |

### Return type

[**GetProjectBrief200Response**](GetProjectBrief200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully retrieved the record for a project brief. |  -  |
| **400** | This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again. |  -  |
| **401** | A valid authentication token was not provided with the request, so the API could not associate a user with the request. |  -  |
| **402** | The request was valid, but the queried object or object mutation specified in the request is above your current premium level. |  -  |
| **403** | The authentication and request syntax was valid but the server is refusing to complete the request. This can happen if you try to read or write to objects or properties that the user does not have access to. |  -  |
| **404** | Either the request method and path supplied do not specify a known action in the API, or the object specified by the request does not exist. |  -  |
| **424** | You have exceeded one of the enforced rate limits in the API. See the [documentation on rate limiting](https://developers.asana.com/docs/#rate-limits) for more information. |  -  |
| **500** | There was a problem on Asana’s end. In the event of a server error the response body should contain an error phrase. These phrases can be used by Asana support to quickly look up the incident that caused the server error. Some errors are due to server load, and will not supply an error phrase. |  -  |
| **501** | There is an issue between the load balancers and Asana&#39;s API. |  -  |
| **503** | Either the upstream service is unavailable to the API, or the API has been intentionally shut off. |  -  |
| **504** | This request took too long to complete. |  -  |

<a id="updateProjectBrief"></a>
# **updateProjectBrief**
> GetProjectBrief200Response updateProjectBrief(projectBriefGid, updateProjectBriefRequest, optPretty, optFields)

Update a project brief

An existing project brief can be updated by making a PUT request on the URL for that project brief. Only the fields provided in the &#x60;data&#x60; block will be updated; any unspecified fields will remain unchanged.  Returns the complete updated project brief record.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectBriefsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.asana.com/api/1.0");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ProjectBriefsApi apiInstance = new ProjectBriefsApi(defaultClient);
    String projectBriefGid = "12345"; // String | Globally unique identifier for the project brief.
    UpdateProjectBriefRequest updateProjectBriefRequest = new UpdateProjectBriefRequest(); // UpdateProjectBriefRequest | The updated fields for the project brief.
    Boolean optPretty = true; // Boolean | Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
    List<String> optFields = Arrays.asList(); // List<String> | Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options.
    try {
      GetProjectBrief200Response result = apiInstance.updateProjectBrief(projectBriefGid, updateProjectBriefRequest, optPretty, optFields);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectBriefsApi#updateProjectBrief");
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
| **projectBriefGid** | **String**| Globally unique identifier for the project brief. | |
| **updateProjectBriefRequest** | [**UpdateProjectBriefRequest**](UpdateProjectBriefRequest.md)| The updated fields for the project brief. | |
| **optPretty** | **Boolean**| Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging. | [optional] |
| **optFields** | [**List&lt;String&gt;**](String.md)| Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options. | [optional] |

### Return type

[**GetProjectBrief200Response**](GetProjectBrief200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully updated the project brief. |  -  |
| **400** | This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again. |  -  |
| **401** | A valid authentication token was not provided with the request, so the API could not associate a user with the request. |  -  |
| **403** | The authentication and request syntax was valid but the server is refusing to complete the request. This can happen if you try to read or write to objects or properties that the user does not have access to. |  -  |
| **404** | Either the request method and path supplied do not specify a known action in the API, or the object specified by the request does not exist. |  -  |
| **500** | There was a problem on Asana’s end. In the event of a server error the response body should contain an error phrase. These phrases can be used by Asana support to quickly look up the incident that caused the server error. Some errors are due to server load, and will not supply an error phrase. |  -  |

