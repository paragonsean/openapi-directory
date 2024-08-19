# ProductOfferingsApi

All URIs are relative to */api/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**productOfferingsList**](ProductOfferingsApi.md#productOfferingsList) | **GET** /product-offerings |  |
| [**productOfferingsRead**](ProductOfferingsApi.md#productOfferingsRead) | **GET** /product-offerings/{id} |  |


<a id="productOfferingsList"></a>
# **productOfferingsList**
> List&lt;ProductOfferingPartial&gt; productOfferingsList(id, type, name, handoverMetroArea, handoverMetroAreaNetwork, serviceMetroArea, serviceMetroAreaNetwork, serviceProvider, downgradeAllowed, upgradeAllowed, bandwidth, physicalPortSpeed, serviceProviderRegion, serviceProviderPop, deliveryMethod, cloudKey, fields)



List all (filtered) products-offerings available on the platform

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductOfferingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");
    
    // Configure HTTP bearer authorization: Bearer
    HttpBearerAuth Bearer = (HttpBearerAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setBearerToken("BEARER TOKEN");

    ProductOfferingsApi apiInstance = new ProductOfferingsApi(defaultClient);
    List<String> id = Arrays.asList(); // List<String> | Filter by id
    String type = "exchange_lan"; // String | Filter by type
    String name = "name_example"; // String | Filter by name
    String handoverMetroArea = "handoverMetroArea_example"; // String | Filter by handover_metro_area
    String handoverMetroAreaNetwork = "handoverMetroAreaNetwork_example"; // String | Filter by handover_metro_area_network
    String serviceMetroArea = "serviceMetroArea_example"; // String | Filter by service_metro_area
    String serviceMetroAreaNetwork = "serviceMetroAreaNetwork_example"; // String | Filter by service_metro_area_network
    String serviceProvider = "serviceProvider_example"; // String | Filter by service_provider
    String downgradeAllowed = "true"; // String | Filter by downgrade_allowed
    String upgradeAllowed = "true"; // String | Filter by upgrade_allowed
    Integer bandwidth = 56; // Integer | Find product offerings where bandwidth is within the range of `bandwidth_min` and `bandwidth_max`.
    Integer physicalPortSpeed = 56; // Integer | Filter by physical_port_speed
    String serviceProviderRegion = "serviceProviderRegion_example"; // String | Filter by service_provider_region
    String serviceProviderPop = "serviceProviderPop_example"; // String | Filter by service_provider_pop
    String deliveryMethod = "dedicated"; // String | Filter by delivery_method
    String cloudKey = "cloudKey_example"; // String | For product offerings of type `cloud_vc`, if the `service_provider_workflow` is `provider_first` the `cloud_key` will be used for filtering the relevant offerings.
    String fields = "handover_metro_area,service_provider"; // String | Returned objects only have properties which are present in the list of fields. The required `type` property is *implicitly* included. The results are *deduplicated*. 
    try {
      List<ProductOfferingPartial> result = apiInstance.productOfferingsList(id, type, name, handoverMetroArea, handoverMetroAreaNetwork, serviceMetroArea, serviceMetroAreaNetwork, serviceProvider, downgradeAllowed, upgradeAllowed, bandwidth, physicalPortSpeed, serviceProviderRegion, serviceProviderPop, deliveryMethod, cloudKey, fields);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductOfferingsApi#productOfferingsList");
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
| **id** | [**List&lt;String&gt;**](String.md)| Filter by id | [optional] |
| **type** | **String**| Filter by type | [optional] [enum: exchange_lan, p2p_vc, mp2mp_vc, p2mp_vc, cloud_vc] |
| **name** | **String**| Filter by name | [optional] |
| **handoverMetroArea** | **String**| Filter by handover_metro_area | [optional] |
| **handoverMetroAreaNetwork** | **String**| Filter by handover_metro_area_network | [optional] |
| **serviceMetroArea** | **String**| Filter by service_metro_area | [optional] |
| **serviceMetroAreaNetwork** | **String**| Filter by service_metro_area_network | [optional] |
| **serviceProvider** | **String**| Filter by service_provider | [optional] |
| **downgradeAllowed** | **String**| Filter by downgrade_allowed | [optional] [enum: true, true] |
| **upgradeAllowed** | **String**| Filter by upgrade_allowed | [optional] [enum: true, false] |
| **bandwidth** | **Integer**| Find product offerings where bandwidth is within the range of &#x60;bandwidth_min&#x60; and &#x60;bandwidth_max&#x60;. | [optional] |
| **physicalPortSpeed** | **Integer**| Filter by physical_port_speed | [optional] |
| **serviceProviderRegion** | **String**| Filter by service_provider_region | [optional] |
| **serviceProviderPop** | **String**| Filter by service_provider_pop | [optional] |
| **deliveryMethod** | **String**| Filter by delivery_method | [optional] [enum: dedicated, shared] |
| **cloudKey** | **String**| For product offerings of type &#x60;cloud_vc&#x60;, if the &#x60;service_provider_workflow&#x60; is &#x60;provider_first&#x60; the &#x60;cloud_key&#x60; will be used for filtering the relevant offerings. | [optional] |
| **fields** | **String**| Returned objects only have properties which are present in the list of fields. The required &#x60;type&#x60; property is *implicitly* included. The results are *deduplicated*.  | [optional] |

### Return type

[**List&lt;ProductOfferingPartial&gt;**](ProductOfferingPartial.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of: Polymorphic Product Offering |  -  |
| **400** | ValidationError |  -  |
| **401** | Authentication |  -  |
| **403** | PermissionDenied |  -  |

<a id="productOfferingsRead"></a>
# **productOfferingsRead**
> ProductOffering productOfferingsRead(id)



Get a single products-offering by id.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductOfferingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");
    
    // Configure HTTP bearer authorization: Bearer
    HttpBearerAuth Bearer = (HttpBearerAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setBearerToken("BEARER TOKEN");

    ProductOfferingsApi apiInstance = new ProductOfferingsApi(defaultClient);
    String id = "id_example"; // String | Get by id
    try {
      ProductOffering result = apiInstance.productOfferingsRead(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductOfferingsApi#productOfferingsRead");
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
| **id** | **String**| Get by id | |

### Return type

[**ProductOffering**](ProductOffering.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Polymorphic Product Offering |  -  |
| **401** | Authentication |  -  |
| **403** | PermissionDenied |  -  |
| **404** | NotFound |  -  |

