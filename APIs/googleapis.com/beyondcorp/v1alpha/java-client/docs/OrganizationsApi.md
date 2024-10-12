# OrganizationsApi

All URIs are relative to *https://beyondcorp.googleapis.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**beyondcorpOrganizationsLocationsGlobalPartnerTenantsBrowserDlpRulesCreate**](OrganizationsApi.md#beyondcorpOrganizationsLocationsGlobalPartnerTenantsBrowserDlpRulesCreate) | **POST** /v1alpha/{parent}/browserDlpRules |  |
| [**beyondcorpOrganizationsLocationsGlobalPartnerTenantsBrowserDlpRulesList**](OrganizationsApi.md#beyondcorpOrganizationsLocationsGlobalPartnerTenantsBrowserDlpRulesList) | **GET** /v1alpha/{parent}/browserDlpRules |  |
| [**beyondcorpOrganizationsLocationsGlobalPartnerTenantsCreate**](OrganizationsApi.md#beyondcorpOrganizationsLocationsGlobalPartnerTenantsCreate) | **POST** /v1alpha/{parent}/partnerTenants |  |
| [**beyondcorpOrganizationsLocationsGlobalPartnerTenantsList**](OrganizationsApi.md#beyondcorpOrganizationsLocationsGlobalPartnerTenantsList) | **GET** /v1alpha/{parent}/partnerTenants |  |
| [**beyondcorpOrganizationsLocationsGlobalPartnerTenantsProxyConfigsCreate**](OrganizationsApi.md#beyondcorpOrganizationsLocationsGlobalPartnerTenantsProxyConfigsCreate) | **POST** /v1alpha/{parent}/proxyConfigs |  |
| [**beyondcorpOrganizationsLocationsGlobalPartnerTenantsProxyConfigsList**](OrganizationsApi.md#beyondcorpOrganizationsLocationsGlobalPartnerTenantsProxyConfigsList) | **GET** /v1alpha/{parent}/proxyConfigs |  |
| [**beyondcorpOrganizationsLocationsSubscriptionsCreate**](OrganizationsApi.md#beyondcorpOrganizationsLocationsSubscriptionsCreate) | **POST** /v1alpha/{parent}/subscriptions |  |
| [**beyondcorpOrganizationsLocationsSubscriptionsList**](OrganizationsApi.md#beyondcorpOrganizationsLocationsSubscriptionsList) | **GET** /v1alpha/{parent}/subscriptions |  |


<a id="beyondcorpOrganizationsLocationsGlobalPartnerTenantsBrowserDlpRulesCreate"></a>
# **beyondcorpOrganizationsLocationsGlobalPartnerTenantsBrowserDlpRulesCreate**
> GoogleLongrunningOperation beyondcorpOrganizationsLocationsGlobalPartnerTenantsBrowserDlpRulesCreate(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, requestId, googleCloudBeyondcorpPartnerservicesV1alphaBrowserDlpRule)



Creates a new BrowserDlpRule in a given organization and PartnerTenant.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganizationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://beyondcorp.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    OrganizationsApi apiInstance = new OrganizationsApi(defaultClient);
    String parent = "parent_example"; // String | Required. The resource name of the BrowserDlpRule parent using the form: `organizations/{organization_id}/locations/global/partnerTenants/{partner_tenant_id}`
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
    String requestId = "requestId_example"; // String | Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request. For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).
    GoogleCloudBeyondcorpPartnerservicesV1alphaBrowserDlpRule googleCloudBeyondcorpPartnerservicesV1alphaBrowserDlpRule = new GoogleCloudBeyondcorpPartnerservicesV1alphaBrowserDlpRule(); // GoogleCloudBeyondcorpPartnerservicesV1alphaBrowserDlpRule | 
    try {
      GoogleLongrunningOperation result = apiInstance.beyondcorpOrganizationsLocationsGlobalPartnerTenantsBrowserDlpRulesCreate(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, requestId, googleCloudBeyondcorpPartnerservicesV1alphaBrowserDlpRule);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganizationsApi#beyondcorpOrganizationsLocationsGlobalPartnerTenantsBrowserDlpRulesCreate");
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
| **parent** | **String**| Required. The resource name of the BrowserDlpRule parent using the form: &#x60;organizations/{organization_id}/locations/global/partnerTenants/{partner_tenant_id}&#x60; | |
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
| **requestId** | **String**| Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request. For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). | [optional] |
| **googleCloudBeyondcorpPartnerservicesV1alphaBrowserDlpRule** | [**GoogleCloudBeyondcorpPartnerservicesV1alphaBrowserDlpRule**](GoogleCloudBeyondcorpPartnerservicesV1alphaBrowserDlpRule.md)|  | [optional] |

### Return type

[**GoogleLongrunningOperation**](GoogleLongrunningOperation.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="beyondcorpOrganizationsLocationsGlobalPartnerTenantsBrowserDlpRulesList"></a>
# **beyondcorpOrganizationsLocationsGlobalPartnerTenantsBrowserDlpRulesList**
> GoogleCloudBeyondcorpPartnerservicesV1alphaListBrowserDlpRulesResponse beyondcorpOrganizationsLocationsGlobalPartnerTenantsBrowserDlpRulesList(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType)



Lists BrowserDlpRules for PartnerTenant in a given organization.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganizationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://beyondcorp.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    OrganizationsApi apiInstance = new OrganizationsApi(defaultClient);
    String parent = "parent_example"; // String | Required. The parent partnerTenant to which the BrowserDlpRules belong. Format: `organizations/{organization_id}/locations/global/partnerTenants/{partner_tenant_id}`
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
    try {
      GoogleCloudBeyondcorpPartnerservicesV1alphaListBrowserDlpRulesResponse result = apiInstance.beyondcorpOrganizationsLocationsGlobalPartnerTenantsBrowserDlpRulesList(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganizationsApi#beyondcorpOrganizationsLocationsGlobalPartnerTenantsBrowserDlpRulesList");
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
| **parent** | **String**| Required. The parent partnerTenant to which the BrowserDlpRules belong. Format: &#x60;organizations/{organization_id}/locations/global/partnerTenants/{partner_tenant_id}&#x60; | |
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

### Return type

[**GoogleCloudBeyondcorpPartnerservicesV1alphaListBrowserDlpRulesResponse**](GoogleCloudBeyondcorpPartnerservicesV1alphaListBrowserDlpRulesResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="beyondcorpOrganizationsLocationsGlobalPartnerTenantsCreate"></a>
# **beyondcorpOrganizationsLocationsGlobalPartnerTenantsCreate**
> GoogleLongrunningOperation beyondcorpOrganizationsLocationsGlobalPartnerTenantsCreate(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, requestId, googleCloudBeyondcorpPartnerservicesV1alphaPartnerTenant)



Creates a new BeyondCorp Enterprise partnerTenant in a given organization and can only be called by onboarded BeyondCorp Enterprise partner.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganizationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://beyondcorp.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    OrganizationsApi apiInstance = new OrganizationsApi(defaultClient);
    String parent = "parent_example"; // String | Required. The resource name of the parent organization using the form: `organizations/{organization_id}/locations/global`
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
    String requestId = "requestId_example"; // String | Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request. For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).
    GoogleCloudBeyondcorpPartnerservicesV1alphaPartnerTenant googleCloudBeyondcorpPartnerservicesV1alphaPartnerTenant = new GoogleCloudBeyondcorpPartnerservicesV1alphaPartnerTenant(); // GoogleCloudBeyondcorpPartnerservicesV1alphaPartnerTenant | 
    try {
      GoogleLongrunningOperation result = apiInstance.beyondcorpOrganizationsLocationsGlobalPartnerTenantsCreate(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, requestId, googleCloudBeyondcorpPartnerservicesV1alphaPartnerTenant);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganizationsApi#beyondcorpOrganizationsLocationsGlobalPartnerTenantsCreate");
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
| **parent** | **String**| Required. The resource name of the parent organization using the form: &#x60;organizations/{organization_id}/locations/global&#x60; | |
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
| **requestId** | **String**| Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request. For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). | [optional] |
| **googleCloudBeyondcorpPartnerservicesV1alphaPartnerTenant** | [**GoogleCloudBeyondcorpPartnerservicesV1alphaPartnerTenant**](GoogleCloudBeyondcorpPartnerservicesV1alphaPartnerTenant.md)|  | [optional] |

### Return type

[**GoogleLongrunningOperation**](GoogleLongrunningOperation.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="beyondcorpOrganizationsLocationsGlobalPartnerTenantsList"></a>
# **beyondcorpOrganizationsLocationsGlobalPartnerTenantsList**
> GoogleCloudBeyondcorpPartnerservicesV1alphaListPartnerTenantsResponse beyondcorpOrganizationsLocationsGlobalPartnerTenantsList(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, filter, orderBy, pageSize, pageToken)



Lists PartnerTenants in a given organization.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganizationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://beyondcorp.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    OrganizationsApi apiInstance = new OrganizationsApi(defaultClient);
    String parent = "parent_example"; // String | Required. The parent organization to which the PartnerTenants belong. Format: `organizations/{organization_id}/locations/global`
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
    String filter = "filter_example"; // String | Optional. A filter specifying constraints of a list operation. All fields in the PartnerTenant message are supported. For example, the following query will return the PartnerTenants with displayName \"test-tenant\" organizations/${ORG_ID}/locations/${LOCATION}/partnerTenants?filter=displayName=\"test-tenant\" Nested fields are also supported. The follow query will return PartnerTenants with internal_tenant_id \"1234\" organizations/${ORG_ID}/locations/${LOCATION}/partnerTenants?filter=partnerMetadata.internalTenantId=\"1234\" For more information, please refer to https://google.aip.dev/160.
    String orderBy = "orderBy_example"; // String | Optional. Specifies the ordering of results. See [Sorting order](https://cloud.google.com/apis/design/design_patterns#sorting_order) for more information.
    Integer pageSize = 56; // Integer | Optional. The maximum number of items to return. If not specified, a default value of 50 will be used by the service. Regardless of the page_size value, the response may include a partial list and a caller should only rely on response's next_page_token to determine if there are more instances left to be queried.
    String pageToken = "pageToken_example"; // String | Optional. The next_page_token value returned from a previous ListPartnerTenantsResponse, if any.
    try {
      GoogleCloudBeyondcorpPartnerservicesV1alphaListPartnerTenantsResponse result = apiInstance.beyondcorpOrganizationsLocationsGlobalPartnerTenantsList(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, filter, orderBy, pageSize, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganizationsApi#beyondcorpOrganizationsLocationsGlobalPartnerTenantsList");
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
| **parent** | **String**| Required. The parent organization to which the PartnerTenants belong. Format: &#x60;organizations/{organization_id}/locations/global&#x60; | |
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
| **filter** | **String**| Optional. A filter specifying constraints of a list operation. All fields in the PartnerTenant message are supported. For example, the following query will return the PartnerTenants with displayName \&quot;test-tenant\&quot; organizations/${ORG_ID}/locations/${LOCATION}/partnerTenants?filter&#x3D;displayName&#x3D;\&quot;test-tenant\&quot; Nested fields are also supported. The follow query will return PartnerTenants with internal_tenant_id \&quot;1234\&quot; organizations/${ORG_ID}/locations/${LOCATION}/partnerTenants?filter&#x3D;partnerMetadata.internalTenantId&#x3D;\&quot;1234\&quot; For more information, please refer to https://google.aip.dev/160. | [optional] |
| **orderBy** | **String**| Optional. Specifies the ordering of results. See [Sorting order](https://cloud.google.com/apis/design/design_patterns#sorting_order) for more information. | [optional] |
| **pageSize** | **Integer**| Optional. The maximum number of items to return. If not specified, a default value of 50 will be used by the service. Regardless of the page_size value, the response may include a partial list and a caller should only rely on response&#39;s next_page_token to determine if there are more instances left to be queried. | [optional] |
| **pageToken** | **String**| Optional. The next_page_token value returned from a previous ListPartnerTenantsResponse, if any. | [optional] |

### Return type

[**GoogleCloudBeyondcorpPartnerservicesV1alphaListPartnerTenantsResponse**](GoogleCloudBeyondcorpPartnerservicesV1alphaListPartnerTenantsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="beyondcorpOrganizationsLocationsGlobalPartnerTenantsProxyConfigsCreate"></a>
# **beyondcorpOrganizationsLocationsGlobalPartnerTenantsProxyConfigsCreate**
> GoogleLongrunningOperation beyondcorpOrganizationsLocationsGlobalPartnerTenantsProxyConfigsCreate(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, requestId, googleCloudBeyondcorpPartnerservicesV1alphaProxyConfig)



Creates a new BeyondCorp Enterprise ProxyConfig in a given organization and PartnerTenant. Can only be called by on onboarded Beyondcorp Enterprise partner.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganizationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://beyondcorp.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    OrganizationsApi apiInstance = new OrganizationsApi(defaultClient);
    String parent = "parent_example"; // String | Required. The resource name of the parent PartnerTenant using the form: `organizations/{organization_id}/locations/global/partnerTenants/{partner_tenant_id}`
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
    String requestId = "requestId_example"; // String | Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request. For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).
    GoogleCloudBeyondcorpPartnerservicesV1alphaProxyConfig googleCloudBeyondcorpPartnerservicesV1alphaProxyConfig = new GoogleCloudBeyondcorpPartnerservicesV1alphaProxyConfig(); // GoogleCloudBeyondcorpPartnerservicesV1alphaProxyConfig | 
    try {
      GoogleLongrunningOperation result = apiInstance.beyondcorpOrganizationsLocationsGlobalPartnerTenantsProxyConfigsCreate(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, requestId, googleCloudBeyondcorpPartnerservicesV1alphaProxyConfig);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganizationsApi#beyondcorpOrganizationsLocationsGlobalPartnerTenantsProxyConfigsCreate");
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
| **parent** | **String**| Required. The resource name of the parent PartnerTenant using the form: &#x60;organizations/{organization_id}/locations/global/partnerTenants/{partner_tenant_id}&#x60; | |
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
| **requestId** | **String**| Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request. For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). | [optional] |
| **googleCloudBeyondcorpPartnerservicesV1alphaProxyConfig** | [**GoogleCloudBeyondcorpPartnerservicesV1alphaProxyConfig**](GoogleCloudBeyondcorpPartnerservicesV1alphaProxyConfig.md)|  | [optional] |

### Return type

[**GoogleLongrunningOperation**](GoogleLongrunningOperation.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="beyondcorpOrganizationsLocationsGlobalPartnerTenantsProxyConfigsList"></a>
# **beyondcorpOrganizationsLocationsGlobalPartnerTenantsProxyConfigsList**
> GoogleCloudBeyondcorpPartnerservicesV1alphaListProxyConfigsResponse beyondcorpOrganizationsLocationsGlobalPartnerTenantsProxyConfigsList(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, filter, orderBy, pageSize, pageToken)



Lists ProxyConfigs for PartnerTenant in a given organization.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganizationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://beyondcorp.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    OrganizationsApi apiInstance = new OrganizationsApi(defaultClient);
    String parent = "parent_example"; // String | Required. The parent organization to which the ProxyConfigs belong. Format: `organizations/{organization_id}/locations/global/partnerTenants/{partner_tenant_id}`
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
    String filter = "filter_example"; // String | Optional. A filter specifying constraints of a list operation. All fields in the ProxyConfig message are supported. For example, the following query will return the ProxyConfigs with displayName \"test-config\" organizations/${ORG_ID}/locations/global/partnerTenants/${PARTNER_TENANT_ID}/proxyConfigs?filter=displayName=\"test-config\" Nested fields are also supported. The follow query will return ProxyConfigs with pacUri \"example.com/pac.pac\" organizations/${ORG_ID}/locations/global/partnerTenants/${PARTNER_TENANT_ID}/proxyConfigs?filter=routingInfo.pacUri=\"example.com/pac.pac\" For more information, please refer to https://google.aip.dev/160.
    String orderBy = "orderBy_example"; // String | Optional. Specifies the ordering of results. See [Sorting order](https://cloud.google.com/apis/design/design_patterns#sorting_order) for more information.
    Integer pageSize = 56; // Integer | Optional. The maximum number of items to return. If not specified, a default value of 50 will be used by the service. Regardless of the page_size value, the response may include a partial list and a caller should only rely on response's next_page_token to determine if there are more instances left to be queried.
    String pageToken = "pageToken_example"; // String | Optional. The next_page_token value returned from a previous ListProxyConfigsRequest, if any.
    try {
      GoogleCloudBeyondcorpPartnerservicesV1alphaListProxyConfigsResponse result = apiInstance.beyondcorpOrganizationsLocationsGlobalPartnerTenantsProxyConfigsList(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, filter, orderBy, pageSize, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganizationsApi#beyondcorpOrganizationsLocationsGlobalPartnerTenantsProxyConfigsList");
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
| **parent** | **String**| Required. The parent organization to which the ProxyConfigs belong. Format: &#x60;organizations/{organization_id}/locations/global/partnerTenants/{partner_tenant_id}&#x60; | |
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
| **filter** | **String**| Optional. A filter specifying constraints of a list operation. All fields in the ProxyConfig message are supported. For example, the following query will return the ProxyConfigs with displayName \&quot;test-config\&quot; organizations/${ORG_ID}/locations/global/partnerTenants/${PARTNER_TENANT_ID}/proxyConfigs?filter&#x3D;displayName&#x3D;\&quot;test-config\&quot; Nested fields are also supported. The follow query will return ProxyConfigs with pacUri \&quot;example.com/pac.pac\&quot; organizations/${ORG_ID}/locations/global/partnerTenants/${PARTNER_TENANT_ID}/proxyConfigs?filter&#x3D;routingInfo.pacUri&#x3D;\&quot;example.com/pac.pac\&quot; For more information, please refer to https://google.aip.dev/160. | [optional] |
| **orderBy** | **String**| Optional. Specifies the ordering of results. See [Sorting order](https://cloud.google.com/apis/design/design_patterns#sorting_order) for more information. | [optional] |
| **pageSize** | **Integer**| Optional. The maximum number of items to return. If not specified, a default value of 50 will be used by the service. Regardless of the page_size value, the response may include a partial list and a caller should only rely on response&#39;s next_page_token to determine if there are more instances left to be queried. | [optional] |
| **pageToken** | **String**| Optional. The next_page_token value returned from a previous ListProxyConfigsRequest, if any. | [optional] |

### Return type

[**GoogleCloudBeyondcorpPartnerservicesV1alphaListProxyConfigsResponse**](GoogleCloudBeyondcorpPartnerservicesV1alphaListProxyConfigsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="beyondcorpOrganizationsLocationsSubscriptionsCreate"></a>
# **beyondcorpOrganizationsLocationsSubscriptionsCreate**
> GoogleCloudBeyondcorpSaasplatformSubscriptionsV1alphaSubscription beyondcorpOrganizationsLocationsSubscriptionsCreate(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, googleCloudBeyondcorpSaasplatformSubscriptionsV1alphaSubscription)



Creates a new BeyondCorp Enterprise Subscription in a given organization. Location will always be global as BeyondCorp subscriptions are per organization.

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
    defaultClient.setBasePath("https://beyondcorp.googleapis.com");

    OrganizationsApi apiInstance = new OrganizationsApi(defaultClient);
    String parent = "parent_example"; // String | Required. The resource name of the subscription location using the form: `organizations/{organization_id}/locations/{location}`
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
    GoogleCloudBeyondcorpSaasplatformSubscriptionsV1alphaSubscription googleCloudBeyondcorpSaasplatformSubscriptionsV1alphaSubscription = new GoogleCloudBeyondcorpSaasplatformSubscriptionsV1alphaSubscription(); // GoogleCloudBeyondcorpSaasplatformSubscriptionsV1alphaSubscription | 
    try {
      GoogleCloudBeyondcorpSaasplatformSubscriptionsV1alphaSubscription result = apiInstance.beyondcorpOrganizationsLocationsSubscriptionsCreate(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, googleCloudBeyondcorpSaasplatformSubscriptionsV1alphaSubscription);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganizationsApi#beyondcorpOrganizationsLocationsSubscriptionsCreate");
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
| **parent** | **String**| Required. The resource name of the subscription location using the form: &#x60;organizations/{organization_id}/locations/{location}&#x60; | |
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
| **googleCloudBeyondcorpSaasplatformSubscriptionsV1alphaSubscription** | [**GoogleCloudBeyondcorpSaasplatformSubscriptionsV1alphaSubscription**](GoogleCloudBeyondcorpSaasplatformSubscriptionsV1alphaSubscription.md)|  | [optional] |

### Return type

[**GoogleCloudBeyondcorpSaasplatformSubscriptionsV1alphaSubscription**](GoogleCloudBeyondcorpSaasplatformSubscriptionsV1alphaSubscription.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="beyondcorpOrganizationsLocationsSubscriptionsList"></a>
# **beyondcorpOrganizationsLocationsSubscriptionsList**
> GoogleCloudBeyondcorpSaasplatformSubscriptionsV1alphaListSubscriptionsResponse beyondcorpOrganizationsLocationsSubscriptionsList(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, pageSize, pageToken)



Lists Subscriptions in a given organization and location.

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
    defaultClient.setBasePath("https://beyondcorp.googleapis.com");

    OrganizationsApi apiInstance = new OrganizationsApi(defaultClient);
    String parent = "parent_example"; // String | Required. The resource name of Subscription using the form: `organizations/{organization_id}/locations/{location}`
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
    Integer pageSize = 56; // Integer | Optional. The maximum number of items to return. If not specified, a default value of 50 will be used by the service. Regardless of the page_size value, the response may include a partial list and a caller should only rely on response's next_page_token to determine if there are more instances left to be queried.
    String pageToken = "pageToken_example"; // String | Optional. The next_page_token value returned from a previous ListSubscriptionsRequest, if any.
    try {
      GoogleCloudBeyondcorpSaasplatformSubscriptionsV1alphaListSubscriptionsResponse result = apiInstance.beyondcorpOrganizationsLocationsSubscriptionsList(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, pageSize, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganizationsApi#beyondcorpOrganizationsLocationsSubscriptionsList");
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
| **parent** | **String**| Required. The resource name of Subscription using the form: &#x60;organizations/{organization_id}/locations/{location}&#x60; | |
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
| **pageSize** | **Integer**| Optional. The maximum number of items to return. If not specified, a default value of 50 will be used by the service. Regardless of the page_size value, the response may include a partial list and a caller should only rely on response&#39;s next_page_token to determine if there are more instances left to be queried. | [optional] |
| **pageToken** | **String**| Optional. The next_page_token value returned from a previous ListSubscriptionsRequest, if any. | [optional] |

### Return type

[**GoogleCloudBeyondcorpSaasplatformSubscriptionsV1alphaListSubscriptionsResponse**](GoogleCloudBeyondcorpSaasplatformSubscriptionsV1alphaListSubscriptionsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

