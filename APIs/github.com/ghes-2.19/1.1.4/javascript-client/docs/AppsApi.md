# GitHubV3RestApi.AppsApi

All URIs are relative to *http://HOSTNAME/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**appsAddRepoToInstallation**](AppsApi.md#appsAddRepoToInstallation) | **PUT** /user/installations/{installation_id}/repositories/{repository_id} | Add a repository to an app installation
[**appsCreateContentAttachment**](AppsApi.md#appsCreateContentAttachment) | **POST** /repos/{owner}/{repo}/content_references/{content_reference_id}/attachments | Create a content attachment
[**appsCreateFromManifest**](AppsApi.md#appsCreateFromManifest) | **POST** /app-manifests/{code}/conversions | Create a GitHub App from a manifest
[**appsCreateInstallationAccessToken**](AppsApi.md#appsCreateInstallationAccessToken) | **POST** /app/installations/{installation_id}/access_tokens | Create an installation access token for an app
[**appsDeleteInstallation**](AppsApi.md#appsDeleteInstallation) | **DELETE** /app/installations/{installation_id} | Delete an installation for the authenticated app
[**appsGetAuthenticated**](AppsApi.md#appsGetAuthenticated) | **GET** /app | Get the authenticated app
[**appsGetBySlug**](AppsApi.md#appsGetBySlug) | **GET** /apps/{app_slug} | Get an app
[**appsGetInstallation**](AppsApi.md#appsGetInstallation) | **GET** /app/installations/{installation_id} | Get an installation for the authenticated app
[**appsGetOrgInstallation**](AppsApi.md#appsGetOrgInstallation) | **GET** /orgs/{org}/installation | Get an organization installation for the authenticated app
[**appsGetRepoInstallation**](AppsApi.md#appsGetRepoInstallation) | **GET** /repos/{owner}/{repo}/installation | Get a repository installation for the authenticated app
[**appsGetUserInstallation**](AppsApi.md#appsGetUserInstallation) | **GET** /users/{username}/installation | Get a user installation for the authenticated app
[**appsListInstallationReposForAuthenticatedUser**](AppsApi.md#appsListInstallationReposForAuthenticatedUser) | **GET** /user/installations/{installation_id}/repositories | List repositories accessible to the user access token
[**appsListInstallations**](AppsApi.md#appsListInstallations) | **GET** /app/installations | List installations for the authenticated app
[**appsListInstallationsForAuthenticatedUser**](AppsApi.md#appsListInstallationsForAuthenticatedUser) | **GET** /user/installations | List app installations accessible to the user access token
[**appsListReposAccessibleToInstallation**](AppsApi.md#appsListReposAccessibleToInstallation) | **GET** /installation/repositories | List repositories accessible to the app installation
[**appsRemoveRepoFromInstallation**](AppsApi.md#appsRemoveRepoFromInstallation) | **DELETE** /user/installations/{installation_id}/repositories/{repository_id} | Remove a repository from an app installation



## appsAddRepoToInstallation

> appsAddRepoToInstallation(installationId, repositoryId)

Add a repository to an app installation

Add a single repository to an installation. The authenticated user must have admin access to the repository.  You must use a personal access token (which you can create via the [command line](https://docs.github.com/enterprise-server@2.19/github/authenticating-to-github/creating-a-personal-access-token) or [Basic Authentication](https://docs.github.com/enterprise-server@2.19/rest/overview/other-authentication-methods#basic-authentication)) to access this endpoint.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.AppsApi();
let installationId = 56; // Number | installation_id parameter
let repositoryId = 56; // Number | 
apiInstance.appsAddRepoToInstallation(installationId, repositoryId, (error, data, response) => {
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
 **installationId** | **Number**| installation_id parameter | 
 **repositoryId** | **Number**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appsCreateContentAttachment

> ContentReferenceAttachment appsCreateContentAttachment(owner, repo, contentReferenceId, appsCreateContentAttachmentRequest)

Create a content attachment

Creates an attachment under a content reference URL in the body or comment of an issue or pull request. Use the &#x60;id&#x60; and &#x60;repository&#x60; &#x60;full_name&#x60; of the content reference from the [&#x60;content_reference&#x60; event](https://docs.github.com/enterprise-server@2.19/webhooks/event-payloads/#content_reference) to create an attachment.  The app must create a content attachment within six hours of the content reference URL being posted. See \&quot;[Using content attachments](https://docs.github.com/enterprise-server@2.19/apps/using-content-attachments/)\&quot; for details about content attachments.  You must use an [installation access token](https://docs.github.com/enterprise-server@2.19/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-an-installation) to access this endpoint.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.AppsApi();
let owner = "owner_example"; // String | The owner of the repository. Determined from the `repository` `full_name` of the `content_reference` event.
let repo = "repo_example"; // String | The name of the repository. Determined from the `repository` `full_name` of the `content_reference` event.
let contentReferenceId = 56; // Number | The `id` of the `content_reference` event.
let appsCreateContentAttachmentRequest = new GitHubV3RestApi.AppsCreateContentAttachmentRequest(); // AppsCreateContentAttachmentRequest | 
apiInstance.appsCreateContentAttachment(owner, repo, contentReferenceId, appsCreateContentAttachmentRequest, (error, data, response) => {
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
 **owner** | **String**| The owner of the repository. Determined from the &#x60;repository&#x60; &#x60;full_name&#x60; of the &#x60;content_reference&#x60; event. | 
 **repo** | **String**| The name of the repository. Determined from the &#x60;repository&#x60; &#x60;full_name&#x60; of the &#x60;content_reference&#x60; event. | 
 **contentReferenceId** | **Number**| The &#x60;id&#x60; of the &#x60;content_reference&#x60; event. | 
 **appsCreateContentAttachmentRequest** | [**AppsCreateContentAttachmentRequest**](AppsCreateContentAttachmentRequest.md)|  | 

### Return type

[**ContentReferenceAttachment**](ContentReferenceAttachment.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## appsCreateFromManifest

> AppsCreateFromManifest201Response appsCreateFromManifest(code, opts)

Create a GitHub App from a manifest

Use this endpoint to complete the handshake necessary when implementing the [GitHub App Manifest flow](https://docs.github.com/enterprise-server@2.19/apps/building-github-apps/creating-github-apps-from-a-manifest/). When you create a GitHub App with the manifest flow, you receive a temporary &#x60;code&#x60; used to retrieve the GitHub App&#39;s &#x60;id&#x60;, &#x60;pem&#x60; (private key), and &#x60;webhook_secret&#x60;.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.AppsApi();
let code = "code_example"; // String | 
let opts = {
  'body': {key: null} // Object | 
};
apiInstance.appsCreateFromManifest(code, opts, (error, data, response) => {
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
 **body** | **Object**|  | [optional] 

### Return type

[**AppsCreateFromManifest201Response**](AppsCreateFromManifest201Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## appsCreateInstallationAccessToken

> InstallationToken appsCreateInstallationAccessToken(accept, installationId, opts)

Create an installation access token for an app

Creates an installation access token that enables a GitHub App to make authenticated API requests for the app&#39;s installation on an organization or individual account. Installation tokens expire one hour from the time you create them. Using an expired token produces a status code of &#x60;401 - Unauthorized&#x60;, and requires creating a new installation token. By default the installation token has access to all repositories that the installation can access. To restrict the access to specific repositories, you can provide the &#x60;repository_ids&#x60; when creating the token. When you omit &#x60;repository_ids&#x60;, the response does not contain the &#x60;repositories&#x60; key.  You must use a [JWT](https://docs.github.com/enterprise-server@2.19/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-a-github-app) to access this endpoint.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.AppsApi();
let accept = "'application/vnd.github.machine-man-preview+json'"; // String | This API is under preview and subject to change.
let installationId = 56; // Number | installation_id parameter
let opts = {
  'appsCreateInstallationAccessTokenRequest': new GitHubV3RestApi.AppsCreateInstallationAccessTokenRequest() // AppsCreateInstallationAccessTokenRequest | 
};
apiInstance.appsCreateInstallationAccessToken(accept, installationId, opts, (error, data, response) => {
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
 **accept** | **String**| This API is under preview and subject to change. | [default to &#39;application/vnd.github.machine-man-preview+json&#39;]
 **installationId** | **Number**| installation_id parameter | 
 **appsCreateInstallationAccessTokenRequest** | [**AppsCreateInstallationAccessTokenRequest**](AppsCreateInstallationAccessTokenRequest.md)|  | [optional] 

### Return type

[**InstallationToken**](InstallationToken.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## appsDeleteInstallation

> appsDeleteInstallation(accept, installationId)

Delete an installation for the authenticated app

Uninstalls a GitHub App on a user, organization, or business account. You must use a [JWT](https://docs.github.com/enterprise-server@2.19/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-a-github-app) to access this endpoint.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.AppsApi();
let accept = "'application/vnd.github.gambit-preview+json,application/vnd.github.machine-man-preview+json'"; // String | This API is under preview and subject to change.
let installationId = 56; // Number | installation_id parameter
apiInstance.appsDeleteInstallation(accept, installationId, (error, data, response) => {
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
 **accept** | **String**| This API is under preview and subject to change. | [default to &#39;application/vnd.github.gambit-preview+json,application/vnd.github.machine-man-preview+json&#39;]
 **installationId** | **Number**| installation_id parameter | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appsGetAuthenticated

> Integration appsGetAuthenticated()

Get the authenticated app

Returns the GitHub App associated with the authentication credentials used. To see how many app installations are associated with this GitHub App, see the &#x60;installations_count&#x60; in the response. For more details about your app&#39;s installations, see the \&quot;[List installations for the authenticated app](https://docs.github.com/enterprise-server@2.19/rest/reference/apps#list-installations-for-the-authenticated-app)\&quot; endpoint.  You must use a [JWT](https://docs.github.com/enterprise-server@2.19/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-a-github-app) to access this endpoint.

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

**Note**: The &#x60;:app_slug&#x60; is just the URL-friendly name of your GitHub App. You can find this on the settings page for your GitHub App (e.g., &#x60;https://github.com/settings/apps/:app_slug&#x60;).  If the GitHub App you specify is public, you can access this endpoint without authenticating. If the GitHub App you specify is private, you must authenticate with a [personal access token](https://help.github.com/articles/creating-a-personal-access-token-for-the-command-line/) or an [installation access token](https://docs.github.com/enterprise-server@2.19/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-an-installation) to access this endpoint.

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

> InstallationGhes2 appsGetInstallation(accept, installationId)

Get an installation for the authenticated app

Enables an authenticated GitHub App to find an installation&#39;s information using the installation id. The installation&#39;s account type (&#x60;target_type&#x60;) will be either an organization or a user account, depending which account the repository belongs to.  You must use a [JWT](https://docs.github.com/enterprise-server@2.19/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-a-github-app) to access this endpoint.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.AppsApi();
let accept = "'application/vnd.github.machine-man-preview+json'"; // String | This API is under preview and subject to change.
let installationId = 56; // Number | installation_id parameter
apiInstance.appsGetInstallation(accept, installationId, (error, data, response) => {
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
 **accept** | **String**| This API is under preview and subject to change. | [default to &#39;application/vnd.github.machine-man-preview+json&#39;]
 **installationId** | **Number**| installation_id parameter | 

### Return type

[**InstallationGhes2**](InstallationGhes2.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appsGetOrgInstallation

> InstallationGhes2 appsGetOrgInstallation(accept, org)

Get an organization installation for the authenticated app

Enables an authenticated GitHub App to find the organization&#39;s installation information.  You must use a [JWT](https://docs.github.com/enterprise-server@2.19/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-a-github-app) to access this endpoint.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.AppsApi();
let accept = "'application/vnd.github.machine-man-preview+json'"; // String | This API is under preview and subject to change.
let org = "org_example"; // String | 
apiInstance.appsGetOrgInstallation(accept, org, (error, data, response) => {
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
 **accept** | **String**| This API is under preview and subject to change. | [default to &#39;application/vnd.github.machine-man-preview+json&#39;]
 **org** | **String**|  | 

### Return type

[**InstallationGhes2**](InstallationGhes2.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appsGetRepoInstallation

> InstallationGhes2 appsGetRepoInstallation(accept, owner, repo)

Get a repository installation for the authenticated app

Enables an authenticated GitHub App to find the repository&#39;s installation information. The installation&#39;s account type will be either an organization or a user account, depending which account the repository belongs to.  You must use a [JWT](https://docs.github.com/enterprise-server@2.19/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-a-github-app) to access this endpoint.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.AppsApi();
let accept = "'application/vnd.github.machine-man-preview+json'"; // String | This API is under preview and subject to change.
let owner = "owner_example"; // String | 
let repo = "repo_example"; // String | 
apiInstance.appsGetRepoInstallation(accept, owner, repo, (error, data, response) => {
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
 **accept** | **String**| This API is under preview and subject to change. | [default to &#39;application/vnd.github.machine-man-preview+json&#39;]
 **owner** | **String**|  | 
 **repo** | **String**|  | 

### Return type

[**InstallationGhes2**](InstallationGhes2.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appsGetUserInstallation

> InstallationGhes2 appsGetUserInstallation(accept, username)

Get a user installation for the authenticated app

Enables an authenticated GitHub App to find the user’s installation information.  You must use a [JWT](https://docs.github.com/enterprise-server@2.19/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-a-github-app) to access this endpoint.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.AppsApi();
let accept = "'application/vnd.github.machine-man-preview+json'"; // String | This API is under preview and subject to change.
let username = "username_example"; // String | 
apiInstance.appsGetUserInstallation(accept, username, (error, data, response) => {
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
 **accept** | **String**| This API is under preview and subject to change. | [default to &#39;application/vnd.github.machine-man-preview+json&#39;]
 **username** | **String**|  | 

### Return type

[**InstallationGhes2**](InstallationGhes2.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appsListInstallationReposForAuthenticatedUser

> AppsListInstallationReposForAuthenticatedUser200Response appsListInstallationReposForAuthenticatedUser(accept, installationId, opts)

List repositories accessible to the user access token

List repositories that the authenticated user has explicit permission (&#x60;:read&#x60;, &#x60;:write&#x60;, or &#x60;:admin&#x60;) to access for an installation.  The authenticated user has explicit permission to access repositories they own, repositories where they are a collaborator, and repositories that they can access through an organization membership.  You must use a [user-to-server OAuth access token](https://docs.github.com/enterprise-server@2.19/apps/building-github-apps/identifying-and-authorizing-users-for-github-apps/#identifying-users-on-your-site), created for a user who has authorized your GitHub App, to access this endpoint.  The access the user has to each repository is included in the hash under the &#x60;permissions&#x60; key.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.AppsApi();
let accept = "'application/vnd.github.machine-man-preview+json'"; // String | This API is under preview and subject to change.
let installationId = 56; // Number | installation_id parameter
let opts = {
  'perPage': 30, // Number | Results per page (max 100)
  'page': 1 // Number | Page number of the results to fetch.
};
apiInstance.appsListInstallationReposForAuthenticatedUser(accept, installationId, opts, (error, data, response) => {
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
 **accept** | **String**| This API is under preview and subject to change. | [default to &#39;application/vnd.github.machine-man-preview+json&#39;]
 **installationId** | **Number**| installation_id parameter | 
 **perPage** | **Number**| Results per page (max 100) | [optional] [default to 30]
 **page** | **Number**| Page number of the results to fetch. | [optional] [default to 1]

### Return type

[**AppsListInstallationReposForAuthenticatedUser200Response**](AppsListInstallationReposForAuthenticatedUser200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appsListInstallations

> [InstallationGhes2] appsListInstallations(accept, opts)

List installations for the authenticated app

You must use a [JWT](https://docs.github.com/enterprise-server@2.19/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-a-github-app) to access this endpoint.  The permissions the installation has are included under the &#x60;permissions&#x60; key.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.AppsApi();
let accept = "'application/vnd.github.machine-man-preview+json'"; // String | This API is under preview and subject to change.
let opts = {
  'perPage': 30, // Number | Results per page (max 100)
  'page': 1 // Number | Page number of the results to fetch.
};
apiInstance.appsListInstallations(accept, opts, (error, data, response) => {
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
 **accept** | **String**| This API is under preview and subject to change. | [default to &#39;application/vnd.github.machine-man-preview+json&#39;]
 **perPage** | **Number**| Results per page (max 100) | [optional] [default to 30]
 **page** | **Number**| Page number of the results to fetch. | [optional] [default to 1]

### Return type

[**[InstallationGhes2]**](InstallationGhes2.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appsListInstallationsForAuthenticatedUser

> OrgsListAppInstallations200Response appsListInstallationsForAuthenticatedUser(accept, opts)

List app installations accessible to the user access token

Lists installations of your GitHub App that the authenticated user has explicit permission (&#x60;:read&#x60;, &#x60;:write&#x60;, or &#x60;:admin&#x60;) to access.  You must use a [user-to-server OAuth access token](https://docs.github.com/enterprise-server@2.19/apps/building-github-apps/identifying-and-authorizing-users-for-github-apps/#identifying-users-on-your-site), created for a user who has authorized your GitHub App, to access this endpoint.  The authenticated user has explicit permission to access repositories they own, repositories where they are a collaborator, and repositories that they can access through an organization membership.  You can find the permissions for the installation under the &#x60;permissions&#x60; key.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.AppsApi();
let accept = "'application/vnd.github.machine-man-preview+json'"; // String | This API is under preview and subject to change.
let opts = {
  'perPage': 30, // Number | Results per page (max 100)
  'page': 1 // Number | Page number of the results to fetch.
};
apiInstance.appsListInstallationsForAuthenticatedUser(accept, opts, (error, data, response) => {
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
 **accept** | **String**| This API is under preview and subject to change. | [default to &#39;application/vnd.github.machine-man-preview+json&#39;]
 **perPage** | **Number**| Results per page (max 100) | [optional] [default to 30]
 **page** | **Number**| Page number of the results to fetch. | [optional] [default to 1]

### Return type

[**OrgsListAppInstallations200Response**](OrgsListAppInstallations200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appsListReposAccessibleToInstallation

> AppsListReposAccessibleToInstallation200Response appsListReposAccessibleToInstallation(accept, opts)

List repositories accessible to the app installation

List repositories that an app installation can access.  You must use an [installation access token](https://docs.github.com/enterprise-server@2.19/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-an-installation) to access this endpoint.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.AppsApi();
let accept = "'application/vnd.github.machine-man-preview+json'"; // String | This API is under preview and subject to change.
let opts = {
  'perPage': 30, // Number | Results per page (max 100)
  'page': 1 // Number | Page number of the results to fetch.
};
apiInstance.appsListReposAccessibleToInstallation(accept, opts, (error, data, response) => {
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
 **accept** | **String**| This API is under preview and subject to change. | [default to &#39;application/vnd.github.machine-man-preview+json&#39;]
 **perPage** | **Number**| Results per page (max 100) | [optional] [default to 30]
 **page** | **Number**| Page number of the results to fetch. | [optional] [default to 1]

### Return type

[**AppsListReposAccessibleToInstallation200Response**](AppsListReposAccessibleToInstallation200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appsRemoveRepoFromInstallation

> appsRemoveRepoFromInstallation(installationId, repositoryId)

Remove a repository from an app installation

Remove a single repository from an installation. The authenticated user must have admin access to the repository.  You must use a personal access token (which you can create via the [command line](https://docs.github.com/enterprise-server@2.19/github/authenticating-to-github/creating-a-personal-access-token) or [Basic Authentication](https://docs.github.com/enterprise-server@2.19/rest/overview/other-authentication-methods#basic-authentication)) to access this endpoint.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.AppsApi();
let installationId = 56; // Number | installation_id parameter
let repositoryId = 56; // Number | 
apiInstance.appsRemoveRepoFromInstallation(installationId, repositoryId, (error, data, response) => {
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
 **installationId** | **Number**| installation_id parameter | 
 **repositoryId** | **Number**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

