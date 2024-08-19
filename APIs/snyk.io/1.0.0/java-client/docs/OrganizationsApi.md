# OrganizationsApi

All URIs are relative to *https://api.snyk.io/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createANewOrganization**](OrganizationsApi.md#createANewOrganization) | **POST** /org | Create a new organization |
| [**deletePendingUserProvision**](OrganizationsApi.md#deletePendingUserProvision) | **DELETE** /org/{orgId}/provision | Delete pending user provision |
| [**inviteUsers**](OrganizationsApi.md#inviteUsers) | **POST** /org/{orgId}/invite | Invite users |
| [**listAllTheOrganizationsAUserBelongsTo**](OrganizationsApi.md#listAllTheOrganizationsAUserBelongsTo) | **GET** /orgs | List all the organizations a user belongs to |
| [**listMembers**](OrganizationsApi.md#listMembers) | **GET** /org/{orgId}/members | List Members |
| [**listPendingUserProvisions**](OrganizationsApi.md#listPendingUserProvisions) | **GET** /org/{orgId}/provision | List pending user provisions |
| [**orgOrgIdNotificationSettingsGet**](OrganizationsApi.md#orgOrgIdNotificationSettingsGet) | **GET** /org/{orgId}/notification-settings | Get organization notification settings |
| [**provisionAUserToTheOrganization**](OrganizationsApi.md#provisionAUserToTheOrganization) | **POST** /org/{orgId}/provision | Provision a user to the organization |
| [**removeAMemberFromTheOrganization**](OrganizationsApi.md#removeAMemberFromTheOrganization) | **DELETE** /org/{orgId}/members/{userId} | Remove a member from the organization |
| [**removeOrganization**](OrganizationsApi.md#removeOrganization) | **DELETE** /org/{orgId} | Remove organization |
| [**setNotificationSettings**](OrganizationsApi.md#setNotificationSettings) | **PUT** /org/{orgId}/notification-settings | Set notification settings |
| [**updateAMemberInTheOrganization**](OrganizationsApi.md#updateAMemberInTheOrganization) | **PUT** /org/{orgId}/members/{userId} | Update a member in the organization |
| [**updateAMembersRoleInTheOrganization**](OrganizationsApi.md#updateAMembersRoleInTheOrganization) | **PUT** /org/{orgId}/members/update/{userId} | Update a member&#39;s role in the organization |
| [**updateOrganizationSettings**](OrganizationsApi.md#updateOrganizationSettings) | **PUT** /org/{orgId}/settings | Update organization settings |
| [**viewOrganizationSettings**](OrganizationsApi.md#viewOrganizationSettings) | **GET** /org/{orgId}/settings | View organization settings |


<a id="createANewOrganization"></a>
# **createANewOrganization**
> createANewOrganization(createANewOrganizationRequest)

Create a new organization



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganizationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.snyk.io/v1");

    OrganizationsApi apiInstance = new OrganizationsApi(defaultClient);
    CreateANewOrganizationRequest createANewOrganizationRequest = new CreateANewOrganizationRequest(); // CreateANewOrganizationRequest | 
    try {
      apiInstance.createANewOrganization(createANewOrganizationRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganizationsApi#createANewOrganization");
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
| **createANewOrganizationRequest** | [**CreateANewOrganizationRequest**](CreateANewOrganizationRequest.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8, application/json, charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |
| **400** | A group of errors that happened in the process of creating a new organization and were unexpected |  -  |
| **401** | Authorization errors. |  -  |
| **422** | A group of errors that show input errors about the parameters provided in the request. |  -  |

<a id="deletePendingUserProvision"></a>
# **deletePendingUserProvision**
> DeletePendingUserProvision200Response deletePendingUserProvision(orgId)

Delete pending user provision



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganizationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.snyk.io/v1");

    OrganizationsApi apiInstance = new OrganizationsApi(defaultClient);
    String orgId = "25065eb1-109c-4c3e-9503-68fc56ef6f44"; // String | The organization ID.
    try {
      DeletePendingUserProvision200Response result = apiInstance.deletePendingUserProvision(orgId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganizationsApi#deletePendingUserProvision");
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
| **orgId** | **String**| The organization ID. | |

### Return type

[**DeletePendingUserProvision200Response**](DeletePendingUserProvision200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **403** | Provided &#x60;API_KEY&#x60; has no user provision permission or does not have permissions in role being provisioned. |  -  |

<a id="inviteUsers"></a>
# **inviteUsers**
> inviteUsers(orgId, inviteUsersRequest)

Invite users



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganizationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.snyk.io/v1");

    OrganizationsApi apiInstance = new OrganizationsApi(defaultClient);
    String orgId = "4a18d42f-0706-4ad0-b127-24078731fbed"; // String | The organization ID. The `API_KEY` must have admin access to this organization.
    InviteUsersRequest inviteUsersRequest = new InviteUsersRequest(); // InviteUsersRequest | 
    try {
      apiInstance.inviteUsers(orgId, inviteUsersRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganizationsApi#inviteUsers");
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
| **orgId** | **String**| The organization ID. The &#x60;API_KEY&#x60; must have admin access to this organization. | |
| **inviteUsersRequest** | [**InviteUsersRequest**](InviteUsersRequest.md)|  | [optional] |

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

<a id="listAllTheOrganizationsAUserBelongsTo"></a>
# **listAllTheOrganizationsAUserBelongsTo**
> listAllTheOrganizationsAUserBelongsTo()

List all the organizations a user belongs to



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganizationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.snyk.io/v1");

    OrganizationsApi apiInstance = new OrganizationsApi(defaultClient);
    try {
      apiInstance.listAllTheOrganizationsAUserBelongsTo();
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganizationsApi#listAllTheOrganizationsAUserBelongsTo");
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

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listMembers"></a>
# **listMembers**
> List&lt;Object&gt; listMembers(orgId, includeGroupAdmins)

List Members



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganizationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.snyk.io/v1");

    OrganizationsApi apiInstance = new OrganizationsApi(defaultClient);
    String orgId = "4a18d42f-0706-4ad0-b127-24078731fbed"; // String | The organization ID.
    Boolean includeGroupAdmins = false; // Boolean | Include group administrators who also have access to this organization.
    try {
      List<Object> result = apiInstance.listMembers(orgId, includeGroupAdmins);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganizationsApi#listMembers");
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
| **orgId** | **String**| The organization ID. | |
| **includeGroupAdmins** | **Boolean**| Include group administrators who also have access to this organization. | [optional] [default to false] |

### Return type

**List&lt;Object&gt;**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listPendingUserProvisions"></a>
# **listPendingUserProvisions**
> List&lt;Object&gt; listPendingUserProvisions(orgId)

List pending user provisions



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganizationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.snyk.io/v1");

    OrganizationsApi apiInstance = new OrganizationsApi(defaultClient);
    String orgId = "25065eb1-109c-4c3e-9503-68fc56ef6f44"; // String | The organization ID.
    try {
      List<Object> result = apiInstance.listPendingUserProvisions(orgId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganizationsApi#listPendingUserProvisions");
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
| **orgId** | **String**| The organization ID. | |

### Return type

**List&lt;Object&gt;**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **403** | Provided &#x60;API_KEY&#x60; has no user provision permission or does not have permissions in role being provisioned. |  -  |

<a id="orgOrgIdNotificationSettingsGet"></a>
# **orgOrgIdNotificationSettingsGet**
> OrgOrgIdNotificationSettingsGet200Response orgOrgIdNotificationSettingsGet(orgId)

Get organization notification settings



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganizationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.snyk.io/v1");

    OrganizationsApi apiInstance = new OrganizationsApi(defaultClient);
    String orgId = "4a18d42f-0706-4ad0-b127-24078731fbed"; // String | The organization ID. The `API_KEY` must have access to this organization.
    try {
      OrgOrgIdNotificationSettingsGet200Response result = apiInstance.orgOrgIdNotificationSettingsGet(orgId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganizationsApi#orgOrgIdNotificationSettingsGet");
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

<a id="provisionAUserToTheOrganization"></a>
# **provisionAUserToTheOrganization**
> ProvisionAUserToTheOrganization200Response provisionAUserToTheOrganization(orgId, provisionAUserToTheOrganizationRequest)

Provision a user to the organization



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganizationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.snyk.io/v1");

    OrganizationsApi apiInstance = new OrganizationsApi(defaultClient);
    String orgId = "25065eb1-109c-4c3e-9503-68fc56ef6f44"; // String | The organization ID. The `API_KEY` must not exceed the permissions being granted to the provisioned user.
    ProvisionAUserToTheOrganizationRequest provisionAUserToTheOrganizationRequest = new ProvisionAUserToTheOrganizationRequest(); // ProvisionAUserToTheOrganizationRequest | 
    try {
      ProvisionAUserToTheOrganization200Response result = apiInstance.provisionAUserToTheOrganization(orgId, provisionAUserToTheOrganizationRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganizationsApi#provisionAUserToTheOrganization");
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
| **orgId** | **String**| The organization ID. The &#x60;API_KEY&#x60; must not exceed the permissions being granted to the provisioned user. | |
| **provisionAUserToTheOrganizationRequest** | [**ProvisionAUserToTheOrganizationRequest**](ProvisionAUserToTheOrganizationRequest.md)|  | [optional] |

### Return type

[**ProvisionAUserToTheOrganization200Response**](ProvisionAUserToTheOrganization200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **403** | Provided &#x60;API_KEY&#x60; has no user provision permission or does not have permissions in role being provisioned. |  -  |

<a id="removeAMemberFromTheOrganization"></a>
# **removeAMemberFromTheOrganization**
> removeAMemberFromTheOrganization(orgId, userId)

Remove a member from the organization



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganizationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.snyk.io/v1");

    OrganizationsApi apiInstance = new OrganizationsApi(defaultClient);
    String orgId = "4a18d42f-0706-4ad0-b127-24078731fbed"; // String | The organization ID. The `API_KEY` must admin have access to this organization.
    String userId = "4a18d42f-0706-4ad0-b127-24078731fbed"; // String | The user ID we want to remove.
    try {
      apiInstance.removeAMemberFromTheOrganization(orgId, userId);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganizationsApi#removeAMemberFromTheOrganization");
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
| **orgId** | **String**| The organization ID. The &#x60;API_KEY&#x60; must admin have access to this organization. | |
| **userId** | **String**| The user ID we want to remove. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="removeOrganization"></a>
# **removeOrganization**
> removeOrganization(orgId)

Remove organization



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganizationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.snyk.io/v1");

    OrganizationsApi apiInstance = new OrganizationsApi(defaultClient);
    String orgId = "4a18d42f-0706-4ad0-b127-24078731fbed"; // String | The organization ID. The `API_KEY` must have permission to delete the provided organization. Currently this operation is only supported for organizations without any projects.
    try {
      apiInstance.removeOrganization(orgId);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganizationsApi#removeOrganization");
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
| **orgId** | **String**| The organization ID. The &#x60;API_KEY&#x60; must have permission to delete the provided organization. Currently this operation is only supported for organizations without any projects. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |

<a id="setNotificationSettings"></a>
# **setNotificationSettings**
> OrgOrgIdNotificationSettingsGet200Response setNotificationSettings(orgId, setNotificationSettingsRequest)

Set notification settings



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganizationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.snyk.io/v1");

    OrganizationsApi apiInstance = new OrganizationsApi(defaultClient);
    String orgId = "orgId_example"; // String | Automatically added
    SetNotificationSettingsRequest setNotificationSettingsRequest = new SetNotificationSettingsRequest(); // SetNotificationSettingsRequest | 
    try {
      OrgOrgIdNotificationSettingsGet200Response result = apiInstance.setNotificationSettings(orgId, setNotificationSettingsRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganizationsApi#setNotificationSettings");
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

<a id="updateAMemberInTheOrganization"></a>
# **updateAMemberInTheOrganization**
> updateAMemberInTheOrganization(orgId, userId, updateAMemberInTheOrganizationRequest)

Update a member in the organization



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganizationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.snyk.io/v1");

    OrganizationsApi apiInstance = new OrganizationsApi(defaultClient);
    String orgId = "4a18d42f-0706-4ad0-b127-24078731fbed"; // String | The organization ID. The `API_KEY` must have admin access to this organization.
    String userId = "4a18d42f-0706-4ad0-b127-24078731fbed"; // String | The user ID.
    UpdateAMemberInTheOrganizationRequest updateAMemberInTheOrganizationRequest = new UpdateAMemberInTheOrganizationRequest(); // UpdateAMemberInTheOrganizationRequest | 
    try {
      apiInstance.updateAMemberInTheOrganization(orgId, userId, updateAMemberInTheOrganizationRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganizationsApi#updateAMemberInTheOrganization");
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
| **orgId** | **String**| The organization ID. The &#x60;API_KEY&#x60; must have admin access to this organization. | |
| **userId** | **String**| The user ID. | |
| **updateAMemberInTheOrganizationRequest** | [**UpdateAMemberInTheOrganizationRequest**](UpdateAMemberInTheOrganizationRequest.md)|  | [optional] |

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

<a id="updateAMembersRoleInTheOrganization"></a>
# **updateAMembersRoleInTheOrganization**
> updateAMembersRoleInTheOrganization(orgId, userId, updateAMemberSRoleInTheOrganizationRequest)

Update a member&#39;s role in the organization



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganizationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.snyk.io/v1");

    OrganizationsApi apiInstance = new OrganizationsApi(defaultClient);
    String orgId = "4a18d42f-0706-4ad0-b127-24078731fbed"; // String | The organization ID. The `API_KEY` must have admin access to this organization.
    String userId = "4a18d42f-0706-4ad0-b127-24078731fbed"; // String | The user ID.
    UpdateAMemberSRoleInTheOrganizationRequest updateAMemberSRoleInTheOrganizationRequest = new UpdateAMemberSRoleInTheOrganizationRequest(); // UpdateAMemberSRoleInTheOrganizationRequest | 
    try {
      apiInstance.updateAMembersRoleInTheOrganization(orgId, userId, updateAMemberSRoleInTheOrganizationRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganizationsApi#updateAMembersRoleInTheOrganization");
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
| **orgId** | **String**| The organization ID. The &#x60;API_KEY&#x60; must have admin access to this organization. | |
| **userId** | **String**| The user ID. | |
| **updateAMemberSRoleInTheOrganizationRequest** | [**UpdateAMemberSRoleInTheOrganizationRequest**](UpdateAMemberSRoleInTheOrganizationRequest.md)|  | [optional] |

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

<a id="updateOrganizationSettings"></a>
# **updateOrganizationSettings**
> ViewOrganizationSettings200Response updateOrganizationSettings(orgId, updateOrganizationSettingsRequest)

Update organization settings

Settings that are not provided will not be modified.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganizationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.snyk.io/v1");

    OrganizationsApi apiInstance = new OrganizationsApi(defaultClient);
    String orgId = "25065eb1-109c-4c3e-9503-68fc56ef6f44"; // String | The organization ID. The `API_KEY` must have admin access to this organization.
    UpdateOrganizationSettingsRequest updateOrganizationSettingsRequest = new UpdateOrganizationSettingsRequest(); // UpdateOrganizationSettingsRequest | 
    try {
      ViewOrganizationSettings200Response result = apiInstance.updateOrganizationSettings(orgId, updateOrganizationSettingsRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganizationsApi#updateOrganizationSettings");
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
| **orgId** | **String**| The organization ID. The &#x60;API_KEY&#x60; must have admin access to this organization. | |
| **updateOrganizationSettingsRequest** | [**UpdateOrganizationSettingsRequest**](UpdateOrganizationSettingsRequest.md)|  | [optional] |

### Return type

[**ViewOrganizationSettings200Response**](ViewOrganizationSettings200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **403** | If provided a setting that the &#x60;API_KEY&#x60; has no edit permission for. |  -  |

<a id="viewOrganizationSettings"></a>
# **viewOrganizationSettings**
> ViewOrganizationSettings200Response viewOrganizationSettings(orgId)

View organization settings



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganizationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.snyk.io/v1");

    OrganizationsApi apiInstance = new OrganizationsApi(defaultClient);
    String orgId = "25065eb1-109c-4c3e-9503-68fc56ef6f44"; // String | The organization ID. The `API_KEY` must have access to this organization.
    try {
      ViewOrganizationSettings200Response result = apiInstance.viewOrganizationSettings(orgId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganizationsApi#viewOrganizationSettings");
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

[**ViewOrganizationSettings200Response**](ViewOrganizationSettings200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

