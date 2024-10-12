# UserApi

All URIs are relative to *https://phantauth.net*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**userPost**](UserApi.md#userPost) | **POST** /user | Create a User Selfie |
| [**userUsernameGet**](UserApi.md#userUsernameGet) | **GET** /user/{username} | Get a User |
| [**userUsernameTokenKindGet**](UserApi.md#userUsernameTokenKindGet) | **GET** /user/{username}/token/{kind} | Get a User Token |


<a id="userPost"></a>
# **userPost**
> userPost(userPostRequest)

Create a User Selfie

To create a selfie token from the user data, you need an opaqe string token, which contains the encoded user properties sent in the request. Later, the selfie token can be used as a login name. In this case, the user data is included in the selfie token, that is, the user properties are taken from the token. By the use of a selfie token, you can use your own user objects during the authentication process.  Its use, however, is limited by its relatively large size (more than 100 characters), which exceeds the maximum size of the user name in several systems.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://phantauth.net");

    UserApi apiInstance = new UserApi(defaultClient);
    UserPostRequest userPostRequest = new UserPostRequest(); // UserPostRequest | 
    try {
      apiInstance.userPost(userPostRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserApi#userPost");
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
| **userPostRequest** | [**UserPostRequest**](UserPostRequest.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="userUsernameGet"></a>
# **userUsernameGet**
> UserUsernameGet200Response userUsernameGet(username)

Get a User

Use this endpoint to generate a random user. The user is generated in a deterministic way, on the bases of the user name given as a path parameter. In the case of identical user names, the endpoint will generate the same user object. The properties of the generated user object are randomly generated on the basis of the user name. In lack of a user name, all calls generate a different user object to the randomly generated user name.  By providing an email address as the &#x60;username&#x60; parameter, you can customize the user picture by the use of the gravatar associated with the email address.  If the &#x60;username&#x60; parameter contains at least one dot (&#x60;.&#x60;) or space (&#x60; &#x60;) character, the whole name is produced from the parameter, rather than being generated. In this case, these cahracters play the role of separator between the units of the full name (family name, given name).&#x60;  The result is always a user object. If you want to generate multiple users in one single step, you can do it by the use of *Team* generation. The members of a team are users randomly generated from the team name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://phantauth.net");

    UserApi apiInstance = new UserApi(defaultClient);
    String username = "username_example"; // String | The username or email used for generation purposes.
    try {
      UserUsernameGet200Response result = apiInstance.userUsernameGet(username);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserApi#userUsernameGet");
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
| **username** | **String**| The username or email used for generation purposes. | |

### Return type

[**UserUsernameGet200Response**](UserUsernameGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="userUsernameTokenKindGet"></a>
# **userUsernameTokenKindGet**
> userUsernameTokenKindGet(username, kind, scope)

Get a User Token

It is used to generate OpenID Connect tokens as path parameters to a user of a given name.  This method is mainly used in the testing process, when, for example, the token received from the normal authenticaton flow is not available to the test code. Generating an access token, for example, will let you avoid authentication, and immediately call an operation requiring the access token.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://phantauth.net");

    UserApi apiInstance = new UserApi(defaultClient);
    String username = "username_example"; // String | A username or email.
    String kind = "'access'"; // String | Token type
    String scope = "scope_example"; // String | OpenID Connect scope
    try {
      apiInstance.userUsernameTokenKindGet(username, kind, scope);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserApi#userUsernameTokenKindGet");
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
| **username** | **String**| A username or email. | |
| **kind** | **String**| Token type | [enum: 'access', 'refresh', 'authorization', 'id', 'selfie', 'plain'] |
| **scope** | **String**| OpenID Connect scope | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

