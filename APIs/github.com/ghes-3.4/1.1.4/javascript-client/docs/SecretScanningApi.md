# GitHubV3RestApi.SecretScanningApi

All URIs are relative to *https://github.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**secretScanningGetAlert**](SecretScanningApi.md#secretScanningGetAlert) | **GET** /repos/{owner}/{repo}/secret-scanning/alerts/{alert_number} | Get a secret scanning alert
[**secretScanningListAlertsForEnterprise**](SecretScanningApi.md#secretScanningListAlertsForEnterprise) | **GET** /enterprises/{enterprise}/secret-scanning/alerts | List secret scanning alerts for an enterprise
[**secretScanningListAlertsForOrg**](SecretScanningApi.md#secretScanningListAlertsForOrg) | **GET** /orgs/{org}/secret-scanning/alerts | List secret scanning alerts for an organization
[**secretScanningListAlertsForRepo**](SecretScanningApi.md#secretScanningListAlertsForRepo) | **GET** /repos/{owner}/{repo}/secret-scanning/alerts | List secret scanning alerts for a repository
[**secretScanningListLocationsForAlert**](SecretScanningApi.md#secretScanningListLocationsForAlert) | **GET** /repos/{owner}/{repo}/secret-scanning/alerts/{alert_number}/locations | List locations for a secret scanning alert
[**secretScanningUpdateAlert**](SecretScanningApi.md#secretScanningUpdateAlert) | **PATCH** /repos/{owner}/{repo}/secret-scanning/alerts/{alert_number} | Update a secret scanning alert



## secretScanningGetAlert

> SecretScanningAlert secretScanningGetAlert(owner, repo, alertNumber)

Get a secret scanning alert

Gets a single secret scanning alert detected in a private repository. To use this endpoint, you must be an administrator for the repository or organization, and you must use an access token with the &#x60;repo&#x60; scope or &#x60;security_events&#x60; scope.  GitHub Apps must have the &#x60;secret_scanning_alerts&#x60; read permission to use this endpoint.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.SecretScanningApi();
let owner = "owner_example"; // String | The account owner of the repository. The name is not case sensitive.
let repo = "repo_example"; // String | The name of the repository. The name is not case sensitive.
let alertNumber = 56; // Number | The number that identifies an alert. You can find this at the end of the URL for a code scanning alert within GitHub, and in the `number` field in the response from the `GET /repos/{owner}/{repo}/code-scanning/alerts` operation.
apiInstance.secretScanningGetAlert(owner, repo, alertNumber, (error, data, response) => {
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
 **alertNumber** | **Number**| The number that identifies an alert. You can find this at the end of the URL for a code scanning alert within GitHub, and in the &#x60;number&#x60; field in the response from the &#x60;GET /repos/{owner}/{repo}/code-scanning/alerts&#x60; operation. | 

### Return type

[**SecretScanningAlert**](SecretScanningAlert.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## secretScanningListAlertsForEnterprise

> [OrganizationSecretScanningAlert] secretScanningListAlertsForEnterprise(enterprise, opts)

List secret scanning alerts for an enterprise

Lists secret scanning alerts for eligible repositories in an enterprise, from newest to oldest. To use this endpoint, you must be a member of the enterprise, and you must use an access token with the &#x60;repo&#x60; scope or &#x60;security_events&#x60; scope. Alerts are only returned for organizations in the enterprise for which you are an organization owner or a [security manager](https://docs.github.com/enterprise-server@3.4/organizations/managing-peoples-access-to-your-organization-with-roles/managing-security-managers-in-your-organization).

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.SecretScanningApi();
let enterprise = "enterprise_example"; // String | The slug version of the enterprise name. You can also substitute this value with the enterprise id.
let opts = {
  'state': "state_example", // String | Set to `open` or `resolved` to only list secret scanning alerts in a specific state.
  'secretType': "secretType_example", // String | A comma-separated list of secret types to return. By default all secret types are returned. See \"[Secret scanning patterns](https://docs.github.com/enterprise-server@3.4/code-security/secret-scanning/secret-scanning-patterns#supported-secrets-for-advanced-security)\" for a complete list of secret types.
  'resolution': "resolution_example", // String | A comma-separated list of resolutions. Only secret scanning alerts with one of these resolutions are listed. Valid resolutions are `false_positive`, `wont_fix`, `revoked`, `pattern_edited`, `pattern_deleted` or `used_in_tests`.
  'perPage': 30, // Number | The number of results per page (max 100).
  'before': "before_example", // String | A cursor, as given in the [Link header](https://docs.github.com/enterprise-server@3.4/rest/overview/resources-in-the-rest-api#link-header). If specified, the query only searches for results before this cursor.
  'after': "after_example" // String | A cursor, as given in the [Link header](https://docs.github.com/enterprise-server@3.4/rest/overview/resources-in-the-rest-api#link-header). If specified, the query only searches for results after this cursor.
};
apiInstance.secretScanningListAlertsForEnterprise(enterprise, opts, (error, data, response) => {
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
 **enterprise** | **String**| The slug version of the enterprise name. You can also substitute this value with the enterprise id. | 
 **state** | **String**| Set to &#x60;open&#x60; or &#x60;resolved&#x60; to only list secret scanning alerts in a specific state. | [optional] 
 **secretType** | **String**| A comma-separated list of secret types to return. By default all secret types are returned. See \&quot;[Secret scanning patterns](https://docs.github.com/enterprise-server@3.4/code-security/secret-scanning/secret-scanning-patterns#supported-secrets-for-advanced-security)\&quot; for a complete list of secret types. | [optional] 
 **resolution** | **String**| A comma-separated list of resolutions. Only secret scanning alerts with one of these resolutions are listed. Valid resolutions are &#x60;false_positive&#x60;, &#x60;wont_fix&#x60;, &#x60;revoked&#x60;, &#x60;pattern_edited&#x60;, &#x60;pattern_deleted&#x60; or &#x60;used_in_tests&#x60;. | [optional] 
 **perPage** | **Number**| The number of results per page (max 100). | [optional] [default to 30]
 **before** | **String**| A cursor, as given in the [Link header](https://docs.github.com/enterprise-server@3.4/rest/overview/resources-in-the-rest-api#link-header). If specified, the query only searches for results before this cursor. | [optional] 
 **after** | **String**| A cursor, as given in the [Link header](https://docs.github.com/enterprise-server@3.4/rest/overview/resources-in-the-rest-api#link-header). If specified, the query only searches for results after this cursor. | [optional] 

### Return type

[**[OrganizationSecretScanningAlert]**](OrganizationSecretScanningAlert.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## secretScanningListAlertsForOrg

> [OrganizationSecretScanningAlert] secretScanningListAlertsForOrg(org, opts)

List secret scanning alerts for an organization

Lists secret scanning alerts for eligible repositories in an organization, from newest to oldest. To use this endpoint, you must be an administrator or security manager for the organization, and you must use an access token with the &#x60;repo&#x60; scope or &#x60;security_events&#x60; scope.  GitHub Apps must have the &#x60;secret_scanning_alerts&#x60; read permission to use this endpoint.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.SecretScanningApi();
let org = "org_example"; // String | The organization name. The name is not case sensitive.
let opts = {
  'state': "state_example", // String | Set to `open` or `resolved` to only list secret scanning alerts in a specific state.
  'secretType': "secretType_example", // String | A comma-separated list of secret types to return. By default all secret types are returned. See \"[Secret scanning patterns](https://docs.github.com/enterprise-server@3.4/code-security/secret-scanning/secret-scanning-patterns#supported-secrets-for-advanced-security)\" for a complete list of secret types.
  'resolution': "resolution_example", // String | A comma-separated list of resolutions. Only secret scanning alerts with one of these resolutions are listed. Valid resolutions are `false_positive`, `wont_fix`, `revoked`, `pattern_edited`, `pattern_deleted` or `used_in_tests`.
  'page': 1, // Number | Page number of the results to fetch.
  'perPage': 30 // Number | The number of results per page (max 100).
};
apiInstance.secretScanningListAlertsForOrg(org, opts, (error, data, response) => {
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
 **state** | **String**| Set to &#x60;open&#x60; or &#x60;resolved&#x60; to only list secret scanning alerts in a specific state. | [optional] 
 **secretType** | **String**| A comma-separated list of secret types to return. By default all secret types are returned. See \&quot;[Secret scanning patterns](https://docs.github.com/enterprise-server@3.4/code-security/secret-scanning/secret-scanning-patterns#supported-secrets-for-advanced-security)\&quot; for a complete list of secret types. | [optional] 
 **resolution** | **String**| A comma-separated list of resolutions. Only secret scanning alerts with one of these resolutions are listed. Valid resolutions are &#x60;false_positive&#x60;, &#x60;wont_fix&#x60;, &#x60;revoked&#x60;, &#x60;pattern_edited&#x60;, &#x60;pattern_deleted&#x60; or &#x60;used_in_tests&#x60;. | [optional] 
 **page** | **Number**| Page number of the results to fetch. | [optional] [default to 1]
 **perPage** | **Number**| The number of results per page (max 100). | [optional] [default to 30]

### Return type

[**[OrganizationSecretScanningAlert]**](OrganizationSecretScanningAlert.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## secretScanningListAlertsForRepo

> [SecretScanningAlert] secretScanningListAlertsForRepo(owner, repo, opts)

List secret scanning alerts for a repository

Lists secret scanning alerts for a private repository, from newest to oldest. To use this endpoint, you must be an administrator for the repository or organization, and you must use an access token with the &#x60;repo&#x60; scope or &#x60;security_events&#x60; scope.  GitHub Apps must have the &#x60;secret_scanning_alerts&#x60; read permission to use this endpoint.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.SecretScanningApi();
let owner = "owner_example"; // String | The account owner of the repository. The name is not case sensitive.
let repo = "repo_example"; // String | The name of the repository. The name is not case sensitive.
let opts = {
  'state': "state_example", // String | Set to `open` or `resolved` to only list secret scanning alerts in a specific state.
  'secretType': "secretType_example", // String | A comma-separated list of secret types to return. By default all secret types are returned. See \"[Secret scanning patterns](https://docs.github.com/enterprise-server@3.4/code-security/secret-scanning/secret-scanning-patterns#supported-secrets-for-advanced-security)\" for a complete list of secret types.
  'resolution': "resolution_example", // String | A comma-separated list of resolutions. Only secret scanning alerts with one of these resolutions are listed. Valid resolutions are `false_positive`, `wont_fix`, `revoked`, `pattern_edited`, `pattern_deleted` or `used_in_tests`.
  'page': 1, // Number | Page number of the results to fetch.
  'perPage': 30 // Number | The number of results per page (max 100).
};
apiInstance.secretScanningListAlertsForRepo(owner, repo, opts, (error, data, response) => {
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
 **state** | **String**| Set to &#x60;open&#x60; or &#x60;resolved&#x60; to only list secret scanning alerts in a specific state. | [optional] 
 **secretType** | **String**| A comma-separated list of secret types to return. By default all secret types are returned. See \&quot;[Secret scanning patterns](https://docs.github.com/enterprise-server@3.4/code-security/secret-scanning/secret-scanning-patterns#supported-secrets-for-advanced-security)\&quot; for a complete list of secret types. | [optional] 
 **resolution** | **String**| A comma-separated list of resolutions. Only secret scanning alerts with one of these resolutions are listed. Valid resolutions are &#x60;false_positive&#x60;, &#x60;wont_fix&#x60;, &#x60;revoked&#x60;, &#x60;pattern_edited&#x60;, &#x60;pattern_deleted&#x60; or &#x60;used_in_tests&#x60;. | [optional] 
 **page** | **Number**| Page number of the results to fetch. | [optional] [default to 1]
 **perPage** | **Number**| The number of results per page (max 100). | [optional] [default to 30]

### Return type

[**[SecretScanningAlert]**](SecretScanningAlert.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## secretScanningListLocationsForAlert

> [SecretScanningLocation] secretScanningListLocationsForAlert(owner, repo, alertNumber, opts)

List locations for a secret scanning alert

Lists all locations for a given secret scanning alert for a private repository. To use this endpoint, you must be an administrator for the repository or organization, and you must use an access token with the &#x60;repo&#x60; scope or &#x60;security_events&#x60; scope.  GitHub Apps must have the &#x60;secret_scanning_alerts&#x60; read permission to use this endpoint.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.SecretScanningApi();
let owner = "owner_example"; // String | The account owner of the repository. The name is not case sensitive.
let repo = "repo_example"; // String | The name of the repository. The name is not case sensitive.
let alertNumber = 56; // Number | The number that identifies an alert. You can find this at the end of the URL for a code scanning alert within GitHub, and in the `number` field in the response from the `GET /repos/{owner}/{repo}/code-scanning/alerts` operation.
let opts = {
  'page': 1, // Number | Page number of the results to fetch.
  'perPage': 30 // Number | The number of results per page (max 100).
};
apiInstance.secretScanningListLocationsForAlert(owner, repo, alertNumber, opts, (error, data, response) => {
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
 **alertNumber** | **Number**| The number that identifies an alert. You can find this at the end of the URL for a code scanning alert within GitHub, and in the &#x60;number&#x60; field in the response from the &#x60;GET /repos/{owner}/{repo}/code-scanning/alerts&#x60; operation. | 
 **page** | **Number**| Page number of the results to fetch. | [optional] [default to 1]
 **perPage** | **Number**| The number of results per page (max 100). | [optional] [default to 30]

### Return type

[**[SecretScanningLocation]**](SecretScanningLocation.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## secretScanningUpdateAlert

> SecretScanningAlert secretScanningUpdateAlert(owner, repo, alertNumber, secretScanningUpdateAlertRequest)

Update a secret scanning alert

Updates the status of a secret scanning alert in a private repository. To use this endpoint, you must be an administrator for the repository or organization, and you must use an access token with the &#x60;repo&#x60; scope or &#x60;security_events&#x60; scope.  GitHub Apps must have the &#x60;secret_scanning_alerts&#x60; write permission to use this endpoint.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.SecretScanningApi();
let owner = "owner_example"; // String | The account owner of the repository. The name is not case sensitive.
let repo = "repo_example"; // String | The name of the repository. The name is not case sensitive.
let alertNumber = 56; // Number | The number that identifies an alert. You can find this at the end of the URL for a code scanning alert within GitHub, and in the `number` field in the response from the `GET /repos/{owner}/{repo}/code-scanning/alerts` operation.
let secretScanningUpdateAlertRequest = {"resolution":"false_positive","state":"resolved"}; // SecretScanningUpdateAlertRequest | 
apiInstance.secretScanningUpdateAlert(owner, repo, alertNumber, secretScanningUpdateAlertRequest, (error, data, response) => {
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
 **alertNumber** | **Number**| The number that identifies an alert. You can find this at the end of the URL for a code scanning alert within GitHub, and in the &#x60;number&#x60; field in the response from the &#x60;GET /repos/{owner}/{repo}/code-scanning/alerts&#x60; operation. | 
 **secretScanningUpdateAlertRequest** | [**SecretScanningUpdateAlertRequest**](SecretScanningUpdateAlertRequest.md)|  | 

### Return type

[**SecretScanningAlert**](SecretScanningAlert.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

