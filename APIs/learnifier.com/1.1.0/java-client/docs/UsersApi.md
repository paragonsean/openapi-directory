# UsersApi

All URIs are relative to *http://learnifier.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**extparticipationGet**](UsersApi.md#extparticipationGet) | **GET** /extparticipation | Gets a participation by external id |
| [**extuserGet**](UsersApi.md#extuserGet) | **GET** /extuser | Gets a user by external id |
| [**usersGet**](UsersApi.md#usersGet) | **GET** /users | Lists all users |
| [**usersPost**](UsersApi.md#usersPost) | **POST** /users | Adds a user |
| [**usersUseridGet**](UsersApi.md#usersUseridGet) | **GET** /users/{userid} | User information |
| [**usersUseridPatch**](UsersApi.md#usersUseridPatch) | **PATCH** /users/{userid} | Updates user information |
| [**usersUseridPickeyAPIKEYGet**](UsersApi.md#usersUseridPickeyAPIKEYGet) | **GET** /users/{userid}/pic?key&#x3D;{APIKEY} | User profile picture |
| [**usersUseridProjectParticipationsGet**](UsersApi.md#usersUseridProjectParticipationsGet) | **GET** /users/{userid}/projectParticipations | Returns information about the projects the user is a participant in. |


<a id="extparticipationGet"></a>
# **extparticipationGet**
> Participation extparticipationGet(extid)

Gets a participation by external id

Gets a participation by external id.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://learnifier.com");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String extid = "extid_example"; // String | The external id of the participation
    try {
      Participation result = apiInstance.extparticipationGet(extid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#extparticipationGet");
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
| **extid** | **String**| The external id of the participation | |

### Return type

[**Participation**](Participation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The matching participation |  -  |
| **404** | User not found |  -  |
| **0** | Unexpected error |  -  |

<a id="extuserGet"></a>
# **extuserGet**
> User extuserGet(extid)

Gets a user by external id

Gets a user by external id.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://learnifier.com");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String extid = "extid_example"; // String | The external id of the user
    try {
      User result = apiInstance.extuserGet(extid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#extuserGet");
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
| **extid** | **String**| The external id of the user | |

### Return type

[**User**](User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | User was successfully added |  -  |
| **404** | User not found |  -  |
| **0** | Unexpected error |  -  |

<a id="usersGet"></a>
# **usersGet**
> List&lt;UserWithPermissions&gt; usersGet(limit, offset)

Lists all users

Lists all users. Only api callers that have full access can call this method.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://learnifier.com");

    UsersApi apiInstance = new UsersApi(defaultClient);
    Integer limit = 5000; // Integer | The maximum number of users to return
    Integer offset = 0; // Integer | The offset to start listing users from
    try {
      List<UserWithPermissions> result = apiInstance.usersGet(limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#usersGet");
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
| **limit** | **Integer**| The maximum number of users to return | [optional] [default to 5000] |
| **offset** | **Integer**| The offset to start listing users from | [optional] [default to 0] |

### Return type

[**List&lt;UserWithPermissions&gt;**](UserWithPermissions.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List with users |  * X-More - Indicates if there are more users available <br>  * X-Offset - The offset that was used <br>  * X-Limit - The limit that was used <br>  * X-Size - The number of users returned <br>  |
| **0** | Unexpected error |  -  |

<a id="usersPost"></a>
# **usersPost**
> AddUserResponse usersPost(body)

Adds a user

Adds a user. No two users can have the same email address. Email is saved WITH case but compared regardless of case. Email can be changed for a user assuming it doesn&#39;t cause a conflict.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://learnifier.com");

    UsersApi apiInstance = new UsersApi(defaultClient);
    AddUser body = new AddUser(); // AddUser | 
    try {
      AddUserResponse result = apiInstance.usersPost(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#usersPost");
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
| **body** | [**AddUser**](AddUser.md)|  | |

### Return type

[**AddUserResponse**](AddUserResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | User was successfully added |  -  |
| **409** | A user with the same primary email already existed. |  -  |
| **0** | Unexpected error |  -  |

<a id="usersUseridGet"></a>
# **usersUseridGet**
> User usersUseridGet(userid)

User information

Returns information about a user 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://learnifier.com");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String userid = "userid_example"; // String | A user id
    try {
      User result = apiInstance.usersUseridGet(userid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#usersUseridGet");
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
| **userid** | **String**| A user id | |

### Return type

[**User**](User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | User information |  -  |
| **0** | Unexpected error |  -  |

<a id="usersUseridPatch"></a>
# **usersUseridPatch**
> usersUseridPatch(userid, body)

Updates user information

Updates a user. All values that have a key defined in the input will be set. So if a value should not be updated omit it totally from the input, otherwise it will be unset.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://learnifier.com");

    UsersApi apiInstance = new UsersApi(defaultClient);
    UUID userid = UUID.randomUUID(); // UUID | The user id
    AddUser body = new AddUser(); // AddUser | 
    try {
      apiInstance.usersUseridPatch(userid, body);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#usersUseridPatch");
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
| **userid** | **UUID**| The user id | |
| **body** | [**AddUser**](AddUser.md)|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | User was successfully updated |  -  |
| **409** | A user with the same primary email already existed. |  -  |
| **0** | Unexpected error |  -  |

<a id="usersUseridPickeyAPIKEYGet"></a>
# **usersUseridPickeyAPIKEYGet**
> usersUseridPickeyAPIKEYGet(userid, APIKEY)

User profile picture

Returns a thumbnail picture of the user. This can either be a selected picture or an auto generated image. This method doesn&#39;t require a full sign in. The api key is sufficient. The image is square and is likely, but not necessary, to be in 128x128 PNG format. However the format will always be either PNG, JPEG or GIF. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://learnifier.com");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String userid = "userid_example"; // String | The user id
    String APIKEY = "APIKEY_example"; // String | 
    try {
      apiInstance.usersUseridPickeyAPIKEYGet(userid, APIKEY);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#usersUseridPickeyAPIKEYGet");
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
| **userid** | **String**| The user id | |
| **APIKEY** | **String**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | An image. Check the Content-Type header to determine which type the returned image have |  -  |
| **302** | A redirect to the profile |  -  |
| **0** | Unexpected error |  -  |

<a id="usersUseridProjectParticipationsGet"></a>
# **usersUseridProjectParticipationsGet**
> UserParticipationInfo usersUseridProjectParticipationsGet(userid)

Returns information about the projects the user is a participant in.

Returns information about the projects the user is a participant in. Only the projects that the current token have access to will be listed. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://learnifier.com");

    UsersApi apiInstance = new UsersApi(defaultClient);
    UUID userid = UUID.randomUUID(); // UUID | A user id
    try {
      UserParticipationInfo result = apiInstance.usersUseridProjectParticipationsGet(userid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#usersUseridProjectParticipationsGet");
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
| **userid** | **UUID**| A user id | |

### Return type

[**UserParticipationInfo**](UserParticipationInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Project participation info |  -  |
| **0** | Unexpected error |  -  |

