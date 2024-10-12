# ZonesApi

All URIs are relative to *https://management.azure.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**zonesCreateOrUpdate**](ZonesApi.md#zonesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/dnsZones/{zoneName} |  |
| [**zonesDelete**](ZonesApi.md#zonesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/dnsZones/{zoneName} |  |
| [**zonesGet**](ZonesApi.md#zonesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/dnsZones/{zoneName} |  |
| [**zonesList**](ZonesApi.md#zonesList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Network/dnszones |  |
| [**zonesListByResourceGroup**](ZonesApi.md#zonesListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/dnsZones |  |
| [**zonesUpdate**](ZonesApi.md#zonesUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/dnsZones/{zoneName} |  |


<a id="zonesCreateOrUpdate"></a>
# **zonesCreateOrUpdate**
> Zone zonesCreateOrUpdate(resourceGroupName, zoneName, apiVersion, subscriptionId, parameters, ifMatch, ifNoneMatch)



Creates or updates a DNS zone. Does not modify DNS records within the zone.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ZonesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    ZonesApi apiInstance = new ZonesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
    String zoneName = "zoneName_example"; // String | The name of the DNS zone (without a terminating dot).
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    Zone parameters = new Zone(); // Zone | Parameters supplied to the CreateOrUpdate operation.
    String ifMatch = "ifMatch_example"; // String | The etag of the DNS zone. Omit this value to always overwrite the current zone. Specify the last-seen etag value to prevent accidentally overwriting any concurrent changes.
    String ifNoneMatch = "ifNoneMatch_example"; // String | Set to '*' to allow a new DNS zone to be created, but to prevent updating an existing zone. Other values will be ignored.
    try {
      Zone result = apiInstance.zonesCreateOrUpdate(resourceGroupName, zoneName, apiVersion, subscriptionId, parameters, ifMatch, ifNoneMatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ZonesApi#zonesCreateOrUpdate");
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
| **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | |
| **zoneName** | **String**| The name of the DNS zone (without a terminating dot). | |
| **apiVersion** | **String**| The API version to use for this operation. | |
| **subscriptionId** | **String**| The ID of the target subscription. | |
| **parameters** | [**Zone**](Zone.md)| Parameters supplied to the CreateOrUpdate operation. | |
| **ifMatch** | **String**| The etag of the DNS zone. Omit this value to always overwrite the current zone. Specify the last-seen etag value to prevent accidentally overwriting any concurrent changes. | [optional] |
| **ifNoneMatch** | **String**| Set to &#39;*&#39; to allow a new DNS zone to be created, but to prevent updating an existing zone. Other values will be ignored. | [optional] |

### Return type

[**Zone**](Zone.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The DNS zone has been updated. |  -  |
| **201** | The DNS zone has been created. |  -  |
| **0** | Default response. It will be deserialized as per the Error definition. |  -  |

<a id="zonesDelete"></a>
# **zonesDelete**
> zonesDelete(resourceGroupName, zoneName, apiVersion, subscriptionId, ifMatch)



Deletes a DNS zone. WARNING: All DNS records in the zone will also be deleted. This operation cannot be undone.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ZonesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    ZonesApi apiInstance = new ZonesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
    String zoneName = "zoneName_example"; // String | The name of the DNS zone (without a terminating dot).
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    String ifMatch = "ifMatch_example"; // String | The etag of the DNS zone. Omit this value to always delete the current zone. Specify the last-seen etag value to prevent accidentally deleting any concurrent changes.
    try {
      apiInstance.zonesDelete(resourceGroupName, zoneName, apiVersion, subscriptionId, ifMatch);
    } catch (ApiException e) {
      System.err.println("Exception when calling ZonesApi#zonesDelete");
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
| **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | |
| **zoneName** | **String**| The name of the DNS zone (without a terminating dot). | |
| **apiVersion** | **String**| The API version to use for this operation. | |
| **subscriptionId** | **String**| The ID of the target subscription. | |
| **ifMatch** | **String**| The etag of the DNS zone. Omit this value to always delete the current zone. Specify the last-seen etag value to prevent accidentally deleting any concurrent changes. | [optional] |

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
| **200** | The DNS zone has been deleted. |  -  |
| **202** | The DNS zone delete operation has been accepted and will complete asynchronously. |  -  |
| **204** | The DNS zone was not found. |  -  |
| **0** | Default response. It will be deserialized as per the Error definition. |  -  |

<a id="zonesGet"></a>
# **zonesGet**
> Zone zonesGet(resourceGroupName, zoneName, apiVersion, subscriptionId)



Gets a DNS zone. Retrieves the zone properties, but not the record sets within the zone.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ZonesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    ZonesApi apiInstance = new ZonesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
    String zoneName = "zoneName_example"; // String | The name of the DNS zone (without a terminating dot).
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    try {
      Zone result = apiInstance.zonesGet(resourceGroupName, zoneName, apiVersion, subscriptionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ZonesApi#zonesGet");
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
| **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | |
| **zoneName** | **String**| The name of the DNS zone (without a terminating dot). | |
| **apiVersion** | **String**| The API version to use for this operation. | |
| **subscriptionId** | **String**| The ID of the target subscription. | |

### Return type

[**Zone**](Zone.md)

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

<a id="zonesList"></a>
# **zonesList**
> ZoneListResult zonesList(apiVersion, subscriptionId, $top)



Lists the DNS zones in all resource groups in a subscription.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ZonesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    ZonesApi apiInstance = new ZonesApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    Integer $top = 56; // Integer | The maximum number of DNS zones to return. If not specified, returns up to 100 zones.
    try {
      ZoneListResult result = apiInstance.zonesList(apiVersion, subscriptionId, $top);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ZonesApi#zonesList");
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
| **apiVersion** | **String**| The API version to use for this operation. | |
| **subscriptionId** | **String**| The ID of the target subscription. | |
| **$top** | **Integer**| The maximum number of DNS zones to return. If not specified, returns up to 100 zones. | [optional] |

### Return type

[**ZoneListResult**](ZoneListResult.md)

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

<a id="zonesListByResourceGroup"></a>
# **zonesListByResourceGroup**
> ZoneListResult zonesListByResourceGroup(resourceGroupName, apiVersion, subscriptionId, $top)



Lists the DNS zones within a resource group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ZonesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    ZonesApi apiInstance = new ZonesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    Integer $top = 56; // Integer | The maximum number of record sets to return. If not specified, returns up to 100 record sets.
    try {
      ZoneListResult result = apiInstance.zonesListByResourceGroup(resourceGroupName, apiVersion, subscriptionId, $top);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ZonesApi#zonesListByResourceGroup");
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
| **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | |
| **apiVersion** | **String**| The API version to use for this operation. | |
| **subscriptionId** | **String**| The ID of the target subscription. | |
| **$top** | **Integer**| The maximum number of record sets to return. If not specified, returns up to 100 record sets. | [optional] |

### Return type

[**ZoneListResult**](ZoneListResult.md)

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

<a id="zonesUpdate"></a>
# **zonesUpdate**
> Zone zonesUpdate(resourceGroupName, zoneName, apiVersion, subscriptionId, parameters, ifMatch)



Updates a DNS zone. Does not modify DNS records within the zone.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ZonesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management.azure.com");

    ZonesApi apiInstance = new ZonesApi(defaultClient);
    String resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
    String zoneName = "zoneName_example"; // String | The name of the DNS zone (without a terminating dot).
    String apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
    String subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
    ZoneUpdate parameters = new ZoneUpdate(); // ZoneUpdate | Parameters supplied to the Update operation.
    String ifMatch = "ifMatch_example"; // String | The etag of the DNS zone. Omit this value to always overwrite the current zone. Specify the last-seen etag value to prevent accidentally overwriting any concurrent changes.
    try {
      Zone result = apiInstance.zonesUpdate(resourceGroupName, zoneName, apiVersion, subscriptionId, parameters, ifMatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ZonesApi#zonesUpdate");
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
| **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | |
| **zoneName** | **String**| The name of the DNS zone (without a terminating dot). | |
| **apiVersion** | **String**| The API version to use for this operation. | |
| **subscriptionId** | **String**| The ID of the target subscription. | |
| **parameters** | [**ZoneUpdate**](ZoneUpdate.md)| Parameters supplied to the Update operation. | |
| **ifMatch** | **String**| The etag of the DNS zone. Omit this value to always overwrite the current zone. Specify the last-seen etag value to prevent accidentally overwriting any concurrent changes. | [optional] |

### Return type

[**Zone**](Zone.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The DNS zone has been updated. |  -  |
| **0** | Default response. It will be deserialized as per the Error definition. |  -  |

