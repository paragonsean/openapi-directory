# BusinessUsersApi

All URIs are relative to *https://sandbox-api.onsched.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**setupV1BusinessusersEmailCompaniesGet**](BusinessUsersApi.md#setupV1BusinessusersEmailCompaniesGet) | **GET** /setup/v1/businessusers/{email}/companies | List User Companies |
| [**setupV1BusinessusersGet**](BusinessUsersApi.md#setupV1BusinessusersGet) | **GET** /setup/v1/businessusers | List Users |
| [**setupV1BusinessusersIdDelete**](BusinessUsersApi.md#setupV1BusinessusersIdDelete) | **DELETE** /setup/v1/businessusers/{id} | Delete User |
| [**setupV1BusinessusersIdGet**](BusinessUsersApi.md#setupV1BusinessusersIdGet) | **GET** /setup/v1/businessusers/{id} | Get User |
| [**setupV1BusinessusersIdPut**](BusinessUsersApi.md#setupV1BusinessusersIdPut) | **PUT** /setup/v1/businessusers/{id} | Update User |
| [**setupV1BusinessusersPermissionsGet**](BusinessUsersApi.md#setupV1BusinessusersPermissionsGet) | **GET** /setup/v1/businessusers/permissions | List User Permissions |
| [**setupV1BusinessusersPost**](BusinessUsersApi.md#setupV1BusinessusersPost) | **POST** /setup/v1/businessusers | Create User |


<a id="setupV1BusinessusersEmailCompaniesGet"></a>
# **setupV1BusinessusersEmailCompaniesGet**
> AuthorizedCompanyListViewModel setupV1BusinessusersEmailCompaniesGet(email, searchText, offset, limit)

List User Companies

&lt;p&gt;Use this endpoint to return a &lt;b&gt;List of Companies&lt;/b&gt; associated with the business users email requested. A business user &lt;b&gt;email&lt;/b&gt; address is required. Use the offset and limit parameters to control the page start and number of results. Default offset is 0, limit is 20, max is 100. Use the query parameters to filter the results further.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BusinessUsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sandbox-api.onsched.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    BusinessUsersApi apiInstance = new BusinessUsersApi(defaultClient);
    String email = "email_example"; // String | Email of business user
    String searchText = "searchText_example"; // String | All or partial company name
    Integer offset = 56; // Integer | Starting row of page, default 0
    Integer limit = 56; // Integer | Page limit default 20, max 100
    try {
      AuthorizedCompanyListViewModel result = apiInstance.setupV1BusinessusersEmailCompaniesGet(email, searchText, offset, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BusinessUsersApi#setupV1BusinessusersEmailCompaniesGet");
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
| **email** | **String**| Email of business user | |
| **searchText** | **String**| All or partial company name | [optional] |
| **offset** | **Integer**| Starting row of page, default 0 | [optional] |
| **limit** | **Integer**| Page limit default 20, max 100 | [optional] |

### Return type

[**AuthorizedCompanyListViewModel**](AuthorizedCompanyListViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="setupV1BusinessusersGet"></a>
# **setupV1BusinessusersGet**
> BusinessUserListViewModel setupV1BusinessusersGet(locationId, email, role, offset, limit)

List Users

&lt;p&gt;Use this endpoint to return a &lt;b&gt;List of Business Users and their Roles&lt;/b&gt;. The results are returned in pages. Use the offset and limit parameters to control the page start and number of results. Default offset is 0, limit is 20, max is 100. Use the query parameters to filter the results further.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BusinessUsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sandbox-api.onsched.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    BusinessUsersApi apiInstance = new BusinessUsersApi(defaultClient);
    String locationId = "locationId_example"; // String | id of business location, defaults to primary business location
    String email = "email_example"; // String | Filter by email address
    String role = "role_example"; // String | Filter user role
    Integer offset = 56; // Integer | Starting row of page, default 0
    Integer limit = 56; // Integer | Page limit default 20, max 100
    try {
      BusinessUserListViewModel result = apiInstance.setupV1BusinessusersGet(locationId, email, role, offset, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BusinessUsersApi#setupV1BusinessusersGet");
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
| **locationId** | **String**| id of business location, defaults to primary business location | [optional] |
| **email** | **String**| Filter by email address | [optional] |
| **role** | **String**| Filter user role | [optional] |
| **offset** | **Integer**| Starting row of page, default 0 | [optional] |
| **limit** | **Integer**| Page limit default 20, max 100 | [optional] |

### Return type

[**BusinessUserListViewModel**](BusinessUserListViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="setupV1BusinessusersIdDelete"></a>
# **setupV1BusinessusersIdDelete**
> setupV1BusinessusersIdDelete(id)

Delete User

&lt;p&gt;Use this endpoint to permanently &lt;b&gt;Delete&lt;/b&gt; a Business User. A valid &lt;b&gt;businessUser id&lt;/b&gt; is required.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BusinessUsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sandbox-api.onsched.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    BusinessUsersApi apiInstance = new BusinessUsersApi(defaultClient);
    String id = "id_example"; // String | 
    try {
      apiInstance.setupV1BusinessusersIdDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling BusinessUsersApi#setupV1BusinessusersIdDelete");
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
| **id** | **String**|  | |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="setupV1BusinessusersIdGet"></a>
# **setupV1BusinessusersIdGet**
> BusinessUserViewModel setupV1BusinessusersIdGet(id)

Get User

&lt;p&gt;Use this endpoint to return a &lt;b&gt;Business User&lt;/b&gt; object. A valid &lt;b&gt;businessUser id&lt;/b&gt; is required. Find businessUser id&#39;s using the &lt;i&gt;GET /setup/v1/businessusers&lt;/i&gt; endpoint.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BusinessUsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sandbox-api.onsched.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    BusinessUsersApi apiInstance = new BusinessUsersApi(defaultClient);
    String id = "id_example"; // String | id of businessUser object
    try {
      BusinessUserViewModel result = apiInstance.setupV1BusinessusersIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BusinessUsersApi#setupV1BusinessusersIdGet");
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
| **id** | **String**| id of businessUser object | |

### Return type

[**BusinessUserViewModel**](BusinessUserViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="setupV1BusinessusersIdPut"></a>
# **setupV1BusinessusersIdPut**
> BusinessUserViewModel setupV1BusinessusersIdPut(id, businessUserUpdateModel)

Update User

&lt;p&gt;Use this endpoint to &lt;b&gt;Update&lt;/b&gt; a Business User. A valid &lt;b&gt;businessUser id&lt;/b&gt; is required.&lt;/p&gt;  &lt;p&gt;    &lt;b&gt;Business Roles Include: bizowner&lt;/b&gt; (Business Owner), &lt;b&gt;bizadmin&lt;/b&gt; (Business Administrator), &lt;b&gt;bizresource&lt;/b&gt; (Business User - Bookable Resource).&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BusinessUsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sandbox-api.onsched.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    BusinessUsersApi apiInstance = new BusinessUsersApi(defaultClient);
    String id = "id_example"; // String | 
    BusinessUserUpdateModel businessUserUpdateModel = new BusinessUserUpdateModel(); // BusinessUserUpdateModel | 
    try {
      BusinessUserViewModel result = apiInstance.setupV1BusinessusersIdPut(id, businessUserUpdateModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BusinessUsersApi#setupV1BusinessusersIdPut");
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
| **id** | **String**|  | |
| **businessUserUpdateModel** | [**BusinessUserUpdateModel**](BusinessUserUpdateModel.md)|  | [optional] |

### Return type

[**BusinessUserViewModel**](BusinessUserViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="setupV1BusinessusersPermissionsGet"></a>
# **setupV1BusinessusersPermissionsGet**
> BusinessPermissionListViewModel setupV1BusinessusersPermissionsGet(role, offset, limit)

List User Permissions

&lt;p&gt;Use this endpoint to return a &lt;b&gt;List of Business User Permissions by Role&lt;/b&gt;. Results are returned in pages. Use the offset and limit parameters to control the page start and number of results. Default offset is 0, limit is 20, max is 100. Use the query parameters to filter the results further.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BusinessUsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sandbox-api.onsched.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    BusinessUsersApi apiInstance = new BusinessUsersApi(defaultClient);
    String role = "role_example"; // String | Filter permissions by role
    Integer offset = 56; // Integer | Starting row of page, default 0
    Integer limit = 56; // Integer | Page limit default 20, max 100
    try {
      BusinessPermissionListViewModel result = apiInstance.setupV1BusinessusersPermissionsGet(role, offset, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BusinessUsersApi#setupV1BusinessusersPermissionsGet");
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
| **role** | **String**| Filter permissions by role | [optional] |
| **offset** | **Integer**| Starting row of page, default 0 | [optional] |
| **limit** | **Integer**| Page limit default 20, max 100 | [optional] |

### Return type

[**BusinessPermissionListViewModel**](BusinessPermissionListViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="setupV1BusinessusersPost"></a>
# **setupV1BusinessusersPost**
> BusinessUserViewModel setupV1BusinessusersPost(businessUserInputModel)

Create User

&lt;p&gt;Use this endpoint to &lt;b&gt;Create&lt;/b&gt; a Business User. If not specified, the business location defaults to the primary business location. &lt;/p&gt;  &lt;p&gt;Required fields: &lt;b&gt;Name&lt;/b&gt;, &lt;b&gt;Email&lt;/b&gt; and &lt;b&gt;Role&lt;/b&gt;&lt;b&gt;Note:&lt;/b&gt; If the businessUser is a bookable resource (bizresource) then a resourceId is required.&lt;/p&gt;  &lt;p&gt;For role, use one of the values listed. &lt;b&gt;Business Roles Include: bizowner&lt;/b&gt; (Business Owner), &lt;b&gt;bizadmin&lt;/b&gt; (Business Administrator), &lt;b&gt;bizresource&lt;/b&gt; (Business User - Bookable Resource).&lt;/p&gt;  &lt;p&gt;The &lt;b&gt;sendRegistrationInvite&lt;/b&gt; parameter is available to API consumers for their own use. It provides no added functionality in OnSched.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BusinessUsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sandbox-api.onsched.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    BusinessUsersApi apiInstance = new BusinessUsersApi(defaultClient);
    BusinessUserInputModel businessUserInputModel = new BusinessUserInputModel(); // BusinessUserInputModel | 
    try {
      BusinessUserViewModel result = apiInstance.setupV1BusinessusersPost(businessUserInputModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BusinessUsersApi#setupV1BusinessusersPost");
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
| **businessUserInputModel** | [**BusinessUserInputModel**](BusinessUserInputModel.md)|  | [optional] |

### Return type

[**BusinessUserViewModel**](BusinessUserViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

