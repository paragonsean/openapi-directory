# SecretScanningApi

All URIs are relative to *https://github.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**secretScanningGetAlert**](SecretScanningApi.md#secretScanningGetAlert) | **GET** /repos/{owner}/{repo}/secret-scanning/alerts/{alert_number} | Get a secret scanning alert |
| [**secretScanningListAlertsForEnterprise**](SecretScanningApi.md#secretScanningListAlertsForEnterprise) | **GET** /enterprises/{enterprise}/secret-scanning/alerts | List secret scanning alerts for an enterprise |
| [**secretScanningListAlertsForOrg**](SecretScanningApi.md#secretScanningListAlertsForOrg) | **GET** /orgs/{org}/secret-scanning/alerts | List secret scanning alerts for an organization |
| [**secretScanningListAlertsForRepo**](SecretScanningApi.md#secretScanningListAlertsForRepo) | **GET** /repos/{owner}/{repo}/secret-scanning/alerts | List secret scanning alerts for a repository |
| [**secretScanningListLocationsForAlert**](SecretScanningApi.md#secretScanningListLocationsForAlert) | **GET** /repos/{owner}/{repo}/secret-scanning/alerts/{alert_number}/locations | List locations for a secret scanning alert |
| [**secretScanningUpdateAlert**](SecretScanningApi.md#secretScanningUpdateAlert) | **PATCH** /repos/{owner}/{repo}/secret-scanning/alerts/{alert_number} | Update a secret scanning alert |


<a id="secretScanningGetAlert"></a>
# **secretScanningGetAlert**
> SecretScanningAlert secretScanningGetAlert(owner, repo, alertNumber)

Get a secret scanning alert

Gets a single secret scanning alert detected in a private repository. To use this endpoint, you must be an administrator for the repository or organization, and you must use an access token with the &#x60;repo&#x60; scope or &#x60;security_events&#x60; scope.  GitHub Apps must have the &#x60;secret_scanning_alerts&#x60; read permission to use this endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SecretScanningApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    SecretScanningApi apiInstance = new SecretScanningApi(defaultClient);
    String owner = "owner_example"; // String | The account owner of the repository. The name is not case sensitive.
    String repo = "repo_example"; // String | The name of the repository. The name is not case sensitive.
    Integer alertNumber = 56; // Integer | The number that identifies an alert. You can find this at the end of the URL for a code scanning alert within GitHub, and in the `number` field in the response from the `GET /repos/{owner}/{repo}/code-scanning/alerts` operation.
    try {
      SecretScanningAlert result = apiInstance.secretScanningGetAlert(owner, repo, alertNumber);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SecretScanningApi#secretScanningGetAlert");
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
| **owner** | **String**| The account owner of the repository. The name is not case sensitive. | |
| **repo** | **String**| The name of the repository. The name is not case sensitive. | |
| **alertNumber** | **Integer**| The number that identifies an alert. You can find this at the end of the URL for a code scanning alert within GitHub, and in the &#x60;number&#x60; field in the response from the &#x60;GET /repos/{owner}/{repo}/code-scanning/alerts&#x60; operation. | |

### Return type

[**SecretScanningAlert**](SecretScanningAlert.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |
| **304** | Not modified |  -  |
| **404** | Repository is public, or secret scanning is disabled for the repository, or the resource is not found |  -  |
| **503** | Service unavailable |  -  |

<a id="secretScanningListAlertsForEnterprise"></a>
# **secretScanningListAlertsForEnterprise**
> List&lt;OrganizationSecretScanningAlert&gt; secretScanningListAlertsForEnterprise(enterprise, state, secretType, resolution, perPage, before, after)

List secret scanning alerts for an enterprise

Lists secret scanning alerts for eligible repositories in an enterprise, from newest to oldest. To use this endpoint, you must be a member of the enterprise, and you must use an access token with the &#x60;repo&#x60; scope or &#x60;security_events&#x60; scope. Alerts are only returned for organizations in the enterprise for which you are an organization owner or a [security manager](https://docs.github.com/enterprise-server@3.4/organizations/managing-peoples-access-to-your-organization-with-roles/managing-security-managers-in-your-organization).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SecretScanningApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    SecretScanningApi apiInstance = new SecretScanningApi(defaultClient);
    String enterprise = "enterprise_example"; // String | The slug version of the enterprise name. You can also substitute this value with the enterprise id.
    String state = "open"; // String | Set to `open` or `resolved` to only list secret scanning alerts in a specific state.
    String secretType = "secretType_example"; // String | A comma-separated list of secret types to return. By default all secret types are returned. See \"[Secret scanning patterns](https://docs.github.com/enterprise-server@3.4/code-security/secret-scanning/secret-scanning-patterns#supported-secrets-for-advanced-security)\" for a complete list of secret types.
    String resolution = "resolution_example"; // String | A comma-separated list of resolutions. Only secret scanning alerts with one of these resolutions are listed. Valid resolutions are `false_positive`, `wont_fix`, `revoked`, `pattern_edited`, `pattern_deleted` or `used_in_tests`.
    Integer perPage = 30; // Integer | The number of results per page (max 100).
    String before = "before_example"; // String | A cursor, as given in the [Link header](https://docs.github.com/enterprise-server@3.4/rest/overview/resources-in-the-rest-api#link-header). If specified, the query only searches for results before this cursor.
    String after = "after_example"; // String | A cursor, as given in the [Link header](https://docs.github.com/enterprise-server@3.4/rest/overview/resources-in-the-rest-api#link-header). If specified, the query only searches for results after this cursor.
    try {
      List<OrganizationSecretScanningAlert> result = apiInstance.secretScanningListAlertsForEnterprise(enterprise, state, secretType, resolution, perPage, before, after);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SecretScanningApi#secretScanningListAlertsForEnterprise");
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
| **enterprise** | **String**| The slug version of the enterprise name. You can also substitute this value with the enterprise id. | |
| **state** | **String**| Set to &#x60;open&#x60; or &#x60;resolved&#x60; to only list secret scanning alerts in a specific state. | [optional] [enum: open, resolved] |
| **secretType** | **String**| A comma-separated list of secret types to return. By default all secret types are returned. See \&quot;[Secret scanning patterns](https://docs.github.com/enterprise-server@3.4/code-security/secret-scanning/secret-scanning-patterns#supported-secrets-for-advanced-security)\&quot; for a complete list of secret types. | [optional] |
| **resolution** | **String**| A comma-separated list of resolutions. Only secret scanning alerts with one of these resolutions are listed. Valid resolutions are &#x60;false_positive&#x60;, &#x60;wont_fix&#x60;, &#x60;revoked&#x60;, &#x60;pattern_edited&#x60;, &#x60;pattern_deleted&#x60; or &#x60;used_in_tests&#x60;. | [optional] |
| **perPage** | **Integer**| The number of results per page (max 100). | [optional] [default to 30] |
| **before** | **String**| A cursor, as given in the [Link header](https://docs.github.com/enterprise-server@3.4/rest/overview/resources-in-the-rest-api#link-header). If specified, the query only searches for results before this cursor. | [optional] |
| **after** | **String**| A cursor, as given in the [Link header](https://docs.github.com/enterprise-server@3.4/rest/overview/resources-in-the-rest-api#link-header). If specified, the query only searches for results after this cursor. | [optional] |

### Return type

[**List&lt;OrganizationSecretScanningAlert&gt;**](OrganizationSecretScanningAlert.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  * Link -  <br>  |
| **404** | Resource not found |  -  |
| **503** | Service unavailable |  -  |

<a id="secretScanningListAlertsForOrg"></a>
# **secretScanningListAlertsForOrg**
> List&lt;OrganizationSecretScanningAlert&gt; secretScanningListAlertsForOrg(org, state, secretType, resolution, page, perPage)

List secret scanning alerts for an organization

Lists secret scanning alerts for eligible repositories in an organization, from newest to oldest. To use this endpoint, you must be an administrator or security manager for the organization, and you must use an access token with the &#x60;repo&#x60; scope or &#x60;security_events&#x60; scope.  GitHub Apps must have the &#x60;secret_scanning_alerts&#x60; read permission to use this endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SecretScanningApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    SecretScanningApi apiInstance = new SecretScanningApi(defaultClient);
    String org = "org_example"; // String | The organization name. The name is not case sensitive.
    String state = "open"; // String | Set to `open` or `resolved` to only list secret scanning alerts in a specific state.
    String secretType = "secretType_example"; // String | A comma-separated list of secret types to return. By default all secret types are returned. See \"[Secret scanning patterns](https://docs.github.com/enterprise-server@3.4/code-security/secret-scanning/secret-scanning-patterns#supported-secrets-for-advanced-security)\" for a complete list of secret types.
    String resolution = "resolution_example"; // String | A comma-separated list of resolutions. Only secret scanning alerts with one of these resolutions are listed. Valid resolutions are `false_positive`, `wont_fix`, `revoked`, `pattern_edited`, `pattern_deleted` or `used_in_tests`.
    Integer page = 1; // Integer | Page number of the results to fetch.
    Integer perPage = 30; // Integer | The number of results per page (max 100).
    try {
      List<OrganizationSecretScanningAlert> result = apiInstance.secretScanningListAlertsForOrg(org, state, secretType, resolution, page, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SecretScanningApi#secretScanningListAlertsForOrg");
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
| **org** | **String**| The organization name. The name is not case sensitive. | |
| **state** | **String**| Set to &#x60;open&#x60; or &#x60;resolved&#x60; to only list secret scanning alerts in a specific state. | [optional] [enum: open, resolved] |
| **secretType** | **String**| A comma-separated list of secret types to return. By default all secret types are returned. See \&quot;[Secret scanning patterns](https://docs.github.com/enterprise-server@3.4/code-security/secret-scanning/secret-scanning-patterns#supported-secrets-for-advanced-security)\&quot; for a complete list of secret types. | [optional] |
| **resolution** | **String**| A comma-separated list of resolutions. Only secret scanning alerts with one of these resolutions are listed. Valid resolutions are &#x60;false_positive&#x60;, &#x60;wont_fix&#x60;, &#x60;revoked&#x60;, &#x60;pattern_edited&#x60;, &#x60;pattern_deleted&#x60; or &#x60;used_in_tests&#x60;. | [optional] |
| **page** | **Integer**| Page number of the results to fetch. | [optional] [default to 1] |
| **perPage** | **Integer**| The number of results per page (max 100). | [optional] [default to 30] |

### Return type

[**List&lt;OrganizationSecretScanningAlert&gt;**](OrganizationSecretScanningAlert.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  * Link -  <br>  |
| **404** | Resource not found |  -  |
| **503** | Service unavailable |  -  |

<a id="secretScanningListAlertsForRepo"></a>
# **secretScanningListAlertsForRepo**
> List&lt;SecretScanningAlert&gt; secretScanningListAlertsForRepo(owner, repo, state, secretType, resolution, page, perPage)

List secret scanning alerts for a repository

Lists secret scanning alerts for a private repository, from newest to oldest. To use this endpoint, you must be an administrator for the repository or organization, and you must use an access token with the &#x60;repo&#x60; scope or &#x60;security_events&#x60; scope.  GitHub Apps must have the &#x60;secret_scanning_alerts&#x60; read permission to use this endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SecretScanningApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    SecretScanningApi apiInstance = new SecretScanningApi(defaultClient);
    String owner = "owner_example"; // String | The account owner of the repository. The name is not case sensitive.
    String repo = "repo_example"; // String | The name of the repository. The name is not case sensitive.
    String state = "open"; // String | Set to `open` or `resolved` to only list secret scanning alerts in a specific state.
    String secretType = "secretType_example"; // String | A comma-separated list of secret types to return. By default all secret types are returned. See \"[Secret scanning patterns](https://docs.github.com/enterprise-server@3.4/code-security/secret-scanning/secret-scanning-patterns#supported-secrets-for-advanced-security)\" for a complete list of secret types.
    String resolution = "resolution_example"; // String | A comma-separated list of resolutions. Only secret scanning alerts with one of these resolutions are listed. Valid resolutions are `false_positive`, `wont_fix`, `revoked`, `pattern_edited`, `pattern_deleted` or `used_in_tests`.
    Integer page = 1; // Integer | Page number of the results to fetch.
    Integer perPage = 30; // Integer | The number of results per page (max 100).
    try {
      List<SecretScanningAlert> result = apiInstance.secretScanningListAlertsForRepo(owner, repo, state, secretType, resolution, page, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SecretScanningApi#secretScanningListAlertsForRepo");
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
| **owner** | **String**| The account owner of the repository. The name is not case sensitive. | |
| **repo** | **String**| The name of the repository. The name is not case sensitive. | |
| **state** | **String**| Set to &#x60;open&#x60; or &#x60;resolved&#x60; to only list secret scanning alerts in a specific state. | [optional] [enum: open, resolved] |
| **secretType** | **String**| A comma-separated list of secret types to return. By default all secret types are returned. See \&quot;[Secret scanning patterns](https://docs.github.com/enterprise-server@3.4/code-security/secret-scanning/secret-scanning-patterns#supported-secrets-for-advanced-security)\&quot; for a complete list of secret types. | [optional] |
| **resolution** | **String**| A comma-separated list of resolutions. Only secret scanning alerts with one of these resolutions are listed. Valid resolutions are &#x60;false_positive&#x60;, &#x60;wont_fix&#x60;, &#x60;revoked&#x60;, &#x60;pattern_edited&#x60;, &#x60;pattern_deleted&#x60; or &#x60;used_in_tests&#x60;. | [optional] |
| **page** | **Integer**| Page number of the results to fetch. | [optional] [default to 1] |
| **perPage** | **Integer**| The number of results per page (max 100). | [optional] [default to 30] |

### Return type

[**List&lt;SecretScanningAlert&gt;**](SecretScanningAlert.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |
| **404** | Repository is public or secret scanning is disabled for the repository |  -  |
| **503** | Service unavailable |  -  |

<a id="secretScanningListLocationsForAlert"></a>
# **secretScanningListLocationsForAlert**
> List&lt;SecretScanningLocation&gt; secretScanningListLocationsForAlert(owner, repo, alertNumber, page, perPage)

List locations for a secret scanning alert

Lists all locations for a given secret scanning alert for a private repository. To use this endpoint, you must be an administrator for the repository or organization, and you must use an access token with the &#x60;repo&#x60; scope or &#x60;security_events&#x60; scope.  GitHub Apps must have the &#x60;secret_scanning_alerts&#x60; read permission to use this endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SecretScanningApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    SecretScanningApi apiInstance = new SecretScanningApi(defaultClient);
    String owner = "owner_example"; // String | The account owner of the repository. The name is not case sensitive.
    String repo = "repo_example"; // String | The name of the repository. The name is not case sensitive.
    Integer alertNumber = 56; // Integer | The number that identifies an alert. You can find this at the end of the URL for a code scanning alert within GitHub, and in the `number` field in the response from the `GET /repos/{owner}/{repo}/code-scanning/alerts` operation.
    Integer page = 1; // Integer | Page number of the results to fetch.
    Integer perPage = 30; // Integer | The number of results per page (max 100).
    try {
      List<SecretScanningLocation> result = apiInstance.secretScanningListLocationsForAlert(owner, repo, alertNumber, page, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SecretScanningApi#secretScanningListLocationsForAlert");
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
| **owner** | **String**| The account owner of the repository. The name is not case sensitive. | |
| **repo** | **String**| The name of the repository. The name is not case sensitive. | |
| **alertNumber** | **Integer**| The number that identifies an alert. You can find this at the end of the URL for a code scanning alert within GitHub, and in the &#x60;number&#x60; field in the response from the &#x60;GET /repos/{owner}/{repo}/code-scanning/alerts&#x60; operation. | |
| **page** | **Integer**| Page number of the results to fetch. | [optional] [default to 1] |
| **perPage** | **Integer**| The number of results per page (max 100). | [optional] [default to 30] |

### Return type

[**List&lt;SecretScanningLocation&gt;**](SecretScanningLocation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  * Link -  <br>  |
| **404** | Repository is public, or secret scanning is disabled for the repository, or the resource is not found |  -  |
| **503** | Service unavailable |  -  |

<a id="secretScanningUpdateAlert"></a>
# **secretScanningUpdateAlert**
> SecretScanningAlert secretScanningUpdateAlert(owner, repo, alertNumber, secretScanningUpdateAlertRequest)

Update a secret scanning alert

Updates the status of a secret scanning alert in a private repository. To use this endpoint, you must be an administrator for the repository or organization, and you must use an access token with the &#x60;repo&#x60; scope or &#x60;security_events&#x60; scope.  GitHub Apps must have the &#x60;secret_scanning_alerts&#x60; write permission to use this endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SecretScanningApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    SecretScanningApi apiInstance = new SecretScanningApi(defaultClient);
    String owner = "owner_example"; // String | The account owner of the repository. The name is not case sensitive.
    String repo = "repo_example"; // String | The name of the repository. The name is not case sensitive.
    Integer alertNumber = 56; // Integer | The number that identifies an alert. You can find this at the end of the URL for a code scanning alert within GitHub, and in the `number` field in the response from the `GET /repos/{owner}/{repo}/code-scanning/alerts` operation.
    SecretScanningUpdateAlertRequest secretScanningUpdateAlertRequest = new SecretScanningUpdateAlertRequest(); // SecretScanningUpdateAlertRequest | 
    try {
      SecretScanningAlert result = apiInstance.secretScanningUpdateAlert(owner, repo, alertNumber, secretScanningUpdateAlertRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SecretScanningApi#secretScanningUpdateAlert");
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
| **owner** | **String**| The account owner of the repository. The name is not case sensitive. | |
| **repo** | **String**| The name of the repository. The name is not case sensitive. | |
| **alertNumber** | **Integer**| The number that identifies an alert. You can find this at the end of the URL for a code scanning alert within GitHub, and in the &#x60;number&#x60; field in the response from the &#x60;GET /repos/{owner}/{repo}/code-scanning/alerts&#x60; operation. | |
| **secretScanningUpdateAlertRequest** | [**SecretScanningUpdateAlertRequest**](SecretScanningUpdateAlertRequest.md)|  | |

### Return type

[**SecretScanningAlert**](SecretScanningAlert.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |
| **404** | Repository is public, or secret scanning is disabled for the repository, or the resource is not found |  -  |
| **422** | State does not match the resolution |  -  |
| **503** | Service unavailable |  -  |

