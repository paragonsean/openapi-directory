# HostApi

All URIs are relative to */api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**bulkRegisterHostAsync**](HostApi.md#bulkRegisterHostAsync) | **POST** /host/bulk_background | Register hosts |
| [**deleteHost**](HostApi.md#deleteHost) | **DELETE** /host/{id} | Delete a registered host |
| [**discoverNasShares**](HostApi.md#discoverNasShares) | **GET** /host/{id}/nas_share_discover | Discover and return all shares on a NAS host |
| [**getHost**](HostApi.md#getHost) | **GET** /host/{id} | Get summary information for a host |
| [**getRbsHostInfo**](HostApi.md#getRbsHostInfo) | **GET** /host/rbs | Get the Rubrik Backup Service details for a host |
| [**hostMakePrimary**](HostApi.md#hostMakePrimary) | **POST** /host/make_primary | Make this cluster the primary for agents on a set of hosts |
| [**queryHost**](HostApi.md#queryHost) | **GET** /host | Get summary information for hosts |
| [**queryHostVolume**](HostApi.md#queryHostVolume) | **GET** /host/{id}/volume | Get list of Volume Group volumes |
| [**rbsInstall**](HostApi.md#rbsInstall) | **POST** /host/rbs/install | Install Rubrik Backup Service on a host |
| [**rbsUninstall**](HostApi.md#rbsUninstall) | **POST** /host/rbs/uninstall | Uninstall Rubrik Backup Service from a host |
| [**rbsUpgrade**](HostApi.md#rbsUpgrade) | **POST** /host/rbs/upgrade | Upgrade Rubrik Backup Service on a host |
| [**refreshHost**](HostApi.md#refreshHost) | **POST** /host/{id}/refresh | Refresh a host |
| [**registerHost**](HostApi.md#registerHost) | **POST** /host | Register a host |
| [**registerHostAsync**](HostApi.md#registerHostAsync) | **POST** /host/background | Register a host |
| [**searchHost**](HostApi.md#searchHost) | **GET** /host/{id}/search | Search for a file within the host |
| [**updateCertificateHost**](HostApi.md#updateCertificateHost) | **PUT** /host/certificate/{id} | Update certificate |
| [**updateHost**](HostApi.md#updateHost) | **PATCH** /host/{id} | Modify information for a registered host |


<a id="bulkRegisterHostAsync"></a>
# **bulkRegisterHostAsync**
> List&lt;HostDetail&gt; bulkRegisterHostAsync(hostRegister)

Register hosts

Register multiple hosts and perform discovery for databases and Microsoft SQL Server instances. When called, this API returns a success message, but completes the host registration in the background. Monitor the status of the background host discovery with the \&quot;status\&quot; field in GET API on /hosts. The POST API on /hosts can take longer for discovery, depending on the number of hosts on the system. POST on this API can be used instead to perform the discovery in the background and quickly register the host. Doing this requires that you install RBS for Linux and Windows hosts, similar to regular register using POST on /hosts.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HostApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    HostApi apiInstance = new HostApi(defaultClient);
    List<HostRegister> hostRegister = Arrays.asList(); // List<HostRegister> | Registration definition for each host.
    try {
      List<HostDetail> result = apiInstance.bulkRegisterHostAsync(hostRegister);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HostApi#bulkRegisterHostAsync");
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
| **hostRegister** | [**List&lt;HostRegister&gt;**](HostRegister.md)| Registration definition for each host. | |

### Return type

[**List&lt;HostDetail&gt;**](HostDetail.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Summary information from host registration. |  -  |

<a id="deleteHost"></a>
# **deleteHost**
> deleteHost(id)

Delete a registered host

Delete host by specifying the host ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HostApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    HostApi apiInstance = new HostApi(defaultClient);
    String id = "id_example"; // String | ID of the host to delete.
    try {
      apiInstance.deleteHost(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling HostApi#deleteHost");
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
| **id** | **String**| ID of the host to delete. | |

### Return type

null (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Deleted specified host. |  -  |

<a id="discoverNasShares"></a>
# **discoverNasShares**
> List&lt;DiscoveredNasShare&gt; discoverNasShares(id)

Discover and return all shares on a NAS host

Discover and return all shares on the identified NAS host.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HostApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    HostApi apiInstance = new HostApi(defaultClient);
    String id = "id_example"; // String | The discoverable NAS host ID.
    try {
      List<DiscoveredNasShare> result = apiInstance.discoverNasShares(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HostApi#discoverNasShares");
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
| **id** | **String**| The discoverable NAS host ID. | |

### Return type

[**List&lt;DiscoveredNasShare&gt;**](DiscoveredNasShare.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The discovered NAS shares. |  -  |

<a id="getHost"></a>
# **getHost**
> HostDetail getHost(id)

Get summary information for a host

Retrieve summary information for a registered host.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HostApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    HostApi apiInstance = new HostApi(defaultClient);
    String id = "id_example"; // String | ID of the registered host.
    try {
      HostDetail result = apiInstance.getHost(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HostApi#getHost");
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
| **id** | **String**| ID of the registered host. | |

### Return type

[**HostDetail**](HostDetail.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Summary information for the specified host. |  -  |

<a id="getRbsHostInfo"></a>
# **getRbsHostInfo**
> RbsHostSummary getRbsHostInfo(name, username, password, operationTimeout)

Get the Rubrik Backup Service details for a host

Get the details of the Rubrik Backup Service (RBS) installed on a specific host. Specify the details of the host to check whether RBS is installed on the host or not. If RBS is installed, the response will include the RBS details.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HostApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    HostApi apiInstance = new HostApi(defaultClient);
    String name = "name_example"; // String | IP address or hostname of the host.
    String username = "username_example"; // String | Name of the user account that has sudo/admin privileges on the RBS host. This is required to install/uninstall/upgrade RBS packages on the RBS host.
    String password = "password_example"; // String | Password associated with the username that has access to the host.
    Long operationTimeout = 600L; // Long | Number of seconds after which the operation is terminated if it has not completed execution. Default value is 600 seconds.
    try {
      RbsHostSummary result = apiInstance.getRbsHostInfo(name, username, password, operationTimeout);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HostApi#getRbsHostInfo");
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
| **name** | **String**| IP address or hostname of the host. | |
| **username** | **String**| Name of the user account that has sudo/admin privileges on the RBS host. This is required to install/uninstall/upgrade RBS packages on the RBS host. | |
| **password** | **String**| Password associated with the username that has access to the host. | |
| **operationTimeout** | **Long**| Number of seconds after which the operation is terminated if it has not completed execution. Default value is 600 seconds. | [optional] [default to 600] |

### Return type

[**RbsHostSummary**](RbsHostSummary.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Rubrik Backup Service details for the specified host. |  -  |
| **404** | Rubrik Backup Service is not installed on the host. |  -  |
| **422** | Failed to get Rubrik Backup Service details for the specified host. |  -  |

<a id="hostMakePrimary"></a>
# **hostMakePrimary**
> AsyncRequestStatus hostMakePrimary(hostMakePrimaryRequest)

Make this cluster the primary for agents on a set of hosts

Migrate the primary cluster with which the agent is able to perform regular operations (backup, restore etc). This can be done on a specified set of hosts or for all hosts that currently have a specified primary cluster for disaster recovery. Specify exactly one of &#x60;ids&#x60; or &#x60;oldPrimaryClusterUuid&#x60;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HostApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    HostApi apiInstance = new HostApi(defaultClient);
    HostMakePrimaryRequest hostMakePrimaryRequest = new HostMakePrimaryRequest(); // HostMakePrimaryRequest | Description of hosts to migrate.
    try {
      AsyncRequestStatus result = apiInstance.hostMakePrimary(hostMakePrimaryRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HostApi#hostMakePrimary");
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
| **hostMakePrimaryRequest** | [**HostMakePrimaryRequest**](HostMakePrimaryRequest.md)| Description of hosts to migrate. | |

### Return type

[**AsyncRequestStatus**](AsyncRequestStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Asynchronous request for making this cluster primary. |  -  |

<a id="queryHost"></a>
# **queryHost**
> HostSummaryListResponse queryHost(operatingSystemType, operatingSystem, primaryClusterId, name, hostname, sortBy, sortOrder, snappableStatus)

Get summary information for hosts

Retrieve summary information for all hosts that are registered with a Rubrik cluster.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HostApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    HostApi apiInstance = new HostApi(defaultClient);
    String operatingSystemType = "ANY"; // String | Filter the summary information based on the operating system type. Accepted values are 'Windows', 'UnixLike', 'ANY', 'NONE'. Use **_NONE_** to only return information for hosts templates that do not have operating system type set. Use **_ANY_** to only return information for hosts that have operating system type set.
    String operatingSystem = "operatingSystem_example"; // String | Filter the summary information based on the operating system. Use **_AIX_**, **_Linux_** or **_Solaris_** to restrict the returned information to hosts with operating systems within the specified operating system family. Use a specific operating system release version to restrict the returned information to hosts with operating systems that match the specified version.
    String primaryClusterId = "primaryClusterId_example"; // String | Filters the summary information based on the Rubrik cluster specified by the value of primary_cluster_id. Use 'local' for the Rubrik cluster that is hosting the current REST API session.
    String name = "name_example"; // String | Retrieve hosts with a host name matching the provided name. The search type is infix.
    String hostname = "hostname_example"; // String | (Deprecated) Retrieve hosts with a host name matching the provided name. The search type is infix.
    String sortBy = "hostname"; // String | Specifies the host attribute to use in sorting the host summary information. Performs an ASCII sort of the summary information using the specified attribute, in the order specified. Valid attributes are 'hostname'.
    String sortOrder = "asc"; // String | Sort order, either ascending or descending.
    String snappableStatus = "Protectable"; // String | Determines whether to fetch hosts with additional privilege checks.
    try {
      HostSummaryListResponse result = apiInstance.queryHost(operatingSystemType, operatingSystem, primaryClusterId, name, hostname, sortBy, sortOrder, snappableStatus);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HostApi#queryHost");
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
| **operatingSystemType** | **String**| Filter the summary information based on the operating system type. Accepted values are &#39;Windows&#39;, &#39;UnixLike&#39;, &#39;ANY&#39;, &#39;NONE&#39;. Use **_NONE_** to only return information for hosts templates that do not have operating system type set. Use **_ANY_** to only return information for hosts that have operating system type set. | [optional] [enum: ANY, NONE, UnixLike, Windows] |
| **operatingSystem** | **String**| Filter the summary information based on the operating system. Use **_AIX_**, **_Linux_** or **_Solaris_** to restrict the returned information to hosts with operating systems within the specified operating system family. Use a specific operating system release version to restrict the returned information to hosts with operating systems that match the specified version. | [optional] |
| **primaryClusterId** | **String**| Filters the summary information based on the Rubrik cluster specified by the value of primary_cluster_id. Use &#39;local&#39; for the Rubrik cluster that is hosting the current REST API session. | [optional] |
| **name** | **String**| Retrieve hosts with a host name matching the provided name. The search type is infix. | [optional] |
| **hostname** | **String**| (Deprecated) Retrieve hosts with a host name matching the provided name. The search type is infix. | [optional] |
| **sortBy** | **String**| Specifies the host attribute to use in sorting the host summary information. Performs an ASCII sort of the summary information using the specified attribute, in the order specified. Valid attributes are &#39;hostname&#39;. | [optional] [enum: hostname] |
| **sortOrder** | **String**| Sort order, either ascending or descending. | [optional] [enum: asc, desc] |
| **snappableStatus** | **String**| Determines whether to fetch hosts with additional privilege checks. | [optional] [enum: Protectable] |

### Return type

[**HostSummaryListResponse**](HostSummaryListResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Summary information for registered hosts. |  -  |

<a id="queryHostVolume"></a>
# **queryHostVolume**
> HostVolumeSummaryListResponse queryHostVolume(id)

Get list of Volume Group volumes

Retrieve summary information for each volume on a specified Volume Group host.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HostApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    HostApi apiInstance = new HostApi(defaultClient);
    String id = "id_example"; // String | The ID of the host.
    try {
      HostVolumeSummaryListResponse result = apiInstance.queryHostVolume(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HostApi#queryHostVolume");
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
| **id** | **String**| The ID of the host. | |

### Return type

[**HostVolumeSummaryListResponse**](HostVolumeSummaryListResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get volume summary from the host. |  -  |

<a id="rbsInstall"></a>
# **rbsInstall**
> RbsHostOperationResponse rbsInstall(rbsHostOperationRequest)

Install Rubrik Backup Service on a host

Install Rubrik Backup Service on a host.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HostApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    HostApi apiInstance = new HostApi(defaultClient);
    RbsHostOperationRequest rbsHostOperationRequest = new RbsHostOperationRequest(); // RbsHostOperationRequest | Configuration parameters to install RBS on a host.
    try {
      RbsHostOperationResponse result = apiInstance.rbsInstall(rbsHostOperationRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HostApi#rbsInstall");
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
| **rbsHostOperationRequest** | [**RbsHostOperationRequest**](RbsHostOperationRequest.md)| Configuration parameters to install RBS on a host. | |

### Return type

[**RbsHostOperationResponse**](RbsHostOperationResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response for the Rubrik Backup Service installation request. |  -  |
| **408** | Rubrik Backup Service install operation timed out on the host. |  -  |
| **422** | Failed to install Rubrik Backup Service on the host. |  -  |

<a id="rbsUninstall"></a>
# **rbsUninstall**
> RbsHostOperationResponse rbsUninstall(rbsHostOperationRequest)

Uninstall Rubrik Backup Service from a host

Uninstall Rubrik Backup Service from a host.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HostApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    HostApi apiInstance = new HostApi(defaultClient);
    RbsHostOperationRequest rbsHostOperationRequest = new RbsHostOperationRequest(); // RbsHostOperationRequest | Configuration parameters to uninstall RBS from a host.
    try {
      RbsHostOperationResponse result = apiInstance.rbsUninstall(rbsHostOperationRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HostApi#rbsUninstall");
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
| **rbsHostOperationRequest** | [**RbsHostOperationRequest**](RbsHostOperationRequest.md)| Configuration parameters to uninstall RBS from a host. | |

### Return type

[**RbsHostOperationResponse**](RbsHostOperationResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully uninstalled RBS from the host. |  -  |
| **408** | Rubrik Backup Service uninstall operation timed out on the host. |  -  |
| **422** | Failed to uninstall Rubrik Backup Service from the host. |  -  |

<a id="rbsUpgrade"></a>
# **rbsUpgrade**
> RbsHostOperationResponse rbsUpgrade(rbsHostOperationRequest)

Upgrade Rubrik Backup Service on a host

Upgrade Rubrik Backup Service on a host.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HostApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    HostApi apiInstance = new HostApi(defaultClient);
    RbsHostOperationRequest rbsHostOperationRequest = new RbsHostOperationRequest(); // RbsHostOperationRequest | Configuration parameters to upgrade RBS on a host.
    try {
      RbsHostOperationResponse result = apiInstance.rbsUpgrade(rbsHostOperationRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HostApi#rbsUpgrade");
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
| **rbsHostOperationRequest** | [**RbsHostOperationRequest**](RbsHostOperationRequest.md)| Configuration parameters to upgrade RBS on a host. | |

### Return type

[**RbsHostOperationResponse**](RbsHostOperationResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Rubrik Backup Service upgrade response. |  -  |
| **408** | Rubrik Backup Service upgrade operation timed out on the host. |  -  |
| **422** | Failed to upgrade Rubrik Backup Service on the host. |  -  |

<a id="refreshHost"></a>
# **refreshHost**
> HostDetail refreshHost(id)

Refresh a host

Refresh the properties of a host object when changes on the host are not seen in the Rubrik web UI.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HostApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    HostApi apiInstance = new HostApi(defaultClient);
    String id = "id_example"; // String | ID assigned to a host object.
    try {
      HostDetail result = apiInstance.refreshHost(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HostApi#refreshHost");
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
| **id** | **String**| ID assigned to a host object. | |

### Return type

[**HostDetail**](HostDetail.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Refreshed the properties shown for the specified host. |  -  |

<a id="registerHost"></a>
# **registerHost**
> HostDetail registerHost(hostRegister)

Register a host

Register a host.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HostApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    HostApi apiInstance = new HostApi(defaultClient);
    HostRegister hostRegister = new HostRegister(); // HostRegister | Registration definition for a host.
    try {
      HostDetail result = apiInstance.registerHost(hostRegister);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HostApi#registerHost");
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
| **hostRegister** | [**HostRegister**](HostRegister.md)| Registration definition for a host. | |

### Return type

[**HostDetail**](HostDetail.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Summary information from registration of the host. |  -  |

<a id="registerHostAsync"></a>
# **registerHostAsync**
> HostDetail registerHostAsync(hostRegister)

Register a host

Register a host and perform discovery for databases and Microsoft SQL Server instances. When called, this API returns a success message, but completes the host registration in the background. Monitor the status of the background host discovery with the \&quot;status\&quot; field in GET API on /hosts. The POST API on /hosts can take longer for discovery, depending on the number of hosts on the system. POST on this API can be used instead to perform the discovery in the background and quickly register the host. Doing this requires that you install RBS for Linux and Windows hosts, similar to regular register using POST on /hosts.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HostApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    HostApi apiInstance = new HostApi(defaultClient);
    HostRegister hostRegister = new HostRegister(); // HostRegister | Registration definition for a host.
    try {
      HostDetail result = apiInstance.registerHostAsync(hostRegister);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HostApi#registerHostAsync");
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
| **hostRegister** | [**HostRegister**](HostRegister.md)| Registration definition for a host. | |

### Return type

[**HostDetail**](HostDetail.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Summary host registration information. |  -  |

<a id="searchHost"></a>
# **searchHost**
> SearchResponseListResponse searchHost(id, path)

Search for a file within the host

Search for a file within the host. Search via full path prefix or filename prefix.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HostApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    HostApi apiInstance = new HostApi(defaultClient);
    String id = "id_example"; // String | ID of the host to search.
    String path = "path_example"; // String | The path query. Either path prefix or filename prefix.
    try {
      SearchResponseListResponse result = apiInstance.searchHost(id, path);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HostApi#searchHost");
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
| **id** | **String**| ID of the host to search. | |
| **path** | **String**| The path query. Either path prefix or filename prefix. | |

### Return type

[**SearchResponseListResponse**](SearchResponseListResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Search results. |  -  |

<a id="updateCertificateHost"></a>
# **updateCertificateHost**
> HostDetail updateCertificateHost(id)

Update certificate

Provide an updated certificate for a specified host.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HostApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    HostApi apiInstance = new HostApi(defaultClient);
    String id = "id_example"; // String | ID of the host.
    try {
      HostDetail result = apiInstance.updateCertificateHost(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HostApi#updateCertificateHost");
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
| **id** | **String**| ID of the host. | |

### Return type

[**HostDetail**](HostDetail.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns a detailed view of the update host. |  -  |

<a id="updateHost"></a>
# **updateHost**
> HostDetail updateHost(id, hostUpdate)

Modify information for a registered host

Change the FQDN and IPv4 address that is assigned to a host object. Enable or disable pre-transfer data compression. Enable or disable change block tracking (CBT) for backups of SQL Server databases on Windows hosts. Enable or disable volume filter driver (VFD) for volume backups on Windows hosts. Set an Oracle user with sysdba privileges to permit Oracle discovery queries.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HostApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    HostApi apiInstance = new HostApi(defaultClient);
    String id = "id_example"; // String | ID of the registered host.
    HostUpdate hostUpdate = new HostUpdate(); // HostUpdate | Properties of host to update.
    try {
      HostDetail result = apiInstance.updateHost(id, hostUpdate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HostApi#updateHost");
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
| **id** | **String**| ID of the registered host. | |
| **hostUpdate** | [**HostUpdate**](HostUpdate.md)| Properties of host to update. | |

### Return type

[**HostDetail**](HostDetail.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Summary information for the specified host. |  -  |

