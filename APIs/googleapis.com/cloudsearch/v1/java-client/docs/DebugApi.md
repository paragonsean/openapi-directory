# DebugApi

All URIs are relative to *https://cloudsearch.googleapis.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**cloudsearchDebugDatasourcesItemsCheckAccess**](DebugApi.md#cloudsearchDebugDatasourcesItemsCheckAccess) | **POST** /v1/debug/{name}:checkAccess |  |
| [**cloudsearchDebugDatasourcesItemsSearchByViewUrl**](DebugApi.md#cloudsearchDebugDatasourcesItemsSearchByViewUrl) | **POST** /v1/debug/{name}/items:searchByViewUrl |  |
| [**cloudsearchDebugIdentitysourcesItemsListForunmappedidentity**](DebugApi.md#cloudsearchDebugIdentitysourcesItemsListForunmappedidentity) | **GET** /v1/debug/{parent}/items:forunmappedidentity |  |
| [**cloudsearchDebugIdentitysourcesUnmappedidsList**](DebugApi.md#cloudsearchDebugIdentitysourcesUnmappedidsList) | **GET** /v1/debug/{parent}/unmappedids |  |


<a id="cloudsearchDebugDatasourcesItemsCheckAccess"></a>
# **cloudsearchDebugDatasourcesItemsCheckAccess**
> CheckAccessResponse cloudsearchDebugDatasourcesItemsCheckAccess(name, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, debugOptionsEnableDebugging, principal)



Checks whether an item is accessible by specified principal. Principal must be a user; groups and domain values aren&#39;t supported. **Note:** This API requires an admin account to execute.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DebugApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cloudsearch.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    DebugApi apiInstance = new DebugApi(defaultClient);
    String name = "name_example"; // String | Item name, format: datasources/{source_id}/items/{item_id}
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
    Boolean debugOptionsEnableDebugging = true; // Boolean | If you are asked by Google to help with debugging, set this field. Otherwise, ignore this field.
    Principal principal = new Principal(); // Principal | 
    try {
      CheckAccessResponse result = apiInstance.cloudsearchDebugDatasourcesItemsCheckAccess(name, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, debugOptionsEnableDebugging, principal);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DebugApi#cloudsearchDebugDatasourcesItemsCheckAccess");
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
| **name** | **String**| Item name, format: datasources/{source_id}/items/{item_id} | |
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
| **debugOptionsEnableDebugging** | **Boolean**| If you are asked by Google to help with debugging, set this field. Otherwise, ignore this field. | [optional] |
| **principal** | [**Principal**](Principal.md)|  | [optional] |

### Return type

[**CheckAccessResponse**](CheckAccessResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="cloudsearchDebugDatasourcesItemsSearchByViewUrl"></a>
# **cloudsearchDebugDatasourcesItemsSearchByViewUrl**
> SearchItemsByViewUrlResponse cloudsearchDebugDatasourcesItemsSearchByViewUrl(name, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, searchItemsByViewUrlRequest)



Fetches the item whose viewUrl exactly matches that of the URL provided in the request. **Note:** This API requires an admin account to execute.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DebugApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cloudsearch.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    DebugApi apiInstance = new DebugApi(defaultClient);
    String name = "name_example"; // String | Source name, format: datasources/{source_id}
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
    SearchItemsByViewUrlRequest searchItemsByViewUrlRequest = new SearchItemsByViewUrlRequest(); // SearchItemsByViewUrlRequest | 
    try {
      SearchItemsByViewUrlResponse result = apiInstance.cloudsearchDebugDatasourcesItemsSearchByViewUrl(name, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, searchItemsByViewUrlRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DebugApi#cloudsearchDebugDatasourcesItemsSearchByViewUrl");
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
| **name** | **String**| Source name, format: datasources/{source_id} | |
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
| **searchItemsByViewUrlRequest** | [**SearchItemsByViewUrlRequest**](SearchItemsByViewUrlRequest.md)|  | [optional] |

### Return type

[**SearchItemsByViewUrlResponse**](SearchItemsByViewUrlResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="cloudsearchDebugIdentitysourcesItemsListForunmappedidentity"></a>
# **cloudsearchDebugIdentitysourcesItemsListForunmappedidentity**
> ListItemNamesForUnmappedIdentityResponse cloudsearchDebugIdentitysourcesItemsListForunmappedidentity(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, debugOptionsEnableDebugging, groupResourceName, pageSize, pageToken, userResourceName)



Lists names of items associated with an unmapped identity. **Note:** This API requires an admin account to execute.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DebugApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cloudsearch.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    DebugApi apiInstance = new DebugApi(defaultClient);
    String parent = "parent_example"; // String | The name of the identity source, in the following format: identitysources/{source_id}}
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
    Boolean debugOptionsEnableDebugging = true; // Boolean | If you are asked by Google to help with debugging, set this field. Otherwise, ignore this field.
    String groupResourceName = "groupResourceName_example"; // String | 
    Integer pageSize = 56; // Integer | Maximum number of items to fetch in a request. Defaults to 100.
    String pageToken = "pageToken_example"; // String | The next_page_token value returned from a previous List request, if any.
    String userResourceName = "userResourceName_example"; // String | 
    try {
      ListItemNamesForUnmappedIdentityResponse result = apiInstance.cloudsearchDebugIdentitysourcesItemsListForunmappedidentity(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, debugOptionsEnableDebugging, groupResourceName, pageSize, pageToken, userResourceName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DebugApi#cloudsearchDebugIdentitysourcesItemsListForunmappedidentity");
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
| **parent** | **String**| The name of the identity source, in the following format: identitysources/{source_id}} | |
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
| **debugOptionsEnableDebugging** | **Boolean**| If you are asked by Google to help with debugging, set this field. Otherwise, ignore this field. | [optional] |
| **groupResourceName** | **String**|  | [optional] |
| **pageSize** | **Integer**| Maximum number of items to fetch in a request. Defaults to 100. | [optional] |
| **pageToken** | **String**| The next_page_token value returned from a previous List request, if any. | [optional] |
| **userResourceName** | **String**|  | [optional] |

### Return type

[**ListItemNamesForUnmappedIdentityResponse**](ListItemNamesForUnmappedIdentityResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="cloudsearchDebugIdentitysourcesUnmappedidsList"></a>
# **cloudsearchDebugIdentitysourcesUnmappedidsList**
> ListUnmappedIdentitiesResponse cloudsearchDebugIdentitysourcesUnmappedidsList(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, debugOptionsEnableDebugging, pageSize, pageToken, resolutionStatusCode)



Lists unmapped user identities for an identity source. **Note:** This API requires an admin account to execute.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DebugApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cloudsearch.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    DebugApi apiInstance = new DebugApi(defaultClient);
    String parent = "parent_example"; // String | The name of the identity source, in the following format: identitysources/{source_id}
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
    Boolean debugOptionsEnableDebugging = true; // Boolean | If you are asked by Google to help with debugging, set this field. Otherwise, ignore this field.
    Integer pageSize = 56; // Integer | Maximum number of items to fetch in a request. Defaults to 100.
    String pageToken = "pageToken_example"; // String | The next_page_token value returned from a previous List request, if any.
    String resolutionStatusCode = "CODE_UNSPECIFIED"; // String | Limit users selection to this status.
    try {
      ListUnmappedIdentitiesResponse result = apiInstance.cloudsearchDebugIdentitysourcesUnmappedidsList(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, debugOptionsEnableDebugging, pageSize, pageToken, resolutionStatusCode);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DebugApi#cloudsearchDebugIdentitysourcesUnmappedidsList");
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
| **parent** | **String**| The name of the identity source, in the following format: identitysources/{source_id} | |
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
| **debugOptionsEnableDebugging** | **Boolean**| If you are asked by Google to help with debugging, set this field. Otherwise, ignore this field. | [optional] |
| **pageSize** | **Integer**| Maximum number of items to fetch in a request. Defaults to 100. | [optional] |
| **pageToken** | **String**| The next_page_token value returned from a previous List request, if any. | [optional] |
| **resolutionStatusCode** | **String**| Limit users selection to this status. | [optional] [enum: CODE_UNSPECIFIED, NOT_FOUND, IDENTITY_SOURCE_NOT_FOUND, IDENTITY_SOURCE_MISCONFIGURED, TOO_MANY_MAPPINGS_FOUND, INTERNAL_ERROR] |

### Return type

[**ListUnmappedIdentitiesResponse**](ListUnmappedIdentitiesResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

