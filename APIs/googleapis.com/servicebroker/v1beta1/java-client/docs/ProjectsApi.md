# ProjectsApi

All URIs are relative to *https://servicebroker.googleapis.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**servicebrokerProjectsBrokersCreate**](ProjectsApi.md#servicebrokerProjectsBrokersCreate) | **POST** /v1beta1/{parent}/brokers |  |
| [**servicebrokerProjectsBrokersInstancesBindingsList**](ProjectsApi.md#servicebrokerProjectsBrokersInstancesBindingsList) | **GET** /v1beta1/{parent}/bindings |  |
| [**servicebrokerProjectsBrokersInstancesList**](ProjectsApi.md#servicebrokerProjectsBrokersInstancesList) | **GET** /v1beta1/{parent}/instances |  |
| [**servicebrokerProjectsBrokersList**](ProjectsApi.md#servicebrokerProjectsBrokersList) | **GET** /v1beta1/{parent}/brokers |  |
| [**servicebrokerProjectsBrokersV2CatalogList**](ProjectsApi.md#servicebrokerProjectsBrokersV2CatalogList) | **GET** /v1beta1/{parent}/v2/catalog |  |
| [**servicebrokerProjectsBrokersV2ServiceInstancesCreate**](ProjectsApi.md#servicebrokerProjectsBrokersV2ServiceInstancesCreate) | **PUT** /v1beta1/{parent}/v2/service_instances/{instance_id} |  |
| [**servicebrokerProjectsBrokersV2ServiceInstancesPatch**](ProjectsApi.md#servicebrokerProjectsBrokersV2ServiceInstancesPatch) | **PATCH** /v1beta1/{name} |  |
| [**servicebrokerProjectsBrokersV2ServiceInstancesServiceBindingsCreate**](ProjectsApi.md#servicebrokerProjectsBrokersV2ServiceInstancesServiceBindingsCreate) | **PUT** /v1beta1/{parent}/service_bindings/{binding_id} |  |
| [**servicebrokerProjectsBrokersV2ServiceInstancesServiceBindingsDelete**](ProjectsApi.md#servicebrokerProjectsBrokersV2ServiceInstancesServiceBindingsDelete) | **DELETE** /v1beta1/{name} |  |
| [**servicebrokerProjectsBrokersV2ServiceInstancesServiceBindingsGet**](ProjectsApi.md#servicebrokerProjectsBrokersV2ServiceInstancesServiceBindingsGet) | **GET** /v1beta1/{name} |  |
| [**servicebrokerProjectsBrokersV2ServiceInstancesServiceBindingsGetLastOperation**](ProjectsApi.md#servicebrokerProjectsBrokersV2ServiceInstancesServiceBindingsGetLastOperation) | **GET** /v1beta1/{name}/last_operation |  |


<a id="servicebrokerProjectsBrokersCreate"></a>
# **servicebrokerProjectsBrokersCreate**
> GoogleCloudServicebrokerV1beta1Broker servicebrokerProjectsBrokersCreate(parent, fields, uploadType, paramCallback, oauthToken, $xgafv, alt, accessToken, key, uploadProtocol, quotaUser, prettyPrint, googleCloudServicebrokerV1beta1Broker)



CreateBroker creates a Broker.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

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

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String parent = "parent_example"; // String | The project in which to create broker.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    String paramCallback = "paramCallback_example"; // String | JSONP
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    String $xgafv = "1"; // String | V1 error format.
    String alt = "json"; // String | Data format for response.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    GoogleCloudServicebrokerV1beta1Broker googleCloudServicebrokerV1beta1Broker = new GoogleCloudServicebrokerV1beta1Broker(); // GoogleCloudServicebrokerV1beta1Broker | 
    try {
      GoogleCloudServicebrokerV1beta1Broker result = apiInstance.servicebrokerProjectsBrokersCreate(parent, fields, uploadType, paramCallback, oauthToken, $xgafv, alt, accessToken, key, uploadProtocol, quotaUser, prettyPrint, googleCloudServicebrokerV1beta1Broker);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#servicebrokerProjectsBrokersCreate");
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
| **parent** | **String**| The project in which to create broker. | |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |
| **paramCallback** | **String**| JSONP | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **alt** | **String**| Data format for response. | [optional] [default to json] [enum: json, media, proto] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true] |
| **googleCloudServicebrokerV1beta1Broker** | [**GoogleCloudServicebrokerV1beta1Broker**](GoogleCloudServicebrokerV1beta1Broker.md)|  | [optional] |

### Return type

[**GoogleCloudServicebrokerV1beta1Broker**](GoogleCloudServicebrokerV1beta1Broker.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="servicebrokerProjectsBrokersInstancesBindingsList"></a>
# **servicebrokerProjectsBrokersInstancesBindingsList**
> GoogleCloudServicebrokerV1beta1ListBindingsResponse servicebrokerProjectsBrokersInstancesBindingsList(parent, fields, uploadType, paramCallback, oauthToken, $xgafv, alt, accessToken, key, uploadProtocol, quotaUser, prettyPrint, pageSize, pageToken)



Lists all the bindings in the instance.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

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

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String parent = "parent_example"; // String | Parent must match `projects/[PROJECT_ID]/brokers/[BROKER_ID]/` + `v2/service_instances/[INSTANCE_ID]` or `projects/[PROJECT_ID]/brokers/[BROKER_ID]/instances/[INSTANCE_ID]`.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    String paramCallback = "paramCallback_example"; // String | JSONP
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    String $xgafv = "1"; // String | V1 error format.
    String alt = "json"; // String | Data format for response.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    Integer pageSize = 56; // Integer | Specifies the number of results to return per page. If there are fewer elements than the specified number, returns all elements. Optional. Acceptable values are 0 to 200, inclusive. (Default: 100)
    String pageToken = "pageToken_example"; // String | Specifies a page token to use. Set `pageToken` to a `nextPageToken` returned by a previous list request to get the next page of results.
    try {
      GoogleCloudServicebrokerV1beta1ListBindingsResponse result = apiInstance.servicebrokerProjectsBrokersInstancesBindingsList(parent, fields, uploadType, paramCallback, oauthToken, $xgafv, alt, accessToken, key, uploadProtocol, quotaUser, prettyPrint, pageSize, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#servicebrokerProjectsBrokersInstancesBindingsList");
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
| **parent** | **String**| Parent must match &#x60;projects/[PROJECT_ID]/brokers/[BROKER_ID]/&#x60; + &#x60;v2/service_instances/[INSTANCE_ID]&#x60; or &#x60;projects/[PROJECT_ID]/brokers/[BROKER_ID]/instances/[INSTANCE_ID]&#x60;. | |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |
| **paramCallback** | **String**| JSONP | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **alt** | **String**| Data format for response. | [optional] [default to json] [enum: json, media, proto] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true] |
| **pageSize** | **Integer**| Specifies the number of results to return per page. If there are fewer elements than the specified number, returns all elements. Optional. Acceptable values are 0 to 200, inclusive. (Default: 100) | [optional] |
| **pageToken** | **String**| Specifies a page token to use. Set &#x60;pageToken&#x60; to a &#x60;nextPageToken&#x60; returned by a previous list request to get the next page of results. | [optional] |

### Return type

[**GoogleCloudServicebrokerV1beta1ListBindingsResponse**](GoogleCloudServicebrokerV1beta1ListBindingsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="servicebrokerProjectsBrokersInstancesList"></a>
# **servicebrokerProjectsBrokersInstancesList**
> GoogleCloudServicebrokerV1beta1ListServiceInstancesResponse servicebrokerProjectsBrokersInstancesList(parent, fields, uploadType, paramCallback, oauthToken, $xgafv, alt, accessToken, key, uploadProtocol, quotaUser, prettyPrint, pageSize, pageToken)



Lists all the instances in the brokers This API is an extension and not part of the OSB spec. Hence the path is a standard Google API URL.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

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

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String parent = "parent_example"; // String | Parent must match `projects/[PROJECT_ID]/brokers/[BROKER_ID]`.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    String paramCallback = "paramCallback_example"; // String | JSONP
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    String $xgafv = "1"; // String | V1 error format.
    String alt = "json"; // String | Data format for response.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    Integer pageSize = 56; // Integer | Specifies the number of results to return per page. If there are fewer elements than the specified number, returns all elements. Optional. Acceptable values are 0 to 200, inclusive. (Default: 100)
    String pageToken = "pageToken_example"; // String | Specifies a page token to use. Set `pageToken` to a `nextPageToken` returned by a previous list request to get the next page of results.
    try {
      GoogleCloudServicebrokerV1beta1ListServiceInstancesResponse result = apiInstance.servicebrokerProjectsBrokersInstancesList(parent, fields, uploadType, paramCallback, oauthToken, $xgafv, alt, accessToken, key, uploadProtocol, quotaUser, prettyPrint, pageSize, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#servicebrokerProjectsBrokersInstancesList");
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
| **parent** | **String**| Parent must match &#x60;projects/[PROJECT_ID]/brokers/[BROKER_ID]&#x60;. | |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |
| **paramCallback** | **String**| JSONP | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **alt** | **String**| Data format for response. | [optional] [default to json] [enum: json, media, proto] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true] |
| **pageSize** | **Integer**| Specifies the number of results to return per page. If there are fewer elements than the specified number, returns all elements. Optional. Acceptable values are 0 to 200, inclusive. (Default: 100) | [optional] |
| **pageToken** | **String**| Specifies a page token to use. Set &#x60;pageToken&#x60; to a &#x60;nextPageToken&#x60; returned by a previous list request to get the next page of results. | [optional] |

### Return type

[**GoogleCloudServicebrokerV1beta1ListServiceInstancesResponse**](GoogleCloudServicebrokerV1beta1ListServiceInstancesResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="servicebrokerProjectsBrokersList"></a>
# **servicebrokerProjectsBrokersList**
> GoogleCloudServicebrokerV1beta1ListBrokersResponse servicebrokerProjectsBrokersList(parent, fields, uploadType, paramCallback, oauthToken, $xgafv, alt, accessToken, key, uploadProtocol, quotaUser, prettyPrint, pageSize, pageToken)



ListBrokers lists brokers.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

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

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String parent = "parent_example"; // String | Parent must match `projects/[PROJECT_ID]/brokers`.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    String paramCallback = "paramCallback_example"; // String | JSONP
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    String $xgafv = "1"; // String | V1 error format.
    String alt = "json"; // String | Data format for response.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    Integer pageSize = 56; // Integer | Specifies the number of results to return per page. If there are fewer elements than the specified number, returns all elements. Optional. Acceptable values are 0 to 200, inclusive. (Default: 100)
    String pageToken = "pageToken_example"; // String | Specifies a page token to use. Set `pageToken` to a `nextPageToken` returned by a previous list request to get the next page of results.
    try {
      GoogleCloudServicebrokerV1beta1ListBrokersResponse result = apiInstance.servicebrokerProjectsBrokersList(parent, fields, uploadType, paramCallback, oauthToken, $xgafv, alt, accessToken, key, uploadProtocol, quotaUser, prettyPrint, pageSize, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#servicebrokerProjectsBrokersList");
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
| **parent** | **String**| Parent must match &#x60;projects/[PROJECT_ID]/brokers&#x60;. | |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |
| **paramCallback** | **String**| JSONP | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **alt** | **String**| Data format for response. | [optional] [default to json] [enum: json, media, proto] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true] |
| **pageSize** | **Integer**| Specifies the number of results to return per page. If there are fewer elements than the specified number, returns all elements. Optional. Acceptable values are 0 to 200, inclusive. (Default: 100) | [optional] |
| **pageToken** | **String**| Specifies a page token to use. Set &#x60;pageToken&#x60; to a &#x60;nextPageToken&#x60; returned by a previous list request to get the next page of results. | [optional] |

### Return type

[**GoogleCloudServicebrokerV1beta1ListBrokersResponse**](GoogleCloudServicebrokerV1beta1ListBrokersResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="servicebrokerProjectsBrokersV2CatalogList"></a>
# **servicebrokerProjectsBrokersV2CatalogList**
> GoogleCloudServicebrokerV1beta1ListCatalogResponse servicebrokerProjectsBrokersV2CatalogList(parent, fields, uploadType, paramCallback, oauthToken, $xgafv, alt, accessToken, key, uploadProtocol, quotaUser, prettyPrint, pageSize, pageToken)



Lists all the Services registered with this broker for consumption for given service registry broker, which contains an set of services. Note, that Service producer API is separate from Broker API.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

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

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String parent = "parent_example"; // String | Parent must match `projects/[PROJECT_ID]/brokers/[BROKER_ID]`.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    String paramCallback = "paramCallback_example"; // String | JSONP
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    String $xgafv = "1"; // String | V1 error format.
    String alt = "json"; // String | Data format for response.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    Integer pageSize = 56; // Integer | Specifies the number of results to return per page. If there are fewer elements than the specified number, returns all elements. Optional. If unset or 0, all the results will be returned.
    String pageToken = "pageToken_example"; // String | Specifies a page token to use. Set `pageToken` to a `nextPageToken` returned by a previous list request to get the next page of results.
    try {
      GoogleCloudServicebrokerV1beta1ListCatalogResponse result = apiInstance.servicebrokerProjectsBrokersV2CatalogList(parent, fields, uploadType, paramCallback, oauthToken, $xgafv, alt, accessToken, key, uploadProtocol, quotaUser, prettyPrint, pageSize, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#servicebrokerProjectsBrokersV2CatalogList");
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
| **parent** | **String**| Parent must match &#x60;projects/[PROJECT_ID]/brokers/[BROKER_ID]&#x60;. | |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |
| **paramCallback** | **String**| JSONP | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **alt** | **String**| Data format for response. | [optional] [default to json] [enum: json, media, proto] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true] |
| **pageSize** | **Integer**| Specifies the number of results to return per page. If there are fewer elements than the specified number, returns all elements. Optional. If unset or 0, all the results will be returned. | [optional] |
| **pageToken** | **String**| Specifies a page token to use. Set &#x60;pageToken&#x60; to a &#x60;nextPageToken&#x60; returned by a previous list request to get the next page of results. | [optional] |

### Return type

[**GoogleCloudServicebrokerV1beta1ListCatalogResponse**](GoogleCloudServicebrokerV1beta1ListCatalogResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="servicebrokerProjectsBrokersV2ServiceInstancesCreate"></a>
# **servicebrokerProjectsBrokersV2ServiceInstancesCreate**
> GoogleCloudServicebrokerV1beta1CreateServiceInstanceResponse servicebrokerProjectsBrokersV2ServiceInstancesCreate(parent, instanceId, fields, uploadType, paramCallback, oauthToken, $xgafv, alt, accessToken, key, uploadProtocol, quotaUser, prettyPrint, acceptsIncomplete, googleCloudServicebrokerV1beta1ServiceInstance)



Provisions a service instance. If &#x60;request.accepts_incomplete&#x60; is false and Broker cannot execute request synchronously HTTP 422 error will be returned along with FAILED_PRECONDITION status. If &#x60;request.accepts_incomplete&#x60; is true and the Broker decides to execute resource asynchronously then HTTP 202 response code will be returned and a valid polling operation in the response will be included. If Broker executes the request synchronously and it succeeds HTTP 201 response will be furnished. If identical instance exists, then HTTP 200 response will be returned. If an instance with identical ID but mismatching parameters exists, then HTTP 409 status code will be returned.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

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

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String parent = "parent_example"; // String | Parent must match `projects/[PROJECT_ID]/brokers/[BROKER_ID]`.
    String instanceId = "instanceId_example"; // String | The id of the service instance. Must be unique within GCP project. Maximum length is 64, GUID recommended. Required.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    String paramCallback = "paramCallback_example"; // String | JSONP
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    String $xgafv = "1"; // String | V1 error format.
    String alt = "json"; // String | Data format for response.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    Boolean acceptsIncomplete = true; // Boolean | Value indicating that API client supports asynchronous operations. If Broker cannot execute the request synchronously HTTP 422 code will be returned to HTTP clients along with FAILED_PRECONDITION error. If true and broker will execute request asynchronously 202 HTTP code will be returned. This broker always requires this to be true as all mutator operations are asynchronous.
    GoogleCloudServicebrokerV1beta1ServiceInstance googleCloudServicebrokerV1beta1ServiceInstance = new GoogleCloudServicebrokerV1beta1ServiceInstance(); // GoogleCloudServicebrokerV1beta1ServiceInstance | 
    try {
      GoogleCloudServicebrokerV1beta1CreateServiceInstanceResponse result = apiInstance.servicebrokerProjectsBrokersV2ServiceInstancesCreate(parent, instanceId, fields, uploadType, paramCallback, oauthToken, $xgafv, alt, accessToken, key, uploadProtocol, quotaUser, prettyPrint, acceptsIncomplete, googleCloudServicebrokerV1beta1ServiceInstance);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#servicebrokerProjectsBrokersV2ServiceInstancesCreate");
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
| **parent** | **String**| Parent must match &#x60;projects/[PROJECT_ID]/brokers/[BROKER_ID]&#x60;. | |
| **instanceId** | **String**| The id of the service instance. Must be unique within GCP project. Maximum length is 64, GUID recommended. Required. | |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |
| **paramCallback** | **String**| JSONP | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **alt** | **String**| Data format for response. | [optional] [default to json] [enum: json, media, proto] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true] |
| **acceptsIncomplete** | **Boolean**| Value indicating that API client supports asynchronous operations. If Broker cannot execute the request synchronously HTTP 422 code will be returned to HTTP clients along with FAILED_PRECONDITION error. If true and broker will execute request asynchronously 202 HTTP code will be returned. This broker always requires this to be true as all mutator operations are asynchronous. | [optional] |
| **googleCloudServicebrokerV1beta1ServiceInstance** | [**GoogleCloudServicebrokerV1beta1ServiceInstance**](GoogleCloudServicebrokerV1beta1ServiceInstance.md)|  | [optional] |

### Return type

[**GoogleCloudServicebrokerV1beta1CreateServiceInstanceResponse**](GoogleCloudServicebrokerV1beta1CreateServiceInstanceResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="servicebrokerProjectsBrokersV2ServiceInstancesPatch"></a>
# **servicebrokerProjectsBrokersV2ServiceInstancesPatch**
> GoogleCloudServicebrokerV1beta1UpdateServiceInstanceResponse servicebrokerProjectsBrokersV2ServiceInstancesPatch(name, fields, uploadType, paramCallback, oauthToken, $xgafv, alt, accessToken, key, uploadProtocol, quotaUser, prettyPrint, acceptsIncomplete, googleCloudServicebrokerV1beta1ServiceInstance)



Updates an existing service instance. See CreateServiceInstance for possible response codes.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

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

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String name = "name_example"; // String | Name must match `projects/[PROJECT_ID]/brokers/[BROKER_ID]/v2/service_instances/[INSTANCE_ID]`.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    String paramCallback = "paramCallback_example"; // String | JSONP
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    String $xgafv = "1"; // String | V1 error format.
    String alt = "json"; // String | Data format for response.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    Boolean acceptsIncomplete = true; // Boolean | See CreateServiceInstanceRequest for details.
    GoogleCloudServicebrokerV1beta1ServiceInstance googleCloudServicebrokerV1beta1ServiceInstance = new GoogleCloudServicebrokerV1beta1ServiceInstance(); // GoogleCloudServicebrokerV1beta1ServiceInstance | 
    try {
      GoogleCloudServicebrokerV1beta1UpdateServiceInstanceResponse result = apiInstance.servicebrokerProjectsBrokersV2ServiceInstancesPatch(name, fields, uploadType, paramCallback, oauthToken, $xgafv, alt, accessToken, key, uploadProtocol, quotaUser, prettyPrint, acceptsIncomplete, googleCloudServicebrokerV1beta1ServiceInstance);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#servicebrokerProjectsBrokersV2ServiceInstancesPatch");
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
| **name** | **String**| Name must match &#x60;projects/[PROJECT_ID]/brokers/[BROKER_ID]/v2/service_instances/[INSTANCE_ID]&#x60;. | |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |
| **paramCallback** | **String**| JSONP | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **alt** | **String**| Data format for response. | [optional] [default to json] [enum: json, media, proto] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true] |
| **acceptsIncomplete** | **Boolean**| See CreateServiceInstanceRequest for details. | [optional] |
| **googleCloudServicebrokerV1beta1ServiceInstance** | [**GoogleCloudServicebrokerV1beta1ServiceInstance**](GoogleCloudServicebrokerV1beta1ServiceInstance.md)|  | [optional] |

### Return type

[**GoogleCloudServicebrokerV1beta1UpdateServiceInstanceResponse**](GoogleCloudServicebrokerV1beta1UpdateServiceInstanceResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="servicebrokerProjectsBrokersV2ServiceInstancesServiceBindingsCreate"></a>
# **servicebrokerProjectsBrokersV2ServiceInstancesServiceBindingsCreate**
> GoogleCloudServicebrokerV1beta1CreateBindingResponse servicebrokerProjectsBrokersV2ServiceInstancesServiceBindingsCreate(parent, bindingId, fields, uploadType, paramCallback, oauthToken, $xgafv, alt, accessToken, key, uploadProtocol, quotaUser, prettyPrint, acceptsIncomplete, googleCloudServicebrokerV1beta1Binding)



CreateBinding generates a service binding to an existing service instance. See ProviServiceInstance for async operation details.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

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

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String parent = "parent_example"; // String | The GCP container. Must match `projects/[PROJECT_ID]/brokers/[BROKER_ID]/v2/service_instances/[INSTANCE_ID]`.
    String bindingId = "bindingId_example"; // String | The id of the binding. Must be unique within GCP project. Maximum length is 64, GUID recommended. Required.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    String paramCallback = "paramCallback_example"; // String | JSONP
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    String $xgafv = "1"; // String | V1 error format.
    String alt = "json"; // String | Data format for response.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    Boolean acceptsIncomplete = true; // Boolean | See CreateServiceInstanceRequest for details.
    GoogleCloudServicebrokerV1beta1Binding googleCloudServicebrokerV1beta1Binding = new GoogleCloudServicebrokerV1beta1Binding(); // GoogleCloudServicebrokerV1beta1Binding | 
    try {
      GoogleCloudServicebrokerV1beta1CreateBindingResponse result = apiInstance.servicebrokerProjectsBrokersV2ServiceInstancesServiceBindingsCreate(parent, bindingId, fields, uploadType, paramCallback, oauthToken, $xgafv, alt, accessToken, key, uploadProtocol, quotaUser, prettyPrint, acceptsIncomplete, googleCloudServicebrokerV1beta1Binding);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#servicebrokerProjectsBrokersV2ServiceInstancesServiceBindingsCreate");
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
| **parent** | **String**| The GCP container. Must match &#x60;projects/[PROJECT_ID]/brokers/[BROKER_ID]/v2/service_instances/[INSTANCE_ID]&#x60;. | |
| **bindingId** | **String**| The id of the binding. Must be unique within GCP project. Maximum length is 64, GUID recommended. Required. | |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |
| **paramCallback** | **String**| JSONP | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **alt** | **String**| Data format for response. | [optional] [default to json] [enum: json, media, proto] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true] |
| **acceptsIncomplete** | **Boolean**| See CreateServiceInstanceRequest for details. | [optional] |
| **googleCloudServicebrokerV1beta1Binding** | [**GoogleCloudServicebrokerV1beta1Binding**](GoogleCloudServicebrokerV1beta1Binding.md)|  | [optional] |

### Return type

[**GoogleCloudServicebrokerV1beta1CreateBindingResponse**](GoogleCloudServicebrokerV1beta1CreateBindingResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="servicebrokerProjectsBrokersV2ServiceInstancesServiceBindingsDelete"></a>
# **servicebrokerProjectsBrokersV2ServiceInstancesServiceBindingsDelete**
> GoogleCloudServicebrokerV1beta1DeleteBindingResponse servicebrokerProjectsBrokersV2ServiceInstancesServiceBindingsDelete(name, fields, uploadType, paramCallback, oauthToken, $xgafv, alt, accessToken, key, uploadProtocol, quotaUser, prettyPrint, acceptsIncomplete, planId, serviceId)



Unbinds from a service instance. For synchronous/asynchronous request details see CreateServiceInstance method. If binding does not exist HTTP 410 status will be returned.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

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

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String name = "name_example"; // String | Name must match `projects/[PROJECT_ID]/brokers/[BROKER_ID]/` `v2/service_instances/[INSTANCE_ID]/service_bindings/[BINDING_ID]` or `projects/[PROJECT_ID]/brokers/[BROKER_ID]/` `/instances/[INSTANCE_ID]/bindings/[BINDING_ID]`.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    String paramCallback = "paramCallback_example"; // String | JSONP
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    String $xgafv = "1"; // String | V1 error format.
    String alt = "json"; // String | Data format for response.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    Boolean acceptsIncomplete = true; // Boolean | See CreateServiceInstanceRequest for details.
    String planId = "planId_example"; // String | The plan id of the service instance.
    String serviceId = "serviceId_example"; // String | Additional query parameter hints. The service id of the service instance.
    try {
      GoogleCloudServicebrokerV1beta1DeleteBindingResponse result = apiInstance.servicebrokerProjectsBrokersV2ServiceInstancesServiceBindingsDelete(name, fields, uploadType, paramCallback, oauthToken, $xgafv, alt, accessToken, key, uploadProtocol, quotaUser, prettyPrint, acceptsIncomplete, planId, serviceId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#servicebrokerProjectsBrokersV2ServiceInstancesServiceBindingsDelete");
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
| **name** | **String**| Name must match &#x60;projects/[PROJECT_ID]/brokers/[BROKER_ID]/&#x60; &#x60;v2/service_instances/[INSTANCE_ID]/service_bindings/[BINDING_ID]&#x60; or &#x60;projects/[PROJECT_ID]/brokers/[BROKER_ID]/&#x60; &#x60;/instances/[INSTANCE_ID]/bindings/[BINDING_ID]&#x60;. | |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |
| **paramCallback** | **String**| JSONP | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **alt** | **String**| Data format for response. | [optional] [default to json] [enum: json, media, proto] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true] |
| **acceptsIncomplete** | **Boolean**| See CreateServiceInstanceRequest for details. | [optional] |
| **planId** | **String**| The plan id of the service instance. | [optional] |
| **serviceId** | **String**| Additional query parameter hints. The service id of the service instance. | [optional] |

### Return type

[**GoogleCloudServicebrokerV1beta1DeleteBindingResponse**](GoogleCloudServicebrokerV1beta1DeleteBindingResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="servicebrokerProjectsBrokersV2ServiceInstancesServiceBindingsGet"></a>
# **servicebrokerProjectsBrokersV2ServiceInstancesServiceBindingsGet**
> GoogleCloudServicebrokerV1beta1GetBindingResponse servicebrokerProjectsBrokersV2ServiceInstancesServiceBindingsGet(name, fields, uploadType, paramCallback, oauthToken, $xgafv, alt, accessToken, key, uploadProtocol, quotaUser, prettyPrint, planId, serviceId)



GetBinding returns the binding information.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

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

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String name = "name_example"; // String | Name must match `projects/[PROJECT_ID]/brokers/[BROKER_ID]/v2/service_instances/[INSTANCE_ID]/service_bindings`.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    String paramCallback = "paramCallback_example"; // String | JSONP
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    String $xgafv = "1"; // String | V1 error format.
    String alt = "json"; // String | Data format for response.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String planId = "planId_example"; // String | Plan id.
    String serviceId = "serviceId_example"; // String | Service id.
    try {
      GoogleCloudServicebrokerV1beta1GetBindingResponse result = apiInstance.servicebrokerProjectsBrokersV2ServiceInstancesServiceBindingsGet(name, fields, uploadType, paramCallback, oauthToken, $xgafv, alt, accessToken, key, uploadProtocol, quotaUser, prettyPrint, planId, serviceId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#servicebrokerProjectsBrokersV2ServiceInstancesServiceBindingsGet");
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
| **name** | **String**| Name must match &#x60;projects/[PROJECT_ID]/brokers/[BROKER_ID]/v2/service_instances/[INSTANCE_ID]/service_bindings&#x60;. | |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |
| **paramCallback** | **String**| JSONP | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **alt** | **String**| Data format for response. | [optional] [default to json] [enum: json, media, proto] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true] |
| **planId** | **String**| Plan id. | [optional] |
| **serviceId** | **String**| Service id. | [optional] |

### Return type

[**GoogleCloudServicebrokerV1beta1GetBindingResponse**](GoogleCloudServicebrokerV1beta1GetBindingResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="servicebrokerProjectsBrokersV2ServiceInstancesServiceBindingsGetLastOperation"></a>
# **servicebrokerProjectsBrokersV2ServiceInstancesServiceBindingsGetLastOperation**
> GoogleCloudServicebrokerV1beta1Operation servicebrokerProjectsBrokersV2ServiceInstancesServiceBindingsGetLastOperation(name, fields, uploadType, paramCallback, oauthToken, $xgafv, alt, accessToken, key, uploadProtocol, quotaUser, prettyPrint, operation, planId, serviceId)



Returns the state of the last operation for the binding. Only last (or current) operation can be polled.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

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

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String name = "name_example"; // String | Name must match `projects/[PROJECT_ID]/brokers/[BROKER_ID]/v2/service_instances/[INSTANCE_ID]/service_binding/[BINDING_ID]`.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    String paramCallback = "paramCallback_example"; // String | JSONP
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    String $xgafv = "1"; // String | V1 error format.
    String alt = "json"; // String | Data format for response.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String operation = "operation_example"; // String | If `operation` was returned during mutation operation, this field must be populated with the provided value.
    String planId = "planId_example"; // String | Plan id.
    String serviceId = "serviceId_example"; // String | Service id.
    try {
      GoogleCloudServicebrokerV1beta1Operation result = apiInstance.servicebrokerProjectsBrokersV2ServiceInstancesServiceBindingsGetLastOperation(name, fields, uploadType, paramCallback, oauthToken, $xgafv, alt, accessToken, key, uploadProtocol, quotaUser, prettyPrint, operation, planId, serviceId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#servicebrokerProjectsBrokersV2ServiceInstancesServiceBindingsGetLastOperation");
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
| **name** | **String**| Name must match &#x60;projects/[PROJECT_ID]/brokers/[BROKER_ID]/v2/service_instances/[INSTANCE_ID]/service_binding/[BINDING_ID]&#x60;. | |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |
| **paramCallback** | **String**| JSONP | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **alt** | **String**| Data format for response. | [optional] [default to json] [enum: json, media, proto] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true] |
| **operation** | **String**| If &#x60;operation&#x60; was returned during mutation operation, this field must be populated with the provided value. | [optional] |
| **planId** | **String**| Plan id. | [optional] |
| **serviceId** | **String**| Service id. | [optional] |

### Return type

[**GoogleCloudServicebrokerV1beta1Operation**](GoogleCloudServicebrokerV1beta1Operation.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

