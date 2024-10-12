# PublicApi.LinuxHostingsApi

All URIs are relative to */v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addScheduledTasks**](LinuxHostingsApi.md#addScheduledTasks) | **POST** /linuxhostings/{domainName}/scheduledtasks | Add a scheduled task
[**addSshKey**](LinuxHostingsApi.md#addSshKey) | **POST** /linuxhostings/{domainName}/ssh/keys | Add a SSH key
[**changeApcu**](LinuxHostingsApi.md#changeApcu) | **PUT** /linuxhostings/{domainName}/phpsettings/apcu | Configure PHP APCu setting
[**changeAutoRedirect**](LinuxHostingsApi.md#changeAutoRedirect) | **PUT** /linuxhostings/{domainName}/sslsettings/{hostname}/autoredirect | Configure auto redirect
[**changeGzipCompression**](LinuxHostingsApi.md#changeGzipCompression) | **PUT** /linuxhostings/{domainName}/settings/gzipcompression | Enable/disable GZIP compression
[**changeLetsEncrypt**](LinuxHostingsApi.md#changeLetsEncrypt) | **PUT** /linuxhostings/{domainName}/sslsettings/{hostname}/letsencrypt | Configure let&#39;s encrypt
[**changePhpMemoryLimit**](LinuxHostingsApi.md#changePhpMemoryLimit) | **PUT** /linuxhostings/{domainName}/phpsettings/memorylimit | Configure PHP memory limit
[**changePhpVersion**](LinuxHostingsApi.md#changePhpVersion) | **PUT** /linuxhostings/{domainName}/phpsettings/version | Change the Linux hosting PHP version.
[**configureFtp**](LinuxHostingsApi.md#configureFtp) | **PUT** /linuxhostings/{domainName}/ftp/configuration | Configure FTP
[**configureHttp2**](LinuxHostingsApi.md#configureHttp2) | **PUT** /linuxhostings/{domainName}/sites/{siteName}/http2/configuration | Configure HTTP/2
[**configureScheduledTask**](LinuxHostingsApi.md#configureScheduledTask) | **PUT** /linuxhostings/{domainName}/scheduledtasks/{scheduledTaskId} | Configure a scheduled task
[**configureSsh**](LinuxHostingsApi.md#configureSsh) | **PUT** /linuxhostings/{domainName}/ssh/configuration | Configure SSH
[**createHostHeader**](LinuxHostingsApi.md#createHostHeader) | **POST** /linuxhostings/{domainName}/sites/{siteName}/hostheaders | Create a host header
[**createSubsite**](LinuxHostingsApi.md#createSubsite) | **POST** /linuxhostings/{domainName}/subsites | Create a subsite
[**deleteScheduledTask**](LinuxHostingsApi.md#deleteScheduledTask) | **DELETE** /linuxhostings/{domainName}/scheduledtasks/{scheduledTaskId} | Delete a scheduled task
[**deleteSshKey**](LinuxHostingsApi.md#deleteSshKey) | **DELETE** /linuxhostings/{domainName}/ssh/keys/{fingerprint} | Delete a SSH key
[**deleteSubsite**](LinuxHostingsApi.md#deleteSubsite) | **DELETE** /linuxhostings/{domainName}/subsites/{siteName} | Delete a subsite
[**getAvailablePhpVersions**](LinuxHostingsApi.md#getAvailablePhpVersions) | **GET** /linuxhostings/{domainName}/phpsettings/availableversions | Get the available PHP versions.
[**getLinuxHosting**](LinuxHostingsApi.md#getLinuxHosting) | **GET** /linuxhostings/{domainName} | Linux hosting detail
[**getLinuxHostings**](LinuxHostingsApi.md#getLinuxHostings) | **GET** /linuxhostings | Overview of linux hostings
[**getScheduledTask**](LinuxHostingsApi.md#getScheduledTask) | **GET** /linuxhostings/{domainName}/scheduledtasks/{scheduledTaskId} | Get scheduled task detail
[**getScheduledTasks**](LinuxHostingsApi.md#getScheduledTasks) | **GET** /linuxhostings/{domainName}/scheduledtasks | Overview of scheduled tasks
[**getSshKeys**](LinuxHostingsApi.md#getSshKeys) | **GET** /linuxhostings/{domainName}/ssh/keys | Overview of SSH keys



## addScheduledTasks

> addScheduledTasks(domainName, domainName2, opts)

Add a scheduled task

### Example

```javascript
import PublicApi from 'public_api';

let apiInstance = new PublicApi.LinuxHostingsApi();
let domainName = "domainName_example"; // String | Linux hosting domain name.
let domainName2 = "domainName_example"; // String | Automatically added
let opts = {
  'scheduledTask': new PublicApi.ScheduledTask() // ScheduledTask | 
};
apiInstance.addScheduledTasks(domainName, domainName2, opts, (error, data, response) => {
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
 **domainName** | **String**| Linux hosting domain name. | 
 **domainName2** | **String**| Automatically added | 
 **scheduledTask** | [**ScheduledTask**](ScheduledTask.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## addSshKey

> addSshKey(domainName, domainName2, opts)

Add a SSH key

### Example

```javascript
import PublicApi from 'public_api';

let apiInstance = new PublicApi.LinuxHostingsApi();
let domainName = "domainName_example"; // String | Linux hosting domain name.
let domainName2 = "domainName_example"; // String | Automatically added
let opts = {
  'addSshKeyRequest': new PublicApi.AddSshKeyRequest() // AddSshKeyRequest | SSH key public key.
};
apiInstance.addSshKey(domainName, domainName2, opts, (error, data, response) => {
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
 **domainName** | **String**| Linux hosting domain name. | 
 **domainName2** | **String**| Automatically added | 
 **addSshKeyRequest** | [**AddSshKeyRequest**](AddSshKeyRequest.md)| SSH key public key. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## changeApcu

> changeApcu(domainName, domainName2, opts)

Configure PHP APCu setting

### Example

```javascript
import PublicApi from 'public_api';

let apiInstance = new PublicApi.LinuxHostingsApi();
let domainName = "domainName_example"; // String | Linux hosting domain name
let domainName2 = "domainName_example"; // String | Automatically added
let opts = {
  'updatePhpAPcuRequest': new PublicApi.UpdatePhpAPcuRequest() // UpdatePhpAPcuRequest | Php APcu config
};
apiInstance.changeApcu(domainName, domainName2, opts, (error, data, response) => {
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
 **domainName** | **String**| Linux hosting domain name | 
 **domainName2** | **String**| Automatically added | 
 **updatePhpAPcuRequest** | [**UpdatePhpAPcuRequest**](UpdatePhpAPcuRequest.md)| Php APcu config | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## changeAutoRedirect

> changeAutoRedirect(domainName, hostname, domainName2, opts)

Configure auto redirect

### Example

```javascript
import PublicApi from 'public_api';

let apiInstance = new PublicApi.LinuxHostingsApi();
let domainName = "domainName_example"; // String | Linux hosting domain name.
let hostname = "hostname_example"; // String | Specific hostname.
let domainName2 = "domainName_example"; // String | Automatically added
let opts = {
  'autoRedirectConfig': new PublicApi.AutoRedirectConfig() // AutoRedirectConfig | Auto redirect config.
};
apiInstance.changeAutoRedirect(domainName, hostname, domainName2, opts, (error, data, response) => {
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
 **domainName** | **String**| Linux hosting domain name. | 
 **hostname** | **String**| Specific hostname. | 
 **domainName2** | **String**| Automatically added | 
 **autoRedirectConfig** | [**AutoRedirectConfig**](AutoRedirectConfig.md)| Auto redirect config. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## changeGzipCompression

> changeGzipCompression(domainName, domainName2, opts)

Enable/disable GZIP compression

### Example

```javascript
import PublicApi from 'public_api';

let apiInstance = new PublicApi.LinuxHostingsApi();
let domainName = "domainName_example"; // String | Linux hosting domain name
let domainName2 = "domainName_example"; // String | Automatically added
let opts = {
  'gzipConfig': new PublicApi.GzipConfig() // GzipConfig | Whether GZIP compression is enabled or not.
};
apiInstance.changeGzipCompression(domainName, domainName2, opts, (error, data, response) => {
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
 **domainName** | **String**| Linux hosting domain name | 
 **domainName2** | **String**| Automatically added | 
 **gzipConfig** | [**GzipConfig**](GzipConfig.md)| Whether GZIP compression is enabled or not. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## changeLetsEncrypt

> changeLetsEncrypt(domainName, hostname, domainName2, opts)

Configure let&#39;s encrypt

### Example

```javascript
import PublicApi from 'public_api';

let apiInstance = new PublicApi.LinuxHostingsApi();
let domainName = "domainName_example"; // String | Linux hosting domain name.
let hostname = "hostname_example"; // String | Specific hostname.
let domainName2 = "domainName_example"; // String | Automatically added
let opts = {
  'letsEncryptConfig': new PublicApi.LetsEncryptConfig() // LetsEncryptConfig | Let's encrypt config.
};
apiInstance.changeLetsEncrypt(domainName, hostname, domainName2, opts, (error, data, response) => {
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
 **domainName** | **String**| Linux hosting domain name. | 
 **hostname** | **String**| Specific hostname. | 
 **domainName2** | **String**| Automatically added | 
 **letsEncryptConfig** | [**LetsEncryptConfig**](LetsEncryptConfig.md)| Let&#39;s encrypt config. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## changePhpMemoryLimit

> changePhpMemoryLimit(domainName, domainName2, opts)

Configure PHP memory limit

### Example

```javascript
import PublicApi from 'public_api';

let apiInstance = new PublicApi.LinuxHostingsApi();
let domainName = "domainName_example"; // String | Linux hosting domain name.
let domainName2 = "domainName_example"; // String | Automatically added
let opts = {
  'updatePhpMemoryLimitRequest': new PublicApi.UpdatePhpMemoryLimitRequest() // UpdatePhpMemoryLimitRequest | Memory limit config
};
apiInstance.changePhpMemoryLimit(domainName, domainName2, opts, (error, data, response) => {
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
 **domainName** | **String**| Linux hosting domain name. | 
 **domainName2** | **String**| Automatically added | 
 **updatePhpMemoryLimitRequest** | [**UpdatePhpMemoryLimitRequest**](UpdatePhpMemoryLimitRequest.md)| Memory limit config | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## changePhpVersion

> changePhpVersion(domainName, domainName2, opts)

Change the Linux hosting PHP version.

### Example

```javascript
import PublicApi from 'public_api';

let apiInstance = new PublicApi.LinuxHostingsApi();
let domainName = "domainName_example"; // String | Linux hosting domain name.
let domainName2 = "domainName_example"; // String | Automatically added
let opts = {
  'phpVersion': new PublicApi.PhpVersion() // PhpVersion | The new PHP version.
};
apiInstance.changePhpVersion(domainName, domainName2, opts, (error, data, response) => {
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
 **domainName** | **String**| Linux hosting domain name. | 
 **domainName2** | **String**| Automatically added | 
 **phpVersion** | [**PhpVersion**](PhpVersion.md)| The new PHP version. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## configureFtp

> configureFtp(domainName, domainName2, opts)

Configure FTP

### Example

```javascript
import PublicApi from 'public_api';

let apiInstance = new PublicApi.LinuxHostingsApi();
let domainName = "domainName_example"; // String | Linux hosting domain name.
let domainName2 = "domainName_example"; // String | Automatically added
let opts = {
  'ftpConfiguration': new PublicApi.FtpConfiguration() // FtpConfiguration | 
};
apiInstance.configureFtp(domainName, domainName2, opts, (error, data, response) => {
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
 **domainName** | **String**| Linux hosting domain name. | 
 **domainName2** | **String**| Automatically added | 
 **ftpConfiguration** | [**FtpConfiguration**](FtpConfiguration.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## configureHttp2

> configureHttp2(domainName, siteName, domainName2, siteName2, opts)

Configure HTTP/2

### Example

```javascript
import PublicApi from 'public_api';

let apiInstance = new PublicApi.LinuxHostingsApi();
let domainName = "domainName_example"; // String | Linux hosting domain name.
let siteName = "siteName_example"; // String | Site name where HTTP/2 should be configured.<br />  For HTTP/2 to work correctly, the site must have ssl enabled.
let domainName2 = "domainName_example"; // String | Automatically added
let siteName2 = "siteName_example"; // String | Automatically added
let opts = {
  'http2Configuration': new PublicApi.Http2Configuration() // Http2Configuration | 
};
apiInstance.configureHttp2(domainName, siteName, domainName2, siteName2, opts, (error, data, response) => {
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
 **domainName** | **String**| Linux hosting domain name. | 
 **siteName** | **String**| Site name where HTTP/2 should be configured.&lt;br /&gt;  For HTTP/2 to work correctly, the site must have ssl enabled. | 
 **domainName2** | **String**| Automatically added | 
 **siteName2** | **String**| Automatically added | 
 **http2Configuration** | [**Http2Configuration**](Http2Configuration.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## configureScheduledTask

> configureScheduledTask(domainName, scheduledTaskId, domainName2, scheduledTaskId2, opts)

Configure a scheduled task

### Example

```javascript
import PublicApi from 'public_api';

let apiInstance = new PublicApi.LinuxHostingsApi();
let domainName = "domainName_example"; // String | Linux hosting domain name.
let scheduledTaskId = "scheduledTaskId_example"; // String | Id of the scheduled task.
let domainName2 = "domainName_example"; // String | Automatically added
let scheduledTaskId2 = "scheduledTaskId_example"; // String | Automatically added
let opts = {
  'scheduledTask': new PublicApi.ScheduledTask() // ScheduledTask | 
};
apiInstance.configureScheduledTask(domainName, scheduledTaskId, domainName2, scheduledTaskId2, opts, (error, data, response) => {
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
 **domainName** | **String**| Linux hosting domain name. | 
 **scheduledTaskId** | **String**| Id of the scheduled task. | 
 **domainName2** | **String**| Automatically added | 
 **scheduledTaskId2** | **String**| Automatically added | 
 **scheduledTask** | [**ScheduledTask**](ScheduledTask.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## configureSsh

> configureSsh(domainName, domainName2, opts)

Configure SSH

### Example

```javascript
import PublicApi from 'public_api';

let apiInstance = new PublicApi.LinuxHostingsApi();
let domainName = "domainName_example"; // String | Linux hosting domain name.
let domainName2 = "domainName_example"; // String | Automatically added
let opts = {
  'sshConfiguration': new PublicApi.SshConfiguration() // SshConfiguration | 
};
apiInstance.configureSsh(domainName, domainName2, opts, (error, data, response) => {
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
 **domainName** | **String**| Linux hosting domain name. | 
 **domainName2** | **String**| Automatically added | 
 **sshConfiguration** | [**SshConfiguration**](SshConfiguration.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## createHostHeader

> createHostHeader(domainName, siteName, domainName2, siteName2, opts)

Create a host header

### Example

```javascript
import PublicApi from 'public_api';

let apiInstance = new PublicApi.LinuxHostingsApi();
let domainName = "domainName_example"; // String | Linux hosting domain name.
let siteName = "siteName_example"; // String | Name of the site on the linux hosting.
let domainName2 = "domainName_example"; // String | Automatically added
let siteName2 = "siteName_example"; // String | Automatically added
let opts = {
  'addHostHeaderRequest': new PublicApi.AddHostHeaderRequest() // AddHostHeaderRequest | Add host header request
};
apiInstance.createHostHeader(domainName, siteName, domainName2, siteName2, opts, (error, data, response) => {
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
 **domainName** | **String**| Linux hosting domain name. | 
 **siteName** | **String**| Name of the site on the linux hosting. | 
 **domainName2** | **String**| Automatically added | 
 **siteName2** | **String**| Automatically added | 
 **addHostHeaderRequest** | [**AddHostHeaderRequest**](AddHostHeaderRequest.md)| Add host header request | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## createSubsite

> createSubsite(domainName, domainName2, opts)

Create a subsite

### Example

```javascript
import PublicApi from 'public_api';

let apiInstance = new PublicApi.LinuxHostingsApi();
let domainName = "domainName_example"; // String | Linux hosting domain name.
let domainName2 = "domainName_example"; // String | Automatically added
let opts = {
  'addSubsiteRequest': new PublicApi.AddSubsiteRequest() // AddSubsiteRequest | Add subsite request
};
apiInstance.createSubsite(domainName, domainName2, opts, (error, data, response) => {
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
 **domainName** | **String**| Linux hosting domain name. | 
 **domainName2** | **String**| Automatically added | 
 **addSubsiteRequest** | [**AddSubsiteRequest**](AddSubsiteRequest.md)| Add subsite request | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## deleteScheduledTask

> deleteScheduledTask(domainName, scheduledTaskId, domainName2, scheduledTaskId2)

Delete a scheduled task

### Example

```javascript
import PublicApi from 'public_api';

let apiInstance = new PublicApi.LinuxHostingsApi();
let domainName = "domainName_example"; // String | Linux hosting domain name.
let scheduledTaskId = "scheduledTaskId_example"; // String | Id of the scheduled task.
let domainName2 = "domainName_example"; // String | Automatically added
let scheduledTaskId2 = "scheduledTaskId_example"; // String | Automatically added
apiInstance.deleteScheduledTask(domainName, scheduledTaskId, domainName2, scheduledTaskId2, (error, data, response) => {
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
 **domainName** | **String**| Linux hosting domain name. | 
 **scheduledTaskId** | **String**| Id of the scheduled task. | 
 **domainName2** | **String**| Automatically added | 
 **scheduledTaskId2** | **String**| Automatically added | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteSshKey

> deleteSshKey(domainName, fingerprint, domainName2)

Delete a SSH key

### Example

```javascript
import PublicApi from 'public_api';

let apiInstance = new PublicApi.LinuxHostingsApi();
let domainName = "domainName_example"; // String | Linux hosting domain name.
let fingerprint = "fingerprint_example"; // String | Fingerprint of public key.
let domainName2 = "domainName_example"; // String | Automatically added
apiInstance.deleteSshKey(domainName, fingerprint, domainName2, (error, data, response) => {
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
 **domainName** | **String**| Linux hosting domain name. | 
 **fingerprint** | **String**| Fingerprint of public key. | 
 **domainName2** | **String**| Automatically added | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteSubsite

> deleteSubsite(domainName, siteName, domainName2, siteName2)

Delete a subsite

### Example

```javascript
import PublicApi from 'public_api';

let apiInstance = new PublicApi.LinuxHostingsApi();
let domainName = "domainName_example"; // String | Linux hosting domain name.
let siteName = "siteName_example"; // String | Name of the site on the linux hosting.
let domainName2 = "domainName_example"; // String | Automatically added
let siteName2 = "siteName_example"; // String | Automatically added
apiInstance.deleteSubsite(domainName, siteName, domainName2, siteName2, (error, data, response) => {
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
 **domainName** | **String**| Linux hosting domain name. | 
 **siteName** | **String**| Name of the site on the linux hosting. | 
 **domainName2** | **String**| Automatically added | 
 **siteName2** | **String**| Automatically added | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getAvailablePhpVersions

> [PhpVersion] getAvailablePhpVersions(domainName, domainName2)

Get the available PHP versions.

### Example

```javascript
import PublicApi from 'public_api';

let apiInstance = new PublicApi.LinuxHostingsApi();
let domainName = "domainName_example"; // String | Linux hosting domain name.
let domainName2 = "domainName_example"; // String | Automatically added
apiInstance.getAvailablePhpVersions(domainName, domainName2, (error, data, response) => {
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
 **domainName** | **String**| Linux hosting domain name. | 
 **domainName2** | **String**| Automatically added | 

### Return type

[**[PhpVersion]**](PhpVersion.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getLinuxHosting

> LinuxHostingDetail getLinuxHosting(domainName, domainName2)

Linux hosting detail

### Example

```javascript
import PublicApi from 'public_api';

let apiInstance = new PublicApi.LinuxHostingsApi();
let domainName = "domainName_example"; // String | The Linux hosting domain name.
let domainName2 = "domainName_example"; // String | Automatically added
apiInstance.getLinuxHosting(domainName, domainName2, (error, data, response) => {
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
 **domainName** | **String**| The Linux hosting domain name. | 
 **domainName2** | **String**| Automatically added | 

### Return type

[**LinuxHostingDetail**](LinuxHostingDetail.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getLinuxHostings

> [LinuxHosting] getLinuxHostings(opts)

Overview of linux hostings

### Example

```javascript
import PublicApi from 'public_api';

let apiInstance = new PublicApi.LinuxHostingsApi();
let opts = {
  'skip': 56, // Number | The number of items to skip in the resultset.
  'take': 56 // Number | The number of items to return in the resultset. The returned count can be equal or less than this number.
};
apiInstance.getLinuxHostings(opts, (error, data, response) => {
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
 **skip** | **Number**| The number of items to skip in the resultset. | [optional] 
 **take** | **Number**| The number of items to return in the resultset. The returned count can be equal or less than this number. | [optional] 

### Return type

[**[LinuxHosting]**](LinuxHosting.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getScheduledTask

> ScheduledTask getScheduledTask(domainName, scheduledTaskId, domainName2, scheduledTaskId2)

Get scheduled task detail

### Example

```javascript
import PublicApi from 'public_api';

let apiInstance = new PublicApi.LinuxHostingsApi();
let domainName = "domainName_example"; // String | Linux hosting domain name.
let scheduledTaskId = "scheduledTaskId_example"; // String | Id of the scheduled task.
let domainName2 = "domainName_example"; // String | Automatically added
let scheduledTaskId2 = "scheduledTaskId_example"; // String | Automatically added
apiInstance.getScheduledTask(domainName, scheduledTaskId, domainName2, scheduledTaskId2, (error, data, response) => {
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
 **domainName** | **String**| Linux hosting domain name. | 
 **scheduledTaskId** | **String**| Id of the scheduled task. | 
 **domainName2** | **String**| Automatically added | 
 **scheduledTaskId2** | **String**| Automatically added | 

### Return type

[**ScheduledTask**](ScheduledTask.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getScheduledTasks

> [ScheduledTask] getScheduledTasks(domainName, domainName2)

Overview of scheduled tasks

Manage scheduled tasks which are also manageable via the control panel.

### Example

```javascript
import PublicApi from 'public_api';

let apiInstance = new PublicApi.LinuxHostingsApi();
let domainName = "domainName_example"; // String | Linux hosting domain name.
let domainName2 = "domainName_example"; // String | Automatically added
apiInstance.getScheduledTasks(domainName, domainName2, (error, data, response) => {
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
 **domainName** | **String**| Linux hosting domain name. | 
 **domainName2** | **String**| Automatically added | 

### Return type

[**[ScheduledTask]**](ScheduledTask.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSshKeys

> [SshKey] getSshKeys(domainName, domainName2)

Overview of SSH keys

### Example

```javascript
import PublicApi from 'public_api';

let apiInstance = new PublicApi.LinuxHostingsApi();
let domainName = "domainName_example"; // String | Linux hosting domain name.
let domainName2 = "domainName_example"; // String | Automatically added
apiInstance.getSshKeys(domainName, domainName2, (error, data, response) => {
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
 **domainName** | **String**| Linux hosting domain name. | 
 **domainName2** | **String**| Automatically added | 

### Return type

[**[SshKey]**](SshKey.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

