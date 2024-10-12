# DefaultApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**checkNameAvailability**](DefaultApi.md#checkNameAvailability) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.Web/checknameavailability | Check if a resource name is available. |
| [**getPublishingUser**](DefaultApi.md#getPublishingUser) | **GET** /providers/Microsoft.Web/publishingUsers/web | Gets publishing user |
| [**getSourceControl**](DefaultApi.md#getSourceControl) | **GET** /providers/Microsoft.Web/sourcecontrols/{sourceControlType} | Gets source control token |
| [**getSubscriptionDeploymentLocations**](DefaultApi.md#getSubscriptionDeploymentLocations) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Web/deploymentLocations | Gets list of available geo regions plus ministamps |
| [**listBillingMeters**](DefaultApi.md#listBillingMeters) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Web/billingMeters | Gets a list of meters for a given location. |
| [**listGeoRegions**](DefaultApi.md#listGeoRegions) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Web/geoRegions | Get a list of available geographical regions. |
| [**listPremierAddOnOffers**](DefaultApi.md#listPremierAddOnOffers) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Web/premieraddonoffers | List all premier add-on offers. |
| [**listSiteIdentifiersAssignedToHostName**](DefaultApi.md#listSiteIdentifiersAssignedToHostName) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.Web/listSitesAssignedToHostName | List all apps that are assigned to a hostname. |
| [**listSkus**](DefaultApi.md#listSkus) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Web/skus | List all SKUs. |
| [**listSourceControls**](DefaultApi.md#listSourceControls) | **GET** /providers/Microsoft.Web/sourcecontrols | Gets the source controls available for Azure websites. |
| [**move**](DefaultApi.md#move) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/moveResources | Move resources between resource groups. |
| [**updatePublishingUser**](DefaultApi.md#updatePublishingUser) | **PUT** /providers/Microsoft.Web/publishingUsers/web | Updates publishing user |
| [**updateSourceControl**](DefaultApi.md#updateSourceControl) | **PUT** /providers/Microsoft.Web/sourcecontrols/{sourceControlType} | Updates source control token |
| [**validate**](DefaultApi.md#validate) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/validate | Validate if a resource can be created. |
| [**validateContainerSettings**](DefaultApi.md#validateContainerSettings) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/validateContainerSettings | Validate if the container settings are correct. |
| [**validateMove**](DefaultApi.md#validateMove) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/validateMoveResources | Validate whether a resource can be moved. |
| [**verifyHostingEnvironmentVnet**](DefaultApi.md#verifyHostingEnvironmentVnet) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.Web/verifyHostingEnvironmentVnet | Verifies if this VNET is compatible with an App Service Environment by analyzing the Network Security Group rules. |


<a id="checkNameAvailability"></a>
# **checkNameAvailability**
> ResourceNameAvailability checkNameAvailability(subscriptionId, apiVersion, request)

Check if a resource name is available.

Check if a resource name is available.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    String apiVersion = "apiVersion_example"; // String | API Version
    ResourceNameAvailabilityRequest request = new ResourceNameAvailabilityRequest(); // ResourceNameAvailabilityRequest | Name availability request.
    try {
      ResourceNameAvailability result = apiInstance.checkNameAvailability(subscriptionId, apiVersion, request);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#checkNameAvailability");
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
| **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | |
| **apiVersion** | **String**| API Version | |
| **request** | [**ResourceNameAvailabilityRequest**](ResourceNameAvailabilityRequest.md)| Name availability request. | |

### Return type

[**ResourceNameAvailability**](ResourceNameAvailability.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | App Service error response. |  -  |

<a id="getPublishingUser"></a>
# **getPublishingUser**
> GetPublishingUser200Response getPublishingUser(apiVersion)

Gets publishing user

Gets publishing user

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      GetPublishingUser200Response result = apiInstance.getPublishingUser(apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getPublishingUser");
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
| **apiVersion** | **String**| API Version | |

### Return type

[**GetPublishingUser200Response**](GetPublishingUser200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | App Service error response. |  -  |

<a id="getSourceControl"></a>
# **getSourceControl**
> SourceControl getSourceControl(sourceControlType, apiVersion)

Gets source control token

Gets source control token

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String sourceControlType = "sourceControlType_example"; // String | Type of source control
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      SourceControl result = apiInstance.getSourceControl(sourceControlType, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getSourceControl");
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
| **sourceControlType** | **String**| Type of source control | |
| **apiVersion** | **String**| API Version | |

### Return type

[**SourceControl**](SourceControl.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | App Service error response. |  -  |

<a id="getSubscriptionDeploymentLocations"></a>
# **getSubscriptionDeploymentLocations**
> DeploymentLocations getSubscriptionDeploymentLocations(subscriptionId, apiVersion)

Gets list of available geo regions plus ministamps

Gets list of available geo regions plus ministamps

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      DeploymentLocations result = apiInstance.getSubscriptionDeploymentLocations(subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getSubscriptionDeploymentLocations");
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
| **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | |
| **apiVersion** | **String**| API Version | |

### Return type

[**DeploymentLocations**](DeploymentLocations.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | App Service error response. |  -  |

<a id="listBillingMeters"></a>
# **listBillingMeters**
> BillingMeterCollection listBillingMeters(subscriptionId, apiVersion, billingLocation, osType)

Gets a list of meters for a given location.

Gets a list of meters for a given location.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    String apiVersion = "apiVersion_example"; // String | API Version
    String billingLocation = "billingLocation_example"; // String | Azure Location of billable resource
    String osType = "osType_example"; // String | App Service OS type meters used for
    try {
      BillingMeterCollection result = apiInstance.listBillingMeters(subscriptionId, apiVersion, billingLocation, osType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listBillingMeters");
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
| **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | |
| **apiVersion** | **String**| API Version | |
| **billingLocation** | **String**| Azure Location of billable resource | [optional] |
| **osType** | **String**| App Service OS type meters used for | [optional] |

### Return type

[**BillingMeterCollection**](BillingMeterCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | App Service error response. |  -  |

<a id="listGeoRegions"></a>
# **listGeoRegions**
> GeoRegionCollection listGeoRegions(subscriptionId, apiVersion, sku, linuxWorkersEnabled, xenonWorkersEnabled, linuxDynamicWorkersEnabled)

Get a list of available geographical regions.

Get a list of available geographical regions.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    String apiVersion = "apiVersion_example"; // String | API Version
    String sku = "Free"; // String | Name of SKU used to filter the regions.
    Boolean linuxWorkersEnabled = true; // Boolean | Specify <code>true</code> if you want to filter to only regions that support Linux workers.
    Boolean xenonWorkersEnabled = true; // Boolean | Specify <code>true</code> if you want to filter to only regions that support Xenon workers.
    Boolean linuxDynamicWorkersEnabled = true; // Boolean | Specify <code>true</code> if you want to filter to only regions that support Linux Consumption Workers.
    try {
      GeoRegionCollection result = apiInstance.listGeoRegions(subscriptionId, apiVersion, sku, linuxWorkersEnabled, xenonWorkersEnabled, linuxDynamicWorkersEnabled);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listGeoRegions");
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
| **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | |
| **apiVersion** | **String**| API Version | |
| **sku** | **String**| Name of SKU used to filter the regions. | [optional] [enum: Free, Shared, Basic, Standard, Premium, Dynamic, Isolated, PremiumV2, ElasticPremium, ElasticIsolated] |
| **linuxWorkersEnabled** | **Boolean**| Specify &lt;code&gt;true&lt;/code&gt; if you want to filter to only regions that support Linux workers. | [optional] |
| **xenonWorkersEnabled** | **Boolean**| Specify &lt;code&gt;true&lt;/code&gt; if you want to filter to only regions that support Xenon workers. | [optional] |
| **linuxDynamicWorkersEnabled** | **Boolean**| Specify &lt;code&gt;true&lt;/code&gt; if you want to filter to only regions that support Linux Consumption Workers. | [optional] |

### Return type

[**GeoRegionCollection**](GeoRegionCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | App Service error response. |  -  |

<a id="listPremierAddOnOffers"></a>
# **listPremierAddOnOffers**
> PremierAddOnOfferCollection listPremierAddOnOffers(subscriptionId, apiVersion)

List all premier add-on offers.

List all premier add-on offers.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      PremierAddOnOfferCollection result = apiInstance.listPremierAddOnOffers(subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listPremierAddOnOffers");
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
| **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | |
| **apiVersion** | **String**| API Version | |

### Return type

[**PremierAddOnOfferCollection**](PremierAddOnOfferCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | App Service error response. |  -  |

<a id="listSiteIdentifiersAssignedToHostName"></a>
# **listSiteIdentifiersAssignedToHostName**
> ListSiteIdentifiersAssignedToHostName200Response listSiteIdentifiersAssignedToHostName(subscriptionId, apiVersion, nameIdentifier)

List all apps that are assigned to a hostname.

List all apps that are assigned to a hostname.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    String apiVersion = "apiVersion_example"; // String | API Version
    ListSiteIdentifiersAssignedToHostNameRequest nameIdentifier = new ListSiteIdentifiersAssignedToHostNameRequest(); // ListSiteIdentifiersAssignedToHostNameRequest | Hostname information.
    try {
      ListSiteIdentifiersAssignedToHostName200Response result = apiInstance.listSiteIdentifiersAssignedToHostName(subscriptionId, apiVersion, nameIdentifier);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listSiteIdentifiersAssignedToHostName");
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
| **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | |
| **apiVersion** | **String**| API Version | |
| **nameIdentifier** | [**ListSiteIdentifiersAssignedToHostNameRequest**](ListSiteIdentifiersAssignedToHostNameRequest.md)| Hostname information. | |

### Return type

[**ListSiteIdentifiersAssignedToHostName200Response**](ListSiteIdentifiersAssignedToHostName200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | App Service error response. |  -  |

<a id="listSkus"></a>
# **listSkus**
> SkuInfos listSkus(subscriptionId, apiVersion)

List all SKUs.

List all SKUs.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      SkuInfos result = apiInstance.listSkus(subscriptionId, apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listSkus");
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
| **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | |
| **apiVersion** | **String**| API Version | |

### Return type

[**SkuInfos**](SkuInfos.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | App Service error response. |  -  |

<a id="listSourceControls"></a>
# **listSourceControls**
> SourceControlCollection listSourceControls(apiVersion)

Gets the source controls available for Azure websites.

Gets the source controls available for Azure websites.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | API Version
    try {
      SourceControlCollection result = apiInstance.listSourceControls(apiVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listSourceControls");
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
| **apiVersion** | **String**| API Version | |

### Return type

[**SourceControlCollection**](SourceControlCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | App Service error response. |  -  |

<a id="move"></a>
# **move**
> move(resourceGroupName, subscriptionId, apiVersion, moveResourceEnvelope)

Move resources between resource groups.

Move resources between resource groups.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
    String subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    String apiVersion = "apiVersion_example"; // String | API Version
    CsmMoveResourceEnvelope moveResourceEnvelope = new CsmMoveResourceEnvelope(); // CsmMoveResourceEnvelope | Object that represents the resource to move.
    try {
      apiInstance.move(resourceGroupName, subscriptionId, apiVersion, moveResourceEnvelope);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#move");
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
| **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | |
| **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | |
| **apiVersion** | **String**| API Version | |
| **moveResourceEnvelope** | [**CsmMoveResourceEnvelope**](CsmMoveResourceEnvelope.md)| Object that represents the resource to move. | |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |

<a id="updatePublishingUser"></a>
# **updatePublishingUser**
> GetPublishingUser200Response updatePublishingUser(apiVersion, userDetails)

Updates publishing user

Updates publishing user

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | API Version
    GetPublishingUser200Response userDetails = new GetPublishingUser200Response(); // GetPublishingUser200Response | Details of publishing user
    try {
      GetPublishingUser200Response result = apiInstance.updatePublishingUser(apiVersion, userDetails);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#updatePublishingUser");
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
| **apiVersion** | **String**| API Version | |
| **userDetails** | [**GetPublishingUser200Response**](GetPublishingUser200Response.md)| Details of publishing user | |

### Return type

[**GetPublishingUser200Response**](GetPublishingUser200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | App Service error response. |  -  |

<a id="updateSourceControl"></a>
# **updateSourceControl**
> SourceControl updateSourceControl(sourceControlType, apiVersion, requestMessage)

Updates source control token

Updates source control token

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String sourceControlType = "sourceControlType_example"; // String | Type of source control
    String apiVersion = "apiVersion_example"; // String | API Version
    SourceControl requestMessage = new SourceControl(); // SourceControl | Source control token information
    try {
      SourceControl result = apiInstance.updateSourceControl(sourceControlType, apiVersion, requestMessage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#updateSourceControl");
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
| **sourceControlType** | **String**| Type of source control | |
| **apiVersion** | **String**| API Version | |
| **requestMessage** | [**SourceControl**](SourceControl.md)| Source control token information | |

### Return type

[**SourceControl**](SourceControl.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | App Service error response. |  -  |

<a id="validate"></a>
# **validate**
> ValidateResponse validate(resourceGroupName, subscriptionId, apiVersion, validateRequest)

Validate if a resource can be created.

Validate if a resource can be created.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
    String subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    String apiVersion = "apiVersion_example"; // String | API Version
    ValidateRequest validateRequest = new ValidateRequest(); // ValidateRequest | Request with the resources to validate.
    try {
      ValidateResponse result = apiInstance.validate(resourceGroupName, subscriptionId, apiVersion, validateRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#validate");
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
| **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | |
| **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | |
| **apiVersion** | **String**| API Version | |
| **validateRequest** | [**ValidateRequest**](ValidateRequest.md)| Request with the resources to validate. | |

### Return type

[**ValidateResponse**](ValidateResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | App Service error response. |  -  |

<a id="validateContainerSettings"></a>
# **validateContainerSettings**
> Object validateContainerSettings(resourceGroupName, subscriptionId, apiVersion, validateContainerSettingsRequest)

Validate if the container settings are correct.

Validate if the container settings are correct.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
    String subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    String apiVersion = "apiVersion_example"; // String | API Version
    ValidateContainerSettingsRequest validateContainerSettingsRequest = new ValidateContainerSettingsRequest(); // ValidateContainerSettingsRequest | 
    try {
      Object result = apiInstance.validateContainerSettings(resourceGroupName, subscriptionId, apiVersion, validateContainerSettingsRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#validateContainerSettings");
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
| **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | |
| **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | |
| **apiVersion** | **String**| API Version | |
| **validateContainerSettingsRequest** | [**ValidateContainerSettingsRequest**](ValidateContainerSettingsRequest.md)|  | |

### Return type

**Object**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | App Service error response. |  -  |

<a id="validateMove"></a>
# **validateMove**
> validateMove(resourceGroupName, subscriptionId, apiVersion, moveResourceEnvelope)

Validate whether a resource can be moved.

Validate whether a resource can be moved.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
    String subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    String apiVersion = "apiVersion_example"; // String | API Version
    CsmMoveResourceEnvelope moveResourceEnvelope = new CsmMoveResourceEnvelope(); // CsmMoveResourceEnvelope | Object that represents the resource to move.
    try {
      apiInstance.validateMove(resourceGroupName, subscriptionId, apiVersion, moveResourceEnvelope);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#validateMove");
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
| **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | |
| **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | |
| **apiVersion** | **String**| API Version | |
| **moveResourceEnvelope** | [**CsmMoveResourceEnvelope**](CsmMoveResourceEnvelope.md)| Object that represents the resource to move. | |

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |

<a id="verifyHostingEnvironmentVnet"></a>
# **verifyHostingEnvironmentVnet**
> VnetValidationFailureDetails verifyHostingEnvironmentVnet(subscriptionId, apiVersion, parameters)

Verifies if this VNET is compatible with an App Service Environment by analyzing the Network Security Group rules.

Verifies if this VNET is compatible with an App Service Environment by analyzing the Network Security Group rules.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");
    
    // Configure OAuth2 access token for authorization: azure_auth
    OAuth azure_auth = (OAuth) defaultClient.getAuthentication("azure_auth");
    azure_auth.setAccessToken("YOUR ACCESS TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    String apiVersion = "apiVersion_example"; // String | API Version
    VnetParameters parameters = new VnetParameters(); // VnetParameters | VNET information
    try {
      VnetValidationFailureDetails result = apiInstance.verifyHostingEnvironmentVnet(subscriptionId, apiVersion, parameters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#verifyHostingEnvironmentVnet");
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
| **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | |
| **apiVersion** | **String**| API Version | |
| **parameters** | [**VnetParameters**](VnetParameters.md)| VNET information | |

### Return type

[**VnetValidationFailureDetails**](VnetValidationFailureDetails.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | App Service error response. |  -  |

