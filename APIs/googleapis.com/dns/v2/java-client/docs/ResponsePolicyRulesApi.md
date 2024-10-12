# ResponsePolicyRulesApi

All URIs are relative to *https://dns.googleapis.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**dnsResponsePolicyRulesCreate**](ResponsePolicyRulesApi.md#dnsResponsePolicyRulesCreate) | **POST** /dns/v2/projects/{project}/locations/{location}/responsePolicies/{responsePolicy}/rules |  |
| [**dnsResponsePolicyRulesDelete**](ResponsePolicyRulesApi.md#dnsResponsePolicyRulesDelete) | **DELETE** /dns/v2/projects/{project}/locations/{location}/responsePolicies/{responsePolicy}/rules/{responsePolicyRule} |  |
| [**dnsResponsePolicyRulesGet**](ResponsePolicyRulesApi.md#dnsResponsePolicyRulesGet) | **GET** /dns/v2/projects/{project}/locations/{location}/responsePolicies/{responsePolicy}/rules/{responsePolicyRule} |  |
| [**dnsResponsePolicyRulesList**](ResponsePolicyRulesApi.md#dnsResponsePolicyRulesList) | **GET** /dns/v2/projects/{project}/locations/{location}/responsePolicies/{responsePolicy}/rules |  |
| [**dnsResponsePolicyRulesPatch**](ResponsePolicyRulesApi.md#dnsResponsePolicyRulesPatch) | **PATCH** /dns/v2/projects/{project}/locations/{location}/responsePolicies/{responsePolicy}/rules/{responsePolicyRule} |  |
| [**dnsResponsePolicyRulesUpdate**](ResponsePolicyRulesApi.md#dnsResponsePolicyRulesUpdate) | **PUT** /dns/v2/projects/{project}/locations/{location}/responsePolicies/{responsePolicy}/rules/{responsePolicyRule} |  |


<a id="dnsResponsePolicyRulesCreate"></a>
# **dnsResponsePolicyRulesCreate**
> ResponsePolicyRule dnsResponsePolicyRulesCreate(project, location, responsePolicy, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, clientOperationId, responsePolicyRule)



Creates a new Response Policy Rule.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ResponsePolicyRulesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dns.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ResponsePolicyRulesApi apiInstance = new ResponsePolicyRulesApi(defaultClient);
    String project = "project_example"; // String | Identifies the project addressed by this request.
    String location = "location_example"; // String | Specifies the location of the resource. This information will be used for routing and will be part of the resource name.
    String responsePolicy = "responsePolicy_example"; // String | User assigned name of the Response Policy containing the Response Policy Rule.
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
    String clientOperationId = "clientOperationId_example"; // String | For mutating operation requests only. An optional identifier specified by the client. Must be unique for operation resources in the Operations collection.
    ResponsePolicyRule responsePolicyRule = new ResponsePolicyRule(); // ResponsePolicyRule | 
    try {
      ResponsePolicyRule result = apiInstance.dnsResponsePolicyRulesCreate(project, location, responsePolicy, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, clientOperationId, responsePolicyRule);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ResponsePolicyRulesApi#dnsResponsePolicyRulesCreate");
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
| **project** | **String**| Identifies the project addressed by this request. | |
| **location** | **String**| Specifies the location of the resource. This information will be used for routing and will be part of the resource name. | |
| **responsePolicy** | **String**| User assigned name of the Response Policy containing the Response Policy Rule. | |
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
| **clientOperationId** | **String**| For mutating operation requests only. An optional identifier specified by the client. Must be unique for operation resources in the Operations collection. | [optional] |
| **responsePolicyRule** | [**ResponsePolicyRule**](ResponsePolicyRule.md)|  | [optional] |

### Return type

[**ResponsePolicyRule**](ResponsePolicyRule.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="dnsResponsePolicyRulesDelete"></a>
# **dnsResponsePolicyRulesDelete**
> dnsResponsePolicyRulesDelete(project, location, responsePolicy, responsePolicyRule, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, clientOperationId)



Deletes a previously created Response Policy Rule.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ResponsePolicyRulesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dns.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ResponsePolicyRulesApi apiInstance = new ResponsePolicyRulesApi(defaultClient);
    String project = "project_example"; // String | Identifies the project addressed by this request.
    String location = "location_example"; // String | Specifies the location of the resource. This information will be used for routing and will be part of the resource name.
    String responsePolicy = "responsePolicy_example"; // String | User assigned name of the Response Policy containing the Response Policy Rule.
    String responsePolicyRule = "responsePolicyRule_example"; // String | User assigned name of the Response Policy Rule addressed by this request.
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
    String clientOperationId = "clientOperationId_example"; // String | For mutating operation requests only. An optional identifier specified by the client. Must be unique for operation resources in the Operations collection.
    try {
      apiInstance.dnsResponsePolicyRulesDelete(project, location, responsePolicy, responsePolicyRule, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, clientOperationId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ResponsePolicyRulesApi#dnsResponsePolicyRulesDelete");
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
| **project** | **String**| Identifies the project addressed by this request. | |
| **location** | **String**| Specifies the location of the resource. This information will be used for routing and will be part of the resource name. | |
| **responsePolicy** | **String**| User assigned name of the Response Policy containing the Response Policy Rule. | |
| **responsePolicyRule** | **String**| User assigned name of the Response Policy Rule addressed by this request. | |
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
| **clientOperationId** | **String**| For mutating operation requests only. An optional identifier specified by the client. Must be unique for operation resources in the Operations collection. | [optional] |

### Return type

null (empty response body)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="dnsResponsePolicyRulesGet"></a>
# **dnsResponsePolicyRulesGet**
> ResponsePolicyRule dnsResponsePolicyRulesGet(project, location, responsePolicy, responsePolicyRule, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, clientOperationId)



Fetches the representation of an existing Response Policy Rule.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ResponsePolicyRulesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dns.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ResponsePolicyRulesApi apiInstance = new ResponsePolicyRulesApi(defaultClient);
    String project = "project_example"; // String | Identifies the project addressed by this request.
    String location = "location_example"; // String | Specifies the location of the resource. This information will be used for routing and will be part of the resource name.
    String responsePolicy = "responsePolicy_example"; // String | User assigned name of the Response Policy containing the Response Policy Rule.
    String responsePolicyRule = "responsePolicyRule_example"; // String | User assigned name of the Response Policy Rule addressed by this request.
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
    String clientOperationId = "clientOperationId_example"; // String | For mutating operation requests only. An optional identifier specified by the client. Must be unique for operation resources in the Operations collection.
    try {
      ResponsePolicyRule result = apiInstance.dnsResponsePolicyRulesGet(project, location, responsePolicy, responsePolicyRule, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, clientOperationId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ResponsePolicyRulesApi#dnsResponsePolicyRulesGet");
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
| **project** | **String**| Identifies the project addressed by this request. | |
| **location** | **String**| Specifies the location of the resource. This information will be used for routing and will be part of the resource name. | |
| **responsePolicy** | **String**| User assigned name of the Response Policy containing the Response Policy Rule. | |
| **responsePolicyRule** | **String**| User assigned name of the Response Policy Rule addressed by this request. | |
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
| **clientOperationId** | **String**| For mutating operation requests only. An optional identifier specified by the client. Must be unique for operation resources in the Operations collection. | [optional] |

### Return type

[**ResponsePolicyRule**](ResponsePolicyRule.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="dnsResponsePolicyRulesList"></a>
# **dnsResponsePolicyRulesList**
> ResponsePolicyRulesListResponse dnsResponsePolicyRulesList(project, location, responsePolicy, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, maxResults, pageToken)



Enumerates all Response Policy Rules associated with a project.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ResponsePolicyRulesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dns.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ResponsePolicyRulesApi apiInstance = new ResponsePolicyRulesApi(defaultClient);
    String project = "project_example"; // String | Identifies the project addressed by this request.
    String location = "location_example"; // String | Specifies the location of the resource. This information will be used for routing and will be part of the resource name.
    String responsePolicy = "responsePolicy_example"; // String | User assigned name of the Response Policy to list.
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
    Integer maxResults = 56; // Integer | Optional. Maximum number of results to be returned. If unspecified, the server decides how many results to return.
    String pageToken = "pageToken_example"; // String | Optional. A tag returned by a previous list request that was truncated. Use this parameter to continue a previous list request.
    try {
      ResponsePolicyRulesListResponse result = apiInstance.dnsResponsePolicyRulesList(project, location, responsePolicy, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, maxResults, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ResponsePolicyRulesApi#dnsResponsePolicyRulesList");
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
| **project** | **String**| Identifies the project addressed by this request. | |
| **location** | **String**| Specifies the location of the resource. This information will be used for routing and will be part of the resource name. | |
| **responsePolicy** | **String**| User assigned name of the Response Policy to list. | |
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
| **maxResults** | **Integer**| Optional. Maximum number of results to be returned. If unspecified, the server decides how many results to return. | [optional] |
| **pageToken** | **String**| Optional. A tag returned by a previous list request that was truncated. Use this parameter to continue a previous list request. | [optional] |

### Return type

[**ResponsePolicyRulesListResponse**](ResponsePolicyRulesListResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="dnsResponsePolicyRulesPatch"></a>
# **dnsResponsePolicyRulesPatch**
> ResponsePolicyRulesPatchResponse dnsResponsePolicyRulesPatch(project, location, responsePolicy, responsePolicyRule, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, clientOperationId, responsePolicyRule2)



Applies a partial update to an existing Response Policy Rule.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ResponsePolicyRulesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dns.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ResponsePolicyRulesApi apiInstance = new ResponsePolicyRulesApi(defaultClient);
    String project = "project_example"; // String | Identifies the project addressed by this request.
    String location = "location_example"; // String | Specifies the location of the resource. This information will be used for routing and will be part of the resource name.
    String responsePolicy = "responsePolicy_example"; // String | User assigned name of the Response Policy containing the Response Policy Rule.
    String responsePolicyRule = "responsePolicyRule_example"; // String | User assigned name of the Response Policy Rule addressed by this request.
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
    String clientOperationId = "clientOperationId_example"; // String | For mutating operation requests only. An optional identifier specified by the client. Must be unique for operation resources in the Operations collection.
    ResponsePolicyRule responsePolicyRule2 = new ResponsePolicyRule(); // ResponsePolicyRule | 
    try {
      ResponsePolicyRulesPatchResponse result = apiInstance.dnsResponsePolicyRulesPatch(project, location, responsePolicy, responsePolicyRule, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, clientOperationId, responsePolicyRule2);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ResponsePolicyRulesApi#dnsResponsePolicyRulesPatch");
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
| **project** | **String**| Identifies the project addressed by this request. | |
| **location** | **String**| Specifies the location of the resource. This information will be used for routing and will be part of the resource name. | |
| **responsePolicy** | **String**| User assigned name of the Response Policy containing the Response Policy Rule. | |
| **responsePolicyRule** | **String**| User assigned name of the Response Policy Rule addressed by this request. | |
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
| **clientOperationId** | **String**| For mutating operation requests only. An optional identifier specified by the client. Must be unique for operation resources in the Operations collection. | [optional] |
| **responsePolicyRule2** | [**ResponsePolicyRule**](ResponsePolicyRule.md)|  | [optional] |

### Return type

[**ResponsePolicyRulesPatchResponse**](ResponsePolicyRulesPatchResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="dnsResponsePolicyRulesUpdate"></a>
# **dnsResponsePolicyRulesUpdate**
> ResponsePolicyRulesUpdateResponse dnsResponsePolicyRulesUpdate(project, location, responsePolicy, responsePolicyRule, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, clientOperationId, responsePolicyRule2)



Updates an existing Response Policy Rule.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ResponsePolicyRulesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dns.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ResponsePolicyRulesApi apiInstance = new ResponsePolicyRulesApi(defaultClient);
    String project = "project_example"; // String | Identifies the project addressed by this request.
    String location = "location_example"; // String | Specifies the location of the resource. This information will be used for routing and will be part of the resource name.
    String responsePolicy = "responsePolicy_example"; // String | User assigned name of the Response Policy containing the Response Policy Rule.
    String responsePolicyRule = "responsePolicyRule_example"; // String | User assigned name of the Response Policy Rule addressed by this request.
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
    String clientOperationId = "clientOperationId_example"; // String | For mutating operation requests only. An optional identifier specified by the client. Must be unique for operation resources in the Operations collection.
    ResponsePolicyRule responsePolicyRule2 = new ResponsePolicyRule(); // ResponsePolicyRule | 
    try {
      ResponsePolicyRulesUpdateResponse result = apiInstance.dnsResponsePolicyRulesUpdate(project, location, responsePolicy, responsePolicyRule, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, clientOperationId, responsePolicyRule2);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ResponsePolicyRulesApi#dnsResponsePolicyRulesUpdate");
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
| **project** | **String**| Identifies the project addressed by this request. | |
| **location** | **String**| Specifies the location of the resource. This information will be used for routing and will be part of the resource name. | |
| **responsePolicy** | **String**| User assigned name of the Response Policy containing the Response Policy Rule. | |
| **responsePolicyRule** | **String**| User assigned name of the Response Policy Rule addressed by this request. | |
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
| **clientOperationId** | **String**| For mutating operation requests only. An optional identifier specified by the client. Must be unique for operation resources in the Operations collection. | [optional] |
| **responsePolicyRule2** | [**ResponsePolicyRule**](ResponsePolicyRule.md)|  | [optional] |

### Return type

[**ResponsePolicyRulesUpdateResponse**](ResponsePolicyRulesUpdateResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

