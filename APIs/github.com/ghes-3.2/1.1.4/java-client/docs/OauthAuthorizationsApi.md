# OauthAuthorizationsApi

All URIs are relative to *https://github.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**oauthAuthorizationsCreateAuthorization**](OauthAuthorizationsApi.md#oauthAuthorizationsCreateAuthorization) | **POST** /authorizations | Create a new authorization |
| [**oauthAuthorizationsDeleteAuthorization**](OauthAuthorizationsApi.md#oauthAuthorizationsDeleteAuthorization) | **DELETE** /authorizations/{authorization_id} | Delete an authorization |
| [**oauthAuthorizationsDeleteGrant**](OauthAuthorizationsApi.md#oauthAuthorizationsDeleteGrant) | **DELETE** /applications/grants/{grant_id} | Delete a grant |
| [**oauthAuthorizationsGetAuthorization**](OauthAuthorizationsApi.md#oauthAuthorizationsGetAuthorization) | **GET** /authorizations/{authorization_id} | Get a single authorization |
| [**oauthAuthorizationsGetGrant**](OauthAuthorizationsApi.md#oauthAuthorizationsGetGrant) | **GET** /applications/grants/{grant_id} | Get a single grant |
| [**oauthAuthorizationsGetOrCreateAuthorizationForApp**](OauthAuthorizationsApi.md#oauthAuthorizationsGetOrCreateAuthorizationForApp) | **PUT** /authorizations/clients/{client_id} | Get-or-create an authorization for a specific app |
| [**oauthAuthorizationsGetOrCreateAuthorizationForAppAndFingerprint**](OauthAuthorizationsApi.md#oauthAuthorizationsGetOrCreateAuthorizationForAppAndFingerprint) | **PUT** /authorizations/clients/{client_id}/{fingerprint} | Get-or-create an authorization for a specific app and fingerprint |
| [**oauthAuthorizationsListAuthorizations**](OauthAuthorizationsApi.md#oauthAuthorizationsListAuthorizations) | **GET** /authorizations | List your authorizations |
| [**oauthAuthorizationsListGrants**](OauthAuthorizationsApi.md#oauthAuthorizationsListGrants) | **GET** /applications/grants | List your grants |
| [**oauthAuthorizationsUpdateAuthorization**](OauthAuthorizationsApi.md#oauthAuthorizationsUpdateAuthorization) | **PATCH** /authorizations/{authorization_id} | Update an existing authorization |


<a id="oauthAuthorizationsCreateAuthorization"></a>
# **oauthAuthorizationsCreateAuthorization**
> Authorization oauthAuthorizationsCreateAuthorization(oauthAuthorizationsCreateAuthorizationRequest)

Create a new authorization

**Deprecation Notice:** GitHub Enterprise Server will discontinue the [OAuth Authorizations API](https://docs.github.com/enterprise-server@3.2/rest/reference/oauth-authorizations), which is used by integrations to create personal access tokens and OAuth tokens, and you must now create these tokens using our [web application flow](https://docs.github.com/enterprise-server@3.2/developers/apps/authorizing-oauth-apps#web-application-flow). The [OAuth Authorizations API](https://docs.github.com/enterprise-server@3.2/rest/reference/oauth-authorizations) will be removed on November, 13, 2020. For more information, including scheduled brownouts, see the [blog post](https://developer.github.com/changes/2020-02-14-deprecating-oauth-auth-endpoint/).  **Warning:** Apps must use the [web application flow](https://docs.github.com/enterprise-server@3.2/apps/building-oauth-apps/authorizing-oauth-apps/#web-application-flow) to obtain OAuth tokens that work with GitHub Enterprise Server SAML organizations. OAuth tokens created using the Authorizations API will be unable to access GitHub Enterprise Server SAML organizations. For more information, see the [blog post](https://developer.github.com/changes/2019-11-05-deprecated-passwords-and-authorizations-api).  Creates OAuth tokens using [Basic Authentication](https://docs.github.com/enterprise-server@3.2/rest/overview/other-authentication-methods#basic-authentication). If you have two-factor authentication setup, Basic Authentication for this endpoint requires that you use a one-time password (OTP) and your username and password instead of tokens. For more information, see \&quot;[Working with two-factor authentication](https://docs.github.com/enterprise-server@3.2/rest/overview/other-authentication-methods#working-with-two-factor-authentication).\&quot;  To create tokens for a particular OAuth application using this endpoint, you must authenticate as the user you want to create an authorization for and provide the app&#39;s client ID and secret, found on your OAuth application&#39;s settings page. If your OAuth application intends to create multiple tokens for one user, use &#x60;fingerprint&#x60; to differentiate between them.  You can also create tokens on GitHub Enterprise Server from the [personal access tokens settings](https://github.com/settings/tokens) page. Read more about these tokens in [the GitHub Help documentation](https://docs.github.com/articles/creating-an-access-token-for-command-line-use).  Organizations that enforce SAML SSO require personal access tokens to be allowed. Read more about allowing tokens in [the GitHub Help documentation](https://docs.github.com/articles/about-identity-and-access-management-with-saml-single-sign-on).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OauthAuthorizationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    OauthAuthorizationsApi apiInstance = new OauthAuthorizationsApi(defaultClient);
    OauthAuthorizationsCreateAuthorizationRequest oauthAuthorizationsCreateAuthorizationRequest = new OauthAuthorizationsCreateAuthorizationRequest(); // OauthAuthorizationsCreateAuthorizationRequest | 
    try {
      Authorization result = apiInstance.oauthAuthorizationsCreateAuthorization(oauthAuthorizationsCreateAuthorizationRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OauthAuthorizationsApi#oauthAuthorizationsCreateAuthorization");
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
| **oauthAuthorizationsCreateAuthorizationRequest** | [**OauthAuthorizationsCreateAuthorizationRequest**](OauthAuthorizationsCreateAuthorizationRequest.md)|  | [optional] |

### Return type

[**Authorization**](Authorization.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Response |  * Location -  <br>  |
| **304** | Not modified |  -  |
| **401** | Requires authentication |  -  |
| **403** | Forbidden |  -  |
| **410** | Gone |  -  |
| **422** | Validation failed, or the endpoint has been spammed. |  -  |

<a id="oauthAuthorizationsDeleteAuthorization"></a>
# **oauthAuthorizationsDeleteAuthorization**
> oauthAuthorizationsDeleteAuthorization(authorizationId)

Delete an authorization

**Deprecation Notice:** GitHub Enterprise Server will discontinue the [OAuth Authorizations API](https://docs.github.com/enterprise-server@3.2/rest/reference/oauth-authorizations), which is used by integrations to create personal access tokens and OAuth tokens, and you must now create these tokens using our [web application flow](https://docs.github.com/enterprise-server@3.2/apps/building-oauth-apps/authorizing-oauth-apps/#web-application-flow). The [OAuth Authorizations API](https://docs.github.com/enterprise-server@3.2/rest/reference/oauth-authorizations) will be removed on November, 13, 2020. For more information, including scheduled brownouts, see the [blog post](https://developer.github.com/changes/2020-02-14-deprecating-oauth-auth-endpoint/).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OauthAuthorizationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    OauthAuthorizationsApi apiInstance = new OauthAuthorizationsApi(defaultClient);
    Integer authorizationId = 56; // Integer | The unique identifier of the authorization.
    try {
      apiInstance.oauthAuthorizationsDeleteAuthorization(authorizationId);
    } catch (ApiException e) {
      System.err.println("Exception when calling OauthAuthorizationsApi#oauthAuthorizationsDeleteAuthorization");
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
| **authorizationId** | **Integer**| The unique identifier of the authorization. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Response |  -  |
| **304** | Not modified |  -  |
| **401** | Requires authentication |  -  |
| **403** | Forbidden |  -  |

<a id="oauthAuthorizationsDeleteGrant"></a>
# **oauthAuthorizationsDeleteGrant**
> oauthAuthorizationsDeleteGrant(grantId)

Delete a grant

**Deprecation Notice:** GitHub Enterprise Server will discontinue the [OAuth Authorizations API](https://docs.github.com/enterprise-server@3.2/rest/reference/oauth-authorizations/), which is used by integrations to create personal access tokens and OAuth tokens, and you must now create these tokens using our [web application flow](https://docs.github.com/enterprise-server@3.2/developers/apps/authorizing-oauth-apps#web-application-flow). The [OAuth Authorizations API](https://docs.github.com/enterprise-server@3.2/rest/reference/oauth-authorizations/) will be removed on November, 13, 2020. For more information, including scheduled brownouts, see the [blog post](https://developer.github.com/changes/2020-02-14-deprecating-oauth-auth-endpoint/).  Deleting an OAuth application&#39;s grant will also delete all OAuth tokens associated with the application for your user. Once deleted, the application has no access to your account and is no longer listed on [the application authorizations settings screen within GitHub](https://github.com/settings/applications#authorized).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OauthAuthorizationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    OauthAuthorizationsApi apiInstance = new OauthAuthorizationsApi(defaultClient);
    Integer grantId = 56; // Integer | The unique identifier of the grant.
    try {
      apiInstance.oauthAuthorizationsDeleteGrant(grantId);
    } catch (ApiException e) {
      System.err.println("Exception when calling OauthAuthorizationsApi#oauthAuthorizationsDeleteGrant");
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
| **grantId** | **Integer**| The unique identifier of the grant. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Response |  -  |
| **304** | Not modified |  -  |
| **401** | Requires authentication |  -  |
| **403** | Forbidden |  -  |

<a id="oauthAuthorizationsGetAuthorization"></a>
# **oauthAuthorizationsGetAuthorization**
> Authorization oauthAuthorizationsGetAuthorization(authorizationId)

Get a single authorization

**Deprecation Notice:** GitHub Enterprise Server will discontinue the [OAuth Authorizations API](https://docs.github.com/enterprise-server@3.2/rest/reference/oauth-authorizations), which is used by integrations to create personal access tokens and OAuth tokens, and you must now create these tokens using our [web application flow](https://docs.github.com/enterprise-server@3.2/apps/building-oauth-apps/authorizing-oauth-apps/#web-application-flow). The [OAuth Authorizations API](https://docs.github.com/enterprise-server@3.2/rest/reference/oauth-authorizations) will be removed on November, 13, 2020. For more information, including scheduled brownouts, see the [blog post](https://developer.github.com/changes/2020-02-14-deprecating-oauth-auth-endpoint/).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OauthAuthorizationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    OauthAuthorizationsApi apiInstance = new OauthAuthorizationsApi(defaultClient);
    Integer authorizationId = 56; // Integer | The unique identifier of the authorization.
    try {
      Authorization result = apiInstance.oauthAuthorizationsGetAuthorization(authorizationId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OauthAuthorizationsApi#oauthAuthorizationsGetAuthorization");
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
| **authorizationId** | **Integer**| The unique identifier of the authorization. | |

### Return type

[**Authorization**](Authorization.md)

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
| **401** | Requires authentication |  -  |
| **403** | Forbidden |  -  |

<a id="oauthAuthorizationsGetGrant"></a>
# **oauthAuthorizationsGetGrant**
> ApplicationGrant oauthAuthorizationsGetGrant(grantId)

Get a single grant

**Deprecation Notice:** GitHub Enterprise Server will discontinue the [OAuth Authorizations API](https://docs.github.com/enterprise-server@3.2/rest/reference/oauth-authorizations), which is used by integrations to create personal access tokens and OAuth tokens, and you must now create these tokens using our [web application flow](https://docs.github.com/enterprise-server@3.2/apps/building-oauth-apps/authorizing-oauth-apps/#web-application-flow). The [OAuth Authorizations API](https://docs.github.com/enterprise-server@3.2/rest/reference/oauth-authorizations) will be removed on November, 13, 2020. For more information, including scheduled brownouts, see the [blog post](https://developer.github.com/changes/2020-02-14-deprecating-oauth-auth-endpoint/).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OauthAuthorizationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    OauthAuthorizationsApi apiInstance = new OauthAuthorizationsApi(defaultClient);
    Integer grantId = 56; // Integer | The unique identifier of the grant.
    try {
      ApplicationGrant result = apiInstance.oauthAuthorizationsGetGrant(grantId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OauthAuthorizationsApi#oauthAuthorizationsGetGrant");
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
| **grantId** | **Integer**| The unique identifier of the grant. | |

### Return type

[**ApplicationGrant**](ApplicationGrant.md)

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
| **401** | Requires authentication |  -  |
| **403** | Forbidden |  -  |

<a id="oauthAuthorizationsGetOrCreateAuthorizationForApp"></a>
# **oauthAuthorizationsGetOrCreateAuthorizationForApp**
> Authorization oauthAuthorizationsGetOrCreateAuthorizationForApp(clientId, oauthAuthorizationsGetOrCreateAuthorizationForAppRequest)

Get-or-create an authorization for a specific app

**Deprecation Notice:** GitHub Enterprise Server will discontinue the [OAuth Authorizations API](https://docs.github.com/enterprise-server@3.2/rest/reference/oauth-authorizations/), which is used by integrations to create personal access tokens and OAuth tokens, and you must now create these tokens using our [web application flow](https://docs.github.com/enterprise-server@3.2/developers/apps/authorizing-oauth-apps#web-application-flow). The [OAuth Authorizations API](https://docs.github.com/enterprise-server@3.2/rest/reference/oauth-authorizations) will be removed on November, 13, 2020. For more information, including scheduled brownouts, see the [blog post](https://developer.github.com/changes/2020-02-14-deprecating-oauth-auth-endpoint/).  **Warning:** Apps must use the [web application flow](https://docs.github.com/enterprise-server@3.2/apps/building-oauth-apps/authorizing-oauth-apps/#web-application-flow) to obtain OAuth tokens that work with GitHub Enterprise Server SAML organizations. OAuth tokens created using the Authorizations API will be unable to access GitHub Enterprise Server SAML organizations. For more information, see the [blog post](https://developer.github.com/changes/2019-11-05-deprecated-passwords-and-authorizations-api).  Creates a new authorization for the specified OAuth application, only if an authorization for that application doesn&#39;t already exist for the user. The URL includes the 20 character client ID for the OAuth app that is requesting the token. It returns the user&#39;s existing authorization for the application if one is present. Otherwise, it creates and returns a new one.  If you have two-factor authentication setup, Basic Authentication for this endpoint requires that you use a one-time password (OTP) and your username and password instead of tokens. For more information, see \&quot;[Working with two-factor authentication](https://docs.github.com/enterprise-server@3.2/rest/overview/other-authentication-methods#working-with-two-factor-authentication).\&quot;  **Deprecation Notice:** GitHub Enterprise Server will discontinue the [OAuth Authorizations API](https://docs.github.com/enterprise-server@3.2/rest/reference/oauth-authorizations/), which is used by integrations to create personal access tokens and OAuth tokens, and you must now create these tokens using our [web application flow](https://docs.github.com/enterprise-server@3.2/developers/apps/authorizing-oauth-apps#web-application-flow). The [OAuth Authorizations API](https://docs.github.com/enterprise-server@3.2/rest/reference/oauth-authorizations) will be removed on November, 13, 2020. For more information, including scheduled brownouts, see the [blog post](https://developer.github.com/changes/2020-02-14-deprecating-oauth-auth-endpoint/).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OauthAuthorizationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    OauthAuthorizationsApi apiInstance = new OauthAuthorizationsApi(defaultClient);
    String clientId = "abcde12345fghij67890"; // String | The client ID of the OAuth app.
    OauthAuthorizationsGetOrCreateAuthorizationForAppRequest oauthAuthorizationsGetOrCreateAuthorizationForAppRequest = new OauthAuthorizationsGetOrCreateAuthorizationForAppRequest(); // OauthAuthorizationsGetOrCreateAuthorizationForAppRequest | 
    try {
      Authorization result = apiInstance.oauthAuthorizationsGetOrCreateAuthorizationForApp(clientId, oauthAuthorizationsGetOrCreateAuthorizationForAppRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OauthAuthorizationsApi#oauthAuthorizationsGetOrCreateAuthorizationForApp");
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
| **clientId** | **String**| The client ID of the OAuth app. | |
| **oauthAuthorizationsGetOrCreateAuthorizationForAppRequest** | [**OauthAuthorizationsGetOrCreateAuthorizationForAppRequest**](OauthAuthorizationsGetOrCreateAuthorizationForAppRequest.md)|  | |

### Return type

[**Authorization**](Authorization.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | if returning an existing token |  * Location -  <br>  |
| **201** | **Deprecation Notice:** GitHub will discontinue the [OAuth Authorizations API](https://docs.github.com/enterprise-server@3.2/rest/reference/oauth-authorizations), which is used by integrations to create personal access tokens and OAuth tokens, and you must now create these tokens using our [web application flow](https://docs.github.com/enterprise-server@3.2/apps/building-oauth-apps/authorizing-oauth-apps/#web-application-flow). The [OAuth Authorizations API](https://docs.github.com/enterprise-server@3.2/rest/reference/oauth-authorizations) will be removed on November, 13, 2020. For more information, including scheduled brownouts, see the [blog post](https://developer.github.com/changes/2020-02-14-deprecating-oauth-auth-endpoint/). |  * Location -  <br>  |
| **304** | Not modified |  -  |
| **401** | Requires authentication |  -  |
| **403** | Forbidden |  -  |
| **422** | Validation failed, or the endpoint has been spammed. |  -  |

<a id="oauthAuthorizationsGetOrCreateAuthorizationForAppAndFingerprint"></a>
# **oauthAuthorizationsGetOrCreateAuthorizationForAppAndFingerprint**
> Authorization oauthAuthorizationsGetOrCreateAuthorizationForAppAndFingerprint(clientId, fingerprint, oauthAuthorizationsGetOrCreateAuthorizationForAppAndFingerprintRequest)

Get-or-create an authorization for a specific app and fingerprint

**Deprecation Notice:** GitHub Enterprise Server will discontinue the [OAuth Authorizations API](https://docs.github.com/enterprise-server@3.2/rest/reference/oauth-authorizations/), which is used by integrations to create personal access tokens and OAuth tokens, and you must now create these tokens using our [web application flow](https://docs.github.com/enterprise-server@3.2/developers/apps/authorizing-oauth-apps#web-application-flow). The [OAuth Authorizations API](https://docs.github.com/enterprise-server@3.2/rest/reference/oauth-authorizations) will be removed on November, 13, 2020. For more information, including scheduled brownouts, see the [blog post](https://developer.github.com/changes/2020-02-14-deprecating-oauth-auth-endpoint/).  **Warning:** Apps must use the [web application flow](https://docs.github.com/enterprise-server@3.2/apps/building-oauth-apps/authorizing-oauth-apps/#web-application-flow) to obtain OAuth tokens that work with GitHub Enterprise Server SAML organizations. OAuth tokens created using the Authorizations API will be unable to access GitHub Enterprise Server SAML organizations. For more information, see the [blog post](https://developer.github.com/changes/2019-11-05-deprecated-passwords-and-authorizations-api).  This method will create a new authorization for the specified OAuth application, only if an authorization for that application and fingerprint do not already exist for the user. The URL includes the 20 character client ID for the OAuth app that is requesting the token. &#x60;fingerprint&#x60; is a unique string to distinguish an authorization from others created for the same client ID and user. It returns the user&#39;s existing authorization for the application if one is present. Otherwise, it creates and returns a new one.  If you have two-factor authentication setup, Basic Authentication for this endpoint requires that you use a one-time password (OTP) and your username and password instead of tokens. For more information, see \&quot;[Working with two-factor authentication](https://docs.github.com/enterprise-server@3.2/rest/overview/other-authentication-methods#working-with-two-factor-authentication).\&quot;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OauthAuthorizationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    OauthAuthorizationsApi apiInstance = new OauthAuthorizationsApi(defaultClient);
    String clientId = "abcde12345fghij67890"; // String | The client ID of the OAuth app.
    String fingerprint = "fingerprint_example"; // String | 
    OauthAuthorizationsGetOrCreateAuthorizationForAppAndFingerprintRequest oauthAuthorizationsGetOrCreateAuthorizationForAppAndFingerprintRequest = new OauthAuthorizationsGetOrCreateAuthorizationForAppAndFingerprintRequest(); // OauthAuthorizationsGetOrCreateAuthorizationForAppAndFingerprintRequest | 
    try {
      Authorization result = apiInstance.oauthAuthorizationsGetOrCreateAuthorizationForAppAndFingerprint(clientId, fingerprint, oauthAuthorizationsGetOrCreateAuthorizationForAppAndFingerprintRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OauthAuthorizationsApi#oauthAuthorizationsGetOrCreateAuthorizationForAppAndFingerprint");
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
| **clientId** | **String**| The client ID of the OAuth app. | |
| **fingerprint** | **String**|  | |
| **oauthAuthorizationsGetOrCreateAuthorizationForAppAndFingerprintRequest** | [**OauthAuthorizationsGetOrCreateAuthorizationForAppAndFingerprintRequest**](OauthAuthorizationsGetOrCreateAuthorizationForAppAndFingerprintRequest.md)|  | |

### Return type

[**Authorization**](Authorization.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | if returning an existing token |  * Location -  <br>  |
| **201** | Response if returning a new token |  * Location -  <br>  |
| **422** | Validation failed, or the endpoint has been spammed. |  -  |

<a id="oauthAuthorizationsListAuthorizations"></a>
# **oauthAuthorizationsListAuthorizations**
> List&lt;Authorization&gt; oauthAuthorizationsListAuthorizations(perPage, page, clientId)

List your authorizations

**Deprecation Notice:** GitHub Enterprise Server will discontinue the [OAuth Authorizations API](https://docs.github.com/enterprise-server@3.2/rest/reference/oauth-authorizations), which is used by integrations to create personal access tokens and OAuth tokens, and you must now create these tokens using our [web application flow](https://docs.github.com/enterprise-server@3.2/apps/building-oauth-apps/authorizing-oauth-apps/#web-application-flow). The [OAuth Authorizations API](https://docs.github.com/enterprise-server@3.2/rest/reference/oauth-authorizations) will be removed on November, 13, 2020. For more information, including scheduled brownouts, see the [blog post](https://developer.github.com/changes/2020-02-14-deprecating-oauth-auth-endpoint/).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OauthAuthorizationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    OauthAuthorizationsApi apiInstance = new OauthAuthorizationsApi(defaultClient);
    Integer perPage = 30; // Integer | The number of results per page (max 100).
    Integer page = 1; // Integer | Page number of the results to fetch.
    String clientId = "clientId_example"; // String | The client ID of your GitHub app.
    try {
      List<Authorization> result = apiInstance.oauthAuthorizationsListAuthorizations(perPage, page, clientId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OauthAuthorizationsApi#oauthAuthorizationsListAuthorizations");
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
| **perPage** | **Integer**| The number of results per page (max 100). | [optional] [default to 30] |
| **page** | **Integer**| Page number of the results to fetch. | [optional] [default to 1] |
| **clientId** | **String**| The client ID of your GitHub app. | [optional] |

### Return type

[**List&lt;Authorization&gt;**](Authorization.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  * Link -  <br>  |
| **304** | Not modified |  -  |
| **401** | Requires authentication |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |

<a id="oauthAuthorizationsListGrants"></a>
# **oauthAuthorizationsListGrants**
> List&lt;ApplicationGrant&gt; oauthAuthorizationsListGrants(perPage, page, clientId)

List your grants

**Deprecation Notice:** GitHub Enterprise Server will discontinue the [OAuth Authorizations API](https://docs.github.com/enterprise-server@3.2/rest/reference/oauth-authorizations/), which is used by integrations to create personal access tokens and OAuth tokens, and you must now create these tokens using our [web application flow](https://docs.github.com/enterprise-server@3.2/developers/apps/authorizing-oauth-apps#web-application-flow). The [OAuth Authorizations API](https://docs.github.com/enterprise-server@3.2/rest/reference/oauth-authorizations) will be removed on November, 13, 2020. For more information, including scheduled brownouts, see the [blog post](https://developer.github.com/changes/2020-02-14-deprecating-oauth-auth-endpoint/).  You can use this API to list the set of OAuth applications that have been granted access to your account. Unlike the [list your authorizations](https://docs.github.com/enterprise-server@3.2/rest/reference/oauth-authorizations#list-your-authorizations) API, this API does not manage individual tokens. This API will return one entry for each OAuth application that has been granted access to your account, regardless of the number of tokens an application has generated for your user. The list of OAuth applications returned matches what is shown on [the application authorizations settings screen within GitHub](https://github.com/settings/applications#authorized). The &#x60;scopes&#x60; returned are the union of scopes authorized for the application. For example, if an application has one token with &#x60;repo&#x60; scope and another token with &#x60;user&#x60; scope, the grant will return &#x60;[\&quot;repo\&quot;, \&quot;user\&quot;]&#x60;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OauthAuthorizationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    OauthAuthorizationsApi apiInstance = new OauthAuthorizationsApi(defaultClient);
    Integer perPage = 30; // Integer | The number of results per page (max 100).
    Integer page = 1; // Integer | Page number of the results to fetch.
    String clientId = "clientId_example"; // String | The client ID of your GitHub app.
    try {
      List<ApplicationGrant> result = apiInstance.oauthAuthorizationsListGrants(perPage, page, clientId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OauthAuthorizationsApi#oauthAuthorizationsListGrants");
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
| **perPage** | **Integer**| The number of results per page (max 100). | [optional] [default to 30] |
| **page** | **Integer**| Page number of the results to fetch. | [optional] [default to 1] |
| **clientId** | **String**| The client ID of your GitHub app. | [optional] |

### Return type

[**List&lt;ApplicationGrant&gt;**](ApplicationGrant.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  * Link -  <br>  |
| **304** | Not modified |  -  |
| **401** | Requires authentication |  -  |
| **403** | Forbidden |  -  |
| **404** | Resource not found |  -  |

<a id="oauthAuthorizationsUpdateAuthorization"></a>
# **oauthAuthorizationsUpdateAuthorization**
> Authorization oauthAuthorizationsUpdateAuthorization(authorizationId, oauthAuthorizationsUpdateAuthorizationRequest)

Update an existing authorization

**Deprecation Notice:** GitHub Enterprise Server will discontinue the [OAuth Authorizations API](https://docs.github.com/enterprise-server@3.2/rest/reference/oauth-authorizations/), which is used by integrations to create personal access tokens and OAuth tokens, and you must now create these tokens using our [web application flow](https://docs.github.com/enterprise-server@3.2/developers/apps/authorizing-oauth-apps#web-application-flow). The [OAuth Authorizations API](https://docs.github.com/enterprise-server@3.2/rest/reference/oauth-authorizations) will be removed on November, 13, 2020. For more information, including scheduled brownouts, see the [blog post](https://developer.github.com/changes/2020-02-14-deprecating-oauth-auth-endpoint/).  If you have two-factor authentication setup, Basic Authentication for this endpoint requires that you use a one-time password (OTP) and your username and password instead of tokens. For more information, see \&quot;[Working with two-factor authentication](https://docs.github.com/enterprise-server@3.2/rest/overview/other-authentication-methods#working-with-two-factor-authentication).\&quot;  You can only send one of these scope keys at a time.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OauthAuthorizationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://github.com");

    OauthAuthorizationsApi apiInstance = new OauthAuthorizationsApi(defaultClient);
    Integer authorizationId = 56; // Integer | The unique identifier of the authorization.
    OauthAuthorizationsUpdateAuthorizationRequest oauthAuthorizationsUpdateAuthorizationRequest = new OauthAuthorizationsUpdateAuthorizationRequest(); // OauthAuthorizationsUpdateAuthorizationRequest | 
    try {
      Authorization result = apiInstance.oauthAuthorizationsUpdateAuthorization(authorizationId, oauthAuthorizationsUpdateAuthorizationRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OauthAuthorizationsApi#oauthAuthorizationsUpdateAuthorization");
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
| **authorizationId** | **Integer**| The unique identifier of the authorization. | |
| **oauthAuthorizationsUpdateAuthorizationRequest** | [**OauthAuthorizationsUpdateAuthorizationRequest**](OauthAuthorizationsUpdateAuthorizationRequest.md)|  | [optional] |

### Return type

[**Authorization**](Authorization.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response |  -  |
| **422** | Validation failed, or the endpoint has been spammed. |  -  |

