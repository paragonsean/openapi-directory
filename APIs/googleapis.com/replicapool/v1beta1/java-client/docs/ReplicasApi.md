# ReplicasApi

All URIs are relative to *https://www.googleapis.com/replicapool/v1beta1/projects*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**replicapoolReplicasDelete**](ReplicasApi.md#replicapoolReplicasDelete) | **POST** /{projectName}/zones/{zone}/pools/{poolName}/replicas/{replicaName} |  |
| [**replicapoolReplicasGet**](ReplicasApi.md#replicapoolReplicasGet) | **GET** /{projectName}/zones/{zone}/pools/{poolName}/replicas/{replicaName} |  |
| [**replicapoolReplicasList**](ReplicasApi.md#replicapoolReplicasList) | **GET** /{projectName}/zones/{zone}/pools/{poolName}/replicas |  |
| [**replicapoolReplicasRestart**](ReplicasApi.md#replicapoolReplicasRestart) | **POST** /{projectName}/zones/{zone}/pools/{poolName}/replicas/{replicaName}/restart |  |


<a id="replicapoolReplicasDelete"></a>
# **replicapoolReplicasDelete**
> Replica replicapoolReplicasDelete(projectName, zone, poolName, replicaName, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, replicasDeleteRequest)



Deletes a replica from the pool.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReplicasApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.googleapis.com/replicapool/v1beta1/projects");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ReplicasApi apiInstance = new ReplicasApi(defaultClient);
    String projectName = "projectName_example"; // String | The project ID for this request.
    String zone = "zone_example"; // String | The zone where the replica lives.
    String poolName = "poolName_example"; // String | The replica pool name for this request.
    String replicaName = "replicaName_example"; // String | The name of the replica for this request.
    String alt = "json"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    ReplicasDeleteRequest replicasDeleteRequest = new ReplicasDeleteRequest(); // ReplicasDeleteRequest | 
    try {
      Replica result = apiInstance.replicapoolReplicasDelete(projectName, zone, poolName, replicaName, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, replicasDeleteRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReplicasApi#replicapoolReplicasDelete");
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
| **projectName** | **String**| The project ID for this request. | |
| **zone** | **String**| The zone where the replica lives. | |
| **poolName** | **String**| The replica pool name for this request. | |
| **replicaName** | **String**| The name of the replica for this request. | |
| **alt** | **String**| Data format for the response. | [optional] [default to json] [enum: json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |
| **replicasDeleteRequest** | [**ReplicasDeleteRequest**](ReplicasDeleteRequest.md)|  | [optional] |

### Return type

[**Replica**](Replica.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="replicapoolReplicasGet"></a>
# **replicapoolReplicasGet**
> Replica replicapoolReplicasGet(projectName, zone, poolName, replicaName, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp)



Gets information about a specific replica.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReplicasApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.googleapis.com/replicapool/v1beta1/projects");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ReplicasApi apiInstance = new ReplicasApi(defaultClient);
    String projectName = "projectName_example"; // String | The project ID for this request.
    String zone = "zone_example"; // String | The zone where the replica lives.
    String poolName = "poolName_example"; // String | The replica pool name for this request.
    String replicaName = "replicaName_example"; // String | The name of the replica for this request.
    String alt = "json"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    try {
      Replica result = apiInstance.replicapoolReplicasGet(projectName, zone, poolName, replicaName, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReplicasApi#replicapoolReplicasGet");
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
| **projectName** | **String**| The project ID for this request. | |
| **zone** | **String**| The zone where the replica lives. | |
| **poolName** | **String**| The replica pool name for this request. | |
| **replicaName** | **String**| The name of the replica for this request. | |
| **alt** | **String**| Data format for the response. | [optional] [default to json] [enum: json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |

### Return type

[**Replica**](Replica.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="replicapoolReplicasList"></a>
# **replicapoolReplicasList**
> ReplicasListResponse replicapoolReplicasList(projectName, zone, poolName, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, maxResults, pageToken)



Lists all replicas in a pool.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReplicasApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.googleapis.com/replicapool/v1beta1/projects");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ReplicasApi apiInstance = new ReplicasApi(defaultClient);
    String projectName = "projectName_example"; // String | The project ID for this request.
    String zone = "zone_example"; // String | The zone where the replica pool lives.
    String poolName = "poolName_example"; // String | The replica pool name for this request.
    String alt = "json"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    Integer maxResults = 500; // Integer | Maximum count of results to be returned. Acceptable values are 0 to 100, inclusive. (Default: 50)
    String pageToken = "pageToken_example"; // String | Set this to the nextPageToken value returned by a previous list request to obtain the next page of results from the previous list request.
    try {
      ReplicasListResponse result = apiInstance.replicapoolReplicasList(projectName, zone, poolName, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp, maxResults, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReplicasApi#replicapoolReplicasList");
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
| **projectName** | **String**| The project ID for this request. | |
| **zone** | **String**| The zone where the replica pool lives. | |
| **poolName** | **String**| The replica pool name for this request. | |
| **alt** | **String**| Data format for the response. | [optional] [default to json] [enum: json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |
| **maxResults** | **Integer**| Maximum count of results to be returned. Acceptable values are 0 to 100, inclusive. (Default: 50) | [optional] [default to 500] |
| **pageToken** | **String**| Set this to the nextPageToken value returned by a previous list request to obtain the next page of results from the previous list request. | [optional] |

### Return type

[**ReplicasListResponse**](ReplicasListResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="replicapoolReplicasRestart"></a>
# **replicapoolReplicasRestart**
> Replica replicapoolReplicasRestart(projectName, zone, poolName, replicaName, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp)



Restarts a replica in a pool.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReplicasApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.googleapis.com/replicapool/v1beta1/projects");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ReplicasApi apiInstance = new ReplicasApi(defaultClient);
    String projectName = "projectName_example"; // String | The project ID for this request.
    String zone = "zone_example"; // String | The zone where the replica lives.
    String poolName = "poolName_example"; // String | The replica pool name for this request.
    String replicaName = "replicaName_example"; // String | The name of the replica for this request.
    String alt = "json"; // String | Data format for the response.
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    String userIp = "userIp_example"; // String | Deprecated. Please use quotaUser instead.
    try {
      Replica result = apiInstance.replicapoolReplicasRestart(projectName, zone, poolName, replicaName, alt, fields, key, oauthToken, prettyPrint, quotaUser, userIp);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReplicasApi#replicapoolReplicasRestart");
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
| **projectName** | **String**| The project ID for this request. | |
| **zone** | **String**| The zone where the replica lives. | |
| **poolName** | **String**| The replica pool name for this request. | |
| **replicaName** | **String**| The name of the replica for this request. | |
| **alt** | **String**| Data format for the response. | [optional] [default to json] [enum: json] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true] |
| **quotaUser** | **String**| An opaque string that represents a user for quota purposes. Must not exceed 40 characters. | [optional] |
| **userIp** | **String**| Deprecated. Please use quotaUser instead. | [optional] |

### Return type

[**Replica**](Replica.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

