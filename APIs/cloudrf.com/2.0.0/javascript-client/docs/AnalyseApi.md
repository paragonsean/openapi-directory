# CloudRfApi.AnalyseApi

All URIs are relative to *https://api.cloudrf.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**interference**](AnalyseApi.md#interference) | **GET** /interference | Find the best server for overlapping coverage
[**mesh**](AnalyseApi.md#mesh) | **GET** /mesh | Merge sites into a super layer.
[**network**](AnalyseApi.md#network) | **GET** /network | Find the best server for somewhere



## interference

> interference(network, name)

Find the best server for overlapping coverage

Merge and analyse sites within a network channel to determine the best server at a given location. Each site will be dynamically allocated a monochrome colour from a palette and the strongest signal promoted at a given location.

### Example

```javascript
import CloudRfApi from 'cloud_rf_api';
let defaultClient = CloudRfApi.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new CloudRfApi.AnalyseApi();
let network = "network_example"; // String | Network name eg. Overlapping broadcast stations
let name = "name_example"; // String | Interference layer name eg. QRM_map
apiInstance.interference(network, name, (error, data, response) => {
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
 **network** | **String**| Network name eg. Overlapping broadcast stations | 
 **name** | **String**| Interference layer name eg. QRM_map | 

### Return type

null (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## mesh

> mesh(network, name)

Merge sites into a super layer.

A merge of &#39;area&#39; calculations for a network to create a single super layer. Stronger signals are promoted over weaker ones. The same colour key must be used.

### Example

```javascript
import CloudRfApi from 'cloud_rf_api';
let defaultClient = CloudRfApi.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new CloudRfApi.AnalyseApi();
let network = "network_example"; // String | Network name eg. 100_BLUE_repeaters_nationwide
let name = "name_example"; // String | Super layer name eg. National_map
apiInstance.mesh(network, name, (error, data, response) => {
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
 **network** | **String**| Network name eg. 100_BLUE_repeaters_nationwide | 
 **name** | **String**| Super layer name eg. National_map | 

### Return type

null (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## network

> network(net, nam, lat, lon, alt, opts)

Find the best server for somewhere

Query your network to find the best server(s) for a given receiver/customer location. A previously generated network is required.

### Example

```javascript
import CloudRfApi from 'cloud_rf_api';
let defaultClient = CloudRfApi.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new CloudRfApi.AnalyseApi();
let net = "net_example"; // String | Network name
let nam = "nam_example"; // String | Super layer name
let lat = 3.4; // Number | Latitude in decimal degrees
let lon = 3.4; // Number | Longitude in decimal degrees
let alt = 56; // Number | Height above ground level in metres
let opts = {
  'rxg': 3.4 // Number | Receiver gain in dBi
};
apiInstance.network(net, nam, lat, lon, alt, opts, (error, data, response) => {
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
 **net** | **String**| Network name | 
 **nam** | **String**| Super layer name | 
 **lat** | **Number**| Latitude in decimal degrees | 
 **lon** | **Number**| Longitude in decimal degrees | 
 **alt** | **Number**| Height above ground level in metres | 
 **rxg** | **Number**| Receiver gain in dBi | [optional] 

### Return type

null (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

