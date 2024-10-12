# ClusterApi

All URIs are relative to */api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addKmipServer**](ClusterApi.md#addKmipServer) | **PUT** /cluster/{id}/security/kmip/server | Add a KMIP server |
| [**addSyslogExportRule**](ClusterApi.md#addSyslogExportRule) | **POST** /syslog/export | Add a new syslog export rule |
| [**availableVersion**](ClusterApi.md#availableVersion) | **GET** /cluster/{id}/upgrade/available_version | Retrieve CDM versions available for upgrade |
| [**changeClusterNodeHostnames**](ClusterApi.md#changeClusterNodeHostnames) | **POST** /cluster/{id}/node_hostname | Change hostname for nodes in a Rubrik cluster |
| [**deleteKmipServer**](ClusterApi.md#deleteKmipServer) | **DELETE** /cluster/{id}/security/kmip/server | Remove the specified KMIP server |
| [**deleteSyslogExportRule**](ClusterApi.md#deleteSyslogExportRule) | **DELETE** /syslog/export/{id} | Delete the specified syslog export rule |
| [**getAsyncRequestStatusForUpgrade**](ClusterApi.md#getAsyncRequestStatusForUpgrade) | **GET** /cluster/{id}/upgrade/request/{request_id} | Get asynchronous request details |
| [**getClusterApiVersion**](ClusterApi.md#getClusterApiVersion) | **GET** /cluster/{id}/api_version | Get cluster REST API version |
| [**getClusterCertificate**](ClusterApi.md#getClusterCertificate) | **GET** /cluster/{id}/certificate | Get the cluster certificate |
| [**getClusterNodeHostnames**](ClusterApi.md#getClusterNodeHostnames) | **GET** /cluster/{id}/node_hostname | Get the node ID to hostname mapping for all the nodes in a Rubrik cluster  |
| [**getClusterNodeIds**](ClusterApi.md#getClusterNodeIds) | **GET** /cluster/{id}/node_id | Get the name of the nodes in the cluster |
| [**getClusterVersion**](ClusterApi.md#getClusterVersion) | **GET** /cluster/{id}/version | Get cluster software version |
| [**getCorsConfiguration**](ClusterApi.md#getCorsConfiguration) | **GET** /cluster/{id}/security/cors | Get CORS configuration |
| [**getEncryptionStatus**](ClusterApi.md#getEncryptionStatus) | **GET** /cluster/{id}/security/encryption | Get encryption at rest status |
| [**getFips**](ClusterApi.md#getFips) | **GET** /cluster/{id}/security/fips | Get FIPS enablement status |
| [**getKmipClient**](ClusterApi.md#getKmipClient) | **GET** /cluster/{id}/security/kmip/client | Get the KMIP client configuration |
| [**getKmipServer**](ClusterApi.md#getKmipServer) | **GET** /cluster/{id}/security/kmip/server | Get KMIP server information |
| [**getPeriodicUpgradePrechecksStatus**](ClusterApi.md#getPeriodicUpgradePrechecksStatus) | **GET** /cluster/{id}/upgrade/precheck_status | Get the result of the latest run of the upgrade prechecks |
| [**getPublicClusterInfo**](ClusterApi.md#getPublicClusterInfo) | **GET** /cluster/{id} | Get cluster details |
| [**getRubrikSnmpMibDownloadLink**](ClusterApi.md#getRubrikSnmpMibDownloadLink) | **GET** /cluster/{id}/snmp_mib_link | Get the link for Rubrik SNMP MIB file |
| [**getSyslogExportRule**](ClusterApi.md#getSyslogExportRule) | **GET** /syslog/export/{id} | Get the specified syslog export rule |
| [**getSyslogExportRules**](ClusterApi.md#getSyslogExportRules) | **GET** /syslog/export | Get the configured syslog export rules |
| [**getSyslogMsgSnmpMibDownloadLink**](ClusterApi.md#getSyslogMsgSnmpMibDownloadLink) | **GET** /cluster/{id}/syslog_msg_mib_link | Get the link for SYSLOG-MSG-MIB file |
| [**getSyslogTcSnmpMibDownloadLink**](ClusterApi.md#getSyslogTcSnmpMibDownloadLink) | **GET** /cluster/{id}/syslog_tc_mib_link | Get the link for SYSLOG-TC-MIB file |
| [**getTotpGlobalSetting**](ClusterApi.md#getTotpGlobalSetting) | **GET** /cluster/{id}/security/totp/setting | Get global TOTP setting |
| [**getTruststores**](ClusterApi.md#getTruststores) | **GET** /cluster/{id}/security/truststore | Get summary of all truststores |
| [**getWebSignedCertificate**](ClusterApi.md#getWebSignedCertificate) | **GET** /cluster/{id}/security/web_signed_cert | Get the signed certificate for Web server |
| [**hasRubrikSupportPortalCredentials**](ClusterApi.md#hasRubrikSupportPortalCredentials) | **GET** /cluster/{id}/rubrik_support_portal_credentials | Check credentials to the Rubrik support portal |
| [**manualDiscover**](ClusterApi.md#manualDiscover) | **POST** /cluster/{id}/manual_discover | Manually discover nodes |
| [**manualDiscoverIpv4**](ClusterApi.md#manualDiscoverIpv4) | **POST** /cluster/{id}/manual_discover_ipv4 | Manually discover nodes over IPv4 address |
| [**monitorEvents**](ClusterApi.md#monitorEvents) | **GET** /cluster/me/upgrade/monitor_events | Get event notifications |
| [**patchPasswordRequirements**](ClusterApi.md#patchPasswordRequirements) | **PATCH** /cluster/{id}/security/password_requirements | Set password requirements |
| [**queryPasswordRequirements**](ClusterApi.md#queryPasswordRequirements) | **GET** /cluster/{id}/security/password_requirements | Get password requirements |
| [**resetWebSignedCertificate**](ClusterApi.md#resetWebSignedCertificate) | **DELETE** /cluster/{id}/security/web_signed_cert | Reset the signed certificate for Web server |
| [**runPeriodicUpgradePrechecks**](ClusterApi.md#runPeriodicUpgradePrechecks) | **POST** /cluster/{id}/upgrade/precheck_status | Start an on demand run of the prechecks |
| [**setKmipClient**](ClusterApi.md#setKmipClient) | **PUT** /cluster/{id}/security/kmip/client | Specify KMIP client credentials for nodes |
| [**setTruststoreCertificate**](ClusterApi.md#setTruststoreCertificate) | **PATCH** /cluster/{id}/security/truststore | Set certificates for one or more truststores |
| [**setWebSignedCertificate**](ClusterApi.md#setWebSignedCertificate) | **PUT** /cluster/{id}/security/web_signed_cert | Set a signed certificate for Web server |
| [**stageCdmSoftware**](ClusterApi.md#stageCdmSoftware) | **POST** /cluster/{id}/upgrade/stage_cdm_software | Stage software on CDM for upgrade |
| [**testSyslogExportRule**](ClusterApi.md#testSyslogExportRule) | **POST** /syslog/export/test | Test the specified syslog export rule |
| [**unsetTruststoreCertificate**](ClusterApi.md#unsetTruststoreCertificate) | **DELETE** /cluster/{id}/security/truststore | Remove certificate associated with specified truststore |
| [**updateCluster**](ClusterApi.md#updateCluster) | **PATCH** /cluster/{id} | Change Rubrik cluster properties |
| [**updateCorsConfiguration**](ClusterApi.md#updateCorsConfiguration) | **PATCH** /cluster/{id}/security/cors | Update CORS configuration |
| [**updateFips**](ClusterApi.md#updateFips) | **PATCH** /cluster/{id}/security/fips | Update FIPS enablement status |
| [**updateRubrikSupportPortalCredentials**](ClusterApi.md#updateRubrikSupportPortalCredentials) | **POST** /cluster/{id}/rubrik_support_portal_credentials | Update credentials to the Rubrik support portal |
| [**updateSyslogExportRule**](ClusterApi.md#updateSyslogExportRule) | **PATCH** /syslog/export/{id} | Update the specified syslog export rule |
| [**updateTotpGlobalSetting**](ClusterApi.md#updateTotpGlobalSetting) | **PUT** /cluster/{id}/security/totp/setting | Update TOTP global setting |


<a id="addKmipServer"></a>
# **addKmipServer**
> AsyncRequestStatus addKmipServer(id, kmipServerConfiguration)

Add a KMIP server

Add the specified KMIP server to the set of active KMIP servers.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClusterApi;

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

    ClusterApi apiInstance = new ClusterApi(defaultClient);
    String id = "me"; // String | ID assigned to a Rubrik cluster. Use *me* to refer to the Rubrik cluster that is hosting the current API session.
    KmipServerConfiguration kmipServerConfiguration = new KmipServerConfiguration(); // KmipServerConfiguration | Object containing the configuration details for a KMIP server.
    try {
      AsyncRequestStatus result = apiInstance.addKmipServer(id, kmipServerConfiguration);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClusterApi#addKmipServer");
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
| **id** | **String**| ID assigned to a Rubrik cluster. Use *me* to refer to the Rubrik cluster that is hosting the current API session. | [default to me] |
| **kmipServerConfiguration** | [**KmipServerConfiguration**](KmipServerConfiguration.md)| Object containing the configuration details for a KMIP server. | |

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
| **202** | Status of the request for setting configuration. |  -  |

<a id="addSyslogExportRule"></a>
# **addSyslogExportRule**
> SyslogExportRuleSummary addSyslogExportRule(syslogExportRuleFull)

Add a new syslog export rule

Adds a new rule specifying where to export the specified syslog information. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClusterApi;

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

    ClusterApi apiInstance = new ClusterApi(defaultClient);
    SyslogExportRuleFull syslogExportRuleFull = new SyslogExportRuleFull(); // SyslogExportRuleFull | Syslog export rule.
    try {
      SyslogExportRuleSummary result = apiInstance.addSyslogExportRule(syslogExportRuleFull);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClusterApi#addSyslogExportRule");
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
| **syslogExportRuleFull** | [**SyslogExportRuleFull**](SyslogExportRuleFull.md)| Syslog export rule. | |

### Return type

[**SyslogExportRuleSummary**](SyslogExportRuleSummary.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Summary of the newly added syslog export rule. |  -  |

<a id="availableVersion"></a>
# **availableVersion**
> List&lt;AvailableVersionInfo&gt; availableVersion(id, filterVersion, fetchLinks, sourceVersion, ignoreLocal, ignoreRemote, ignoreDownloading, downloadJobInstanceId, filterUpgradable, showAll)

Retrieve CDM versions available for upgrade

Retrieve a list of Rubrik CDM versions available to upgrade the Rubrik cluster.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClusterApi;

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

    ClusterApi apiInstance = new ClusterApi(defaultClient);
    String id = "me"; // String | The ID of the Rubrik cluster. To query the local cluster, use *me*.
    String filterVersion = "filterVersion_example"; // String | A string that filters the results based on the prefix. For example, the string \"5.1\" filters all releases in the 5.1 family. If more than one result is desired then this parameter can be used in conjunction with the `show_all` parameter.
    Boolean fetchLinks = false; // Boolean | Include a download URL for the single version passed in the 'filter_version' parameter. A link response will not be provided if the chosen version is locally available, or if 'filter_version' is not specified. 
    String sourceVersion = "sourceVersion_example"; // String | The source version of Rubrik CDM used for the upgradeability check if 'filter_upgradable' if specified. If 'filter_upgradable' is not specified, this parameter is ignored. 
    Boolean ignoreLocal = false; // Boolean | If specified, ignore locally available versions.
    Boolean ignoreRemote = false; // Boolean | If specified, ignore versions available in the Rubrik remote central repository. 
    Boolean ignoreDownloading = true; // Boolean | If specified, ignore versions currently being downloaded.
    String downloadJobInstanceId = "downloadJobInstanceId_example"; // String | If specified, filter results for downloading versions to the provided job instance ID. 
    Boolean filterUpgradable = true; // Boolean | When this parameter is set, the query only returns versions of the Rubrik CDM that can be upgraded to from the version specified in the 'source_version' parameter. If 'source_version' is not specified, we use the cluster version as the source_version. 
    Boolean showAll = false; // Boolean | When this parameter is set, the query shows all patch releases including releases with a newer version released in the same family. When set to false, the query returns only the latest version from each release family. 
    try {
      List<AvailableVersionInfo> result = apiInstance.availableVersion(id, filterVersion, fetchLinks, sourceVersion, ignoreLocal, ignoreRemote, ignoreDownloading, downloadJobInstanceId, filterUpgradable, showAll);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClusterApi#availableVersion");
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
| **id** | **String**| The ID of the Rubrik cluster. To query the local cluster, use *me*. | [default to me] |
| **filterVersion** | **String**| A string that filters the results based on the prefix. For example, the string \&quot;5.1\&quot; filters all releases in the 5.1 family. If more than one result is desired then this parameter can be used in conjunction with the &#x60;show_all&#x60; parameter. | [optional] |
| **fetchLinks** | **Boolean**| Include a download URL for the single version passed in the &#39;filter_version&#39; parameter. A link response will not be provided if the chosen version is locally available, or if &#39;filter_version&#39; is not specified.  | [optional] [default to false] |
| **sourceVersion** | **String**| The source version of Rubrik CDM used for the upgradeability check if &#39;filter_upgradable&#39; if specified. If &#39;filter_upgradable&#39; is not specified, this parameter is ignored.  | [optional] |
| **ignoreLocal** | **Boolean**| If specified, ignore locally available versions. | [optional] [default to false] |
| **ignoreRemote** | **Boolean**| If specified, ignore versions available in the Rubrik remote central repository.  | [optional] [default to false] |
| **ignoreDownloading** | **Boolean**| If specified, ignore versions currently being downloaded. | [optional] [default to true] |
| **downloadJobInstanceId** | **String**| If specified, filter results for downloading versions to the provided job instance ID.  | [optional] |
| **filterUpgradable** | **Boolean**| When this parameter is set, the query only returns versions of the Rubrik CDM that can be upgraded to from the version specified in the &#39;source_version&#39; parameter. If &#39;source_version&#39; is not specified, we use the cluster version as the source_version.  | [optional] [default to true] |
| **showAll** | **Boolean**| When this parameter is set, the query shows all patch releases including releases with a newer version released in the same family. When set to false, the query returns only the latest version from each release family.  | [optional] [default to false] |

### Return type

[**List&lt;AvailableVersionInfo&gt;**](AvailableVersionInfo.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of available software versions. |  -  |

<a id="changeClusterNodeHostnames"></a>
# **changeClusterNodeHostnames**
> changeClusterNodeHostnames(id, nodeHostnameInfo)

Change hostname for nodes in a Rubrik cluster

Change hostnames for multiple nodes at a time, for a specified Rubrik cluster. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClusterApi;

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

    ClusterApi apiInstance = new ClusterApi(defaultClient);
    String id = "me"; // String | ID of the Rubrik cluster or *me* for self.
    List<NodeHostnameInfo> nodeHostnameInfo = Arrays.asList(); // List<NodeHostnameInfo> | Node ID to hostname mapping.
    try {
      apiInstance.changeClusterNodeHostnames(id, nodeHostnameInfo);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClusterApi#changeClusterNodeHostnames");
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
| **id** | **String**| ID of the Rubrik cluster or *me* for self. | [default to me] |
| **nodeHostnameInfo** | [**List&lt;NodeHostnameInfo&gt;**](NodeHostnameInfo.md)| Node ID to hostname mapping. | |

### Return type

null (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Successfully changed hostnames for all the specified nodes in the Rubrik cluster.  |  -  |

<a id="deleteKmipServer"></a>
# **deleteKmipServer**
> AsyncRequestStatus deleteKmipServer(id, serverAddress)

Remove the specified KMIP server

Remove the server with the specified server address from the set of active KMIP servers.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClusterApi;

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

    ClusterApi apiInstance = new ClusterApi(defaultClient);
    String id = "me"; // String | ID assigned to a Rubrik cluster. Use *me* to refer to the Rubrik cluster that is hosting the current API session.
    String serverAddress = "serverAddress_example"; // String | IPv4 address or FQDN (fully qualified domain name) of the KMIP server.
    try {
      AsyncRequestStatus result = apiInstance.deleteKmipServer(id, serverAddress);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClusterApi#deleteKmipServer");
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
| **id** | **String**| ID assigned to a Rubrik cluster. Use *me* to refer to the Rubrik cluster that is hosting the current API session. | [default to me] |
| **serverAddress** | **String**| IPv4 address or FQDN (fully qualified domain name) of the KMIP server. | |

### Return type

[**AsyncRequestStatus**](AsyncRequestStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Status of the request for removing the KMIP server. |  -  |

<a id="deleteSyslogExportRule"></a>
# **deleteSyslogExportRule**
> deleteSyslogExportRule(id)

Delete the specified syslog export rule

Delete the syslog export rule specified by the given id.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClusterApi;

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

    ClusterApi apiInstance = new ClusterApi(defaultClient);
    String id = "id_example"; // String | The ID of the syslog export rule.
    try {
      apiInstance.deleteSyslogExportRule(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClusterApi#deleteSyslogExportRule");
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
| **id** | **String**| The ID of the syslog export rule. | |

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
| **204** | Syslog server export rule successfully deleted. |  -  |

<a id="getAsyncRequestStatusForUpgrade"></a>
# **getAsyncRequestStatusForUpgrade**
> AsyncRequestStatus getAsyncRequestStatusForUpgrade(id, requestId)

Get asynchronous request details

Get asynchronous request details for an upgrade request.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClusterApi;

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

    ClusterApi apiInstance = new ClusterApi(defaultClient);
    String id = "me"; // String | ID of the Rubrik cluster or *me* for self.
    String requestId = "requestId_example"; // String | ID of the request.
    try {
      AsyncRequestStatus result = apiInstance.getAsyncRequestStatusForUpgrade(id, requestId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClusterApi#getAsyncRequestStatusForUpgrade");
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
| **id** | **String**| ID of the Rubrik cluster or *me* for self. | [default to me] |
| **requestId** | **String**| ID of the request. | |

### Return type

[**AsyncRequestStatus**](AsyncRequestStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Status of an asynchronous request. |  -  |

<a id="getClusterApiVersion"></a>
# **getClusterApiVersion**
> ClusterApiVersion getClusterApiVersion(id)

Get cluster REST API version

Retrieves software version of the Rubrik cluster.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClusterApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");

    ClusterApi apiInstance = new ClusterApi(defaultClient);
    String id = "me"; // String | ID of the Rubrik cluster or *me* for self.
    try {
      ClusterApiVersion result = apiInstance.getClusterApiVersion(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClusterApi#getClusterApiVersion");
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
| **id** | **String**| ID of the Rubrik cluster or *me* for self. | [default to me] |

### Return type

[**ClusterApiVersion**](ClusterApiVersion.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | REST API version running on the cluster. |  -  |

<a id="getClusterCertificate"></a>
# **getClusterCertificate**
> ClusterCertificate getClusterCertificate(id)

Get the cluster certificate

Returns the cluster certificate.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClusterApi;

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

    ClusterApi apiInstance = new ClusterApi(defaultClient);
    String id = "me"; // String | ID of the Rubrik cluster or *me* for self.
    try {
      ClusterCertificate result = apiInstance.getClusterCertificate(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClusterApi#getClusterCertificate");
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
| **id** | **String**| ID of the Rubrik cluster or *me* for self. | [default to me] |

### Return type

[**ClusterCertificate**](ClusterCertificate.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns the cluster certificate. |  -  |

<a id="getClusterNodeHostnames"></a>
# **getClusterNodeHostnames**
> NodeHostnameInfoListResponse getClusterNodeHostnames(id)

Get the node ID to hostname mapping for all the nodes in a Rubrik cluster 

Retrieve the ID to hostname mapping for all the nodes that belong to a specified Rubrik cluster. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClusterApi;

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

    ClusterApi apiInstance = new ClusterApi(defaultClient);
    String id = "me"; // String | ID of the Rubrik cluster or *me* for self.
    try {
      NodeHostnameInfoListResponse result = apiInstance.getClusterNodeHostnames(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClusterApi#getClusterNodeHostnames");
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
| **id** | **String**| ID of the Rubrik cluster or *me* for self. | [default to me] |

### Return type

[**NodeHostnameInfoListResponse**](NodeHostnameInfoListResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of node ID to hostname mappings. |  -  |

<a id="getClusterNodeIds"></a>
# **getClusterNodeIds**
> List&lt;NodeId&gt; getClusterNodeIds(id)

Get the name of the nodes in the cluster

Retrieve the list of node IDs for the nodes in this Rubrik CDM cluster.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClusterApi;

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

    ClusterApi apiInstance = new ClusterApi(defaultClient);
    String id = "me"; // String | ID of the Rubrik cluster or *me* for self.
    try {
      List<NodeId> result = apiInstance.getClusterNodeIds(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClusterApi#getClusterNodeIds");
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
| **id** | **String**| ID of the Rubrik cluster or *me* for self. | [default to me] |

### Return type

[**List&lt;NodeId&gt;**](NodeId.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of node IDs. |  -  |

<a id="getClusterVersion"></a>
# **getClusterVersion**
> ClusterVersion getClusterVersion(id)

Get cluster software version

Retrieves software version of the Rubrik cluster.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClusterApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");

    ClusterApi apiInstance = new ClusterApi(defaultClient);
    String id = "me"; // String | ID of the Rubrik cluster or *me* for self.
    try {
      ClusterVersion result = apiInstance.getClusterVersion(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClusterApi#getClusterVersion");
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
| **id** | **String**| ID of the Rubrik cluster or *me* for self. | [default to me] |

### Return type

[**ClusterVersion**](ClusterVersion.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Software version running on the cluster. |  -  |

<a id="getCorsConfiguration"></a>
# **getCorsConfiguration**
> CorsConfiguration getCorsConfiguration(id)

Get CORS configuration

Get the current CORS support configuration for a web server.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClusterApi;

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

    ClusterApi apiInstance = new ClusterApi(defaultClient);
    String id = "me"; // String | ID of the Rubrik cluster or *me* for self.
    try {
      CorsConfiguration result = apiInstance.getCorsConfiguration(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClusterApi#getCorsConfiguration");
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
| **id** | **String**| ID of the Rubrik cluster or *me* for self. | [default to me] |

### Return type

[**CorsConfiguration**](CorsConfiguration.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The current CORS support configuration for a web server. |  -  |

<a id="getEncryptionStatus"></a>
# **getEncryptionStatus**
> EncryptionStatus getEncryptionStatus(id)

Get encryption at rest status

Get the current encryption at rest status of the cluster.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClusterApi;

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

    ClusterApi apiInstance = new ClusterApi(defaultClient);
    String id = "me"; // String | ID of the Rubrik cluster or *me* for self.
    try {
      EncryptionStatus result = apiInstance.getEncryptionStatus(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClusterApi#getEncryptionStatus");
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
| **id** | **String**| ID of the Rubrik cluster or *me* for self. | [default to me] |

### Return type

[**EncryptionStatus**](EncryptionStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The current encryption at rest status for the cluster. |  -  |

<a id="getFips"></a>
# **getFips**
> FipsStatus getFips(id)

Get FIPS enablement status

Returns the current status of FIPS on the specified cluster. When the status is true, FIPS is enabled.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClusterApi;

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

    ClusterApi apiInstance = new ClusterApi(defaultClient);
    String id = "me"; // String | ID of the Rubrik cluster or *me* for self.
    try {
      FipsStatus result = apiInstance.getFips(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClusterApi#getFips");
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
| **id** | **String**| ID of the Rubrik cluster or *me* for self. | [default to me] |

### Return type

[**FipsStatus**](FipsStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The current FIPS enablement status for a cluster. |  -  |

<a id="getKmipClient"></a>
# **getKmipClient**
> KmipClientDetail getKmipClient(id)

Get the KMIP client configuration

Return the currently configured KMIP client information. The response object contains empty fields when KMIP is not configured.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClusterApi;

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

    ClusterApi apiInstance = new ClusterApi(defaultClient);
    String id = "me"; // String | ID assigned to a Rubrik cluster. Use *me* to refer to the Rubrik cluster that is hosting the current API session.
    try {
      KmipClientDetail result = apiInstance.getKmipClient(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClusterApi#getKmipClient");
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
| **id** | **String**| ID assigned to a Rubrik cluster. Use *me* to refer to the Rubrik cluster that is hosting the current API session. | [default to me] |

### Return type

[**KmipClientDetail**](KmipClientDetail.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Current KMIP client configuration detail. |  -  |

<a id="getKmipServer"></a>
# **getKmipServer**
> List&lt;KmipServerDetail&gt; getKmipServer(id, serverAddress)

Get KMIP server information

Returns the KMIP server information for the specified server address. When no server address is specified, this call returns information on all active KMIP servers. The response array is empty when KMIP is not configured or when the server address cannot be found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClusterApi;

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

    ClusterApi apiInstance = new ClusterApi(defaultClient);
    String id = "me"; // String | ID assigned to a Rubrik cluster. Use *me* to refer to the Rubrik cluster that is hosting the current API session.
    String serverAddress = "serverAddress_example"; // String | The address of the KMIP server.
    try {
      List<KmipServerDetail> result = apiInstance.getKmipServer(id, serverAddress);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClusterApi#getKmipServer");
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
| **id** | **String**| ID assigned to a Rubrik cluster. Use *me* to refer to the Rubrik cluster that is hosting the current API session. | [default to me] |
| **serverAddress** | **String**| The address of the KMIP server. | [optional] |

### Return type

[**List&lt;KmipServerDetail&gt;**](KmipServerDetail.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Information for the specified KMIP server(s). |  -  |

<a id="getPeriodicUpgradePrechecksStatus"></a>
# **getPeriodicUpgradePrechecksStatus**
> PrecheckStatusResponse getPeriodicUpgradePrechecksStatus(id, fetchNextRunInfo)

Get the result of the latest run of the upgrade prechecks

Get the result of the latest run of the upgrade prechecks. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClusterApi;

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

    ClusterApi apiInstance = new ClusterApi(defaultClient);
    String id = "me"; // String | ID of the Rubrik cluster or *me* for self.
    Boolean fetchNextRunInfo = false; // Boolean | If specified, fetch information corresponding to next upgrade prechecks job instance. If an upgrade prechecks job instance is currently running, results corresponding to it are returned. 
    try {
      PrecheckStatusResponse result = apiInstance.getPeriodicUpgradePrechecksStatus(id, fetchNextRunInfo);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClusterApi#getPeriodicUpgradePrechecksStatus");
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
| **id** | **String**| ID of the Rubrik cluster or *me* for self. | [default to me] |
| **fetchNextRunInfo** | **Boolean**| If specified, fetch information corresponding to next upgrade prechecks job instance. If an upgrade prechecks job instance is currently running, results corresponding to it are returned.  | [optional] [default to false] |

### Return type

[**PrecheckStatusResponse**](PrecheckStatusResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns the list of precheck failures during the latest run of the upgrade prechecks job.  |  -  |

<a id="getPublicClusterInfo"></a>
# **getPublicClusterInfo**
> ClusterInfo getPublicClusterInfo(id)

Get cluster details

Retrieve public information about the Rubrik cluster.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClusterApi;

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

    ClusterApi apiInstance = new ClusterApi(defaultClient);
    String id = "me"; // String | ID of the Rubrik cluster or *me* for self.
    try {
      ClusterInfo result = apiInstance.getPublicClusterInfo(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClusterApi#getPublicClusterInfo");
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
| **id** | **String**| ID of the Rubrik cluster or *me* for self. | [default to me] |

### Return type

[**ClusterInfo**](ClusterInfo.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Information about the cluster. |  -  |

<a id="getRubrikSnmpMibDownloadLink"></a>
# **getRubrikSnmpMibDownloadLink**
> RubrikMibFileDownloadLink getRubrikSnmpMibDownloadLink(id)

Get the link for Rubrik SNMP MIB file

Retrieve the download link for the Rubrik SNMP MIB file. The retrieval is a synchronous operation.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClusterApi;

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

    ClusterApi apiInstance = new ClusterApi(defaultClient);
    String id = "me"; // String | ID of the Rubrik cluster or *me* for self.
    try {
      RubrikMibFileDownloadLink result = apiInstance.getRubrikSnmpMibDownloadLink(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClusterApi#getRubrikSnmpMibDownloadLink");
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
| **id** | **String**| ID of the Rubrik cluster or *me* for self. | [default to me] |

### Return type

[**RubrikMibFileDownloadLink**](RubrikMibFileDownloadLink.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Download link for the Rubrik SNMP MIB file. |  -  |

<a id="getSyslogExportRule"></a>
# **getSyslogExportRule**
> SyslogExportRuleSummary getSyslogExportRule(id)

Get the specified syslog export rule

Get the summary of the syslog export rule specified by the given id. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClusterApi;

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

    ClusterApi apiInstance = new ClusterApi(defaultClient);
    String id = "id_example"; // String | The ID of syslog export rule.
    try {
      SyslogExportRuleSummary result = apiInstance.getSyslogExportRule(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClusterApi#getSyslogExportRule");
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
| **id** | **String**| The ID of syslog export rule. | |

### Return type

[**SyslogExportRuleSummary**](SyslogExportRuleSummary.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Summary of the syslog export rule. |  -  |

<a id="getSyslogExportRules"></a>
# **getSyslogExportRules**
> SyslogExportRuleSummaryListResponse getSyslogExportRules()

Get the configured syslog export rules

Return the list of all configured syslog export rules.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClusterApi;

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

    ClusterApi apiInstance = new ClusterApi(defaultClient);
    try {
      SyslogExportRuleSummaryListResponse result = apiInstance.getSyslogExportRules();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClusterApi#getSyslogExportRules");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SyslogExportRuleSummaryListResponse**](SyslogExportRuleSummaryListResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of all configured syslog export rules. |  -  |

<a id="getSyslogMsgSnmpMibDownloadLink"></a>
# **getSyslogMsgSnmpMibDownloadLink**
> SyslogMsgMibFileDownloadLink getSyslogMsgSnmpMibDownloadLink(id)

Get the link for SYSLOG-MSG-MIB file

Retrieve the download link for the SYSLOG-MSG-MIB file. The retrieval is a synchronous operation.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClusterApi;

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

    ClusterApi apiInstance = new ClusterApi(defaultClient);
    String id = "me"; // String | ID of the Rubrik cluster or *me* for self.
    try {
      SyslogMsgMibFileDownloadLink result = apiInstance.getSyslogMsgSnmpMibDownloadLink(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClusterApi#getSyslogMsgSnmpMibDownloadLink");
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
| **id** | **String**| ID of the Rubrik cluster or *me* for self. | [default to me] |

### Return type

[**SyslogMsgMibFileDownloadLink**](SyslogMsgMibFileDownloadLink.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Download link for the SYSLOG-MSG-MIB file. |  -  |

<a id="getSyslogTcSnmpMibDownloadLink"></a>
# **getSyslogTcSnmpMibDownloadLink**
> SyslogTcMibFileDownloadLink getSyslogTcSnmpMibDownloadLink(id)

Get the link for SYSLOG-TC-MIB file

Retrieve the download link for the SYSLOG-TC-MIB file. The retrieval is a synchronous operation.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClusterApi;

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

    ClusterApi apiInstance = new ClusterApi(defaultClient);
    String id = "me"; // String | ID of the Rubrik cluster or *me* for self.
    try {
      SyslogTcMibFileDownloadLink result = apiInstance.getSyslogTcSnmpMibDownloadLink(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClusterApi#getSyslogTcSnmpMibDownloadLink");
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
| **id** | **String**| ID of the Rubrik cluster or *me* for self. | [default to me] |

### Return type

[**SyslogTcMibFileDownloadLink**](SyslogTcMibFileDownloadLink.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Download link for the SYSLOG-TC-MIB file. |  -  |

<a id="getTotpGlobalSetting"></a>
# **getTotpGlobalSetting**
> TotpGlobalSetting getTotpGlobalSetting(id)

Get global TOTP setting

Returns TOTP global setting, including whether TOTP is enforced or not.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClusterApi;

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

    ClusterApi apiInstance = new ClusterApi(defaultClient);
    String id = "me"; // String | ID assigned to a Rubrik cluster. Use *me* to refer to the Rubrik cluster that is hosting the current API session.
    try {
      TotpGlobalSetting result = apiInstance.getTotpGlobalSetting(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClusterApi#getTotpGlobalSetting");
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
| **id** | **String**| ID assigned to a Rubrik cluster. Use *me* to refer to the Rubrik cluster that is hosting the current API session. | [default to me] |

### Return type

[**TotpGlobalSetting**](TotpGlobalSetting.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | TOTP global setting for the specified Rubrik cluster. |  -  |

<a id="getTruststores"></a>
# **getTruststores**
> TruststoreSummaryListResponse getTruststores(id)

Get summary of all truststores

Get summary of all truststores.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClusterApi;

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

    ClusterApi apiInstance = new ClusterApi(defaultClient);
    String id = "me"; // String | ID of the Rubrik cluster or *me* for self.
    try {
      TruststoreSummaryListResponse result = apiInstance.getTruststores(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClusterApi#getTruststores");
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
| **id** | **String**| ID of the Rubrik cluster or *me* for self. | [default to me] |

### Return type

[**TruststoreSummaryListResponse**](TruststoreSummaryListResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of truststore summaries. |  -  |

<a id="getWebSignedCertificate"></a>
# **getWebSignedCertificate**
> WebServerCertificateSummary getWebSignedCertificate(id)

Get the signed certificate for Web server

If the web server uses a signed certificate, fetch it.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClusterApi;

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

    ClusterApi apiInstance = new ClusterApi(defaultClient);
    String id = "me"; // String | ID of the Rubrik cluster or *me* for self.
    try {
      WebServerCertificateSummary result = apiInstance.getWebSignedCertificate(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClusterApi#getWebSignedCertificate");
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
| **id** | **String**| ID of the Rubrik cluster or *me* for self. | [default to me] |

### Return type

[**WebServerCertificateSummary**](WebServerCertificateSummary.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Signed certificate of the web server. |  -  |

<a id="hasRubrikSupportPortalCredentials"></a>
# **hasRubrikSupportPortalCredentials**
> BooleanResponse hasRubrikSupportPortalCredentials(id)

Check credentials to the Rubrik support portal

Check whether the specified Rubrik cluster has an existing set of credentials for the Rubrik support portal. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClusterApi;

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

    ClusterApi apiInstance = new ClusterApi(defaultClient);
    String id = "me"; // String | The ID of a Rubrik cluster, or use *me* for the Rubrik cluster that is hosting the current session. 
    try {
      BooleanResponse result = apiInstance.hasRubrikSupportPortalCredentials(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClusterApi#hasRubrikSupportPortalCredentials");
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
| **id** | **String**| The ID of a Rubrik cluster, or use *me* for the Rubrik cluster that is hosting the current session.  | [default to me] |

### Return type

[**BooleanResponse**](BooleanResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns &#39;True&#39; if the specified Rubrik cluster already has credentials for the Rubrik support portal.  |  -  |

<a id="manualDiscover"></a>
# **manualDiscover**
> ManualDiscoveryNodeInfo manualDiscover(id, manualDiscoveryNodeInfo)

Manually discover nodes

Manually specifies mDNS discovery data. Output for this endpoint is identical to the output of the &#39;discover&#39; endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClusterApi;

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

    ClusterApi apiInstance = new ClusterApi(defaultClient);
    String id = "me"; // String | ID of the Rubrik cluster or *me* for self.
    ManualDiscoveryNodeInfo manualDiscoveryNodeInfo = new ManualDiscoveryNodeInfo(); // ManualDiscoveryNodeInfo | Manual discovery input data.
    try {
      ManualDiscoveryNodeInfo result = apiInstance.manualDiscover(id, manualDiscoveryNodeInfo);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClusterApi#manualDiscover");
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
| **id** | **String**| ID of the Rubrik cluster or *me* for self. | [default to me] |
| **manualDiscoveryNodeInfo** | [**ManualDiscoveryNodeInfo**](ManualDiscoveryNodeInfo.md)| Manual discovery input data. | |

### Return type

[**ManualDiscoveryNodeInfo**](ManualDiscoveryNodeInfo.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of nodes available to bootstrap into the specified cluster along with their IPv6 addresses. |  -  |

<a id="manualDiscoverIpv4"></a>
# **manualDiscoverIpv4**
> ManualDiscoveryNodeIpv4Info manualDiscoverIpv4(id, manualDiscoveryNodeIpv4Info)

Manually discover nodes over IPv4 address

Manually specifies discovery data. This endpoint output is identical to the output of the &#39;discover&#39; endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClusterApi;

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

    ClusterApi apiInstance = new ClusterApi(defaultClient);
    String id = "me"; // String | ID of the Rubrik cluster, or *me* for the current cluster.
    ManualDiscoveryNodeIpv4Info manualDiscoveryNodeIpv4Info = new ManualDiscoveryNodeIpv4Info(); // ManualDiscoveryNodeIpv4Info | Manual discovery input data.
    try {
      ManualDiscoveryNodeIpv4Info result = apiInstance.manualDiscoverIpv4(id, manualDiscoveryNodeIpv4Info);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClusterApi#manualDiscoverIpv4");
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
| **id** | **String**| ID of the Rubrik cluster, or *me* for the current cluster. | [default to me] |
| **manualDiscoveryNodeIpv4Info** | [**ManualDiscoveryNodeIpv4Info**](ManualDiscoveryNodeIpv4Info.md)| Manual discovery input data. | |

### Return type

[**ManualDiscoveryNodeIpv4Info**](ManualDiscoveryNodeIpv4Info.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of nodes available to bootstrap into the specified cluster, including their link-local IPv4 addresses. |  -  |

<a id="monitorEvents"></a>
# **monitorEvents**
> List&lt;EventNotification&gt; monitorEvents(eventNotificationQuery)

Get event notifications

Gets notifications about events from a specified set of possible events. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClusterApi;

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

    ClusterApi apiInstance = new ClusterApi(defaultClient);
    List<String> eventNotificationQuery = Arrays.asList(); // List<String> | Specifies a list of events to monitor for notifications.
    try {
      List<EventNotification> result = apiInstance.monitorEvents(eventNotificationQuery);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClusterApi#monitorEvents");
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
| **eventNotificationQuery** | [**List&lt;String&gt;**](String.md)| Specifies a list of events to monitor for notifications. | |

### Return type

[**List&lt;EventNotification&gt;**](EventNotification.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Name and timestamp of an event sent as a notification.  |  -  |

<a id="patchPasswordRequirements"></a>
# **patchPasswordRequirements**
> PasswordRequirementsSummary patchPasswordRequirements(id, passwordRequirementsPatchRequest)

Set password requirements

Update user password requirements for a cluster.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClusterApi;

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

    ClusterApi apiInstance = new ClusterApi(defaultClient);
    String id = "me"; // String | ID of the Rubrik cluster or *me* for self.
    PasswordRequirementsPatchRequest passwordRequirementsPatchRequest = new PasswordRequirementsPatchRequest(); // PasswordRequirementsPatchRequest | Password requirements.
    try {
      PasswordRequirementsSummary result = apiInstance.patchPasswordRequirements(id, passwordRequirementsPatchRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClusterApi#patchPasswordRequirements");
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
| **id** | **String**| ID of the Rubrik cluster or *me* for self. | [default to me] |
| **passwordRequirementsPatchRequest** | [**PasswordRequirementsPatchRequest**](PasswordRequirementsPatchRequest.md)| Password requirements. | |

### Return type

[**PasswordRequirementsSummary**](PasswordRequirementsSummary.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Succesfully patched password requirements. |  -  |

<a id="queryPasswordRequirements"></a>
# **queryPasswordRequirements**
> PasswordRequirementsSummary queryPasswordRequirements(id)

Get password requirements

Query user password requirements for a cluster.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClusterApi;

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

    ClusterApi apiInstance = new ClusterApi(defaultClient);
    String id = "me"; // String | ID of the Rubrik cluster or *me* for self.
    try {
      PasswordRequirementsSummary result = apiInstance.queryPasswordRequirements(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClusterApi#queryPasswordRequirements");
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
| **id** | **String**| ID of the Rubrik cluster or *me* for self. | [default to me] |

### Return type

[**PasswordRequirementsSummary**](PasswordRequirementsSummary.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Active password requirements. |  -  |

<a id="resetWebSignedCertificate"></a>
# **resetWebSignedCertificate**
> AsyncRequestStatus resetWebSignedCertificate(id)

Reset the signed certificate for Web server

Resetting the customer-given certificate for each node&#39;s web server.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClusterApi;

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

    ClusterApi apiInstance = new ClusterApi(defaultClient);
    String id = "me"; // String | ID of the Rubrik cluster or *me* for self.
    try {
      AsyncRequestStatus result = apiInstance.resetWebSignedCertificate(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClusterApi#resetWebSignedCertificate");
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
| **id** | **String**| ID of the Rubrik cluster or *me* for self. | [default to me] |

### Return type

[**AsyncRequestStatus**](AsyncRequestStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Status of the request for resetting the certificate. |  -  |

<a id="runPeriodicUpgradePrechecks"></a>
# **runPeriodicUpgradePrechecks**
> AsyncRequestStatus runPeriodicUpgradePrechecks(id)

Start an on demand run of the prechecks

Start an on demand run of the prechecks. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClusterApi;

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

    ClusterApi apiInstance = new ClusterApi(defaultClient);
    String id = "me"; // String | ID of the Rubrik cluster or *me* for self.
    try {
      AsyncRequestStatus result = apiInstance.runPeriodicUpgradePrechecks(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClusterApi#runPeriodicUpgradePrechecks");
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
| **id** | **String**| ID of the Rubrik cluster or *me* for self. | [default to me] |

### Return type

[**AsyncRequestStatus**](AsyncRequestStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Status of an asynchronous request. |  -  |

<a id="setKmipClient"></a>
# **setKmipClient**
> AsyncRequestStatus setKmipClient(id, kmipClientConfiguration)

Specify KMIP client credentials for nodes

Specify KMIP client credentials for each of the Rubrik cluster nodes.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClusterApi;

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

    ClusterApi apiInstance = new ClusterApi(defaultClient);
    String id = "me"; // String | ID assigned to a Rubrik cluster. Use *me* to refer to the Rubrik cluster that is hosting the current API session.
    KmipClientConfiguration kmipClientConfiguration = new KmipClientConfiguration(); // KmipClientConfiguration | KMIP client configuration.
    try {
      AsyncRequestStatus result = apiInstance.setKmipClient(id, kmipClientConfiguration);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClusterApi#setKmipClient");
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
| **id** | **String**| ID assigned to a Rubrik cluster. Use *me* to refer to the Rubrik cluster that is hosting the current API session. | [default to me] |
| **kmipClientConfiguration** | [**KmipClientConfiguration**](KmipClientConfiguration.md)| KMIP client configuration. | |

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
| **202** | Status of the request for setting client configuration. |  -  |

<a id="setTruststoreCertificate"></a>
# **setTruststoreCertificate**
> setTruststoreCertificate(id, truststorePayload)

Set certificates for one or more truststores

Setting the given certificate for each node&#39;s truststores.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClusterApi;

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

    ClusterApi apiInstance = new ClusterApi(defaultClient);
    String id = "me"; // String | ID of the Rubrik cluster or *me* for self.
    List<TruststorePayload> truststorePayload = Arrays.asList(); // List<TruststorePayload> | Request to update certificate for truststore.
    try {
      apiInstance.setTruststoreCertificate(id, truststorePayload);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClusterApi#setTruststoreCertificate");
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
| **id** | **String**| ID of the Rubrik cluster or *me* for self. | [default to me] |
| **truststorePayload** | [**List&lt;TruststorePayload&gt;**](TruststorePayload.md)| Request to update certificate for truststore. | |

### Return type

null (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | OK on success. |  -  |

<a id="setWebSignedCertificate"></a>
# **setWebSignedCertificate**
> AsyncRequestStatus setWebSignedCertificate(id, webServerCertificatePayload)

Set a signed certificate for Web server

Setting the given certificate for each node&#39;s web server to use.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClusterApi;

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

    ClusterApi apiInstance = new ClusterApi(defaultClient);
    String id = "me"; // String | ID of the Rubrik cluster or *me* for self.
    WebServerCertificatePayload webServerCertificatePayload = new WebServerCertificatePayload(); // WebServerCertificatePayload | Request to update certificate for web server.
    try {
      AsyncRequestStatus result = apiInstance.setWebSignedCertificate(id, webServerCertificatePayload);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClusterApi#setWebSignedCertificate");
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
| **id** | **String**| ID of the Rubrik cluster or *me* for self. | [default to me] |
| **webServerCertificatePayload** | [**WebServerCertificatePayload**](WebServerCertificatePayload.md)| Request to update certificate for web server. | |

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
| **202** | Status of the request for setting certificate. |  -  |

<a id="stageCdmSoftware"></a>
# **stageCdmSoftware**
> AsyncRequestStatus stageCdmSoftware(id, stageCdmSoftwareInfo)

Stage software on CDM for upgrade

Stage software corresponding to a given CDM version on the cluster, in preparation for an upgrade.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClusterApi;

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

    ClusterApi apiInstance = new ClusterApi(defaultClient);
    String id = "me"; // String | ID of the Rubrik cluster or *me* for self.
    StageCdmSoftwareInfo stageCdmSoftwareInfo = new StageCdmSoftwareInfo(); // StageCdmSoftwareInfo | Information about the provided CDM software package.
    try {
      AsyncRequestStatus result = apiInstance.stageCdmSoftware(id, stageCdmSoftwareInfo);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClusterApi#stageCdmSoftware");
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
| **id** | **String**| ID of the Rubrik cluster or *me* for self. | [default to me] |
| **stageCdmSoftwareInfo** | [**StageCdmSoftwareInfo**](StageCdmSoftwareInfo.md)| Information about the provided CDM software package. | |

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
| **202** | ID of the stage CDM software job. |  -  |

<a id="testSyslogExportRule"></a>
# **testSyslogExportRule**
> SyslogServerTestResult testSyslogExportRule(syslogExportRuleFull)

Test the specified syslog export rule

Send a test message using the syslog export rule specified by the given id. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClusterApi;

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

    ClusterApi apiInstance = new ClusterApi(defaultClient);
    SyslogExportRuleFull syslogExportRuleFull = new SyslogExportRuleFull(); // SyslogExportRuleFull | Syslog export rule.
    try {
      SyslogServerTestResult result = apiInstance.testSyslogExportRule(syslogExportRuleFull);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClusterApi#testSyslogExportRule");
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
| **syslogExportRuleFull** | [**SyslogExportRuleFull**](SyslogExportRuleFull.md)| Syslog export rule. | |

### Return type

[**SyslogServerTestResult**](SyslogServerTestResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Syslog export rule was tested successfully. |  -  |

<a id="unsetTruststoreCertificate"></a>
# **unsetTruststoreCertificate**
> unsetTruststoreCertificate(id, truststores)

Remove certificate associated with specified truststore

Remove certificate associated with specified truststore.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClusterApi;

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

    ClusterApi apiInstance = new ClusterApi(defaultClient);
    String id = "me"; // String | ID of the Rubrik cluster or *me* for self.
    List<String> truststores = Arrays.asList(); // List<String> | Comma separated list of truststore types.
    try {
      apiInstance.unsetTruststoreCertificate(id, truststores);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClusterApi#unsetTruststoreCertificate");
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
| **id** | **String**| ID of the Rubrik cluster or *me* for self. | [default to me] |
| **truststores** | [**List&lt;String&gt;**](String.md)| Comma separated list of truststore types. | [enum: System, Gcp] |

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
| **204** | OK on success. |  -  |

<a id="updateCluster"></a>
# **updateCluster**
> ClusterInfo updateCluster(id, clusterUpdate)

Change Rubrik cluster properties

Change the properties of a specified Rubrik cluster. Changes to cluster name could take upto 10 minutes to be propagated to all nodes.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClusterApi;

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

    ClusterApi apiInstance = new ClusterApi(defaultClient);
    String id = "me"; // String | ID of a Rubrik cluster object, or use *me* for the Rubrik cluster that is hosting the current API session.
    ClusterUpdate clusterUpdate = new ClusterUpdate(); // ClusterUpdate | Array that contains the changed information for the Rubrik cluster object.
    try {
      ClusterInfo result = apiInstance.updateCluster(id, clusterUpdate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClusterApi#updateCluster");
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
| **id** | **String**| ID of a Rubrik cluster object, or use *me* for the Rubrik cluster that is hosting the current API session. | [default to me] |
| **clusterUpdate** | [**ClusterUpdate**](ClusterUpdate.md)| Array that contains the changed information for the Rubrik cluster object. | |

### Return type

[**ClusterInfo**](ClusterInfo.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Updated information for a specified Rubrik cluster. |  -  |

<a id="updateCorsConfiguration"></a>
# **updateCorsConfiguration**
> CorsConfiguration updateCorsConfiguration(id, corsConfigurationPatch)

Update CORS configuration

Update the CORS support configuration for a web server.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClusterApi;

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

    ClusterApi apiInstance = new ClusterApi(defaultClient);
    String id = "me"; // String | ID of the Rubrik cluster or *me* for self.
    CorsConfigurationPatch corsConfigurationPatch = new CorsConfigurationPatch(); // CorsConfigurationPatch | CORS configuration.
    try {
      CorsConfiguration result = apiInstance.updateCorsConfiguration(id, corsConfigurationPatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClusterApi#updateCorsConfiguration");
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
| **id** | **String**| ID of the Rubrik cluster or *me* for self. | [default to me] |
| **corsConfigurationPatch** | [**CorsConfigurationPatch**](CorsConfigurationPatch.md)| CORS configuration. | |

### Return type

[**CorsConfiguration**](CorsConfiguration.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The updated CORS support configuration for a web server. |  -  |

<a id="updateFips"></a>
# **updateFips**
> FipsStatus updateFips(id, fipsStatusPatch)

Update FIPS enablement status

Update the current FIPS enablement status for a cluster.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClusterApi;

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

    ClusterApi apiInstance = new ClusterApi(defaultClient);
    String id = "me"; // String | ID of the Rubrik cluster or *me* for self.
    FipsStatusPatch fipsStatusPatch = new FipsStatusPatch(); // FipsStatusPatch | Update FIPS enablement status.
    try {
      FipsStatus result = apiInstance.updateFips(id, fipsStatusPatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClusterApi#updateFips");
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
| **id** | **String**| ID of the Rubrik cluster or *me* for self. | [default to me] |
| **fipsStatusPatch** | [**FipsStatusPatch**](FipsStatusPatch.md)| Update FIPS enablement status. | |

### Return type

[**FipsStatus**](FipsStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The current FIPS enablement status for a cluster. |  -  |

<a id="updateRubrikSupportPortalCredentials"></a>
# **updateRubrikSupportPortalCredentials**
> updateRubrikSupportPortalCredentials(id, communityUserCredentials)

Update credentials to the Rubrik support portal

Update credentials for the specified Rubrik cluster to connect to the Rubrik support portal. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClusterApi;

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

    ClusterApi apiInstance = new ClusterApi(defaultClient);
    String id = "me"; // String | The ID of a Rubrik cluster, or use *me* for the Rubrik cluster that is hosting the current session. 
    CommunityUserCredentials communityUserCredentials = new CommunityUserCredentials(); // CommunityUserCredentials | The credentials used to connect to the Rubrik support portal. 
    try {
      apiInstance.updateRubrikSupportPortalCredentials(id, communityUserCredentials);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClusterApi#updateRubrikSupportPortalCredentials");
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
| **id** | **String**| The ID of a Rubrik cluster, or use *me* for the Rubrik cluster that is hosting the current session.  | [default to me] |
| **communityUserCredentials** | [**CommunityUserCredentials**](CommunityUserCredentials.md)| The credentials used to connect to the Rubrik support portal.  | |

### Return type

null (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Successfully updated Rubrik support portal credentials.  |  -  |

<a id="updateSyslogExportRule"></a>
# **updateSyslogExportRule**
> SyslogExportRuleSummary updateSyslogExportRule(id, syslogExportRulePartial)

Update the specified syslog export rule

Update the syslog export rule specified by the given id.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClusterApi;

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

    ClusterApi apiInstance = new ClusterApi(defaultClient);
    String id = "id_example"; // String | The ID of syslog export rule.
    SyslogExportRulePartial syslogExportRulePartial = new SyslogExportRulePartial(); // SyslogExportRulePartial | Syslog export rule.
    try {
      SyslogExportRuleSummary result = apiInstance.updateSyslogExportRule(id, syslogExportRulePartial);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClusterApi#updateSyslogExportRule");
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
| **id** | **String**| The ID of syslog export rule. | |
| **syslogExportRulePartial** | [**SyslogExportRulePartial**](SyslogExportRulePartial.md)| Syslog export rule. | |

### Return type

[**SyslogExportRuleSummary**](SyslogExportRuleSummary.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Updated syslog export rule. |  -  |

<a id="updateTotpGlobalSetting"></a>
# **updateTotpGlobalSetting**
> TotpGlobalSetting updateTotpGlobalSetting(id, totpGlobalSettingUpdate)

Update TOTP global setting

Update TOTP global setting, including whether TOTP is enforced or not.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClusterApi;

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

    ClusterApi apiInstance = new ClusterApi(defaultClient);
    String id = "me"; // String | ID assigned to a Rubrik cluster. Use *me* to refer to the Rubrik cluster that is hosting the current API session.
    TotpGlobalSettingUpdate totpGlobalSettingUpdate = new TotpGlobalSettingUpdate(); // TotpGlobalSettingUpdate | 
    try {
      TotpGlobalSetting result = apiInstance.updateTotpGlobalSetting(id, totpGlobalSettingUpdate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClusterApi#updateTotpGlobalSetting");
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
| **id** | **String**| ID assigned to a Rubrik cluster. Use *me* to refer to the Rubrik cluster that is hosting the current API session. | [default to me] |
| **totpGlobalSettingUpdate** | [**TotpGlobalSettingUpdate**](TotpGlobalSettingUpdate.md)|  | |

### Return type

[**TotpGlobalSetting**](TotpGlobalSetting.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Updated TOTP global setting for the specified Rubrik cluster. |  -  |

