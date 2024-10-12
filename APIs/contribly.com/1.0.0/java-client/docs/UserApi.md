# UserApi

All URIs are relative to *https://api.contribly.com/1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**usersGet**](UserApi.md#usersGet) | **GET** /users | List users |
| [**usersIdGet**](UserApi.md#usersIdGet) | **GET** /users/{id} | Retrieve a single user by id |
| [**usersIdLinkedTypeGet**](UserApi.md#usersIdLinkedTypeGet) | **GET** /users/{id}/linked/{type} | Retrieve a users linked profile by type |


<a id="usersGet"></a>
# **usersGet**
> List&lt;User&gt; usersGet(assignment, country, minimumContributions, linkedProfile, ownedBy, submittedBefore, submittedAfter, username)

List users

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
    defaultClient.setBasePath("https://api.contribly.com/1");

    UserApi apiInstance = new UserApi(defaultClient);
    String assignment = "assignment_example"; // String | Restrict results to the users who have contributed to this assignment.
    String country = "country_example"; // String | Restrict results to the users who have submitted a contribution with a public location located within this country.
    BigDecimal minimumContributions = new BigDecimal(78); // BigDecimal | Restrict results to the users who have submitted at least this many contributions.
    String linkedProfile = "linkedProfile_example"; // String | Restrict results to the users who a linked profile of this type.
    String ownedBy = "ownedBy_example"; // String | Restrict results to the users who are owned by of this owner.
    OffsetDateTime submittedBefore = OffsetDateTime.now(); // OffsetDateTime | Limit results to users who have submitted at least one contribution before this date time.
    OffsetDateTime submittedAfter = OffsetDateTime.now(); // OffsetDateTime | Limit results to users who have submitted at least one contribution after this date time.
    String username = "username_example"; // String | Restrict results to the user with this username.
    try {
      List<User> result = apiInstance.usersGet(assignment, country, minimumContributions, linkedProfile, ownedBy, submittedBefore, submittedAfter, username);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserApi#usersGet");
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
| **assignment** | **String**| Restrict results to the users who have contributed to this assignment. | [optional] |
| **country** | **String**| Restrict results to the users who have submitted a contribution with a public location located within this country. | [optional] |
| **minimumContributions** | **BigDecimal**| Restrict results to the users who have submitted at least this many contributions. | [optional] |
| **linkedProfile** | **String**| Restrict results to the users who a linked profile of this type. | [optional] |
| **ownedBy** | **String**| Restrict results to the users who are owned by of this owner. | [optional] |
| **submittedBefore** | **OffsetDateTime**| Limit results to users who have submitted at least one contribution before this date time. | [optional] |
| **submittedAfter** | **OffsetDateTime**| Limit results to users who have submitted at least one contribution after this date time. | [optional] |
| **username** | **String**| Restrict results to the user with this username. | [optional] |

### Return type

[**List&lt;User&gt;**](User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of users |  * X-total-count - Total number of matching users <br>  |

<a id="usersIdGet"></a>
# **usersIdGet**
> User usersIdGet(id)

Retrieve a single user by id

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
    defaultClient.setBasePath("https://api.contribly.com/1");

    UserApi apiInstance = new UserApi(defaultClient);
    String id = "id_example"; // String | Id of the user to return
    try {
      User result = apiInstance.usersIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserApi#usersIdGet");
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
| **id** | **String**| Id of the user to return | |

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
| **200** | Successful |  -  |
| **404** | Not found |  -  |

<a id="usersIdLinkedTypeGet"></a>
# **usersIdLinkedTypeGet**
> LinkedProfile usersIdLinkedTypeGet(id, type)

Retrieve a users linked profile by type

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
    defaultClient.setBasePath("https://api.contribly.com/1");

    UserApi apiInstance = new UserApi(defaultClient);
    String id = "id_example"; // String | Id of the user to return
    String type = "type_example"; // String | Type of the linked profile to fetch
    try {
      LinkedProfile result = apiInstance.usersIdLinkedTypeGet(id, type);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserApi#usersIdLinkedTypeGet");
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
| **id** | **String**| Id of the user to return | |
| **type** | **String**| Type of the linked profile to fetch | |

### Return type

[**LinkedProfile**](LinkedProfile.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful |  -  |
| **404** | Not found |  -  |

