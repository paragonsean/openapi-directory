# PrivateZonesApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**privateZonesCreateOrUpdate**](PrivateZonesApi.md#privateZonesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/privateDnsZones/{privateZoneName} |  |
| [**privateZonesDelete**](PrivateZonesApi.md#privateZonesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/privateDnsZones/{privateZoneName} |  |
| [**privateZonesGet**](PrivateZonesApi.md#privateZonesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/privateDnsZones/{privateZoneName} |  |
| [**privateZonesList**](PrivateZonesApi.md#privateZonesList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Network/privateDnsZones |  |
| [**privateZonesListByResourceGroup**](PrivateZonesApi.md#privateZonesListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/privateDnsZones |  |
| [**privateZonesUpdate**](PrivateZonesApi.md#privateZonesUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/privateDnsZones/{privateZoneName} |  |


<a id="privateZonesCreateOrUpdate"></a>
# **privateZonesCreateOrUpdate**
> PrivateZone privateZonesCreateOrUpdate(resourceGroupName, privateZoneName, apiVersion, subscriptionId, parameters, ifMatch, ifNoneMatch)



Creates or updates a Private DNS zone. Does not modify Links to virtual networks or DNS records within the zone.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PrivateZonesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    PrivateZonesApi apiInstance = new PrivateZonesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String privateZoneName = "privateZoneName_example"; // String | The name of the Private DNS zone (without a terminating dot).
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    PrivateZone parameters = new PrivateZone(); // PrivateZone | Parameters supplied to the CreateOrUpdate operation.
    String ifMatch = "ifMatch_example"; // String | The ETag of the Private DNS zone. Omit this value to always overwrite the current zone. Specify the last-seen ETag value to prevent accidentally overwriting any concurrent changes.
    String ifNoneMatch = "ifNoneMatch_example"; // String | Set to '*' to allow a new Private DNS zone to be created, but to prevent updating an existing zone. Other values will be ignored.
    try {
      PrivateZone result = apiInstance.privateZonesCreateOrUpdate(resourceGroupName, privateZoneName, apiVersion, subscriptionId, parameters, ifMatch, ifNoneMatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PrivateZonesApi#privateZonesCreateOrUpdate");
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
| **parameters** | [**PrivateZone**](PrivateZone.md)| Parameters supplied to the CreateOrUpdate operation. | |
| **ifMatch** | **String**| The ETag of the Private DNS zone. Omit this value to always overwrite the current zone. Specify the last-seen ETag value to prevent accidentally overwriting any concurrent changes. | [optional] |
| **ifNoneMatch** | **String**| Set to &#39;*&#39; to allow a new Private DNS zone to be created, but to prevent updating an existing zone. Other values will be ignored. | [optional] |

### Return type

[**PrivateZone**](PrivateZone.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The Private DNS zone has been updated. |  -  |
| **201** | The Private DNS zone has been created. |  -  |
| **202** | The Private DNS zone upsert operation has been accepted and will complete asynchronously. |  -  |
| **0** | Default response. It will be deserialized as per the Error definition. |  -  |

<a id="privateZonesDelete"></a>
# **privateZonesDelete**
> privateZonesDelete(resourceGroupName, privateZoneName, apiVersion, subscriptionId, ifMatch)



Deletes a Private DNS zone. WARNING: All DNS records in the zone will also be deleted. This operation cannot be undone. Private DNS zone cannot be deleted unless all virtual network links to it are removed.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PrivateZonesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    PrivateZonesApi apiInstance = new PrivateZonesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String privateZoneName = "privateZoneName_example"; // String | The name of the Private DNS zone (without a terminating dot).
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    String ifMatch = "ifMatch_example"; // String | The ETag of the Private DNS zone. Omit this value to always delete the current zone. Specify the last-seen ETag value to prevent accidentally deleting any concurrent changes.
    try {
      apiInstance.privateZonesDelete(resourceGroupName, privateZoneName, apiVersion, subscriptionId, ifMatch);
    } catch (ApiException e) {
      System.err.println("Exception when calling PrivateZonesApi#privateZonesDelete");
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
| **ifMatch** | **String**| The ETag of the Private DNS zone. Omit this value to always delete the current zone. Specify the last-seen ETag value to prevent accidentally deleting any concurrent changes. | [optional] |

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
| **200** | The Private DNS zone has been deleted. |  -  |
| **202** | The Private DNS zone delete operation has been accepted and will complete asynchronously. |  -  |
| **204** | The Private DNS zone was not found. |  -  |
| **0** | Default response. It will be deserialized as per the Error definition. |  -  |

<a id="privateZonesGet"></a>
# **privateZonesGet**
> PrivateZone privateZonesGet(resourceGroupName, privateZoneName, apiVersion, subscriptionId)



Gets a Private DNS zone. Retrieves the zone properties, but not the virtual networks links or the record sets within the zone.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PrivateZonesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    PrivateZonesApi apiInstance = new PrivateZonesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String privateZoneName = "privateZoneName_example"; // String | The name of the Private DNS zone (without a terminating dot).
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    try {
      PrivateZone result = apiInstance.privateZonesGet(resourceGroupName, privateZoneName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PrivateZonesApi#privateZonesGet");
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

### Return type

[**PrivateZone**](PrivateZone.md)

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

<a id="privateZonesList"></a>
# **privateZonesList**
> PrivateZoneListResult privateZonesList(apiVersion, subscriptionId, $top)



Lists the Private DNS zones in all resource groups in a subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PrivateZonesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    PrivateZonesApi apiInstance = new PrivateZonesApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    Integer $top = 56; // Integer | The maximum number of Private DNS zones to return. If not specified, returns up to 100 zones.
    try {
      PrivateZoneListResult result = apiInstance.privateZonesList(apiVersion, subscriptionId, $top);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PrivateZonesApi#privateZonesList");
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
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **$top** | **Integer**| The maximum number of Private DNS zones to return. If not specified, returns up to 100 zones. | [optional] |

### Return type

[**PrivateZoneListResult**](PrivateZoneListResult.md)

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

<a id="privateZonesListByResourceGroup"></a>
# **privateZonesListByResourceGroup**
> PrivateZoneListResult privateZonesListByResourceGroup(resourceGroupName, apiVersion, subscriptionId, $top)



Lists the Private DNS zones within a resource group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PrivateZonesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    PrivateZonesApi apiInstance = new PrivateZonesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    Integer $top = 56; // Integer | The maximum number of record sets to return. If not specified, returns up to 100 record sets.
    try {
      PrivateZoneListResult result = apiInstance.privateZonesListByResourceGroup(resourceGroupName, apiVersion, subscriptionId, $top);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PrivateZonesApi#privateZonesListByResourceGroup");
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
| **apiVersion** | **String**| Client Api Version. | |
| **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | |
| **$top** | **Integer**| The maximum number of record sets to return. If not specified, returns up to 100 record sets. | [optional] |

### Return type

[**PrivateZoneListResult**](PrivateZoneListResult.md)

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

<a id="privateZonesUpdate"></a>
# **privateZonesUpdate**
> PrivateZone privateZonesUpdate(resourceGroupName, privateZoneName, apiVersion, subscriptionId, parameters, ifMatch)



Updates a Private DNS zone. Does not modify virtual network links or DNS records within the zone.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PrivateZonesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    PrivateZonesApi apiInstance = new PrivateZonesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
    String privateZoneName = "privateZoneName_example"; // String | The name of the Private DNS zone (without a terminating dot).
    String apiVersion = "apiVersion_example"; // String | Client Api Version.
    String subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    PrivateZone parameters = new PrivateZone(); // PrivateZone | Parameters supplied to the Update operation.
    String ifMatch = "ifMatch_example"; // String | The ETag of the Private DNS zone. Omit this value to always overwrite the current zone. Specify the last-seen ETag value to prevent accidentally overwriting any concurrent changes.
    try {
      PrivateZone result = apiInstance.privateZonesUpdate(resourceGroupName, privateZoneName, apiVersion, subscriptionId, parameters, ifMatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PrivateZonesApi#privateZonesUpdate");
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
| **parameters** | [**PrivateZone**](PrivateZone.md)| Parameters supplied to the Update operation. | |
| **ifMatch** | **String**| The ETag of the Private DNS zone. Omit this value to always overwrite the current zone. Specify the last-seen ETag value to prevent accidentally overwriting any concurrent changes. | [optional] |

### Return type

[**PrivateZone**](PrivateZone.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The Private DNS zone has been updated. |  -  |
| **202** | The Private DNS zone update operation has been accepted and will complete asynchronously. |  -  |
| **0** | Default response. It will be deserialized as per the Error definition. |  -  |

