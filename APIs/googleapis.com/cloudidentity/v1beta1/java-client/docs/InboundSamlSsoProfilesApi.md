# InboundSamlSsoProfilesApi

All URIs are relative to *https://cloudidentity.googleapis.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**cloudidentityInboundSamlSsoProfilesCreate**](InboundSamlSsoProfilesApi.md#cloudidentityInboundSamlSsoProfilesCreate) | **POST** /v1beta1/inboundSamlSsoProfiles |  |
| [**cloudidentityInboundSamlSsoProfilesIdpCredentialsAdd**](InboundSamlSsoProfilesApi.md#cloudidentityInboundSamlSsoProfilesIdpCredentialsAdd) | **POST** /v1beta1/{parent}/idpCredentials:add |  |
| [**cloudidentityInboundSamlSsoProfilesIdpCredentialsList**](InboundSamlSsoProfilesApi.md#cloudidentityInboundSamlSsoProfilesIdpCredentialsList) | **GET** /v1beta1/{parent}/idpCredentials |  |
| [**cloudidentityInboundSamlSsoProfilesList**](InboundSamlSsoProfilesApi.md#cloudidentityInboundSamlSsoProfilesList) | **GET** /v1beta1/inboundSamlSsoProfiles |  |


<a id="cloudidentityInboundSamlSsoProfilesCreate"></a>
# **cloudidentityInboundSamlSsoProfilesCreate**
> Operation cloudidentityInboundSamlSsoProfilesCreate($xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, inboundSamlSsoProfile)



Creates an InboundSamlSsoProfile for a customer.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InboundSamlSsoProfilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cloudidentity.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    InboundSamlSsoProfilesApi apiInstance = new InboundSamlSsoProfilesApi(defaultClient);
    String $xgafv = "1"; // String | V1 error format.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String alt = "json"; // String | Data format for response.
    String paramCallback = "paramCallback_example"; // String | JSONP
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    InboundSamlSsoProfile inboundSamlSsoProfile = new InboundSamlSsoProfile(); // InboundSamlSsoProfile | 
    try {
      Operation result = apiInstance.cloudidentityInboundSamlSsoProfilesCreate($xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, inboundSamlSsoProfile);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InboundSamlSsoProfilesApi#cloudidentityInboundSamlSsoProfilesCreate");
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
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **alt** | **String**| Data format for response. | [optional] [enum: json, media, proto] |
| **paramCallback** | **String**| JSONP | [optional] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |
| **inboundSamlSsoProfile** | [**InboundSamlSsoProfile**](InboundSamlSsoProfile.md)|  | [optional] |

### Return type

[**Operation**](Operation.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="cloudidentityInboundSamlSsoProfilesIdpCredentialsAdd"></a>
# **cloudidentityInboundSamlSsoProfilesIdpCredentialsAdd**
> Operation cloudidentityInboundSamlSsoProfilesIdpCredentialsAdd(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, addIdpCredentialRequest)



Adds an IdpCredential. Up to 2 credentials are allowed.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InboundSamlSsoProfilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cloudidentity.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    InboundSamlSsoProfilesApi apiInstance = new InboundSamlSsoProfilesApi(defaultClient);
    String parent = "parent_example"; // String | Required. The InboundSamlSsoProfile that owns the IdpCredential. Format: `inboundSamlSsoProfiles/{sso_profile_id}`
    String $xgafv = "1"; // String | V1 error format.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String alt = "json"; // String | Data format for response.
    String paramCallback = "paramCallback_example"; // String | JSONP
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    AddIdpCredentialRequest addIdpCredentialRequest = new AddIdpCredentialRequest(); // AddIdpCredentialRequest | 
    try {
      Operation result = apiInstance.cloudidentityInboundSamlSsoProfilesIdpCredentialsAdd(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, addIdpCredentialRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InboundSamlSsoProfilesApi#cloudidentityInboundSamlSsoProfilesIdpCredentialsAdd");
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
| **parent** | **String**| Required. The InboundSamlSsoProfile that owns the IdpCredential. Format: &#x60;inboundSamlSsoProfiles/{sso_profile_id}&#x60; | |
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **alt** | **String**| Data format for response. | [optional] [enum: json, media, proto] |
| **paramCallback** | **String**| JSONP | [optional] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |
| **addIdpCredentialRequest** | [**AddIdpCredentialRequest**](AddIdpCredentialRequest.md)|  | [optional] |

### Return type

[**Operation**](Operation.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="cloudidentityInboundSamlSsoProfilesIdpCredentialsList"></a>
# **cloudidentityInboundSamlSsoProfilesIdpCredentialsList**
> ListIdpCredentialsResponse cloudidentityInboundSamlSsoProfilesIdpCredentialsList(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, pageSize, pageToken)



Returns a list of IdpCredentials in an InboundSamlSsoProfile.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InboundSamlSsoProfilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cloudidentity.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    InboundSamlSsoProfilesApi apiInstance = new InboundSamlSsoProfilesApi(defaultClient);
    String parent = "parent_example"; // String | Required. The parent, which owns this collection of `IdpCredential`s. Format: `inboundSamlSsoProfiles/{sso_profile_id}`
    String $xgafv = "1"; // String | V1 error format.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String alt = "json"; // String | Data format for response.
    String paramCallback = "paramCallback_example"; // String | JSONP
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    Integer pageSize = 56; // Integer | The maximum number of `IdpCredential`s to return. The service may return fewer than this value.
    String pageToken = "pageToken_example"; // String | A page token, received from a previous `ListIdpCredentials` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListIdpCredentials` must match the call that provided the page token.
    try {
      ListIdpCredentialsResponse result = apiInstance.cloudidentityInboundSamlSsoProfilesIdpCredentialsList(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, pageSize, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InboundSamlSsoProfilesApi#cloudidentityInboundSamlSsoProfilesIdpCredentialsList");
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
| **parent** | **String**| Required. The parent, which owns this collection of &#x60;IdpCredential&#x60;s. Format: &#x60;inboundSamlSsoProfiles/{sso_profile_id}&#x60; | |
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **alt** | **String**| Data format for response. | [optional] [enum: json, media, proto] |
| **paramCallback** | **String**| JSONP | [optional] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |
| **pageSize** | **Integer**| The maximum number of &#x60;IdpCredential&#x60;s to return. The service may return fewer than this value. | [optional] |
| **pageToken** | **String**| A page token, received from a previous &#x60;ListIdpCredentials&#x60; call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to &#x60;ListIdpCredentials&#x60; must match the call that provided the page token. | [optional] |

### Return type

[**ListIdpCredentialsResponse**](ListIdpCredentialsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="cloudidentityInboundSamlSsoProfilesList"></a>
# **cloudidentityInboundSamlSsoProfilesList**
> ListInboundSamlSsoProfilesResponse cloudidentityInboundSamlSsoProfilesList($xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, filter, pageSize, pageToken)



Lists InboundSamlSsoProfiles for a customer.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InboundSamlSsoProfilesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cloudidentity.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    InboundSamlSsoProfilesApi apiInstance = new InboundSamlSsoProfilesApi(defaultClient);
    String $xgafv = "1"; // String | V1 error format.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String alt = "json"; // String | Data format for response.
    String paramCallback = "paramCallback_example"; // String | JSONP
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    String filter = "filter_example"; // String | A [Common Expression Language](https://github.com/google/cel-spec) expression to filter the results. The only supported filter is filtering by customer. For example: `customer==\"customers/C0123abc\"`. Omitting the filter or specifying a filter of `customer==\"customers/my_customer\"` will return the profiles for the customer that the caller (authenticated user) belongs to.
    Integer pageSize = 56; // Integer | The maximum number of InboundSamlSsoProfiles to return. The service may return fewer than this value. If omitted (or defaulted to zero) the server will use a sensible default. This default may change over time. The maximum allowed value is 100. Requests with page_size greater than that will be silently interpreted as having this maximum value.
    String pageToken = "pageToken_example"; // String | A page token, received from a previous `ListInboundSamlSsoProfiles` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListInboundSamlSsoProfiles` must match the call that provided the page token.
    try {
      ListInboundSamlSsoProfilesResponse result = apiInstance.cloudidentityInboundSamlSsoProfilesList($xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, filter, pageSize, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InboundSamlSsoProfilesApi#cloudidentityInboundSamlSsoProfilesList");
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
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **alt** | **String**| Data format for response. | [optional] [enum: json, media, proto] |
| **paramCallback** | **String**| JSONP | [optional] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |
| **filter** | **String**| A [Common Expression Language](https://github.com/google/cel-spec) expression to filter the results. The only supported filter is filtering by customer. For example: &#x60;customer&#x3D;&#x3D;\&quot;customers/C0123abc\&quot;&#x60;. Omitting the filter or specifying a filter of &#x60;customer&#x3D;&#x3D;\&quot;customers/my_customer\&quot;&#x60; will return the profiles for the customer that the caller (authenticated user) belongs to. | [optional] |
| **pageSize** | **Integer**| The maximum number of InboundSamlSsoProfiles to return. The service may return fewer than this value. If omitted (or defaulted to zero) the server will use a sensible default. This default may change over time. The maximum allowed value is 100. Requests with page_size greater than that will be silently interpreted as having this maximum value. | [optional] |
| **pageToken** | **String**| A page token, received from a previous &#x60;ListInboundSamlSsoProfiles&#x60; call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to &#x60;ListInboundSamlSsoProfiles&#x60; must match the call that provided the page token. | [optional] |

### Return type

[**ListInboundSamlSsoProfilesResponse**](ListInboundSamlSsoProfilesResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

