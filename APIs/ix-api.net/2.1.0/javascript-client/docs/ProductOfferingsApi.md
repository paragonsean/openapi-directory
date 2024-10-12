# IxApi.ProductOfferingsApi

All URIs are relative to */api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**productOfferingsList**](ProductOfferingsApi.md#productOfferingsList) | **GET** /product-offerings | 
[**productOfferingsRead**](ProductOfferingsApi.md#productOfferingsRead) | **GET** /product-offerings/{id} | 



## productOfferingsList

> [ProductOfferingPartial] productOfferingsList(opts)



List all (filtered) products-offerings available on the platform

### Example

```javascript
import IxApi from 'ix_api';
let defaultClient = IxApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IxApi.ProductOfferingsApi();
let opts = {
  'id': ["null"], // [String] | Filter by id
  'type': "type_example", // String | Filter by type
  'name': "name_example", // String | Filter by name
  'handoverMetroArea': "handoverMetroArea_example", // String | Filter by handover_metro_area
  'handoverMetroAreaNetwork': "handoverMetroAreaNetwork_example", // String | Filter by handover_metro_area_network
  'serviceMetroArea': "serviceMetroArea_example", // String | Filter by service_metro_area
  'serviceMetroAreaNetwork': "serviceMetroAreaNetwork_example", // String | Filter by service_metro_area_network
  'serviceProvider': "serviceProvider_example", // String | Filter by service_provider
  'downgradeAllowed': "downgradeAllowed_example", // String | Filter by downgrade_allowed
  'upgradeAllowed': "upgradeAllowed_example", // String | Filter by upgrade_allowed
  'bandwidth': 56, // Number | Find product offerings where bandwidth is within the range of `bandwidth_min` and `bandwidth_max`.
  'physicalPortSpeed': 56, // Number | Filter by physical_port_speed
  'serviceProviderRegion': "serviceProviderRegion_example", // String | Filter by service_provider_region
  'serviceProviderPop': "serviceProviderPop_example", // String | Filter by service_provider_pop
  'deliveryMethod': "deliveryMethod_example", // String | Filter by delivery_method
  'cloudKey': "cloudKey_example", // String | For product offerings of type `cloud_vc`, if the `service_provider_workflow` is `provider_first` the `cloud_key` will be used for filtering the relevant offerings.
  'fields': "handover_metro_area,service_provider" // String | Returned objects only have properties which are present in the list of fields. The required `type` property is *implicitly* included. The results are *deduplicated*. 
};
apiInstance.productOfferingsList(opts, (error, data, response) => {
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
 **id** | [**[String]**](String.md)| Filter by id | [optional] 
 **type** | **String**| Filter by type | [optional] 
 **name** | **String**| Filter by name | [optional] 
 **handoverMetroArea** | **String**| Filter by handover_metro_area | [optional] 
 **handoverMetroAreaNetwork** | **String**| Filter by handover_metro_area_network | [optional] 
 **serviceMetroArea** | **String**| Filter by service_metro_area | [optional] 
 **serviceMetroAreaNetwork** | **String**| Filter by service_metro_area_network | [optional] 
 **serviceProvider** | **String**| Filter by service_provider | [optional] 
 **downgradeAllowed** | **String**| Filter by downgrade_allowed | [optional] 
 **upgradeAllowed** | **String**| Filter by upgrade_allowed | [optional] 
 **bandwidth** | **Number**| Find product offerings where bandwidth is within the range of &#x60;bandwidth_min&#x60; and &#x60;bandwidth_max&#x60;. | [optional] 
 **physicalPortSpeed** | **Number**| Filter by physical_port_speed | [optional] 
 **serviceProviderRegion** | **String**| Filter by service_provider_region | [optional] 
 **serviceProviderPop** | **String**| Filter by service_provider_pop | [optional] 
 **deliveryMethod** | **String**| Filter by delivery_method | [optional] 
 **cloudKey** | **String**| For product offerings of type &#x60;cloud_vc&#x60;, if the &#x60;service_provider_workflow&#x60; is &#x60;provider_first&#x60; the &#x60;cloud_key&#x60; will be used for filtering the relevant offerings. | [optional] 
 **fields** | **String**| Returned objects only have properties which are present in the list of fields. The required &#x60;type&#x60; property is *implicitly* included. The results are *deduplicated*.  | [optional] 

### Return type

[**[ProductOfferingPartial]**](ProductOfferingPartial.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## productOfferingsRead

> ProductOffering productOfferingsRead(id)



Get a single products-offering by id.

### Example

```javascript
import IxApi from 'ix_api';
let defaultClient = IxApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IxApi.ProductOfferingsApi();
let id = "id_example"; // String | Get by id
apiInstance.productOfferingsRead(id, (error, data, response) => {
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
 **id** | **String**| Get by id | 

### Return type

[**ProductOffering**](ProductOffering.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

