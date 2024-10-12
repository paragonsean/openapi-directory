# PiWebApi2018Sp1SwaggerSpec.AttributeTraitApi

All URIs are relative to *https://devdata.osisoft.com/piwebapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**attributeTraitGet**](AttributeTraitApi.md#attributeTraitGet) | **GET** /attributetraits/{name} | Retrieve an attribute trait.
[**attributeTraitGetByCategory**](AttributeTraitApi.md#attributeTraitGetByCategory) | **GET** /attributetraits | Retrieve all attribute traits of the specified category/categories.



## attributeTraitGet

> AttributeTrait attributeTraitGet(name, opts)

Retrieve an attribute trait.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.AttributeTraitApi();
let name = "name_example"; // String | The name or abbreviation of the attribute trait.
let opts = {
  'selectedFields': "selectedFields_example" // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
};
apiInstance.attributeTraitGet(name, opts, (error, data, response) => {
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
 **name** | **String**| The name or abbreviation of the attribute trait. | 
 **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 

### Return type

[**AttributeTrait**](AttributeTrait.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/html, application/x-ms-application


## attributeTraitGetByCategory

> ItemsAttributeTrait attributeTraitGetByCategory(category, opts)

Retrieve all attribute traits of the specified category/categories.

### Example

```javascript
import PiWebApi2018Sp1SwaggerSpec from 'pi_web_api_2018_sp1_swagger_spec';

let apiInstance = new PiWebApi2018Sp1SwaggerSpec.AttributeTraitApi();
let category = ["null"]; // [String] | The category of the attribute traits. Multiple categories may be specified with multiple instances of the parameter. If the parameter is not specified, or if its value is \"all\", then all attribute traits of all categories will be returned.
let opts = {
  'selectedFields': "selectedFields_example" // String | List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned.
};
apiInstance.attributeTraitGetByCategory(category, opts, (error, data, response) => {
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
 **category** | [**[String]**](String.md)| The category of the attribute traits. Multiple categories may be specified with multiple instances of the parameter. If the parameter is not specified, or if its value is \&quot;all\&quot;, then all attribute traits of all categories will be returned. | 
 **selectedFields** | **String**| List of fields to be returned in the response, separated by semicolons (;). If this parameter is not specified, all available fields will be returned. | [optional] 

### Return type

[**ItemsAttributeTrait**](ItemsAttributeTrait.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/html, application/x-ms-application

