# CloudMonitoringApi

All URIs are relative to *https://api.meraki.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createOrganizationInventoryOnboardingCloudMonitoringExportEvent_3**](CloudMonitoringApi.md#createOrganizationInventoryOnboardingCloudMonitoringExportEvent_3) | **POST** /organizations/{organizationId}/inventory/onboarding/cloudMonitoring/exportEvents | Imports event logs related to the onboarding app into elastisearch |
| [**createOrganizationInventoryOnboardingCloudMonitoringImport_3**](CloudMonitoringApi.md#createOrganizationInventoryOnboardingCloudMonitoringImport_3) | **POST** /organizations/{organizationId}/inventory/onboarding/cloudMonitoring/imports | Commits the import operation to complete the onboarding of a device into Dashboard for monitoring. |
| [**createOrganizationInventoryOnboardingCloudMonitoringPrepare_3**](CloudMonitoringApi.md#createOrganizationInventoryOnboardingCloudMonitoringPrepare_3) | **POST** /organizations/{organizationId}/inventory/onboarding/cloudMonitoring/prepare | Initiates or updates an import session |
| [**getOrganizationInventoryOnboardingCloudMonitoringImports_3**](CloudMonitoringApi.md#getOrganizationInventoryOnboardingCloudMonitoringImports_3) | **GET** /organizations/{organizationId}/inventory/onboarding/cloudMonitoring/imports | Check the status of a committed Import operation |
| [**getOrganizationInventoryOnboardingCloudMonitoringNetworks_3**](CloudMonitoringApi.md#getOrganizationInventoryOnboardingCloudMonitoringNetworks_3) | **GET** /organizations/{organizationId}/inventory/onboarding/cloudMonitoring/networks | Returns list of networks eligible for adding cloud monitored device |


<a id="createOrganizationInventoryOnboardingCloudMonitoringExportEvent_3"></a>
# **createOrganizationInventoryOnboardingCloudMonitoringExportEvent_3**
> Object createOrganizationInventoryOnboardingCloudMonitoringExportEvent_3(organizationId, createOrganizationInventoryOnboardingCloudMonitoringExportEventRequest)

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
import org.openapitools.client.api.CloudMonitoringApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    CloudMonitoringApi apiInstance = new CloudMonitoringApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    CreateOrganizationInventoryOnboardingCloudMonitoringExportEventRequest createOrganizationInventoryOnboardingCloudMonitoringExportEventRequest = new CreateOrganizationInventoryOnboardingCloudMonitoringExportEventRequest(); // CreateOrganizationInventoryOnboardingCloudMonitoringExportEventRequest | 
    try {
      Object result = apiInstance.createOrganizationInventoryOnboardingCloudMonitoringExportEvent_3(organizationId, createOrganizationInventoryOnboardingCloudMonitoringExportEventRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CloudMonitoringApi#createOrganizationInventoryOnboardingCloudMonitoringExportEvent_3");
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

<a id="createOrganizationInventoryOnboardingCloudMonitoringImport_3"></a>
# **createOrganizationInventoryOnboardingCloudMonitoringImport_3**
> List&lt;CreateOrganizationInventoryOnboardingCloudMonitoringImport201ResponseInner&gt; createOrganizationInventoryOnboardingCloudMonitoringImport_3(organizationId, createOrganizationInventoryOnboardingCloudMonitoringImportRequest)

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
import org.openapitools.client.api.CloudMonitoringApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    CloudMonitoringApi apiInstance = new CloudMonitoringApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    CreateOrganizationInventoryOnboardingCloudMonitoringImportRequest createOrganizationInventoryOnboardingCloudMonitoringImportRequest = new CreateOrganizationInventoryOnboardingCloudMonitoringImportRequest(); // CreateOrganizationInventoryOnboardingCloudMonitoringImportRequest | 
    try {
      List<CreateOrganizationInventoryOnboardingCloudMonitoringImport201ResponseInner> result = apiInstance.createOrganizationInventoryOnboardingCloudMonitoringImport_3(organizationId, createOrganizationInventoryOnboardingCloudMonitoringImportRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CloudMonitoringApi#createOrganizationInventoryOnboardingCloudMonitoringImport_3");
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

<a id="createOrganizationInventoryOnboardingCloudMonitoringPrepare_3"></a>
# **createOrganizationInventoryOnboardingCloudMonitoringPrepare_3**
> List&lt;CreateOrganizationInventoryOnboardingCloudMonitoringPrepare201ResponseInner&gt; createOrganizationInventoryOnboardingCloudMonitoringPrepare_3(organizationId, createOrganizationInventoryOnboardingCloudMonitoringPrepareRequest)

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
import org.openapitools.client.api.CloudMonitoringApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    CloudMonitoringApi apiInstance = new CloudMonitoringApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    CreateOrganizationInventoryOnboardingCloudMonitoringPrepareRequest createOrganizationInventoryOnboardingCloudMonitoringPrepareRequest = new CreateOrganizationInventoryOnboardingCloudMonitoringPrepareRequest(); // CreateOrganizationInventoryOnboardingCloudMonitoringPrepareRequest | 
    try {
      List<CreateOrganizationInventoryOnboardingCloudMonitoringPrepare201ResponseInner> result = apiInstance.createOrganizationInventoryOnboardingCloudMonitoringPrepare_3(organizationId, createOrganizationInventoryOnboardingCloudMonitoringPrepareRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CloudMonitoringApi#createOrganizationInventoryOnboardingCloudMonitoringPrepare_3");
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

<a id="getOrganizationInventoryOnboardingCloudMonitoringImports_3"></a>
# **getOrganizationInventoryOnboardingCloudMonitoringImports_3**
> List&lt;GetOrganizationInventoryOnboardingCloudMonitoringImports200ResponseInner&gt; getOrganizationInventoryOnboardingCloudMonitoringImports_3(organizationId, importIds)

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
import org.openapitools.client.api.CloudMonitoringApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    CloudMonitoringApi apiInstance = new CloudMonitoringApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    List<String> importIds = Arrays.asList(); // List<String> | import ids from an imports
    try {
      List<GetOrganizationInventoryOnboardingCloudMonitoringImports200ResponseInner> result = apiInstance.getOrganizationInventoryOnboardingCloudMonitoringImports_3(organizationId, importIds);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CloudMonitoringApi#getOrganizationInventoryOnboardingCloudMonitoringImports_3");
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

<a id="getOrganizationInventoryOnboardingCloudMonitoringNetworks_3"></a>
# **getOrganizationInventoryOnboardingCloudMonitoringNetworks_3**
> List&lt;GetNetwork200Response&gt; getOrganizationInventoryOnboardingCloudMonitoringNetworks_3(organizationId, deviceType, perPage, startingAfter, endingBefore)

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
import org.openapitools.client.api.CloudMonitoringApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    CloudMonitoringApi apiInstance = new CloudMonitoringApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    String deviceType = "switch"; // String | Device Type switch or wireless controller
    Integer perPage = 56; // Integer | The number of entries per page returned. Acceptable range is 3 - 100000. Default is 1000.
    String startingAfter = "startingAfter_example"; // String | A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    String endingBefore = "endingBefore_example"; // String | A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    try {
      List<GetNetwork200Response> result = apiInstance.getOrganizationInventoryOnboardingCloudMonitoringNetworks_3(organizationId, deviceType, perPage, startingAfter, endingBefore);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CloudMonitoringApi#getOrganizationInventoryOnboardingCloudMonitoringNetworks_3");
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

