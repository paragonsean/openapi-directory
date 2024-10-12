# EuBonUtis.UtisControllerApi

All URIs are relative to *http://cybertaxonomy.eu/eu-bon/utis/1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**capabilities**](UtisControllerApi.md#capabilities) | **GET** /capabilities | capabilities
[**search**](UtisControllerApi.md#search) | **GET** /search | search



## capabilities

> [ServiceProviderInfo] capabilities()

capabilities

capabilities

### Example

```javascript
import EuBonUtis from 'eu_bon_utis';

let apiInstance = new EuBonUtis.UtisControllerApi();
apiInstance.capabilities((error, data, response) => {
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

[**[ServiceProviderInfo]**](ServiceProviderInfo.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## search

> TnrMsg search(query, opts)

search

search

### Example

```javascript
import EuBonUtis from 'eu_bon_utis';

let apiInstance = new EuBonUtis.UtisControllerApi();
let query = "query_example"; // String | The scientific name to search for. For example: \"Bellis perennis\", \"Prionus\" or \"Bolinus brandaris\". This is an exact search so wildcard characters are not supported.
let opts = {
  'providers': "'pesi,eunis,bgbm-cdm-server[col]'", // String | A list of provider id strings concatenated by comma characters. The default : \"pesi,bgbm-cdm-server[col]\" will be used if this parameter is not set. A list of all available provider ids can be obtained from the '/capabilities' service end point. Providers can be nested, that is a parent provider can have sub providers. If the id of the parent provider is supplied all subproviders will be queried. The query can also be restriced to one or more subproviders by using the following syntax: parent-id[sub-id-1,sub-id2,...]
  'searchMode': "'scientificNameExact'", // String | Specifies the searchMode. Possible search modes are: scientificNameExact, scientificNameLike (begins with), vernacularNameExact, vernacularNameLike (contains), findByIdentifier. If the a provider does not support the chosen searchMode it will be skipped and the status message in the tnrClientStatus will be set to 'unsupported search mode' in this case.
  'addSynonymy': false, // Boolean | Indicates whether the synonymy of the accepted taxon should be included into the response. Turning this option on may cause an increased response time.
  'timeout': 0 // Number | The maximum of milliseconds to wait for responses from any of the providers. If the timeout is exceeded the service will jut return the resonses that have been received so far. The default timeout is 0 ms (wait for ever)
};
apiInstance.search(query, opts, (error, data, response) => {
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
 **query** | **String**| The scientific name to search for. For example: \&quot;Bellis perennis\&quot;, \&quot;Prionus\&quot; or \&quot;Bolinus brandaris\&quot;. This is an exact search so wildcard characters are not supported. | 
 **providers** | **String**| A list of provider id strings concatenated by comma characters. The default : \&quot;pesi,bgbm-cdm-server[col]\&quot; will be used if this parameter is not set. A list of all available provider ids can be obtained from the &#39;/capabilities&#39; service end point. Providers can be nested, that is a parent provider can have sub providers. If the id of the parent provider is supplied all subproviders will be queried. The query can also be restriced to one or more subproviders by using the following syntax: parent-id[sub-id-1,sub-id2,...] | [optional] [default to &#39;pesi,eunis,bgbm-cdm-server[col]&#39;]
 **searchMode** | **String**| Specifies the searchMode. Possible search modes are: scientificNameExact, scientificNameLike (begins with), vernacularNameExact, vernacularNameLike (contains), findByIdentifier. If the a provider does not support the chosen searchMode it will be skipped and the status message in the tnrClientStatus will be set to &#39;unsupported search mode&#39; in this case. | [optional] [default to &#39;scientificNameExact&#39;]
 **addSynonymy** | **Boolean**| Indicates whether the synonymy of the accepted taxon should be included into the response. Turning this option on may cause an increased response time. | [optional] [default to false]
 **timeout** | **Number**| The maximum of milliseconds to wait for responses from any of the providers. If the timeout is exceeded the service will jut return the resonses that have been received so far. The default timeout is 0 ms (wait for ever) | [optional] [default to 0]

### Return type

[**TnrMsg**](TnrMsg.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

