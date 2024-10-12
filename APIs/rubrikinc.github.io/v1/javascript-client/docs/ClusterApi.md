# RubrikRestApi.ClusterApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addKmipServer**](ClusterApi.md#addKmipServer) | **PUT** /cluster/{id}/security/kmip/server | Add a KMIP server
[**addSyslogExportRule**](ClusterApi.md#addSyslogExportRule) | **POST** /syslog/export | Add a new syslog export rule
[**availableVersion**](ClusterApi.md#availableVersion) | **GET** /cluster/{id}/upgrade/available_version | Retrieve CDM versions available for upgrade
[**changeClusterNodeHostnames**](ClusterApi.md#changeClusterNodeHostnames) | **POST** /cluster/{id}/node_hostname | Change hostname for nodes in a Rubrik cluster
[**deleteKmipServer**](ClusterApi.md#deleteKmipServer) | **DELETE** /cluster/{id}/security/kmip/server | Remove the specified KMIP server
[**deleteSyslogExportRule**](ClusterApi.md#deleteSyslogExportRule) | **DELETE** /syslog/export/{id} | Delete the specified syslog export rule
[**getAsyncRequestStatusForUpgrade**](ClusterApi.md#getAsyncRequestStatusForUpgrade) | **GET** /cluster/{id}/upgrade/request/{request_id} | Get asynchronous request details
[**getClusterApiVersion**](ClusterApi.md#getClusterApiVersion) | **GET** /cluster/{id}/api_version | Get cluster REST API version
[**getClusterCertificate**](ClusterApi.md#getClusterCertificate) | **GET** /cluster/{id}/certificate | Get the cluster certificate
[**getClusterNodeHostnames**](ClusterApi.md#getClusterNodeHostnames) | **GET** /cluster/{id}/node_hostname | Get the node ID to hostname mapping for all the nodes in a Rubrik cluster 
[**getClusterNodeIds**](ClusterApi.md#getClusterNodeIds) | **GET** /cluster/{id}/node_id | Get the name of the nodes in the cluster
[**getClusterVersion**](ClusterApi.md#getClusterVersion) | **GET** /cluster/{id}/version | Get cluster software version
[**getCorsConfiguration**](ClusterApi.md#getCorsConfiguration) | **GET** /cluster/{id}/security/cors | Get CORS configuration
[**getEncryptionStatus**](ClusterApi.md#getEncryptionStatus) | **GET** /cluster/{id}/security/encryption | Get encryption at rest status
[**getFips**](ClusterApi.md#getFips) | **GET** /cluster/{id}/security/fips | Get FIPS enablement status
[**getKmipClient**](ClusterApi.md#getKmipClient) | **GET** /cluster/{id}/security/kmip/client | Get the KMIP client configuration
[**getKmipServer**](ClusterApi.md#getKmipServer) | **GET** /cluster/{id}/security/kmip/server | Get KMIP server information
[**getPeriodicUpgradePrechecksStatus**](ClusterApi.md#getPeriodicUpgradePrechecksStatus) | **GET** /cluster/{id}/upgrade/precheck_status | Get the result of the latest run of the upgrade prechecks
[**getPublicClusterInfo**](ClusterApi.md#getPublicClusterInfo) | **GET** /cluster/{id} | Get cluster details
[**getRubrikSnmpMibDownloadLink**](ClusterApi.md#getRubrikSnmpMibDownloadLink) | **GET** /cluster/{id}/snmp_mib_link | Get the link for Rubrik SNMP MIB file
[**getSyslogExportRule**](ClusterApi.md#getSyslogExportRule) | **GET** /syslog/export/{id} | Get the specified syslog export rule
[**getSyslogExportRules**](ClusterApi.md#getSyslogExportRules) | **GET** /syslog/export | Get the configured syslog export rules
[**getSyslogMsgSnmpMibDownloadLink**](ClusterApi.md#getSyslogMsgSnmpMibDownloadLink) | **GET** /cluster/{id}/syslog_msg_mib_link | Get the link for SYSLOG-MSG-MIB file
[**getSyslogTcSnmpMibDownloadLink**](ClusterApi.md#getSyslogTcSnmpMibDownloadLink) | **GET** /cluster/{id}/syslog_tc_mib_link | Get the link for SYSLOG-TC-MIB file
[**getTotpGlobalSetting**](ClusterApi.md#getTotpGlobalSetting) | **GET** /cluster/{id}/security/totp/setting | Get global TOTP setting
[**getTruststores**](ClusterApi.md#getTruststores) | **GET** /cluster/{id}/security/truststore | Get summary of all truststores
[**getWebSignedCertificate**](ClusterApi.md#getWebSignedCertificate) | **GET** /cluster/{id}/security/web_signed_cert | Get the signed certificate for Web server
[**hasRubrikSupportPortalCredentials**](ClusterApi.md#hasRubrikSupportPortalCredentials) | **GET** /cluster/{id}/rubrik_support_portal_credentials | Check credentials to the Rubrik support portal
[**manualDiscover**](ClusterApi.md#manualDiscover) | **POST** /cluster/{id}/manual_discover | Manually discover nodes
[**manualDiscoverIpv4**](ClusterApi.md#manualDiscoverIpv4) | **POST** /cluster/{id}/manual_discover_ipv4 | Manually discover nodes over IPv4 address
[**monitorEvents**](ClusterApi.md#monitorEvents) | **GET** /cluster/me/upgrade/monitor_events | Get event notifications
[**patchPasswordRequirements**](ClusterApi.md#patchPasswordRequirements) | **PATCH** /cluster/{id}/security/password_requirements | Set password requirements
[**queryPasswordRequirements**](ClusterApi.md#queryPasswordRequirements) | **GET** /cluster/{id}/security/password_requirements | Get password requirements
[**resetWebSignedCertificate**](ClusterApi.md#resetWebSignedCertificate) | **DELETE** /cluster/{id}/security/web_signed_cert | Reset the signed certificate for Web server
[**runPeriodicUpgradePrechecks**](ClusterApi.md#runPeriodicUpgradePrechecks) | **POST** /cluster/{id}/upgrade/precheck_status | Start an on demand run of the prechecks
[**setKmipClient**](ClusterApi.md#setKmipClient) | **PUT** /cluster/{id}/security/kmip/client | Specify KMIP client credentials for nodes
[**setTruststoreCertificate**](ClusterApi.md#setTruststoreCertificate) | **PATCH** /cluster/{id}/security/truststore | Set certificates for one or more truststores
[**setWebSignedCertificate**](ClusterApi.md#setWebSignedCertificate) | **PUT** /cluster/{id}/security/web_signed_cert | Set a signed certificate for Web server
[**stageCdmSoftware**](ClusterApi.md#stageCdmSoftware) | **POST** /cluster/{id}/upgrade/stage_cdm_software | Stage software on CDM for upgrade
[**testSyslogExportRule**](ClusterApi.md#testSyslogExportRule) | **POST** /syslog/export/test | Test the specified syslog export rule
[**unsetTruststoreCertificate**](ClusterApi.md#unsetTruststoreCertificate) | **DELETE** /cluster/{id}/security/truststore | Remove certificate associated with specified truststore
[**updateCluster**](ClusterApi.md#updateCluster) | **PATCH** /cluster/{id} | Change Rubrik cluster properties
[**updateCorsConfiguration**](ClusterApi.md#updateCorsConfiguration) | **PATCH** /cluster/{id}/security/cors | Update CORS configuration
[**updateFips**](ClusterApi.md#updateFips) | **PATCH** /cluster/{id}/security/fips | Update FIPS enablement status
[**updateRubrikSupportPortalCredentials**](ClusterApi.md#updateRubrikSupportPortalCredentials) | **POST** /cluster/{id}/rubrik_support_portal_credentials | Update credentials to the Rubrik support portal
[**updateSyslogExportRule**](ClusterApi.md#updateSyslogExportRule) | **PATCH** /syslog/export/{id} | Update the specified syslog export rule
[**updateTotpGlobalSetting**](ClusterApi.md#updateTotpGlobalSetting) | **PUT** /cluster/{id}/security/totp/setting | Update TOTP global setting



## addKmipServer

> AsyncRequestStatus addKmipServer(id, kmipServerConfiguration)

Add a KMIP server

Add the specified KMIP server to the set of active KMIP servers.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.ClusterApi();
let id = "'me'"; // String | ID assigned to a Rubrik cluster. Use *me* to refer to the Rubrik cluster that is hosting the current API session.
let kmipServerConfiguration = new RubrikRestApi.KmipServerConfiguration(); // KmipServerConfiguration | Object containing the configuration details for a KMIP server.
apiInstance.addKmipServer(id, kmipServerConfiguration, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| ID assigned to a Rubrik cluster. Use *me* to refer to the Rubrik cluster that is hosting the current API session. | [default to &#39;me&#39;]
 **kmipServerConfiguration** | [**KmipServerConfiguration**](KmipServerConfiguration.md)| Object containing the configuration details for a KMIP server. | 

### Return type

[**AsyncRequestStatus**](AsyncRequestStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## addSyslogExportRule

> SyslogExportRuleSummary addSyslogExportRule(syslogExportRuleFull)

Add a new syslog export rule

Adds a new rule specifying where to export the specified syslog information. 

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.ClusterApi();
let syslogExportRuleFull = new RubrikRestApi.SyslogExportRuleFull(); // SyslogExportRuleFull | Syslog export rule.
apiInstance.addSyslogExportRule(syslogExportRuleFull, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **syslogExportRuleFull** | [**SyslogExportRuleFull**](SyslogExportRuleFull.md)| Syslog export rule. | 

### Return type

[**SyslogExportRuleSummary**](SyslogExportRuleSummary.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## availableVersion

> [AvailableVersionInfo] availableVersion(id, opts)

Retrieve CDM versions available for upgrade

Retrieve a list of Rubrik CDM versions available to upgrade the Rubrik cluster.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.ClusterApi();
let id = "'me'"; // String | The ID of the Rubrik cluster. To query the local cluster, use *me*.
let opts = {
  'filterVersion': "filterVersion_example", // String | A string that filters the results based on the prefix. For example, the string \"5.1\" filters all releases in the 5.1 family. If more than one result is desired then this parameter can be used in conjunction with the `show_all` parameter.
  'fetchLinks': false, // Boolean | Include a download URL for the single version passed in the 'filter_version' parameter. A link response will not be provided if the chosen version is locally available, or if 'filter_version' is not specified. 
  'sourceVersion': "sourceVersion_example", // String | The source version of Rubrik CDM used for the upgradeability check if 'filter_upgradable' if specified. If 'filter_upgradable' is not specified, this parameter is ignored. 
  'ignoreLocal': false, // Boolean | If specified, ignore locally available versions.
  'ignoreRemote': false, // Boolean | If specified, ignore versions available in the Rubrik remote central repository. 
  'ignoreDownloading': true, // Boolean | If specified, ignore versions currently being downloaded.
  'downloadJobInstanceId': "downloadJobInstanceId_example", // String | If specified, filter results for downloading versions to the provided job instance ID. 
  'filterUpgradable': true, // Boolean | When this parameter is set, the query only returns versions of the Rubrik CDM that can be upgraded to from the version specified in the 'source_version' parameter. If 'source_version' is not specified, we use the cluster version as the source_version. 
  'showAll': false // Boolean | When this parameter is set, the query shows all patch releases including releases with a newer version released in the same family. When set to false, the query returns only the latest version from each release family. 
};
apiInstance.availableVersion(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| The ID of the Rubrik cluster. To query the local cluster, use *me*. | [default to &#39;me&#39;]
 **filterVersion** | **String**| A string that filters the results based on the prefix. For example, the string \&quot;5.1\&quot; filters all releases in the 5.1 family. If more than one result is desired then this parameter can be used in conjunction with the &#x60;show_all&#x60; parameter. | [optional] 
 **fetchLinks** | **Boolean**| Include a download URL for the single version passed in the &#39;filter_version&#39; parameter. A link response will not be provided if the chosen version is locally available, or if &#39;filter_version&#39; is not specified.  | [optional] [default to false]
 **sourceVersion** | **String**| The source version of Rubrik CDM used for the upgradeability check if &#39;filter_upgradable&#39; if specified. If &#39;filter_upgradable&#39; is not specified, this parameter is ignored.  | [optional] 
 **ignoreLocal** | **Boolean**| If specified, ignore locally available versions. | [optional] [default to false]
 **ignoreRemote** | **Boolean**| If specified, ignore versions available in the Rubrik remote central repository.  | [optional] [default to false]
 **ignoreDownloading** | **Boolean**| If specified, ignore versions currently being downloaded. | [optional] [default to true]
 **downloadJobInstanceId** | **String**| If specified, filter results for downloading versions to the provided job instance ID.  | [optional] 
 **filterUpgradable** | **Boolean**| When this parameter is set, the query only returns versions of the Rubrik CDM that can be upgraded to from the version specified in the &#39;source_version&#39; parameter. If &#39;source_version&#39; is not specified, we use the cluster version as the source_version.  | [optional] [default to true]
 **showAll** | **Boolean**| When this parameter is set, the query shows all patch releases including releases with a newer version released in the same family. When set to false, the query returns only the latest version from each release family.  | [optional] [default to false]

### Return type

[**[AvailableVersionInfo]**](AvailableVersionInfo.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## changeClusterNodeHostnames

> changeClusterNodeHostnames(id, nodeHostnameInfo)

Change hostname for nodes in a Rubrik cluster

Change hostnames for multiple nodes at a time, for a specified Rubrik cluster. 

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.ClusterApi();
let id = "'me'"; // String | ID of the Rubrik cluster or *me* for self.
let nodeHostnameInfo = [new RubrikRestApi.NodeHostnameInfo()]; // [NodeHostnameInfo] | Node ID to hostname mapping.
apiInstance.changeClusterNodeHostnames(id, nodeHostnameInfo, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| ID of the Rubrik cluster or *me* for self. | [default to &#39;me&#39;]
 **nodeHostnameInfo** | [**[NodeHostnameInfo]**](NodeHostnameInfo.md)| Node ID to hostname mapping. | 

### Return type

null (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## deleteKmipServer

> AsyncRequestStatus deleteKmipServer(id, serverAddress)

Remove the specified KMIP server

Remove the server with the specified server address from the set of active KMIP servers.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.ClusterApi();
let id = "'me'"; // String | ID assigned to a Rubrik cluster. Use *me* to refer to the Rubrik cluster that is hosting the current API session.
let serverAddress = "serverAddress_example"; // String | IPv4 address or FQDN (fully qualified domain name) of the KMIP server.
apiInstance.deleteKmipServer(id, serverAddress, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| ID assigned to a Rubrik cluster. Use *me* to refer to the Rubrik cluster that is hosting the current API session. | [default to &#39;me&#39;]
 **serverAddress** | **String**| IPv4 address or FQDN (fully qualified domain name) of the KMIP server. | 

### Return type

[**AsyncRequestStatus**](AsyncRequestStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteSyslogExportRule

> deleteSyslogExportRule(id)

Delete the specified syslog export rule

Delete the syslog export rule specified by the given id.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.ClusterApi();
let id = "id_example"; // String | The ID of the syslog export rule.
apiInstance.deleteSyslogExportRule(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| The ID of the syslog export rule. | 

### Return type

null (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getAsyncRequestStatusForUpgrade

> AsyncRequestStatus getAsyncRequestStatusForUpgrade(id, requestId)

Get asynchronous request details

Get asynchronous request details for an upgrade request.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.ClusterApi();
let id = "'me'"; // String | ID of the Rubrik cluster or *me* for self.
let requestId = "requestId_example"; // String | ID of the request.
apiInstance.getAsyncRequestStatusForUpgrade(id, requestId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| ID of the Rubrik cluster or *me* for self. | [default to &#39;me&#39;]
 **requestId** | **String**| ID of the request. | 

### Return type

[**AsyncRequestStatus**](AsyncRequestStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getClusterApiVersion

> ClusterApiVersion getClusterApiVersion(id)

Get cluster REST API version

Retrieves software version of the Rubrik cluster.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';

let apiInstance = new RubrikRestApi.ClusterApi();
let id = "'me'"; // String | ID of the Rubrik cluster or *me* for self.
apiInstance.getClusterApiVersion(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| ID of the Rubrik cluster or *me* for self. | [default to &#39;me&#39;]

### Return type

[**ClusterApiVersion**](ClusterApiVersion.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getClusterCertificate

> ClusterCertificate getClusterCertificate(id)

Get the cluster certificate

Returns the cluster certificate.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.ClusterApi();
let id = "'me'"; // String | ID of the Rubrik cluster or *me* for self.
apiInstance.getClusterCertificate(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| ID of the Rubrik cluster or *me* for self. | [default to &#39;me&#39;]

### Return type

[**ClusterCertificate**](ClusterCertificate.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getClusterNodeHostnames

> NodeHostnameInfoListResponse getClusterNodeHostnames(id)

Get the node ID to hostname mapping for all the nodes in a Rubrik cluster 

Retrieve the ID to hostname mapping for all the nodes that belong to a specified Rubrik cluster. 

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.ClusterApi();
let id = "'me'"; // String | ID of the Rubrik cluster or *me* for self.
apiInstance.getClusterNodeHostnames(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| ID of the Rubrik cluster or *me* for self. | [default to &#39;me&#39;]

### Return type

[**NodeHostnameInfoListResponse**](NodeHostnameInfoListResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getClusterNodeIds

> [NodeId] getClusterNodeIds(id)

Get the name of the nodes in the cluster

Retrieve the list of node IDs for the nodes in this Rubrik CDM cluster.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.ClusterApi();
let id = "'me'"; // String | ID of the Rubrik cluster or *me* for self.
apiInstance.getClusterNodeIds(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| ID of the Rubrik cluster or *me* for self. | [default to &#39;me&#39;]

### Return type

[**[NodeId]**](NodeId.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getClusterVersion

> ClusterVersion getClusterVersion(id)

Get cluster software version

Retrieves software version of the Rubrik cluster.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';

let apiInstance = new RubrikRestApi.ClusterApi();
let id = "'me'"; // String | ID of the Rubrik cluster or *me* for self.
apiInstance.getClusterVersion(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| ID of the Rubrik cluster or *me* for self. | [default to &#39;me&#39;]

### Return type

[**ClusterVersion**](ClusterVersion.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getCorsConfiguration

> CorsConfiguration getCorsConfiguration(id)

Get CORS configuration

Get the current CORS support configuration for a web server.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.ClusterApi();
let id = "'me'"; // String | ID of the Rubrik cluster or *me* for self.
apiInstance.getCorsConfiguration(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| ID of the Rubrik cluster or *me* for self. | [default to &#39;me&#39;]

### Return type

[**CorsConfiguration**](CorsConfiguration.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getEncryptionStatus

> EncryptionStatus getEncryptionStatus(id)

Get encryption at rest status

Get the current encryption at rest status of the cluster.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.ClusterApi();
let id = "'me'"; // String | ID of the Rubrik cluster or *me* for self.
apiInstance.getEncryptionStatus(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| ID of the Rubrik cluster or *me* for self. | [default to &#39;me&#39;]

### Return type

[**EncryptionStatus**](EncryptionStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getFips

> FipsStatus getFips(id)

Get FIPS enablement status

Returns the current status of FIPS on the specified cluster. When the status is true, FIPS is enabled.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.ClusterApi();
let id = "'me'"; // String | ID of the Rubrik cluster or *me* for self.
apiInstance.getFips(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| ID of the Rubrik cluster or *me* for self. | [default to &#39;me&#39;]

### Return type

[**FipsStatus**](FipsStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getKmipClient

> KmipClientDetail getKmipClient(id)

Get the KMIP client configuration

Return the currently configured KMIP client information. The response object contains empty fields when KMIP is not configured.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.ClusterApi();
let id = "'me'"; // String | ID assigned to a Rubrik cluster. Use *me* to refer to the Rubrik cluster that is hosting the current API session.
apiInstance.getKmipClient(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| ID assigned to a Rubrik cluster. Use *me* to refer to the Rubrik cluster that is hosting the current API session. | [default to &#39;me&#39;]

### Return type

[**KmipClientDetail**](KmipClientDetail.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getKmipServer

> [KmipServerDetail] getKmipServer(id, opts)

Get KMIP server information

Returns the KMIP server information for the specified server address. When no server address is specified, this call returns information on all active KMIP servers. The response array is empty when KMIP is not configured or when the server address cannot be found.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.ClusterApi();
let id = "'me'"; // String | ID assigned to a Rubrik cluster. Use *me* to refer to the Rubrik cluster that is hosting the current API session.
let opts = {
  'serverAddress': "serverAddress_example" // String | The address of the KMIP server.
};
apiInstance.getKmipServer(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| ID assigned to a Rubrik cluster. Use *me* to refer to the Rubrik cluster that is hosting the current API session. | [default to &#39;me&#39;]
 **serverAddress** | **String**| The address of the KMIP server. | [optional] 

### Return type

[**[KmipServerDetail]**](KmipServerDetail.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPeriodicUpgradePrechecksStatus

> PrecheckStatusResponse getPeriodicUpgradePrechecksStatus(id, opts)

Get the result of the latest run of the upgrade prechecks

Get the result of the latest run of the upgrade prechecks. 

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.ClusterApi();
let id = "'me'"; // String | ID of the Rubrik cluster or *me* for self.
let opts = {
  'fetchNextRunInfo': false // Boolean | If specified, fetch information corresponding to next upgrade prechecks job instance. If an upgrade prechecks job instance is currently running, results corresponding to it are returned. 
};
apiInstance.getPeriodicUpgradePrechecksStatus(id, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| ID of the Rubrik cluster or *me* for self. | [default to &#39;me&#39;]
 **fetchNextRunInfo** | **Boolean**| If specified, fetch information corresponding to next upgrade prechecks job instance. If an upgrade prechecks job instance is currently running, results corresponding to it are returned.  | [optional] [default to false]

### Return type

[**PrecheckStatusResponse**](PrecheckStatusResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPublicClusterInfo

> ClusterInfo getPublicClusterInfo(id)

Get cluster details

Retrieve public information about the Rubrik cluster.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.ClusterApi();
let id = "'me'"; // String | ID of the Rubrik cluster or *me* for self.
apiInstance.getPublicClusterInfo(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| ID of the Rubrik cluster or *me* for self. | [default to &#39;me&#39;]

### Return type

[**ClusterInfo**](ClusterInfo.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getRubrikSnmpMibDownloadLink

> RubrikMibFileDownloadLink getRubrikSnmpMibDownloadLink(id)

Get the link for Rubrik SNMP MIB file

Retrieve the download link for the Rubrik SNMP MIB file. The retrieval is a synchronous operation.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.ClusterApi();
let id = "'me'"; // String | ID of the Rubrik cluster or *me* for self.
apiInstance.getRubrikSnmpMibDownloadLink(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| ID of the Rubrik cluster or *me* for self. | [default to &#39;me&#39;]

### Return type

[**RubrikMibFileDownloadLink**](RubrikMibFileDownloadLink.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSyslogExportRule

> SyslogExportRuleSummary getSyslogExportRule(id)

Get the specified syslog export rule

Get the summary of the syslog export rule specified by the given id. 

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.ClusterApi();
let id = "id_example"; // String | The ID of syslog export rule.
apiInstance.getSyslogExportRule(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| The ID of syslog export rule. | 

### Return type

[**SyslogExportRuleSummary**](SyslogExportRuleSummary.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSyslogExportRules

> SyslogExportRuleSummaryListResponse getSyslogExportRules()

Get the configured syslog export rules

Return the list of all configured syslog export rules.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.ClusterApi();
apiInstance.getSyslogExportRules((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
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


## getSyslogMsgSnmpMibDownloadLink

> SyslogMsgMibFileDownloadLink getSyslogMsgSnmpMibDownloadLink(id)

Get the link for SYSLOG-MSG-MIB file

Retrieve the download link for the SYSLOG-MSG-MIB file. The retrieval is a synchronous operation.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.ClusterApi();
let id = "'me'"; // String | ID of the Rubrik cluster or *me* for self.
apiInstance.getSyslogMsgSnmpMibDownloadLink(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| ID of the Rubrik cluster or *me* for self. | [default to &#39;me&#39;]

### Return type

[**SyslogMsgMibFileDownloadLink**](SyslogMsgMibFileDownloadLink.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSyslogTcSnmpMibDownloadLink

> SyslogTcMibFileDownloadLink getSyslogTcSnmpMibDownloadLink(id)

Get the link for SYSLOG-TC-MIB file

Retrieve the download link for the SYSLOG-TC-MIB file. The retrieval is a synchronous operation.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.ClusterApi();
let id = "'me'"; // String | ID of the Rubrik cluster or *me* for self.
apiInstance.getSyslogTcSnmpMibDownloadLink(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| ID of the Rubrik cluster or *me* for self. | [default to &#39;me&#39;]

### Return type

[**SyslogTcMibFileDownloadLink**](SyslogTcMibFileDownloadLink.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTotpGlobalSetting

> TotpGlobalSetting getTotpGlobalSetting(id)

Get global TOTP setting

Returns TOTP global setting, including whether TOTP is enforced or not.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.ClusterApi();
let id = "'me'"; // String | ID assigned to a Rubrik cluster. Use *me* to refer to the Rubrik cluster that is hosting the current API session.
apiInstance.getTotpGlobalSetting(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| ID assigned to a Rubrik cluster. Use *me* to refer to the Rubrik cluster that is hosting the current API session. | [default to &#39;me&#39;]

### Return type

[**TotpGlobalSetting**](TotpGlobalSetting.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTruststores

> TruststoreSummaryListResponse getTruststores(id)

Get summary of all truststores

Get summary of all truststores.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.ClusterApi();
let id = "'me'"; // String | ID of the Rubrik cluster or *me* for self.
apiInstance.getTruststores(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| ID of the Rubrik cluster or *me* for self. | [default to &#39;me&#39;]

### Return type

[**TruststoreSummaryListResponse**](TruststoreSummaryListResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getWebSignedCertificate

> WebServerCertificateSummary getWebSignedCertificate(id)

Get the signed certificate for Web server

If the web server uses a signed certificate, fetch it.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.ClusterApi();
let id = "'me'"; // String | ID of the Rubrik cluster or *me* for self.
apiInstance.getWebSignedCertificate(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| ID of the Rubrik cluster or *me* for self. | [default to &#39;me&#39;]

### Return type

[**WebServerCertificateSummary**](WebServerCertificateSummary.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## hasRubrikSupportPortalCredentials

> BooleanResponse hasRubrikSupportPortalCredentials(id)

Check credentials to the Rubrik support portal

Check whether the specified Rubrik cluster has an existing set of credentials for the Rubrik support portal. 

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.ClusterApi();
let id = "'me'"; // String | The ID of a Rubrik cluster, or use *me* for the Rubrik cluster that is hosting the current session. 
apiInstance.hasRubrikSupportPortalCredentials(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| The ID of a Rubrik cluster, or use *me* for the Rubrik cluster that is hosting the current session.  | [default to &#39;me&#39;]

### Return type

[**BooleanResponse**](BooleanResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## manualDiscover

> ManualDiscoveryNodeInfo manualDiscover(id, manualDiscoveryNodeInfo)

Manually discover nodes

Manually specifies mDNS discovery data. Output for this endpoint is identical to the output of the &#39;discover&#39; endpoint.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.ClusterApi();
let id = "'me'"; // String | ID of the Rubrik cluster or *me* for self.
let manualDiscoveryNodeInfo = new RubrikRestApi.ManualDiscoveryNodeInfo(); // ManualDiscoveryNodeInfo | Manual discovery input data.
apiInstance.manualDiscover(id, manualDiscoveryNodeInfo, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| ID of the Rubrik cluster or *me* for self. | [default to &#39;me&#39;]
 **manualDiscoveryNodeInfo** | [**ManualDiscoveryNodeInfo**](ManualDiscoveryNodeInfo.md)| Manual discovery input data. | 

### Return type

[**ManualDiscoveryNodeInfo**](ManualDiscoveryNodeInfo.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## manualDiscoverIpv4

> ManualDiscoveryNodeIpv4Info manualDiscoverIpv4(id, manualDiscoveryNodeIpv4Info)

Manually discover nodes over IPv4 address

Manually specifies discovery data. This endpoint output is identical to the output of the &#39;discover&#39; endpoint.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.ClusterApi();
let id = "'me'"; // String | ID of the Rubrik cluster, or *me* for the current cluster.
let manualDiscoveryNodeIpv4Info = new RubrikRestApi.ManualDiscoveryNodeIpv4Info(); // ManualDiscoveryNodeIpv4Info | Manual discovery input data.
apiInstance.manualDiscoverIpv4(id, manualDiscoveryNodeIpv4Info, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| ID of the Rubrik cluster, or *me* for the current cluster. | [default to &#39;me&#39;]
 **manualDiscoveryNodeIpv4Info** | [**ManualDiscoveryNodeIpv4Info**](ManualDiscoveryNodeIpv4Info.md)| Manual discovery input data. | 

### Return type

[**ManualDiscoveryNodeIpv4Info**](ManualDiscoveryNodeIpv4Info.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## monitorEvents

> [EventNotification] monitorEvents(eventNotificationQuery)

Get event notifications

Gets notifications about events from a specified set of possible events. 

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.ClusterApi();
let eventNotificationQuery = ["null"]; // [String] | Specifies a list of events to monitor for notifications.
apiInstance.monitorEvents(eventNotificationQuery, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **eventNotificationQuery** | [**[String]**](String.md)| Specifies a list of events to monitor for notifications. | 

### Return type

[**[EventNotification]**](EventNotification.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## patchPasswordRequirements

> PasswordRequirementsSummary patchPasswordRequirements(id, passwordRequirementsPatchRequest)

Set password requirements

Update user password requirements for a cluster.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.ClusterApi();
let id = "'me'"; // String | ID of the Rubrik cluster or *me* for self.
let passwordRequirementsPatchRequest = new RubrikRestApi.PasswordRequirementsPatchRequest(); // PasswordRequirementsPatchRequest | Password requirements.
apiInstance.patchPasswordRequirements(id, passwordRequirementsPatchRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| ID of the Rubrik cluster or *me* for self. | [default to &#39;me&#39;]
 **passwordRequirementsPatchRequest** | [**PasswordRequirementsPatchRequest**](PasswordRequirementsPatchRequest.md)| Password requirements. | 

### Return type

[**PasswordRequirementsSummary**](PasswordRequirementsSummary.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## queryPasswordRequirements

> PasswordRequirementsSummary queryPasswordRequirements(id)

Get password requirements

Query user password requirements for a cluster.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.ClusterApi();
let id = "'me'"; // String | ID of the Rubrik cluster or *me* for self.
apiInstance.queryPasswordRequirements(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| ID of the Rubrik cluster or *me* for self. | [default to &#39;me&#39;]

### Return type

[**PasswordRequirementsSummary**](PasswordRequirementsSummary.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## resetWebSignedCertificate

> AsyncRequestStatus resetWebSignedCertificate(id)

Reset the signed certificate for Web server

Resetting the customer-given certificate for each node&#39;s web server.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.ClusterApi();
let id = "'me'"; // String | ID of the Rubrik cluster or *me* for self.
apiInstance.resetWebSignedCertificate(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| ID of the Rubrik cluster or *me* for self. | [default to &#39;me&#39;]

### Return type

[**AsyncRequestStatus**](AsyncRequestStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## runPeriodicUpgradePrechecks

> AsyncRequestStatus runPeriodicUpgradePrechecks(id)

Start an on demand run of the prechecks

Start an on demand run of the prechecks. 

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.ClusterApi();
let id = "'me'"; // String | ID of the Rubrik cluster or *me* for self.
apiInstance.runPeriodicUpgradePrechecks(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| ID of the Rubrik cluster or *me* for self. | [default to &#39;me&#39;]

### Return type

[**AsyncRequestStatus**](AsyncRequestStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## setKmipClient

> AsyncRequestStatus setKmipClient(id, kmipClientConfiguration)

Specify KMIP client credentials for nodes

Specify KMIP client credentials for each of the Rubrik cluster nodes.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.ClusterApi();
let id = "'me'"; // String | ID assigned to a Rubrik cluster. Use *me* to refer to the Rubrik cluster that is hosting the current API session.
let kmipClientConfiguration = new RubrikRestApi.KmipClientConfiguration(); // KmipClientConfiguration | KMIP client configuration.
apiInstance.setKmipClient(id, kmipClientConfiguration, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| ID assigned to a Rubrik cluster. Use *me* to refer to the Rubrik cluster that is hosting the current API session. | [default to &#39;me&#39;]
 **kmipClientConfiguration** | [**KmipClientConfiguration**](KmipClientConfiguration.md)| KMIP client configuration. | 

### Return type

[**AsyncRequestStatus**](AsyncRequestStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## setTruststoreCertificate

> setTruststoreCertificate(id, truststorePayload)

Set certificates for one or more truststores

Setting the given certificate for each node&#39;s truststores.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.ClusterApi();
let id = "'me'"; // String | ID of the Rubrik cluster or *me* for self.
let truststorePayload = [new RubrikRestApi.TruststorePayload()]; // [TruststorePayload] | Request to update certificate for truststore.
apiInstance.setTruststoreCertificate(id, truststorePayload, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| ID of the Rubrik cluster or *me* for self. | [default to &#39;me&#39;]
 **truststorePayload** | [**[TruststorePayload]**](TruststorePayload.md)| Request to update certificate for truststore. | 

### Return type

null (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## setWebSignedCertificate

> AsyncRequestStatus setWebSignedCertificate(id, webServerCertificatePayload)

Set a signed certificate for Web server

Setting the given certificate for each node&#39;s web server to use.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.ClusterApi();
let id = "'me'"; // String | ID of the Rubrik cluster or *me* for self.
let webServerCertificatePayload = new RubrikRestApi.WebServerCertificatePayload(); // WebServerCertificatePayload | Request to update certificate for web server.
apiInstance.setWebSignedCertificate(id, webServerCertificatePayload, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| ID of the Rubrik cluster or *me* for self. | [default to &#39;me&#39;]
 **webServerCertificatePayload** | [**WebServerCertificatePayload**](WebServerCertificatePayload.md)| Request to update certificate for web server. | 

### Return type

[**AsyncRequestStatus**](AsyncRequestStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## stageCdmSoftware

> AsyncRequestStatus stageCdmSoftware(id, stageCdmSoftwareInfo)

Stage software on CDM for upgrade

Stage software corresponding to a given CDM version on the cluster, in preparation for an upgrade.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.ClusterApi();
let id = "'me'"; // String | ID of the Rubrik cluster or *me* for self.
let stageCdmSoftwareInfo = new RubrikRestApi.StageCdmSoftwareInfo(); // StageCdmSoftwareInfo | Information about the provided CDM software package.
apiInstance.stageCdmSoftware(id, stageCdmSoftwareInfo, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| ID of the Rubrik cluster or *me* for self. | [default to &#39;me&#39;]
 **stageCdmSoftwareInfo** | [**StageCdmSoftwareInfo**](StageCdmSoftwareInfo.md)| Information about the provided CDM software package. | 

### Return type

[**AsyncRequestStatus**](AsyncRequestStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## testSyslogExportRule

> SyslogServerTestResult testSyslogExportRule(syslogExportRuleFull)

Test the specified syslog export rule

Send a test message using the syslog export rule specified by the given id. 

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.ClusterApi();
let syslogExportRuleFull = new RubrikRestApi.SyslogExportRuleFull(); // SyslogExportRuleFull | Syslog export rule.
apiInstance.testSyslogExportRule(syslogExportRuleFull, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **syslogExportRuleFull** | [**SyslogExportRuleFull**](SyslogExportRuleFull.md)| Syslog export rule. | 

### Return type

[**SyslogServerTestResult**](SyslogServerTestResult.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## unsetTruststoreCertificate

> unsetTruststoreCertificate(id, truststores)

Remove certificate associated with specified truststore

Remove certificate associated with specified truststore.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.ClusterApi();
let id = "'me'"; // String | ID of the Rubrik cluster or *me* for self.
let truststores = ["null"]; // [String] | Comma separated list of truststore types.
apiInstance.unsetTruststoreCertificate(id, truststores, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| ID of the Rubrik cluster or *me* for self. | [default to &#39;me&#39;]
 **truststores** | [**[String]**](String.md)| Comma separated list of truststore types. | 

### Return type

null (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## updateCluster

> ClusterInfo updateCluster(id, clusterUpdate)

Change Rubrik cluster properties

Change the properties of a specified Rubrik cluster. Changes to cluster name could take upto 10 minutes to be propagated to all nodes.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.ClusterApi();
let id = "'me'"; // String | ID of a Rubrik cluster object, or use *me* for the Rubrik cluster that is hosting the current API session.
let clusterUpdate = new RubrikRestApi.ClusterUpdate(); // ClusterUpdate | Array that contains the changed information for the Rubrik cluster object.
apiInstance.updateCluster(id, clusterUpdate, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| ID of a Rubrik cluster object, or use *me* for the Rubrik cluster that is hosting the current API session. | [default to &#39;me&#39;]
 **clusterUpdate** | [**ClusterUpdate**](ClusterUpdate.md)| Array that contains the changed information for the Rubrik cluster object. | 

### Return type

[**ClusterInfo**](ClusterInfo.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateCorsConfiguration

> CorsConfiguration updateCorsConfiguration(id, corsConfigurationPatch)

Update CORS configuration

Update the CORS support configuration for a web server.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.ClusterApi();
let id = "'me'"; // String | ID of the Rubrik cluster or *me* for self.
let corsConfigurationPatch = new RubrikRestApi.CorsConfigurationPatch(); // CorsConfigurationPatch | CORS configuration.
apiInstance.updateCorsConfiguration(id, corsConfigurationPatch, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| ID of the Rubrik cluster or *me* for self. | [default to &#39;me&#39;]
 **corsConfigurationPatch** | [**CorsConfigurationPatch**](CorsConfigurationPatch.md)| CORS configuration. | 

### Return type

[**CorsConfiguration**](CorsConfiguration.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateFips

> FipsStatus updateFips(id, fipsStatusPatch)

Update FIPS enablement status

Update the current FIPS enablement status for a cluster.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.ClusterApi();
let id = "'me'"; // String | ID of the Rubrik cluster or *me* for self.
let fipsStatusPatch = new RubrikRestApi.FipsStatusPatch(); // FipsStatusPatch | Update FIPS enablement status.
apiInstance.updateFips(id, fipsStatusPatch, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| ID of the Rubrik cluster or *me* for self. | [default to &#39;me&#39;]
 **fipsStatusPatch** | [**FipsStatusPatch**](FipsStatusPatch.md)| Update FIPS enablement status. | 

### Return type

[**FipsStatus**](FipsStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateRubrikSupportPortalCredentials

> updateRubrikSupportPortalCredentials(id, communityUserCredentials)

Update credentials to the Rubrik support portal

Update credentials for the specified Rubrik cluster to connect to the Rubrik support portal. 

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.ClusterApi();
let id = "'me'"; // String | The ID of a Rubrik cluster, or use *me* for the Rubrik cluster that is hosting the current session. 
let communityUserCredentials = new RubrikRestApi.CommunityUserCredentials(); // CommunityUserCredentials | The credentials used to connect to the Rubrik support portal. 
apiInstance.updateRubrikSupportPortalCredentials(id, communityUserCredentials, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| The ID of a Rubrik cluster, or use *me* for the Rubrik cluster that is hosting the current session.  | [default to &#39;me&#39;]
 **communityUserCredentials** | [**CommunityUserCredentials**](CommunityUserCredentials.md)| The credentials used to connect to the Rubrik support portal.  | 

### Return type

null (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## updateSyslogExportRule

> SyslogExportRuleSummary updateSyslogExportRule(id, syslogExportRulePartial)

Update the specified syslog export rule

Update the syslog export rule specified by the given id.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.ClusterApi();
let id = "id_example"; // String | The ID of syslog export rule.
let syslogExportRulePartial = new RubrikRestApi.SyslogExportRulePartial(); // SyslogExportRulePartial | Syslog export rule.
apiInstance.updateSyslogExportRule(id, syslogExportRulePartial, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| The ID of syslog export rule. | 
 **syslogExportRulePartial** | [**SyslogExportRulePartial**](SyslogExportRulePartial.md)| Syslog export rule. | 

### Return type

[**SyslogExportRuleSummary**](SyslogExportRuleSummary.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateTotpGlobalSetting

> TotpGlobalSetting updateTotpGlobalSetting(id, totpGlobalSettingUpdate)

Update TOTP global setting

Update TOTP global setting, including whether TOTP is enforced or not.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.ClusterApi();
let id = "'me'"; // String | ID assigned to a Rubrik cluster. Use *me* to refer to the Rubrik cluster that is hosting the current API session.
let totpGlobalSettingUpdate = new RubrikRestApi.TotpGlobalSettingUpdate(); // TotpGlobalSettingUpdate | 
apiInstance.updateTotpGlobalSetting(id, totpGlobalSettingUpdate, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| ID assigned to a Rubrik cluster. Use *me* to refer to the Rubrik cluster that is hosting the current API session. | [default to &#39;me&#39;]
 **totpGlobalSettingUpdate** | [**TotpGlobalSettingUpdate**](TotpGlobalSettingUpdate.md)|  | 

### Return type

[**TotpGlobalSetting**](TotpGlobalSetting.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

