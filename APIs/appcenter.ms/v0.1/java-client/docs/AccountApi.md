# AccountApi

All URIs are relative to *https://api.appcenter.ms*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**appApiTokensDelete**](AccountApi.md#appApiTokensDelete) | **DELETE** /v0.1/apps/{owner_name}/{app_name}/api_tokens/{api_token_id} |  |
| [**appApiTokensList**](AccountApi.md#appApiTokensList) | **GET** /v0.1/apps/{owner_name}/{app_name}/api_tokens |  |
| [**appApiTokensNew**](AccountApi.md#appApiTokensNew) | **POST** /v0.1/apps/{owner_name}/{app_name}/api_tokens |  |
| [**appInvitationsAccept**](AccountApi.md#appInvitationsAccept) | **POST** /v0.1/user/invitations/apps/{invitation_token}/accept |  |
| [**appInvitationsCreate**](AccountApi.md#appInvitationsCreate) | **POST** /v0.1/apps/{owner_name}/{app_name}/invitations |  |
| [**appInvitationsCreateByEmail**](AccountApi.md#appInvitationsCreateByEmail) | **POST** /v0.1/apps/{owner_name}/{app_name}/invitations/{user_email} |  |
| [**appInvitationsDelete**](AccountApi.md#appInvitationsDelete) | **DELETE** /v0.1/apps/{owner_name}/{app_name}/invitations/{user_email} |  |
| [**appInvitationsList**](AccountApi.md#appInvitationsList) | **GET** /v0.1/apps/{owner_name}/{app_name}/invitations |  |
| [**appInvitationsReject**](AccountApi.md#appInvitationsReject) | **POST** /v0.1/user/invitations/apps/{invitation_token}/reject |  |
| [**appInvitationsUpdatePermissions**](AccountApi.md#appInvitationsUpdatePermissions) | **PATCH** /v0.1/apps/{owner_name}/{app_name}/invitations/{user_email} |  |
| [**appsCreate**](AccountApi.md#appsCreate) | **POST** /v0.1/apps |  |
| [**appsCreateForOrg**](AccountApi.md#appsCreateForOrg) | **POST** /v0.1/orgs/{org_name}/apps |  |
| [**appsDelete**](AccountApi.md#appsDelete) | **DELETE** /v0.1/apps/{owner_name}/{app_name} |  |
| [**appsDeleteAvatar**](AccountApi.md#appsDeleteAvatar) | **DELETE** /v0.1/apps/{owner_name}/{app_name}/avatar |  |
| [**appsGet**](AccountApi.md#appsGet) | **GET** /v0.1/apps/{owner_name}/{app_name} |  |
| [**appsGetForOrgUser**](AccountApi.md#appsGetForOrgUser) | **GET** /v0.1/orgs/{org_name}/users/{user_name}/apps |  |
| [**appsGetTeams**](AccountApi.md#appsGetTeams) | **GET** /v0.1/apps/{owner_name}/{app_name}/teams |  |
| [**appsList**](AccountApi.md#appsList) | **GET** /v0.1/apps |  |
| [**appsListForOrg**](AccountApi.md#appsListForOrg) | **GET** /v0.1/orgs/{org_name}/apps |  |
| [**appsListTesters**](AccountApi.md#appsListTesters) | **GET** /v0.1/apps/{owner_name}/{app_name}/testers |  |
| [**appsRemoveUser**](AccountApi.md#appsRemoveUser) | **DELETE** /v0.1/apps/{owner_name}/{app_name}/users/{user_email} |  |
| [**appsTransferOwnership**](AccountApi.md#appsTransferOwnership) | **POST** /v0.1/apps/{owner_name}/{app_name}/transfer/{destination_owner_name} |  |
| [**appsTransferToOrg**](AccountApi.md#appsTransferToOrg) | **POST** /v0.1/apps/{owner_name}/{app_name}/transfer_to_org |  |
| [**appsUpdate**](AccountApi.md#appsUpdate) | **PATCH** /v0.1/apps/{owner_name}/{app_name} |  |
| [**appsUpdateAvatar**](AccountApi.md#appsUpdateAvatar) | **POST** /v0.1/apps/{owner_name}/{app_name}/avatar |  |
| [**appsUpdateUserPermissions**](AccountApi.md#appsUpdateUserPermissions) | **PATCH** /v0.1/apps/{owner_name}/{app_name}/users/{user_email} |  |
| [**azureSubscriptionDeleteForApp**](AccountApi.md#azureSubscriptionDeleteForApp) | **DELETE** /v0.1/apps/{owner_name}/{app_name}/azure_subscriptions/{azure_subscription_id} |  |
| [**azureSubscriptionLinkForApp**](AccountApi.md#azureSubscriptionLinkForApp) | **POST** /v0.1/apps/{owner_name}/{app_name}/azure_subscriptions |  |
| [**azureSubscriptionListForApp**](AccountApi.md#azureSubscriptionListForApp) | **GET** /v0.1/apps/{owner_name}/{app_name}/azure_subscriptions |  |
| [**azureSubscriptionListForOrg**](AccountApi.md#azureSubscriptionListForOrg) | **GET** /v0.1/orgs/{org_name}/azure_subscriptions |  |
| [**azureSubscriptionListForUser**](AccountApi.md#azureSubscriptionListForUser) | **GET** /v0.1/azure_subscriptions |  |
| [**distributionGroupInvitationsAcceptAll**](AccountApi.md#distributionGroupInvitationsAcceptAll) | **POST** /v0.1/user/invitations/distribution_groups/accept |  |
| [**distributionGroupsAddApps**](AccountApi.md#distributionGroupsAddApps) | **POST** /v0.1/orgs/{org_name}/distribution_groups/{distribution_group_name}/apps |  |
| [**distributionGroupsAddUser**](AccountApi.md#distributionGroupsAddUser) | **POST** /v0.1/apps/{owner_name}/{app_name}/distribution_groups/{distribution_group_name}/members |  |
| [**distributionGroupsAddUsersForOrg**](AccountApi.md#distributionGroupsAddUsersForOrg) | **POST** /v0.1/orgs/{org_name}/distribution_groups/{distribution_group_name}/members |  |
| [**distributionGroupsBulkDeleteApps**](AccountApi.md#distributionGroupsBulkDeleteApps) | **POST** /v0.1/orgs/{org_name}/distribution_groups/{distribution_group_name}/apps/bulk_delete |  |
| [**distributionGroupsBulkDeleteUsers**](AccountApi.md#distributionGroupsBulkDeleteUsers) | **POST** /v0.1/orgs/{org_name}/distribution_groups/{distribution_group_name}/members/bulk_delete |  |
| [**distributionGroupsCreate**](AccountApi.md#distributionGroupsCreate) | **POST** /v0.1/apps/{owner_name}/{app_name}/distribution_groups |  |
| [**distributionGroupsCreateForOrg**](AccountApi.md#distributionGroupsCreateForOrg) | **POST** /v0.1/orgs/{org_name}/distribution_groups |  |
| [**distributionGroupsDelete**](AccountApi.md#distributionGroupsDelete) | **DELETE** /v0.1/apps/{owner_name}/{app_name}/distribution_groups/{distribution_group_name} |  |
| [**distributionGroupsDeleteForOrg**](AccountApi.md#distributionGroupsDeleteForOrg) | **DELETE** /v0.1/orgs/{org_name}/distribution_groups/{distribution_group_name} |  |
| [**distributionGroupsDetailsForOrg**](AccountApi.md#distributionGroupsDetailsForOrg) | **GET** /v0.1/orgs/{org_name}/distribution_groups_details |  |
| [**distributionGroupsGet**](AccountApi.md#distributionGroupsGet) | **GET** /v0.1/apps/{owner_name}/{app_name}/distribution_groups/{distribution_group_name} |  |
| [**distributionGroupsGetApps**](AccountApi.md#distributionGroupsGetApps) | **GET** /v0.1/orgs/{org_name}/distribution_groups/{distribution_group_name}/apps |  |
| [**distributionGroupsGetForOrg**](AccountApi.md#distributionGroupsGetForOrg) | **GET** /v0.1/orgs/{org_name}/distribution_groups/{distribution_group_name} |  |
| [**distributionGroupsList**](AccountApi.md#distributionGroupsList) | **GET** /v0.1/apps/{owner_name}/{app_name}/distribution_groups |  |
| [**distributionGroupsListAllTestersForOrg**](AccountApi.md#distributionGroupsListAllTestersForOrg) | **GET** /v0.1/orgs/{org_name}/testers |  |
| [**distributionGroupsListForOrg**](AccountApi.md#distributionGroupsListForOrg) | **GET** /v0.1/orgs/{org_name}/distribution_groups |  |
| [**distributionGroupsListUsers**](AccountApi.md#distributionGroupsListUsers) | **GET** /v0.1/apps/{owner_name}/{app_name}/distribution_groups/{distribution_group_name}/members |  |
| [**distributionGroupsListUsersForOrg**](AccountApi.md#distributionGroupsListUsersForOrg) | **GET** /v0.1/orgs/{org_name}/distribution_groups/{distribution_group_name}/members |  |
| [**distributionGroupsPatchForOrg**](AccountApi.md#distributionGroupsPatchForOrg) | **PATCH** /v0.1/orgs/{org_name}/distribution_groups/{distribution_group_name} |  |
| [**distributionGroupsRemoveUser**](AccountApi.md#distributionGroupsRemoveUser) | **POST** /v0.1/apps/{owner_name}/{app_name}/distribution_groups/{distribution_group_name}/members/bulk_delete |  |
| [**distributionGroupsResendInvite**](AccountApi.md#distributionGroupsResendInvite) | **POST** /v0.1/apps/{owner_name}/{app_name}/distribution_groups/{distribution_group_name}/resend_invite |  |
| [**distributionGroupsResendSharedInvite**](AccountApi.md#distributionGroupsResendSharedInvite) | **POST** /v0.1/orgs/{org_name}/distribution_groups/{distribution_group_name}/resend_invite |  |
| [**distributionGroupsUpdate**](AccountApi.md#distributionGroupsUpdate) | **PATCH** /v0.1/apps/{owner_name}/{app_name}/distribution_groups/{distribution_group_name} |  |
| [**invitationsSent**](AccountApi.md#invitationsSent) | **GET** /v0.1/invitations/sent |  |
| [**orgInvitations**](AccountApi.md#orgInvitations) | **POST** /v0.1/orgs/{org_name}/invitations/{email}/revoke |  |
| [**orgInvitationsAccept**](AccountApi.md#orgInvitationsAccept) | **POST** /v0.1/user/invitations/orgs/{invitation_token}/accept |  |
| [**orgInvitationsCreate**](AccountApi.md#orgInvitationsCreate) | **POST** /v0.1/orgs/{org_name}/invitations |  |
| [**orgInvitationsDelete**](AccountApi.md#orgInvitationsDelete) | **DELETE** /v0.1/orgs/{org_name}/invitations |  |
| [**orgInvitationsListPending**](AccountApi.md#orgInvitationsListPending) | **GET** /v0.1/orgs/{org_name}/invitations |  |
| [**orgInvitationsReject**](AccountApi.md#orgInvitationsReject) | **POST** /v0.1/user/invitations/orgs/{invitation_token}/reject |  |
| [**orgInvitationsSendNewInvitation**](AccountApi.md#orgInvitationsSendNewInvitation) | **POST** /v0.1/orgs/{org_name}/invitations/{email}/resend |  |
| [**orgInvitationsUpdate**](AccountApi.md#orgInvitationsUpdate) | **PATCH** /v0.1/orgs/{org_name}/invitations/{email} |  |
| [**organizationDeleteAvatar**](AccountApi.md#organizationDeleteAvatar) | **DELETE** /v0.1/orgs/{org_name}/avatar |  |
| [**organizationUpdateAvatar**](AccountApi.md#organizationUpdateAvatar) | **POST** /v0.1/orgs/{org_name}/avatar |  |
| [**organizationsCreateOrUpdate**](AccountApi.md#organizationsCreateOrUpdate) | **POST** /v0.1/orgs |  |
| [**organizationsDelete**](AccountApi.md#organizationsDelete) | **DELETE** /v0.1/orgs/{org_name} |  |
| [**organizationsGet**](AccountApi.md#organizationsGet) | **GET** /v0.1/orgs/{org_name} |  |
| [**organizationsList**](AccountApi.md#organizationsList) | **GET** /v0.1/orgs |  |
| [**organizationsListAdministered**](AccountApi.md#organizationsListAdministered) | **GET** /v0.1/administeredOrgs |  |
| [**organizationsUpdate**](AccountApi.md#organizationsUpdate) | **PATCH** /v0.1/orgs/{org_name} |  |
| [**sharedconnectionConnections**](AccountApi.md#sharedconnectionConnections) | **GET** /v0.1/user/export/serviceConnections |  |
| [**teamsAddApp**](AccountApi.md#teamsAddApp) | **POST** /v0.1/orgs/{org_name}/teams/{team_name}/apps |  |
| [**teamsAddUser**](AccountApi.md#teamsAddUser) | **POST** /v0.1/orgs/{org_name}/teams/{team_name}/users |  |
| [**teamsCreateTeam**](AccountApi.md#teamsCreateTeam) | **POST** /v0.1/orgs/{org_name}/teams |  |
| [**teamsDelete**](AccountApi.md#teamsDelete) | **DELETE** /v0.1/orgs/{org_name}/teams/{team_name} |  |
| [**teamsGetTeam**](AccountApi.md#teamsGetTeam) | **GET** /v0.1/orgs/{org_name}/teams/{team_name} |  |
| [**teamsGetUsers**](AccountApi.md#teamsGetUsers) | **GET** /v0.1/orgs/{org_name}/teams/{team_name}/users |  |
| [**teamsListAll**](AccountApi.md#teamsListAll) | **GET** /v0.1/orgs/{org_name}/teams |  |
| [**teamsListApps**](AccountApi.md#teamsListApps) | **GET** /v0.1/orgs/{org_name}/teams/{team_name}/apps |  |
| [**teamsRemoveApp**](AccountApi.md#teamsRemoveApp) | **DELETE** /v0.1/orgs/{org_name}/teams/{team_name}/apps/{app_name} |  |
| [**teamsRemoveUser**](AccountApi.md#teamsRemoveUser) | **DELETE** /v0.1/orgs/{org_name}/teams/{team_name}/users/{user_name} |  |
| [**teamsUpdate**](AccountApi.md#teamsUpdate) | **PATCH** /v0.1/orgs/{org_name}/teams/{team_name} |  |
| [**teamsUpdatePermissions**](AccountApi.md#teamsUpdatePermissions) | **PATCH** /v0.1/orgs/{org_name}/teams/{team_name}/apps/{app_name} |  |
| [**userApiTokensDelete**](AccountApi.md#userApiTokensDelete) | **DELETE** /v0.1/api_tokens/{api_token_id} |  |
| [**userApiTokensList**](AccountApi.md#userApiTokensList) | **GET** /v0.1/api_tokens |  |
| [**userApiTokensNew**](AccountApi.md#userApiTokensNew) | **POST** /v0.1/api_tokens |  |
| [**usersGet**](AccountApi.md#usersGet) | **GET** /v0.1/user |  |
| [**usersGetForOrg**](AccountApi.md#usersGetForOrg) | **GET** /v0.1/orgs/{org_name}/users/{user_name} |  |
| [**usersGetUserMetadata**](AccountApi.md#usersGetUserMetadata) | **GET** /v0.1/user/metadata/optimizely |  |
| [**usersList**](AccountApi.md#usersList) | **GET** /v0.1/apps/{owner_name}/{app_name}/users |  |
| [**usersListForOrg**](AccountApi.md#usersListForOrg) | **GET** /v0.1/orgs/{org_name}/users |  |
| [**usersRemoveFromOrg**](AccountApi.md#usersRemoveFromOrg) | **DELETE** /v0.1/orgs/{org_name}/users/{user_name} |  |
| [**usersUpdate**](AccountApi.md#usersUpdate) | **PATCH** /v0.1/user |  |
| [**usersUpdateOrgRole**](AccountApi.md#usersUpdateOrgRole) | **PATCH** /v0.1/orgs/{org_name}/users/{user_name} |  |


<a id="appApiTokensDelete"></a>
# **appApiTokensDelete**
> appApiTokensDelete(ownerName, appName, apiTokenId)



Delete the App Api Token object with the specific ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure HTTP basic authorization: Basic
    HttpBasicAuth Basic = (HttpBasicAuth) defaultClient.getAuthentication("Basic");
    Basic.setUsername("YOUR USERNAME");
    Basic.setPassword("YOUR PASSWORD");

    AccountApi apiInstance = new AccountApi(defaultClient);
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    String apiTokenId = "apiTokenId_example"; // String | The unique ID (UUID) of the api token
    try {
      apiInstance.appApiTokensDelete(ownerName, appName, apiTokenId);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#appApiTokensDelete");
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
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |
| **apiTokenId** | **String**| The unique ID (UUID) of the api token | |

### Return type

null (empty response body)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **400** | Error |  -  |
| **401** | Unauthorized |  -  |
| **404** | NotFound |  -  |

<a id="appApiTokensList"></a>
# **appApiTokensList**
> List&lt;UserApiTokensList200ResponseInner&gt; appApiTokensList(ownerName, appName)



Returns App API tokens for the app

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure HTTP basic authorization: Basic
    HttpBasicAuth Basic = (HttpBasicAuth) defaultClient.getAuthentication("Basic");
    Basic.setUsername("YOUR USERNAME");
    Basic.setPassword("YOUR PASSWORD");

    AccountApi apiInstance = new AccountApi(defaultClient);
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    try {
      List<UserApiTokensList200ResponseInner> result = apiInstance.appApiTokensList(ownerName, appName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#appApiTokensList");
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
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |

### Return type

[**List&lt;UserApiTokensList200ResponseInner&gt;**](UserApiTokensList200ResponseInner.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Error |  -  |
| **401** | Unauthorized |  -  |

<a id="appApiTokensNew"></a>
# **appApiTokensNew**
> UserApiTokensNew201Response appApiTokensNew(ownerName, appName, userApiTokensNewRequest)



Creates a new App API token

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure HTTP basic authorization: Basic
    HttpBasicAuth Basic = (HttpBasicAuth) defaultClient.getAuthentication("Basic");
    Basic.setUsername("YOUR USERNAME");
    Basic.setPassword("YOUR PASSWORD");

    AccountApi apiInstance = new AccountApi(defaultClient);
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    UserApiTokensNewRequest userApiTokensNewRequest = new UserApiTokensNewRequest(); // UserApiTokensNewRequest | Description of the token
    try {
      UserApiTokensNew201Response result = apiInstance.appApiTokensNew(ownerName, appName, userApiTokensNewRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#appApiTokensNew");
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
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |
| **userApiTokensNewRequest** | [**UserApiTokensNewRequest**](UserApiTokensNewRequest.md)| Description of the token | [optional] |

### Return type

[**UserApiTokensNew201Response**](UserApiTokensNew201Response.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Success |  -  |
| **400** | Error |  -  |
| **401** | Unauthorized |  -  |

<a id="appInvitationsAccept"></a>
# **appInvitationsAccept**
> appInvitationsAccept(invitationToken, body)



Accepts a pending invitation for the specified user

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    AccountApi apiInstance = new AccountApi(defaultClient);
    String invitationToken = "invitationToken_example"; // String | The app invitation token that was sent to the user
    Object body = null; // Object | allow empty body for custom http-client lib
    try {
      apiInstance.appInvitationsAccept(invitationToken, body);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#appInvitationsAccept");
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
| **invitationToken** | **String**| The app invitation token that was sent to the user | |
| **body** | **Object**| allow empty body for custom http-client lib | [optional] |

### Return type

null (empty response body)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **0** | Error |  -  |

<a id="appInvitationsCreate"></a>
# **appInvitationsCreate**
> appInvitationsCreate(ownerName, appName, appInvitationsCreateRequest)



Invites a new or existing user to an app

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    AccountApi apiInstance = new AccountApi(defaultClient);
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    AppInvitationsCreateRequest appInvitationsCreateRequest = new AppInvitationsCreateRequest(); // AppInvitationsCreateRequest | The email of the user to invite
    try {
      apiInstance.appInvitationsCreate(ownerName, appName, appInvitationsCreateRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#appInvitationsCreate");
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
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |
| **appInvitationsCreateRequest** | [**AppInvitationsCreateRequest**](AppInvitationsCreateRequest.md)| The email of the user to invite | [optional] |

### Return type

null (empty response body)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **0** | Error |  -  |

<a id="appInvitationsCreateByEmail"></a>
# **appInvitationsCreateByEmail**
> appInvitationsCreateByEmail(ownerName, appName, userEmail, appInvitationsCreateByEmailRequest)



Invites a new or existing user to an app

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    AccountApi apiInstance = new AccountApi(defaultClient);
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    String userEmail = "userEmail_example"; // String | The email of the user to invite
    AppInvitationsCreateByEmailRequest appInvitationsCreateByEmailRequest = new AppInvitationsCreateByEmailRequest(); // AppInvitationsCreateByEmailRequest | The role of the user to be added
    try {
      apiInstance.appInvitationsCreateByEmail(ownerName, appName, userEmail, appInvitationsCreateByEmailRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#appInvitationsCreateByEmail");
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
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |
| **userEmail** | **String**| The email of the user to invite | |
| **appInvitationsCreateByEmailRequest** | [**AppInvitationsCreateByEmailRequest**](AppInvitationsCreateByEmailRequest.md)| The role of the user to be added | [optional] |

### Return type

null (empty response body)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **0** | Error |  -  |

<a id="appInvitationsDelete"></a>
# **appInvitationsDelete**
> appInvitationsDelete(ownerName, appName, userEmail)



Removes a user&#39;s invitation to an app

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    AccountApi apiInstance = new AccountApi(defaultClient);
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    String userEmail = "userEmail_example"; // String | The email of the user to invite
    try {
      apiInstance.appInvitationsDelete(ownerName, appName, userEmail);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#appInvitationsDelete");
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
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |
| **userEmail** | **String**| The email of the user to invite | |

### Return type

null (empty response body)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **0** | Error |  -  |

<a id="appInvitationsList"></a>
# **appInvitationsList**
> AppInvitationsList200Response appInvitationsList(ownerName, appName)



Gets the pending invitations for the app

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    AccountApi apiInstance = new AccountApi(defaultClient);
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    try {
      AppInvitationsList200Response result = apiInstance.appInvitationsList(ownerName, appName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#appInvitationsList");
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
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |

### Return type

[**AppInvitationsList200Response**](AppInvitationsList200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **0** | Error |  -  |

<a id="appInvitationsReject"></a>
# **appInvitationsReject**
> appInvitationsReject(invitationToken, body)



Rejects a pending invitation for the specified user

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    AccountApi apiInstance = new AccountApi(defaultClient);
    String invitationToken = "invitationToken_example"; // String | The app invitation token that was sent to the user
    Object body = null; // Object | allow empty body for custom http-client lib
    try {
      apiInstance.appInvitationsReject(invitationToken, body);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#appInvitationsReject");
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
| **invitationToken** | **String**| The app invitation token that was sent to the user | |
| **body** | **Object**| allow empty body for custom http-client lib | [optional] |

### Return type

null (empty response body)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **0** | Error |  -  |

<a id="appInvitationsUpdatePermissions"></a>
# **appInvitationsUpdatePermissions**
> appInvitationsUpdatePermissions(ownerName, appName, userEmail, appInvitationsUpdatePermissionsRequest)



Update pending invitation permission

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    AccountApi apiInstance = new AccountApi(defaultClient);
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    String userEmail = "userEmail_example"; // String | The email of the user to invite
    AppInvitationsUpdatePermissionsRequest appInvitationsUpdatePermissionsRequest = new AppInvitationsUpdatePermissionsRequest(); // AppInvitationsUpdatePermissionsRequest | The value to update the user permission in the invite.
    try {
      apiInstance.appInvitationsUpdatePermissions(ownerName, appName, userEmail, appInvitationsUpdatePermissionsRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#appInvitationsUpdatePermissions");
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
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |
| **userEmail** | **String**| The email of the user to invite | |
| **appInvitationsUpdatePermissionsRequest** | [**AppInvitationsUpdatePermissionsRequest**](AppInvitationsUpdatePermissionsRequest.md)| The value to update the user permission in the invite. | |

### Return type

null (empty response body)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **0** | Error |  -  |

<a id="appsCreate"></a>
# **appsCreate**
> AppsList200ResponseInner appsCreate(appsCreateRequest)



Creates a new app and returns it to the caller

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    AccountApi apiInstance = new AccountApi(defaultClient);
    AppsCreateRequest appsCreateRequest = new AppsCreateRequest(); // AppsCreateRequest | The data for the app
    try {
      AppsList200ResponseInner result = apiInstance.appsCreate(appsCreateRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#appsCreate");
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
| **appsCreateRequest** | [**AppsCreateRequest**](AppsCreateRequest.md)| The data for the app | |

### Return type

[**AppsList200ResponseInner**](AppsList200ResponseInner.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Success |  -  |
| **0** | Error |  -  |

<a id="appsCreateForOrg"></a>
# **appsCreateForOrg**
> AppsList200ResponseInner appsCreateForOrg(orgName, appsCreateRequest)



Creates a new app for the organization and returns it to the caller

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    AccountApi apiInstance = new AccountApi(defaultClient);
    String orgName = "orgName_example"; // String | The organization's name
    AppsCreateRequest appsCreateRequest = new AppsCreateRequest(); // AppsCreateRequest | The data for the app
    try {
      AppsList200ResponseInner result = apiInstance.appsCreateForOrg(orgName, appsCreateRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#appsCreateForOrg");
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
| **orgName** | **String**| The organization&#39;s name | |
| **appsCreateRequest** | [**AppsCreateRequest**](AppsCreateRequest.md)| The data for the app | |

### Return type

[**AppsList200ResponseInner**](AppsList200ResponseInner.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **201** | Success |  -  |
| **0** | Error |  -  |

<a id="appsDelete"></a>
# **appsDelete**
> appsDelete(appName, ownerName)



Delete an app

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    AccountApi apiInstance = new AccountApi(defaultClient);
    String appName = "appName_example"; // String | The name of the application
    String ownerName = "ownerName_example"; // String | The name of the owner
    try {
      apiInstance.appsDelete(appName, ownerName);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#appsDelete");
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
| **appName** | **String**| The name of the application | |
| **ownerName** | **String**| The name of the owner | |

### Return type

null (empty response body)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **0** | Error |  -  |

<a id="appsDeleteAvatar"></a>
# **appsDeleteAvatar**
> AppsList200ResponseInner appsDeleteAvatar(ownerName, appName)



Deletes the uploaded app avatar

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    AccountApi apiInstance = new AccountApi(defaultClient);
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    try {
      AppsList200ResponseInner result = apiInstance.appsDeleteAvatar(ownerName, appName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#appsDeleteAvatar");
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
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |

### Return type

[**AppsList200ResponseInner**](AppsList200ResponseInner.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **0** | Error |  -  |

<a id="appsGet"></a>
# **appsGet**
> AppsList200ResponseInner appsGet(ownerName, appName)



Return a specific app with the given app name which belongs to the given owner.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    AccountApi apiInstance = new AccountApi(defaultClient);
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    try {
      AppsList200ResponseInner result = apiInstance.appsGet(ownerName, appName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#appsGet");
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
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |

### Return type

[**AppsList200ResponseInner**](AppsList200ResponseInner.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **0** | Error |  -  |

<a id="appsGetForOrgUser"></a>
# **appsGetForOrgUser**
> List&lt;AppsList200ResponseInner&gt; appsGetForOrgUser(orgName, userName)



Get a user apps information from an organization by name

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    AccountApi apiInstance = new AccountApi(defaultClient);
    String orgName = "orgName_example"; // String | The organization's name
    String userName = "userName_example"; // String | The slug name of the user
    try {
      List<AppsList200ResponseInner> result = apiInstance.appsGetForOrgUser(orgName, userName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#appsGetForOrgUser");
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
| **orgName** | **String**| The organization&#39;s name | |
| **userName** | **String**| The slug name of the user | |

### Return type

[**List&lt;AppsList200ResponseInner&gt;**](AppsList200ResponseInner.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **0** | Error |  -  |

<a id="appsGetTeams"></a>
# **appsGetTeams**
> List&lt;AppsGetTeams200ResponseInner&gt; appsGetTeams(appName, ownerName)



Returns the details of all teams that have access to the app.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    AccountApi apiInstance = new AccountApi(defaultClient);
    String appName = "appName_example"; // String | The name of the application
    String ownerName = "ownerName_example"; // String | The name of the owner
    try {
      List<AppsGetTeams200ResponseInner> result = apiInstance.appsGetTeams(appName, ownerName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#appsGetTeams");
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
| **appName** | **String**| The name of the application | |
| **ownerName** | **String**| The name of the owner | |

### Return type

[**List&lt;AppsGetTeams200ResponseInner&gt;**](AppsGetTeams200ResponseInner.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **0** | Error |  -  |

<a id="appsList"></a>
# **appsList**
> List&lt;AppsList200ResponseInner&gt; appsList($orderBy)



Returns a list of apps

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    AccountApi apiInstance = new AccountApi(defaultClient);
    String $orderBy = "display_name"; // String | The name of the attribute by which to order the response by. By default, apps are in order of creation. All results are ordered in ascending order.
    try {
      List<AppsList200ResponseInner> result = apiInstance.appsList($orderBy);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#appsList");
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
| **$orderBy** | **String**| The name of the attribute by which to order the response by. By default, apps are in order of creation. All results are ordered in ascending order. | [optional] [enum: display_name, name] |

### Return type

[**List&lt;AppsList200ResponseInner&gt;**](AppsList200ResponseInner.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **0** | Error |  -  |

<a id="appsListForOrg"></a>
# **appsListForOrg**
> List&lt;AppsList200ResponseInner&gt; appsListForOrg(orgName)



Returns a list of apps for the organization

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    AccountApi apiInstance = new AccountApi(defaultClient);
    String orgName = "orgName_example"; // String | The organization's name
    try {
      List<AppsList200ResponseInner> result = apiInstance.appsListForOrg(orgName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#appsListForOrg");
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
| **orgName** | **String**| The organization&#39;s name | |

### Return type

[**List&lt;AppsList200ResponseInner&gt;**](AppsList200ResponseInner.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **0** | Error |  -  |

<a id="appsListTesters"></a>
# **appsListTesters**
> List&lt;AppInvitationsList200ResponseInvitedBy&gt; appsListTesters(ownerName, appName)



Returns the testers associated with the app specified with the given app name which belongs to the given owner.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    AccountApi apiInstance = new AccountApi(defaultClient);
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    try {
      List<AppInvitationsList200ResponseInvitedBy> result = apiInstance.appsListTesters(ownerName, appName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#appsListTesters");
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
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |

### Return type

[**List&lt;AppInvitationsList200ResponseInvitedBy&gt;**](AppInvitationsList200ResponseInvitedBy.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **0** | Error |  -  |

<a id="appsRemoveUser"></a>
# **appsRemoveUser**
> appsRemoveUser(ownerName, appName, userEmail)



Removes the user from the app

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    AccountApi apiInstance = new AccountApi(defaultClient);
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    String userEmail = "userEmail_example"; // String | The user email of the user to delete
    try {
      apiInstance.appsRemoveUser(ownerName, appName, userEmail);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#appsRemoveUser");
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
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |
| **userEmail** | **String**| The user email of the user to delete | |

### Return type

null (empty response body)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **0** | BadRequest |  -  |

<a id="appsTransferOwnership"></a>
# **appsTransferOwnership**
> AppsList200ResponseInner appsTransferOwnership(ownerName, appName, destinationOwnerName, body)



Transfers ownership of an app to a different user or organization

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    AccountApi apiInstance = new AccountApi(defaultClient);
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    String destinationOwnerName = "destinationOwnerName_example"; // String | The name of the owner (user or organization) to which the app is being transferred
    Object body = null; // Object | allow empty body for custom http-client lib
    try {
      AppsList200ResponseInner result = apiInstance.appsTransferOwnership(ownerName, appName, destinationOwnerName, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#appsTransferOwnership");
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
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |
| **destinationOwnerName** | **String**| The name of the owner (user or organization) to which the app is being transferred | |
| **body** | **Object**| allow empty body for custom http-client lib | [optional] |

### Return type

[**AppsList200ResponseInner**](AppsList200ResponseInner.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json, application/octet-stream
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **0** | Error |  -  |

<a id="appsTransferToOrg"></a>
# **appsTransferToOrg**
> OrganizationsListAdministered200ResponseOrganizations appsTransferToOrg(ownerName, appName, body)



Transfers ownership of an app to a new organization

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    AccountApi apiInstance = new AccountApi(defaultClient);
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    Object body = null; // Object | allow empty body for custom http-client lib
    try {
      OrganizationsListAdministered200ResponseOrganizations result = apiInstance.appsTransferToOrg(ownerName, appName, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#appsTransferToOrg");
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
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |
| **body** | **Object**| allow empty body for custom http-client lib | [optional] |

### Return type

[**OrganizationsListAdministered200ResponseOrganizations**](OrganizationsListAdministered200ResponseOrganizations.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **0** | Error |  -  |

<a id="appsUpdate"></a>
# **appsUpdate**
> AppsList200ResponseInner appsUpdate(appName, ownerName, appsUpdateRequest)



Partially updates a single app

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    AccountApi apiInstance = new AccountApi(defaultClient);
    String appName = "appName_example"; // String | The name of the application
    String ownerName = "ownerName_example"; // String | The name of the owner
    AppsUpdateRequest appsUpdateRequest = new AppsUpdateRequest(); // AppsUpdateRequest | The partial data for the app
    try {
      AppsList200ResponseInner result = apiInstance.appsUpdate(appName, ownerName, appsUpdateRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#appsUpdate");
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
| **appName** | **String**| The name of the application | |
| **ownerName** | **String**| The name of the owner | |
| **appsUpdateRequest** | [**AppsUpdateRequest**](AppsUpdateRequest.md)| The partial data for the app | [optional] |

### Return type

[**AppsList200ResponseInner**](AppsList200ResponseInner.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **0** | BadRequest |  -  |

<a id="appsUpdateAvatar"></a>
# **appsUpdateAvatar**
> AppsList200ResponseInner appsUpdateAvatar(ownerName, appName, avatar)



Sets the app avatar

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    AccountApi apiInstance = new AccountApi(defaultClient);
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    File avatar = new File("/path/to/file"); // File | The image for an app avatar to upload.
    try {
      AppsList200ResponseInner result = apiInstance.appsUpdateAvatar(ownerName, appName, avatar);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#appsUpdateAvatar");
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
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |
| **avatar** | **File**| The image for an app avatar to upload. | [optional] |

### Return type

[**AppsList200ResponseInner**](AppsList200ResponseInner.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **0** | Error |  -  |

<a id="appsUpdateUserPermissions"></a>
# **appsUpdateUserPermissions**
> appsUpdateUserPermissions(ownerName, appName, userEmail, appsUpdateUserPermissionsRequest)



Update user permission for the app

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    AccountApi apiInstance = new AccountApi(defaultClient);
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    String userEmail = "userEmail_example"; // String | The user email of the user to patch
    AppsUpdateUserPermissionsRequest appsUpdateUserPermissionsRequest = new AppsUpdateUserPermissionsRequest(); // AppsUpdateUserPermissionsRequest | The value to update the user permission for the app.
    try {
      apiInstance.appsUpdateUserPermissions(ownerName, appName, userEmail, appsUpdateUserPermissionsRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#appsUpdateUserPermissions");
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
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |
| **userEmail** | **String**| The user email of the user to patch | |
| **appsUpdateUserPermissionsRequest** | [**AppsUpdateUserPermissionsRequest**](AppsUpdateUserPermissionsRequest.md)| The value to update the user permission for the app. | |

### Return type

null (empty response body)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **0** | BadRequest |  -  |

<a id="azureSubscriptionDeleteForApp"></a>
# **azureSubscriptionDeleteForApp**
> azureSubscriptionDeleteForApp(azureSubscriptionId, ownerName, appName)



Delete the azure subscriptions for the app

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    AccountApi apiInstance = new AccountApi(defaultClient);
    UUID azureSubscriptionId = UUID.randomUUID(); // UUID | The unique ID (UUID) of the azure subscription
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    try {
      apiInstance.azureSubscriptionDeleteForApp(azureSubscriptionId, ownerName, appName);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#azureSubscriptionDeleteForApp");
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
| **azureSubscriptionId** | **UUID**| The unique ID (UUID) of the azure subscription | |
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |

### Return type

null (empty response body)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **0** | Error |  -  |

<a id="azureSubscriptionLinkForApp"></a>
# **azureSubscriptionLinkForApp**
> azureSubscriptionLinkForApp(ownerName, appName, azureSubscriptionLinkForAppRequest)



Link azure subscription to an app

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    AccountApi apiInstance = new AccountApi(defaultClient);
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    AzureSubscriptionLinkForAppRequest azureSubscriptionLinkForAppRequest = new AzureSubscriptionLinkForAppRequest(); // AzureSubscriptionLinkForAppRequest | The azure subscription data needed to be link to the app.
    try {
      apiInstance.azureSubscriptionLinkForApp(ownerName, appName, azureSubscriptionLinkForAppRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#azureSubscriptionLinkForApp");
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
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |
| **azureSubscriptionLinkForAppRequest** | [**AzureSubscriptionLinkForAppRequest**](AzureSubscriptionLinkForAppRequest.md)| The azure subscription data needed to be link to the app. | |

### Return type

null (empty response body)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **0** | Error |  -  |

<a id="azureSubscriptionListForApp"></a>
# **azureSubscriptionListForApp**
> List&lt;AppsList200ResponseInnerAllOfAzureSubscription&gt; azureSubscriptionListForApp(ownerName, appName)



Returns a list of azure subscriptions for the app

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    AccountApi apiInstance = new AccountApi(defaultClient);
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    try {
      List<AppsList200ResponseInnerAllOfAzureSubscription> result = apiInstance.azureSubscriptionListForApp(ownerName, appName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#azureSubscriptionListForApp");
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
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |

### Return type

[**List&lt;AppsList200ResponseInnerAllOfAzureSubscription&gt;**](AppsList200ResponseInnerAllOfAzureSubscription.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **0** | Error |  -  |

<a id="azureSubscriptionListForOrg"></a>
# **azureSubscriptionListForOrg**
> List&lt;AppsList200ResponseInnerAllOfAzureSubscription&gt; azureSubscriptionListForOrg(orgName)



Returns a list of azure subscriptions for the organization

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    AccountApi apiInstance = new AccountApi(defaultClient);
    String orgName = "orgName_example"; // String | The organization's name
    try {
      List<AppsList200ResponseInnerAllOfAzureSubscription> result = apiInstance.azureSubscriptionListForOrg(orgName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#azureSubscriptionListForOrg");
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
| **orgName** | **String**| The organization&#39;s name | |

### Return type

[**List&lt;AppsList200ResponseInnerAllOfAzureSubscription&gt;**](AppsList200ResponseInnerAllOfAzureSubscription.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **0** | Error |  -  |

<a id="azureSubscriptionListForUser"></a>
# **azureSubscriptionListForUser**
> List&lt;AppsList200ResponseInnerAllOfAzureSubscription&gt; azureSubscriptionListForUser()



Returns a list of azure subscriptions for the user

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    AccountApi apiInstance = new AccountApi(defaultClient);
    try {
      List<AppsList200ResponseInnerAllOfAzureSubscription> result = apiInstance.azureSubscriptionListForUser();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#azureSubscriptionListForUser");
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

[**List&lt;AppsList200ResponseInnerAllOfAzureSubscription&gt;**](AppsList200ResponseInnerAllOfAzureSubscription.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **0** | BadRequest |  -  |

<a id="distributionGroupInvitationsAcceptAll"></a>
# **distributionGroupInvitationsAcceptAll**
> distributionGroupInvitationsAcceptAll(body)



Accepts all pending invitations to distribution groups for the specified user

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    AccountApi apiInstance = new AccountApi(defaultClient);
    Object body = null; // Object | allow empty body for custom http-client lib
    try {
      apiInstance.distributionGroupInvitationsAcceptAll(body);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#distributionGroupInvitationsAcceptAll");
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
| **body** | **Object**| allow empty body for custom http-client lib | [optional] |

### Return type

null (empty response body)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **0** | Error |  -  |

<a id="distributionGroupsAddApps"></a>
# **distributionGroupsAddApps**
> distributionGroupsAddApps(orgName, distributionGroupName, distributionGroupsAddAppsRequest)



Add apps to distribution group in an org

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    AccountApi apiInstance = new AccountApi(defaultClient);
    String orgName = "orgName_example"; // String | The organization's name
    String distributionGroupName = "distributionGroupName_example"; // String | The name of the distribution group
    DistributionGroupsAddAppsRequest distributionGroupsAddAppsRequest = new DistributionGroupsAddAppsRequest(); // DistributionGroupsAddAppsRequest | The name of the apps to be added to the distribution group. The apps have to be owned by the organization.
    try {
      apiInstance.distributionGroupsAddApps(orgName, distributionGroupName, distributionGroupsAddAppsRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#distributionGroupsAddApps");
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
| **orgName** | **String**| The organization&#39;s name | |
| **distributionGroupName** | **String**| The name of the distribution group | |
| **distributionGroupsAddAppsRequest** | [**DistributionGroupsAddAppsRequest**](DistributionGroupsAddAppsRequest.md)| The name of the apps to be added to the distribution group. The apps have to be owned by the organization. | |

### Return type

null (empty response body)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |

<a id="distributionGroupsAddUser"></a>
# **distributionGroupsAddUser**
> List&lt;DistributionGroupsAddUser200ResponseInner&gt; distributionGroupsAddUser(ownerName, appName, distributionGroupName, distributionGroupsAddUserRequest)



Adds the members to the specified distribution group

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    AccountApi apiInstance = new AccountApi(defaultClient);
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    String distributionGroupName = "distributionGroupName_example"; // String | The name of the distribution group
    DistributionGroupsAddUserRequest distributionGroupsAddUserRequest = new DistributionGroupsAddUserRequest(); // DistributionGroupsAddUserRequest | The list of members to add
    try {
      List<DistributionGroupsAddUser200ResponseInner> result = apiInstance.distributionGroupsAddUser(ownerName, appName, distributionGroupName, distributionGroupsAddUserRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#distributionGroupsAddUser");
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
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |
| **distributionGroupName** | **String**| The name of the distribution group | |
| **distributionGroupsAddUserRequest** | [**DistributionGroupsAddUserRequest**](DistributionGroupsAddUserRequest.md)| The list of members to add | |

### Return type

[**List&lt;DistributionGroupsAddUser200ResponseInner&gt;**](DistributionGroupsAddUser200ResponseInner.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **0** | Error |  -  |

<a id="distributionGroupsAddUsersForOrg"></a>
# **distributionGroupsAddUsersForOrg**
> List&lt;DistributionGroupsAddUser200ResponseInner&gt; distributionGroupsAddUsersForOrg(orgName, distributionGroupName, distributionGroupsAddUserRequest)



Accepts an array of user email addresses to get added to the specified group

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    AccountApi apiInstance = new AccountApi(defaultClient);
    String orgName = "orgName_example"; // String | The organization's name
    String distributionGroupName = "distributionGroupName_example"; // String | The name of the distribution group
    DistributionGroupsAddUserRequest distributionGroupsAddUserRequest = new DistributionGroupsAddUserRequest(); // DistributionGroupsAddUserRequest | list of user email addresses that should get added as members to the specified group
    try {
      List<DistributionGroupsAddUser200ResponseInner> result = apiInstance.distributionGroupsAddUsersForOrg(orgName, distributionGroupName, distributionGroupsAddUserRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#distributionGroupsAddUsersForOrg");
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
| **orgName** | **String**| The organization&#39;s name | |
| **distributionGroupName** | **String**| The name of the distribution group | |
| **distributionGroupsAddUserRequest** | [**DistributionGroupsAddUserRequest**](DistributionGroupsAddUserRequest.md)| list of user email addresses that should get added as members to the specified group | |

### Return type

[**List&lt;DistributionGroupsAddUser200ResponseInner&gt;**](DistributionGroupsAddUser200ResponseInner.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **0** | Error |  -  |

<a id="distributionGroupsBulkDeleteApps"></a>
# **distributionGroupsBulkDeleteApps**
> distributionGroupsBulkDeleteApps(orgName, distributionGroupName, distributionGroupsBulkDeleteAppsRequest)



Delete apps from distribution group in an org

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    AccountApi apiInstance = new AccountApi(defaultClient);
    String orgName = "orgName_example"; // String | The organization's name
    String distributionGroupName = "distributionGroupName_example"; // String | The name of the distribution group
    DistributionGroupsBulkDeleteAppsRequest distributionGroupsBulkDeleteAppsRequest = new DistributionGroupsBulkDeleteAppsRequest(); // DistributionGroupsBulkDeleteAppsRequest | The name of the apps to be deleted from the distribution group. The apps have to be owned by the organization.
    try {
      apiInstance.distributionGroupsBulkDeleteApps(orgName, distributionGroupName, distributionGroupsBulkDeleteAppsRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#distributionGroupsBulkDeleteApps");
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
| **orgName** | **String**| The organization&#39;s name | |
| **distributionGroupName** | **String**| The name of the distribution group | |
| **distributionGroupsBulkDeleteAppsRequest** | [**DistributionGroupsBulkDeleteAppsRequest**](DistributionGroupsBulkDeleteAppsRequest.md)| The name of the apps to be deleted from the distribution group. The apps have to be owned by the organization. | |

### Return type

null (empty response body)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |

<a id="distributionGroupsBulkDeleteUsers"></a>
# **distributionGroupsBulkDeleteUsers**
> distributionGroupsBulkDeleteUsers(orgName, distributionGroupName, distributionGroupsAddUserRequest)



Delete testers from distribution group in an org

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    AccountApi apiInstance = new AccountApi(defaultClient);
    String orgName = "orgName_example"; // String | The organization's name
    String distributionGroupName = "distributionGroupName_example"; // String | The name of the distribution group
    DistributionGroupsAddUserRequest distributionGroupsAddUserRequest = new DistributionGroupsAddUserRequest(); // DistributionGroupsAddUserRequest | The list of members to add
    try {
      apiInstance.distributionGroupsBulkDeleteUsers(orgName, distributionGroupName, distributionGroupsAddUserRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#distributionGroupsBulkDeleteUsers");
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
| **orgName** | **String**| The organization&#39;s name | |
| **distributionGroupName** | **String**| The name of the distribution group | |
| **distributionGroupsAddUserRequest** | [**DistributionGroupsAddUserRequest**](DistributionGroupsAddUserRequest.md)| The list of members to add | |

### Return type

null (empty response body)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |

<a id="distributionGroupsCreate"></a>
# **distributionGroupsCreate**
> DistributionGroupsList200ResponseInner distributionGroupsCreate(ownerName, appName, distributionGroupsCreateRequest)



Creates a new distribution group and returns it to the caller

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    AccountApi apiInstance = new AccountApi(defaultClient);
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    DistributionGroupsCreateRequest distributionGroupsCreateRequest = new DistributionGroupsCreateRequest(); // DistributionGroupsCreateRequest | The attributes to update for the distribution group
    try {
      DistributionGroupsList200ResponseInner result = apiInstance.distributionGroupsCreate(ownerName, appName, distributionGroupsCreateRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#distributionGroupsCreate");
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
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |
| **distributionGroupsCreateRequest** | [**DistributionGroupsCreateRequest**](DistributionGroupsCreateRequest.md)| The attributes to update for the distribution group | |

### Return type

[**DistributionGroupsList200ResponseInner**](DistributionGroupsList200ResponseInner.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Success |  -  |
| **0** | Error |  -  |

<a id="distributionGroupsCreateForOrg"></a>
# **distributionGroupsCreateForOrg**
> DistributionGroupsList200ResponseInner distributionGroupsCreateForOrg(orgName, distributionGroupsCreateRequest)



Creates a disribution goup which can be shared across apps under an organization

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    AccountApi apiInstance = new AccountApi(defaultClient);
    String orgName = "orgName_example"; // String | The organization's name
    DistributionGroupsCreateRequest distributionGroupsCreateRequest = new DistributionGroupsCreateRequest(); // DistributionGroupsCreateRequest | The attributes to update for the distribution group
    try {
      DistributionGroupsList200ResponseInner result = apiInstance.distributionGroupsCreateForOrg(orgName, distributionGroupsCreateRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#distributionGroupsCreateForOrg");
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
| **orgName** | **String**| The organization&#39;s name | |
| **distributionGroupsCreateRequest** | [**DistributionGroupsCreateRequest**](DistributionGroupsCreateRequest.md)| The attributes to update for the distribution group | |

### Return type

[**DistributionGroupsList200ResponseInner**](DistributionGroupsList200ResponseInner.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Success |  -  |
| **0** | Error |  -  |

<a id="distributionGroupsDelete"></a>
# **distributionGroupsDelete**
> distributionGroupsDelete(appName, ownerName, distributionGroupName)



Deletes a distribution group

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    AccountApi apiInstance = new AccountApi(defaultClient);
    String appName = "appName_example"; // String | The name of the application
    String ownerName = "ownerName_example"; // String | The name of the owner
    String distributionGroupName = "distributionGroupName_example"; // String | The name of the distribution group
    try {
      apiInstance.distributionGroupsDelete(appName, ownerName, distributionGroupName);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#distributionGroupsDelete");
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
| **appName** | **String**| The name of the application | |
| **ownerName** | **String**| The name of the owner | |
| **distributionGroupName** | **String**| The name of the distribution group | |

### Return type

null (empty response body)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **0** | Error |  -  |

<a id="distributionGroupsDeleteForOrg"></a>
# **distributionGroupsDeleteForOrg**
> distributionGroupsDeleteForOrg(orgName, distributionGroupName)



Deletes a single distribution group from an org with a given distribution group name

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    AccountApi apiInstance = new AccountApi(defaultClient);
    String orgName = "orgName_example"; // String | The organization's name
    String distributionGroupName = "distributionGroupName_example"; // String | The name of the distribution group
    try {
      apiInstance.distributionGroupsDeleteForOrg(orgName, distributionGroupName);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#distributionGroupsDeleteForOrg");
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
| **orgName** | **String**| The organization&#39;s name | |
| **distributionGroupName** | **String**| The name of the distribution group | |

### Return type

null (empty response body)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **0** | Error |  -  |

<a id="distributionGroupsDetailsForOrg"></a>
# **distributionGroupsDetailsForOrg**
> List&lt;DistributionGroupsDetailsForOrg200ResponseInner&gt; distributionGroupsDetailsForOrg(orgName, appsLimit)



Returns a list of distribution groups with details for an organization

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    AccountApi apiInstance = new AccountApi(defaultClient);
    String orgName = "orgName_example"; // String | The organization's name
    BigDecimal appsLimit = new BigDecimal(78); // BigDecimal | The max number of apps to include in the response
    try {
      List<DistributionGroupsDetailsForOrg200ResponseInner> result = apiInstance.distributionGroupsDetailsForOrg(orgName, appsLimit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#distributionGroupsDetailsForOrg");
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
| **orgName** | **String**| The organization&#39;s name | |
| **appsLimit** | **BigDecimal**| The max number of apps to include in the response | [optional] |

### Return type

[**List&lt;DistributionGroupsDetailsForOrg200ResponseInner&gt;**](DistributionGroupsDetailsForOrg200ResponseInner.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **0** | Error |  -  |

<a id="distributionGroupsGet"></a>
# **distributionGroupsGet**
> DistributionGroupsList200ResponseInner distributionGroupsGet(ownerName, appName, distributionGroupName)



Returns a single distribution group for a given distribution group name

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    AccountApi apiInstance = new AccountApi(defaultClient);
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    String distributionGroupName = "distributionGroupName_example"; // String | The name of the distribution group
    try {
      DistributionGroupsList200ResponseInner result = apiInstance.distributionGroupsGet(ownerName, appName, distributionGroupName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#distributionGroupsGet");
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
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |
| **distributionGroupName** | **String**| The name of the distribution group | |

### Return type

[**DistributionGroupsList200ResponseInner**](DistributionGroupsList200ResponseInner.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **0** | Error |  -  |

<a id="distributionGroupsGetApps"></a>
# **distributionGroupsGetApps**
> List&lt;DistributionGroupsGetApps200ResponseInner&gt; distributionGroupsGetApps(orgName, distributionGroupName)



Get apps from a distribution group in an org

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    AccountApi apiInstance = new AccountApi(defaultClient);
    String orgName = "orgName_example"; // String | The organization's name
    String distributionGroupName = "distributionGroupName_example"; // String | The name of the distribution group
    try {
      List<DistributionGroupsGetApps200ResponseInner> result = apiInstance.distributionGroupsGetApps(orgName, distributionGroupName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#distributionGroupsGetApps");
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
| **orgName** | **String**| The organization&#39;s name | |
| **distributionGroupName** | **String**| The name of the distribution group | |

### Return type

[**List&lt;DistributionGroupsGetApps200ResponseInner&gt;**](DistributionGroupsGetApps200ResponseInner.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="distributionGroupsGetForOrg"></a>
# **distributionGroupsGetForOrg**
> DistributionGroupsList200ResponseInner distributionGroupsGetForOrg(orgName, distributionGroupName)



Returns a single distribution group in org for a given distribution group name

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    AccountApi apiInstance = new AccountApi(defaultClient);
    String orgName = "orgName_example"; // String | The organization's name
    String distributionGroupName = "distributionGroupName_example"; // String | The name of the distribution group
    try {
      DistributionGroupsList200ResponseInner result = apiInstance.distributionGroupsGetForOrg(orgName, distributionGroupName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#distributionGroupsGetForOrg");
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
| **orgName** | **String**| The organization&#39;s name | |
| **distributionGroupName** | **String**| The name of the distribution group | |

### Return type

[**DistributionGroupsList200ResponseInner**](DistributionGroupsList200ResponseInner.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **0** | Error |  -  |

<a id="distributionGroupsList"></a>
# **distributionGroupsList**
> List&lt;DistributionGroupsList200ResponseInner&gt; distributionGroupsList(ownerName, appName)



Returns a list of distribution groups in the app specified

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    AccountApi apiInstance = new AccountApi(defaultClient);
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    try {
      List<DistributionGroupsList200ResponseInner> result = apiInstance.distributionGroupsList(ownerName, appName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#distributionGroupsList");
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
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |

### Return type

[**List&lt;DistributionGroupsList200ResponseInner&gt;**](DistributionGroupsList200ResponseInner.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **0** | Error |  -  |

<a id="distributionGroupsListAllTestersForOrg"></a>
# **distributionGroupsListAllTestersForOrg**
> List&lt;DistributionGroupsListAllTestersForOrg200ResponseInner&gt; distributionGroupsListAllTestersForOrg(orgName)



Returns a unique list of users including the whole organization members plus testers in any shared group of that org

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    AccountApi apiInstance = new AccountApi(defaultClient);
    String orgName = "orgName_example"; // String | The organization's name
    try {
      List<DistributionGroupsListAllTestersForOrg200ResponseInner> result = apiInstance.distributionGroupsListAllTestersForOrg(orgName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#distributionGroupsListAllTestersForOrg");
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
| **orgName** | **String**| The organization&#39;s name | |

### Return type

[**List&lt;DistributionGroupsListAllTestersForOrg200ResponseInner&gt;**](DistributionGroupsListAllTestersForOrg200ResponseInner.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **0** | Error |  -  |

<a id="distributionGroupsListForOrg"></a>
# **distributionGroupsListForOrg**
> List&lt;DistributionGroupsList200ResponseInner&gt; distributionGroupsListForOrg(orgName)



Returns a list of distribution groups in the org specified

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    AccountApi apiInstance = new AccountApi(defaultClient);
    String orgName = "orgName_example"; // String | The organization's name
    try {
      List<DistributionGroupsList200ResponseInner> result = apiInstance.distributionGroupsListForOrg(orgName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#distributionGroupsListForOrg");
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
| **orgName** | **String**| The organization&#39;s name | |

### Return type

[**List&lt;DistributionGroupsList200ResponseInner&gt;**](DistributionGroupsList200ResponseInner.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Success |  -  |
| **0** | Error |  -  |

<a id="distributionGroupsListUsers"></a>
# **distributionGroupsListUsers**
> List&lt;DistributionGroupsListUsers200ResponseInner&gt; distributionGroupsListUsers(ownerName, appName, distributionGroupName, excludePendingInvitations)



Returns a list of member details in the distribution group specified

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    AccountApi apiInstance = new AccountApi(defaultClient);
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    String distributionGroupName = "distributionGroupName_example"; // String | The name of the distribution group
    Boolean excludePendingInvitations = true; // Boolean | Whether to exclude pending invitations in the response
    try {
      List<DistributionGroupsListUsers200ResponseInner> result = apiInstance.distributionGroupsListUsers(ownerName, appName, distributionGroupName, excludePendingInvitations);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#distributionGroupsListUsers");
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
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |
| **distributionGroupName** | **String**| The name of the distribution group | |
| **excludePendingInvitations** | **Boolean**| Whether to exclude pending invitations in the response | [optional] |

### Return type

[**List&lt;DistributionGroupsListUsers200ResponseInner&gt;**](DistributionGroupsListUsers200ResponseInner.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **0** | Error |  -  |

<a id="distributionGroupsListUsersForOrg"></a>
# **distributionGroupsListUsersForOrg**
> List&lt;DistributionGroupsListUsers200ResponseInner&gt; distributionGroupsListUsersForOrg(orgName, distributionGroupName)



Returns a list of member in the distribution group specified

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    AccountApi apiInstance = new AccountApi(defaultClient);
    String orgName = "orgName_example"; // String | The organization's name
    String distributionGroupName = "distributionGroupName_example"; // String | The name of the distribution group
    try {
      List<DistributionGroupsListUsers200ResponseInner> result = apiInstance.distributionGroupsListUsersForOrg(orgName, distributionGroupName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#distributionGroupsListUsersForOrg");
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
| **orgName** | **String**| The organization&#39;s name | |
| **distributionGroupName** | **String**| The name of the distribution group | |

### Return type

[**List&lt;DistributionGroupsListUsers200ResponseInner&gt;**](DistributionGroupsListUsers200ResponseInner.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **0** | Error |  -  |

<a id="distributionGroupsPatchForOrg"></a>
# **distributionGroupsPatchForOrg**
> DistributionGroupsList200ResponseInner distributionGroupsPatchForOrg(orgName, distributionGroupName, distributionGroupsUpdateRequest)



Update one given distribution group name in an org

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    AccountApi apiInstance = new AccountApi(defaultClient);
    String orgName = "orgName_example"; // String | The organization's name
    String distributionGroupName = "distributionGroupName_example"; // String | The name of the distribution group
    DistributionGroupsUpdateRequest distributionGroupsUpdateRequest = new DistributionGroupsUpdateRequest(); // DistributionGroupsUpdateRequest | The attributes to update for the distribution group
    try {
      DistributionGroupsList200ResponseInner result = apiInstance.distributionGroupsPatchForOrg(orgName, distributionGroupName, distributionGroupsUpdateRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#distributionGroupsPatchForOrg");
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
| **orgName** | **String**| The organization&#39;s name | |
| **distributionGroupName** | **String**| The name of the distribution group | |
| **distributionGroupsUpdateRequest** | [**DistributionGroupsUpdateRequest**](DistributionGroupsUpdateRequest.md)| The attributes to update for the distribution group | [optional] |

### Return type

[**DistributionGroupsList200ResponseInner**](DistributionGroupsList200ResponseInner.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **0** | Error |  -  |

<a id="distributionGroupsRemoveUser"></a>
# **distributionGroupsRemoveUser**
> List&lt;DistributionGroupsRemoveUser200ResponseInner&gt; distributionGroupsRemoveUser(ownerName, appName, distributionGroupName, distributionGroupsAddUserRequest)



Remove the users from the distribution group

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    AccountApi apiInstance = new AccountApi(defaultClient);
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    String distributionGroupName = "distributionGroupName_example"; // String | The name of the distribution group
    DistributionGroupsAddUserRequest distributionGroupsAddUserRequest = new DistributionGroupsAddUserRequest(); // DistributionGroupsAddUserRequest | The list of members to add
    try {
      List<DistributionGroupsRemoveUser200ResponseInner> result = apiInstance.distributionGroupsRemoveUser(ownerName, appName, distributionGroupName, distributionGroupsAddUserRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#distributionGroupsRemoveUser");
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
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |
| **distributionGroupName** | **String**| The name of the distribution group | |
| **distributionGroupsAddUserRequest** | [**DistributionGroupsAddUserRequest**](DistributionGroupsAddUserRequest.md)| The list of members to add | |

### Return type

[**List&lt;DistributionGroupsRemoveUser200ResponseInner&gt;**](DistributionGroupsRemoveUser200ResponseInner.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **0** | Error |  -  |

<a id="distributionGroupsResendInvite"></a>
# **distributionGroupsResendInvite**
> distributionGroupsResendInvite(ownerName, appName, distributionGroupName, distributionGroupsAddUserRequest)



Resend distribution group app invite notification to previously invited testers

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    AccountApi apiInstance = new AccountApi(defaultClient);
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    String distributionGroupName = "distributionGroupName_example"; // String | The name of the distribution group
    DistributionGroupsAddUserRequest distributionGroupsAddUserRequest = new DistributionGroupsAddUserRequest(); // DistributionGroupsAddUserRequest | The list of members to add
    try {
      apiInstance.distributionGroupsResendInvite(ownerName, appName, distributionGroupName, distributionGroupsAddUserRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#distributionGroupsResendInvite");
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
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |
| **distributionGroupName** | **String**| The name of the distribution group | |
| **distributionGroupsAddUserRequest** | [**DistributionGroupsAddUserRequest**](DistributionGroupsAddUserRequest.md)| The list of members to add | |

### Return type

null (empty response body)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **0** | Error |  -  |

<a id="distributionGroupsResendSharedInvite"></a>
# **distributionGroupsResendSharedInvite**
> distributionGroupsResendSharedInvite(orgName, distributionGroupName, distributionGroupsAddUserRequest)



Resend shared distribution group invite notification to previously invited testers

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    AccountApi apiInstance = new AccountApi(defaultClient);
    String orgName = "orgName_example"; // String | The organization's name
    String distributionGroupName = "distributionGroupName_example"; // String | The name of the distribution group
    DistributionGroupsAddUserRequest distributionGroupsAddUserRequest = new DistributionGroupsAddUserRequest(); // DistributionGroupsAddUserRequest | The list of members to add
    try {
      apiInstance.distributionGroupsResendSharedInvite(orgName, distributionGroupName, distributionGroupsAddUserRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#distributionGroupsResendSharedInvite");
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
| **orgName** | **String**| The organization&#39;s name | |
| **distributionGroupName** | **String**| The name of the distribution group | |
| **distributionGroupsAddUserRequest** | [**DistributionGroupsAddUserRequest**](DistributionGroupsAddUserRequest.md)| The list of members to add | |

### Return type

null (empty response body)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **0** | Error |  -  |

<a id="distributionGroupsUpdate"></a>
# **distributionGroupsUpdate**
> DistributionGroupsList200ResponseInner distributionGroupsUpdate(ownerName, appName, distributionGroupName, distributionGroupsUpdateRequest)



Updates the attributes of distribution group

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    AccountApi apiInstance = new AccountApi(defaultClient);
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    String distributionGroupName = "distributionGroupName_example"; // String | The name of the distribution group
    DistributionGroupsUpdateRequest distributionGroupsUpdateRequest = new DistributionGroupsUpdateRequest(); // DistributionGroupsUpdateRequest | The attributes to update for the distribution group
    try {
      DistributionGroupsList200ResponseInner result = apiInstance.distributionGroupsUpdate(ownerName, appName, distributionGroupName, distributionGroupsUpdateRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#distributionGroupsUpdate");
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
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |
| **distributionGroupName** | **String**| The name of the distribution group | |
| **distributionGroupsUpdateRequest** | [**DistributionGroupsUpdateRequest**](DistributionGroupsUpdateRequest.md)| The attributes to update for the distribution group | |

### Return type

[**DistributionGroupsList200ResponseInner**](DistributionGroupsList200ResponseInner.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **0** | Error |  -  |

<a id="invitationsSent"></a>
# **invitationsSent**
> List&lt;InvitationsSent200ResponseInner&gt; invitationsSent()



Returns all invitations sent by the caller

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    AccountApi apiInstance = new AccountApi(defaultClient);
    try {
      List<InvitationsSent200ResponseInner> result = apiInstance.invitationsSent();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#invitationsSent");
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

[**List&lt;InvitationsSent200ResponseInner&gt;**](InvitationsSent200ResponseInner.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **0** | Error |  -  |

<a id="orgInvitations"></a>
# **orgInvitations**
> orgInvitations(orgName, email, body)



Removes a user&#39;s invitation to an organization

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    AccountApi apiInstance = new AccountApi(defaultClient);
    String orgName = "orgName_example"; // String | The organization's name
    String email = "email_example"; // String | The email address of the user to send the password reset mail to.
    Object body = null; // Object | allow empty body for custom http-client lib
    try {
      apiInstance.orgInvitations(orgName, email, body);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#orgInvitations");
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
| **orgName** | **String**| The organization&#39;s name | |
| **email** | **String**| The email address of the user to send the password reset mail to. | |
| **body** | **Object**| allow empty body for custom http-client lib | [optional] |

### Return type

null (empty response body)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **0** | Error |  -  |

<a id="orgInvitationsAccept"></a>
# **orgInvitationsAccept**
> orgInvitationsAccept(invitationToken, body)



Accepts a pending organization invitation for the specified user

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    AccountApi apiInstance = new AccountApi(defaultClient);
    String invitationToken = "invitationToken_example"; // String | The app invitation token that was sent to the user
    Object body = null; // Object | allow empty body for custom http-client lib
    try {
      apiInstance.orgInvitationsAccept(invitationToken, body);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#orgInvitationsAccept");
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
| **invitationToken** | **String**| The app invitation token that was sent to the user | |
| **body** | **Object**| allow empty body for custom http-client lib | [optional] |

### Return type

null (empty response body)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **0** | Error |  -  |

<a id="orgInvitationsCreate"></a>
# **orgInvitationsCreate**
> orgInvitationsCreate(orgName, appInvitationsCreateRequest)



Invites a new or existing user to an organization

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    AccountApi apiInstance = new AccountApi(defaultClient);
    String orgName = "orgName_example"; // String | The organization's name
    AppInvitationsCreateRequest appInvitationsCreateRequest = new AppInvitationsCreateRequest(); // AppInvitationsCreateRequest | The email of the user to invite
    try {
      apiInstance.orgInvitationsCreate(orgName, appInvitationsCreateRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#orgInvitationsCreate");
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
| **orgName** | **String**| The organization&#39;s name | |
| **appInvitationsCreateRequest** | [**AppInvitationsCreateRequest**](AppInvitationsCreateRequest.md)| The email of the user to invite | |

### Return type

null (empty response body)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **0** | Error |  -  |

<a id="orgInvitationsDelete"></a>
# **orgInvitationsDelete**
> orgInvitationsDelete(orgName, orgInvitationsDeleteRequest)



Removes a user&#39;s invitation to an organization

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    AccountApi apiInstance = new AccountApi(defaultClient);
    String orgName = "orgName_example"; // String | The organization's name
    OrgInvitationsDeleteRequest orgInvitationsDeleteRequest = new OrgInvitationsDeleteRequest(); // OrgInvitationsDeleteRequest | The email of the user whose invitation should be removed
    try {
      apiInstance.orgInvitationsDelete(orgName, orgInvitationsDeleteRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#orgInvitationsDelete");
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
| **orgName** | **String**| The organization&#39;s name | |
| **orgInvitationsDeleteRequest** | [**OrgInvitationsDeleteRequest**](OrgInvitationsDeleteRequest.md)| The email of the user whose invitation should be removed | |

### Return type

null (empty response body)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **0** | Error |  -  |

<a id="orgInvitationsListPending"></a>
# **orgInvitationsListPending**
> List&lt;OrgInvitationsListPending200ResponseInner&gt; orgInvitationsListPending(orgName)



Gets the pending invitations for the organization

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    AccountApi apiInstance = new AccountApi(defaultClient);
    String orgName = "orgName_example"; // String | The organization's name
    try {
      List<OrgInvitationsListPending200ResponseInner> result = apiInstance.orgInvitationsListPending(orgName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#orgInvitationsListPending");
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
| **orgName** | **String**| The organization&#39;s name | |

### Return type

[**List&lt;OrgInvitationsListPending200ResponseInner&gt;**](OrgInvitationsListPending200ResponseInner.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **0** | Error |  -  |

<a id="orgInvitationsReject"></a>
# **orgInvitationsReject**
> orgInvitationsReject(invitationToken, body)



Rejects a pending organization invitation

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    AccountApi apiInstance = new AccountApi(defaultClient);
    String invitationToken = "invitationToken_example"; // String | The app invitation token that was sent to the user
    Object body = null; // Object | allow empty body for custom http-client lib
    try {
      apiInstance.orgInvitationsReject(invitationToken, body);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#orgInvitationsReject");
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
| **invitationToken** | **String**| The app invitation token that was sent to the user | |
| **body** | **Object**| allow empty body for custom http-client lib | [optional] |

### Return type

null (empty response body)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **0** | Error |  -  |

<a id="orgInvitationsSendNewInvitation"></a>
# **orgInvitationsSendNewInvitation**
> orgInvitationsSendNewInvitation(orgName, email, appInvitationsCreateByEmailRequest)



Cancels an existing organization invitation for the user and sends a new one

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    AccountApi apiInstance = new AccountApi(defaultClient);
    String orgName = "orgName_example"; // String | The organization's name
    String email = "email_example"; // String | The email address of the user to send the password reset mail to.
    AppInvitationsCreateByEmailRequest appInvitationsCreateByEmailRequest = new AppInvitationsCreateByEmailRequest(); // AppInvitationsCreateByEmailRequest | The role of the user to be added
    try {
      apiInstance.orgInvitationsSendNewInvitation(orgName, email, appInvitationsCreateByEmailRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#orgInvitationsSendNewInvitation");
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
| **orgName** | **String**| The organization&#39;s name | |
| **email** | **String**| The email address of the user to send the password reset mail to. | |
| **appInvitationsCreateByEmailRequest** | [**AppInvitationsCreateByEmailRequest**](AppInvitationsCreateByEmailRequest.md)| The role of the user to be added | [optional] |

### Return type

null (empty response body)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **0** | Error |  -  |

<a id="orgInvitationsUpdate"></a>
# **orgInvitationsUpdate**
> orgInvitationsUpdate(orgName, email, orgInvitationsUpdateRequest)



Allows the role of an invited user to be changed

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    AccountApi apiInstance = new AccountApi(defaultClient);
    String orgName = "orgName_example"; // String | The organization's name
    String email = "email_example"; // String | The email address of the user to send the password reset mail to.
    OrgInvitationsUpdateRequest orgInvitationsUpdateRequest = new OrgInvitationsUpdateRequest(); // OrgInvitationsUpdateRequest | The new role of the user
    try {
      apiInstance.orgInvitationsUpdate(orgName, email, orgInvitationsUpdateRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#orgInvitationsUpdate");
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
| **orgName** | **String**| The organization&#39;s name | |
| **email** | **String**| The email address of the user to send the password reset mail to. | |
| **orgInvitationsUpdateRequest** | [**OrgInvitationsUpdateRequest**](OrgInvitationsUpdateRequest.md)| The new role of the user | |

### Return type

null (empty response body)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **0** | Error |  -  |

<a id="organizationDeleteAvatar"></a>
# **organizationDeleteAvatar**
> OrganizationsListAdministered200ResponseOrganizations organizationDeleteAvatar(orgName)



Deletes the uploaded organization avatar

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    AccountApi apiInstance = new AccountApi(defaultClient);
    String orgName = "orgName_example"; // String | The organization's name
    try {
      OrganizationsListAdministered200ResponseOrganizations result = apiInstance.organizationDeleteAvatar(orgName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#organizationDeleteAvatar");
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
| **orgName** | **String**| The organization&#39;s name | |

### Return type

[**OrganizationsListAdministered200ResponseOrganizations**](OrganizationsListAdministered200ResponseOrganizations.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **0** | Error |  -  |

<a id="organizationUpdateAvatar"></a>
# **organizationUpdateAvatar**
> OrganizationsListAdministered200ResponseOrganizations organizationUpdateAvatar(orgName, avatar)



Sets the organization avatar

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    AccountApi apiInstance = new AccountApi(defaultClient);
    String orgName = "orgName_example"; // String | The organization's name
    File avatar = new File("/path/to/file"); // File | The image for an Organization avatar to upload.
    try {
      OrganizationsListAdministered200ResponseOrganizations result = apiInstance.organizationUpdateAvatar(orgName, avatar);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#organizationUpdateAvatar");
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
| **orgName** | **String**| The organization&#39;s name | |
| **avatar** | **File**| The image for an Organization avatar to upload. | [optional] |

### Return type

[**OrganizationsListAdministered200ResponseOrganizations**](OrganizationsListAdministered200ResponseOrganizations.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **0** | Error |  -  |

<a id="organizationsCreateOrUpdate"></a>
# **organizationsCreateOrUpdate**
> OrganizationsListAdministered200ResponseOrganizations organizationsCreateOrUpdate(organizationsCreateOrUpdateRequest)



Creates a new organization and returns it to the caller

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    AccountApi apiInstance = new AccountApi(defaultClient);
    OrganizationsCreateOrUpdateRequest organizationsCreateOrUpdateRequest = new OrganizationsCreateOrUpdateRequest(); // OrganizationsCreateOrUpdateRequest | The organization data
    try {
      OrganizationsListAdministered200ResponseOrganizations result = apiInstance.organizationsCreateOrUpdate(organizationsCreateOrUpdateRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#organizationsCreateOrUpdate");
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
| **organizationsCreateOrUpdateRequest** | [**OrganizationsCreateOrUpdateRequest**](OrganizationsCreateOrUpdateRequest.md)| The organization data | |

### Return type

[**OrganizationsListAdministered200ResponseOrganizations**](OrganizationsListAdministered200ResponseOrganizations.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |
| **0** | Error |  -  |

<a id="organizationsDelete"></a>
# **organizationsDelete**
> organizationsDelete(orgName)



Deletes a single organization

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    AccountApi apiInstance = new AccountApi(defaultClient);
    String orgName = "orgName_example"; // String | The organization's name
    try {
      apiInstance.organizationsDelete(orgName);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#organizationsDelete");
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
| **orgName** | **String**| The organization&#39;s name | |

### Return type

null (empty response body)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **0** | Error |  -  |

<a id="organizationsGet"></a>
# **organizationsGet**
> OrganizationsListAdministered200ResponseOrganizations organizationsGet(orgName)



Returns the details of a single organization

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    AccountApi apiInstance = new AccountApi(defaultClient);
    String orgName = "orgName_example"; // String | The organization's name
    try {
      OrganizationsListAdministered200ResponseOrganizations result = apiInstance.organizationsGet(orgName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#organizationsGet");
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
| **orgName** | **String**| The organization&#39;s name | |

### Return type

[**OrganizationsListAdministered200ResponseOrganizations**](OrganizationsListAdministered200ResponseOrganizations.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **0** | Error |  -  |

<a id="organizationsList"></a>
# **organizationsList**
> List&lt;OrganizationsList200ResponseInner&gt; organizationsList()



Returns a list of organizations the requesting user has access to

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    AccountApi apiInstance = new AccountApi(defaultClient);
    try {
      List<OrganizationsList200ResponseInner> result = apiInstance.organizationsList();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#organizationsList");
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

[**List&lt;OrganizationsList200ResponseInner&gt;**](OrganizationsList200ResponseInner.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **0** | Error |  -  |

<a id="organizationsListAdministered"></a>
# **organizationsListAdministered**
> OrganizationsListAdministered200Response organizationsListAdministered()



Returns a list organizations in which the requesting user is an admin

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    AccountApi apiInstance = new AccountApi(defaultClient);
    try {
      OrganizationsListAdministered200Response result = apiInstance.organizationsListAdministered();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#organizationsListAdministered");
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

[**OrganizationsListAdministered200Response**](OrganizationsListAdministered200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **0** | Error |  -  |

<a id="organizationsUpdate"></a>
# **organizationsUpdate**
> OrganizationsListAdministered200ResponseOrganizations organizationsUpdate(orgName, organizationsUpdateRequest)



Returns a list of organizations the requesting user has access to

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    AccountApi apiInstance = new AccountApi(defaultClient);
    String orgName = "orgName_example"; // String | The organization's name
    OrganizationsUpdateRequest organizationsUpdateRequest = new OrganizationsUpdateRequest(); // OrganizationsUpdateRequest | The data for the org
    try {
      OrganizationsListAdministered200ResponseOrganizations result = apiInstance.organizationsUpdate(orgName, organizationsUpdateRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#organizationsUpdate");
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
| **orgName** | **String**| The organization&#39;s name | |
| **organizationsUpdateRequest** | [**OrganizationsUpdateRequest**](OrganizationsUpdateRequest.md)| The data for the org | |

### Return type

[**OrganizationsListAdministered200ResponseOrganizations**](OrganizationsListAdministered200ResponseOrganizations.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **0** | Error |  -  |

<a id="sharedconnectionConnections"></a>
# **sharedconnectionConnections**
> List&lt;SharedconnectionConnections200ResponseInner&gt; sharedconnectionConnections()



Gets all service connections of the service type for GDPR export.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    AccountApi apiInstance = new AccountApi(defaultClient);
    try {
      List<SharedconnectionConnections200ResponseInner> result = apiInstance.sharedconnectionConnections();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#sharedconnectionConnections");
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

[**List&lt;SharedconnectionConnections200ResponseInner&gt;**](SharedconnectionConnections200ResponseInner.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **0** | bad_request: proper details are not provided for connection in body.  |  -  |

<a id="teamsAddApp"></a>
# **teamsAddApp**
> TeamsListApps200ResponseInner teamsAddApp(orgName, teamName, distributionGroupsAddAppsRequestAppsInner)



Adds an app to a team

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    AccountApi apiInstance = new AccountApi(defaultClient);
    String orgName = "orgName_example"; // String | The organization's name
    String teamName = "teamName_example"; // String | The team's name
    DistributionGroupsAddAppsRequestAppsInner distributionGroupsAddAppsRequestAppsInner = new DistributionGroupsAddAppsRequestAppsInner(); // DistributionGroupsAddAppsRequestAppsInner | The name of the app to be added to the team. The app has to be owned by the organization.
    try {
      TeamsListApps200ResponseInner result = apiInstance.teamsAddApp(orgName, teamName, distributionGroupsAddAppsRequestAppsInner);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#teamsAddApp");
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
| **orgName** | **String**| The organization&#39;s name | |
| **teamName** | **String**| The team&#39;s name | |
| **distributionGroupsAddAppsRequestAppsInner** | [**DistributionGroupsAddAppsRequestAppsInner**](DistributionGroupsAddAppsRequestAppsInner.md)| The name of the app to be added to the team. The app has to be owned by the organization. | |

### Return type

[**TeamsListApps200ResponseInner**](TeamsListApps200ResponseInner.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Success |  -  |
| **0** | Error |  -  |

<a id="teamsAddUser"></a>
# **teamsAddUser**
> TeamsGetUsers200Response teamsAddUser(orgName, teamName, orgInvitationsDeleteRequest)



Adds a new user to a team that is owned by an organization

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    AccountApi apiInstance = new AccountApi(defaultClient);
    String orgName = "orgName_example"; // String | The organization's name
    String teamName = "teamName_example"; // String | The team's name
    OrgInvitationsDeleteRequest orgInvitationsDeleteRequest = new OrgInvitationsDeleteRequest(); // OrgInvitationsDeleteRequest | The email of the user to add to the team
    try {
      TeamsGetUsers200Response result = apiInstance.teamsAddUser(orgName, teamName, orgInvitationsDeleteRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#teamsAddUser");
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
| **orgName** | **String**| The organization&#39;s name | |
| **teamName** | **String**| The team&#39;s name | |
| **orgInvitationsDeleteRequest** | [**OrgInvitationsDeleteRequest**](OrgInvitationsDeleteRequest.md)| The email of the user to add to the team | |

### Return type

[**TeamsGetUsers200Response**](TeamsGetUsers200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Success |  -  |
| **0** | Error |  -  |

<a id="teamsCreateTeam"></a>
# **teamsCreateTeam**
> List&lt;TeamsListAll200ResponseInner&gt; teamsCreateTeam(orgName, teamsCreateTeamRequest)



Creates a team and returns it

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    AccountApi apiInstance = new AccountApi(defaultClient);
    String orgName = "orgName_example"; // String | The organization's name
    TeamsCreateTeamRequest teamsCreateTeamRequest = new TeamsCreateTeamRequest(); // TeamsCreateTeamRequest | The information used to create the team
    try {
      List<TeamsListAll200ResponseInner> result = apiInstance.teamsCreateTeam(orgName, teamsCreateTeamRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#teamsCreateTeam");
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
| **orgName** | **String**| The organization&#39;s name | |
| **teamsCreateTeamRequest** | [**TeamsCreateTeamRequest**](TeamsCreateTeamRequest.md)| The information used to create the team | |

### Return type

[**List&lt;TeamsListAll200ResponseInner&gt;**](TeamsListAll200ResponseInner.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Success |  -  |
| **0** | Error |  -  |

<a id="teamsDelete"></a>
# **teamsDelete**
> teamsDelete(orgName, teamName)



Deletes a single team

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    AccountApi apiInstance = new AccountApi(defaultClient);
    String orgName = "orgName_example"; // String | The organization's name
    String teamName = "teamName_example"; // String | The team's name
    try {
      apiInstance.teamsDelete(orgName, teamName);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#teamsDelete");
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
| **orgName** | **String**| The organization&#39;s name | |
| **teamName** | **String**| The team&#39;s name | |

### Return type

null (empty response body)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **0** | Error |  -  |

<a id="teamsGetTeam"></a>
# **teamsGetTeam**
> TeamsListAll200ResponseInner teamsGetTeam(orgName, teamName)



Returns the details of a single team

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    AccountApi apiInstance = new AccountApi(defaultClient);
    String orgName = "orgName_example"; // String | The organization's name
    String teamName = "teamName_example"; // String | The team's name
    try {
      TeamsListAll200ResponseInner result = apiInstance.teamsGetTeam(orgName, teamName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#teamsGetTeam");
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
| **orgName** | **String**| The organization&#39;s name | |
| **teamName** | **String**| The team&#39;s name | |

### Return type

[**TeamsListAll200ResponseInner**](TeamsListAll200ResponseInner.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **0** | Error |  -  |

<a id="teamsGetUsers"></a>
# **teamsGetUsers**
> TeamsGetUsers200Response teamsGetUsers(orgName, teamName)



Returns the users of a team which is owned by an organization

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    AccountApi apiInstance = new AccountApi(defaultClient);
    String orgName = "orgName_example"; // String | The organization's name
    String teamName = "teamName_example"; // String | The team's name
    try {
      TeamsGetUsers200Response result = apiInstance.teamsGetUsers(orgName, teamName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#teamsGetUsers");
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
| **orgName** | **String**| The organization&#39;s name | |
| **teamName** | **String**| The team&#39;s name | |

### Return type

[**TeamsGetUsers200Response**](TeamsGetUsers200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **0** | Error |  -  |

<a id="teamsListAll"></a>
# **teamsListAll**
> List&lt;TeamsListAll200ResponseInner&gt; teamsListAll(orgName)



Returns the list of all teams in this org

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    AccountApi apiInstance = new AccountApi(defaultClient);
    String orgName = "orgName_example"; // String | The organization's name
    try {
      List<TeamsListAll200ResponseInner> result = apiInstance.teamsListAll(orgName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#teamsListAll");
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
| **orgName** | **String**| The organization&#39;s name | |

### Return type

[**List&lt;TeamsListAll200ResponseInner&gt;**](TeamsListAll200ResponseInner.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **0** | Error |  -  |

<a id="teamsListApps"></a>
# **teamsListApps**
> List&lt;TeamsListApps200ResponseInner&gt; teamsListApps(orgName, teamName)



Returns the apps a team has access to

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    AccountApi apiInstance = new AccountApi(defaultClient);
    String orgName = "orgName_example"; // String | The organization's name
    String teamName = "teamName_example"; // String | The team's name
    try {
      List<TeamsListApps200ResponseInner> result = apiInstance.teamsListApps(orgName, teamName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#teamsListApps");
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
| **orgName** | **String**| The organization&#39;s name | |
| **teamName** | **String**| The team&#39;s name | |

### Return type

[**List&lt;TeamsListApps200ResponseInner&gt;**](TeamsListApps200ResponseInner.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **0** | Error |  -  |

<a id="teamsRemoveApp"></a>
# **teamsRemoveApp**
> teamsRemoveApp(orgName, teamName, appName)



Removes an app from a team

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    AccountApi apiInstance = new AccountApi(defaultClient);
    String orgName = "orgName_example"; // String | The organization's name
    String teamName = "teamName_example"; // String | The team's name
    String appName = "appName_example"; // String | The name of the application
    try {
      apiInstance.teamsRemoveApp(orgName, teamName, appName);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#teamsRemoveApp");
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
| **orgName** | **String**| The organization&#39;s name | |
| **teamName** | **String**| The team&#39;s name | |
| **appName** | **String**| The name of the application | |

### Return type

null (empty response body)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **0** | Error |  -  |

<a id="teamsRemoveUser"></a>
# **teamsRemoveUser**
> teamsRemoveUser(orgName, teamName, userName)



Removes a user from a team that is owned by an organization

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    AccountApi apiInstance = new AccountApi(defaultClient);
    String orgName = "orgName_example"; // String | The organization's name
    String teamName = "teamName_example"; // String | The team's name
    String userName = "userName_example"; // String | The slug name of the user
    try {
      apiInstance.teamsRemoveUser(orgName, teamName, userName);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#teamsRemoveUser");
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
| **orgName** | **String**| The organization&#39;s name | |
| **teamName** | **String**| The team&#39;s name | |
| **userName** | **String**| The slug name of the user | |

### Return type

null (empty response body)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **0** | Error |  -  |

<a id="teamsUpdate"></a>
# **teamsUpdate**
> TeamsListAll200ResponseInner teamsUpdate(orgName, teamName, teamsUpdateRequest)



Updates a single team

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    AccountApi apiInstance = new AccountApi(defaultClient);
    String orgName = "orgName_example"; // String | The organization's name
    String teamName = "teamName_example"; // String | The team's name
    TeamsUpdateRequest teamsUpdateRequest = new TeamsUpdateRequest(); // TeamsUpdateRequest | The information used to update the team
    try {
      TeamsListAll200ResponseInner result = apiInstance.teamsUpdate(orgName, teamName, teamsUpdateRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#teamsUpdate");
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
| **orgName** | **String**| The organization&#39;s name | |
| **teamName** | **String**| The team&#39;s name | |
| **teamsUpdateRequest** | [**TeamsUpdateRequest**](TeamsUpdateRequest.md)| The information used to update the team | |

### Return type

[**TeamsListAll200ResponseInner**](TeamsListAll200ResponseInner.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **0** | Error |  -  |

<a id="teamsUpdatePermissions"></a>
# **teamsUpdatePermissions**
> TeamsListApps200ResponseInner teamsUpdatePermissions(orgName, teamName, appName, teamsUpdatePermissionsRequest)



Updates the permissions the team has to the app

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    AccountApi apiInstance = new AccountApi(defaultClient);
    String orgName = "orgName_example"; // String | The organization's name
    String teamName = "teamName_example"; // String | The team's name
    String appName = "appName_example"; // String | The name of the application
    TeamsUpdatePermissionsRequest teamsUpdatePermissionsRequest = new TeamsUpdatePermissionsRequest(); // TeamsUpdatePermissionsRequest | 
    try {
      TeamsListApps200ResponseInner result = apiInstance.teamsUpdatePermissions(orgName, teamName, appName, teamsUpdatePermissionsRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#teamsUpdatePermissions");
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
| **orgName** | **String**| The organization&#39;s name | |
| **teamName** | **String**| The team&#39;s name | |
| **appName** | **String**| The name of the application | |
| **teamsUpdatePermissionsRequest** | [**TeamsUpdatePermissionsRequest**](TeamsUpdatePermissionsRequest.md)|  | |

### Return type

[**TeamsListApps200ResponseInner**](TeamsListApps200ResponseInner.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **0** | Error |  -  |

<a id="userApiTokensDelete"></a>
# **userApiTokensDelete**
> userApiTokensDelete(apiTokenId)



Delete the user api_token object with the specific id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure HTTP basic authorization: Basic
    HttpBasicAuth Basic = (HttpBasicAuth) defaultClient.getAuthentication("Basic");
    Basic.setUsername("YOUR USERNAME");
    Basic.setPassword("YOUR PASSWORD");

    AccountApi apiInstance = new AccountApi(defaultClient);
    String apiTokenId = "apiTokenId_example"; // String | The unique ID (UUID) of the api token
    try {
      apiInstance.userApiTokensDelete(apiTokenId);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#userApiTokensDelete");
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
| **apiTokenId** | **String**| The unique ID (UUID) of the api token | |

### Return type

null (empty response body)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **400** | Error |  -  |
| **401** | Unauthorized |  -  |
| **404** | NotFound |  -  |

<a id="userApiTokensList"></a>
# **userApiTokensList**
> List&lt;UserApiTokensList200ResponseInner&gt; userApiTokensList()



Returns api tokens for the authenticated user

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure HTTP basic authorization: Basic
    HttpBasicAuth Basic = (HttpBasicAuth) defaultClient.getAuthentication("Basic");
    Basic.setUsername("YOUR USERNAME");
    Basic.setPassword("YOUR PASSWORD");

    AccountApi apiInstance = new AccountApi(defaultClient);
    try {
      List<UserApiTokensList200ResponseInner> result = apiInstance.userApiTokensList();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#userApiTokensList");
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

[**List&lt;UserApiTokensList200ResponseInner&gt;**](UserApiTokensList200ResponseInner.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Error |  -  |
| **401** | Unauthorized |  -  |

<a id="userApiTokensNew"></a>
# **userApiTokensNew**
> UserApiTokensNew201Response userApiTokensNew(userApiTokensNewRequest)



Creates a new User API token

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure HTTP basic authorization: Basic
    HttpBasicAuth Basic = (HttpBasicAuth) defaultClient.getAuthentication("Basic");
    Basic.setUsername("YOUR USERNAME");
    Basic.setPassword("YOUR PASSWORD");

    AccountApi apiInstance = new AccountApi(defaultClient);
    UserApiTokensNewRequest userApiTokensNewRequest = new UserApiTokensNewRequest(); // UserApiTokensNewRequest | Description of the token
    try {
      UserApiTokensNew201Response result = apiInstance.userApiTokensNew(userApiTokensNewRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#userApiTokensNew");
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
| **userApiTokensNewRequest** | [**UserApiTokensNewRequest**](UserApiTokensNewRequest.md)| Description of the token | [optional] |

### Return type

[**UserApiTokensNew201Response**](UserApiTokensNew201Response.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Success |  -  |
| **400** | Error |  -  |
| **401** | Unauthorized |  -  |

<a id="usersGet"></a>
# **usersGet**
> AppInvitationsList200ResponseInvitedBy usersGet()



Returns the user profile data

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    AccountApi apiInstance = new AccountApi(defaultClient);
    try {
      AppInvitationsList200ResponseInvitedBy result = apiInstance.usersGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#usersGet");
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

[**AppInvitationsList200ResponseInvitedBy**](AppInvitationsList200ResponseInvitedBy.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **0** | Error |  -  |

<a id="usersGetForOrg"></a>
# **usersGetForOrg**
> UsersListForOrg200ResponseInner usersGetForOrg(orgName, userName)



Get a user information from an organization by name - if there is explicit permission return it, if not if not return highest implicit permission

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    AccountApi apiInstance = new AccountApi(defaultClient);
    String orgName = "orgName_example"; // String | The organization's name
    String userName = "userName_example"; // String | The slug name of the user
    try {
      UsersListForOrg200ResponseInner result = apiInstance.usersGetForOrg(orgName, userName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#usersGetForOrg");
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
| **orgName** | **String**| The organization&#39;s name | |
| **userName** | **String**| The slug name of the user | |

### Return type

[**UsersListForOrg200ResponseInner**](UsersListForOrg200ResponseInner.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **0** | Error |  -  |

<a id="usersGetUserMetadata"></a>
# **usersGetUserMetadata**
> UsersGetUserMetadata200Response usersGetUserMetadata()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    AccountApi apiInstance = new AccountApi(defaultClient);
    try {
      UsersGetUserMetadata200Response result = apiInstance.usersGetUserMetadata();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#usersGetUserMetadata");
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

[**UsersGetUserMetadata200Response**](UsersGetUserMetadata200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **0** | Error |  -  |

<a id="usersList"></a>
# **usersList**
> List&lt;AppInvitationsList200ResponseInvitedBy&gt; usersList(ownerName, appName)



Returns the users associated with the app specified with the given app name which belongs to the given owner.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    AccountApi apiInstance = new AccountApi(defaultClient);
    String ownerName = "ownerName_example"; // String | The name of the owner
    String appName = "appName_example"; // String | The name of the application
    try {
      List<AppInvitationsList200ResponseInvitedBy> result = apiInstance.usersList(ownerName, appName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#usersList");
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
| **ownerName** | **String**| The name of the owner | |
| **appName** | **String**| The name of the application | |

### Return type

[**List&lt;AppInvitationsList200ResponseInvitedBy&gt;**](AppInvitationsList200ResponseInvitedBy.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **0** | Error |  -  |

<a id="usersListForOrg"></a>
# **usersListForOrg**
> List&lt;UsersListForOrg200ResponseInner&gt; usersListForOrg(orgName)



Returns a list of users that belong to an organization

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    AccountApi apiInstance = new AccountApi(defaultClient);
    String orgName = "orgName_example"; // String | The organization's name
    try {
      List<UsersListForOrg200ResponseInner> result = apiInstance.usersListForOrg(orgName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#usersListForOrg");
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
| **orgName** | **String**| The organization&#39;s name | |

### Return type

[**List&lt;UsersListForOrg200ResponseInner&gt;**](UsersListForOrg200ResponseInner.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **0** | Error |  -  |

<a id="usersRemoveFromOrg"></a>
# **usersRemoveFromOrg**
> usersRemoveFromOrg(orgName, userName)



Removes a user from an organization.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    AccountApi apiInstance = new AccountApi(defaultClient);
    String orgName = "orgName_example"; // String | The organization's name
    String userName = "userName_example"; // String | The slug name of the user
    try {
      apiInstance.usersRemoveFromOrg(orgName, userName);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#usersRemoveFromOrg");
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
| **orgName** | **String**| The organization&#39;s name | |
| **userName** | **String**| The slug name of the user | |

### Return type

null (empty response body)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **0** | Error |  -  |

<a id="usersUpdate"></a>
# **usersUpdate**
> AppInvitationsList200ResponseInvitedBy usersUpdate(usersUpdateRequest)



Updates the user profile and returns the updated user data

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    AccountApi apiInstance = new AccountApi(defaultClient);
    UsersUpdateRequest usersUpdateRequest = new UsersUpdateRequest(); // UsersUpdateRequest | The data for the created user
    try {
      AppInvitationsList200ResponseInvitedBy result = apiInstance.usersUpdate(usersUpdateRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#usersUpdate");
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
| **usersUpdateRequest** | [**UsersUpdateRequest**](UsersUpdateRequest.md)| The data for the created user | |

### Return type

[**AppInvitationsList200ResponseInvitedBy**](AppInvitationsList200ResponseInvitedBy.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **0** | Error |  -  |

<a id="usersUpdateOrgRole"></a>
# **usersUpdateOrgRole**
> UsersListForOrg200ResponseInner usersUpdateOrgRole(orgName, userName, orgInvitationsUpdateRequest)



Updates the given organization user

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appcenter.ms");
    
    // Configure API key authorization: APIToken
    ApiKeyAuth APIToken = (ApiKeyAuth) defaultClient.getAuthentication("APIToken");
    APIToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //APIToken.setApiKeyPrefix("Token");

    AccountApi apiInstance = new AccountApi(defaultClient);
    String orgName = "orgName_example"; // String | The organization's name
    String userName = "userName_example"; // String | The slug name of the user
    OrgInvitationsUpdateRequest orgInvitationsUpdateRequest = new OrgInvitationsUpdateRequest(); // OrgInvitationsUpdateRequest | 
    try {
      UsersListForOrg200ResponseInner result = apiInstance.usersUpdateOrgRole(orgName, userName, orgInvitationsUpdateRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#usersUpdateOrgRole");
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
| **orgName** | **String**| The organization&#39;s name | |
| **userName** | **String**| The slug name of the user | |
| **orgInvitationsUpdateRequest** | [**OrgInvitationsUpdateRequest**](OrgInvitationsUpdateRequest.md)|  | |

### Return type

[**UsersListForOrg200ResponseInner**](UsersListForOrg200ResponseInner.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **0** | Error |  -  |

