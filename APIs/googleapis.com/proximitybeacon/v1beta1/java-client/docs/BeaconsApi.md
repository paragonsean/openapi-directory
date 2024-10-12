# BeaconsApi

All URIs are relative to *https://proximitybeacon.googleapis.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**proximitybeaconBeaconsActivate**](BeaconsApi.md#proximitybeaconBeaconsActivate) | **POST** /v1beta1/{beaconName}:activate |  |
| [**proximitybeaconBeaconsAttachmentsBatchDelete**](BeaconsApi.md#proximitybeaconBeaconsAttachmentsBatchDelete) | **POST** /v1beta1/{beaconName}/attachments:batchDelete |  |
| [**proximitybeaconBeaconsAttachmentsCreate**](BeaconsApi.md#proximitybeaconBeaconsAttachmentsCreate) | **POST** /v1beta1/{beaconName}/attachments |  |
| [**proximitybeaconBeaconsAttachmentsDelete**](BeaconsApi.md#proximitybeaconBeaconsAttachmentsDelete) | **DELETE** /v1beta1/{attachmentName} |  |
| [**proximitybeaconBeaconsAttachmentsList**](BeaconsApi.md#proximitybeaconBeaconsAttachmentsList) | **GET** /v1beta1/{beaconName}/attachments |  |
| [**proximitybeaconBeaconsDeactivate**](BeaconsApi.md#proximitybeaconBeaconsDeactivate) | **POST** /v1beta1/{beaconName}:deactivate |  |
| [**proximitybeaconBeaconsDecommission**](BeaconsApi.md#proximitybeaconBeaconsDecommission) | **POST** /v1beta1/{beaconName}:decommission |  |
| [**proximitybeaconBeaconsDelete**](BeaconsApi.md#proximitybeaconBeaconsDelete) | **DELETE** /v1beta1/{beaconName} |  |
| [**proximitybeaconBeaconsDiagnosticsList**](BeaconsApi.md#proximitybeaconBeaconsDiagnosticsList) | **GET** /v1beta1/{beaconName}/diagnostics |  |
| [**proximitybeaconBeaconsGet**](BeaconsApi.md#proximitybeaconBeaconsGet) | **GET** /v1beta1/{beaconName} |  |
| [**proximitybeaconBeaconsList**](BeaconsApi.md#proximitybeaconBeaconsList) | **GET** /v1beta1/beacons |  |
| [**proximitybeaconBeaconsRegister**](BeaconsApi.md#proximitybeaconBeaconsRegister) | **POST** /v1beta1/beacons:register |  |
| [**proximitybeaconBeaconsUpdate**](BeaconsApi.md#proximitybeaconBeaconsUpdate) | **PUT** /v1beta1/{beaconName} |  |


<a id="proximitybeaconBeaconsActivate"></a>
# **proximitybeaconBeaconsActivate**
> Object proximitybeaconBeaconsActivate(beaconName, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, projectId)



Activates a beacon. A beacon that is active will return information and attachment data when queried via &#x60;beaconinfo.getforobserved&#x60;. Calling this method on an already active beacon will do nothing (but will return a successful response code). Authenticate using an [OAuth access token](https://developers.google.com/identity/protocols/OAuth2) from a signed-in user with **Is owner** or **Can edit** permissions in the Google Developers Console project.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BeaconsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://proximitybeacon.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    BeaconsApi apiInstance = new BeaconsApi(defaultClient);
    String beaconName = "beaconName_example"; // String | Beacon that should be activated. A beacon name has the format \"beacons/N!beaconId\" where the beaconId is the base16 ID broadcast by the beacon and N is a code for the beacon's type. Possible values are `3` for Eddystone-UID, `4` for Eddystone-EID, `1` for iBeacon, or `5` for AltBeacon. For Eddystone-EID beacons, you may use either the current EID or the beacon's \"stable\" UID. Required.
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
    String projectId = "projectId_example"; // String | The project id of the beacon to activate. If the project id is not specified then the project making the request is used. The project id must match the project that owns the beacon. Optional.
    try {
      Object result = apiInstance.proximitybeaconBeaconsActivate(beaconName, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, projectId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BeaconsApi#proximitybeaconBeaconsActivate");
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
| **beaconName** | **String**| Beacon that should be activated. A beacon name has the format \&quot;beacons/N!beaconId\&quot; where the beaconId is the base16 ID broadcast by the beacon and N is a code for the beacon&#39;s type. Possible values are &#x60;3&#x60; for Eddystone-UID, &#x60;4&#x60; for Eddystone-EID, &#x60;1&#x60; for iBeacon, or &#x60;5&#x60; for AltBeacon. For Eddystone-EID beacons, you may use either the current EID or the beacon&#39;s \&quot;stable\&quot; UID. Required. | |
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
| **projectId** | **String**| The project id of the beacon to activate. If the project id is not specified then the project making the request is used. The project id must match the project that owns the beacon. Optional. | [optional] |

### Return type

**Object**

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="proximitybeaconBeaconsAttachmentsBatchDelete"></a>
# **proximitybeaconBeaconsAttachmentsBatchDelete**
> DeleteAttachmentsResponse proximitybeaconBeaconsAttachmentsBatchDelete(beaconName, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, namespacedType, projectId)



Deletes multiple attachments on a given beacon. This operation is permanent and cannot be undone. You can optionally specify &#x60;namespacedType&#x60; to choose which attachments should be deleted. If you do not specify &#x60;namespacedType&#x60;, all your attachments on the given beacon will be deleted. You also may explicitly specify &#x60;*_/_*&#x60; to delete all. Authenticate using an [OAuth access token](https://developers.google.com/identity/protocols/OAuth2) from a signed-in user with **Is owner** or **Can edit** permissions in the Google Developers Console project.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BeaconsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://proximitybeacon.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    BeaconsApi apiInstance = new BeaconsApi(defaultClient);
    String beaconName = "beaconName_example"; // String | The beacon whose attachments should be deleted. A beacon name has the format \"beacons/N!beaconId\" where the beaconId is the base16 ID broadcast by the beacon and N is a code for the beacon's type. Possible values are `3` for Eddystone-UID, `4` for Eddystone-EID, `1` for iBeacon, or `5` for AltBeacon. For Eddystone-EID beacons, you may use either the current EID or the beacon's \"stable\" UID. Required.
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
    String namespacedType = "namespacedType_example"; // String | Specifies the namespace and type of attachments to delete in `namespace/type` format. Accepts `*_/_*` to specify \"all types in all namespaces\". Optional.
    String projectId = "projectId_example"; // String | The project id to delete beacon attachments under. This field can be used when \"*\" is specified to mean all attachment namespaces. Projects may have multiple attachments with multiple namespaces. If \"*\" is specified and the projectId string is empty, then the project making the request is used. Optional.
    try {
      DeleteAttachmentsResponse result = apiInstance.proximitybeaconBeaconsAttachmentsBatchDelete(beaconName, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, namespacedType, projectId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BeaconsApi#proximitybeaconBeaconsAttachmentsBatchDelete");
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
| **beaconName** | **String**| The beacon whose attachments should be deleted. A beacon name has the format \&quot;beacons/N!beaconId\&quot; where the beaconId is the base16 ID broadcast by the beacon and N is a code for the beacon&#39;s type. Possible values are &#x60;3&#x60; for Eddystone-UID, &#x60;4&#x60; for Eddystone-EID, &#x60;1&#x60; for iBeacon, or &#x60;5&#x60; for AltBeacon. For Eddystone-EID beacons, you may use either the current EID or the beacon&#39;s \&quot;stable\&quot; UID. Required. | |
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
| **namespacedType** | **String**| Specifies the namespace and type of attachments to delete in &#x60;namespace/type&#x60; format. Accepts &#x60;*_/_*&#x60; to specify \&quot;all types in all namespaces\&quot;. Optional. | [optional] |
| **projectId** | **String**| The project id to delete beacon attachments under. This field can be used when \&quot;*\&quot; is specified to mean all attachment namespaces. Projects may have multiple attachments with multiple namespaces. If \&quot;*\&quot; is specified and the projectId string is empty, then the project making the request is used. Optional. | [optional] |

### Return type

[**DeleteAttachmentsResponse**](DeleteAttachmentsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="proximitybeaconBeaconsAttachmentsCreate"></a>
# **proximitybeaconBeaconsAttachmentsCreate**
> BeaconAttachment proximitybeaconBeaconsAttachmentsCreate(beaconName, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, projectId, beaconAttachment)



Associates the given data with the specified beacon. Attachment data must contain two parts: - A namespaced type. - The actual attachment data itself. The namespaced type consists of two parts, the namespace and the type. The namespace must be one of the values returned by the &#x60;namespaces&#x60; endpoint, while the type can be a string of any characters except for the forward slash (&#x60;/&#x60;) up to 100 characters in length. Attachment data can be up to 1024 bytes long. Authenticate using an [OAuth access token](https://developers.google.com/identity/protocols/OAuth2) from a signed-in user with **Is owner** or **Can edit** permissions in the Google Developers Console project.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BeaconsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://proximitybeacon.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    BeaconsApi apiInstance = new BeaconsApi(defaultClient);
    String beaconName = "beaconName_example"; // String | Beacon on which the attachment should be created. A beacon name has the format \"beacons/N!beaconId\" where the beaconId is the base16 ID broadcast by the beacon and N is a code for the beacon's type. Possible values are `3` for Eddystone-UID, `4` for Eddystone-EID, `1` for iBeacon, or `5` for AltBeacon. For Eddystone-EID beacons, you may use either the current EID or the beacon's \"stable\" UID. Required.
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
    String projectId = "projectId_example"; // String | The project id of the project the attachment will belong to. If the project id is not specified then the project making the request is used. Optional.
    BeaconAttachment beaconAttachment = new BeaconAttachment(); // BeaconAttachment | 
    try {
      BeaconAttachment result = apiInstance.proximitybeaconBeaconsAttachmentsCreate(beaconName, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, projectId, beaconAttachment);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BeaconsApi#proximitybeaconBeaconsAttachmentsCreate");
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
| **beaconName** | **String**| Beacon on which the attachment should be created. A beacon name has the format \&quot;beacons/N!beaconId\&quot; where the beaconId is the base16 ID broadcast by the beacon and N is a code for the beacon&#39;s type. Possible values are &#x60;3&#x60; for Eddystone-UID, &#x60;4&#x60; for Eddystone-EID, &#x60;1&#x60; for iBeacon, or &#x60;5&#x60; for AltBeacon. For Eddystone-EID beacons, you may use either the current EID or the beacon&#39;s \&quot;stable\&quot; UID. Required. | |
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
| **projectId** | **String**| The project id of the project the attachment will belong to. If the project id is not specified then the project making the request is used. Optional. | [optional] |
| **beaconAttachment** | [**BeaconAttachment**](BeaconAttachment.md)|  | [optional] |

### Return type

[**BeaconAttachment**](BeaconAttachment.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="proximitybeaconBeaconsAttachmentsDelete"></a>
# **proximitybeaconBeaconsAttachmentsDelete**
> Object proximitybeaconBeaconsAttachmentsDelete(attachmentName, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, projectId)



Deletes the specified attachment for the given beacon. Each attachment has a unique attachment name (&#x60;attachmentName&#x60;) which is returned when you fetch the attachment data via this API. You specify this with the delete request to control which attachment is removed. This operation cannot be undone. Authenticate using an [OAuth access token](https://developers.google.com/identity/protocols/OAuth2) from a signed-in user with **Is owner** or **Can edit** permissions in the Google Developers Console project.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BeaconsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://proximitybeacon.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    BeaconsApi apiInstance = new BeaconsApi(defaultClient);
    String attachmentName = "attachmentName_example"; // String | The attachment name (`attachmentName`) of the attachment to remove. For example: `beacons/3!893737abc9/attachments/c5e937-af0-494-959-ec49d12738`. For Eddystone-EID beacons, the beacon ID portion (`3!893737abc9`) may be the beacon's current EID, or its \"stable\" Eddystone-UID. Required.
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
    String projectId = "projectId_example"; // String | The project id of the attachment to delete. If not provided, the project that is making the request is used. Optional.
    try {
      Object result = apiInstance.proximitybeaconBeaconsAttachmentsDelete(attachmentName, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, projectId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BeaconsApi#proximitybeaconBeaconsAttachmentsDelete");
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
| **attachmentName** | **String**| The attachment name (&#x60;attachmentName&#x60;) of the attachment to remove. For example: &#x60;beacons/3!893737abc9/attachments/c5e937-af0-494-959-ec49d12738&#x60;. For Eddystone-EID beacons, the beacon ID portion (&#x60;3!893737abc9&#x60;) may be the beacon&#39;s current EID, or its \&quot;stable\&quot; Eddystone-UID. Required. | |
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
| **projectId** | **String**| The project id of the attachment to delete. If not provided, the project that is making the request is used. Optional. | [optional] |

### Return type

**Object**

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="proximitybeaconBeaconsAttachmentsList"></a>
# **proximitybeaconBeaconsAttachmentsList**
> ListBeaconAttachmentsResponse proximitybeaconBeaconsAttachmentsList(beaconName, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, namespacedType, projectId)



Returns the attachments for the specified beacon that match the specified namespaced-type pattern. To control which namespaced types are returned, you add the &#x60;namespacedType&#x60; query parameter to the request. You must either use &#x60;*_/_*&#x60;, to return all attachments, or the namespace must be one of the ones returned from the &#x60;namespaces&#x60; endpoint. Authenticate using an [OAuth access token](https://developers.google.com/identity/protocols/OAuth2) from a signed-in user with **viewer**, **Is owner** or **Can edit** permissions in the Google Developers Console project.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BeaconsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://proximitybeacon.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    BeaconsApi apiInstance = new BeaconsApi(defaultClient);
    String beaconName = "beaconName_example"; // String | Beacon whose attachments should be fetched. A beacon name has the format \"beacons/N!beaconId\" where the beaconId is the base16 ID broadcast by the beacon and N is a code for the beacon's type. Possible values are `3` for Eddystone-UID, `4` for Eddystone-EID, `1` for iBeacon, or `5` for AltBeacon. For Eddystone-EID beacons, you may use either the current EID or the beacon's \"stable\" UID. Required.
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
    String namespacedType = "namespacedType_example"; // String | Specifies the namespace and type of attachment to include in response in namespace/type format. Accepts `*_/_*` to specify \"all types in all namespaces\".
    String projectId = "projectId_example"; // String | The project id to list beacon attachments under. This field can be used when \"*\" is specified to mean all attachment namespaces. Projects may have multiple attachments with multiple namespaces. If \"*\" is specified and the projectId string is empty, then the project making the request is used. Optional.
    try {
      ListBeaconAttachmentsResponse result = apiInstance.proximitybeaconBeaconsAttachmentsList(beaconName, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, namespacedType, projectId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BeaconsApi#proximitybeaconBeaconsAttachmentsList");
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
| **beaconName** | **String**| Beacon whose attachments should be fetched. A beacon name has the format \&quot;beacons/N!beaconId\&quot; where the beaconId is the base16 ID broadcast by the beacon and N is a code for the beacon&#39;s type. Possible values are &#x60;3&#x60; for Eddystone-UID, &#x60;4&#x60; for Eddystone-EID, &#x60;1&#x60; for iBeacon, or &#x60;5&#x60; for AltBeacon. For Eddystone-EID beacons, you may use either the current EID or the beacon&#39;s \&quot;stable\&quot; UID. Required. | |
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
| **namespacedType** | **String**| Specifies the namespace and type of attachment to include in response in namespace/type format. Accepts &#x60;*_/_*&#x60; to specify \&quot;all types in all namespaces\&quot;. | [optional] |
| **projectId** | **String**| The project id to list beacon attachments under. This field can be used when \&quot;*\&quot; is specified to mean all attachment namespaces. Projects may have multiple attachments with multiple namespaces. If \&quot;*\&quot; is specified and the projectId string is empty, then the project making the request is used. Optional. | [optional] |

### Return type

[**ListBeaconAttachmentsResponse**](ListBeaconAttachmentsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="proximitybeaconBeaconsDeactivate"></a>
# **proximitybeaconBeaconsDeactivate**
> Object proximitybeaconBeaconsDeactivate(beaconName, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, projectId)



Deactivates a beacon. Once deactivated, the API will not return information nor attachment data for the beacon when queried via &#x60;beaconinfo.getforobserved&#x60;. Calling this method on an already inactive beacon will do nothing (but will return a successful response code). Authenticate using an [OAuth access token](https://developers.google.com/identity/protocols/OAuth2) from a signed-in user with **Is owner** or **Can edit** permissions in the Google Developers Console project.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BeaconsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://proximitybeacon.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    BeaconsApi apiInstance = new BeaconsApi(defaultClient);
    String beaconName = "beaconName_example"; // String | Beacon that should be deactivated. A beacon name has the format \"beacons/N!beaconId\" where the beaconId is the base16 ID broadcast by the beacon and N is a code for the beacon's type. Possible values are `3` for Eddystone-UID, `4` for Eddystone-EID, `1` for iBeacon, or `5` for AltBeacon. For Eddystone-EID beacons, you may use either the current EID or the beacon's \"stable\" UID. Required.
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
    String projectId = "projectId_example"; // String | The project id of the beacon to deactivate. If the project id is not specified then the project making the request is used. The project id must match the project that owns the beacon. Optional.
    try {
      Object result = apiInstance.proximitybeaconBeaconsDeactivate(beaconName, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, projectId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BeaconsApi#proximitybeaconBeaconsDeactivate");
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
| **beaconName** | **String**| Beacon that should be deactivated. A beacon name has the format \&quot;beacons/N!beaconId\&quot; where the beaconId is the base16 ID broadcast by the beacon and N is a code for the beacon&#39;s type. Possible values are &#x60;3&#x60; for Eddystone-UID, &#x60;4&#x60; for Eddystone-EID, &#x60;1&#x60; for iBeacon, or &#x60;5&#x60; for AltBeacon. For Eddystone-EID beacons, you may use either the current EID or the beacon&#39;s \&quot;stable\&quot; UID. Required. | |
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
| **projectId** | **String**| The project id of the beacon to deactivate. If the project id is not specified then the project making the request is used. The project id must match the project that owns the beacon. Optional. | [optional] |

### Return type

**Object**

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="proximitybeaconBeaconsDecommission"></a>
# **proximitybeaconBeaconsDecommission**
> Object proximitybeaconBeaconsDecommission(beaconName, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, projectId)



Decommissions the specified beacon in the service. This beacon will no longer be returned from &#x60;beaconinfo.getforobserved&#x60;. This operation is permanent -- you will not be able to re-register a beacon with this ID again. Authenticate using an [OAuth access token](https://developers.google.com/identity/protocols/OAuth2) from a signed-in user with **Is owner** or **Can edit** permissions in the Google Developers Console project.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BeaconsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://proximitybeacon.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    BeaconsApi apiInstance = new BeaconsApi(defaultClient);
    String beaconName = "beaconName_example"; // String | Beacon that should be decommissioned. A beacon name has the format \"beacons/N!beaconId\" where the beaconId is the base16 ID broadcast by the beacon and N is a code for the beacon's type. Possible values are `3` for Eddystone-UID, `4` for Eddystone-EID, `1` for iBeacon, or `5` for AltBeacon. For Eddystone-EID beacons, you may use either the current EID of the beacon's \"stable\" UID. Required.
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
    String projectId = "projectId_example"; // String | The project id of the beacon to decommission. If the project id is not specified then the project making the request is used. The project id must match the project that owns the beacon. Optional.
    try {
      Object result = apiInstance.proximitybeaconBeaconsDecommission(beaconName, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, projectId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BeaconsApi#proximitybeaconBeaconsDecommission");
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
| **beaconName** | **String**| Beacon that should be decommissioned. A beacon name has the format \&quot;beacons/N!beaconId\&quot; where the beaconId is the base16 ID broadcast by the beacon and N is a code for the beacon&#39;s type. Possible values are &#x60;3&#x60; for Eddystone-UID, &#x60;4&#x60; for Eddystone-EID, &#x60;1&#x60; for iBeacon, or &#x60;5&#x60; for AltBeacon. For Eddystone-EID beacons, you may use either the current EID of the beacon&#39;s \&quot;stable\&quot; UID. Required. | |
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
| **projectId** | **String**| The project id of the beacon to decommission. If the project id is not specified then the project making the request is used. The project id must match the project that owns the beacon. Optional. | [optional] |

### Return type

**Object**

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="proximitybeaconBeaconsDelete"></a>
# **proximitybeaconBeaconsDelete**
> Object proximitybeaconBeaconsDelete(beaconName, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, projectId)



Deletes the specified beacon including all diagnostics data for the beacon as well as any attachments on the beacon (including those belonging to other projects). This operation cannot be undone. Authenticate using an [OAuth access token](https://developers.google.com/identity/protocols/OAuth2) from a signed-in user with **Is owner** or **Can edit** permissions in the Google Developers Console project.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BeaconsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://proximitybeacon.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    BeaconsApi apiInstance = new BeaconsApi(defaultClient);
    String beaconName = "beaconName_example"; // String | Beacon that should be deleted. A beacon name has the format \"beacons/N!beaconId\" where the beaconId is the base16 ID broadcast by the beacon and N is a code for the beacon's type. Possible values are `3` for Eddystone-UID, `4` for Eddystone-EID, `1` for iBeacon, or `5` for AltBeacon. For Eddystone-EID beacons, you may use either the current EID or the beacon's \"stable\" UID. Required.
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
    String projectId = "projectId_example"; // String | The project id of the beacon to delete. If not provided, the project that is making the request is used. Optional.
    try {
      Object result = apiInstance.proximitybeaconBeaconsDelete(beaconName, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, projectId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BeaconsApi#proximitybeaconBeaconsDelete");
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
| **beaconName** | **String**| Beacon that should be deleted. A beacon name has the format \&quot;beacons/N!beaconId\&quot; where the beaconId is the base16 ID broadcast by the beacon and N is a code for the beacon&#39;s type. Possible values are &#x60;3&#x60; for Eddystone-UID, &#x60;4&#x60; for Eddystone-EID, &#x60;1&#x60; for iBeacon, or &#x60;5&#x60; for AltBeacon. For Eddystone-EID beacons, you may use either the current EID or the beacon&#39;s \&quot;stable\&quot; UID. Required. | |
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
| **projectId** | **String**| The project id of the beacon to delete. If not provided, the project that is making the request is used. Optional. | [optional] |

### Return type

**Object**

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="proximitybeaconBeaconsDiagnosticsList"></a>
# **proximitybeaconBeaconsDiagnosticsList**
> ListDiagnosticsResponse proximitybeaconBeaconsDiagnosticsList(beaconName, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, alertFilter, pageSize, pageToken, projectId)



List the diagnostics for a single beacon. You can also list diagnostics for all the beacons owned by your Google Developers Console project by using the beacon name &#x60;beacons/-&#x60;. Authenticate using an [OAuth access token](https://developers.google.com/identity/protocols/OAuth2) from a signed-in user with **viewer**, **Is owner** or **Can edit** permissions in the Google Developers Console project.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BeaconsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://proximitybeacon.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    BeaconsApi apiInstance = new BeaconsApi(defaultClient);
    String beaconName = "beaconName_example"; // String | Beacon that the diagnostics are for.
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
    String alertFilter = "ALERT_UNSPECIFIED"; // String | Requests only beacons that have the given alert. For example, to find beacons that have low batteries use `alert_filter=LOW_BATTERY`.
    Integer pageSize = 56; // Integer | Specifies the maximum number of results to return. Defaults to 10. Maximum 1000. Optional.
    String pageToken = "pageToken_example"; // String | Requests results that occur after the `page_token`, obtained from the response to a previous request. Optional.
    String projectId = "projectId_example"; // String | Requests only diagnostic records for the given project id. If not set, then the project making the request will be used for looking up diagnostic records. Optional.
    try {
      ListDiagnosticsResponse result = apiInstance.proximitybeaconBeaconsDiagnosticsList(beaconName, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, alertFilter, pageSize, pageToken, projectId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BeaconsApi#proximitybeaconBeaconsDiagnosticsList");
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
| **beaconName** | **String**| Beacon that the diagnostics are for. | |
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
| **alertFilter** | **String**| Requests only beacons that have the given alert. For example, to find beacons that have low batteries use &#x60;alert_filter&#x3D;LOW_BATTERY&#x60;. | [optional] [enum: ALERT_UNSPECIFIED, WRONG_LOCATION, LOW_BATTERY, LOW_ACTIVITY] |
| **pageSize** | **Integer**| Specifies the maximum number of results to return. Defaults to 10. Maximum 1000. Optional. | [optional] |
| **pageToken** | **String**| Requests results that occur after the &#x60;page_token&#x60;, obtained from the response to a previous request. Optional. | [optional] |
| **projectId** | **String**| Requests only diagnostic records for the given project id. If not set, then the project making the request will be used for looking up diagnostic records. Optional. | [optional] |

### Return type

[**ListDiagnosticsResponse**](ListDiagnosticsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="proximitybeaconBeaconsGet"></a>
# **proximitybeaconBeaconsGet**
> Beacon proximitybeaconBeaconsGet(beaconName, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, projectId)



Returns detailed information about the specified beacon. Authenticate using an [OAuth access token](https://developers.google.com/identity/protocols/OAuth2) from a signed-in user with **viewer**, **Is owner** or **Can edit** permissions in the Google Developers Console project. Requests may supply an Eddystone-EID beacon name in the form: &#x60;beacons/4!beaconId&#x60; where the &#x60;beaconId&#x60; is the base16 ephemeral ID broadcast by the beacon. The returned &#x60;Beacon&#x60; object will contain the beacon&#39;s stable Eddystone-UID. Clients not authorized to resolve the beacon&#39;s ephemeral Eddystone-EID broadcast will receive an error.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BeaconsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://proximitybeacon.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    BeaconsApi apiInstance = new BeaconsApi(defaultClient);
    String beaconName = "beaconName_example"; // String | Resource name of this beacon. A beacon name has the format \"beacons/N!beaconId\" where the beaconId is the base16 ID broadcast by the beacon and N is a code for the beacon's type. Possible values are `3` for Eddystone-UID, `4` for Eddystone-EID, `1` for iBeacon, or `5` for AltBeacon. For Eddystone-EID beacons, you may use either the current EID or the beacon's \"stable\" UID. Required.
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
    String projectId = "projectId_example"; // String | The project id of the beacon to request. If the project id is not specified then the project making the request is used. The project id must match the project that owns the beacon. Optional.
    try {
      Beacon result = apiInstance.proximitybeaconBeaconsGet(beaconName, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, projectId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BeaconsApi#proximitybeaconBeaconsGet");
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
| **beaconName** | **String**| Resource name of this beacon. A beacon name has the format \&quot;beacons/N!beaconId\&quot; where the beaconId is the base16 ID broadcast by the beacon and N is a code for the beacon&#39;s type. Possible values are &#x60;3&#x60; for Eddystone-UID, &#x60;4&#x60; for Eddystone-EID, &#x60;1&#x60; for iBeacon, or &#x60;5&#x60; for AltBeacon. For Eddystone-EID beacons, you may use either the current EID or the beacon&#39;s \&quot;stable\&quot; UID. Required. | |
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
| **projectId** | **String**| The project id of the beacon to request. If the project id is not specified then the project making the request is used. The project id must match the project that owns the beacon. Optional. | [optional] |

### Return type

[**Beacon**](Beacon.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="proximitybeaconBeaconsList"></a>
# **proximitybeaconBeaconsList**
> ListBeaconsResponse proximitybeaconBeaconsList($xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, pageSize, pageToken, projectId, q)



Searches the beacon registry for beacons that match the given search criteria. Only those beacons that the client has permission to list will be returned. Authenticate using an [OAuth access token](https://developers.google.com/identity/protocols/OAuth2) from a signed-in user with **viewer**, **Is owner** or **Can edit** permissions in the Google Developers Console project.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BeaconsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://proximitybeacon.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    BeaconsApi apiInstance = new BeaconsApi(defaultClient);
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
    Integer pageSize = 56; // Integer | The maximum number of records to return for this request, up to a server-defined upper limit.
    String pageToken = "pageToken_example"; // String | A pagination token obtained from a previous request to list beacons.
    String projectId = "projectId_example"; // String | The project id to list beacons under. If not present then the project credential that made the request is used as the project. Optional.
    String q = "q_example"; // String | Filter query string that supports the following field filters: * **description:`\"\"`** For example: **description:\"Room 3\"** Returns beacons whose description matches tokens in the string \"Room 3\" (not necessarily that exact string). The string must be double-quoted. * **status:``** For example: **status:active** Returns beacons whose status matches the given value. Values must be one of the Beacon.Status enum values (case insensitive). Accepts multiple filters which will be combined with OR logic. * **stability:``** For example: **stability:mobile** Returns beacons whose expected stability matches the given value. Values must be one of the Beacon.Stability enum values (case insensitive). Accepts multiple filters which will be combined with OR logic. * **place\\_id:`\"\"`** For example: **place\\_id:\"ChIJVSZzVR8FdkgRXGmmm6SslKw=\"** Returns beacons explicitly registered at the given place, expressed as a Place ID obtained from [Google Places API](/places/place-id). Does not match places inside the given place. Does not consider the beacon's actual location (which may be different from its registered place). Accepts multiple filters that will be combined with OR logic. The place ID must be double-quoted. * **registration\\_time`[<|>|<=|>=]`** For example: **registration\\_time>=1433116800** Returns beacons whose registration time matches the given filter. Supports the operators: <, >, <=, and >=. Timestamp must be expressed as an integer number of seconds since midnight January 1, 1970 UTC. Accepts at most two filters that will be combined with AND logic, to support \"between\" semantics. If more than two are supplied, the latter ones are ignored. * **lat:` lng: radius:`** For example: **lat:51.1232343 lng:-1.093852 radius:1000** Returns beacons whose registered location is within the given circle. When any of these fields are given, all are required. Latitude and longitude must be decimal degrees between -90.0 and 90.0 and between -180.0 and 180.0 respectively. Radius must be an integer number of meters between 10 and 1,000,000 (1000 km). * **property:`\"=\"`** For example: **property:\"battery-type=CR2032\"** Returns beacons which have a property of the given name and value. Supports multiple filters which will be combined with OR logic. The entire name=value string must be double-quoted as one string. * **attachment\\_type:`\"\"`** For example: **attachment_type:\"my-namespace/my-type\"** Returns beacons having at least one attachment of the given namespaced type. Supports \"any within this namespace\" via the partial wildcard syntax: \"my-namespace/_*\". Supports multiple filters which will be combined with OR logic. The string must be double-quoted. * **indoor\\_level:`\"\"`** For example: **indoor\\_level:\"1\"** Returns beacons which are located on the given indoor level. Accepts multiple filters that will be combined with OR logic. Multiple filters on the same field are combined with OR logic (except registration_time which is combined with AND logic). Multiple filters on different fields are combined with AND logic. Filters should be separated by spaces. As with any HTTP query string parameter, the whole filter expression must be URL-encoded. Example REST request: `GET /v1beta1/beacons?q=status:active%20lat:51.123%20lng:-1.095%20radius:1000`
    try {
      ListBeaconsResponse result = apiInstance.proximitybeaconBeaconsList($xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, pageSize, pageToken, projectId, q);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BeaconsApi#proximitybeaconBeaconsList");
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
| **pageSize** | **Integer**| The maximum number of records to return for this request, up to a server-defined upper limit. | [optional] |
| **pageToken** | **String**| A pagination token obtained from a previous request to list beacons. | [optional] |
| **projectId** | **String**| The project id to list beacons under. If not present then the project credential that made the request is used as the project. Optional. | [optional] |
| **q** | **String**| Filter query string that supports the following field filters: * **description:&#x60;\&quot;\&quot;&#x60;** For example: **description:\&quot;Room 3\&quot;** Returns beacons whose description matches tokens in the string \&quot;Room 3\&quot; (not necessarily that exact string). The string must be double-quoted. * **status:&#x60;&#x60;** For example: **status:active** Returns beacons whose status matches the given value. Values must be one of the Beacon.Status enum values (case insensitive). Accepts multiple filters which will be combined with OR logic. * **stability:&#x60;&#x60;** For example: **stability:mobile** Returns beacons whose expected stability matches the given value. Values must be one of the Beacon.Stability enum values (case insensitive). Accepts multiple filters which will be combined with OR logic. * **place\\_id:&#x60;\&quot;\&quot;&#x60;** For example: **place\\_id:\&quot;ChIJVSZzVR8FdkgRXGmmm6SslKw&#x3D;\&quot;** Returns beacons explicitly registered at the given place, expressed as a Place ID obtained from [Google Places API](/places/place-id). Does not match places inside the given place. Does not consider the beacon&#39;s actual location (which may be different from its registered place). Accepts multiple filters that will be combined with OR logic. The place ID must be double-quoted. * **registration\\_time&#x60;[&lt;|&gt;|&lt;&#x3D;|&gt;&#x3D;]&#x60;** For example: **registration\\_time&gt;&#x3D;1433116800** Returns beacons whose registration time matches the given filter. Supports the operators: &lt;, &gt;, &lt;&#x3D;, and &gt;&#x3D;. Timestamp must be expressed as an integer number of seconds since midnight January 1, 1970 UTC. Accepts at most two filters that will be combined with AND logic, to support \&quot;between\&quot; semantics. If more than two are supplied, the latter ones are ignored. * **lat:&#x60; lng: radius:&#x60;** For example: **lat:51.1232343 lng:-1.093852 radius:1000** Returns beacons whose registered location is within the given circle. When any of these fields are given, all are required. Latitude and longitude must be decimal degrees between -90.0 and 90.0 and between -180.0 and 180.0 respectively. Radius must be an integer number of meters between 10 and 1,000,000 (1000 km). * **property:&#x60;\&quot;&#x3D;\&quot;&#x60;** For example: **property:\&quot;battery-type&#x3D;CR2032\&quot;** Returns beacons which have a property of the given name and value. Supports multiple filters which will be combined with OR logic. The entire name&#x3D;value string must be double-quoted as one string. * **attachment\\_type:&#x60;\&quot;\&quot;&#x60;** For example: **attachment_type:\&quot;my-namespace/my-type\&quot;** Returns beacons having at least one attachment of the given namespaced type. Supports \&quot;any within this namespace\&quot; via the partial wildcard syntax: \&quot;my-namespace/_*\&quot;. Supports multiple filters which will be combined with OR logic. The string must be double-quoted. * **indoor\\_level:&#x60;\&quot;\&quot;&#x60;** For example: **indoor\\_level:\&quot;1\&quot;** Returns beacons which are located on the given indoor level. Accepts multiple filters that will be combined with OR logic. Multiple filters on the same field are combined with OR logic (except registration_time which is combined with AND logic). Multiple filters on different fields are combined with AND logic. Filters should be separated by spaces. As with any HTTP query string parameter, the whole filter expression must be URL-encoded. Example REST request: &#x60;GET /v1beta1/beacons?q&#x3D;status:active%20lat:51.123%20lng:-1.095%20radius:1000&#x60; | [optional] |

### Return type

[**ListBeaconsResponse**](ListBeaconsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="proximitybeaconBeaconsRegister"></a>
# **proximitybeaconBeaconsRegister**
> Beacon proximitybeaconBeaconsRegister($xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, projectId, beacon)



Registers a previously unregistered beacon given its &#x60;advertisedId&#x60;. These IDs are unique within the system. An ID can be registered only once. Authenticate using an [OAuth access token](https://developers.google.com/identity/protocols/OAuth2) from a signed-in user with **Is owner** or **Can edit** permissions in the Google Developers Console project.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BeaconsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://proximitybeacon.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    BeaconsApi apiInstance = new BeaconsApi(defaultClient);
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
    String projectId = "projectId_example"; // String | The project id of the project the beacon will be registered to. If the project id is not specified then the project making the request is used. Optional.
    Beacon beacon = new Beacon(); // Beacon | 
    try {
      Beacon result = apiInstance.proximitybeaconBeaconsRegister($xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, projectId, beacon);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BeaconsApi#proximitybeaconBeaconsRegister");
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
| **projectId** | **String**| The project id of the project the beacon will be registered to. If the project id is not specified then the project making the request is used. Optional. | [optional] |
| **beacon** | [**Beacon**](Beacon.md)|  | [optional] |

### Return type

[**Beacon**](Beacon.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="proximitybeaconBeaconsUpdate"></a>
# **proximitybeaconBeaconsUpdate**
> Beacon proximitybeaconBeaconsUpdate(beaconName, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, projectId, beacon)



Updates the information about the specified beacon. **Any field that you do not populate in the submitted beacon will be permanently erased**, so you should follow the \&quot;read, modify, write\&quot; pattern to avoid inadvertently destroying data. Changes to the beacon status via this method will be silently ignored. To update beacon status, use the separate methods on this API for activation, deactivation, and decommissioning. Authenticate using an [OAuth access token](https://developers.google.com/identity/protocols/OAuth2) from a signed-in user with **Is owner** or **Can edit** permissions in the Google Developers Console project.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BeaconsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://proximitybeacon.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    BeaconsApi apiInstance = new BeaconsApi(defaultClient);
    String beaconName = "beaconName_example"; // String | Resource name of this beacon. A beacon name has the format \"beacons/N!beaconId\" where the beaconId is the base16 ID broadcast by the beacon and N is a code for the beacon's type. Possible values are `3` for Eddystone, `1` for iBeacon, or `5` for AltBeacon. This field must be left empty when registering. After reading a beacon, clients can use the name for future operations.
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
    String projectId = "projectId_example"; // String | The project id of the beacon to update. If the project id is not specified then the project making the request is used. The project id must match the project that owns the beacon. Optional.
    Beacon beacon = new Beacon(); // Beacon | 
    try {
      Beacon result = apiInstance.proximitybeaconBeaconsUpdate(beaconName, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, projectId, beacon);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BeaconsApi#proximitybeaconBeaconsUpdate");
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
| **beaconName** | **String**| Resource name of this beacon. A beacon name has the format \&quot;beacons/N!beaconId\&quot; where the beaconId is the base16 ID broadcast by the beacon and N is a code for the beacon&#39;s type. Possible values are &#x60;3&#x60; for Eddystone, &#x60;1&#x60; for iBeacon, or &#x60;5&#x60; for AltBeacon. This field must be left empty when registering. After reading a beacon, clients can use the name for future operations. | |
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
| **projectId** | **String**| The project id of the beacon to update. If the project id is not specified then the project making the request is used. The project id must match the project that owns the beacon. Optional. | [optional] |
| **beacon** | [**Beacon**](Beacon.md)|  | [optional] |

### Return type

[**Beacon**](Beacon.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

