# InventoryApi

All URIs are relative to *https://api.meraki.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**claimIntoOrganizationInventory_1**](InventoryApi.md#claimIntoOrganizationInventory_1) | **POST** /organizations/{organizationId}/inventory/claim | Claim a list of devices, licenses, and/or orders into an organization inventory |
| [**createOrganizationInventoryOnboardingCloudMonitoringExportEvent_1**](InventoryApi.md#createOrganizationInventoryOnboardingCloudMonitoringExportEvent_1) | **POST** /organizations/{organizationId}/inventory/onboarding/cloudMonitoring/exportEvents | Imports event logs related to the onboarding app into elastisearch |
| [**createOrganizationInventoryOnboardingCloudMonitoringImport_1**](InventoryApi.md#createOrganizationInventoryOnboardingCloudMonitoringImport_1) | **POST** /organizations/{organizationId}/inventory/onboarding/cloudMonitoring/imports | Commits the import operation to complete the onboarding of a device into Dashboard for monitoring. |
| [**createOrganizationInventoryOnboardingCloudMonitoringPrepare_1**](InventoryApi.md#createOrganizationInventoryOnboardingCloudMonitoringPrepare_1) | **POST** /organizations/{organizationId}/inventory/onboarding/cloudMonitoring/prepare | Initiates or updates an import session |
| [**getOrganizationInventoryDevice_1**](InventoryApi.md#getOrganizationInventoryDevice_1) | **GET** /organizations/{organizationId}/inventory/devices/{serial} | Return a single device from the inventory of an organization |
| [**getOrganizationInventoryDevices_1**](InventoryApi.md#getOrganizationInventoryDevices_1) | **GET** /organizations/{organizationId}/inventory/devices | Return the device inventory for an organization |
| [**getOrganizationInventoryOnboardingCloudMonitoringImports_1**](InventoryApi.md#getOrganizationInventoryOnboardingCloudMonitoringImports_1) | **GET** /organizations/{organizationId}/inventory/onboarding/cloudMonitoring/imports | Check the status of a committed Import operation |
| [**getOrganizationInventoryOnboardingCloudMonitoringNetworks_1**](InventoryApi.md#getOrganizationInventoryOnboardingCloudMonitoringNetworks_1) | **GET** /organizations/{organizationId}/inventory/onboarding/cloudMonitoring/networks | Returns list of networks eligible for adding cloud monitored device |
| [**releaseFromOrganizationInventory_1**](InventoryApi.md#releaseFromOrganizationInventory_1) | **POST** /organizations/{organizationId}/inventory/release | Release a list of claimed devices from an organization. |


<a id="claimIntoOrganizationInventory_1"></a>
# **claimIntoOrganizationInventory_1**
> Object claimIntoOrganizationInventory_1(organizationId, claimIntoOrganizationInventoryRequest)

Claim a list of devices, licenses, and/or orders into an organization inventory

Claim a list of devices, licenses, and/or orders into an organization inventory. When claiming by order, all devices and licenses in the order will be claimed; licenses will be added to the organization and devices will be placed in the organization&#39;s inventory. Use /organizations/{organizationId}/inventory/release to release devices from an organization.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InventoryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    InventoryApi apiInstance = new InventoryApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    ClaimIntoOrganizationInventoryRequest claimIntoOrganizationInventoryRequest = new ClaimIntoOrganizationInventoryRequest(); // ClaimIntoOrganizationInventoryRequest | 
    try {
      Object result = apiInstance.claimIntoOrganizationInventory_1(organizationId, claimIntoOrganizationInventoryRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InventoryApi#claimIntoOrganizationInventory_1");
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
| **organizationId** | **String**|  | |
| **claimIntoOrganizationInventoryRequest** | [**ClaimIntoOrganizationInventoryRequest**](ClaimIntoOrganizationInventoryRequest.md)|  | [optional] |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="createOrganizationInventoryOnboardingCloudMonitoringExportEvent_1"></a>
# **createOrganizationInventoryOnboardingCloudMonitoringExportEvent_1**
> Object createOrganizationInventoryOnboardingCloudMonitoringExportEvent_1(organizationId, createOrganizationInventoryOnboardingCloudMonitoringExportEventRequest)

Imports event logs related to the onboarding app into elastisearch

Imports event logs related to the onboarding app into elastisearch

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InventoryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    InventoryApi apiInstance = new InventoryApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    CreateOrganizationInventoryOnboardingCloudMonitoringExportEventRequest createOrganizationInventoryOnboardingCloudMonitoringExportEventRequest = new CreateOrganizationInventoryOnboardingCloudMonitoringExportEventRequest(); // CreateOrganizationInventoryOnboardingCloudMonitoringExportEventRequest | 
    try {
      Object result = apiInstance.createOrganizationInventoryOnboardingCloudMonitoringExportEvent_1(organizationId, createOrganizationInventoryOnboardingCloudMonitoringExportEventRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InventoryApi#createOrganizationInventoryOnboardingCloudMonitoringExportEvent_1");
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
| **organizationId** | **String**|  | |
| **createOrganizationInventoryOnboardingCloudMonitoringExportEventRequest** | [**CreateOrganizationInventoryOnboardingCloudMonitoringExportEventRequest**](CreateOrganizationInventoryOnboardingCloudMonitoringExportEventRequest.md)|  | |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Successful operation |  -  |

<a id="createOrganizationInventoryOnboardingCloudMonitoringImport_1"></a>
# **createOrganizationInventoryOnboardingCloudMonitoringImport_1**
> List&lt;CreateOrganizationInventoryOnboardingCloudMonitoringImport201ResponseInner&gt; createOrganizationInventoryOnboardingCloudMonitoringImport_1(organizationId, createOrganizationInventoryOnboardingCloudMonitoringImportRequest)

Commits the import operation to complete the onboarding of a device into Dashboard for monitoring.

Commits the import operation to complete the onboarding of a device into Dashboard for monitoring.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InventoryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    InventoryApi apiInstance = new InventoryApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    CreateOrganizationInventoryOnboardingCloudMonitoringImportRequest createOrganizationInventoryOnboardingCloudMonitoringImportRequest = new CreateOrganizationInventoryOnboardingCloudMonitoringImportRequest(); // CreateOrganizationInventoryOnboardingCloudMonitoringImportRequest | 
    try {
      List<CreateOrganizationInventoryOnboardingCloudMonitoringImport201ResponseInner> result = apiInstance.createOrganizationInventoryOnboardingCloudMonitoringImport_1(organizationId, createOrganizationInventoryOnboardingCloudMonitoringImportRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InventoryApi#createOrganizationInventoryOnboardingCloudMonitoringImport_1");
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
| **organizationId** | **String**|  | |
| **createOrganizationInventoryOnboardingCloudMonitoringImportRequest** | [**CreateOrganizationInventoryOnboardingCloudMonitoringImportRequest**](CreateOrganizationInventoryOnboardingCloudMonitoringImportRequest.md)|  | |

### Return type

[**List&lt;CreateOrganizationInventoryOnboardingCloudMonitoringImport201ResponseInner&gt;**](CreateOrganizationInventoryOnboardingCloudMonitoringImport201ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Successful operation |  -  |

<a id="createOrganizationInventoryOnboardingCloudMonitoringPrepare_1"></a>
# **createOrganizationInventoryOnboardingCloudMonitoringPrepare_1**
> List&lt;CreateOrganizationInventoryOnboardingCloudMonitoringPrepare201ResponseInner&gt; createOrganizationInventoryOnboardingCloudMonitoringPrepare_1(organizationId, createOrganizationInventoryOnboardingCloudMonitoringPrepareRequest)

Initiates or updates an import session

Initiates or updates an import session. An import ID will be generated and used when you are ready to commit the import.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InventoryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    InventoryApi apiInstance = new InventoryApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    CreateOrganizationInventoryOnboardingCloudMonitoringPrepareRequest createOrganizationInventoryOnboardingCloudMonitoringPrepareRequest = new CreateOrganizationInventoryOnboardingCloudMonitoringPrepareRequest(); // CreateOrganizationInventoryOnboardingCloudMonitoringPrepareRequest | 
    try {
      List<CreateOrganizationInventoryOnboardingCloudMonitoringPrepare201ResponseInner> result = apiInstance.createOrganizationInventoryOnboardingCloudMonitoringPrepare_1(organizationId, createOrganizationInventoryOnboardingCloudMonitoringPrepareRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InventoryApi#createOrganizationInventoryOnboardingCloudMonitoringPrepare_1");
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
| **organizationId** | **String**|  | |
| **createOrganizationInventoryOnboardingCloudMonitoringPrepareRequest** | [**CreateOrganizationInventoryOnboardingCloudMonitoringPrepareRequest**](CreateOrganizationInventoryOnboardingCloudMonitoringPrepareRequest.md)|  | |

### Return type

[**List&lt;CreateOrganizationInventoryOnboardingCloudMonitoringPrepare201ResponseInner&gt;**](CreateOrganizationInventoryOnboardingCloudMonitoringPrepare201ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Successful operation |  -  |

<a id="getOrganizationInventoryDevice_1"></a>
# **getOrganizationInventoryDevice_1**
> GetOrganizationInventoryDevices200ResponseInner getOrganizationInventoryDevice_1(organizationId, serial)

Return a single device from the inventory of an organization

Return a single device from the inventory of an organization

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InventoryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    InventoryApi apiInstance = new InventoryApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    String serial = "serial_example"; // String | 
    try {
      GetOrganizationInventoryDevices200ResponseInner result = apiInstance.getOrganizationInventoryDevice_1(organizationId, serial);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InventoryApi#getOrganizationInventoryDevice_1");
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
| **organizationId** | **String**|  | |
| **serial** | **String**|  | |

### Return type

[**GetOrganizationInventoryDevices200ResponseInner**](GetOrganizationInventoryDevices200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getOrganizationInventoryDevices_1"></a>
# **getOrganizationInventoryDevices_1**
> List&lt;GetOrganizationInventoryDevices200ResponseInner&gt; getOrganizationInventoryDevices_1(organizationId, perPage, startingAfter, endingBefore, usedState, search, macs, networkIds, serials, models, orderNumbers, tags, tagsFilterType, productTypes)

Return the device inventory for an organization

Return the device inventory for an organization

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InventoryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    InventoryApi apiInstance = new InventoryApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    Integer perPage = 56; // Integer | The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
    String startingAfter = "startingAfter_example"; // String | A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    String endingBefore = "endingBefore_example"; // String | A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    String usedState = "unused"; // String | Filter results by used or unused inventory. Accepted values are 'used' or 'unused'.
    String search = "search_example"; // String | Search for devices in inventory based on serial number, mac address, or model.
    List<String> macs = Arrays.asList(); // List<String> | Search for devices in inventory based on mac addresses.
    List<String> networkIds = Arrays.asList(); // List<String> | Search for devices in inventory based on network ids.
    List<String> serials = Arrays.asList(); // List<String> | Search for devices in inventory based on serials.
    List<String> models = Arrays.asList(); // List<String> | Search for devices in inventory based on model.
    List<String> orderNumbers = Arrays.asList(); // List<String> | Search for devices in inventory based on order numbers.
    List<String> tags = Arrays.asList(); // List<String> | Filter devices by tags. The filtering is case-sensitive. If tags are included, 'tagsFilterType' should also be included (see below).
    String tagsFilterType = "withAllTags"; // String | To use with 'tags' parameter, to filter devices which contain ANY or ALL given tags. Accepted values are 'withAnyTags' or 'withAllTags', default is 'withAnyTags'.
    List<String> productTypes = Arrays.asList(); // List<String> | Filter devices by product type. Accepted values are appliance, camera, cellularGateway, sensor, switch, systemsManager, and wireless.
    try {
      List<GetOrganizationInventoryDevices200ResponseInner> result = apiInstance.getOrganizationInventoryDevices_1(organizationId, perPage, startingAfter, endingBefore, usedState, search, macs, networkIds, serials, models, orderNumbers, tags, tagsFilterType, productTypes);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InventoryApi#getOrganizationInventoryDevices_1");
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
| **organizationId** | **String**|  | |
| **perPage** | **Integer**| The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000. | [optional] |
| **startingAfter** | **String**| A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] |
| **endingBefore** | **String**| A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] |
| **usedState** | **String**| Filter results by used or unused inventory. Accepted values are &#39;used&#39; or &#39;unused&#39;. | [optional] [enum: unused, used] |
| **search** | **String**| Search for devices in inventory based on serial number, mac address, or model. | [optional] |
| **macs** | [**List&lt;String&gt;**](String.md)| Search for devices in inventory based on mac addresses. | [optional] |
| **networkIds** | [**List&lt;String&gt;**](String.md)| Search for devices in inventory based on network ids. | [optional] |
| **serials** | [**List&lt;String&gt;**](String.md)| Search for devices in inventory based on serials. | [optional] |
| **models** | [**List&lt;String&gt;**](String.md)| Search for devices in inventory based on model. | [optional] |
| **orderNumbers** | [**List&lt;String&gt;**](String.md)| Search for devices in inventory based on order numbers. | [optional] |
| **tags** | [**List&lt;String&gt;**](String.md)| Filter devices by tags. The filtering is case-sensitive. If tags are included, &#39;tagsFilterType&#39; should also be included (see below). | [optional] |
| **tagsFilterType** | **String**| To use with &#39;tags&#39; parameter, to filter devices which contain ANY or ALL given tags. Accepted values are &#39;withAnyTags&#39; or &#39;withAllTags&#39;, default is &#39;withAnyTags&#39;. | [optional] [enum: withAllTags, withAnyTags] |
| **productTypes** | [**List&lt;String&gt;**](String.md)| Filter devices by product type. Accepted values are appliance, camera, cellularGateway, sensor, switch, systemsManager, and wireless. | [optional] [enum: appliance, camera, cellularGateway, sensor, switch, systemsManager, wireless] |

### Return type

[**List&lt;GetOrganizationInventoryDevices200ResponseInner&gt;**](GetOrganizationInventoryDevices200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  * Link - A comma-separated list of first, last, prev, and next relative links used for subsequent paginated requests. <br>  |

<a id="getOrganizationInventoryOnboardingCloudMonitoringImports_1"></a>
# **getOrganizationInventoryOnboardingCloudMonitoringImports_1**
> List&lt;GetOrganizationInventoryOnboardingCloudMonitoringImports200ResponseInner&gt; getOrganizationInventoryOnboardingCloudMonitoringImports_1(organizationId, importIds)

Check the status of a committed Import operation

Check the status of a committed Import operation

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InventoryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    InventoryApi apiInstance = new InventoryApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    List<String> importIds = Arrays.asList(); // List<String> | import ids from an imports
    try {
      List<GetOrganizationInventoryOnboardingCloudMonitoringImports200ResponseInner> result = apiInstance.getOrganizationInventoryOnboardingCloudMonitoringImports_1(organizationId, importIds);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InventoryApi#getOrganizationInventoryOnboardingCloudMonitoringImports_1");
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
| **organizationId** | **String**|  | |
| **importIds** | [**List&lt;String&gt;**](String.md)| import ids from an imports | |

### Return type

[**List&lt;GetOrganizationInventoryOnboardingCloudMonitoringImports200ResponseInner&gt;**](GetOrganizationInventoryOnboardingCloudMonitoringImports200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getOrganizationInventoryOnboardingCloudMonitoringNetworks_1"></a>
# **getOrganizationInventoryOnboardingCloudMonitoringNetworks_1**
> List&lt;GetNetwork200Response&gt; getOrganizationInventoryOnboardingCloudMonitoringNetworks_1(organizationId, deviceType, perPage, startingAfter, endingBefore)

Returns list of networks eligible for adding cloud monitored device

Returns list of networks eligible for adding cloud monitored device

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InventoryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    InventoryApi apiInstance = new InventoryApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    String deviceType = "switch"; // String | Device Type switch or wireless controller
    Integer perPage = 56; // Integer | The number of entries per page returned. Acceptable range is 3 - 100000. Default is 1000.
    String startingAfter = "startingAfter_example"; // String | A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    String endingBefore = "endingBefore_example"; // String | A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    try {
      List<GetNetwork200Response> result = apiInstance.getOrganizationInventoryOnboardingCloudMonitoringNetworks_1(organizationId, deviceType, perPage, startingAfter, endingBefore);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InventoryApi#getOrganizationInventoryOnboardingCloudMonitoringNetworks_1");
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
| **organizationId** | **String**|  | |
| **deviceType** | **String**| Device Type switch or wireless controller | [enum: switch, wireless_controller] |
| **perPage** | **Integer**| The number of entries per page returned. Acceptable range is 3 - 100000. Default is 1000. | [optional] |
| **startingAfter** | **String**| A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] |
| **endingBefore** | **String**| A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] |

### Return type

[**List&lt;GetNetwork200Response&gt;**](GetNetwork200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Successful operation |  * Link - A comma-separated list of first, last, prev, and next relative links used for subsequent paginated requests. <br>  |

<a id="releaseFromOrganizationInventory_1"></a>
# **releaseFromOrganizationInventory_1**
> Object releaseFromOrganizationInventory_1(organizationId, releaseFromOrganizationInventoryRequest)

Release a list of claimed devices from an organization.

Release a list of claimed devices from an organization.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InventoryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    InventoryApi apiInstance = new InventoryApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    ReleaseFromOrganizationInventoryRequest releaseFromOrganizationInventoryRequest = new ReleaseFromOrganizationInventoryRequest(); // ReleaseFromOrganizationInventoryRequest | 
    try {
      Object result = apiInstance.releaseFromOrganizationInventory_1(organizationId, releaseFromOrganizationInventoryRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InventoryApi#releaseFromOrganizationInventory_1");
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
| **organizationId** | **String**|  | |
| **releaseFromOrganizationInventoryRequest** | [**ReleaseFromOrganizationInventoryRequest**](ReleaseFromOrganizationInventoryRequest.md)|  | [optional] |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

