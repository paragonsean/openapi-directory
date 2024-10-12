# CleverCloudApi.ProductsApi

All URIs are relative to *https://api.clever-cloud.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getProductsAddonProvidersProviderId_0**](ProductsApi.md#getProductsAddonProvidersProviderId_0) | **GET** /products/addonproviders/{provider_id} | 
[**getProductsAddonProviders_0**](ProductsApi.md#getProductsAddonProviders_0) | **GET** /products/addonproviders | 
[**getProductsCountries_0**](ProductsApi.md#getProductsCountries_0) | **GET** /products/countries | 
[**getProductsCountrycodes_0**](ProductsApi.md#getProductsCountrycodes_0) | **GET** /products/countrycodes | 
[**getProductsInstancesTypeVersion_0**](ProductsApi.md#getProductsInstancesTypeVersion_0) | **GET** /products/instances/{type}-{version} | 
[**getProductsInstances_0**](ProductsApi.md#getProductsInstances_0) | **GET** /products/instances | 
[**getProductsPackages_0**](ProductsApi.md#getProductsPackages_0) | **GET** /products/packages | 
[**getProductsPrices_0**](ProductsApi.md#getProductsPrices_0) | **GET** /products/prices | 
[**getProductsZones_0**](ProductsApi.md#getProductsZones_0) | **GET** /products/zones | 
[**productsAddonprovidersProviderIdVersionsGet_0**](ProductsApi.md#productsAddonprovidersProviderIdVersionsGet_0) | **GET** /products/addonproviders/{provider_id}/versions | 
[**productsMfaKindsGet_0**](ProductsApi.md#productsMfaKindsGet_0) | **GET** /products/mfa_kinds | 



## getProductsAddonProvidersProviderId_0

> Provider getProductsAddonProvidersProviderId_0(providerId)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.ProductsApi();
let providerId = "providerId_example"; // String | 
apiInstance.getProductsAddonProvidersProviderId_0(providerId, (error, data, response) => {
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
 **providerId** | **String**|  | 

### Return type

[**Provider**](Provider.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getProductsAddonProviders_0

> [Provider] getProductsAddonProviders_0()



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.ProductsApi();
apiInstance.getProductsAddonProviders_0((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**[Provider]**](Provider.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getProductsCountries_0

> Country getProductsCountries_0()



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.ProductsApi();
apiInstance.getProductsCountries_0((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**Country**](Country.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getProductsCountrycodes_0

> Country getProductsCountrycodes_0()



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.ProductsApi();
apiInstance.getProductsCountrycodes_0((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**Country**](Country.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getProductsInstancesTypeVersion_0

> Instance getProductsInstancesTypeVersion_0(type, version, opts)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.ProductsApi();
let type = "type_example"; // String | 
let version = "version_example"; // String | 
let opts = {
  '_for': "_for_example", // String | 
  'app': "app_example" // String | 
};
apiInstance.getProductsInstancesTypeVersion_0(type, version, opts, (error, data, response) => {
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
 **type** | **String**|  | 
 **version** | **String**|  | 
 **_for** | **String**|  | [optional] 
 **app** | **String**|  | [optional] 

### Return type

[**Instance**](Instance.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getProductsInstances_0

> [Instance] getProductsInstances_0(opts)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.ProductsApi();
let opts = {
  '_for': "_for_example" // String | 
};
apiInstance.getProductsInstances_0(opts, (error, data, response) => {
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
 **_for** | **String**|  | [optional] 

### Return type

[**[Instance]**](Instance.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getProductsPackages_0

> getProductsPackages_0(opts)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.ProductsApi();
let opts = {
  'coupon': "coupon_example", // String | 
  'orgaId': "orgaId_example", // String | 
  'currency': "currency_example" // String | 
};
apiInstance.getProductsPackages_0(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **coupon** | **String**|  | [optional] 
 **orgaId** | **String**|  | [optional] 
 **currency** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getProductsPrices_0

> getProductsPrices_0()



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.ProductsApi();
apiInstance.getProductsPrices_0((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getProductsZones_0

> [Zone] getProductsZones_0()



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.ProductsApi();
apiInstance.getProductsZones_0((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**[Zone]**](Zone.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## productsAddonprovidersProviderIdVersionsGet_0

> productsAddonprovidersProviderIdVersionsGet_0(providerId)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.ProductsApi();
let providerId = "providerId_example"; // String | 
apiInstance.productsAddonprovidersProviderIdVersionsGet_0(providerId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **providerId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## productsMfaKindsGet_0

> productsMfaKindsGet_0()



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.ProductsApi();
apiInstance.productsMfaKindsGet_0((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

