# UsersApi

All URIs are relative to *https://api.snyk.io/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getMyDetails**](UsersApi.md#getMyDetails) | **GET** /user/me | Get My Details |
| [**getOrganizationNotificationSettings**](UsersApi.md#getOrganizationNotificationSettings) | **GET** /user/me/notification-settings/org/{orgId} | Get organization notification settings |
| [**getProjectNotificationSettings**](UsersApi.md#getProjectNotificationSettings) | **GET** /user/me/notification-settings/org/{orgId}/project/{projectId} | Get project notification settings |
| [**getUserDetails**](UsersApi.md#getUserDetails) | **GET** /user/{userId} | Get User Details |
| [**modifyOrganizationNotificationSettings**](UsersApi.md#modifyOrganizationNotificationSettings) | **PUT** /user/me/notification-settings/org/{orgId} | Modify organization notification settings |
| [**modifyProjectNotificationSettings**](UsersApi.md#modifyProjectNotificationSettings) | **PUT** /user/me/notification-settings/org/{orgId}/project/{projectId} | Modify project notification settings |


<a id="getMyDetails"></a>
# **getMyDetails**
> GetMyDetails200Response getMyDetails()

Get My Details



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
    defaultClient.setBasePath("https://api.snyk.io/v1");

    UsersApi apiInstance = new UsersApi(defaultClient);
    try {
      GetMyDetails200Response result = apiInstance.getMyDetails();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#getMyDetails");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetMyDetails200Response**](GetMyDetails200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | &#x60;API_KEY&#x60; is invalid. |  -  |

<a id="getOrganizationNotificationSettings"></a>
# **getOrganizationNotificationSettings**
> OrgOrgIdNotificationSettingsGet200Response getOrganizationNotificationSettings(orgId)

Get organization notification settings



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
    defaultClient.setBasePath("https://api.snyk.io/v1");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String orgId = "4a18d42f-0706-4ad0-b127-24078731fbed"; // String | The organization ID. The `API_KEY` must have access to this organization.
    try {
      OrgOrgIdNotificationSettingsGet200Response result = apiInstance.getOrganizationNotificationSettings(orgId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#getOrganizationNotificationSettings");
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
| **orgId** | **String**| The organization ID. The &#x60;API_KEY&#x60; must have access to this organization. | |

### Return type

[**OrgOrgIdNotificationSettingsGet200Response**](OrgOrgIdNotificationSettingsGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="getProjectNotificationSettings"></a>
# **getProjectNotificationSettings**
> OrgOrgIdNotificationSettingsGet200Response getProjectNotificationSettings(orgId, projectId)

Get project notification settings



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
    defaultClient.setBasePath("https://api.snyk.io/v1");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String orgId = "4a18d42f-0706-4ad0-b127-24078731fbed"; // String | The organization ID. The `API_KEY` must have access to this organization.
    String projectId = "6d5813be-7e6d-4ab8-80c2-1e3e2a454545"; // String | The project ID to return notification settings for.
    try {
      OrgOrgIdNotificationSettingsGet200Response result = apiInstance.getProjectNotificationSettings(orgId, projectId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#getProjectNotificationSettings");
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
| **orgId** | **String**| The organization ID. The &#x60;API_KEY&#x60; must have access to this organization. | |
| **projectId** | **String**| The project ID to return notification settings for. | |

### Return type

[**OrgOrgIdNotificationSettingsGet200Response**](OrgOrgIdNotificationSettingsGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="getUserDetails"></a>
# **getUserDetails**
> GetUserDetails200Response getUserDetails(userId)

Get User Details



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
    defaultClient.setBasePath("https://api.snyk.io/v1");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String userId = "4a18d42f-0706-4ad0-b127-24078731fbed"; // String | The users ID. The `API_KEY` must have admin access to at least one group or organization where the requested user is a member and must have the `api` entitlement on their preferred organization.
    try {
      GetUserDetails200Response result = apiInstance.getUserDetails(userId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#getUserDetails");
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
| **userId** | **String**| The users ID. The &#x60;API_KEY&#x60; must have admin access to at least one group or organization where the requested user is a member and must have the &#x60;api&#x60; entitlement on their preferred organization. | |

### Return type

[**GetUserDetails200Response**](GetUserDetails200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | The provided &#x60;id&#x60; is not in a valid format. |  -  |
| **401** | &#x60;API_KEY&#x60; is invalid. |  -  |
| **404** | The requested user could not be found or caller does not have sufficient permissions. |  -  |

<a id="modifyOrganizationNotificationSettings"></a>
# **modifyOrganizationNotificationSettings**
> OrgOrgIdNotificationSettingsGet200Response modifyOrganizationNotificationSettings(orgId, setNotificationSettingsRequest)

Modify organization notification settings



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
    defaultClient.setBasePath("https://api.snyk.io/v1");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String orgId = "orgId_example"; // String | Automatically added
    SetNotificationSettingsRequest setNotificationSettingsRequest = new SetNotificationSettingsRequest(); // SetNotificationSettingsRequest | 
    try {
      OrgOrgIdNotificationSettingsGet200Response result = apiInstance.modifyOrganizationNotificationSettings(orgId, setNotificationSettingsRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#modifyOrganizationNotificationSettings");
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
| **orgId** | **String**| Automatically added | |
| **setNotificationSettingsRequest** | [**SetNotificationSettingsRequest**](SetNotificationSettingsRequest.md)|  | [optional] |

### Return type

[**OrgOrgIdNotificationSettingsGet200Response**](OrgOrgIdNotificationSettingsGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="modifyProjectNotificationSettings"></a>
# **modifyProjectNotificationSettings**
> modifyProjectNotificationSettings(orgId, projectId, modifyProjectNotificationSettingsRequest)

Modify project notification settings



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
    defaultClient.setBasePath("https://api.snyk.io/v1");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String orgId = "orgId_example"; // String | Automatically added
    String projectId = "projectId_example"; // String | Automatically added
    ModifyProjectNotificationSettingsRequest modifyProjectNotificationSettingsRequest = new ModifyProjectNotificationSettingsRequest(); // ModifyProjectNotificationSettingsRequest | 
    try {
      apiInstance.modifyProjectNotificationSettings(orgId, projectId, modifyProjectNotificationSettingsRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#modifyProjectNotificationSettings");
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
| **orgId** | **String**| Automatically added | |
| **projectId** | **String**| Automatically added | |
| **modifyProjectNotificationSettingsRequest** | [**ModifyProjectNotificationSettingsRequest**](ModifyProjectNotificationSettingsRequest.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

