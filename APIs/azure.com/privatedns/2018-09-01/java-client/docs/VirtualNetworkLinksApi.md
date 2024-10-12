# VirtualNetworkLinksApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**virtualNetworkLinksCreateOrUpdate**](VirtualNetworkLinksApi.md#virtualNetworkLinksCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/privateDnsZones/{privateZoneName}/virtualNetworkLinks/{virtualNetworkLinkName} |  |
| [**virtualNetworkLinksDelete**](VirtualNetworkLinksApi.md#virtualNetworkLinksDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/privateDnsZones/{privateZoneName}/virtualNetworkLinks/{virtualNetworkLinkName} |  |
| [**virtualNetworkLinksGet**](VirtualNetworkLinksApi.md#virtualNetworkLinksGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/privateDnsZones/{privateZoneName}/virtualNetworkLinks/{virtualNetworkLinkName} |  |
| [**virtualNetworkLinksList**](VirtualNetworkLinksApi.md#virtualNetworkLinksList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/privateDnsZones/{privateZoneName}/virtualNetworkLinks |  |
| [**virtualNetworkLinksUpdate**](VirtualNetworkLinksApi.md#virtualNetworkLinksUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/privateDnsZones/{privateZoneName}/virtualNetworkLinks/{virtualNetworkLinkName} |  |


<a id="virtualNetworkLinksCreateOrUpdate"></a>
# **virtualNetworkLinksCreateOrUpdate**
> VirtualNetworkLink virtualNetworkLinksCreateOrUpdate(resourceGroupName, privateZoneName, virtualNetworkLinkName, apiVersion, subscriptionId, parameters, ifMatch, ifNoneMatch)



Creates or updates a virtual network link to the specified Private DNS zone.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualNetworkLinksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    VirtualNetworkLinksApi apiInstance = new VirtualNetworkLinksApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String privateZoneName = "privateZoneName_example"; // String | The name of the Private DNS zone (without a terminating dot).
    String virtualNetworkLinkName = "virtualNetworkLinkName_example"; // String | The name of the virtual network link.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    VirtualNetworkLink parameters = new VirtualNetworkLink(); // VirtualNetworkLink | Parameters supplied to the CreateOrUpdate operation.
    String ifMatch = "ifMatch_example"; // String | The ETag of the virtual network link to the Private DNS zone. Omit this value to always overwrite the current virtual network link. Specify the last-seen ETag value to prevent accidentally overwriting any concurrent changes.
    String ifNoneMatch = "ifNoneMatch_example"; // String | Set to '*' to allow a new virtual network link to the Private DNS zone to be created, but to prevent updating an existing link. Other values will be ignored.
    try {
      VirtualNetworkLink result = apiInstance.virtualNetworkLinksCreateOrUpdate(resourceGroupName, privateZoneName, virtualNetworkLinkName, apiVersion, subscriptionId, parameters, ifMatch, ifNoneMatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualNetworkLinksApi#virtualNetworkLinksCreateOrUpdate");
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
| **resourceGroupName** | **String**| The name of the resource group. | |
| **privateZoneName** | **String**| The name of the Private DNS zone (without a terminating dot). | |
| **virtualNetworkLinkName** | **String**| The name of the virtual network link. | |
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **parameters** | [**VirtualNetworkLink**](VirtualNetworkLink.md)| Parameters supplied to the CreateOrUpdate operation. | |
| **ifMatch** | **String**| The ETag of the virtual network link to the Private DNS zone. Omit this value to always overwrite the current virtual network link. Specify the last-seen ETag value to prevent accidentally overwriting any concurrent changes. | [optional] |
| **ifNoneMatch** | **String**| Set to &#39;*&#39; to allow a new virtual network link to the Private DNS zone to be created, but to prevent updating an existing link. Other values will be ignored. | [optional] |

### Return type

[**VirtualNetworkLink**](VirtualNetworkLink.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The virtual network link to the Private DNS zone has been updated. |  -  |
| **201** | The virtual network link to the Private DNS zone has been created. |  -  |
| **202** | The operation to upsert virtual network link to the Private DNS zone has been accepted and will complete asynchronously. |  -  |
| **0** | Default response. It will be deserialized as per the Error definition. |  -  |

<a id="virtualNetworkLinksDelete"></a>
# **virtualNetworkLinksDelete**
> virtualNetworkLinksDelete(resourceGroupName, privateZoneName, virtualNetworkLinkName, apiVersion, subscriptionId, ifMatch)



Deletes a virtual network link to the specified Private DNS zone. WARNING: In case of a registration virtual network, all auto-registered DNS records in the zone for the virtual network will also be deleted. This operation cannot be undone.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualNetworkLinksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    VirtualNetworkLinksApi apiInstance = new VirtualNetworkLinksApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String privateZoneName = "privateZoneName_example"; // String | The name of the Private DNS zone (without a terminating dot).
    String virtualNetworkLinkName = "virtualNetworkLinkName_example"; // String | The name of the virtual network link.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String ifMatch = "ifMatch_example"; // String | The ETag of the virtual network link to the Private DNS zone. Omit this value to always delete the current zone. Specify the last-seen ETag value to prevent accidentally deleting any concurrent changes.
    try {
      apiInstance.virtualNetworkLinksDelete(resourceGroupName, privateZoneName, virtualNetworkLinkName, apiVersion, subscriptionId, ifMatch);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualNetworkLinksApi#virtualNetworkLinksDelete");
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
| **resourceGroupName** | **String**| The name of the resource group. | |
| **privateZoneName** | **String**| The name of the Private DNS zone (without a terminating dot). | |
| **virtualNetworkLinkName** | **String**| The name of the virtual network link. | |
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **ifMatch** | **String**| The ETag of the virtual network link to the Private DNS zone. Omit this value to always delete the current zone. Specify the last-seen ETag value to prevent accidentally deleting any concurrent changes. | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The virtual network link to the Private DNS zone has been deleted. |  -  |
| **202** | The operation to delete virtual network link to the Private DNS zone has been accepted and will complete asynchronously. |  -  |
| **204** | The virtual network link to the Private DNS zone was not found. |  -  |
| **0** | Default response. It will be deserialized as per the Error definition. |  -  |

<a id="virtualNetworkLinksGet"></a>
# **virtualNetworkLinksGet**
> VirtualNetworkLink virtualNetworkLinksGet(resourceGroupName, privateZoneName, virtualNetworkLinkName, apiVersion, subscriptionId)



Gets a virtual network link to the specified Private DNS zone.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualNetworkLinksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    VirtualNetworkLinksApi apiInstance = new VirtualNetworkLinksApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String privateZoneName = "privateZoneName_example"; // String | The name of the Private DNS zone (without a terminating dot).
    String virtualNetworkLinkName = "virtualNetworkLinkName_example"; // String | The name of the virtual network link.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      VirtualNetworkLink result = apiInstance.virtualNetworkLinksGet(resourceGroupName, privateZoneName, virtualNetworkLinkName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualNetworkLinksApi#virtualNetworkLinksGet");
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
| **resourceGroupName** | **String**| The name of the resource group. | |
| **privateZoneName** | **String**| The name of the Private DNS zone (without a terminating dot). | |
| **virtualNetworkLinkName** | **String**| The name of the virtual network link. | |
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |

### Return type

[**VirtualNetworkLink**](VirtualNetworkLink.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success. |  -  |
| **0** | Default response. It will be deserialized as per the Error definition. |  -  |

<a id="virtualNetworkLinksList"></a>
# **virtualNetworkLinksList**
> VirtualNetworkLinkListResult virtualNetworkLinksList(resourceGroupName, privateZoneName, apiVersion, subscriptionId, $top)



Lists the virtual network links to the specified Private DNS zone.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualNetworkLinksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    VirtualNetworkLinksApi apiInstance = new VirtualNetworkLinksApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String privateZoneName = "privateZoneName_example"; // String | The name of the Private DNS zone (without a terminating dot).
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    Integer $top = 56; // Integer | The maximum number of virtual network links to return. If not specified, returns up to 100 virtual network links.
    try {
      VirtualNetworkLinkListResult result = apiInstance.virtualNetworkLinksList(resourceGroupName, privateZoneName, apiVersion, subscriptionId, $top);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualNetworkLinksApi#virtualNetworkLinksList");
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
| **resourceGroupName** | **String**| The name of the resource group. | |
| **privateZoneName** | **String**| The name of the Private DNS zone (without a terminating dot). | |
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **$top** | **Integer**| The maximum number of virtual network links to return. If not specified, returns up to 100 virtual network links. | [optional] |

### Return type

[**VirtualNetworkLinkListResult**](VirtualNetworkLinkListResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success. |  -  |
| **0** | Default response. It will be deserialized as per the Error definition. |  -  |

<a id="virtualNetworkLinksUpdate"></a>
# **virtualNetworkLinksUpdate**
> VirtualNetworkLink virtualNetworkLinksUpdate(resourceGroupName, privateZoneName, virtualNetworkLinkName, apiVersion, subscriptionId, parameters, ifMatch)



Updates a virtual network link to the specified Private DNS zone.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VirtualNetworkLinksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    VirtualNetworkLinksApi apiInstance = new VirtualNetworkLinksApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String privateZoneName = "privateZoneName_example"; // String | The name of the Private DNS zone (without a terminating dot).
    String virtualNetworkLinkName = "virtualNetworkLinkName_example"; // String | The name of the virtual network link.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    VirtualNetworkLink parameters = new VirtualNetworkLink(); // VirtualNetworkLink | Parameters supplied to the Update operation.
    String ifMatch = "ifMatch_example"; // String | The ETag of the virtual network link to the Private DNS zone. Omit this value to always overwrite the current virtual network link. Specify the last-seen ETag value to prevent accidentally overwriting any concurrent changes.
    try {
      VirtualNetworkLink result = apiInstance.virtualNetworkLinksUpdate(resourceGroupName, privateZoneName, virtualNetworkLinkName, apiVersion, subscriptionId, parameters, ifMatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VirtualNetworkLinksApi#virtualNetworkLinksUpdate");
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
| **resourceGroupName** | **String**| The name of the resource group. | |
| **privateZoneName** | **String**| The name of the Private DNS zone (without a terminating dot). | |
| **virtualNetworkLinkName** | **String**| The name of the virtual network link. | |
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **parameters** | [**VirtualNetworkLink**](VirtualNetworkLink.md)| Parameters supplied to the Update operation. | |
| **ifMatch** | **String**| The ETag of the virtual network link to the Private DNS zone. Omit this value to always overwrite the current virtual network link. Specify the last-seen ETag value to prevent accidentally overwriting any concurrent changes. | [optional] |

### Return type

[**VirtualNetworkLink**](VirtualNetworkLink.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The virtual network link to the Private DNS zone has been updated. |  -  |
| **202** | The operation to link virtual network link to Private DNS zone has been accepted and will complete asynchronously. |  -  |
| **0** | Default response. It will be deserialized as per the Error definition. |  -  |

