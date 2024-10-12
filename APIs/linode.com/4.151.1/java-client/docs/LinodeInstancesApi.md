# LinodeInstancesApi

All URIs are relative to *https://api.linode.com/v4*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addLinodeConfig**](LinodeInstancesApi.md#addLinodeConfig) | **POST** /linode/instances/{linodeId}/configs | Configuration Profile Create |
| [**addLinodeDisk**](LinodeInstancesApi.md#addLinodeDisk) | **POST** /linode/instances/{linodeId}/disks | Disk Create |
| [**addLinodeIP**](LinodeInstancesApi.md#addLinodeIP) | **POST** /linode/instances/{linodeId}/ips | IPv4 Address Allocate |
| [**bootLinodeInstance**](LinodeInstancesApi.md#bootLinodeInstance) | **POST** /linode/instances/{linodeId}/boot | Linode Boot |
| [**cancelBackups**](LinodeInstancesApi.md#cancelBackups) | **POST** /linode/instances/{linodeId}/backups/cancel | Backups Cancel |
| [**cloneLinodeDisk**](LinodeInstancesApi.md#cloneLinodeDisk) | **POST** /linode/instances/{linodeId}/disks/{diskId}/clone | Disk Clone |
| [**cloneLinodeInstance**](LinodeInstancesApi.md#cloneLinodeInstance) | **POST** /linode/instances/{linodeId}/clone | Linode Clone |
| [**createLinodeInstance**](LinodeInstancesApi.md#createLinodeInstance) | **POST** /linode/instances | Linode Create |
| [**createSnapshot**](LinodeInstancesApi.md#createSnapshot) | **POST** /linode/instances/{linodeId}/backups | Snapshot Create |
| [**deleteDisk**](LinodeInstancesApi.md#deleteDisk) | **DELETE** /linode/instances/{linodeId}/disks/{diskId} | Disk Delete |
| [**deleteLinodeConfig**](LinodeInstancesApi.md#deleteLinodeConfig) | **DELETE** /linode/instances/{linodeId}/configs/{configId} | Configuration Profile Delete |
| [**deleteLinodeInstance**](LinodeInstancesApi.md#deleteLinodeInstance) | **DELETE** /linode/instances/{linodeId} | Linode Delete |
| [**enableBackups**](LinodeInstancesApi.md#enableBackups) | **POST** /linode/instances/{linodeId}/backups/enable | Backups Enable |
| [**getBackup**](LinodeInstancesApi.md#getBackup) | **GET** /linode/instances/{linodeId}/backups/{backupId} | Backup View |
| [**getBackups**](LinodeInstancesApi.md#getBackups) | **GET** /linode/instances/{linodeId}/backups | Backups List |
| [**getKernel**](LinodeInstancesApi.md#getKernel) | **GET** /linode/kernels/{kernelId} | Kernel View |
| [**getKernels**](LinodeInstancesApi.md#getKernels) | **GET** /linode/kernels | Kernels List |
| [**getLinodeConfig**](LinodeInstancesApi.md#getLinodeConfig) | **GET** /linode/instances/{linodeId}/configs/{configId} | Configuration Profile View |
| [**getLinodeConfigs**](LinodeInstancesApi.md#getLinodeConfigs) | **GET** /linode/instances/{linodeId}/configs | Configuration Profiles List |
| [**getLinodeDisk**](LinodeInstancesApi.md#getLinodeDisk) | **GET** /linode/instances/{linodeId}/disks/{diskId} | Disk View |
| [**getLinodeDisks**](LinodeInstancesApi.md#getLinodeDisks) | **GET** /linode/instances/{linodeId}/disks | Disks List |
| [**getLinodeFirewalls**](LinodeInstancesApi.md#getLinodeFirewalls) | **GET** /linode/instances/{linodeId}/firewalls | Firewalls List |
| [**getLinodeIP**](LinodeInstancesApi.md#getLinodeIP) | **GET** /linode/instances/{linodeId}/ips/{address} | IP Address View |
| [**getLinodeIPs**](LinodeInstancesApi.md#getLinodeIPs) | **GET** /linode/instances/{linodeId}/ips | Networking Information List |
| [**getLinodeInstance**](LinodeInstancesApi.md#getLinodeInstance) | **GET** /linode/instances/{linodeId} | Linode View |
| [**getLinodeInstances**](LinodeInstancesApi.md#getLinodeInstances) | **GET** /linode/instances | Linodes List |
| [**getLinodeNodeBalancers**](LinodeInstancesApi.md#getLinodeNodeBalancers) | **GET** /linode/instances/{linodeId}/nodebalancers | Linode NodeBalancers View |
| [**getLinodeStats**](LinodeInstancesApi.md#getLinodeStats) | **GET** /linode/instances/{linodeId}/stats | Linode Statistics View |
| [**getLinodeStatsByYearMonth**](LinodeInstancesApi.md#getLinodeStatsByYearMonth) | **GET** /linode/instances/{linodeId}/stats/{year}/{month} | Statistics View (year/month) |
| [**getLinodeTransfer**](LinodeInstancesApi.md#getLinodeTransfer) | **GET** /linode/instances/{linodeId}/transfer | Network Transfer View |
| [**getLinodeTransferByYearMonth**](LinodeInstancesApi.md#getLinodeTransferByYearMonth) | **GET** /linode/instances/{linodeId}/transfer/{year}/{month} | Network Transfer View (year/month) |
| [**getLinodeVolumes**](LinodeInstancesApi.md#getLinodeVolumes) | **GET** /linode/instances/{linodeId}/volumes | Linode&#39;s Volumes List |
| [**migrateLinodeInstance**](LinodeInstancesApi.md#migrateLinodeInstance) | **POST** /linode/instances/{linodeId}/migrate | DC Migration/Pending Host Migration Initiate |
| [**mutateLinodeInstance**](LinodeInstancesApi.md#mutateLinodeInstance) | **POST** /linode/instances/{linodeId}/mutate | Linode Upgrade |
| [**rebootLinodeInstance**](LinodeInstancesApi.md#rebootLinodeInstance) | **POST** /linode/instances/{linodeId}/reboot | Linode Reboot |
| [**rebuildLinodeInstance**](LinodeInstancesApi.md#rebuildLinodeInstance) | **POST** /linode/instances/{linodeId}/rebuild | Linode Rebuild |
| [**removeLinodeIP**](LinodeInstancesApi.md#removeLinodeIP) | **DELETE** /linode/instances/{linodeId}/ips/{address} | IPv4 Address Delete |
| [**rescueLinodeInstance**](LinodeInstancesApi.md#rescueLinodeInstance) | **POST** /linode/instances/{linodeId}/rescue | Linode Boot into Rescue Mode |
| [**resetDiskPassword**](LinodeInstancesApi.md#resetDiskPassword) | **POST** /linode/instances/{linodeId}/disks/{diskId}/password | Disk Root Password Reset |
| [**resetLinodePassword**](LinodeInstancesApi.md#resetLinodePassword) | **POST** /linode/instances/{linodeId}/password | Linode Root Password Reset |
| [**resizeDisk**](LinodeInstancesApi.md#resizeDisk) | **POST** /linode/instances/{linodeId}/disks/{diskId}/resize | Disk Resize |
| [**resizeLinodeInstance**](LinodeInstancesApi.md#resizeLinodeInstance) | **POST** /linode/instances/{linodeId}/resize | Linode Resize |
| [**restoreBackup**](LinodeInstancesApi.md#restoreBackup) | **POST** /linode/instances/{linodeId}/backups/{backupId}/restore | Backup Restore |
| [**shutdownLinodeInstance**](LinodeInstancesApi.md#shutdownLinodeInstance) | **POST** /linode/instances/{linodeId}/shutdown | Linode Shut Down |
| [**updateDisk**](LinodeInstancesApi.md#updateDisk) | **PUT** /linode/instances/{linodeId}/disks/{diskId} | Disk Update |
| [**updateLinodeConfig**](LinodeInstancesApi.md#updateLinodeConfig) | **PUT** /linode/instances/{linodeId}/configs/{configId} | Configuration Profile Update |
| [**updateLinodeIP**](LinodeInstancesApi.md#updateLinodeIP) | **PUT** /linode/instances/{linodeId}/ips/{address} | IP Address Update |
| [**updateLinodeInstance**](LinodeInstancesApi.md#updateLinodeInstance) | **PUT** /linode/instances/{linodeId} | Linode Update |


<a id="addLinodeConfig"></a>
# **addLinodeConfig**
> LinodeConfig addLinodeConfig(linodeId, linodeConfig)

Configuration Profile Create

Adds a new Configuration profile to a Linode. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LinodeInstancesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    LinodeInstancesApi apiInstance = new LinodeInstancesApi(defaultClient);
    Integer linodeId = 56; // Integer | ID of the Linode to look up Configuration profiles for.
    LinodeConfig linodeConfig = new LinodeConfig(); // LinodeConfig | The parameters to set when creating the Configuration profile. This determines which kernel, devices, how much memory, etc. a Linode boots with. 
    try {
      LinodeConfig result = apiInstance.addLinodeConfig(linodeId, linodeConfig);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LinodeInstancesApi#addLinodeConfig");
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
| **linodeId** | **Integer**| ID of the Linode to look up Configuration profiles for. | |
| **linodeConfig** | [**LinodeConfig**](LinodeConfig.md)| The parameters to set when creating the Configuration profile. This determines which kernel, devices, how much memory, etc. a Linode boots with.  | |

### Return type

[**LinodeConfig**](LinodeConfig.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A Configuration profile was created.  |  -  |
| **0** | Error |  -  |

<a id="addLinodeDisk"></a>
# **addLinodeDisk**
> Disk addLinodeDisk(linodeId, diskRequest)

Disk Create

Adds a new Disk to a Linode.  * You can optionally create a Disk from an Image or an Empty Disk if no Image is provided with a request.  * When creating an Empty Disk, providing a &#x60;label&#x60; is required.  * If no &#x60;label&#x60; is provided, an &#x60;image&#x60; is required instead.  * When creating a Disk from an Image, &#x60;root_pass&#x60; is required.  * The default filesystem for new Disks is &#x60;ext4&#x60;. If creating a Disk from an Image, the filesystem of the Image is used unless otherwise specified.  * When deploying a StackScript on a Disk:   * See StackScripts List ([GET /linode/stackscripts](/docs/api/stackscripts/#stackscripts-list)) for     a list of available StackScripts.   * Requires a compatible Image to be supplied.     * See StackScript View ([GET /linode/stackscript/{stackscriptId}](/docs/api/stackscripts/#stackscript-view)) for compatible Images.   * It is recommended to supply SSH keys for the root User using the &#x60;authorized_keys&#x60; field.   * You may also supply a list of usernames via the &#x60;authorized_users&#x60; field.     * These users must have an SSH Key associated with their Profiles first. See SSH Key Add ([POST /profile/sshkeys](/docs/api/profile/#ssh-key-add)) for more information. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LinodeInstancesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    LinodeInstancesApi apiInstance = new LinodeInstancesApi(defaultClient);
    Integer linodeId = 56; // Integer | ID of the Linode to look up.
    DiskRequest diskRequest = new DiskRequest(); // DiskRequest | The parameters to set when creating the Disk. 
    try {
      Disk result = apiInstance.addLinodeDisk(linodeId, diskRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LinodeInstancesApi#addLinodeDisk");
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
| **linodeId** | **Integer**| ID of the Linode to look up. | |
| **diskRequest** | [**DiskRequest**](DiskRequest.md)| The parameters to set when creating the Disk.  | |

### Return type

[**Disk**](Disk.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Disk created. |  -  |
| **0** | Error |  -  |

<a id="addLinodeIP"></a>
# **addLinodeIP**
> IPAddress addLinodeIP(linodeId, addLinodeIPRequest)

IPv4 Address Allocate

Allocates a public or private IPv4 address to a Linode. Public IP Addresses, after the one included with each Linode, incur an additional monthly charge. If you need an additional public IP Address you must request one - please [open a support ticket](/docs/api/support/#support-ticket-open). You may not add more than one private IPv4 address to a single Linode. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LinodeInstancesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    LinodeInstancesApi apiInstance = new LinodeInstancesApi(defaultClient);
    Integer linodeId = 56; // Integer | ID of the Linode to look up.
    AddLinodeIPRequest addLinodeIPRequest = new AddLinodeIPRequest(); // AddLinodeIPRequest | Information about the address you are creating.
    try {
      IPAddress result = apiInstance.addLinodeIP(linodeId, addLinodeIPRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LinodeInstancesApi#addLinodeIP");
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
| **linodeId** | **Integer**| ID of the Linode to look up. | |
| **addLinodeIPRequest** | [**AddLinodeIPRequest**](AddLinodeIPRequest.md)| Information about the address you are creating. | |

### Return type

[**IPAddress**](IPAddress.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | IP address was successfully allocated. |  -  |
| **0** | Error |  -  |

<a id="bootLinodeInstance"></a>
# **bootLinodeInstance**
> Object bootLinodeInstance(linodeId, bootLinodeInstanceRequest)

Linode Boot

Boots a Linode you have permission to modify. If no parameters are given, a Config profile will be chosen for this boot based on the following criteria:  * If there is only one Config profile for this Linode, it will be used. * If there is more than one Config profile, the last booted config will be used. * If there is more than one Config profile and none were the last to be booted (because the   Linode was never booted or the last booted config was deleted) an error will be returned. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LinodeInstancesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    LinodeInstancesApi apiInstance = new LinodeInstancesApi(defaultClient);
    Integer linodeId = 56; // Integer | The ID of the Linode to boot.
    BootLinodeInstanceRequest bootLinodeInstanceRequest = new BootLinodeInstanceRequest(); // BootLinodeInstanceRequest | Optional configuration to boot into (see above).
    try {
      Object result = apiInstance.bootLinodeInstance(linodeId, bootLinodeInstanceRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LinodeInstancesApi#bootLinodeInstance");
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
| **linodeId** | **Integer**| The ID of the Linode to boot. | |
| **bootLinodeInstanceRequest** | [**BootLinodeInstanceRequest**](BootLinodeInstanceRequest.md)| Optional configuration to boot into (see above). | [optional] |

### Return type

**Object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Boot started. |  -  |
| **0** | Error |  -  |

<a id="cancelBackups"></a>
# **cancelBackups**
> Object cancelBackups(linodeId)

Backups Cancel

Cancels the Backup service on the given Linode. Deletes all of this Linode&#39;s existing backups forever. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LinodeInstancesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    LinodeInstancesApi apiInstance = new LinodeInstancesApi(defaultClient);
    Integer linodeId = 56; // Integer | The ID of the Linode to cancel backup service for.
    try {
      Object result = apiInstance.cancelBackups(linodeId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LinodeInstancesApi#cancelBackups");
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
| **linodeId** | **Integer**| The ID of the Linode to cancel backup service for. | |

### Return type

**Object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Backup service was cancelled for the specified Linode. |  -  |
| **0** | Error |  -  |

<a id="cloneLinodeDisk"></a>
# **cloneLinodeDisk**
> Disk cloneLinodeDisk(linodeId, diskId)

Disk Clone

Copies a disk, byte-for-byte, into a new Disk belonging to the same Linode. The Linode must have enough storage space available to accept a new Disk of the same size as this one or this operation will fail. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LinodeInstancesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    LinodeInstancesApi apiInstance = new LinodeInstancesApi(defaultClient);
    Integer linodeId = 56; // Integer | ID of the Linode to look up.
    Integer diskId = 56; // Integer | ID of the Disk to clone.
    try {
      Disk result = apiInstance.cloneLinodeDisk(linodeId, diskId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LinodeInstancesApi#cloneLinodeDisk");
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
| **linodeId** | **Integer**| ID of the Linode to look up. | |
| **diskId** | **Integer**| ID of the Disk to clone. | |

### Return type

[**Disk**](Disk.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Disk clone initiated. |  -  |
| **0** | Error |  -  |

<a id="cloneLinodeInstance"></a>
# **cloneLinodeInstance**
> Linode cloneLinodeInstance(linodeId, cloneLinodeInstanceRequest)

Linode Clone

You can clone your Linode&#39;s existing Disks or Configuration profiles to another Linode on your Account. In order for this request to complete successfully, your User must have the &#x60;add_linodes&#x60; grant. Cloning to a new Linode will incur a charge on your Account.  If cloning to an existing Linode, any actions currently running or queued must be completed first before you can clone to it.  Up to five clone operations from any given source Linode can be run concurrently. If more concurrent clones are attempted, an HTTP 400 error will be returned by this endpoint.  Any [tags](/docs/api/tags/#tags-list) existing on the source Linode will be cloned to the target Linode. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LinodeInstancesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    LinodeInstancesApi apiInstance = new LinodeInstancesApi(defaultClient);
    Integer linodeId = 56; // Integer | ID of the Linode to clone.
    CloneLinodeInstanceRequest cloneLinodeInstanceRequest = new CloneLinodeInstanceRequest(); // CloneLinodeInstanceRequest | The requested state your Linode will be cloned into.
    try {
      Linode result = apiInstance.cloneLinodeInstance(linodeId, cloneLinodeInstanceRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LinodeInstancesApi#cloneLinodeInstance");
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
| **linodeId** | **Integer**| ID of the Linode to clone. | |
| **cloneLinodeInstanceRequest** | [**CloneLinodeInstanceRequest**](CloneLinodeInstanceRequest.md)| The requested state your Linode will be cloned into. | |

### Return type

[**Linode**](Linode.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Clone started. |  -  |
| **0** | Error |  -  |

<a id="createLinodeInstance"></a>
# **createLinodeInstance**
> Linode createLinodeInstance(createLinodeInstanceRequest)

Linode Create

Creates a Linode Instance on your Account. In order for this request to complete successfully, your User must have the &#x60;add_linodes&#x60; grant. Creating a new Linode will incur a charge on your Account.  Linodes can be created using one of the available Types. See Types List ([GET /linode/types](/docs/api/linode-types/#types-list)) to get more information about each Type&#39;s specs and cost.  Linodes can be created in any one of our available Regions, which are accessible from the Regions List ([GET /regions](/docs/api/regions/#regions-list)) endpoint.  In an effort to fight spam, Linode restricts outbound connections on ports 25, 465, and 587 on all Linodes for new accounts created after November 5th, 2019. For more information, see [Sending Email on Linode](/docs/guides/running-a-mail-server/#sending-email-on-linode).  Linodes can be created in a number of ways:  * Using a Linode Public Image distribution or a Private Image you created based on another Linode.   * Access the Images List ([GET /images](/docs/api/images/#images-list)) endpoint with authentication to view     all available Images.   * The Linode will be &#x60;running&#x60; after it completes &#x60;provisioning&#x60;.   * A default config with two Disks, one being a 512 swap disk, is created.     * &#x60;swap_size&#x60; can be used to customize the swap disk size.   * Requires a &#x60;root_pass&#x60; be supplied to use for the root User&#39;s Account.   * It is recommended to supply SSH keys for the root User using the &#x60;authorized_keys&#x60; field.   * You may also supply a list of usernames via the &#x60;authorized_users&#x60; field.     * These users must have an SSH Key associated with your Profile first. See SSH Key Add ([POST /profile/sshkeys](/docs/api/profile/#ssh-key-add)) for more information.  * Using a StackScript.   * See StackScripts List ([GET /linode/stackscripts](/docs/api/stackscripts/#stackscripts-list)) for     a list of available StackScripts.   * The Linode will be &#x60;running&#x60; after it completes &#x60;provisioning&#x60;.   * Requires a compatible Image to be supplied.     * See StackScript View ([GET /linode/stackscript/{stackscriptId}](/docs/api/stackscripts/#stackscript-view)) for compatible Images.   * Requires a &#x60;root_pass&#x60; be supplied to use for the root User&#39;s Account.   * It is recommended to supply SSH keys for the root User using the &#x60;authorized_keys&#x60; field.   * You may also supply a list of usernames via the &#x60;authorized_users&#x60; field.     * These users must have an SSH Key associated with your Profile first. See SSH Key Add ([POST /profile/sshkeys](/docs/api/profile/#ssh-key-add)) for more information.  * Using one of your other Linode&#39;s backups.   * You must create a Linode large enough to accommodate the Backup&#39;s size.   * The Disks and Config will match that of the Linode that was backed up.   * The &#x60;root_pass&#x60; will match that of the Linode that was backed up.  * Attached to a private VLAN.   * Review the &#x60;interfaces&#x60; property of the [Request Body Schema](/docs/api/linode-instances/#linode-create__request-body-schema) for details.   * For more information, see our guide on [Getting Started with VLANs](/docs/products/networking/vlans/get-started/).  * Create an empty Linode.   * The Linode will remain &#x60;offline&#x60; and must be manually started.     * See Linode Boot ([POST /linode/instances/{linodeId}/boot](/docs/api/linode-instances/#linode-boot)).   * Disks and Configs must be created manually.   * This is only recommended for advanced use cases.  **Important**: You must be an unrestricted User in order to add or modify tags on Linodes. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LinodeInstancesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    LinodeInstancesApi apiInstance = new LinodeInstancesApi(defaultClient);
    CreateLinodeInstanceRequest createLinodeInstanceRequest = new CreateLinodeInstanceRequest(); // CreateLinodeInstanceRequest | The requested initial state of a new Linode.
    try {
      Linode result = apiInstance.createLinodeInstance(createLinodeInstanceRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LinodeInstancesApi#createLinodeInstance");
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
| **createLinodeInstanceRequest** | [**CreateLinodeInstanceRequest**](CreateLinodeInstanceRequest.md)| The requested initial state of a new Linode. | |

### Return type

[**Linode**](Linode.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A new Linode is being created.  |  -  |
| **0** | Error |  -  |

<a id="createSnapshot"></a>
# **createSnapshot**
> Backup createSnapshot(linodeId, createSnapshotRequest)

Snapshot Create

Creates a snapshot Backup of a Linode.  **Important:** If you already have a snapshot of this Linode, this is a destructive action. The previous snapshot will be deleted. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LinodeInstancesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    LinodeInstancesApi apiInstance = new LinodeInstancesApi(defaultClient);
    Integer linodeId = 56; // Integer | The ID of the Linode the backups belong to.
    CreateSnapshotRequest createSnapshotRequest = new CreateSnapshotRequest(); // CreateSnapshotRequest | 
    try {
      Backup result = apiInstance.createSnapshot(linodeId, createSnapshotRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LinodeInstancesApi#createSnapshot");
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
| **linodeId** | **Integer**| The ID of the Linode the backups belong to. | |
| **createSnapshotRequest** | [**CreateSnapshotRequest**](CreateSnapshotRequest.md)|  | |

### Return type

[**Backup**](Backup.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Snapshot request successful. |  -  |
| **0** | Error |  -  |

<a id="deleteDisk"></a>
# **deleteDisk**
> Object deleteDisk(linodeId, diskId)

Disk Delete

Deletes a Disk you have permission to &#x60;read_write&#x60;.  **Deleting a Disk is a destructive action and cannot be undone.** 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LinodeInstancesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    LinodeInstancesApi apiInstance = new LinodeInstancesApi(defaultClient);
    Integer linodeId = 56; // Integer | ID of the Linode to look up.
    Integer diskId = 56; // Integer | ID of the Disk to look up.
    try {
      Object result = apiInstance.deleteDisk(linodeId, diskId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LinodeInstancesApi#deleteDisk");
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
| **linodeId** | **Integer**| ID of the Linode to look up. | |
| **diskId** | **Integer**| ID of the Disk to look up. | |

### Return type

**Object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Delete successful |  -  |
| **0** | Error |  -  |

<a id="deleteLinodeConfig"></a>
# **deleteLinodeConfig**
> Object deleteLinodeConfig(linodeId, configId)

Configuration Profile Delete

Deletes the specified Configuration profile from the specified Linode. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LinodeInstancesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    LinodeInstancesApi apiInstance = new LinodeInstancesApi(defaultClient);
    Integer linodeId = 56; // Integer | The ID of the Linode whose Configuration profile to look up.
    Integer configId = 56; // Integer | The ID of the Configuration profile to look up.
    try {
      Object result = apiInstance.deleteLinodeConfig(linodeId, configId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LinodeInstancesApi#deleteLinodeConfig");
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
| **linodeId** | **Integer**| The ID of the Linode whose Configuration profile to look up. | |
| **configId** | **Integer**| The ID of the Configuration profile to look up. | |

### Return type

**Object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Configuration profile successfully deleted.  |  -  |
| **0** | Error |  -  |

<a id="deleteLinodeInstance"></a>
# **deleteLinodeInstance**
> Object deleteLinodeInstance(linodeId)

Linode Delete

Deletes a Linode you have permission to &#x60;read_write&#x60;.  **Deleting a Linode is a destructive action and cannot be undone.**  Additionally, deleting a Linode:    * Gives up any IP addresses the Linode was assigned.   * Deletes all Disks, Backups, Configs, etc.   * Stops billing for the Linode and its associated services. You will be billed for time used     within the billing period the Linode was active.  Linodes that are in the process of [cloning](/docs/api/linode-instances/#linode-clone) or [backup restoration](/docs/api/linode-instances/#backup-restore) cannot be deleted. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LinodeInstancesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    LinodeInstancesApi apiInstance = new LinodeInstancesApi(defaultClient);
    Integer linodeId = 56; // Integer | ID of the Linode to look up
    try {
      Object result = apiInstance.deleteLinodeInstance(linodeId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LinodeInstancesApi#deleteLinodeInstance");
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
| **linodeId** | **Integer**| ID of the Linode to look up | |

### Return type

**Object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Delete successful |  -  |
| **0** | Error |  -  |

<a id="enableBackups"></a>
# **enableBackups**
> Object enableBackups(linodeId)

Backups Enable

Enables backups for the specified Linode. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LinodeInstancesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    LinodeInstancesApi apiInstance = new LinodeInstancesApi(defaultClient);
    Integer linodeId = 56; // Integer | The ID of the Linode to enable backup service for.
    try {
      Object result = apiInstance.enableBackups(linodeId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LinodeInstancesApi#enableBackups");
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
| **linodeId** | **Integer**| The ID of the Linode to enable backup service for. | |

### Return type

**Object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Backup service was enabled. |  -  |
| **0** | Error |  -  |

<a id="getBackup"></a>
# **getBackup**
> Backup getBackup(linodeId, backupId)

Backup View

Returns information about a Backup. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LinodeInstancesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    LinodeInstancesApi apiInstance = new LinodeInstancesApi(defaultClient);
    Integer linodeId = 56; // Integer | The ID of the Linode the Backup belongs to.
    Integer backupId = 56; // Integer | The ID of the Backup to look up.
    try {
      Backup result = apiInstance.getBackup(linodeId, backupId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LinodeInstancesApi#getBackup");
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
| **linodeId** | **Integer**| The ID of the Linode the Backup belongs to. | |
| **backupId** | **Integer**| The ID of the Backup to look up. | |

### Return type

[**Backup**](Backup.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A single Backup. |  -  |
| **0** | Error |  -  |

<a id="getBackups"></a>
# **getBackups**
> GetBackups200Response getBackups(linodeId)

Backups List

Returns information about this Linode&#39;s available backups. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LinodeInstancesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    LinodeInstancesApi apiInstance = new LinodeInstancesApi(defaultClient);
    Integer linodeId = 56; // Integer | The ID of the Linode the backups belong to.
    try {
      GetBackups200Response result = apiInstance.getBackups(linodeId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LinodeInstancesApi#getBackups");
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
| **linodeId** | **Integer**| The ID of the Linode the backups belong to. | |

### Return type

[**GetBackups200Response**](GetBackups200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A collection of the specified Linode&#39;s available backups. |  -  |
| **0** | Error |  -  |

<a id="getKernel"></a>
# **getKernel**
> Kernel getKernel(kernelId)

Kernel View

Returns information about a single Kernel. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LinodeInstancesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");

    LinodeInstancesApi apiInstance = new LinodeInstancesApi(defaultClient);
    String kernelId = "kernelId_example"; // String | ID of the Kernel to look up.
    try {
      Kernel result = apiInstance.getKernel(kernelId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LinodeInstancesApi#getKernel");
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
| **kernelId** | **String**| ID of the Kernel to look up. | |

### Return type

[**Kernel**](Kernel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A single Kernel object. |  -  |
| **0** | Error |  -  |

<a id="getKernels"></a>
# **getKernels**
> GetKernels200Response getKernels(page, pageSize)

Kernels List

Lists available Kernels. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LinodeInstancesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");

    LinodeInstancesApi apiInstance = new LinodeInstancesApi(defaultClient);
    Integer page = 1; // Integer | The page of a collection to return.
    Integer pageSize = 100; // Integer | The number of items to return per page.
    try {
      GetKernels200Response result = apiInstance.getKernels(page, pageSize);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LinodeInstancesApi#getKernels");
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
| **page** | **Integer**| The page of a collection to return. | [optional] [default to 1] |
| **pageSize** | **Integer**| The number of items to return per page. | [optional] [default to 100] |

### Return type

[**GetKernels200Response**](GetKernels200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns an array of Kernels. |  -  |
| **0** | Error |  -  |

<a id="getLinodeConfig"></a>
# **getLinodeConfig**
> LinodeConfig getLinodeConfig(linodeId, configId)

Configuration Profile View

Returns information about a specific Configuration profile. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LinodeInstancesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    LinodeInstancesApi apiInstance = new LinodeInstancesApi(defaultClient);
    Integer linodeId = 56; // Integer | The ID of the Linode whose Configuration profile to look up.
    Integer configId = 56; // Integer | The ID of the Configuration profile to look up.
    try {
      LinodeConfig result = apiInstance.getLinodeConfig(linodeId, configId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LinodeInstancesApi#getLinodeConfig");
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
| **linodeId** | **Integer**| The ID of the Linode whose Configuration profile to look up. | |
| **configId** | **Integer**| The ID of the Configuration profile to look up. | |

### Return type

[**LinodeConfig**](LinodeConfig.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A Configuration profile object. |  -  |
| **0** | Error |  -  |

<a id="getLinodeConfigs"></a>
# **getLinodeConfigs**
> GetLinodeConfigs200Response getLinodeConfigs(linodeId, page, pageSize)

Configuration Profiles List

Lists Configuration profiles associated with a Linode. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LinodeInstancesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    LinodeInstancesApi apiInstance = new LinodeInstancesApi(defaultClient);
    Integer linodeId = 56; // Integer | ID of the Linode to look up Configuration profiles for.
    Integer page = 1; // Integer | The page of a collection to return.
    Integer pageSize = 100; // Integer | The number of items to return per page.
    try {
      GetLinodeConfigs200Response result = apiInstance.getLinodeConfigs(linodeId, page, pageSize);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LinodeInstancesApi#getLinodeConfigs");
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
| **linodeId** | **Integer**| ID of the Linode to look up Configuration profiles for. | |
| **page** | **Integer**| The page of a collection to return. | [optional] [default to 1] |
| **pageSize** | **Integer**| The number of items to return per page. | [optional] [default to 100] |

### Return type

[**GetLinodeConfigs200Response**](GetLinodeConfigs200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns an array of Configuration profiles associated with this Linode.  |  -  |

<a id="getLinodeDisk"></a>
# **getLinodeDisk**
> Disk getLinodeDisk(linodeId, diskId)

Disk View

View Disk information for a Disk associated with this Linode. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LinodeInstancesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    LinodeInstancesApi apiInstance = new LinodeInstancesApi(defaultClient);
    Integer linodeId = 56; // Integer | ID of the Linode to look up.
    Integer diskId = 56; // Integer | ID of the Disk to look up.
    try {
      Disk result = apiInstance.getLinodeDisk(linodeId, diskId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LinodeInstancesApi#getLinodeDisk");
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
| **linodeId** | **Integer**| ID of the Linode to look up. | |
| **diskId** | **Integer**| ID of the Disk to look up. | |

### Return type

[**Disk**](Disk.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns a single Disk object. |  -  |
| **0** | Error |  -  |

<a id="getLinodeDisks"></a>
# **getLinodeDisks**
> GetLinodeDisks200Response getLinodeDisks(linodeId, page, pageSize)

Disks List

View Disk information for Disks associated with this Linode. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LinodeInstancesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    LinodeInstancesApi apiInstance = new LinodeInstancesApi(defaultClient);
    Integer linodeId = 56; // Integer | ID of the Linode to look up.
    Integer page = 1; // Integer | The page of a collection to return.
    Integer pageSize = 100; // Integer | The number of items to return per page.
    try {
      GetLinodeDisks200Response result = apiInstance.getLinodeDisks(linodeId, page, pageSize);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LinodeInstancesApi#getLinodeDisks");
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
| **linodeId** | **Integer**| ID of the Linode to look up. | |
| **page** | **Integer**| The page of a collection to return. | [optional] [default to 1] |
| **pageSize** | **Integer**| The number of items to return per page. | [optional] [default to 100] |

### Return type

[**GetLinodeDisks200Response**](GetLinodeDisks200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns a paginated list of disks associated with this Linode. |  -  |
| **0** | Error |  -  |

<a id="getLinodeFirewalls"></a>
# **getLinodeFirewalls**
> GetLinodeFirewalls200Response getLinodeFirewalls(linodeId, page, pageSize)

Firewalls List

View Firewall information for Firewalls associated with this Linode. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LinodeInstancesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    LinodeInstancesApi apiInstance = new LinodeInstancesApi(defaultClient);
    Integer linodeId = 56; // Integer | ID of the Linode to look up.
    Integer page = 1; // Integer | The page of a collection to return.
    Integer pageSize = 100; // Integer | The number of items to return per page.
    try {
      GetLinodeFirewalls200Response result = apiInstance.getLinodeFirewalls(linodeId, page, pageSize);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LinodeInstancesApi#getLinodeFirewalls");
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
| **linodeId** | **Integer**| ID of the Linode to look up. | |
| **page** | **Integer**| The page of a collection to return. | [optional] [default to 1] |
| **pageSize** | **Integer**| The number of items to return per page. | [optional] [default to 100] |

### Return type

[**GetLinodeFirewalls200Response**](GetLinodeFirewalls200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns a paginated list of Firewalls associated with this Linode. |  -  |
| **0** | Error |  -  |

<a id="getLinodeIP"></a>
# **getLinodeIP**
> IPAddress getLinodeIP(linodeId, address)

IP Address View

View information about the specified IP address associated with the specified Linode. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LinodeInstancesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    LinodeInstancesApi apiInstance = new LinodeInstancesApi(defaultClient);
    Integer linodeId = 56; // Integer | The ID of the Linode to look up.
    String address = "address_example"; // String | The IP address to look up.
    try {
      IPAddress result = apiInstance.getLinodeIP(linodeId, address);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LinodeInstancesApi#getLinodeIP");
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
| **linodeId** | **Integer**| The ID of the Linode to look up. | |
| **address** | **String**| The IP address to look up. | |

### Return type

[**IPAddress**](IPAddress.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A single IP address. |  -  |
| **0** | Error |  -  |

<a id="getLinodeIPs"></a>
# **getLinodeIPs**
> GetLinodeIPs200Response getLinodeIPs(linodeId)

Networking Information List

Returns networking information for a single Linode. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LinodeInstancesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    LinodeInstancesApi apiInstance = new LinodeInstancesApi(defaultClient);
    Integer linodeId = 56; // Integer | ID of the Linode to look up.
    try {
      GetLinodeIPs200Response result = apiInstance.getLinodeIPs(linodeId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LinodeInstancesApi#getLinodeIPs");
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
| **linodeId** | **Integer**| ID of the Linode to look up. | |

### Return type

[**GetLinodeIPs200Response**](GetLinodeIPs200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Requested Linode&#39;s networking configuration. |  -  |
| **0** | Error |  -  |

<a id="getLinodeInstance"></a>
# **getLinodeInstance**
> Linode getLinodeInstance(linodeId)

Linode View

Get a specific Linode by ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LinodeInstancesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    LinodeInstancesApi apiInstance = new LinodeInstancesApi(defaultClient);
    Integer linodeId = 56; // Integer | ID of the Linode to look up
    try {
      Linode result = apiInstance.getLinodeInstance(linodeId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LinodeInstancesApi#getLinodeInstance");
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
| **linodeId** | **Integer**| ID of the Linode to look up | |

### Return type

[**Linode**](Linode.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns a single Linode object. |  -  |
| **0** | Error |  -  |

<a id="getLinodeInstances"></a>
# **getLinodeInstances**
> GetLinodeInstances200Response getLinodeInstances(page, pageSize)

Linodes List

Returns a paginated list of Linodes you have permission to view. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LinodeInstancesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    LinodeInstancesApi apiInstance = new LinodeInstancesApi(defaultClient);
    Integer page = 1; // Integer | The page of a collection to return.
    Integer pageSize = 100; // Integer | The number of items to return per page.
    try {
      GetLinodeInstances200Response result = apiInstance.getLinodeInstances(page, pageSize);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LinodeInstancesApi#getLinodeInstances");
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
| **page** | **Integer**| The page of a collection to return. | [optional] [default to 1] |
| **pageSize** | **Integer**| The number of items to return per page. | [optional] [default to 100] |

### Return type

[**GetLinodeInstances200Response**](GetLinodeInstances200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns an array of all Linodes on your Account. |  -  |
| **0** | Error |  -  |

<a id="getLinodeNodeBalancers"></a>
# **getLinodeNodeBalancers**
> GetLinodeNodeBalancers200Response getLinodeNodeBalancers(linodeId)

Linode NodeBalancers View

Returns a list of NodeBalancers that are assigned to this Linode and readable by the requesting User.  Read permission to a NodeBalancer can be given to a User by accessing the User&#39;s Grants Update ([PUT /account/users/{username}/grants](/docs/api/account/#users-grants-update)) endpoint. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LinodeInstancesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    LinodeInstancesApi apiInstance = new LinodeInstancesApi(defaultClient);
    Integer linodeId = 56; // Integer | ID of the Linode to look up
    try {
      GetLinodeNodeBalancers200Response result = apiInstance.getLinodeNodeBalancers(linodeId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LinodeInstancesApi#getLinodeNodeBalancers");
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
| **linodeId** | **Integer**| ID of the Linode to look up | |

### Return type

[**GetLinodeNodeBalancers200Response**](GetLinodeNodeBalancers200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns a paginated list of NodeBalancers. |  -  |

<a id="getLinodeStats"></a>
# **getLinodeStats**
> LinodeStats getLinodeStats(linodeId)

Linode Statistics View

Returns CPU, IO, IPv4, and IPv6 statistics for your Linode for the past 24 hours. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LinodeInstancesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    LinodeInstancesApi apiInstance = new LinodeInstancesApi(defaultClient);
    Integer linodeId = 56; // Integer | ID of the Linode to look up.
    try {
      LinodeStats result = apiInstance.getLinodeStats(linodeId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LinodeInstancesApi#getLinodeStats");
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
| **linodeId** | **Integer**| ID of the Linode to look up. | |

### Return type

[**LinodeStats**](LinodeStats.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The Linode&#39;s stats for the past 24 hours. |  -  |
| **0** | Error |  -  |

<a id="getLinodeStatsByYearMonth"></a>
# **getLinodeStatsByYearMonth**
> LinodeStats getLinodeStatsByYearMonth(linodeId, year, month)

Statistics View (year/month)

Returns statistics for a specific month. The year/month values must be either a date in the past, or the current month. If the current month, statistics will be retrieved for the past 30 days. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LinodeInstancesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    LinodeInstancesApi apiInstance = new LinodeInstancesApi(defaultClient);
    Integer linodeId = 56; // Integer | ID of the Linode to look up.
    Integer year = 56; // Integer | Numeric value representing the year to look up.
    Integer month = 56; // Integer | Numeric value representing the month to look up.
    try {
      LinodeStats result = apiInstance.getLinodeStatsByYearMonth(linodeId, year, month);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LinodeInstancesApi#getLinodeStatsByYearMonth");
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
| **linodeId** | **Integer**| ID of the Linode to look up. | |
| **year** | **Integer**| Numeric value representing the year to look up. | |
| **month** | **Integer**| Numeric value representing the month to look up. | |

### Return type

[**LinodeStats**](LinodeStats.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The Linode&#39;s statistics for the requested period. |  -  |
| **0** | Error |  -  |

<a id="getLinodeTransfer"></a>
# **getLinodeTransfer**
> GetLinodeTransfer200Response getLinodeTransfer(linodeId)

Network Transfer View

Returns a Linode&#39;s network transfer pool statistics for the current month. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LinodeInstancesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    LinodeInstancesApi apiInstance = new LinodeInstancesApi(defaultClient);
    Integer linodeId = 56; // Integer | ID of the Linode to look up.
    try {
      GetLinodeTransfer200Response result = apiInstance.getLinodeTransfer(linodeId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LinodeInstancesApi#getLinodeTransfer");
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
| **linodeId** | **Integer**| ID of the Linode to look up. | |

### Return type

[**GetLinodeTransfer200Response**](GetLinodeTransfer200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A collection of the specified Linode&#39;s network transfer statistics. |  -  |
| **0** | Error |  -  |

<a id="getLinodeTransferByYearMonth"></a>
# **getLinodeTransferByYearMonth**
> GetLinodeTransferByYearMonth200Response getLinodeTransferByYearMonth(linodeId, year, month)

Network Transfer View (year/month)

Returns a Linode&#39;s network transfer statistics for a specific month. The year/month values must be either a date in the past, or the current month. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LinodeInstancesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    LinodeInstancesApi apiInstance = new LinodeInstancesApi(defaultClient);
    Integer linodeId = 56; // Integer | ID of the Linode to look up.
    Integer year = 56; // Integer | Numeric value representing the year to look up.
    Integer month = 56; // Integer | Numeric value representing the month to look up.
    try {
      GetLinodeTransferByYearMonth200Response result = apiInstance.getLinodeTransferByYearMonth(linodeId, year, month);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LinodeInstancesApi#getLinodeTransferByYearMonth");
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
| **linodeId** | **Integer**| ID of the Linode to look up. | |
| **year** | **Integer**| Numeric value representing the year to look up. | |
| **month** | **Integer**| Numeric value representing the month to look up. | |

### Return type

[**GetLinodeTransferByYearMonth200Response**](GetLinodeTransferByYearMonth200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A collection of the specified Linode&#39;s network transfer statistics for the requested month.  |  -  |
| **0** | Error |  -  |

<a id="getLinodeVolumes"></a>
# **getLinodeVolumes**
> GetLinodeVolumes200Response getLinodeVolumes(linodeId, page, pageSize)

Linode&#39;s Volumes List

View Block Storage Volumes attached to this Linode. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LinodeInstancesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    LinodeInstancesApi apiInstance = new LinodeInstancesApi(defaultClient);
    Integer linodeId = 56; // Integer | ID of the Linode to look up.
    Integer page = 1; // Integer | The page of a collection to return.
    Integer pageSize = 100; // Integer | The number of items to return per page.
    try {
      GetLinodeVolumes200Response result = apiInstance.getLinodeVolumes(linodeId, page, pageSize);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LinodeInstancesApi#getLinodeVolumes");
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
| **linodeId** | **Integer**| ID of the Linode to look up. | |
| **page** | **Integer**| The page of a collection to return. | [optional] [default to 1] |
| **pageSize** | **Integer**| The number of items to return per page. | [optional] [default to 100] |

### Return type

[**GetLinodeVolumes200Response**](GetLinodeVolumes200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns an array of Block Storage Volumes attached to this Linode.  |  -  |
| **0** | Error |  -  |

<a id="migrateLinodeInstance"></a>
# **migrateLinodeInstance**
> Object migrateLinodeInstance(linodeId, migrateLinodeInstanceRequest)

DC Migration/Pending Host Migration Initiate

Initiate a pending host migration that has been scheduled by Linode or initiate a cross data center (DC) migration.  A list of pending migrations, if any, can be accessed from [GET /account/notifications](/docs/api/account/#notifications-list). When the migration begins, your Linode will be shutdown if not already off. If the migration initiated the shutdown, it will reboot the Linode when completed.  To initiate a cross DC migration, you must pass a &#x60;region&#x60; parameter to the request body specifying the target data center region. You can view a list of all available regions and their feature capabilities from [GET /regions](/docs/api/regions/#regions-list). If your Linode has a DC migration already queued or you have initiated a previously scheduled migration, you will not be able to initiate a DC migration until it has completed.  **Note:** Next Generation Network (NGN) data centers do not support IPv6 &#x60;/116&#x60; pools or IP Failover. If you have these features enabled on your Linode and attempt to migrate to an NGN data center, the migration will not initiate. If a Linode cannot be migrated because of an incompatibility, you will be prompted to select a different data center or contact support. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LinodeInstancesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    LinodeInstancesApi apiInstance = new LinodeInstancesApi(defaultClient);
    Integer linodeId = 56; // Integer | ID of the Linode to migrate.
    MigrateLinodeInstanceRequest migrateLinodeInstanceRequest = new MigrateLinodeInstanceRequest(); // MigrateLinodeInstanceRequest | 
    try {
      Object result = apiInstance.migrateLinodeInstance(linodeId, migrateLinodeInstanceRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LinodeInstancesApi#migrateLinodeInstance");
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
| **linodeId** | **Integer**| ID of the Linode to migrate. | |
| **migrateLinodeInstanceRequest** | [**MigrateLinodeInstanceRequest**](MigrateLinodeInstanceRequest.md)|  | [optional] |

### Return type

**Object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Scheduled migration started |  -  |
| **0** | Error |  -  |

<a id="mutateLinodeInstance"></a>
# **mutateLinodeInstance**
> Object mutateLinodeInstance(linodeId, mutateLinodeInstanceRequest)

Linode Upgrade

Linodes created with now-deprecated Types are entitled to a free upgrade to the next generation. A mutating Linode will be allocated any new resources the upgraded Type provides, and will be subsequently restarted if it was currently running. If any actions are currently running or queued, those actions must be completed first before you can initiate a mutate. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LinodeInstancesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    LinodeInstancesApi apiInstance = new LinodeInstancesApi(defaultClient);
    Integer linodeId = 56; // Integer | ID of the Linode to mutate.
    MutateLinodeInstanceRequest mutateLinodeInstanceRequest = new MutateLinodeInstanceRequest(); // MutateLinodeInstanceRequest | Whether to automatically resize disks or not.
    try {
      Object result = apiInstance.mutateLinodeInstance(linodeId, mutateLinodeInstanceRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LinodeInstancesApi#mutateLinodeInstance");
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
| **linodeId** | **Integer**| ID of the Linode to mutate. | |
| **mutateLinodeInstanceRequest** | [**MutateLinodeInstanceRequest**](MutateLinodeInstanceRequest.md)| Whether to automatically resize disks or not. | [optional] |

### Return type

**Object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Mutate started. |  -  |
| **0** | Error |  -  |

<a id="rebootLinodeInstance"></a>
# **rebootLinodeInstance**
> Object rebootLinodeInstance(linodeId, rebootLinodeInstanceRequest)

Linode Reboot

Reboots a Linode you have permission to modify. If any actions are currently running or queued, those actions must be completed first before you can initiate a reboot. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LinodeInstancesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    LinodeInstancesApi apiInstance = new LinodeInstancesApi(defaultClient);
    Integer linodeId = 56; // Integer | ID of the linode to reboot.
    RebootLinodeInstanceRequest rebootLinodeInstanceRequest = new RebootLinodeInstanceRequest(); // RebootLinodeInstanceRequest | Optional reboot parameters.
    try {
      Object result = apiInstance.rebootLinodeInstance(linodeId, rebootLinodeInstanceRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LinodeInstancesApi#rebootLinodeInstance");
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
| **linodeId** | **Integer**| ID of the linode to reboot. | |
| **rebootLinodeInstanceRequest** | [**RebootLinodeInstanceRequest**](RebootLinodeInstanceRequest.md)| Optional reboot parameters. | [optional] |

### Return type

**Object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Reboot started. |  -  |
| **0** | Error |  -  |

<a id="rebuildLinodeInstance"></a>
# **rebuildLinodeInstance**
> Linode rebuildLinodeInstance(linodeId, UNKNOWN_BASE_TYPE)

Linode Rebuild

Rebuilds a Linode you have the &#x60;read_write&#x60; permission to modify. A rebuild will first shut down the Linode, delete all disks and configs on the Linode, and then deploy a new &#x60;image&#x60; to the Linode with the given attributes. Additionally:    * Requires an &#x60;image&#x60; be supplied.   * Requires a &#x60;root_pass&#x60; be supplied to use for the root User&#39;s Account.   * It is recommended to supply SSH keys for the root User using the     &#x60;authorized_keys&#x60; field. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LinodeInstancesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    LinodeInstancesApi apiInstance = new LinodeInstancesApi(defaultClient);
    Integer linodeId = 56; // Integer | ID of the Linode to rebuild.
    UNKNOWN_BASE_TYPE UNKNOWN_BASE_TYPE = new HashMap(); // UNKNOWN_BASE_TYPE | The requested state your Linode will be rebuilt into.
    try {
      Linode result = apiInstance.rebuildLinodeInstance(linodeId, UNKNOWN_BASE_TYPE);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LinodeInstancesApi#rebuildLinodeInstance");
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
| **linodeId** | **Integer**| ID of the Linode to rebuild. | |
| **UNKNOWN_BASE_TYPE** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)| The requested state your Linode will be rebuilt into. | |

### Return type

[**Linode**](Linode.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Rebuild started. |  -  |
| **0** | Error |  -  |

<a id="removeLinodeIP"></a>
# **removeLinodeIP**
> Object removeLinodeIP(linodeId, address)

IPv4 Address Delete

Deletes a public or private IPv4 address associated with this Linode. This will fail if it is the Linode&#39;s last remaining public IPv4 address. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LinodeInstancesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    LinodeInstancesApi apiInstance = new LinodeInstancesApi(defaultClient);
    Integer linodeId = 56; // Integer | The ID of the Linode to look up.
    String address = "address_example"; // String | The IP address to look up.
    try {
      Object result = apiInstance.removeLinodeIP(linodeId, address);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LinodeInstancesApi#removeLinodeIP");
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
| **linodeId** | **Integer**| The ID of the Linode to look up. | |
| **address** | **String**| The IP address to look up. | |

### Return type

**Object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | IP address successfully removed. |  -  |
| **0** | Error |  -  |

<a id="rescueLinodeInstance"></a>
# **rescueLinodeInstance**
> Object rescueLinodeInstance(linodeId, rescueLinodeInstanceRequest)

Linode Boot into Rescue Mode

Rescue Mode is a safe environment for performing many system recovery and disk management tasks. Rescue Mode is based on the Finnix recovery distribution, a self-contained and bootable Linux distribution. You can also use Rescue Mode for tasks other than disaster recovery, such as formatting disks to use different filesystems, copying data between disks, and downloading files from a disk via SSH and SFTP. * Note that \&quot;sdh\&quot; is reserved and unavailable during rescue. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LinodeInstancesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    LinodeInstancesApi apiInstance = new LinodeInstancesApi(defaultClient);
    Integer linodeId = 56; // Integer | ID of the Linode to rescue.
    RescueLinodeInstanceRequest rescueLinodeInstanceRequest = new RescueLinodeInstanceRequest(); // RescueLinodeInstanceRequest | Optional object of devices to be mounted.
    try {
      Object result = apiInstance.rescueLinodeInstance(linodeId, rescueLinodeInstanceRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LinodeInstancesApi#rescueLinodeInstance");
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
| **linodeId** | **Integer**| ID of the Linode to rescue. | |
| **rescueLinodeInstanceRequest** | [**RescueLinodeInstanceRequest**](RescueLinodeInstanceRequest.md)| Optional object of devices to be mounted. | [optional] |

### Return type

**Object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Rescue started. |  -  |
| **0** | Error |  -  |

<a id="resetDiskPassword"></a>
# **resetDiskPassword**
> Object resetDiskPassword(linodeId, diskId, resetDiskPasswordRequest)

Disk Root Password Reset

Resets the password of a Disk you have permission to &#x60;read_write&#x60;. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LinodeInstancesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    LinodeInstancesApi apiInstance = new LinodeInstancesApi(defaultClient);
    Integer linodeId = 56; // Integer | ID of the Linode to look up.
    Integer diskId = 56; // Integer | ID of the Disk to look up.
    ResetDiskPasswordRequest resetDiskPasswordRequest = new ResetDiskPasswordRequest(); // ResetDiskPasswordRequest | The new password.
    try {
      Object result = apiInstance.resetDiskPassword(linodeId, diskId, resetDiskPasswordRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LinodeInstancesApi#resetDiskPassword");
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
| **linodeId** | **Integer**| ID of the Linode to look up. | |
| **diskId** | **Integer**| ID of the Disk to look up. | |
| **resetDiskPasswordRequest** | [**ResetDiskPasswordRequest**](ResetDiskPasswordRequest.md)| The new password. | |

### Return type

**Object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns a single Disk object. |  -  |
| **0** | Error |  -  |

<a id="resetLinodePassword"></a>
# **resetLinodePassword**
> Object resetLinodePassword(linodeId, resetLinodePasswordRequest)

Linode Root Password Reset

Resets the root password for this Linode. * Your Linode must be [shut down](/docs/api/linode-instances/#linode-shut-down) for a password reset to complete. * If your Linode has more than one disk (not counting its swap disk), use the [Reset Disk Root Password](/docs/api/linode-instances/#disk-root-password-reset) endpoint to update a specific disk&#39;s root password. * A &#x60;password_reset&#x60; event is generated when a root password reset is successful. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LinodeInstancesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    LinodeInstancesApi apiInstance = new LinodeInstancesApi(defaultClient);
    Integer linodeId = 56; // Integer | ID of the Linode for which to reset its root password.
    ResetLinodePasswordRequest resetLinodePasswordRequest = new ResetLinodePasswordRequest(); // ResetLinodePasswordRequest | This Linode's new root password.
    try {
      Object result = apiInstance.resetLinodePassword(linodeId, resetLinodePasswordRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LinodeInstancesApi#resetLinodePassword");
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
| **linodeId** | **Integer**| ID of the Linode for which to reset its root password. | |
| **resetLinodePasswordRequest** | [**ResetLinodePasswordRequest**](ResetLinodePasswordRequest.md)| This Linode&#39;s new root password. | [optional] |

### Return type

**Object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Password Reset. |  -  |
| **0** | Error |  -  |

<a id="resizeDisk"></a>
# **resizeDisk**
> Object resizeDisk(linodeId, diskId, resizeDiskRequest)

Disk Resize

Resizes a Disk you have permission to &#x60;read_write&#x60;.  The Disk must not be in use. If the Disk is in use, the request will succeed but the resize will ultimately fail. For a request to succeed, the Linode must be shut down prior to resizing the Disk, or the Disk must not be assigned to the Linode&#39;s active Configuration Profile.  If you are resizing the Disk to a smaller size, it cannot be made smaller than what is required by the total size of the files current on the Disk. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LinodeInstancesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    LinodeInstancesApi apiInstance = new LinodeInstancesApi(defaultClient);
    Integer linodeId = 56; // Integer | ID of the Linode to look up.
    Integer diskId = 56; // Integer | ID of the Disk to look up.
    ResizeDiskRequest resizeDiskRequest = new ResizeDiskRequest(); // ResizeDiskRequest | The new size of the Disk.
    try {
      Object result = apiInstance.resizeDisk(linodeId, diskId, resizeDiskRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LinodeInstancesApi#resizeDisk");
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
| **linodeId** | **Integer**| ID of the Linode to look up. | |
| **diskId** | **Integer**| ID of the Disk to look up. | |
| **resizeDiskRequest** | [**ResizeDiskRequest**](ResizeDiskRequest.md)| The new size of the Disk. | |

### Return type

**Object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Resize started. |  -  |
| **0** | Error |  -  |

<a id="resizeLinodeInstance"></a>
# **resizeLinodeInstance**
> Object resizeLinodeInstance(linodeId, resizeLinodeInstanceRequest)

Linode Resize

Resizes a Linode you have the &#x60;read_write&#x60; permission to a different Type. If any actions are currently running or queued, those actions must be completed first before you can initiate a resize. Additionally, the following criteria must be met in order to resize a Linode:    * The Linode must not have a pending migration.   * Your Account cannot have an outstanding balance.   * The Linode must not have more disk allocation than the new Type allows.     * In that situation, you must first delete or resize the disk to be smaller. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LinodeInstancesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    LinodeInstancesApi apiInstance = new LinodeInstancesApi(defaultClient);
    Integer linodeId = 56; // Integer | ID of the Linode to resize.
    ResizeLinodeInstanceRequest resizeLinodeInstanceRequest = new ResizeLinodeInstanceRequest(); // ResizeLinodeInstanceRequest | The Type your current Linode will resize to, and whether to attempt to automatically resize the Linode's disks. 
    try {
      Object result = apiInstance.resizeLinodeInstance(linodeId, resizeLinodeInstanceRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LinodeInstancesApi#resizeLinodeInstance");
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
| **linodeId** | **Integer**| ID of the Linode to resize. | |
| **resizeLinodeInstanceRequest** | [**ResizeLinodeInstanceRequest**](ResizeLinodeInstanceRequest.md)| The Type your current Linode will resize to, and whether to attempt to automatically resize the Linode&#39;s disks.  | |

### Return type

**Object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Resize started. |  -  |
| **0** | Error |  -  |

<a id="restoreBackup"></a>
# **restoreBackup**
> Object restoreBackup(linodeId, backupId, restoreBackupRequest)

Backup Restore

Restores a Linode&#39;s Backup to the specified Linode. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LinodeInstancesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    LinodeInstancesApi apiInstance = new LinodeInstancesApi(defaultClient);
    Integer linodeId = 56; // Integer | The ID of the Linode that the Backup belongs to.
    Integer backupId = 56; // Integer | The ID of the Backup to restore.
    RestoreBackupRequest restoreBackupRequest = new RestoreBackupRequest(); // RestoreBackupRequest | Parameters to provide when restoring the Backup.
    try {
      Object result = apiInstance.restoreBackup(linodeId, backupId, restoreBackupRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LinodeInstancesApi#restoreBackup");
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
| **linodeId** | **Integer**| The ID of the Linode that the Backup belongs to. | |
| **backupId** | **Integer**| The ID of the Backup to restore. | |
| **restoreBackupRequest** | [**RestoreBackupRequest**](RestoreBackupRequest.md)| Parameters to provide when restoring the Backup. | |

### Return type

**Object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Restore from Backup was initiated. |  -  |
| **0** | Error |  -  |

<a id="shutdownLinodeInstance"></a>
# **shutdownLinodeInstance**
> Object shutdownLinodeInstance(linodeId)

Linode Shut Down

Shuts down a Linode you have permission to modify. If any actions are currently running or queued, those actions must be completed first before you can initiate a shutdown. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LinodeInstancesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    LinodeInstancesApi apiInstance = new LinodeInstancesApi(defaultClient);
    Integer linodeId = 56; // Integer | ID of the Linode to shutdown.
    try {
      Object result = apiInstance.shutdownLinodeInstance(linodeId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LinodeInstancesApi#shutdownLinodeInstance");
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
| **linodeId** | **Integer**| ID of the Linode to shutdown. | |

### Return type

**Object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Shutdown started. |  -  |
| **0** | Error |  -  |

<a id="updateDisk"></a>
# **updateDisk**
> Disk updateDisk(linodeId, diskId, disk)

Disk Update

Updates a Disk that you have permission to &#x60;read_write&#x60;. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LinodeInstancesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    LinodeInstancesApi apiInstance = new LinodeInstancesApi(defaultClient);
    Integer linodeId = 56; // Integer | ID of the Linode to look up.
    Integer diskId = 56; // Integer | ID of the Disk to look up.
    Disk disk = new Disk(); // Disk | Updates the parameters of a single Disk. 
    try {
      Disk result = apiInstance.updateDisk(linodeId, diskId, disk);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LinodeInstancesApi#updateDisk");
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
| **linodeId** | **Integer**| ID of the Linode to look up. | |
| **diskId** | **Integer**| ID of the Disk to look up. | |
| **disk** | [**Disk**](Disk.md)| Updates the parameters of a single Disk.  | |

### Return type

[**Disk**](Disk.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The updated Disk. |  -  |
| **0** | Error |  -  |

<a id="updateLinodeConfig"></a>
# **updateLinodeConfig**
> LinodeConfig updateLinodeConfig(linodeId, configId, linodeConfig)

Configuration Profile Update

Updates a Configuration profile. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LinodeInstancesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    LinodeInstancesApi apiInstance = new LinodeInstancesApi(defaultClient);
    Integer linodeId = 56; // Integer | The ID of the Linode whose Configuration profile to look up.
    Integer configId = 56; // Integer | The ID of the Configuration profile to look up.
    LinodeConfig linodeConfig = new LinodeConfig(); // LinodeConfig | The Configuration profile parameters to modify.
    try {
      LinodeConfig result = apiInstance.updateLinodeConfig(linodeId, configId, linodeConfig);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LinodeInstancesApi#updateLinodeConfig");
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
| **linodeId** | **Integer**| The ID of the Linode whose Configuration profile to look up. | |
| **configId** | **Integer**| The ID of the Configuration profile to look up. | |
| **linodeConfig** | [**LinodeConfig**](LinodeConfig.md)| The Configuration profile parameters to modify. | |

### Return type

[**LinodeConfig**](LinodeConfig.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Configuration profile successfully updated. |  -  |
| **0** | Error |  -  |

<a id="updateLinodeIP"></a>
# **updateLinodeIP**
> IPAddress updateLinodeIP(linodeId, address, updateLinodeIPRequest)

IP Address Update

Updates a the reverse DNS (RDNS) for a particular IP Address associated with this Linode.  Setting the RDNS to &#x60;null&#x60; for a public IPv4 address, resets it to the default \&quot;ip.linodeusercontent.com\&quot; RDNS value. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LinodeInstancesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    LinodeInstancesApi apiInstance = new LinodeInstancesApi(defaultClient);
    Integer linodeId = 56; // Integer | The ID of the Linode to look up.
    String address = "address_example"; // String | The IP address to look up.
    UpdateLinodeIPRequest updateLinodeIPRequest = new UpdateLinodeIPRequest(); // UpdateLinodeIPRequest | The information to update for the IP address.
    try {
      IPAddress result = apiInstance.updateLinodeIP(linodeId, address, updateLinodeIPRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LinodeInstancesApi#updateLinodeIP");
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
| **linodeId** | **Integer**| The ID of the Linode to look up. | |
| **address** | **String**| The IP address to look up. | |
| **updateLinodeIPRequest** | [**UpdateLinodeIPRequest**](UpdateLinodeIPRequest.md)| The information to update for the IP address. | [optional] |

### Return type

[**IPAddress**](IPAddress.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The updated IP address record. |  -  |
| **0** | Error |  -  |

<a id="updateLinodeInstance"></a>
# **updateLinodeInstance**
> Linode updateLinodeInstance(linodeId, linode)

Linode Update

Updates a Linode that you have permission to &#x60;read_write&#x60;.  **Important**: You must be an unrestricted User in order to add or modify tags on Linodes. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LinodeInstancesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    LinodeInstancesApi apiInstance = new LinodeInstancesApi(defaultClient);
    Integer linodeId = 56; // Integer | ID of the Linode to look up
    Linode linode = new Linode(); // Linode | Any field that is not marked as `readOnly` may be updated. Fields that are marked `readOnly` will be ignored. If any updated field fails to pass validation, the Linode will not be updated. 
    try {
      Linode result = apiInstance.updateLinodeInstance(linodeId, linode);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LinodeInstancesApi#updateLinodeInstance");
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
| **linodeId** | **Integer**| ID of the Linode to look up | |
| **linode** | [**Linode**](Linode.md)| Any field that is not marked as &#x60;readOnly&#x60; may be updated. Fields that are marked &#x60;readOnly&#x60; will be ignored. If any updated field fails to pass validation, the Linode will not be updated.  | |

### Return type

[**Linode**](Linode.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The updated Linode. |  -  |
| **0** | Error |  -  |

