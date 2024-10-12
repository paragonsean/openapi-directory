# UserApi

All URIs are relative to *https://vtex.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createUser**](UserApi.md#createUser) | **POST** /api/license-manager/users | Create User |
| [**getListUsers**](UserApi.md#getListUsers) | **GET** /api/license-manager/site/pvt/logins/list/paged | Get List of Users |
| [**getUser**](UserApi.md#getUser) | **GET** /api/license-manager/users/{userId} | Get User |


<a id="createUser"></a>
# **createUser**
> CreateUser200Response createUser(createUserRequest)

Create User

Allows you to create a user by providing an email (mandatory) and name (optional). The email must be in a valid format. The success response will contain the generated &#x60;userId&#x60; for that user.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserApi;

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

    UserApi apiInstance = new UserApi(defaultClient);
    CreateUserRequest createUserRequest = new CreateUserRequest(); // CreateUserRequest | 
    try {
      CreateUser200Response result = apiInstance.createUser(createUserRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserApi#createUser");
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
| **createUserRequest** | [**CreateUserRequest**](CreateUserRequest.md)|  | |

### Return type

[**CreateUser200Response**](CreateUser200Response.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |

<a id="getListUsers"></a>
# **getListUsers**
> ListUsersResponse getListUsers(contentType, numItems, pageNumber, sort, sortType)

Get List of Users

Returns a list of registered users. The response is divided in pages. The query parameter &#x60;numItems&#x60; defines the number of items in each page, and consequently the amount of pages for the whole list.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserApi;

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

    UserApi apiInstance = new UserApi(defaultClient);
    String contentType = "application/json"; // String | The media type of the body of the request. Default value for license manager protocol is application/json
    Integer numItems = 10; // Integer | Number of items in the returned page
    Integer pageNumber = 1; // Integer | Which page from the whole list will be returned
    String sort = "name"; // String | Chooses the field that the list will be sorted by
    String sortType = "ASC"; // String | Defines the sorting order. `ASC` is used for ascendant order. `DSC` is used for descendant order
    try {
      ListUsersResponse result = apiInstance.getListUsers(contentType, numItems, pageNumber, sort, sortType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserApi#getListUsers");
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
| **sort** | **String**| Chooses the field that the list will be sorted by | [optional] [default to name] |
| **sortType** | **String**| Defines the sorting order. &#x60;ASC&#x60; is used for ascendant order. &#x60;DSC&#x60; is used for descendant order | [optional] [default to ASC] |

### Return type

[**ListUsersResponse**](ListUsersResponse.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="getUser"></a>
# **getUser**
> CreateUser200Response getUser(contentType, userId)

Get User

Allows you to get a user from the database, using the &#x60;userId&#x60; as the identifier.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserApi;

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

    UserApi apiInstance = new UserApi(defaultClient);
    String contentType = "application/json"; // String | The media type of the body of the request. Default value for license manager protocol is application/json
    String userId = "userId_example"; // String | ID from queried user.
    try {
      CreateUser200Response result = apiInstance.getUser(contentType, userId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserApi#getUser");
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
| **userId** | **String**| ID from queried user. | |

### Return type

[**CreateUser200Response**](CreateUser200Response.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |
| **405** | Method Not Allowed - A null &#x60;userId&#x60; sends the request to a path that is not allowed. |  -  |

