# GrowthServices.ProductLifecycleManagementApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**lifecycleManyToOnePost**](ProductLifecycleManagementApi.md#lifecycleManyToOnePost) | **POST** /lifecycle/many-to-one | Map from old product to new product to create artifical history
[**lifecycleOneToOnePost**](ProductLifecycleManagementApi.md#lifecycleOneToOnePost) | **POST** /lifecycle/one-to-one | Map from old product to new product to create artifical history



## lifecycleManyToOnePost

> PlanningLevelDataDto lifecycleManyToOnePost(opts)

Map from old product to new product to create artifical history

Supports the creation of artificial startup history for new products, based on a flexible mapping of old to new. This is an Enterprise feature.

### Example

```javascript
import GrowthServices from 'growth_services';

let apiInstance = new GrowthServices.ProductLifecycleManagementApi();
let opts = {
  'token': "token_example", // String | User Authentication Token
  'lifecycleManyToOneRequest': new GrowthServices.LifecycleManyToOneRequest() // LifecycleManyToOneRequest | 
};
apiInstance.lifecycleManyToOnePost(opts, (error, data, response) => {
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
 **token** | **String**| User Authentication Token | [optional] 
 **lifecycleManyToOneRequest** | [**LifecycleManyToOneRequest**](LifecycleManyToOneRequest.md)|  | [optional] 

### Return type

[**PlanningLevelDataDto**](PlanningLevelDataDto.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/*+json, application/json, text/json
- **Accept**: application/json, text/json, text/plain


## lifecycleOneToOnePost

> PlanningLevelDataDto lifecycleOneToOnePost(opts)

Map from old product to new product to create artifical history

Supports the creation of artificial startup history for new products, based on a flexible mapping of old to new. This is an Enterprise feature.

### Example

```javascript
import GrowthServices from 'growth_services';

let apiInstance = new GrowthServices.ProductLifecycleManagementApi();
let opts = {
  'token': "token_example", // String | User Authentication Token
  'lifecycleOneToOneRequest': new GrowthServices.LifecycleOneToOneRequest() // LifecycleOneToOneRequest | 
};
apiInstance.lifecycleOneToOnePost(opts, (error, data, response) => {
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
 **token** | **String**| User Authentication Token | [optional] 
 **lifecycleOneToOneRequest** | [**LifecycleOneToOneRequest**](LifecycleOneToOneRequest.md)|  | [optional] 

### Return type

[**PlanningLevelDataDto**](PlanningLevelDataDto.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/*+json, application/json, text/json
- **Accept**: application/json, text/json, text/plain

