# AuthorizationCategoriesApi

All URIs are relative to *https://secure.agco-ats.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**authorizationCategoriesAddUser**](AuthorizationCategoriesApi.md#authorizationCategoriesAddUser) | **POST** /api/v2/AuthorizationCategories/{id}/Users/{userID} | Add a category that a user can see. |
| [**authorizationCategoriesDelete**](AuthorizationCategoriesApi.md#authorizationCategoriesDelete) | **DELETE** /api/v2/AuthorizationCategories/{id} | Remove an authorization category. |
| [**authorizationCategoriesGet**](AuthorizationCategoriesApi.md#authorizationCategoriesGet) | **GET** /api/v2/AuthorizationCategories | Get authorization categories. |
| [**authorizationCategoriesGetUsers**](AuthorizationCategoriesApi.md#authorizationCategoriesGetUsers) | **GET** /api/v2/AuthorizationCategories/Users | Returns a report of access that users have to Authorization Categories. |
| [**authorizationCategoriesPost**](AuthorizationCategoriesApi.md#authorizationCategoriesPost) | **POST** /api/v2/AuthorizationCategories | Add an authorization category. |
| [**authorizationCategoriesPut**](AuthorizationCategoriesApi.md#authorizationCategoriesPut) | **PUT** /api/v2/AuthorizationCategories/{id} | Update an authorization category. |
| [**authorizationCategoriesRemoveUser**](AuthorizationCategoriesApi.md#authorizationCategoriesRemoveUser) | **DELETE** /api/v2/AuthorizationCategories/{id}/Users/{userID} | Deletes a category a user could see. |


<a id="authorizationCategoriesAddUser"></a>
# **authorizationCategoriesAddUser**
> authorizationCategoriesAddUser(id, userID)

Add a category that a user can see.

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuthorizationCategoriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    AuthorizationCategoriesApi apiInstance = new AuthorizationCategoriesApi(defaultClient);
    String id = "id_example"; // String | 
    Integer userID = 56; // Integer | 
    try {
      apiInstance.authorizationCategoriesAddUser(id, userID);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthorizationCategoriesApi#authorizationCategoriesAddUser");
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
| **userID** | **Integer**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |
| **0** | API Error Response |  -  |

<a id="authorizationCategoriesDelete"></a>
# **authorizationCategoriesDelete**
> authorizationCategoriesDelete(id)

Remove an authorization category.

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuthorizationCategoriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    AuthorizationCategoriesApi apiInstance = new AuthorizationCategoriesApi(defaultClient);
    String id = "id_example"; // String | The ID of the authorization category.
    try {
      apiInstance.authorizationCategoriesDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthorizationCategoriesApi#authorizationCategoriesDelete");
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
| **id** | **String**| The ID of the authorization category. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |
| **0** | API Error Response |  -  |

<a id="authorizationCategoriesGet"></a>
# **authorizationCategoriesGet**
> APIIPagedResponseAuthorizationCodesSharedModelsCategory authorizationCategoriesGet(limit, offset, userID, definitionID)

Get authorization categories.

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuthorizationCategoriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    AuthorizationCategoriesApi apiInstance = new AuthorizationCategoriesApi(defaultClient);
    Integer limit = 56; // Integer | Optional. The page limit.  If not specified, the default page limit is 10.
    Integer offset = 56; // Integer | Optional. The page offset.  If not specified, the default page offset is 0.
    Integer userID = 56; // Integer | Optional. Filter by categories visible to the provided user with the provided userID.
    String definitionID = "definitionID_example"; // String | Optional. Filter by categories containing a definition with the provided ID.
    try {
      APIIPagedResponseAuthorizationCodesSharedModelsCategory result = apiInstance.authorizationCategoriesGet(limit, offset, userID, definitionID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthorizationCategoriesApi#authorizationCategoriesGet");
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
| **limit** | **Integer**| Optional. The page limit.  If not specified, the default page limit is 10. | [optional] |
| **offset** | **Integer**| Optional. The page offset.  If not specified, the default page offset is 0. | [optional] |
| **userID** | **Integer**| Optional. Filter by categories visible to the provided user with the provided userID. | [optional] |
| **definitionID** | **String**| Optional. Filter by categories containing a definition with the provided ID. | [optional] |

### Return type

[**APIIPagedResponseAuthorizationCodesSharedModelsCategory**](APIIPagedResponseAuthorizationCodesSharedModelsCategory.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | API Error Response |  -  |

<a id="authorizationCategoriesGetUsers"></a>
# **authorizationCategoriesGetUsers**
> APIIPagedResponseAuthorizationCodesSharedModelsCategoryUserReport authorizationCategoriesGetUsers(limit, offset, userIDs, categoryIDs, includeCategories, includeUsers, userSearch)

Returns a report of access that users have to Authorization Categories.

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuthorizationCategoriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    AuthorizationCategoriesApi apiInstance = new AuthorizationCategoriesApi(defaultClient);
    Integer limit = 56; // Integer | Optional. Defaults to 10.
    Integer offset = 56; // Integer | Optional. Defaults to 0.
    String userIDs = "userIDs_example"; // String | Optional. Includes only users with IDs on the provided comma-separated list.
    String categoryIDs = "categoryIDs_example"; // String | Optional. Includes only users with categories with IDs on the provided comma-separated list.
    Boolean includeCategories = true; // Boolean | If true, include full Authorization Category detail. Defaults to false.
    Boolean includeUsers = true; // Boolean | If true, include full User detail. Defaults to false.
    String userSearch = "userSearch_example"; // String | Optional. Includes only users with a Name, Username, or Email containing the provided value.
    try {
      APIIPagedResponseAuthorizationCodesSharedModelsCategoryUserReport result = apiInstance.authorizationCategoriesGetUsers(limit, offset, userIDs, categoryIDs, includeCategories, includeUsers, userSearch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthorizationCategoriesApi#authorizationCategoriesGetUsers");
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
| **limit** | **Integer**| Optional. Defaults to 10. | [optional] |
| **offset** | **Integer**| Optional. Defaults to 0. | [optional] |
| **userIDs** | **String**| Optional. Includes only users with IDs on the provided comma-separated list. | [optional] |
| **categoryIDs** | **String**| Optional. Includes only users with categories with IDs on the provided comma-separated list. | [optional] |
| **includeCategories** | **Boolean**| If true, include full Authorization Category detail. Defaults to false. | [optional] |
| **includeUsers** | **Boolean**| If true, include full User detail. Defaults to false. | [optional] |
| **userSearch** | **String**| Optional. Includes only users with a Name, Username, or Email containing the provided value. | [optional] |

### Return type

[**APIIPagedResponseAuthorizationCodesSharedModelsCategoryUserReport**](APIIPagedResponseAuthorizationCodesSharedModelsCategoryUserReport.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | API Error Response |  -  |

<a id="authorizationCategoriesPost"></a>
# **authorizationCategoriesPost**
> String authorizationCategoriesPost(authorizationCodesSharedModelsCategory)

Add an authorization category.

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuthorizationCategoriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    AuthorizationCategoriesApi apiInstance = new AuthorizationCategoriesApi(defaultClient);
    AuthorizationCodesSharedModelsCategory authorizationCodesSharedModelsCategory = new AuthorizationCodesSharedModelsCategory(); // AuthorizationCodesSharedModelsCategory | An authorization category.
    try {
      String result = apiInstance.authorizationCategoriesPost(authorizationCodesSharedModelsCategory);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthorizationCategoriesApi#authorizationCategoriesPost");
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
| **authorizationCodesSharedModelsCategory** | [**AuthorizationCodesSharedModelsCategory**](AuthorizationCodesSharedModelsCategory.md)| An authorization category. | |

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | API Error Response |  -  |

<a id="authorizationCategoriesPut"></a>
# **authorizationCategoriesPut**
> authorizationCategoriesPut(id, authorizationCodesSharedModelsCategory)

Update an authorization category.

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuthorizationCategoriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    AuthorizationCategoriesApi apiInstance = new AuthorizationCategoriesApi(defaultClient);
    String id = "id_example"; // String | 
    AuthorizationCodesSharedModelsCategory authorizationCodesSharedModelsCategory = new AuthorizationCodesSharedModelsCategory(); // AuthorizationCodesSharedModelsCategory | An authorization category.
    try {
      apiInstance.authorizationCategoriesPut(id, authorizationCodesSharedModelsCategory);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthorizationCategoriesApi#authorizationCategoriesPut");
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
| **authorizationCodesSharedModelsCategory** | [**AuthorizationCodesSharedModelsCategory**](AuthorizationCodesSharedModelsCategory.md)| An authorization category. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |
| **0** | API Error Response |  -  |

<a id="authorizationCategoriesRemoveUser"></a>
# **authorizationCategoriesRemoveUser**
> authorizationCategoriesRemoveUser(id, userID)

Deletes a category a user could see.

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuthorizationCategoriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    AuthorizationCategoriesApi apiInstance = new AuthorizationCategoriesApi(defaultClient);
    String id = "id_example"; // String | 
    Integer userID = 56; // Integer | 
    try {
      apiInstance.authorizationCategoriesRemoveUser(id, userID);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthorizationCategoriesApi#authorizationCategoriesRemoveUser");
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
| **userID** | **Integer**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |
| **0** | API Error Response |  -  |

