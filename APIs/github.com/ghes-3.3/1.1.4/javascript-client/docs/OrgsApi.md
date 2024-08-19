# GitHubV3RestApi.OrgsApi

All URIs are relative to *https://github.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**orgsCheckMembershipForUser**](OrgsApi.md#orgsCheckMembershipForUser) | **GET** /orgs/{org}/members/{username} | Check organization membership for a user
[**orgsCheckPublicMembershipForUser**](OrgsApi.md#orgsCheckPublicMembershipForUser) | **GET** /orgs/{org}/public_members/{username} | Check public organization membership for a user
[**orgsConvertMemberToOutsideCollaborator**](OrgsApi.md#orgsConvertMemberToOutsideCollaborator) | **PUT** /orgs/{org}/outside_collaborators/{username} | Convert an organization member to outside collaborator
[**orgsCreateWebhook**](OrgsApi.md#orgsCreateWebhook) | **POST** /orgs/{org}/hooks | Create an organization webhook
[**orgsDeleteWebhook**](OrgsApi.md#orgsDeleteWebhook) | **DELETE** /orgs/{org}/hooks/{hook_id} | Delete an organization webhook
[**orgsGet**](OrgsApi.md#orgsGet) | **GET** /orgs/{org} | Get an organization
[**orgsGetAuditLog**](OrgsApi.md#orgsGetAuditLog) | **GET** /orgs/{org}/audit-log | Get the audit log for an organization
[**orgsGetMembershipForAuthenticatedUser**](OrgsApi.md#orgsGetMembershipForAuthenticatedUser) | **GET** /user/memberships/orgs/{org} | Get an organization membership for the authenticated user
[**orgsGetMembershipForUser**](OrgsApi.md#orgsGetMembershipForUser) | **GET** /orgs/{org}/memberships/{username} | Get organization membership for a user
[**orgsGetWebhook**](OrgsApi.md#orgsGetWebhook) | **GET** /orgs/{org}/hooks/{hook_id} | Get an organization webhook
[**orgsGetWebhookConfigForOrg**](OrgsApi.md#orgsGetWebhookConfigForOrg) | **GET** /orgs/{org}/hooks/{hook_id}/config | Get a webhook configuration for an organization
[**orgsGetWebhookDelivery**](OrgsApi.md#orgsGetWebhookDelivery) | **GET** /orgs/{org}/hooks/{hook_id}/deliveries/{delivery_id} | Get a webhook delivery for an organization webhook
[**orgsList**](OrgsApi.md#orgsList) | **GET** /organizations | List organizations
[**orgsListAppInstallations**](OrgsApi.md#orgsListAppInstallations) | **GET** /orgs/{org}/installations | List app installations for an organization
[**orgsListForAuthenticatedUser**](OrgsApi.md#orgsListForAuthenticatedUser) | **GET** /user/orgs | List organizations for the authenticated user
[**orgsListForUser**](OrgsApi.md#orgsListForUser) | **GET** /users/{username}/orgs | List organizations for a user
[**orgsListMembers**](OrgsApi.md#orgsListMembers) | **GET** /orgs/{org}/members | List organization members
[**orgsListMembershipsForAuthenticatedUser**](OrgsApi.md#orgsListMembershipsForAuthenticatedUser) | **GET** /user/memberships/orgs | List organization memberships for the authenticated user
[**orgsListOutsideCollaborators**](OrgsApi.md#orgsListOutsideCollaborators) | **GET** /orgs/{org}/outside_collaborators | List outside collaborators for an organization
[**orgsListPublicMembers**](OrgsApi.md#orgsListPublicMembers) | **GET** /orgs/{org}/public_members | List public organization members
[**orgsListWebhookDeliveries**](OrgsApi.md#orgsListWebhookDeliveries) | **GET** /orgs/{org}/hooks/{hook_id}/deliveries | List deliveries for an organization webhook
[**orgsListWebhooks**](OrgsApi.md#orgsListWebhooks) | **GET** /orgs/{org}/hooks | List organization webhooks
[**orgsPingWebhook**](OrgsApi.md#orgsPingWebhook) | **POST** /orgs/{org}/hooks/{hook_id}/pings | Ping an organization webhook
[**orgsRedeliverWebhookDelivery**](OrgsApi.md#orgsRedeliverWebhookDelivery) | **POST** /orgs/{org}/hooks/{hook_id}/deliveries/{delivery_id}/attempts | Redeliver a delivery for an organization webhook
[**orgsRemoveMember**](OrgsApi.md#orgsRemoveMember) | **DELETE** /orgs/{org}/members/{username} | Remove an organization member
[**orgsRemoveMembershipForUser**](OrgsApi.md#orgsRemoveMembershipForUser) | **DELETE** /orgs/{org}/memberships/{username} | Remove organization membership for a user
[**orgsRemoveOutsideCollaborator**](OrgsApi.md#orgsRemoveOutsideCollaborator) | **DELETE** /orgs/{org}/outside_collaborators/{username} | Remove outside collaborator from an organization
[**orgsRemovePublicMembershipForAuthenticatedUser**](OrgsApi.md#orgsRemovePublicMembershipForAuthenticatedUser) | **DELETE** /orgs/{org}/public_members/{username} | Remove public organization membership for the authenticated user
[**orgsSetMembershipForUser**](OrgsApi.md#orgsSetMembershipForUser) | **PUT** /orgs/{org}/memberships/{username} | Set organization membership for a user
[**orgsSetPublicMembershipForAuthenticatedUser**](OrgsApi.md#orgsSetPublicMembershipForAuthenticatedUser) | **PUT** /orgs/{org}/public_members/{username} | Set public organization membership for the authenticated user
[**orgsUpdate**](OrgsApi.md#orgsUpdate) | **PATCH** /orgs/{org} | Update an organization
[**orgsUpdateMembershipForAuthenticatedUser**](OrgsApi.md#orgsUpdateMembershipForAuthenticatedUser) | **PATCH** /user/memberships/orgs/{org} | Update an organization membership for the authenticated user
[**orgsUpdateWebhook**](OrgsApi.md#orgsUpdateWebhook) | **PATCH** /orgs/{org}/hooks/{hook_id} | Update an organization webhook
[**orgsUpdateWebhookConfigForOrg**](OrgsApi.md#orgsUpdateWebhookConfigForOrg) | **PATCH** /orgs/{org}/hooks/{hook_id}/config | Update a webhook configuration for an organization



## orgsCheckMembershipForUser

> orgsCheckMembershipForUser(org, username)

Check organization membership for a user

Check if a user is, publicly or privately, a member of the organization.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.OrgsApi();
let org = "org_example"; // String | The organization name. The name is not case sensitive.
let username = "username_example"; // String | The handle for the GitHub user account.
apiInstance.orgsCheckMembershipForUser(org, username, (error, data, response) => {
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
 **org** | **String**| The organization name. The name is not case sensitive. | 
 **username** | **String**| The handle for the GitHub user account. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## orgsCheckPublicMembershipForUser

> orgsCheckPublicMembershipForUser(org, username)

Check public organization membership for a user



### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.OrgsApi();
let org = "org_example"; // String | The organization name. The name is not case sensitive.
let username = "username_example"; // String | The handle for the GitHub user account.
apiInstance.orgsCheckPublicMembershipForUser(org, username, (error, data, response) => {
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
 **org** | **String**| The organization name. The name is not case sensitive. | 
 **username** | **String**| The handle for the GitHub user account. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## orgsConvertMemberToOutsideCollaborator

> Object orgsConvertMemberToOutsideCollaborator(org, username, opts)

Convert an organization member to outside collaborator

When an organization member is converted to an outside collaborator, they&#39;ll only have access to the repositories that their current team membership allows. The user will no longer be a member of the organization. For more information, see \&quot;[Converting an organization member to an outside collaborator](https://docs.github.com/enterprise-server@3.3/articles/converting-an-organization-member-to-an-outside-collaborator/)\&quot;. Converting an organization member to an outside collaborator may be restricted by enterprise administrators. For more information, see \&quot;[Enforcing repository management policies in your enterprise](https://docs.github.com/enterprise-server@3.3/admin/policies/enforcing-policies-for-your-enterprise/enforcing-repository-management-policies-in-your-enterprise#enforcing-a-policy-for-inviting-outside-collaborators-to-repositories).\&quot;

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.OrgsApi();
let org = "org_example"; // String | The organization name. The name is not case sensitive.
let username = "username_example"; // String | The handle for the GitHub user account.
let opts = {
  'orgsConvertMemberToOutsideCollaboratorRequest': {"async":true} // OrgsConvertMemberToOutsideCollaboratorRequest | 
};
apiInstance.orgsConvertMemberToOutsideCollaborator(org, username, opts, (error, data, response) => {
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
 **username** | **String**| The handle for the GitHub user account. | 
 **orgsConvertMemberToOutsideCollaboratorRequest** | [**OrgsConvertMemberToOutsideCollaboratorRequest**](OrgsConvertMemberToOutsideCollaboratorRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## orgsCreateWebhook

> OrgHook orgsCreateWebhook(org, orgsCreateWebhookRequest)

Create an organization webhook

Here&#39;s how you can create a hook that posts payloads in JSON format:

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.OrgsApi();
let org = "org_example"; // String | The organization name. The name is not case sensitive.
let orgsCreateWebhookRequest = {"active":true,"config":{"content_type":"json","url":"http://example.com/webhook"},"events":["push","pull_request"],"name":"web"}; // OrgsCreateWebhookRequest | 
apiInstance.orgsCreateWebhook(org, orgsCreateWebhookRequest, (error, data, response) => {
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
 **orgsCreateWebhookRequest** | [**OrgsCreateWebhookRequest**](OrgsCreateWebhookRequest.md)|  | 

### Return type

[**OrgHook**](OrgHook.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## orgsDeleteWebhook

> orgsDeleteWebhook(org, hookId)

Delete an organization webhook



### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.OrgsApi();
let org = "org_example"; // String | The organization name. The name is not case sensitive.
let hookId = 56; // Number | The unique identifier of the hook.
apiInstance.orgsDeleteWebhook(org, hookId, (error, data, response) => {
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
 **org** | **String**| The organization name. The name is not case sensitive. | 
 **hookId** | **Number**| The unique identifier of the hook. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## orgsGet

> OrganizationFull orgsGet(org)

Get an organization

To see many of the organization response values, you need to be an authenticated organization owner with the &#x60;admin:org&#x60; scope. When the value of &#x60;two_factor_requirement_enabled&#x60; is &#x60;true&#x60;, the organization requires all members, billing managers, and outside collaborators to enable [two-factor authentication](https://docs.github.com/enterprise-server@3.3/articles/securing-your-account-with-two-factor-authentication-2fa/).  GitHub Apps with the &#x60;Organization plan&#x60; permission can use this endpoint to retrieve information about an organization&#39;s GitHub Enterprise Server plan. See \&quot;[Authenticating with GitHub Apps](https://docs.github.com/enterprise-server@3.3/apps/building-github-apps/authenticating-with-github-apps/)\&quot; for details. For an example response, see &#39;Response with GitHub Enterprise Server plan information&#39; below.\&quot;

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.OrgsApi();
let org = "org_example"; // String | The organization name. The name is not case sensitive.
apiInstance.orgsGet(org, (error, data, response) => {
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

[**OrganizationFull**](OrganizationFull.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## orgsGetAuditLog

> [AuditLogEvent] orgsGetAuditLog(org, opts)

Get the audit log for an organization

Gets the audit log for an organization. For more information, see \&quot;[Reviewing the audit log for your organization](https://docs.github.com/enterprise-server@3.3/github/setting-up-and-managing-organizations-and-teams/reviewing-the-audit-log-for-your-organization).\&quot;  To use this endpoint, you must be an organization owner, and you must use an access token with the &#x60;admin:org&#x60; scope. GitHub Apps must have the &#x60;organization_administration&#x60; read permission to use this endpoint.  By default, the response includes up to 30 events from the past three months. Use the &#x60;phrase&#x60; parameter to filter results and retrieve older events. For example, use the &#x60;phrase&#x60; parameter with the &#x60;created&#x60; qualifier to filter events based on when the events occurred. For more information, see \&quot;[Reviewing the audit log for your organization](https://docs.github.com/enterprise-server@3.3/organizations/keeping-your-organization-secure/managing-security-settings-for-your-organization/reviewing-the-audit-log-for-your-organization#searching-the-audit-log).\&quot;  Use pagination to retrieve fewer or more than 30 events. For more information, see \&quot;[Resources in the REST API](https://docs.github.com/enterprise-server@3.3/rest/overview/resources-in-the-rest-api#pagination).\&quot;

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.OrgsApi();
let org = "org_example"; // String | The organization name. The name is not case sensitive.
let opts = {
  'phrase': "phrase_example", // String | A search phrase. For more information, see [Searching the audit log](https://docs.github.com/enterprise-server@3.3/github/setting-up-and-managing-organizations-and-teams/reviewing-the-audit-log-for-your-organization#searching-the-audit-log).
  'after': "after_example", // String | A cursor, as given in the [Link header](https://docs.github.com/enterprise-server@3.3/rest/overview/resources-in-the-rest-api#link-header). If specified, the query only searches for events after this cursor.
  'before': "before_example", // String | A cursor, as given in the [Link header](https://docs.github.com/enterprise-server@3.3/rest/overview/resources-in-the-rest-api#link-header). If specified, the query only searches for events before this cursor.
  'order': "order_example", // String | The order of audit log events. To list newest events first, specify `desc`. To list oldest events first, specify `asc`.  The default is `desc`.
  'perPage': 30, // Number | The number of results per page (max 100).
  'page': 1 // Number | Page number of the results to fetch.
};
apiInstance.orgsGetAuditLog(org, opts, (error, data, response) => {
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
 **phrase** | **String**| A search phrase. For more information, see [Searching the audit log](https://docs.github.com/enterprise-server@3.3/github/setting-up-and-managing-organizations-and-teams/reviewing-the-audit-log-for-your-organization#searching-the-audit-log). | [optional] 
 **after** | **String**| A cursor, as given in the [Link header](https://docs.github.com/enterprise-server@3.3/rest/overview/resources-in-the-rest-api#link-header). If specified, the query only searches for events after this cursor. | [optional] 
 **before** | **String**| A cursor, as given in the [Link header](https://docs.github.com/enterprise-server@3.3/rest/overview/resources-in-the-rest-api#link-header). If specified, the query only searches for events before this cursor. | [optional] 
 **order** | **String**| The order of audit log events. To list newest events first, specify &#x60;desc&#x60;. To list oldest events first, specify &#x60;asc&#x60;.  The default is &#x60;desc&#x60;. | [optional] 
 **perPage** | **Number**| The number of results per page (max 100). | [optional] [default to 30]
 **page** | **Number**| Page number of the results to fetch. | [optional] [default to 1]

### Return type

[**[AuditLogEvent]**](AuditLogEvent.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## orgsGetMembershipForAuthenticatedUser

> OrgMembership orgsGetMembershipForAuthenticatedUser(org)

Get an organization membership for the authenticated user



### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.OrgsApi();
let org = "org_example"; // String | The organization name. The name is not case sensitive.
apiInstance.orgsGetMembershipForAuthenticatedUser(org, (error, data, response) => {
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

[**OrgMembership**](OrgMembership.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## orgsGetMembershipForUser

> OrgMembership orgsGetMembershipForUser(org, username)

Get organization membership for a user

In order to get a user&#39;s membership with an organization, the authenticated user must be an organization member. The &#x60;state&#x60; parameter in the response can be used to identify the user&#39;s membership status.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.OrgsApi();
let org = "org_example"; // String | The organization name. The name is not case sensitive.
let username = "username_example"; // String | The handle for the GitHub user account.
apiInstance.orgsGetMembershipForUser(org, username, (error, data, response) => {
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
 **username** | **String**| The handle for the GitHub user account. | 

### Return type

[**OrgMembership**](OrgMembership.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## orgsGetWebhook

> OrgHook orgsGetWebhook(org, hookId)

Get an organization webhook

Returns a webhook configured in an organization. To get only the webhook &#x60;config&#x60; properties, see \&quot;[Get a webhook configuration for an organization](/rest/reference/orgs#get-a-webhook-configuration-for-an-organization).\&quot;

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.OrgsApi();
let org = "org_example"; // String | The organization name. The name is not case sensitive.
let hookId = 56; // Number | The unique identifier of the hook.
apiInstance.orgsGetWebhook(org, hookId, (error, data, response) => {
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
 **hookId** | **Number**| The unique identifier of the hook. | 

### Return type

[**OrgHook**](OrgHook.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## orgsGetWebhookConfigForOrg

> WebhookConfig orgsGetWebhookConfigForOrg(org, hookId)

Get a webhook configuration for an organization

Returns the webhook configuration for an organization. To get more information about the webhook, including the &#x60;active&#x60; state and &#x60;events&#x60;, use \&quot;[Get an organization webhook ](/rest/reference/orgs#get-an-organization-webhook).\&quot;  Access tokens must have the &#x60;admin:org_hook&#x60; scope, and GitHub Apps must have the &#x60;organization_hooks:read&#x60; permission.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.OrgsApi();
let org = "org_example"; // String | The organization name. The name is not case sensitive.
let hookId = 56; // Number | The unique identifier of the hook.
apiInstance.orgsGetWebhookConfigForOrg(org, hookId, (error, data, response) => {
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
 **hookId** | **Number**| The unique identifier of the hook. | 

### Return type

[**WebhookConfig**](WebhookConfig.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## orgsGetWebhookDelivery

> HookDelivery orgsGetWebhookDelivery(org, hookId, deliveryId)

Get a webhook delivery for an organization webhook

Returns a delivery for a webhook configured in an organization.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.OrgsApi();
let org = "org_example"; // String | The organization name. The name is not case sensitive.
let hookId = 56; // Number | The unique identifier of the hook.
let deliveryId = 56; // Number | 
apiInstance.orgsGetWebhookDelivery(org, hookId, deliveryId, (error, data, response) => {
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
 **hookId** | **Number**| The unique identifier of the hook. | 
 **deliveryId** | **Number**|  | 

### Return type

[**HookDelivery**](HookDelivery.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/scim+json


## orgsList

> [OrganizationSimple] orgsList(opts)

List organizations

Lists all organizations, in the order that they were created on GitHub Enterprise Server.  **Note:** Pagination is powered exclusively by the &#x60;since&#x60; parameter. Use the [Link header](https://docs.github.com/enterprise-server@3.3/rest/overview/resources-in-the-rest-api#link-header) to get the URL for the next page of organizations.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.OrgsApi();
let opts = {
  'since': 56, // Number | An organization ID. Only return organizations with an ID greater than this ID.
  'perPage': 30 // Number | The number of results per page (max 100).
};
apiInstance.orgsList(opts, (error, data, response) => {
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
 **since** | **Number**| An organization ID. Only return organizations with an ID greater than this ID. | [optional] 
 **perPage** | **Number**| The number of results per page (max 100). | [optional] [default to 30]

### Return type

[**[OrganizationSimple]**](OrganizationSimple.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## orgsListAppInstallations

> OrgsListAppInstallations200Response orgsListAppInstallations(org, opts)

List app installations for an organization

Lists all GitHub Apps in an organization. The installation count includes all GitHub Apps installed on repositories in the organization. You must be an organization owner with &#x60;admin:read&#x60; scope to use this endpoint.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.OrgsApi();
let org = "org_example"; // String | The organization name. The name is not case sensitive.
let opts = {
  'perPage': 30, // Number | The number of results per page (max 100).
  'page': 1 // Number | Page number of the results to fetch.
};
apiInstance.orgsListAppInstallations(org, opts, (error, data, response) => {
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
 **perPage** | **Number**| The number of results per page (max 100). | [optional] [default to 30]
 **page** | **Number**| Page number of the results to fetch. | [optional] [default to 1]

### Return type

[**OrgsListAppInstallations200Response**](OrgsListAppInstallations200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## orgsListForAuthenticatedUser

> [OrganizationSimple] orgsListForAuthenticatedUser(opts)

List organizations for the authenticated user

List organizations for the authenticated user.  **OAuth scope requirements**  This only lists organizations that your authorization allows you to operate on in some way (e.g., you can list teams with &#x60;read:org&#x60; scope, you can publicize your organization membership with &#x60;user&#x60; scope, etc.). Therefore, this API requires at least &#x60;user&#x60; or &#x60;read:org&#x60; scope. OAuth requests with insufficient scope receive a &#x60;403 Forbidden&#x60; response.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.OrgsApi();
let opts = {
  'perPage': 30, // Number | The number of results per page (max 100).
  'page': 1 // Number | Page number of the results to fetch.
};
apiInstance.orgsListForAuthenticatedUser(opts, (error, data, response) => {
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

[**[OrganizationSimple]**](OrganizationSimple.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## orgsListForUser

> [OrganizationSimple] orgsListForUser(username, opts)

List organizations for a user

List [public organization memberships](https://docs.github.com/enterprise-server@3.3/articles/publicizing-or-concealing-organization-membership) for the specified user.  This method only lists _public_ memberships, regardless of authentication. If you need to fetch all of the organization memberships (public and private) for the authenticated user, use the [List organizations for the authenticated user](https://docs.github.com/enterprise-server@3.3/rest/reference/orgs#list-organizations-for-the-authenticated-user) API instead.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.OrgsApi();
let username = "username_example"; // String | The handle for the GitHub user account.
let opts = {
  'perPage': 30, // Number | The number of results per page (max 100).
  'page': 1 // Number | Page number of the results to fetch.
};
apiInstance.orgsListForUser(username, opts, (error, data, response) => {
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
 **perPage** | **Number**| The number of results per page (max 100). | [optional] [default to 30]
 **page** | **Number**| Page number of the results to fetch. | [optional] [default to 1]

### Return type

[**[OrganizationSimple]**](OrganizationSimple.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## orgsListMembers

> [SimpleUser] orgsListMembers(org, opts)

List organization members

List all users who are members of an organization. If the authenticated user is also a member of this organization then both concealed and public members will be returned.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.OrgsApi();
let org = "org_example"; // String | The organization name. The name is not case sensitive.
let opts = {
  'filter': "'all'", // String | Filter members returned in the list. `2fa_disabled` means that only members without [two-factor authentication](https://github.com/blog/1614-two-factor-authentication) enabled will be returned. This options is only available for organization owners.
  'role': "'all'", // String | Filter members returned by their role.
  'perPage': 30, // Number | The number of results per page (max 100).
  'page': 1 // Number | Page number of the results to fetch.
};
apiInstance.orgsListMembers(org, opts, (error, data, response) => {
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
 **filter** | **String**| Filter members returned in the list. &#x60;2fa_disabled&#x60; means that only members without [two-factor authentication](https://github.com/blog/1614-two-factor-authentication) enabled will be returned. This options is only available for organization owners. | [optional] [default to &#39;all&#39;]
 **role** | **String**| Filter members returned by their role. | [optional] [default to &#39;all&#39;]
 **perPage** | **Number**| The number of results per page (max 100). | [optional] [default to 30]
 **page** | **Number**| Page number of the results to fetch. | [optional] [default to 1]

### Return type

[**[SimpleUser]**](SimpleUser.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## orgsListMembershipsForAuthenticatedUser

> [OrgMembership] orgsListMembershipsForAuthenticatedUser(opts)

List organization memberships for the authenticated user



### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.OrgsApi();
let opts = {
  'state': "state_example", // String | Indicates the state of the memberships to return. If not specified, the API returns both active and pending memberships.
  'perPage': 30, // Number | The number of results per page (max 100).
  'page': 1 // Number | Page number of the results to fetch.
};
apiInstance.orgsListMembershipsForAuthenticatedUser(opts, (error, data, response) => {
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
 **state** | **String**| Indicates the state of the memberships to return. If not specified, the API returns both active and pending memberships. | [optional] 
 **perPage** | **Number**| The number of results per page (max 100). | [optional] [default to 30]
 **page** | **Number**| Page number of the results to fetch. | [optional] [default to 1]

### Return type

[**[OrgMembership]**](OrgMembership.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## orgsListOutsideCollaborators

> [SimpleUser] orgsListOutsideCollaborators(org, opts)

List outside collaborators for an organization

List all users who are outside collaborators of an organization.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.OrgsApi();
let org = "org_example"; // String | The organization name. The name is not case sensitive.
let opts = {
  'filter': "'all'", // String | Filter the list of outside collaborators. `2fa_disabled` means that only outside collaborators without [two-factor authentication](https://github.com/blog/1614-two-factor-authentication) enabled will be returned.
  'perPage': 30, // Number | The number of results per page (max 100).
  'page': 1 // Number | Page number of the results to fetch.
};
apiInstance.orgsListOutsideCollaborators(org, opts, (error, data, response) => {
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
 **filter** | **String**| Filter the list of outside collaborators. &#x60;2fa_disabled&#x60; means that only outside collaborators without [two-factor authentication](https://github.com/blog/1614-two-factor-authentication) enabled will be returned. | [optional] [default to &#39;all&#39;]
 **perPage** | **Number**| The number of results per page (max 100). | [optional] [default to 30]
 **page** | **Number**| Page number of the results to fetch. | [optional] [default to 1]

### Return type

[**[SimpleUser]**](SimpleUser.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## orgsListPublicMembers

> [SimpleUser] orgsListPublicMembers(org, opts)

List public organization members

Members of an organization can choose to have their membership publicized or not.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.OrgsApi();
let org = "org_example"; // String | The organization name. The name is not case sensitive.
let opts = {
  'perPage': 30, // Number | The number of results per page (max 100).
  'page': 1 // Number | Page number of the results to fetch.
};
apiInstance.orgsListPublicMembers(org, opts, (error, data, response) => {
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
 **perPage** | **Number**| The number of results per page (max 100). | [optional] [default to 30]
 **page** | **Number**| Page number of the results to fetch. | [optional] [default to 1]

### Return type

[**[SimpleUser]**](SimpleUser.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## orgsListWebhookDeliveries

> [HookDeliveryItem] orgsListWebhookDeliveries(org, hookId, opts)

List deliveries for an organization webhook

Returns a list of webhook deliveries for a webhook configured in an organization.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.OrgsApi();
let org = "org_example"; // String | The organization name. The name is not case sensitive.
let hookId = 56; // Number | The unique identifier of the hook.
let opts = {
  'perPage': 30, // Number | The number of results per page (max 100).
  'cursor': "cursor_example", // String | Used for pagination: the starting delivery from which the page of deliveries is fetched. Refer to the `link` header for the next and previous page cursors.
  'redelivery': true // Boolean | 
};
apiInstance.orgsListWebhookDeliveries(org, hookId, opts, (error, data, response) => {
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
 **hookId** | **Number**| The unique identifier of the hook. | 
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


## orgsListWebhooks

> [OrgHook] orgsListWebhooks(org, opts)

List organization webhooks



### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.OrgsApi();
let org = "org_example"; // String | The organization name. The name is not case sensitive.
let opts = {
  'perPage': 30, // Number | The number of results per page (max 100).
  'page': 1 // Number | Page number of the results to fetch.
};
apiInstance.orgsListWebhooks(org, opts, (error, data, response) => {
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
 **perPage** | **Number**| The number of results per page (max 100). | [optional] [default to 30]
 **page** | **Number**| Page number of the results to fetch. | [optional] [default to 1]

### Return type

[**[OrgHook]**](OrgHook.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## orgsPingWebhook

> orgsPingWebhook(org, hookId)

Ping an organization webhook

This will trigger a [ping event](https://docs.github.com/enterprise-server@3.3/webhooks/#ping-event) to be sent to the hook.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.OrgsApi();
let org = "org_example"; // String | The organization name. The name is not case sensitive.
let hookId = 56; // Number | The unique identifier of the hook.
apiInstance.orgsPingWebhook(org, hookId, (error, data, response) => {
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
 **org** | **String**| The organization name. The name is not case sensitive. | 
 **hookId** | **Number**| The unique identifier of the hook. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## orgsRedeliverWebhookDelivery

> Object orgsRedeliverWebhookDelivery(org, hookId, deliveryId)

Redeliver a delivery for an organization webhook

Redeliver a delivery for a webhook configured in an organization.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.OrgsApi();
let org = "org_example"; // String | The organization name. The name is not case sensitive.
let hookId = 56; // Number | The unique identifier of the hook.
let deliveryId = 56; // Number | 
apiInstance.orgsRedeliverWebhookDelivery(org, hookId, deliveryId, (error, data, response) => {
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
 **hookId** | **Number**| The unique identifier of the hook. | 
 **deliveryId** | **Number**|  | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/scim+json


## orgsRemoveMember

> orgsRemoveMember(org, username)

Remove an organization member

Removing a user from this list will remove them from all teams and they will no longer have any access to the organization&#39;s repositories.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.OrgsApi();
let org = "org_example"; // String | The organization name. The name is not case sensitive.
let username = "username_example"; // String | The handle for the GitHub user account.
apiInstance.orgsRemoveMember(org, username, (error, data, response) => {
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
 **org** | **String**| The organization name. The name is not case sensitive. | 
 **username** | **String**| The handle for the GitHub user account. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## orgsRemoveMembershipForUser

> orgsRemoveMembershipForUser(org, username)

Remove organization membership for a user

In order to remove a user&#39;s membership with an organization, the authenticated user must be an organization owner.  If the specified user is an active member of the organization, this will remove them from the organization. If the specified user has been invited to the organization, this will cancel their invitation. The specified user will receive an email notification in both cases.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.OrgsApi();
let org = "org_example"; // String | The organization name. The name is not case sensitive.
let username = "username_example"; // String | The handle for the GitHub user account.
apiInstance.orgsRemoveMembershipForUser(org, username, (error, data, response) => {
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
 **org** | **String**| The organization name. The name is not case sensitive. | 
 **username** | **String**| The handle for the GitHub user account. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## orgsRemoveOutsideCollaborator

> orgsRemoveOutsideCollaborator(org, username)

Remove outside collaborator from an organization

Removing a user from this list will remove them from all the organization&#39;s repositories.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.OrgsApi();
let org = "org_example"; // String | The organization name. The name is not case sensitive.
let username = "username_example"; // String | The handle for the GitHub user account.
apiInstance.orgsRemoveOutsideCollaborator(org, username, (error, data, response) => {
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
 **org** | **String**| The organization name. The name is not case sensitive. | 
 **username** | **String**| The handle for the GitHub user account. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## orgsRemovePublicMembershipForAuthenticatedUser

> orgsRemovePublicMembershipForAuthenticatedUser(org, username)

Remove public organization membership for the authenticated user



### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.OrgsApi();
let org = "org_example"; // String | The organization name. The name is not case sensitive.
let username = "username_example"; // String | The handle for the GitHub user account.
apiInstance.orgsRemovePublicMembershipForAuthenticatedUser(org, username, (error, data, response) => {
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
 **org** | **String**| The organization name. The name is not case sensitive. | 
 **username** | **String**| The handle for the GitHub user account. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## orgsSetMembershipForUser

> OrgMembership orgsSetMembershipForUser(org, username, opts)

Set organization membership for a user

Only authenticated organization owners can add a member to the organization or update the member&#39;s role.  *   If the authenticated user is _adding_ a member to the organization, the invited user will receive an email inviting them to the organization. The user&#39;s [membership status](https://docs.github.com/enterprise-server@3.3/rest/reference/orgs#get-organization-membership-for-a-user) will be &#x60;pending&#x60; until they accept the invitation.      *   Authenticated users can _update_ a user&#39;s membership by passing the &#x60;role&#x60; parameter. If the authenticated user changes a member&#39;s role to &#x60;admin&#x60;, the affected user will receive an email notifying them that they&#39;ve been made an organization owner. If the authenticated user changes an owner&#39;s role to &#x60;member&#x60;, no email will be sent.  **Rate limits**  To prevent abuse, the authenticated user is limited to 50 organization invitations per 24 hour period. If the organization is more than one month old or on a paid plan, the limit is 500 invitations per 24 hour period.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.OrgsApi();
let org = "org_example"; // String | The organization name. The name is not case sensitive.
let username = "username_example"; // String | The handle for the GitHub user account.
let opts = {
  'orgsSetMembershipForUserRequest': {"role":"member"} // OrgsSetMembershipForUserRequest | 
};
apiInstance.orgsSetMembershipForUser(org, username, opts, (error, data, response) => {
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
 **username** | **String**| The handle for the GitHub user account. | 
 **orgsSetMembershipForUserRequest** | [**OrgsSetMembershipForUserRequest**](OrgsSetMembershipForUserRequest.md)|  | [optional] 

### Return type

[**OrgMembership**](OrgMembership.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## orgsSetPublicMembershipForAuthenticatedUser

> orgsSetPublicMembershipForAuthenticatedUser(org, username)

Set public organization membership for the authenticated user

The user can publicize their own membership. (A user cannot publicize the membership for another user.)  Note that you&#39;ll need to set &#x60;Content-Length&#x60; to zero when calling out to this endpoint. For more information, see \&quot;[HTTP verbs](https://docs.github.com/enterprise-server@3.3/rest/overview/resources-in-the-rest-api#http-verbs).\&quot;

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.OrgsApi();
let org = "org_example"; // String | The organization name. The name is not case sensitive.
let username = "username_example"; // String | The handle for the GitHub user account.
apiInstance.orgsSetPublicMembershipForAuthenticatedUser(org, username, (error, data, response) => {
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
 **org** | **String**| The organization name. The name is not case sensitive. | 
 **username** | **String**| The handle for the GitHub user account. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## orgsUpdate

> OrganizationFull orgsUpdate(org, opts)

Update an organization

**Parameter Deprecation Notice:** GitHub Enterprise Server will replace and discontinue &#x60;members_allowed_repository_creation_type&#x60; in favor of more granular permissions. The new input parameters are &#x60;members_can_create_public_repositories&#x60;, &#x60;members_can_create_private_repositories&#x60; for all organizations and &#x60;members_can_create_internal_repositories&#x60; for organizations associated with an enterprise account using GitHub Enterprise Cloud or GitHub Enterprise Server 2.20+. For more information, see the [blog post](https://developer.github.com/changes/2019-12-03-internal-visibility-changes).  Enables an authenticated organization owner with the &#x60;admin:org&#x60; scope to update the organization&#39;s profile and member privileges.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.OrgsApi();
let org = "org_example"; // String | The organization name. The name is not case sensitive.
let opts = {
  'orgsUpdateRequest': {"billing_email":"mona@github.com","company":"GitHub","default_repository_permission":"read","description":"GitHub, the company.","email":"mona@github.com","location":"San Francisco","members_allowed_repository_creation_type":"all","members_can_create_repositories":true,"name":"github","twitter_username":"github"} // OrgsUpdateRequest | 
};
apiInstance.orgsUpdate(org, opts, (error, data, response) => {
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
 **orgsUpdateRequest** | [**OrgsUpdateRequest**](OrgsUpdateRequest.md)|  | [optional] 

### Return type

[**OrganizationFull**](OrganizationFull.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## orgsUpdateMembershipForAuthenticatedUser

> OrgMembership orgsUpdateMembershipForAuthenticatedUser(org, orgsUpdateMembershipForAuthenticatedUserRequest)

Update an organization membership for the authenticated user



### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.OrgsApi();
let org = "org_example"; // String | The organization name. The name is not case sensitive.
let orgsUpdateMembershipForAuthenticatedUserRequest = {"state":"active"}; // OrgsUpdateMembershipForAuthenticatedUserRequest | 
apiInstance.orgsUpdateMembershipForAuthenticatedUser(org, orgsUpdateMembershipForAuthenticatedUserRequest, (error, data, response) => {
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
 **orgsUpdateMembershipForAuthenticatedUserRequest** | [**OrgsUpdateMembershipForAuthenticatedUserRequest**](OrgsUpdateMembershipForAuthenticatedUserRequest.md)|  | 

### Return type

[**OrgMembership**](OrgMembership.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## orgsUpdateWebhook

> OrgHook orgsUpdateWebhook(org, hookId, opts)

Update an organization webhook

Updates a webhook configured in an organization. When you update a webhook, the &#x60;secret&#x60; will be overwritten. If you previously had a &#x60;secret&#x60; set, you must provide the same &#x60;secret&#x60; or set a new &#x60;secret&#x60; or the secret will be removed. If you are only updating individual webhook &#x60;config&#x60; properties, use \&quot;[Update a webhook configuration for an organization](/rest/reference/orgs#update-a-webhook-configuration-for-an-organization).\&quot;

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.OrgsApi();
let org = "org_example"; // String | The organization name. The name is not case sensitive.
let hookId = 56; // Number | The unique identifier of the hook.
let opts = {
  'orgsUpdateWebhookRequest': {"active":true,"events":["pull_request"]} // OrgsUpdateWebhookRequest | 
};
apiInstance.orgsUpdateWebhook(org, hookId, opts, (error, data, response) => {
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
 **hookId** | **Number**| The unique identifier of the hook. | 
 **orgsUpdateWebhookRequest** | [**OrgsUpdateWebhookRequest**](OrgsUpdateWebhookRequest.md)|  | [optional] 

### Return type

[**OrgHook**](OrgHook.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## orgsUpdateWebhookConfigForOrg

> WebhookConfig orgsUpdateWebhookConfigForOrg(org, hookId, opts)

Update a webhook configuration for an organization

Updates the webhook configuration for an organization. To update more information about the webhook, including the &#x60;active&#x60; state and &#x60;events&#x60;, use \&quot;[Update an organization webhook ](/rest/reference/orgs#update-an-organization-webhook).\&quot;  Access tokens must have the &#x60;admin:org_hook&#x60; scope, and GitHub Apps must have the &#x60;organization_hooks:write&#x60; permission.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.OrgsApi();
let org = "org_example"; // String | The organization name. The name is not case sensitive.
let hookId = 56; // Number | The unique identifier of the hook.
let opts = {
  'appsUpdateWebhookConfigForAppRequest': {"content_type":"json","insecure_ssl":"0","secret":"********","url":"http://example.com/webhook"} // AppsUpdateWebhookConfigForAppRequest | 
};
apiInstance.orgsUpdateWebhookConfigForOrg(org, hookId, opts, (error, data, response) => {
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
 **hookId** | **Number**| The unique identifier of the hook. | 
 **appsUpdateWebhookConfigForAppRequest** | [**AppsUpdateWebhookConfigForAppRequest**](AppsUpdateWebhookConfigForAppRequest.md)|  | [optional] 

### Return type

[**WebhookConfig**](WebhookConfig.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

