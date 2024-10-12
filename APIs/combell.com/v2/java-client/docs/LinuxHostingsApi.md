# LinuxHostingsApi

All URIs are relative to */v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addScheduledTasks**](LinuxHostingsApi.md#addScheduledTasks) | **POST** /linuxhostings/{domainName}/scheduledtasks | Add a scheduled task |
| [**addSshKey**](LinuxHostingsApi.md#addSshKey) | **POST** /linuxhostings/{domainName}/ssh/keys | Add a SSH key |
| [**changeApcu**](LinuxHostingsApi.md#changeApcu) | **PUT** /linuxhostings/{domainName}/phpsettings/apcu | Configure PHP APCu setting |
| [**changeAutoRedirect**](LinuxHostingsApi.md#changeAutoRedirect) | **PUT** /linuxhostings/{domainName}/sslsettings/{hostname}/autoredirect | Configure auto redirect |
| [**changeGzipCompression**](LinuxHostingsApi.md#changeGzipCompression) | **PUT** /linuxhostings/{domainName}/settings/gzipcompression | Enable/disable GZIP compression |
| [**changeLetsEncrypt**](LinuxHostingsApi.md#changeLetsEncrypt) | **PUT** /linuxhostings/{domainName}/sslsettings/{hostname}/letsencrypt | Configure let&#39;s encrypt |
| [**changePhpMemoryLimit**](LinuxHostingsApi.md#changePhpMemoryLimit) | **PUT** /linuxhostings/{domainName}/phpsettings/memorylimit | Configure PHP memory limit |
| [**changePhpVersion**](LinuxHostingsApi.md#changePhpVersion) | **PUT** /linuxhostings/{domainName}/phpsettings/version | Change the Linux hosting PHP version. |
| [**configureFtp**](LinuxHostingsApi.md#configureFtp) | **PUT** /linuxhostings/{domainName}/ftp/configuration | Configure FTP |
| [**configureHttp2**](LinuxHostingsApi.md#configureHttp2) | **PUT** /linuxhostings/{domainName}/sites/{siteName}/http2/configuration | Configure HTTP/2 |
| [**configureScheduledTask**](LinuxHostingsApi.md#configureScheduledTask) | **PUT** /linuxhostings/{domainName}/scheduledtasks/{scheduledTaskId} | Configure a scheduled task |
| [**configureSsh**](LinuxHostingsApi.md#configureSsh) | **PUT** /linuxhostings/{domainName}/ssh/configuration | Configure SSH |
| [**createHostHeader**](LinuxHostingsApi.md#createHostHeader) | **POST** /linuxhostings/{domainName}/sites/{siteName}/hostheaders | Create a host header |
| [**createSubsite**](LinuxHostingsApi.md#createSubsite) | **POST** /linuxhostings/{domainName}/subsites | Create a subsite |
| [**deleteScheduledTask**](LinuxHostingsApi.md#deleteScheduledTask) | **DELETE** /linuxhostings/{domainName}/scheduledtasks/{scheduledTaskId} | Delete a scheduled task |
| [**deleteSshKey**](LinuxHostingsApi.md#deleteSshKey) | **DELETE** /linuxhostings/{domainName}/ssh/keys/{fingerprint} | Delete a SSH key |
| [**deleteSubsite**](LinuxHostingsApi.md#deleteSubsite) | **DELETE** /linuxhostings/{domainName}/subsites/{siteName} | Delete a subsite |
| [**getAvailablePhpVersions**](LinuxHostingsApi.md#getAvailablePhpVersions) | **GET** /linuxhostings/{domainName}/phpsettings/availableversions | Get the available PHP versions. |
| [**getLinuxHosting**](LinuxHostingsApi.md#getLinuxHosting) | **GET** /linuxhostings/{domainName} | Linux hosting detail |
| [**getLinuxHostings**](LinuxHostingsApi.md#getLinuxHostings) | **GET** /linuxhostings | Overview of linux hostings |
| [**getScheduledTask**](LinuxHostingsApi.md#getScheduledTask) | **GET** /linuxhostings/{domainName}/scheduledtasks/{scheduledTaskId} | Get scheduled task detail |
| [**getScheduledTasks**](LinuxHostingsApi.md#getScheduledTasks) | **GET** /linuxhostings/{domainName}/scheduledtasks | Overview of scheduled tasks |
| [**getSshKeys**](LinuxHostingsApi.md#getSshKeys) | **GET** /linuxhostings/{domainName}/ssh/keys | Overview of SSH keys |


<a id="addScheduledTasks"></a>
# **addScheduledTasks**
> addScheduledTasks(domainName, domainName2, scheduledTask)

Add a scheduled task

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LinuxHostingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/v2");

    LinuxHostingsApi apiInstance = new LinuxHostingsApi(defaultClient);
    String domainName = "domainName_example"; // String | Linux hosting domain name.
    String domainName2 = "domainName_example"; // String | Automatically added
    ScheduledTask scheduledTask = new ScheduledTask(); // ScheduledTask | 
    try {
      apiInstance.addScheduledTasks(domainName, domainName2, scheduledTask);
    } catch (ApiException e) {
      System.err.println("Exception when calling LinuxHostingsApi#addScheduledTasks");
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
| **domainName** | **String**| Linux hosting domain name. | |
| **domainName2** | **String**| Automatically added | |
| **scheduledTask** | [**ScheduledTask**](ScheduledTask.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Success |  * Location - The location referring to a resource that replaced the original resource. <br>  |

<a id="addSshKey"></a>
# **addSshKey**
> addSshKey(domainName, domainName2, addSshKeyRequest)

Add a SSH key

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LinuxHostingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/v2");

    LinuxHostingsApi apiInstance = new LinuxHostingsApi(defaultClient);
    String domainName = "domainName_example"; // String | Linux hosting domain name.
    String domainName2 = "domainName_example"; // String | Automatically added
    AddSshKeyRequest addSshKeyRequest = new AddSshKeyRequest(); // AddSshKeyRequest | SSH key public key.
    try {
      apiInstance.addSshKey(domainName, domainName2, addSshKeyRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling LinuxHostingsApi#addSshKey");
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
| **domainName** | **String**| Linux hosting domain name. | |
| **domainName2** | **String**| Automatically added | |
| **addSshKeyRequest** | [**AddSshKeyRequest**](AddSshKeyRequest.md)| SSH key public key. | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Success |  * Location - The location referring to a resource that replaced the original resource. <br>  |

<a id="changeApcu"></a>
# **changeApcu**
> changeApcu(domainName, domainName2, updatePhpAPcuRequest)

Configure PHP APCu setting

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LinuxHostingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/v2");

    LinuxHostingsApi apiInstance = new LinuxHostingsApi(defaultClient);
    String domainName = "domainName_example"; // String | Linux hosting domain name
    String domainName2 = "domainName_example"; // String | Automatically added
    UpdatePhpAPcuRequest updatePhpAPcuRequest = new UpdatePhpAPcuRequest(); // UpdatePhpAPcuRequest | Php APcu config
    try {
      apiInstance.changeApcu(domainName, domainName2, updatePhpAPcuRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling LinuxHostingsApi#changeApcu");
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
| **domainName** | **String**| Linux hosting domain name | |
| **domainName2** | **String**| Automatically added | |
| **updatePhpAPcuRequest** | [**UpdatePhpAPcuRequest**](UpdatePhpAPcuRequest.md)| Php APcu config | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |

<a id="changeAutoRedirect"></a>
# **changeAutoRedirect**
> changeAutoRedirect(domainName, hostname, domainName2, autoRedirectConfig)

Configure auto redirect

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LinuxHostingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/v2");

    LinuxHostingsApi apiInstance = new LinuxHostingsApi(defaultClient);
    String domainName = "domainName_example"; // String | Linux hosting domain name.
    String hostname = "hostname_example"; // String | Specific hostname.
    String domainName2 = "domainName_example"; // String | Automatically added
    AutoRedirectConfig autoRedirectConfig = new AutoRedirectConfig(); // AutoRedirectConfig | Auto redirect config.
    try {
      apiInstance.changeAutoRedirect(domainName, hostname, domainName2, autoRedirectConfig);
    } catch (ApiException e) {
      System.err.println("Exception when calling LinuxHostingsApi#changeAutoRedirect");
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
| **domainName** | **String**| Linux hosting domain name. | |
| **hostname** | **String**| Specific hostname. | |
| **domainName2** | **String**| Automatically added | |
| **autoRedirectConfig** | [**AutoRedirectConfig**](AutoRedirectConfig.md)| Auto redirect config. | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |

<a id="changeGzipCompression"></a>
# **changeGzipCompression**
> changeGzipCompression(domainName, domainName2, gzipConfig)

Enable/disable GZIP compression

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LinuxHostingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/v2");

    LinuxHostingsApi apiInstance = new LinuxHostingsApi(defaultClient);
    String domainName = "domainName_example"; // String | Linux hosting domain name
    String domainName2 = "domainName_example"; // String | Automatically added
    GzipConfig gzipConfig = new GzipConfig(); // GzipConfig | Whether GZIP compression is enabled or not.
    try {
      apiInstance.changeGzipCompression(domainName, domainName2, gzipConfig);
    } catch (ApiException e) {
      System.err.println("Exception when calling LinuxHostingsApi#changeGzipCompression");
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
| **domainName** | **String**| Linux hosting domain name | |
| **domainName2** | **String**| Automatically added | |
| **gzipConfig** | [**GzipConfig**](GzipConfig.md)| Whether GZIP compression is enabled or not. | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |

<a id="changeLetsEncrypt"></a>
# **changeLetsEncrypt**
> changeLetsEncrypt(domainName, hostname, domainName2, letsEncryptConfig)

Configure let&#39;s encrypt

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LinuxHostingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/v2");

    LinuxHostingsApi apiInstance = new LinuxHostingsApi(defaultClient);
    String domainName = "domainName_example"; // String | Linux hosting domain name.
    String hostname = "hostname_example"; // String | Specific hostname.
    String domainName2 = "domainName_example"; // String | Automatically added
    LetsEncryptConfig letsEncryptConfig = new LetsEncryptConfig(); // LetsEncryptConfig | Let's encrypt config.
    try {
      apiInstance.changeLetsEncrypt(domainName, hostname, domainName2, letsEncryptConfig);
    } catch (ApiException e) {
      System.err.println("Exception when calling LinuxHostingsApi#changeLetsEncrypt");
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
| **domainName** | **String**| Linux hosting domain name. | |
| **hostname** | **String**| Specific hostname. | |
| **domainName2** | **String**| Automatically added | |
| **letsEncryptConfig** | [**LetsEncryptConfig**](LetsEncryptConfig.md)| Let&#39;s encrypt config. | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |

<a id="changePhpMemoryLimit"></a>
# **changePhpMemoryLimit**
> changePhpMemoryLimit(domainName, domainName2, updatePhpMemoryLimitRequest)

Configure PHP memory limit

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LinuxHostingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/v2");

    LinuxHostingsApi apiInstance = new LinuxHostingsApi(defaultClient);
    String domainName = "domainName_example"; // String | Linux hosting domain name.
    String domainName2 = "domainName_example"; // String | Automatically added
    UpdatePhpMemoryLimitRequest updatePhpMemoryLimitRequest = new UpdatePhpMemoryLimitRequest(); // UpdatePhpMemoryLimitRequest | Memory limit config
    try {
      apiInstance.changePhpMemoryLimit(domainName, domainName2, updatePhpMemoryLimitRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling LinuxHostingsApi#changePhpMemoryLimit");
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
| **domainName** | **String**| Linux hosting domain name. | |
| **domainName2** | **String**| Automatically added | |
| **updatePhpMemoryLimitRequest** | [**UpdatePhpMemoryLimitRequest**](UpdatePhpMemoryLimitRequest.md)| Memory limit config | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |

<a id="changePhpVersion"></a>
# **changePhpVersion**
> changePhpVersion(domainName, domainName2, phpVersion)

Change the Linux hosting PHP version.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LinuxHostingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/v2");

    LinuxHostingsApi apiInstance = new LinuxHostingsApi(defaultClient);
    String domainName = "domainName_example"; // String | Linux hosting domain name.
    String domainName2 = "domainName_example"; // String | Automatically added
    PhpVersion phpVersion = new PhpVersion(); // PhpVersion | The new PHP version.
    try {
      apiInstance.changePhpVersion(domainName, domainName2, phpVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling LinuxHostingsApi#changePhpVersion");
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
| **domainName** | **String**| Linux hosting domain name. | |
| **domainName2** | **String**| Automatically added | |
| **phpVersion** | [**PhpVersion**](PhpVersion.md)| The new PHP version. | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |

<a id="configureFtp"></a>
# **configureFtp**
> configureFtp(domainName, domainName2, ftpConfiguration)

Configure FTP

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LinuxHostingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/v2");

    LinuxHostingsApi apiInstance = new LinuxHostingsApi(defaultClient);
    String domainName = "domainName_example"; // String | Linux hosting domain name.
    String domainName2 = "domainName_example"; // String | Automatically added
    FtpConfiguration ftpConfiguration = new FtpConfiguration(); // FtpConfiguration | 
    try {
      apiInstance.configureFtp(domainName, domainName2, ftpConfiguration);
    } catch (ApiException e) {
      System.err.println("Exception when calling LinuxHostingsApi#configureFtp");
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
| **domainName** | **String**| Linux hosting domain name. | |
| **domainName2** | **String**| Automatically added | |
| **ftpConfiguration** | [**FtpConfiguration**](FtpConfiguration.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **400** | Bad Request |  -  |

<a id="configureHttp2"></a>
# **configureHttp2**
> configureHttp2(domainName, siteName, domainName2, siteName2, http2Configuration)

Configure HTTP/2

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LinuxHostingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/v2");

    LinuxHostingsApi apiInstance = new LinuxHostingsApi(defaultClient);
    String domainName = "domainName_example"; // String | Linux hosting domain name.
    String siteName = "siteName_example"; // String | Site name where HTTP/2 should be configured.<br />  For HTTP/2 to work correctly, the site must have ssl enabled.
    String domainName2 = "domainName_example"; // String | Automatically added
    String siteName2 = "siteName_example"; // String | Automatically added
    Http2Configuration http2Configuration = new Http2Configuration(); // Http2Configuration | 
    try {
      apiInstance.configureHttp2(domainName, siteName, domainName2, siteName2, http2Configuration);
    } catch (ApiException e) {
      System.err.println("Exception when calling LinuxHostingsApi#configureHttp2");
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
| **domainName** | **String**| Linux hosting domain name. | |
| **siteName** | **String**| Site name where HTTP/2 should be configured.&lt;br /&gt;  For HTTP/2 to work correctly, the site must have ssl enabled. | |
| **domainName2** | **String**| Automatically added | |
| **siteName2** | **String**| Automatically added | |
| **http2Configuration** | [**Http2Configuration**](Http2Configuration.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **400** | Bad Request |  -  |

<a id="configureScheduledTask"></a>
# **configureScheduledTask**
> configureScheduledTask(domainName, scheduledTaskId, domainName2, scheduledTaskId2, scheduledTask)

Configure a scheduled task

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LinuxHostingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/v2");

    LinuxHostingsApi apiInstance = new LinuxHostingsApi(defaultClient);
    String domainName = "domainName_example"; // String | Linux hosting domain name.
    String scheduledTaskId = "scheduledTaskId_example"; // String | Id of the scheduled task.
    String domainName2 = "domainName_example"; // String | Automatically added
    String scheduledTaskId2 = "scheduledTaskId_example"; // String | Automatically added
    ScheduledTask scheduledTask = new ScheduledTask(); // ScheduledTask | 
    try {
      apiInstance.configureScheduledTask(domainName, scheduledTaskId, domainName2, scheduledTaskId2, scheduledTask);
    } catch (ApiException e) {
      System.err.println("Exception when calling LinuxHostingsApi#configureScheduledTask");
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
| **domainName** | **String**| Linux hosting domain name. | |
| **scheduledTaskId** | **String**| Id of the scheduled task. | |
| **domainName2** | **String**| Automatically added | |
| **scheduledTaskId2** | **String**| Automatically added | |
| **scheduledTask** | [**ScheduledTask**](ScheduledTask.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **400** | Bad Request |  -  |

<a id="configureSsh"></a>
# **configureSsh**
> configureSsh(domainName, domainName2, sshConfiguration)

Configure SSH

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LinuxHostingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/v2");

    LinuxHostingsApi apiInstance = new LinuxHostingsApi(defaultClient);
    String domainName = "domainName_example"; // String | Linux hosting domain name.
    String domainName2 = "domainName_example"; // String | Automatically added
    SshConfiguration sshConfiguration = new SshConfiguration(); // SshConfiguration | 
    try {
      apiInstance.configureSsh(domainName, domainName2, sshConfiguration);
    } catch (ApiException e) {
      System.err.println("Exception when calling LinuxHostingsApi#configureSsh");
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
| **domainName** | **String**| Linux hosting domain name. | |
| **domainName2** | **String**| Automatically added | |
| **sshConfiguration** | [**SshConfiguration**](SshConfiguration.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **400** | Bad Request |  -  |

<a id="createHostHeader"></a>
# **createHostHeader**
> createHostHeader(domainName, siteName, domainName2, siteName2, addHostHeaderRequest)

Create a host header

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LinuxHostingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/v2");

    LinuxHostingsApi apiInstance = new LinuxHostingsApi(defaultClient);
    String domainName = "domainName_example"; // String | Linux hosting domain name.
    String siteName = "siteName_example"; // String | Name of the site on the linux hosting.
    String domainName2 = "domainName_example"; // String | Automatically added
    String siteName2 = "siteName_example"; // String | Automatically added
    AddHostHeaderRequest addHostHeaderRequest = new AddHostHeaderRequest(); // AddHostHeaderRequest | Add host header request
    try {
      apiInstance.createHostHeader(domainName, siteName, domainName2, siteName2, addHostHeaderRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling LinuxHostingsApi#createHostHeader");
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
| **domainName** | **String**| Linux hosting domain name. | |
| **siteName** | **String**| Name of the site on the linux hosting. | |
| **domainName2** | **String**| Automatically added | |
| **siteName2** | **String**| Automatically added | |
| **addHostHeaderRequest** | [**AddHostHeaderRequest**](AddHostHeaderRequest.md)| Add host header request | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Success |  * Location - The location referring to a resource that replaced the original resource. <br>  |

<a id="createSubsite"></a>
# **createSubsite**
> createSubsite(domainName, domainName2, addSubsiteRequest)

Create a subsite

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LinuxHostingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/v2");

    LinuxHostingsApi apiInstance = new LinuxHostingsApi(defaultClient);
    String domainName = "domainName_example"; // String | Linux hosting domain name.
    String domainName2 = "domainName_example"; // String | Automatically added
    AddSubsiteRequest addSubsiteRequest = new AddSubsiteRequest(); // AddSubsiteRequest | Add subsite request
    try {
      apiInstance.createSubsite(domainName, domainName2, addSubsiteRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling LinuxHostingsApi#createSubsite");
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
| **domainName** | **String**| Linux hosting domain name. | |
| **domainName2** | **String**| Automatically added | |
| **addSubsiteRequest** | [**AddSubsiteRequest**](AddSubsiteRequest.md)| Add subsite request | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Success |  * Location - The location referring to a resource that replaced the original resource. <br>  |

<a id="deleteScheduledTask"></a>
# **deleteScheduledTask**
> deleteScheduledTask(domainName, scheduledTaskId, domainName2, scheduledTaskId2)

Delete a scheduled task

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LinuxHostingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/v2");

    LinuxHostingsApi apiInstance = new LinuxHostingsApi(defaultClient);
    String domainName = "domainName_example"; // String | Linux hosting domain name.
    String scheduledTaskId = "scheduledTaskId_example"; // String | Id of the scheduled task.
    String domainName2 = "domainName_example"; // String | Automatically added
    String scheduledTaskId2 = "scheduledTaskId_example"; // String | Automatically added
    try {
      apiInstance.deleteScheduledTask(domainName, scheduledTaskId, domainName2, scheduledTaskId2);
    } catch (ApiException e) {
      System.err.println("Exception when calling LinuxHostingsApi#deleteScheduledTask");
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
| **domainName** | **String**| Linux hosting domain name. | |
| **scheduledTaskId** | **String**| Id of the scheduled task. | |
| **domainName2** | **String**| Automatically added | |
| **scheduledTaskId2** | **String**| Automatically added | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **400** | Bad Request |  -  |

<a id="deleteSshKey"></a>
# **deleteSshKey**
> deleteSshKey(domainName, fingerprint, domainName2)

Delete a SSH key

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LinuxHostingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/v2");

    LinuxHostingsApi apiInstance = new LinuxHostingsApi(defaultClient);
    String domainName = "domainName_example"; // String | Linux hosting domain name.
    String fingerprint = "fingerprint_example"; // String | Fingerprint of public key.
    String domainName2 = "domainName_example"; // String | Automatically added
    try {
      apiInstance.deleteSshKey(domainName, fingerprint, domainName2);
    } catch (ApiException e) {
      System.err.println("Exception when calling LinuxHostingsApi#deleteSshKey");
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
| **domainName** | **String**| Linux hosting domain name. | |
| **fingerprint** | **String**| Fingerprint of public key. | |
| **domainName2** | **String**| Automatically added | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **400** | Bad Request |  -  |

<a id="deleteSubsite"></a>
# **deleteSubsite**
> deleteSubsite(domainName, siteName, domainName2, siteName2)

Delete a subsite

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LinuxHostingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/v2");

    LinuxHostingsApi apiInstance = new LinuxHostingsApi(defaultClient);
    String domainName = "domainName_example"; // String | Linux hosting domain name.
    String siteName = "siteName_example"; // String | Name of the site on the linux hosting.
    String domainName2 = "domainName_example"; // String | Automatically added
    String siteName2 = "siteName_example"; // String | Automatically added
    try {
      apiInstance.deleteSubsite(domainName, siteName, domainName2, siteName2);
    } catch (ApiException e) {
      System.err.println("Exception when calling LinuxHostingsApi#deleteSubsite");
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
| **domainName** | **String**| Linux hosting domain name. | |
| **siteName** | **String**| Name of the site on the linux hosting. | |
| **domainName2** | **String**| Automatically added | |
| **siteName2** | **String**| Automatically added | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **400** | Bad Request |  -  |

<a id="getAvailablePhpVersions"></a>
# **getAvailablePhpVersions**
> List&lt;PhpVersion&gt; getAvailablePhpVersions(domainName, domainName2)

Get the available PHP versions.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LinuxHostingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/v2");

    LinuxHostingsApi apiInstance = new LinuxHostingsApi(defaultClient);
    String domainName = "domainName_example"; // String | Linux hosting domain name.
    String domainName2 = "domainName_example"; // String | Automatically added
    try {
      List<PhpVersion> result = apiInstance.getAvailablePhpVersions(domainName, domainName2);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LinuxHostingsApi#getAvailablePhpVersions");
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
| **domainName** | **String**| Linux hosting domain name. | |
| **domainName2** | **String**| Automatically added | |

### Return type

[**List&lt;PhpVersion&gt;**](PhpVersion.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="getLinuxHosting"></a>
# **getLinuxHosting**
> LinuxHostingDetail getLinuxHosting(domainName, domainName2)

Linux hosting detail

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LinuxHostingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/v2");

    LinuxHostingsApi apiInstance = new LinuxHostingsApi(defaultClient);
    String domainName = "domainName_example"; // String | The Linux hosting domain name.
    String domainName2 = "domainName_example"; // String | Automatically added
    try {
      LinuxHostingDetail result = apiInstance.getLinuxHosting(domainName, domainName2);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LinuxHostingsApi#getLinuxHosting");
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
| **domainName** | **String**| The Linux hosting domain name. | |
| **domainName2** | **String**| Automatically added | |

### Return type

[**LinuxHostingDetail**](LinuxHostingDetail.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="getLinuxHostings"></a>
# **getLinuxHostings**
> List&lt;LinuxHosting&gt; getLinuxHostings(skip, take)

Overview of linux hostings

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LinuxHostingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/v2");

    LinuxHostingsApi apiInstance = new LinuxHostingsApi(defaultClient);
    Integer skip = 56; // Integer | The number of items to skip in the resultset.
    Integer take = 56; // Integer | The number of items to return in the resultset. The returned count can be equal or less than this number.
    try {
      List<LinuxHosting> result = apiInstance.getLinuxHostings(skip, take);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LinuxHostingsApi#getLinuxHostings");
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
| **skip** | **Integer**| The number of items to skip in the resultset. | [optional] |
| **take** | **Integer**| The number of items to return in the resultset. The returned count can be equal or less than this number. | [optional] |

### Return type

[**List&lt;LinuxHosting&gt;**](LinuxHosting.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  * X-Paging-Skipped - The number of results that have been skipped. <br>  * X-Paging-Take - The number of items in the current take. The number might differ from the requested take. It represents the actual number of items returned in the response. <br>  * X-Paging-TotalResults - The total number of results regardless of paging. <br>  |

<a id="getScheduledTask"></a>
# **getScheduledTask**
> ScheduledTask getScheduledTask(domainName, scheduledTaskId, domainName2, scheduledTaskId2)

Get scheduled task detail

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LinuxHostingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/v2");

    LinuxHostingsApi apiInstance = new LinuxHostingsApi(defaultClient);
    String domainName = "domainName_example"; // String | Linux hosting domain name.
    String scheduledTaskId = "scheduledTaskId_example"; // String | Id of the scheduled task.
    String domainName2 = "domainName_example"; // String | Automatically added
    String scheduledTaskId2 = "scheduledTaskId_example"; // String | Automatically added
    try {
      ScheduledTask result = apiInstance.getScheduledTask(domainName, scheduledTaskId, domainName2, scheduledTaskId2);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LinuxHostingsApi#getScheduledTask");
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
| **domainName** | **String**| Linux hosting domain name. | |
| **scheduledTaskId** | **String**| Id of the scheduled task. | |
| **domainName2** | **String**| Automatically added | |
| **scheduledTaskId2** | **String**| Automatically added | |

### Return type

[**ScheduledTask**](ScheduledTask.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="getScheduledTasks"></a>
# **getScheduledTasks**
> List&lt;ScheduledTask&gt; getScheduledTasks(domainName, domainName2)

Overview of scheduled tasks

Manage scheduled tasks which are also manageable via the control panel.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LinuxHostingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/v2");

    LinuxHostingsApi apiInstance = new LinuxHostingsApi(defaultClient);
    String domainName = "domainName_example"; // String | Linux hosting domain name.
    String domainName2 = "domainName_example"; // String | Automatically added
    try {
      List<ScheduledTask> result = apiInstance.getScheduledTasks(domainName, domainName2);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LinuxHostingsApi#getScheduledTasks");
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
| **domainName** | **String**| Linux hosting domain name. | |
| **domainName2** | **String**| Automatically added | |

### Return type

[**List&lt;ScheduledTask&gt;**](ScheduledTask.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="getSshKeys"></a>
# **getSshKeys**
> List&lt;SshKey&gt; getSshKeys(domainName, domainName2)

Overview of SSH keys

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LinuxHostingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/v2");

    LinuxHostingsApi apiInstance = new LinuxHostingsApi(defaultClient);
    String domainName = "domainName_example"; // String | Linux hosting domain name.
    String domainName2 = "domainName_example"; // String | Automatically added
    try {
      List<SshKey> result = apiInstance.getSshKeys(domainName, domainName2);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LinuxHostingsApi#getSshKeys");
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
| **domainName** | **String**| Linux hosting domain name. | |
| **domainName2** | **String**| Automatically added | |

### Return type

[**List&lt;SshKey&gt;**](SshKey.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

