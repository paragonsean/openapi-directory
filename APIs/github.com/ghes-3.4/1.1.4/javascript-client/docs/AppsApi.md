# GitHubV3RestApi.AppsApi

All URIs are relative to *https://github.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**appsAddRepoToInstallationForAuthenticatedUser**](AppsApi.md#appsAddRepoToInstallationForAuthenticatedUser) | **PUT** /user/installations/{installation_id}/repositories/{repository_id} | Add a repository to an app installation
[**appsCheckToken**](AppsApi.md#appsCheckToken) | **POST** /applications/{client_id}/token | Check a token
[**appsCreateFromManifest**](AppsApi.md#appsCreateFromManifest) | **POST** /app-manifests/{code}/conversions | Create a GitHub App from a manifest
[**appsCreateInstallationAccessToken**](AppsApi.md#appsCreateInstallationAccessToken) | **POST** /app/installations/{installation_id}/access_tokens | Create an installation access token for an app
[**appsDeleteAuthorization**](AppsApi.md#appsDeleteAuthorization) | **DELETE** /applications/{client_id}/grant | Delete an app authorization
[**appsDeleteInstallation**](AppsApi.md#appsDeleteInstallation) | **DELETE** /app/installations/{installation_id} | Delete an installation for the authenticated app
[**appsDeleteToken**](AppsApi.md#appsDeleteToken) | **DELETE** /applications/{client_id}/token | Delete an app token
[**appsGetAuthenticated**](AppsApi.md#appsGetAuthenticated) | **GET** /app | Get the authenticated app
[**appsGetBySlug**](AppsApi.md#appsGetBySlug) | **GET** /apps/{app_slug} | Get an app
[**appsGetInstallation**](AppsApi.md#appsGetInstallation) | **GET** /app/installations/{installation_id} | Get an installation for the authenticated app
[**appsGetOrgInstallation**](AppsApi.md#appsGetOrgInstallation) | **GET** /orgs/{org}/installation | Get an organization installation for the authenticated app
[**appsGetRepoInstallation**](AppsApi.md#appsGetRepoInstallation) | **GET** /repos/{owner}/{repo}/installation | Get a repository installation for the authenticated app
[**appsGetUserInstallation**](AppsApi.md#appsGetUserInstallation) | **GET** /users/{username}/installation | Get a user installation for the authenticated app
[**appsGetWebhookConfigForApp**](AppsApi.md#appsGetWebhookConfigForApp) | **GET** /app/hook/config | Get a webhook configuration for an app
[**appsGetWebhookDelivery**](AppsApi.md#appsGetWebhookDelivery) | **GET** /app/hook/deliveries/{delivery_id} | Get a delivery for an app webhook
[**appsListInstallationReposForAuthenticatedUser**](AppsApi.md#appsListInstallationReposForAuthenticatedUser) | **GET** /user/installations/{installation_id}/repositories | List repositories accessible to the user access token
[**appsListInstallations**](AppsApi.md#appsListInstallations) | **GET** /app/installations | List installations for the authenticated app
[**appsListInstallationsForAuthenticatedUser**](AppsApi.md#appsListInstallationsForAuthenticatedUser) | **GET** /user/installations | List app installations accessible to the user access token
[**appsListReposAccessibleToInstallation**](AppsApi.md#appsListReposAccessibleToInstallation) | **GET** /installation/repositories | List repositories accessible to the app installation
[**appsListWebhookDeliveries**](AppsApi.md#appsListWebhookDeliveries) | **GET** /app/hook/deliveries | List deliveries for an app webhook
[**appsRedeliverWebhookDelivery**](AppsApi.md#appsRedeliverWebhookDelivery) | **POST** /app/hook/deliveries/{delivery_id}/attempts | Redeliver a delivery for an app webhook
[**appsRemoveRepoFromInstallationForAuthenticatedUser**](AppsApi.md#appsRemoveRepoFromInstallationForAuthenticatedUser) | **DELETE** /user/installations/{installation_id}/repositories/{repository_id} | Remove a repository from an app installation
[**appsResetToken**](AppsApi.md#appsResetToken) | **PATCH** /applications/{client_id}/token | Reset a token
[**appsRevokeInstallationAccessToken**](AppsApi.md#appsRevokeInstallationAccessToken) | **DELETE** /installation/token | Revoke an installation access token
[**appsScopeToken**](AppsApi.md#appsScopeToken) | **POST** /applications/{client_id}/token/scoped | Create a scoped access token
[**appsSuspendInstallation**](AppsApi.md#appsSuspendInstallation) | **PUT** /app/installations/{installation_id}/suspended | Suspend an app installation
[**appsUnsuspendInstallation**](AppsApi.md#appsUnsuspendInstallation) | **DELETE** /app/installations/{installation_id}/suspended | Unsuspend an app installation
[**appsUpdateWebhookConfigForApp**](AppsApi.md#appsUpdateWebhookConfigForApp) | **PATCH** /app/hook/config | Update a webhook configuration for an app



## appsAddRepoToInstallationForAuthenticatedUser

> appsAddRepoToInstallationForAuthenticatedUser(installationId, repositoryId)

Add a repository to an app installation

Add a single repository to an installation. The authenticated user must have admin access to the repository.  You must use a personal access token (which you can create via the [command line](https://docs.github.com/enterprise-server@3.4/github/authenticating-to-github/creating-a-personal-access-token) or [Basic Authentication](https://docs.github.com/enterprise-server@3.4/rest/overview/other-authentication-methods#basic-authentication)) to access this endpoint.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.AppsApi();
let installationId = 1; // Number | The unique identifier of the installation.
let repositoryId = 56; // Number | The unique identifier of the repository.
apiInstance.appsAddRepoToInstallationForAuthenticatedUser(installationId, repositoryId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **installationId** | **Number**| The unique identifier of the installation. | 
 **repositoryId** | **Number**| The unique identifier of the repository. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appsCheckToken

> Authorization appsCheckToken(clientId, appsCheckTokenRequest)

Check a token

OAuth applications can use a special API method for checking OAuth token validity without exceeding the normal rate limits for failed login attempts. Authentication works differently with this particular endpoint. You must use [Basic Authentication](https://docs.github.com/enterprise-server@3.4/rest/overview/other-authentication-methods#basic-authentication) to use this endpoint, where the username is the OAuth application &#x60;client_id&#x60; and the password is its &#x60;client_secret&#x60;. Invalid tokens will return &#x60;404 NOT FOUND&#x60;.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.AppsApi();
let clientId = "Iv1.8a61f9b3a7aba766"; // String | The client ID of the GitHub app.
let appsCheckTokenRequest = {"access_token":"e72e16c7e42f292c6912e7710c838347ae178b4a"}; // AppsCheckTokenRequest | 
apiInstance.appsCheckToken(clientId, appsCheckTokenRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clientId** | **String**| The client ID of the GitHub app. | 
 **appsCheckTokenRequest** | [**AppsCheckTokenRequest**](AppsCheckTokenRequest.md)|  | 

### Return type

[**Authorization**](Authorization.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## appsCreateFromManifest

> AppsCreateFromManifest201Response appsCreateFromManifest(code)

Create a GitHub App from a manifest

Use this endpoint to complete the handshake necessary when implementing the [GitHub App Manifest flow](https://docs.github.com/enterprise-server@3.4/apps/building-github-apps/creating-github-apps-from-a-manifest/). When you create a GitHub App with the manifest flow, you receive a temporary &#x60;code&#x60; used to retrieve the GitHub App&#39;s &#x60;id&#x60;, &#x60;pem&#x60; (private key), and &#x60;webhook_secret&#x60;.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.AppsApi();
let code = "code_example"; // String | 
apiInstance.appsCreateFromManifest(code, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **String**|  | 

### Return type

[**AppsCreateFromManifest201Response**](AppsCreateFromManifest201Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appsCreateInstallationAccessToken

> InstallationToken appsCreateInstallationAccessToken(installationId, opts)

Create an installation access token for an app

Creates an installation access token that enables a GitHub App to make authenticated API requests for the app&#39;s installation on an organization or individual account. Installation tokens expire one hour from the time you create them. Using an expired token produces a status code of &#x60;401 - Unauthorized&#x60;, and requires creating a new installation token. By default the installation token has access to all repositories that the installation can access. To restrict the access to specific repositories, you can provide the &#x60;repository_ids&#x60; when creating the token. When you omit &#x60;repository_ids&#x60;, the response does not contain the &#x60;repositories&#x60; key.  You must use a [JWT](https://docs.github.com/enterprise-server@3.4/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-a-github-app) to access this endpoint.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.AppsApi();
let installationId = 1; // Number | The unique identifier of the installation.
let opts = {
  'appsCreateInstallationAccessTokenRequest': {"permissions":{"contents":"read","issues":"write"},"repository":"Hello-World"} // AppsCreateInstallationAccessTokenRequest | 
};
apiInstance.appsCreateInstallationAccessToken(installationId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **installationId** | **Number**| The unique identifier of the installation. | 
 **appsCreateInstallationAccessTokenRequest** | [**AppsCreateInstallationAccessTokenRequest**](AppsCreateInstallationAccessTokenRequest.md)|  | [optional] 

### Return type

[**InstallationToken**](InstallationToken.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## appsDeleteAuthorization

> appsDeleteAuthorization(clientId, appsDeleteAuthorizationRequest)

Delete an app authorization

OAuth application owners can revoke a grant for their OAuth application and a specific user. You must use [Basic Authentication](https://docs.github.com/enterprise-server@3.4/rest/overview/other-authentication-methods#basic-authentication) when accessing this endpoint, using the OAuth application&#39;s &#x60;client_id&#x60; and &#x60;client_secret&#x60; as the username and password. You must also provide a valid OAuth &#x60;access_token&#x60; as an input parameter and the grant for the token&#39;s owner will be deleted. Deleting an OAuth application&#39;s grant will also delete all OAuth tokens associated with the application for the user. Once deleted, the application will have no access to the user&#39;s account and will no longer be listed on [the application authorizations settings screen within GitHub](https://github.com/settings/applications#authorized).

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.AppsApi();
let clientId = "Iv1.8a61f9b3a7aba766"; // String | The client ID of the GitHub app.
let appsDeleteAuthorizationRequest = {"access_token":"e72e16c7e42f292c6912e7710c838347ae178b4a"}; // AppsDeleteAuthorizationRequest | 
apiInstance.appsDeleteAuthorization(clientId, appsDeleteAuthorizationRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clientId** | **String**| The client ID of the GitHub app. | 
 **appsDeleteAuthorizationRequest** | [**AppsDeleteAuthorizationRequest**](AppsDeleteAuthorizationRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## appsDeleteInstallation

> appsDeleteInstallation(installationId)

Delete an installation for the authenticated app

Uninstalls a GitHub App on a user, organization, or business account. If you prefer to temporarily suspend an app&#39;s access to your account&#39;s resources, then we recommend the \&quot;[Suspend an app installation](https://docs.github.com/enterprise-server@3.4/rest/reference/apps/#suspend-an-app-installation)\&quot; endpoint.  You must use a [JWT](https://docs.github.com/enterprise-server@3.4/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-a-github-app) to access this endpoint.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.AppsApi();
let installationId = 1; // Number | The unique identifier of the installation.
apiInstance.appsDeleteInstallation(installationId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **installationId** | **Number**| The unique identifier of the installation. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appsDeleteToken

> appsDeleteToken(clientId, appsDeleteAuthorizationRequest)

Delete an app token

OAuth application owners can revoke a single token for an OAuth application. You must use [Basic Authentication](https://docs.github.com/enterprise-server@3.4/rest/overview/other-authentication-methods#basic-authentication) when accessing this endpoint, using the OAuth application&#39;s &#x60;client_id&#x60; and &#x60;client_secret&#x60; as the username and password.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.AppsApi();
let clientId = "Iv1.8a61f9b3a7aba766"; // String | The client ID of the GitHub app.
let appsDeleteAuthorizationRequest = {"access_token":"e72e16c7e42f292c6912e7710c838347ae178b4a"}; // AppsDeleteAuthorizationRequest | 
apiInstance.appsDeleteToken(clientId, appsDeleteAuthorizationRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clientId** | **String**| The client ID of the GitHub app. | 
 **appsDeleteAuthorizationRequest** | [**AppsDeleteAuthorizationRequest**](AppsDeleteAuthorizationRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## appsGetAuthenticated

> Integration appsGetAuthenticated()

Get the authenticated app

Returns the GitHub App associated with the authentication credentials used. To see how many app installations are associated with this GitHub App, see the &#x60;installations_count&#x60; in the response. For more details about your app&#39;s installations, see the \&quot;[List installations for the authenticated app](https://docs.github.com/enterprise-server@3.4/rest/reference/apps#list-installations-for-the-authenticated-app)\&quot; endpoint.  You must use a [JWT](https://docs.github.com/enterprise-server@3.4/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-a-github-app) to access this endpoint.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.AppsApi();
apiInstance.appsGetAuthenticated((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**Integration**](Integration.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appsGetBySlug

> Integration appsGetBySlug(appSlug)

Get an app

**Note**: The &#x60;:app_slug&#x60; is just the URL-friendly name of your GitHub App. You can find this on the settings page for your GitHub App (e.g., &#x60;https://github.com/settings/apps/:app_slug&#x60;).  If the GitHub App you specify is public, you can access this endpoint without authenticating. If the GitHub App you specify is private, you must authenticate with a [personal access token](https://docs.github.com/enterprise-server@3.4/articles/creating-a-personal-access-token-for-the-command-line/) or an [installation access token](https://docs.github.com/enterprise-server@3.4/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-an-installation) to access this endpoint.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.AppsApi();
let appSlug = "appSlug_example"; // String | 
apiInstance.appsGetBySlug(appSlug, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appSlug** | **String**|  | 

### Return type

[**Integration**](Integration.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appsGetInstallation

> Installation appsGetInstallation(installationId)

Get an installation for the authenticated app

Enables an authenticated GitHub App to find an installation&#39;s information using the installation id.  You must use a [JWT](https://docs.github.com/enterprise-server@3.4/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-a-github-app) to access this endpoint.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.AppsApi();
let installationId = 1; // Number | The unique identifier of the installation.
apiInstance.appsGetInstallation(installationId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **installationId** | **Number**| The unique identifier of the installation. | 

### Return type

[**Installation**](Installation.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appsGetOrgInstallation

> Installation appsGetOrgInstallation(org)

Get an organization installation for the authenticated app

Enables an authenticated GitHub App to find the organization&#39;s installation information.  You must use a [JWT](https://docs.github.com/enterprise-server@3.4/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-a-github-app) to access this endpoint.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.AppsApi();
let org = "org_example"; // String | The organization name. The name is not case sensitive.
apiInstance.appsGetOrgInstallation(org, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **String**| The organization name. The name is not case sensitive. | 

### Return type

[**Installation**](Installation.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appsGetRepoInstallation

> Installation appsGetRepoInstallation(owner, repo)

Get a repository installation for the authenticated app

Enables an authenticated GitHub App to find the repository&#39;s installation information. The installation&#39;s account type will be either an organization or a user account, depending which account the repository belongs to.  You must use a [JWT](https://docs.github.com/enterprise-server@3.4/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-a-github-app) to access this endpoint.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.AppsApi();
let owner = "owner_example"; // String | The account owner of the repository. The name is not case sensitive.
let repo = "repo_example"; // String | The name of the repository. The name is not case sensitive.
apiInstance.appsGetRepoInstallation(owner, repo, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **String**| The account owner of the repository. The name is not case sensitive. | 
 **repo** | **String**| The name of the repository. The name is not case sensitive. | 

### Return type

[**Installation**](Installation.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appsGetUserInstallation

> Installation appsGetUserInstallation(username)

Get a user installation for the authenticated app

Enables an authenticated GitHub App to find the user’s installation information.  You must use a [JWT](https://docs.github.com/enterprise-server@3.4/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-a-github-app) to access this endpoint.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.AppsApi();
let username = "username_example"; // String | The handle for the GitHub user account.
apiInstance.appsGetUserInstallation(username, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **String**| The handle for the GitHub user account. | 

### Return type

[**Installation**](Installation.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appsGetWebhookConfigForApp

> WebhookConfig appsGetWebhookConfigForApp()

Get a webhook configuration for an app

Returns the webhook configuration for a GitHub App. For more information about configuring a webhook for your app, see \&quot;[Creating a GitHub App](/developers/apps/creating-a-github-app).\&quot;  You must use a [JWT](https://docs.github.com/enterprise-server@3.4/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-a-github-app) to access this endpoint.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.AppsApi();
apiInstance.appsGetWebhookConfigForApp((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**WebhookConfig**](WebhookConfig.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appsGetWebhookDelivery

> HookDelivery appsGetWebhookDelivery(deliveryId)

Get a delivery for an app webhook

Returns a delivery for the webhook configured for a GitHub App.  You must use a [JWT](https://docs.github.com/enterprise-server@3.4/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-a-github-app) to access this endpoint.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.AppsApi();
let deliveryId = 56; // Number | 
apiInstance.appsGetWebhookDelivery(deliveryId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deliveryId** | **Number**|  | 

### Return type

[**HookDelivery**](HookDelivery.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/scim+json


## appsListInstallationReposForAuthenticatedUser

> AppsListInstallationReposForAuthenticatedUser200Response appsListInstallationReposForAuthenticatedUser(installationId, opts)

List repositories accessible to the user access token

List repositories that the authenticated user has explicit permission (&#x60;:read&#x60;, &#x60;:write&#x60;, or &#x60;:admin&#x60;) to access for an installation.  The authenticated user has explicit permission to access repositories they own, repositories where they are a collaborator, and repositories that they can access through an organization membership.  You must use a [user-to-server OAuth access token](https://docs.github.com/enterprise-server@3.4/apps/building-github-apps/identifying-and-authorizing-users-for-github-apps/#identifying-users-on-your-site), created for a user who has authorized your GitHub App, to access this endpoint.  The access the user has to each repository is included in the hash under the &#x60;permissions&#x60; key.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.AppsApi();
let installationId = 1; // Number | The unique identifier of the installation.
let opts = {
  'perPage': 30, // Number | The number of results per page (max 100).
  'page': 1 // Number | Page number of the results to fetch.
};
apiInstance.appsListInstallationReposForAuthenticatedUser(installationId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **installationId** | **Number**| The unique identifier of the installation. | 
 **perPage** | **Number**| The number of results per page (max 100). | [optional] [default to 30]
 **page** | **Number**| Page number of the results to fetch. | [optional] [default to 1]

### Return type

[**AppsListInstallationReposForAuthenticatedUser200Response**](AppsListInstallationReposForAuthenticatedUser200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appsListInstallations

> [Installation] appsListInstallations(opts)

List installations for the authenticated app

You must use a [JWT](https://docs.github.com/enterprise-server@3.4/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-a-github-app) to access this endpoint.  The permissions the installation has are included under the &#x60;permissions&#x60; key.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.AppsApi();
let opts = {
  'perPage': 30, // Number | The number of results per page (max 100).
  'page': 1, // Number | Page number of the results to fetch.
  'since': new Date("2013-10-20T19:20:30+01:00"), // Date | Only show notifications updated after the given time. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: `YYYY-MM-DDTHH:MM:SSZ`.
  'outdated': "outdated_example" // String | 
};
apiInstance.appsListInstallations(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **perPage** | **Number**| The number of results per page (max 100). | [optional] [default to 30]
 **page** | **Number**| Page number of the results to fetch. | [optional] [default to 1]
 **since** | **Date**| Only show notifications updated after the given time. This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format: &#x60;YYYY-MM-DDTHH:MM:SSZ&#x60;. | [optional] 
 **outdated** | **String**|  | [optional] 

### Return type

[**[Installation]**](Installation.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appsListInstallationsForAuthenticatedUser

> OrgsListAppInstallations200Response appsListInstallationsForAuthenticatedUser(opts)

List app installations accessible to the user access token

Lists installations of your GitHub App that the authenticated user has explicit permission (&#x60;:read&#x60;, &#x60;:write&#x60;, or &#x60;:admin&#x60;) to access.  You must use a [user-to-server OAuth access token](https://docs.github.com/enterprise-server@3.4/apps/building-github-apps/identifying-and-authorizing-users-for-github-apps/#identifying-users-on-your-site), created for a user who has authorized your GitHub App, to access this endpoint.  The authenticated user has explicit permission to access repositories they own, repositories where they are a collaborator, and repositories that they can access through an organization membership.  You can find the permissions for the installation under the &#x60;permissions&#x60; key.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.AppsApi();
let opts = {
  'perPage': 30, // Number | The number of results per page (max 100).
  'page': 1 // Number | Page number of the results to fetch.
};
apiInstance.appsListInstallationsForAuthenticatedUser(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **perPage** | **Number**| The number of results per page (max 100). | [optional] [default to 30]
 **page** | **Number**| Page number of the results to fetch. | [optional] [default to 1]

### Return type

[**OrgsListAppInstallations200Response**](OrgsListAppInstallations200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appsListReposAccessibleToInstallation

> AppsListReposAccessibleToInstallation200Response appsListReposAccessibleToInstallation(opts)

List repositories accessible to the app installation

List repositories that an app installation can access.  You must use an [installation access token](https://docs.github.com/enterprise-server@3.4/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-an-installation) to access this endpoint.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.AppsApi();
let opts = {
  'perPage': 30, // Number | The number of results per page (max 100).
  'page': 1 // Number | Page number of the results to fetch.
};
apiInstance.appsListReposAccessibleToInstallation(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **perPage** | **Number**| The number of results per page (max 100). | [optional] [default to 30]
 **page** | **Number**| Page number of the results to fetch. | [optional] [default to 1]

### Return type

[**AppsListReposAccessibleToInstallation200Response**](AppsListReposAccessibleToInstallation200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appsListWebhookDeliveries

> [HookDeliveryItem] appsListWebhookDeliveries(opts)

List deliveries for an app webhook

Returns a list of webhook deliveries for the webhook configured for a GitHub App.  You must use a [JWT](https://docs.github.com/enterprise-server@3.4/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-a-github-app) to access this endpoint.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.AppsApi();
let opts = {
  'perPage': 30, // Number | The number of results per page (max 100).
  'cursor': "cursor_example", // String | Used for pagination: the starting delivery from which the page of deliveries is fetched. Refer to the `link` header for the next and previous page cursors.
  'redelivery': true // Boolean | 
};
apiInstance.appsListWebhookDeliveries(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **perPage** | **Number**| The number of results per page (max 100). | [optional] [default to 30]
 **cursor** | **String**| Used for pagination: the starting delivery from which the page of deliveries is fetched. Refer to the &#x60;link&#x60; header for the next and previous page cursors. | [optional] 
 **redelivery** | **Boolean**|  | [optional] 

### Return type

[**[HookDeliveryItem]**](HookDeliveryItem.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/scim+json


## appsRedeliverWebhookDelivery

> Object appsRedeliverWebhookDelivery(deliveryId)

Redeliver a delivery for an app webhook

Redeliver a delivery for the webhook configured for a GitHub App.  You must use a [JWT](https://docs.github.com/enterprise-server@3.4/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-a-github-app) to access this endpoint.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.AppsApi();
let deliveryId = 56; // Number | 
apiInstance.appsRedeliverWebhookDelivery(deliveryId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deliveryId** | **Number**|  | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/scim+json


## appsRemoveRepoFromInstallationForAuthenticatedUser

> appsRemoveRepoFromInstallationForAuthenticatedUser(installationId, repositoryId)

Remove a repository from an app installation

Remove a single repository from an installation. The authenticated user must have admin access to the repository.  You must use a personal access token (which you can create via the [command line](https://docs.github.com/enterprise-server@3.4/github/authenticating-to-github/creating-a-personal-access-token) or [Basic Authentication](https://docs.github.com/enterprise-server@3.4/rest/overview/other-authentication-methods#basic-authentication)) to access this endpoint.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.AppsApi();
let installationId = 1; // Number | The unique identifier of the installation.
let repositoryId = 56; // Number | The unique identifier of the repository.
apiInstance.appsRemoveRepoFromInstallationForAuthenticatedUser(installationId, repositoryId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **installationId** | **Number**| The unique identifier of the installation. | 
 **repositoryId** | **Number**| The unique identifier of the repository. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appsResetToken

> Authorization appsResetToken(clientId, appsCheckTokenRequest)

Reset a token

OAuth applications can use this API method to reset a valid OAuth token without end-user involvement. Applications must save the \&quot;token\&quot; property in the response because changes take effect immediately. You must use [Basic Authentication](https://docs.github.com/enterprise-server@3.4/rest/overview/other-authentication-methods#basic-authentication) when accessing this endpoint, using the OAuth application&#39;s &#x60;client_id&#x60; and &#x60;client_secret&#x60; as the username and password. Invalid tokens will return &#x60;404 NOT FOUND&#x60;.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.AppsApi();
let clientId = "Iv1.8a61f9b3a7aba766"; // String | The client ID of the GitHub app.
let appsCheckTokenRequest = {"access_token":"e72e16c7e42f292c6912e7710c838347ae178b4a"}; // AppsCheckTokenRequest | 
apiInstance.appsResetToken(clientId, appsCheckTokenRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clientId** | **String**| The client ID of the GitHub app. | 
 **appsCheckTokenRequest** | [**AppsCheckTokenRequest**](AppsCheckTokenRequest.md)|  | 

### Return type

[**Authorization**](Authorization.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## appsRevokeInstallationAccessToken

> appsRevokeInstallationAccessToken()

Revoke an installation access token

Revokes the installation token you&#39;re using to authenticate as an installation and access this endpoint.  Once an installation token is revoked, the token is invalidated and cannot be used. Other endpoints that require the revoked installation token must have a new installation token to work. You can create a new token using the \&quot;[Create an installation access token for an app](https://docs.github.com/enterprise-server@3.4/rest/reference/apps#create-an-installation-access-token-for-an-app)\&quot; endpoint.  You must use an [installation access token](https://docs.github.com/enterprise-server@3.4/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-an-installation) to access this endpoint.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.AppsApi();
apiInstance.appsRevokeInstallationAccessToken((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## appsScopeToken

> Authorization appsScopeToken(clientId, appsScopeTokenRequest)

Create a scoped access token

Use a non-scoped user-to-server access token to create a repository scoped and/or permission scoped user-to-server access token. You can specify which repositories the token can access and which permissions are granted to the token. You must use [Basic Authentication](https://docs.github.com/enterprise-server@3.4/rest/overview/other-authentication-methods#basic-authentication) when accessing this endpoint, using the &#x60;client_id&#x60; and &#x60;client_secret&#x60; of the GitHub App as the username and password. Invalid tokens will return &#x60;404 NOT FOUND&#x60;.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.AppsApi();
let clientId = "Iv1.8a61f9b3a7aba766"; // String | The client ID of the GitHub app.
let appsScopeTokenRequest = {"access_token":"e72e16c7e42f292c6912e7710c838347ae178b4a","permissions":{"contents":"read","issues":"write","metadata":"read"},"target":"octocat"}; // AppsScopeTokenRequest | 
apiInstance.appsScopeToken(clientId, appsScopeTokenRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clientId** | **String**| The client ID of the GitHub app. | 
 **appsScopeTokenRequest** | [**AppsScopeTokenRequest**](AppsScopeTokenRequest.md)|  | 

### Return type

[**Authorization**](Authorization.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## appsSuspendInstallation

> appsSuspendInstallation(installationId)

Suspend an app installation

Suspends a GitHub App on a user, organization, or business account, which blocks the app from accessing the account&#39;s resources. When a GitHub App is suspended, the app&#39;s access to the GitHub Enterprise Server API or webhook events is blocked for that account.  You must use a [JWT](https://docs.github.com/enterprise-server@3.4/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-a-github-app) to access this endpoint.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.AppsApi();
let installationId = 1; // Number | The unique identifier of the installation.
apiInstance.appsSuspendInstallation(installationId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **installationId** | **Number**| The unique identifier of the installation. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appsUnsuspendInstallation

> appsUnsuspendInstallation(installationId)

Unsuspend an app installation

Removes a GitHub App installation suspension.  You must use a [JWT](https://docs.github.com/enterprise-server@3.4/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-a-github-app) to access this endpoint.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.AppsApi();
let installationId = 1; // Number | The unique identifier of the installation.
apiInstance.appsUnsuspendInstallation(installationId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **installationId** | **Number**| The unique identifier of the installation. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appsUpdateWebhookConfigForApp

> WebhookConfig appsUpdateWebhookConfigForApp(appsUpdateWebhookConfigForAppRequest)

Update a webhook configuration for an app

Updates the webhook configuration for a GitHub App. For more information about configuring a webhook for your app, see \&quot;[Creating a GitHub App](/developers/apps/creating-a-github-app).\&quot;  You must use a [JWT](https://docs.github.com/enterprise-server@3.4/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-a-github-app) to access this endpoint.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.AppsApi();
let appsUpdateWebhookConfigForAppRequest = {"content_type":"json","insecure_ssl":"0","secret":"********","url":"https://example.com/webhook"}; // AppsUpdateWebhookConfigForAppRequest | 
apiInstance.appsUpdateWebhookConfigForApp(appsUpdateWebhookConfigForAppRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appsUpdateWebhookConfigForAppRequest** | [**AppsUpdateWebhookConfigForAppRequest**](AppsUpdateWebhookConfigForAppRequest.md)|  | 

### Return type

[**WebhookConfig**](WebhookConfig.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

