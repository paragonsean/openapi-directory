# Semantria.ConfigurationApi

All URIs are relative to *https://api.semantria.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addConfigurations**](ConfigurationApi.md#addConfigurations) | **POST** /configurations.{content_type} | Create user configurations
[**deleteConfigurations**](ConfigurationApi.md#deleteConfigurations) | **DELETE** /configurations.{content_type} | Remove user configurations
[**getConfigurations**](ConfigurationApi.md#getConfigurations) | **GET** /configurations.{content_type} | Retrieve user configurations
[**updateConfigurations**](ConfigurationApi.md#updateConfigurations) | **PUT** /configurations.{content_type} | Update user configurations



## addConfigurations

> [ConfigurationResponseVersion] addConfigurations(contentType, configurations)

Create user configurations

This method creates configurations on Semantria side.

### Example

```javascript
import Semantria from 'semantria';

let apiInstance = new Semantria.ConfigurationApi();
let contentType = "contentType_example"; // String | 
let configurations = {key: null}; // Object | List of parametrized JSON or XML objects.
apiInstance.addConfigurations(contentType, configurations, (error, data, response) => {
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
 **contentType** | **String**|  | 
 **configurations** | **Object**| List of parametrized JSON or XML objects. | 

### Return type

[**[ConfigurationResponseVersion]**](ConfigurationResponseVersion.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## deleteConfigurations

> deleteConfigurations(contentType, configurationIDs)

Remove user configurations

This method removes certain configuration by unique ID on Semantria side.

### Example

```javascript
import Semantria from 'semantria';

let apiInstance = new Semantria.ConfigurationApi();
let contentType = "contentType_example"; // String | 
let configurationIDs = ["null"]; // [String] | List of configuration identifiers.
apiInstance.deleteConfigurations(contentType, configurationIDs, (error, data, response) => {
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
 **contentType** | **String**|  | 
 **configurationIDs** | [**[String]**](String.md)| List of configuration identifiers. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getConfigurations

> [ConfigurationResponseVersion] getConfigurations(contentType)

Retrieve user configurations

This method retrieves all user configurations available on Semantria side.

### Example

```javascript
import Semantria from 'semantria';

let apiInstance = new Semantria.ConfigurationApi();
let contentType = "contentType_example"; // String | 
apiInstance.getConfigurations(contentType, (error, data, response) => {
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
 **contentType** | **String**|  | 

### Return type

[**[ConfigurationResponseVersion]**](ConfigurationResponseVersion.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## updateConfigurations

> [ConfigurationResponseVersion] updateConfigurations(contentType, configurations)

Update user configurations

This method updates specific configurations by unique IDs on Semantria side.

### Example

```javascript
import Semantria from 'semantria';

let apiInstance = new Semantria.ConfigurationApi();
let contentType = "contentType_example"; // String | 
let configurations = {key: null}; // Object | List of parametrized JSON or XML objects.
apiInstance.updateConfigurations(contentType, configurations, (error, data, response) => {
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
 **contentType** | **String**|  | 
 **configurations** | **Object**| List of parametrized JSON or XML objects. | 

### Return type

[**[ConfigurationResponseVersion]**](ConfigurationResponseVersion.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

