# UserProfileApi

All URIs are relative to *https://api.avaza.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**userProfileGet**](UserProfileApi.md#userProfileGet) | **GET** /api/UserProfile | Get Collection of Users who have roles in the current Avaza account. |


<a id="userProfileGet"></a>
# **userProfileGet**
> UserList userProfileGet(roles, tags, currentUserOnly, companyIDFK)

Get Collection of Users who have roles in the current Avaza account.

Admin and Invoice Managers can see all. Other users are limited to seeing their own profile.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserProfileApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.avaza.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    UserProfileApi apiInstance = new UserProfileApi(defaultClient);
    String roles = "roles_example"; // String | Optional list of comma separated role codes to filter users by (e.g. \"TimesheetUser,Admin\")
    String tags = "tags_example"; // String | 
    Boolean currentUserOnly = true; // Boolean | Optional boolean (true/false) to filter to only show current authenticated user (always true for non Admin/InvoiceManager users)
    Integer companyIDFK = 56; // Integer | Optionally filter by Company ID
    try {
      UserList result = apiInstance.userProfileGet(roles, tags, currentUserOnly, companyIDFK);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserProfileApi#userProfileGet");
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
| **roles** | **String**| Optional list of comma separated role codes to filter users by (e.g. \&quot;TimesheetUser,Admin\&quot;) | [optional] |
| **tags** | **String**|  | [optional] |
| **currentUserOnly** | **Boolean**| Optional boolean (true/false) to filter to only show current authenticated user (always true for non Admin/InvoiceManager users) | [optional] |
| **companyIDFK** | **Integer**| Optionally filter by Company ID | [optional] |

### Return type

[**UserList**](UserList.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

