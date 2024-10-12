# JqlFunctionsAppsApi

All URIs are relative to *https://your-domain.atlassian.net*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getPrecomputations**](JqlFunctionsAppsApi.md#getPrecomputations) | **GET** /rest/api/3/jql/function/computation | Get precomputations (apps) |
| [**updatePrecomputations**](JqlFunctionsAppsApi.md#updatePrecomputations) | **POST** /rest/api/3/jql/function/computation | Update precomputations (apps) |


<a id="getPrecomputations"></a>
# **getPrecomputations**
> PageBeanJqlFunctionPrecomputationBean getPrecomputations(functionKey, startAt, maxResults, orderBy, filter)

Get precomputations (apps)

Returns the list of a function&#39;s precomputations along with information about when they were created, updated, and last used. Each precomputation has a &#x60;value&#x60; \\- the JQL fragment to replace the custom function clause with.  **[Permissions](#permissions) required:** This API is only accessible to apps and apps can only inspect their own functions.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JqlFunctionsAppsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://your-domain.atlassian.net");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    JqlFunctionsAppsApi apiInstance = new JqlFunctionsAppsApi(defaultClient);
    List<String> functionKey = Arrays.asList(); // List<String> | The function key in format:   *  Forge: `ari:cloud:ecosystem::extension/[App ID]/[Environment ID]/static/[Function key from manifest]`.  *  Connect: `[App key]__[Module key]`.
    Long startAt = 0L; // Long | The index of the first item to return in a page of results (page offset).
    Integer maxResults = 100; // Integer | The maximum number of items to return per page.
    String orderBy = "orderBy_example"; // String | Not supported yet.
    String filter = "filter_example"; // String | Not supported yet.
    try {
      PageBeanJqlFunctionPrecomputationBean result = apiInstance.getPrecomputations(functionKey, startAt, maxResults, orderBy, filter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling JqlFunctionsAppsApi#getPrecomputations");
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
| **functionKey** | [**List&lt;String&gt;**](String.md)| The function key in format:   *  Forge: &#x60;ari:cloud:ecosystem::extension/[App ID]/[Environment ID]/static/[Function key from manifest]&#x60;.  *  Connect: &#x60;[App key]__[Module key]&#x60;. | [optional] |
| **startAt** | **Long**| The index of the first item to return in a page of results (page offset). | [optional] [default to 0] |
| **maxResults** | **Integer**| The maximum number of items to return per page. | [optional] [default to 100] |
| **orderBy** | **String**| Not supported yet. | [optional] |
| **filter** | **String**| Not supported yet. | [optional] |

### Return type

[**PageBeanJqlFunctionPrecomputationBean**](PageBeanJqlFunctionPrecomputationBean.md)

### Authorization

[OAuth2](../README.md#OAuth2), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returned if the request is successful. |  -  |
| **400** | Returned if the request is invalid. |  -  |
| **401** | Returned if the authentication credentials are incorrect or missing. |  -  |
| **403** | Returned if the request is not authenticated as the app that provided the function. |  -  |
| **404** | Returned if the function is not found. |  -  |

<a id="updatePrecomputations"></a>
# **updatePrecomputations**
> Object updatePrecomputations(jqlFunctionPrecomputationUpdateRequestBean)

Update precomputations (apps)

Update the precomputation value of a function created by a Forge/Connect app.  **[Permissions](#permissions) required:** An API for apps to update their own precomputations.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JqlFunctionsAppsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://your-domain.atlassian.net");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    JqlFunctionsAppsApi apiInstance = new JqlFunctionsAppsApi(defaultClient);
    JqlFunctionPrecomputationUpdateRequestBean jqlFunctionPrecomputationUpdateRequestBean = new JqlFunctionPrecomputationUpdateRequestBean(); // JqlFunctionPrecomputationUpdateRequestBean | 
    try {
      Object result = apiInstance.updatePrecomputations(jqlFunctionPrecomputationUpdateRequestBean);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling JqlFunctionsAppsApi#updatePrecomputations");
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
| **jqlFunctionPrecomputationUpdateRequestBean** | [**JqlFunctionPrecomputationUpdateRequestBean**](JqlFunctionPrecomputationUpdateRequestBean.md)|  | |

### Return type

**Object**

### Authorization

[OAuth2](../README.md#OAuth2), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Returned if the request is successful. |  -  |
| **400** | Returned if the request is invalid. |  -  |
| **403** | Returned if the request is not authenticated as the app that provided the function. |  -  |
| **404** | Returned if the function is not found. |  -  |

