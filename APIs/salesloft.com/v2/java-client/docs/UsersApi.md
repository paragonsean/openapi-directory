# UsersApi

All URIs are relative to *https://api.salesloft.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**v2UsersIdJsonGet**](UsersApi.md#v2UsersIdJsonGet) | **GET** /v2/users/{id}.json | Fetch a user |
| [**v2UsersIdJsonPut**](UsersApi.md#v2UsersIdJsonPut) | **PUT** /v2/users/{id}.json | Update a user |
| [**v2UsersJsonGet**](UsersApi.md#v2UsersJsonGet) | **GET** /v2/users.json | List users |


<a id="v2UsersIdJsonGet"></a>
# **v2UsersIdJsonGet**
> User v2UsersIdJsonGet(id)

Fetch a user

Fetches a user, by ID only. 

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
    defaultClient.setBasePath("https://api.salesloft.com");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String id = "id_example"; // String | User ID
    try {
      User result = apiInstance.v2UsersIdJsonGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#v2UsersIdJsonGet");
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
| **id** | **String**| User ID | |

### Return type

[**User**](User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="v2UsersIdJsonPut"></a>
# **v2UsersIdJsonPut**
> User v2UsersIdJsonPut(id, active, groupId, roleId, workCountry)

Update a user

Updates a user. 

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
    defaultClient.setBasePath("https://api.salesloft.com");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String id = "id_example"; // String | User ID
    Boolean active = true; // Boolean | Active status of the user's account
    Integer groupId = 56; // Integer | Group assigned to the user
    String roleId = "roleId_example"; // String | Role assigned to the user. Must be one of: Admin, User, or a custom role ID
    String workCountry = "workCountry_example"; // String | The user's work country (alpha-2 code)
    try {
      User result = apiInstance.v2UsersIdJsonPut(id, active, groupId, roleId, workCountry);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#v2UsersIdJsonPut");
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
| **id** | **String**| User ID | |
| **active** | **Boolean**| Active status of the user&#39;s account | [optional] |
| **groupId** | **Integer**| Group assigned to the user | [optional] |
| **roleId** | **String**| Role assigned to the user. Must be one of: Admin, User, or a custom role ID | [optional] |
| **workCountry** | **String**| The user&#39;s work country (alpha-2 code) | [optional] |

### Return type

[**User**](User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="v2UsersJsonGet"></a>
# **v2UsersJsonGet**
> List&lt;User&gt; v2UsersJsonGet(ids, guid, groupId, roleId, search, active, visibleOnly, perPage, page, includePagingCounts, hasCrmUser, workCountry, sortBy, sortDirection)

List users

Non Admin: Lists only your user, or all on team depending on group visibility policy Team Admin: Lists users associated with your team 

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
    defaultClient.setBasePath("https://api.salesloft.com");

    UsersApi apiInstance = new UsersApi(defaultClient);
    List<Integer> ids = Arrays.asList(); // List<Integer> | IDs of users to fetch. If a record can't be found, that record won't be returned and your request will be successful
    List<String> guid = Arrays.asList(); // List<String> | Filters list to only include guids
    List<String> groupId = Arrays.asList(); // List<String> | Filters users by group_id.  An additional value of \"_is_null\" can be passed to filter users that are not in a group
    List<String> roleId = Arrays.asList(); // List<String> | Filters users by role_id
    String search = "search_example"; // String | Space-separated list of keywords used to find case-insensitive substring matches against First Name, Last Name, or Email
    Boolean active = true; // Boolean | Filters users based on active attribute. Defaults to not applied
    Boolean visibleOnly = true; // Boolean | Defaults to true.  When true, only shows users that are actionable based on the team's privacy settings. When false, shows all users on the team, even if you can't take action on that user. Deactivated users are also included when false. 
    Integer perPage = 56; // Integer | How many users to show per page in the range [1, 100]. Defaults to 25.  Results are only paginated if the page parameter is defined
    Integer page = 56; // Integer | The current page to fetch users from. Defaults to returning all users
    Boolean includePagingCounts = true; // Boolean | Whether to include total_pages and total_count in the metadata. Defaults to false
    Boolean hasCrmUser = true; // Boolean | Filters users based on if they have a crm user mapped or not.
    List<String> workCountry = Arrays.asList(); // List<String> | Filters users based on assigned work_country.
    String sortBy = "sortBy_example"; // String | Key to sort on, must be one of: id, email, name, group, role. Defaults to id
    String sortDirection = "sortDirection_example"; // String | Direction to sort in, must be one of: ASC, DESC. Defaults to DESC
    try {
      List<User> result = apiInstance.v2UsersJsonGet(ids, guid, groupId, roleId, search, active, visibleOnly, perPage, page, includePagingCounts, hasCrmUser, workCountry, sortBy, sortDirection);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#v2UsersJsonGet");
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
| **ids** | [**List&lt;Integer&gt;**](Integer.md)| IDs of users to fetch. If a record can&#39;t be found, that record won&#39;t be returned and your request will be successful | [optional] |
| **guid** | [**List&lt;String&gt;**](String.md)| Filters list to only include guids | [optional] |
| **groupId** | [**List&lt;String&gt;**](String.md)| Filters users by group_id.  An additional value of \&quot;_is_null\&quot; can be passed to filter users that are not in a group | [optional] |
| **roleId** | [**List&lt;String&gt;**](String.md)| Filters users by role_id | [optional] |
| **search** | **String**| Space-separated list of keywords used to find case-insensitive substring matches against First Name, Last Name, or Email | [optional] |
| **active** | **Boolean**| Filters users based on active attribute. Defaults to not applied | [optional] |
| **visibleOnly** | **Boolean**| Defaults to true.  When true, only shows users that are actionable based on the team&#39;s privacy settings. When false, shows all users on the team, even if you can&#39;t take action on that user. Deactivated users are also included when false.  | [optional] |
| **perPage** | **Integer**| How many users to show per page in the range [1, 100]. Defaults to 25.  Results are only paginated if the page parameter is defined | [optional] |
| **page** | **Integer**| The current page to fetch users from. Defaults to returning all users | [optional] |
| **includePagingCounts** | **Boolean**| Whether to include total_pages and total_count in the metadata. Defaults to false | [optional] |
| **hasCrmUser** | **Boolean**| Filters users based on if they have a crm user mapped or not. | [optional] |
| **workCountry** | [**List&lt;String&gt;**](String.md)| Filters users based on assigned work_country. | [optional] |
| **sortBy** | **String**| Key to sort on, must be one of: id, email, name, group, role. Defaults to id | [optional] |
| **sortDirection** | **String**| Direction to sort in, must be one of: ASC, DESC. Defaults to DESC | [optional] |

### Return type

[**List&lt;User&gt;**](User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

