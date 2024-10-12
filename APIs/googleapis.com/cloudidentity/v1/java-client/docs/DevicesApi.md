# DevicesApi

All URIs are relative to *https://cloudidentity.googleapis.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**cloudidentityDevicesCreate**](DevicesApi.md#cloudidentityDevicesCreate) | **POST** /v1/devices |  |
| [**cloudidentityDevicesDeviceUsersApprove**](DevicesApi.md#cloudidentityDevicesDeviceUsersApprove) | **POST** /v1/{name}:approve |  |
| [**cloudidentityDevicesDeviceUsersBlock**](DevicesApi.md#cloudidentityDevicesDeviceUsersBlock) | **POST** /v1/{name}:block |  |
| [**cloudidentityDevicesDeviceUsersCancelWipe**](DevicesApi.md#cloudidentityDevicesDeviceUsersCancelWipe) | **POST** /v1/{name}:cancelWipe |  |
| [**cloudidentityDevicesDeviceUsersClientStatesList**](DevicesApi.md#cloudidentityDevicesDeviceUsersClientStatesList) | **GET** /v1/{parent}/clientStates |  |
| [**cloudidentityDevicesDeviceUsersList**](DevicesApi.md#cloudidentityDevicesDeviceUsersList) | **GET** /v1/{parent}/deviceUsers |  |
| [**cloudidentityDevicesDeviceUsersLookup**](DevicesApi.md#cloudidentityDevicesDeviceUsersLookup) | **GET** /v1/{parent}:lookup |  |
| [**cloudidentityDevicesDeviceUsersWipe**](DevicesApi.md#cloudidentityDevicesDeviceUsersWipe) | **POST** /v1/{name}:wipe |  |
| [**cloudidentityDevicesList**](DevicesApi.md#cloudidentityDevicesList) | **GET** /v1/devices |  |


<a id="cloudidentityDevicesCreate"></a>
# **cloudidentityDevicesCreate**
> Operation cloudidentityDevicesCreate($xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, customer, googleAppsCloudidentityDevicesV1Device)



Creates a device. Only company-owned device may be created. **Note**: This method is available only to customers who have one of the following SKUs: Enterprise Standard, Enterprise Plus, Enterprise for Education, and Cloud Identity Premium

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DevicesApi;

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

    DevicesApi apiInstance = new DevicesApi(defaultClient);
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
    String customer = "customer_example"; // String | Optional. [Resource name](https://cloud.google.com/apis/design/resource_names) of the customer. If you're using this API for your own organization, use `customers/my_customer` If you're using this API to manage another organization, use `customers/{customer}`, where customer is the customer to whom the device belongs.
    GoogleAppsCloudidentityDevicesV1Device googleAppsCloudidentityDevicesV1Device = new GoogleAppsCloudidentityDevicesV1Device(); // GoogleAppsCloudidentityDevicesV1Device | 
    try {
      Operation result = apiInstance.cloudidentityDevicesCreate($xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, customer, googleAppsCloudidentityDevicesV1Device);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DevicesApi#cloudidentityDevicesCreate");
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
| **customer** | **String**| Optional. [Resource name](https://cloud.google.com/apis/design/resource_names) of the customer. If you&#39;re using this API for your own organization, use &#x60;customers/my_customer&#x60; If you&#39;re using this API to manage another organization, use &#x60;customers/{customer}&#x60;, where customer is the customer to whom the device belongs. | [optional] |
| **googleAppsCloudidentityDevicesV1Device** | [**GoogleAppsCloudidentityDevicesV1Device**](GoogleAppsCloudidentityDevicesV1Device.md)|  | [optional] |

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

<a id="cloudidentityDevicesDeviceUsersApprove"></a>
# **cloudidentityDevicesDeviceUsersApprove**
> Operation cloudidentityDevicesDeviceUsersApprove(name, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, googleAppsCloudidentityDevicesV1ApproveDeviceUserRequest)



Approves device to access user data.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DevicesApi;

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

    DevicesApi apiInstance = new DevicesApi(defaultClient);
    String name = "name_example"; // String | Required. [Resource name](https://cloud.google.com/apis/design/resource_names) of the Device in format: `devices/{device}/deviceUsers/{device_user}`, where device is the unique ID assigned to the Device, and device_user is the unique ID assigned to the User.
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
    GoogleAppsCloudidentityDevicesV1ApproveDeviceUserRequest googleAppsCloudidentityDevicesV1ApproveDeviceUserRequest = new GoogleAppsCloudidentityDevicesV1ApproveDeviceUserRequest(); // GoogleAppsCloudidentityDevicesV1ApproveDeviceUserRequest | 
    try {
      Operation result = apiInstance.cloudidentityDevicesDeviceUsersApprove(name, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, googleAppsCloudidentityDevicesV1ApproveDeviceUserRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DevicesApi#cloudidentityDevicesDeviceUsersApprove");
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
| **name** | **String**| Required. [Resource name](https://cloud.google.com/apis/design/resource_names) of the Device in format: &#x60;devices/{device}/deviceUsers/{device_user}&#x60;, where device is the unique ID assigned to the Device, and device_user is the unique ID assigned to the User. | |
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
| **googleAppsCloudidentityDevicesV1ApproveDeviceUserRequest** | [**GoogleAppsCloudidentityDevicesV1ApproveDeviceUserRequest**](GoogleAppsCloudidentityDevicesV1ApproveDeviceUserRequest.md)|  | [optional] |

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

<a id="cloudidentityDevicesDeviceUsersBlock"></a>
# **cloudidentityDevicesDeviceUsersBlock**
> Operation cloudidentityDevicesDeviceUsersBlock(name, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, googleAppsCloudidentityDevicesV1BlockDeviceUserRequest)



Blocks device from accessing user data

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DevicesApi;

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

    DevicesApi apiInstance = new DevicesApi(defaultClient);
    String name = "name_example"; // String | Required. [Resource name](https://cloud.google.com/apis/design/resource_names) of the Device in format: `devices/{device}/deviceUsers/{device_user}`, where device is the unique ID assigned to the Device, and device_user is the unique ID assigned to the User.
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
    GoogleAppsCloudidentityDevicesV1BlockDeviceUserRequest googleAppsCloudidentityDevicesV1BlockDeviceUserRequest = new GoogleAppsCloudidentityDevicesV1BlockDeviceUserRequest(); // GoogleAppsCloudidentityDevicesV1BlockDeviceUserRequest | 
    try {
      Operation result = apiInstance.cloudidentityDevicesDeviceUsersBlock(name, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, googleAppsCloudidentityDevicesV1BlockDeviceUserRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DevicesApi#cloudidentityDevicesDeviceUsersBlock");
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
| **name** | **String**| Required. [Resource name](https://cloud.google.com/apis/design/resource_names) of the Device in format: &#x60;devices/{device}/deviceUsers/{device_user}&#x60;, where device is the unique ID assigned to the Device, and device_user is the unique ID assigned to the User. | |
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
| **googleAppsCloudidentityDevicesV1BlockDeviceUserRequest** | [**GoogleAppsCloudidentityDevicesV1BlockDeviceUserRequest**](GoogleAppsCloudidentityDevicesV1BlockDeviceUserRequest.md)|  | [optional] |

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

<a id="cloudidentityDevicesDeviceUsersCancelWipe"></a>
# **cloudidentityDevicesDeviceUsersCancelWipe**
> Operation cloudidentityDevicesDeviceUsersCancelWipe(name, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, googleAppsCloudidentityDevicesV1CancelWipeDeviceUserRequest)



Cancels an unfinished user account wipe. This operation can be used to cancel device wipe in the gap between the wipe operation returning success and the device being wiped.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DevicesApi;

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

    DevicesApi apiInstance = new DevicesApi(defaultClient);
    String name = "name_example"; // String | Required. [Resource name](https://cloud.google.com/apis/design/resource_names) of the Device in format: `devices/{device}/deviceUsers/{device_user}`, where device is the unique ID assigned to the Device, and device_user is the unique ID assigned to the User.
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
    GoogleAppsCloudidentityDevicesV1CancelWipeDeviceUserRequest googleAppsCloudidentityDevicesV1CancelWipeDeviceUserRequest = new GoogleAppsCloudidentityDevicesV1CancelWipeDeviceUserRequest(); // GoogleAppsCloudidentityDevicesV1CancelWipeDeviceUserRequest | 
    try {
      Operation result = apiInstance.cloudidentityDevicesDeviceUsersCancelWipe(name, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, googleAppsCloudidentityDevicesV1CancelWipeDeviceUserRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DevicesApi#cloudidentityDevicesDeviceUsersCancelWipe");
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
| **name** | **String**| Required. [Resource name](https://cloud.google.com/apis/design/resource_names) of the Device in format: &#x60;devices/{device}/deviceUsers/{device_user}&#x60;, where device is the unique ID assigned to the Device, and device_user is the unique ID assigned to the User. | |
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
| **googleAppsCloudidentityDevicesV1CancelWipeDeviceUserRequest** | [**GoogleAppsCloudidentityDevicesV1CancelWipeDeviceUserRequest**](GoogleAppsCloudidentityDevicesV1CancelWipeDeviceUserRequest.md)|  | [optional] |

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

<a id="cloudidentityDevicesDeviceUsersClientStatesList"></a>
# **cloudidentityDevicesDeviceUsersClientStatesList**
> GoogleAppsCloudidentityDevicesV1ListClientStatesResponse cloudidentityDevicesDeviceUsersClientStatesList(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, customer, filter, orderBy, pageToken)



Lists the client states for the given search query.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DevicesApi;

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

    DevicesApi apiInstance = new DevicesApi(defaultClient);
    String parent = "parent_example"; // String | Required. To list all ClientStates, set this to \"devices/-/deviceUsers/-\". To list all ClientStates owned by a DeviceUser, set this to the resource name of the DeviceUser. Format: devices/{device}/deviceUsers/{deviceUser}
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
    String customer = "customer_example"; // String | Optional. [Resource name](https://cloud.google.com/apis/design/resource_names) of the customer. If you're using this API for your own organization, use `customers/my_customer` If you're using this API to manage another organization, use `customers/{customer}`, where customer is the customer to whom the device belongs.
    String filter = "filter_example"; // String | Optional. Additional restrictions when fetching list of client states.
    String orderBy = "orderBy_example"; // String | Optional. Order specification for client states in the response.
    String pageToken = "pageToken_example"; // String | Optional. A page token, received from a previous `ListClientStates` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListClientStates` must match the call that provided the page token.
    try {
      GoogleAppsCloudidentityDevicesV1ListClientStatesResponse result = apiInstance.cloudidentityDevicesDeviceUsersClientStatesList(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, customer, filter, orderBy, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DevicesApi#cloudidentityDevicesDeviceUsersClientStatesList");
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
| **parent** | **String**| Required. To list all ClientStates, set this to \&quot;devices/-/deviceUsers/-\&quot;. To list all ClientStates owned by a DeviceUser, set this to the resource name of the DeviceUser. Format: devices/{device}/deviceUsers/{deviceUser} | |
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
| **customer** | **String**| Optional. [Resource name](https://cloud.google.com/apis/design/resource_names) of the customer. If you&#39;re using this API for your own organization, use &#x60;customers/my_customer&#x60; If you&#39;re using this API to manage another organization, use &#x60;customers/{customer}&#x60;, where customer is the customer to whom the device belongs. | [optional] |
| **filter** | **String**| Optional. Additional restrictions when fetching list of client states. | [optional] |
| **orderBy** | **String**| Optional. Order specification for client states in the response. | [optional] |
| **pageToken** | **String**| Optional. A page token, received from a previous &#x60;ListClientStates&#x60; call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to &#x60;ListClientStates&#x60; must match the call that provided the page token. | [optional] |

### Return type

[**GoogleAppsCloudidentityDevicesV1ListClientStatesResponse**](GoogleAppsCloudidentityDevicesV1ListClientStatesResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="cloudidentityDevicesDeviceUsersList"></a>
# **cloudidentityDevicesDeviceUsersList**
> GoogleAppsCloudidentityDevicesV1ListDeviceUsersResponse cloudidentityDevicesDeviceUsersList(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, customer, filter, orderBy, pageSize, pageToken)



Lists/Searches DeviceUsers.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DevicesApi;

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

    DevicesApi apiInstance = new DevicesApi(defaultClient);
    String parent = "parent_example"; // String | Required. To list all DeviceUsers, set this to \"devices/-\". To list all DeviceUsers owned by a device, set this to the resource name of the device. Format: devices/{device}
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
    String customer = "customer_example"; // String | Optional. [Resource name](https://cloud.google.com/apis/design/resource_names) of the customer. If you're using this API for your own organization, use `customers/my_customer` If you're using this API to manage another organization, use `customers/{customer}`, where customer is the customer to whom the device belongs.
    String filter = "filter_example"; // String | Optional. Additional restrictions when fetching list of devices. For a list of search fields, refer to [Mobile device search fields](https://developers.google.com/admin-sdk/directory/v1/search-operators). Multiple search fields are separated by the space character.
    String orderBy = "orderBy_example"; // String | Optional. Order specification for devices in the response.
    Integer pageSize = 56; // Integer | Optional. The maximum number of DeviceUsers to return. If unspecified, at most 5 DeviceUsers will be returned. The maximum value is 20; values above 20 will be coerced to 20.
    String pageToken = "pageToken_example"; // String | Optional. A page token, received from a previous `ListDeviceUsers` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListBooks` must match the call that provided the page token.
    try {
      GoogleAppsCloudidentityDevicesV1ListDeviceUsersResponse result = apiInstance.cloudidentityDevicesDeviceUsersList(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, customer, filter, orderBy, pageSize, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DevicesApi#cloudidentityDevicesDeviceUsersList");
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
| **parent** | **String**| Required. To list all DeviceUsers, set this to \&quot;devices/-\&quot;. To list all DeviceUsers owned by a device, set this to the resource name of the device. Format: devices/{device} | |
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
| **customer** | **String**| Optional. [Resource name](https://cloud.google.com/apis/design/resource_names) of the customer. If you&#39;re using this API for your own organization, use &#x60;customers/my_customer&#x60; If you&#39;re using this API to manage another organization, use &#x60;customers/{customer}&#x60;, where customer is the customer to whom the device belongs. | [optional] |
| **filter** | **String**| Optional. Additional restrictions when fetching list of devices. For a list of search fields, refer to [Mobile device search fields](https://developers.google.com/admin-sdk/directory/v1/search-operators). Multiple search fields are separated by the space character. | [optional] |
| **orderBy** | **String**| Optional. Order specification for devices in the response. | [optional] |
| **pageSize** | **Integer**| Optional. The maximum number of DeviceUsers to return. If unspecified, at most 5 DeviceUsers will be returned. The maximum value is 20; values above 20 will be coerced to 20. | [optional] |
| **pageToken** | **String**| Optional. A page token, received from a previous &#x60;ListDeviceUsers&#x60; call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to &#x60;ListBooks&#x60; must match the call that provided the page token. | [optional] |

### Return type

[**GoogleAppsCloudidentityDevicesV1ListDeviceUsersResponse**](GoogleAppsCloudidentityDevicesV1ListDeviceUsersResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="cloudidentityDevicesDeviceUsersLookup"></a>
# **cloudidentityDevicesDeviceUsersLookup**
> GoogleAppsCloudidentityDevicesV1LookupSelfDeviceUsersResponse cloudidentityDevicesDeviceUsersLookup(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, androidId, pageSize, pageToken, rawResourceId, userId)



Looks up resource names of the DeviceUsers associated with the caller&#39;s credentials, as well as the properties provided in the request. This method must be called with end-user credentials with the scope: https://www.googleapis.com/auth/cloud-identity.devices.lookup If multiple properties are provided, only DeviceUsers having all of these properties are considered as matches - i.e. the query behaves like an AND. Different platforms require different amounts of information from the caller to ensure that the DeviceUser is uniquely identified. - iOS: No properties need to be passed, the caller&#39;s credentials are sufficient to identify the corresponding DeviceUser. - Android: Specifying the &#39;android_id&#39; field is required. - Desktop: Specifying the &#39;raw_resource_id&#39; field is required.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DevicesApi;

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

    DevicesApi apiInstance = new DevicesApi(defaultClient);
    String parent = "parent_example"; // String | Must be set to \"devices/-/deviceUsers\" to search across all DeviceUser belonging to the user.
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
    String androidId = "androidId_example"; // String | Android Id returned by [Settings.Secure#ANDROID_ID](https://developer.android.com/reference/android/provider/Settings.Secure.html#ANDROID_ID).
    Integer pageSize = 56; // Integer | The maximum number of DeviceUsers to return. If unspecified, at most 20 DeviceUsers will be returned. The maximum value is 20; values above 20 will be coerced to 20.
    String pageToken = "pageToken_example"; // String | A page token, received from a previous `LookupDeviceUsers` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `LookupDeviceUsers` must match the call that provided the page token.
    String rawResourceId = "rawResourceId_example"; // String | Raw Resource Id used by Google Endpoint Verification. If the user is enrolled into Google Endpoint Verification, this id will be saved as the 'device_resource_id' field in the following platform dependent files. * macOS: ~/.secureConnect/context_aware_config.json * Windows: %USERPROFILE%\\AppData\\Local\\Google\\Endpoint Verification\\accounts.json * Linux: ~/.secureConnect/context_aware_config.json
    String userId = "userId_example"; // String | The user whose DeviceUser's resource name will be fetched. Must be set to 'me' to fetch the DeviceUser's resource name for the calling user.
    try {
      GoogleAppsCloudidentityDevicesV1LookupSelfDeviceUsersResponse result = apiInstance.cloudidentityDevicesDeviceUsersLookup(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, androidId, pageSize, pageToken, rawResourceId, userId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DevicesApi#cloudidentityDevicesDeviceUsersLookup");
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
| **parent** | **String**| Must be set to \&quot;devices/-/deviceUsers\&quot; to search across all DeviceUser belonging to the user. | |
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
| **androidId** | **String**| Android Id returned by [Settings.Secure#ANDROID_ID](https://developer.android.com/reference/android/provider/Settings.Secure.html#ANDROID_ID). | [optional] |
| **pageSize** | **Integer**| The maximum number of DeviceUsers to return. If unspecified, at most 20 DeviceUsers will be returned. The maximum value is 20; values above 20 will be coerced to 20. | [optional] |
| **pageToken** | **String**| A page token, received from a previous &#x60;LookupDeviceUsers&#x60; call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to &#x60;LookupDeviceUsers&#x60; must match the call that provided the page token. | [optional] |
| **rawResourceId** | **String**| Raw Resource Id used by Google Endpoint Verification. If the user is enrolled into Google Endpoint Verification, this id will be saved as the &#39;device_resource_id&#39; field in the following platform dependent files. * macOS: ~/.secureConnect/context_aware_config.json * Windows: %USERPROFILE%\\AppData\\Local\\Google\\Endpoint Verification\\accounts.json * Linux: ~/.secureConnect/context_aware_config.json | [optional] |
| **userId** | **String**| The user whose DeviceUser&#39;s resource name will be fetched. Must be set to &#39;me&#39; to fetch the DeviceUser&#39;s resource name for the calling user. | [optional] |

### Return type

[**GoogleAppsCloudidentityDevicesV1LookupSelfDeviceUsersResponse**](GoogleAppsCloudidentityDevicesV1LookupSelfDeviceUsersResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="cloudidentityDevicesDeviceUsersWipe"></a>
# **cloudidentityDevicesDeviceUsersWipe**
> Operation cloudidentityDevicesDeviceUsersWipe(name, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, googleAppsCloudidentityDevicesV1WipeDeviceUserRequest)



Wipes the user&#39;s account on a device. Other data on the device that is not associated with the user&#39;s work account is not affected. For example, if a Gmail app is installed on a device that is used for personal and work purposes, and the user is logged in to the Gmail app with their personal account as well as their work account, wiping the \&quot;deviceUser\&quot; by their work administrator will not affect their personal account within Gmail or other apps such as Photos.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DevicesApi;

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

    DevicesApi apiInstance = new DevicesApi(defaultClient);
    String name = "name_example"; // String | Required. [Resource name](https://cloud.google.com/apis/design/resource_names) of the Device in format: `devices/{device}/deviceUsers/{device_user}`, where device is the unique ID assigned to the Device, and device_user is the unique ID assigned to the User.
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
    GoogleAppsCloudidentityDevicesV1WipeDeviceUserRequest googleAppsCloudidentityDevicesV1WipeDeviceUserRequest = new GoogleAppsCloudidentityDevicesV1WipeDeviceUserRequest(); // GoogleAppsCloudidentityDevicesV1WipeDeviceUserRequest | 
    try {
      Operation result = apiInstance.cloudidentityDevicesDeviceUsersWipe(name, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, googleAppsCloudidentityDevicesV1WipeDeviceUserRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DevicesApi#cloudidentityDevicesDeviceUsersWipe");
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
| **name** | **String**| Required. [Resource name](https://cloud.google.com/apis/design/resource_names) of the Device in format: &#x60;devices/{device}/deviceUsers/{device_user}&#x60;, where device is the unique ID assigned to the Device, and device_user is the unique ID assigned to the User. | |
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
| **googleAppsCloudidentityDevicesV1WipeDeviceUserRequest** | [**GoogleAppsCloudidentityDevicesV1WipeDeviceUserRequest**](GoogleAppsCloudidentityDevicesV1WipeDeviceUserRequest.md)|  | [optional] |

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

<a id="cloudidentityDevicesList"></a>
# **cloudidentityDevicesList**
> GoogleAppsCloudidentityDevicesV1ListDevicesResponse cloudidentityDevicesList($xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, customer, filter, orderBy, pageSize, pageToken, view)



Lists/Searches devices.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DevicesApi;

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

    DevicesApi apiInstance = new DevicesApi(defaultClient);
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
    String customer = "customer_example"; // String | Optional. [Resource name](https://cloud.google.com/apis/design/resource_names) of the customer in the format: `customers/{customer}`, where customer is the customer to whom the device belongs. If you're using this API for your own organization, use `customers/my_customer`. If you're using this API to manage another organization, use `customers/{customer}`, where customer is the customer to whom the device belongs.
    String filter = "filter_example"; // String | Optional. Additional restrictions when fetching list of devices. For a list of search fields, refer to [Mobile device search fields](https://developers.google.com/admin-sdk/directory/v1/search-operators). Multiple search fields are separated by the space character.
    String orderBy = "orderBy_example"; // String | Optional. Order specification for devices in the response. Only one of the following field names may be used to specify the order: `create_time`, `last_sync_time`, `model`, `os_version`, `device_type` and `serial_number`. `desc` may be specified optionally at the end to specify results to be sorted in descending order. Default order is ascending.
    Integer pageSize = 56; // Integer | Optional. The maximum number of Devices to return. If unspecified, at most 20 Devices will be returned. The maximum value is 100; values above 100 will be coerced to 100.
    String pageToken = "pageToken_example"; // String | Optional. A page token, received from a previous `ListDevices` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListDevices` must match the call that provided the page token.
    String view = "VIEW_UNSPECIFIED"; // String | Optional. The view to use for the List request.
    try {
      GoogleAppsCloudidentityDevicesV1ListDevicesResponse result = apiInstance.cloudidentityDevicesList($xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, customer, filter, orderBy, pageSize, pageToken, view);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DevicesApi#cloudidentityDevicesList");
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
| **customer** | **String**| Optional. [Resource name](https://cloud.google.com/apis/design/resource_names) of the customer in the format: &#x60;customers/{customer}&#x60;, where customer is the customer to whom the device belongs. If you&#39;re using this API for your own organization, use &#x60;customers/my_customer&#x60;. If you&#39;re using this API to manage another organization, use &#x60;customers/{customer}&#x60;, where customer is the customer to whom the device belongs. | [optional] |
| **filter** | **String**| Optional. Additional restrictions when fetching list of devices. For a list of search fields, refer to [Mobile device search fields](https://developers.google.com/admin-sdk/directory/v1/search-operators). Multiple search fields are separated by the space character. | [optional] |
| **orderBy** | **String**| Optional. Order specification for devices in the response. Only one of the following field names may be used to specify the order: &#x60;create_time&#x60;, &#x60;last_sync_time&#x60;, &#x60;model&#x60;, &#x60;os_version&#x60;, &#x60;device_type&#x60; and &#x60;serial_number&#x60;. &#x60;desc&#x60; may be specified optionally at the end to specify results to be sorted in descending order. Default order is ascending. | [optional] |
| **pageSize** | **Integer**| Optional. The maximum number of Devices to return. If unspecified, at most 20 Devices will be returned. The maximum value is 100; values above 100 will be coerced to 100. | [optional] |
| **pageToken** | **String**| Optional. A page token, received from a previous &#x60;ListDevices&#x60; call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to &#x60;ListDevices&#x60; must match the call that provided the page token. | [optional] |
| **view** | **String**| Optional. The view to use for the List request. | [optional] [enum: VIEW_UNSPECIFIED, COMPANY_INVENTORY, USER_ASSIGNED_DEVICES] |

### Return type

[**GoogleAppsCloudidentityDevicesV1ListDevicesResponse**](GoogleAppsCloudidentityDevicesV1ListDevicesResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

