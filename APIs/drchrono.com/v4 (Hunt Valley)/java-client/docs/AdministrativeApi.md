# AdministrativeApi

All URIs are relative to *https://app.drchrono.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**doctorsList**](AdministrativeApi.md#doctorsList) | **GET** /api/doctors |  |
| [**doctorsRead**](AdministrativeApi.md#doctorsRead) | **GET** /api/doctors/{id} |  |
| [**userGroupsList**](AdministrativeApi.md#userGroupsList) | **GET** /api/user_groups |  |
| [**userGroupsRead**](AdministrativeApi.md#userGroupsRead) | **GET** /api/user_groups/{id} |  |
| [**usersList**](AdministrativeApi.md#usersList) | **GET** /api/users |  |
| [**usersRead**](AdministrativeApi.md#usersRead) | **GET** /api/users/{id} |  |


<a id="doctorsList"></a>
# **doctorsList**
> DoctorsList200Response doctorsList(cursor, pageSize, doctor)



Retrieve or search doctors within practice group

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AdministrativeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.drchrono.com");
    
    // Configure OAuth2 access token for authorization: drchrono_oauth2
    OAuth drchrono_oauth2 = (OAuth) defaultClient.getAuthentication("drchrono_oauth2");
    drchrono_oauth2.setAccessToken("YOUR ACCESS TOKEN");

    AdministrativeApi apiInstance = new AdministrativeApi(defaultClient);
    String cursor = "cursor_example"; // String | 
    Integer pageSize = 56; // Integer | 
    Integer doctor = 56; // Integer | 
    try {
      DoctorsList200Response result = apiInstance.doctorsList(cursor, pageSize, doctor);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AdministrativeApi#doctorsList");
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
| **cursor** | **String**|  | [optional] |
| **pageSize** | **Integer**|  | [optional] |
| **doctor** | **Integer**|  | [optional] |

### Return type

[**DoctorsList200Response**](DoctorsList200Response.md)

### Authorization

[drchrono_oauth2](../README.md#drchrono_oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Permission Denied |  -  |
| **404** | Not Found |  -  |
| **405** | Method Not Allowed |  -  |
| **500** | Internal Server Error |  -  |

<a id="doctorsRead"></a>
# **doctorsRead**
> Doctor doctorsRead(id, doctor)



Retrieve an existing dcotor

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AdministrativeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.drchrono.com");
    
    // Configure OAuth2 access token for authorization: drchrono_oauth2
    OAuth drchrono_oauth2 = (OAuth) defaultClient.getAuthentication("drchrono_oauth2");
    drchrono_oauth2.setAccessToken("YOUR ACCESS TOKEN");

    AdministrativeApi apiInstance = new AdministrativeApi(defaultClient);
    String id = "id_example"; // String | 
    Integer doctor = 56; // Integer | 
    try {
      Doctor result = apiInstance.doctorsRead(id, doctor);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AdministrativeApi#doctorsRead");
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
| **doctor** | **Integer**|  | [optional] |

### Return type

[**Doctor**](Doctor.md)

### Authorization

[drchrono_oauth2](../README.md#drchrono_oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Permission Denied |  -  |
| **404** | Not Found |  -  |
| **405** | Method Not Allowed |  -  |
| **500** | Internal Server Error |  -  |

<a id="userGroupsList"></a>
# **userGroupsList**
> UserGroupsList200Response userGroupsList(cursor, pageSize, doctor)



Retrieve or search user groups

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AdministrativeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.drchrono.com");
    
    // Configure OAuth2 access token for authorization: drchrono_oauth2
    OAuth drchrono_oauth2 = (OAuth) defaultClient.getAuthentication("drchrono_oauth2");
    drchrono_oauth2.setAccessToken("YOUR ACCESS TOKEN");

    AdministrativeApi apiInstance = new AdministrativeApi(defaultClient);
    String cursor = "cursor_example"; // String | 
    Integer pageSize = 56; // Integer | 
    Integer doctor = 56; // Integer | 
    try {
      UserGroupsList200Response result = apiInstance.userGroupsList(cursor, pageSize, doctor);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AdministrativeApi#userGroupsList");
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
| **cursor** | **String**|  | [optional] |
| **pageSize** | **Integer**|  | [optional] |
| **doctor** | **Integer**|  | [optional] |

### Return type

[**UserGroupsList200Response**](UserGroupsList200Response.md)

### Authorization

[drchrono_oauth2](../README.md#drchrono_oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Permission Denied |  -  |
| **404** | Not Found |  -  |
| **405** | Method Not Allowed |  -  |
| **500** | Internal Server Error |  -  |

<a id="userGroupsRead"></a>
# **userGroupsRead**
> UserProfilesGroup userGroupsRead(id, doctor)



Retrieve an existing user group

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AdministrativeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.drchrono.com");
    
    // Configure OAuth2 access token for authorization: drchrono_oauth2
    OAuth drchrono_oauth2 = (OAuth) defaultClient.getAuthentication("drchrono_oauth2");
    drchrono_oauth2.setAccessToken("YOUR ACCESS TOKEN");

    AdministrativeApi apiInstance = new AdministrativeApi(defaultClient);
    String id = "id_example"; // String | 
    Integer doctor = 56; // Integer | 
    try {
      UserProfilesGroup result = apiInstance.userGroupsRead(id, doctor);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AdministrativeApi#userGroupsRead");
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
| **doctor** | **Integer**|  | [optional] |

### Return type

[**UserProfilesGroup**](UserProfilesGroup.md)

### Authorization

[drchrono_oauth2](../README.md#drchrono_oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Permission Denied |  -  |
| **404** | Not Found |  -  |
| **405** | Method Not Allowed |  -  |
| **500** | Internal Server Error |  -  |

<a id="usersList"></a>
# **usersList**
> UsersList200Response usersList(cursor, pageSize, doctor)



Retrieve or search users, &#x60;/api/users/current&#x60; can be used to identify logged in user, it will redirect to &#x60;/api/users/{current_user_id}&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AdministrativeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.drchrono.com");
    
    // Configure OAuth2 access token for authorization: drchrono_oauth2
    OAuth drchrono_oauth2 = (OAuth) defaultClient.getAuthentication("drchrono_oauth2");
    drchrono_oauth2.setAccessToken("YOUR ACCESS TOKEN");

    AdministrativeApi apiInstance = new AdministrativeApi(defaultClient);
    String cursor = "cursor_example"; // String | 
    Integer pageSize = 56; // Integer | 
    Integer doctor = 56; // Integer | 
    try {
      UsersList200Response result = apiInstance.usersList(cursor, pageSize, doctor);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AdministrativeApi#usersList");
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
| **cursor** | **String**|  | [optional] |
| **pageSize** | **Integer**|  | [optional] |
| **doctor** | **Integer**|  | [optional] |

### Return type

[**UsersList200Response**](UsersList200Response.md)

### Authorization

[drchrono_oauth2](../README.md#drchrono_oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Permission Denied |  -  |
| **404** | Not Found |  -  |
| **405** | Method Not Allowed |  -  |
| **500** | Internal Server Error |  -  |

<a id="usersRead"></a>
# **usersRead**
> UserProfile usersRead(id, doctor)



Retrieve an existing user, &#x60;/api/users/current&#x60; can be used to identify logged in user, it will redirect to &#x60;/api/users/{current_user_id}&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AdministrativeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.drchrono.com");
    
    // Configure OAuth2 access token for authorization: drchrono_oauth2
    OAuth drchrono_oauth2 = (OAuth) defaultClient.getAuthentication("drchrono_oauth2");
    drchrono_oauth2.setAccessToken("YOUR ACCESS TOKEN");

    AdministrativeApi apiInstance = new AdministrativeApi(defaultClient);
    String id = "id_example"; // String | 
    Integer doctor = 56; // Integer | 
    try {
      UserProfile result = apiInstance.usersRead(id, doctor);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AdministrativeApi#usersRead");
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
| **doctor** | **Integer**|  | [optional] |

### Return type

[**UserProfile**](UserProfile.md)

### Authorization

[drchrono_oauth2](../README.md#drchrono_oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Permission Denied |  -  |
| **404** | Not Found |  -  |
| **405** | Method Not Allowed |  -  |
| **500** | Internal Server Error |  -  |

