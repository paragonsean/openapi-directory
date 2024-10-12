# RolesApi

All URIs are relative to *https://vtex.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getListRoles**](RolesApi.md#getListRoles) | **GET** /api/license-manager/site/pvt/roles/list/paged | Get List of Roles |
| [**getRolesbyUser**](RolesApi.md#getRolesbyUser) | **GET** /api/license-manager/users/{userId}/roles | Get Roles by User/appKey |
| [**putRolesinUser**](RolesApi.md#putRolesinUser) | **PUT** /api/license-manager/users/{userId}/roles | Put Roles in User/appKey |
| [**removeRolefromUser**](RolesApi.md#removeRolefromUser) | **DELETE** /api/license-manager/users/{userId}/roles/{roleId} | Remove Role from User/appKey |


<a id="getListRoles"></a>
# **getListRoles**
> ListRolesResponse getListRoles(contentType, numItems, pageNumber, sort, sortType)

Get List of Roles

Returns a list of available roles. The response is divided in pages. The query parameter &#x60;numItems&#x60; defines the number of items in each page, and consequently the amount of pages for the whole list.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RolesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    RolesApi apiInstance = new RolesApi(defaultClient);
    String contentType = "application/json"; // String | The media type of the body of the request. Default value for license manager protocol is application/json
    Integer numItems = 10; // Integer | Number of items in the returned page
    Integer pageNumber = 1; // Integer | Which page from the whole list will be returned
    String sort = "id"; // String | Chooses the field that the list will be sorted by
    String sortType = "ASC"; // String | Defines the sorting order. ASC is used for ascendant order. DSC is used for descendant order
    try {
      ListRolesResponse result = apiInstance.getListRoles(contentType, numItems, pageNumber, sort, sortType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RolesApi#getListRoles");
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
| **contentType** | **String**| The media type of the body of the request. Default value for license manager protocol is application/json | [default to application/json] |
| **numItems** | **Integer**| Number of items in the returned page | [optional] [default to 10] |
| **pageNumber** | **Integer**| Which page from the whole list will be returned | [optional] [default to 1] |
| **sort** | **String**| Chooses the field that the list will be sorted by | [optional] [default to id] |
| **sortType** | **String**| Defines the sorting order. ASC is used for ascendant order. DSC is used for descendant order | [optional] [default to ASC] |

### Return type

[**ListRolesResponse**](ListRolesResponse.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="getRolesbyUser"></a>
# **getRolesbyUser**
> List&lt;GetRolesbyUser200ResponseInner&gt; getRolesbyUser(contentType, userId)

Get Roles by User/appKey

Gets roles of a particular user or application key.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RolesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    RolesApi apiInstance = new RolesApi(defaultClient);
    String contentType = "application/json"; // String | The media type of the body of the request. Default value for license manager protocol is application/json
    String userId = "userId_example"; // String | ID corresponding to the user
    try {
      List<GetRolesbyUser200ResponseInner> result = apiInstance.getRolesbyUser(contentType, userId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RolesApi#getRolesbyUser");
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
| **contentType** | **String**| The media type of the body of the request. Default value for license manager protocol is application/json | |
| **userId** | **String**| ID corresponding to the user | |

### Return type

[**List&lt;GetRolesbyUser200ResponseInner&gt;**](GetRolesbyUser200ResponseInner.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="putRolesinUser"></a>
# **putRolesinUser**
> putRolesinUser(userId, requestBody)

Put Roles in User/appKey

Allows you to add roles to a particular user or application key by specifying the list of roles&#39; IDs on the request&#39;s body.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RolesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    RolesApi apiInstance = new RolesApi(defaultClient);
    String userId = "userId_example"; // String | ID corresponding to the user
    List<Integer> requestBody = [9000,9111,9333,9444]; // List<Integer> | List of roles' IDs to add to the user or application key.
    try {
      apiInstance.putRolesinUser(userId, requestBody);
    } catch (ApiException e) {
      System.err.println("Exception when calling RolesApi#putRolesinUser");
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
| **userId** | **String**| ID corresponding to the user | |
| **requestBody** | [**List&lt;Integer&gt;**](Integer.md)| List of roles&#39; IDs to add to the user or application key. | |

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success - A no-content response, but the roles were added successfully. |  -  |
| **400** | Bad Request - A userId or role list with invalid format. The message on the body of the response will contain further information. |  -  |
| **500** | Unexpected error - One possible reason is that the userId is not present on the database. |  -  |

<a id="removeRolefromUser"></a>
# **removeRolefromUser**
> removeRolefromUser(contentType, userId, roleId)

Remove Role from User/appKey

Allows you to remove a role from a specific user or application key. This method only allows the removal of one role per request. The role&#39;s ID must be specified on the request path, not on the request body.    &gt; Note that a successful response returns a &#x60;204&#x60; response with an empty body. A deletion on a role or user that does not exist will also return a &#x60;204&#x60;. Thus, this method should not be used to verify the existence of a specific user or role.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RolesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    RolesApi apiInstance = new RolesApi(defaultClient);
    String contentType = "application/json"; // String | The media type of the body of the request. Default value for license manager protocol is application/json
    String userId = "userId_example"; // String | ID corresponding to the user
    String roleId = "roleId_example"; // String | ID of the role which will be removed from the user
    try {
      apiInstance.removeRolefromUser(contentType, userId, roleId);
    } catch (ApiException e) {
      System.err.println("Exception when calling RolesApi#removeRolefromUser");
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
| **contentType** | **String**| The media type of the body of the request. Default value for license manager protocol is application/json | |
| **userId** | **String**| ID corresponding to the user | |
| **roleId** | **String**| ID of the role which will be removed from the user | |

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success - A no-content response, but the role deletion was performed successfully. |  -  |
| **400** | Bad Request - A userId or role list with invalid format. The message on the body of the response will contain further information. |  -  |
| **405** | Method Not Allowed |  -  |

