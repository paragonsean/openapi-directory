# V1Api

All URIs are relative to *https://servicebroker.googleapis.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**servicebrokerGetIamPolicy**](V1Api.md#servicebrokerGetIamPolicy) | **GET** /v1/{resource}:getIamPolicy |  |
| [**servicebrokerSetIamPolicy**](V1Api.md#servicebrokerSetIamPolicy) | **POST** /v1/{resource}:setIamPolicy |  |
| [**servicebrokerTestIamPermissions**](V1Api.md#servicebrokerTestIamPermissions) | **POST** /v1/{resource}:testIamPermissions |  |


<a id="servicebrokerGetIamPolicy"></a>
# **servicebrokerGetIamPolicy**
> GoogleIamV1Policy servicebrokerGetIamPolicy(resource, $xgafv, oauthToken, paramCallback, alt, key, accessToken, uploadProtocol, prettyPrint, quotaUser, fields, uploadType, optionsRequestedPolicyVersion)



Gets the access control policy for a resource. Returns an empty policy if the resource exists and does not have a policy set.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.V1Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://servicebroker.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    V1Api apiInstance = new V1Api(defaultClient);
    String resource = "resource_example"; // String | REQUIRED: The resource for which the policy is being requested. See the operation documentation for the appropriate value for this field.
    String $xgafv = "1"; // String | V1 error format.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    String paramCallback = "paramCallback_example"; // String | JSONP
    String alt = "json"; // String | Data format for response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    Integer optionsRequestedPolicyVersion = 56; // Integer | Optional. The policy format version to be returned.  Valid values are 0, 1, and 3. Requests specifying an invalid value will be rejected.  Requests for policies with any conditional bindings must specify version 3. Policies without any conditional bindings may specify any valid value or leave the field unset.
    try {
      GoogleIamV1Policy result = apiInstance.servicebrokerGetIamPolicy(resource, $xgafv, oauthToken, paramCallback, alt, key, accessToken, uploadProtocol, prettyPrint, quotaUser, fields, uploadType, optionsRequestedPolicyVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling V1Api#servicebrokerGetIamPolicy");
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
| **resource** | **String**| REQUIRED: The resource for which the policy is being requested. See the operation documentation for the appropriate value for this field. | |
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **paramCallback** | **String**| JSONP | [optional] |
| **alt** | **String**| Data format for response. | [optional] [default to json] [enum: json, media, proto] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |
| **optionsRequestedPolicyVersion** | **Integer**| Optional. The policy format version to be returned.  Valid values are 0, 1, and 3. Requests specifying an invalid value will be rejected.  Requests for policies with any conditional bindings must specify version 3. Policies without any conditional bindings may specify any valid value or leave the field unset. | [optional] |

### Return type

[**GoogleIamV1Policy**](GoogleIamV1Policy.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="servicebrokerSetIamPolicy"></a>
# **servicebrokerSetIamPolicy**
> GoogleIamV1Policy servicebrokerSetIamPolicy(resource, $xgafv, oauthToken, paramCallback, alt, key, accessToken, uploadProtocol, prettyPrint, quotaUser, fields, uploadType, googleIamV1SetIamPolicyRequest)



Sets the access control policy on the specified resource. Replaces any existing policy.  Can return Public Errors: NOT_FOUND, INVALID_ARGUMENT and PERMISSION_DENIED

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.V1Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://servicebroker.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    V1Api apiInstance = new V1Api(defaultClient);
    String resource = "resource_example"; // String | REQUIRED: The resource for which the policy is being specified. See the operation documentation for the appropriate value for this field.
    String $xgafv = "1"; // String | V1 error format.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    String paramCallback = "paramCallback_example"; // String | JSONP
    String alt = "json"; // String | Data format for response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    GoogleIamV1SetIamPolicyRequest googleIamV1SetIamPolicyRequest = new GoogleIamV1SetIamPolicyRequest(); // GoogleIamV1SetIamPolicyRequest | 
    try {
      GoogleIamV1Policy result = apiInstance.servicebrokerSetIamPolicy(resource, $xgafv, oauthToken, paramCallback, alt, key, accessToken, uploadProtocol, prettyPrint, quotaUser, fields, uploadType, googleIamV1SetIamPolicyRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling V1Api#servicebrokerSetIamPolicy");
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
| **resource** | **String**| REQUIRED: The resource for which the policy is being specified. See the operation documentation for the appropriate value for this field. | |
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **paramCallback** | **String**| JSONP | [optional] |
| **alt** | **String**| Data format for response. | [optional] [default to json] [enum: json, media, proto] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |
| **googleIamV1SetIamPolicyRequest** | [**GoogleIamV1SetIamPolicyRequest**](GoogleIamV1SetIamPolicyRequest.md)|  | [optional] |

### Return type

[**GoogleIamV1Policy**](GoogleIamV1Policy.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="servicebrokerTestIamPermissions"></a>
# **servicebrokerTestIamPermissions**
> GoogleIamV1TestIamPermissionsResponse servicebrokerTestIamPermissions(resource, $xgafv, oauthToken, paramCallback, alt, key, accessToken, uploadProtocol, prettyPrint, quotaUser, fields, uploadType, googleIamV1TestIamPermissionsRequest)



Returns permissions that a caller has on the specified resource. If the resource does not exist, this will return an empty set of permissions, not a NOT_FOUND error.  Note: This operation is designed to be used for building permission-aware UIs and command-line tools, not for authorization checking. This operation may \&quot;fail open\&quot; without warning.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.V1Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://servicebroker.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    V1Api apiInstance = new V1Api(defaultClient);
    String resource = "resource_example"; // String | REQUIRED: The resource for which the policy detail is being requested. See the operation documentation for the appropriate value for this field.
    String $xgafv = "1"; // String | V1 error format.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    String paramCallback = "paramCallback_example"; // String | JSONP
    String alt = "json"; // String | Data format for response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    GoogleIamV1TestIamPermissionsRequest googleIamV1TestIamPermissionsRequest = new GoogleIamV1TestIamPermissionsRequest(); // GoogleIamV1TestIamPermissionsRequest | 
    try {
      GoogleIamV1TestIamPermissionsResponse result = apiInstance.servicebrokerTestIamPermissions(resource, $xgafv, oauthToken, paramCallback, alt, key, accessToken, uploadProtocol, prettyPrint, quotaUser, fields, uploadType, googleIamV1TestIamPermissionsRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling V1Api#servicebrokerTestIamPermissions");
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
| **resource** | **String**| REQUIRED: The resource for which the policy detail is being requested. See the operation documentation for the appropriate value for this field. | |
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **paramCallback** | **String**| JSONP | [optional] |
| **alt** | **String**| Data format for response. | [optional] [default to json] [enum: json, media, proto] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |
| **googleIamV1TestIamPermissionsRequest** | [**GoogleIamV1TestIamPermissionsRequest**](GoogleIamV1TestIamPermissionsRequest.md)|  | [optional] |

### Return type

[**GoogleIamV1TestIamPermissionsResponse**](GoogleIamV1TestIamPermissionsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

