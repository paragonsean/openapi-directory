# BridgedbWebservices.IdentifiersGenesProteinsMetabolitesInteractionsApi

All URIs are relative to *https://webservice.bridgedb.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**organismAttributeSearchQueryGet**](IdentifiersGenesProteinsMetabolitesInteractionsApi.md#organismAttributeSearchQueryGet) | **GET** /{organism}/attributeSearch/{query} | 
[**organismAttributeSetGet**](IdentifiersGenesProteinsMetabolitesInteractionsApi.md#organismAttributeSetGet) | **GET** /{organism}/attributeSet | 
[**organismAttributesSystemCodeIdentifierGet**](IdentifiersGenesProteinsMetabolitesInteractionsApi.md#organismAttributesSystemCodeIdentifierGet) | **GET** /{organism}/attributes/{systemCode}/{identifier} | 
[**organismIsFreeSearchSupportedGet**](IdentifiersGenesProteinsMetabolitesInteractionsApi.md#organismIsFreeSearchSupportedGet) | **GET** /{organism}/isFreeSearchSupported | 
[**organismIsMappingSupportedSourceSystemCodeTargetSystemCodeGet**](IdentifiersGenesProteinsMetabolitesInteractionsApi.md#organismIsMappingSupportedSourceSystemCodeTargetSystemCodeGet) | **GET** /{organism}/isMappingSupported/{sourceSystemCode}/{targetSystemCode} | 
[**organismPropertiesGet**](IdentifiersGenesProteinsMetabolitesInteractionsApi.md#organismPropertiesGet) | **GET** /{organism}/properties | 
[**organismSearchQueryGet**](IdentifiersGenesProteinsMetabolitesInteractionsApi.md#organismSearchQueryGet) | **GET** /{organism}/search/{query} | 
[**organismSourceDataSourcesGet**](IdentifiersGenesProteinsMetabolitesInteractionsApi.md#organismSourceDataSourcesGet) | **GET** /{organism}/sourceDataSources | 
[**organismTargetDataSourcesGet**](IdentifiersGenesProteinsMetabolitesInteractionsApi.md#organismTargetDataSourcesGet) | **GET** /{organism}/targetDataSources | 
[**organismXrefExistsSystemCodeIdentifierGet**](IdentifiersGenesProteinsMetabolitesInteractionsApi.md#organismXrefExistsSystemCodeIdentifierGet) | **GET** /{organism}/xrefExists/{systemCode}/{identifier} | 
[**organismXrefsBatchPost**](IdentifiersGenesProteinsMetabolitesInteractionsApi.md#organismXrefsBatchPost) | **POST** /{organism}/xrefsBatch | 
[**organismXrefsBatchSystemCodePost**](IdentifiersGenesProteinsMetabolitesInteractionsApi.md#organismXrefsBatchSystemCodePost) | **POST** /{organism}/xrefsBatch/{systemCode} | 
[**organismXrefsSystemCodeIdentifierGet**](IdentifiersGenesProteinsMetabolitesInteractionsApi.md#organismXrefsSystemCodeIdentifierGet) | **GET** /{organism}/xrefs/{systemCode}/{identifier} | 



## organismAttributeSearchQueryGet

> organismAttributeSearchQueryGet(organism, query, opts)



Returns a list of xrefs and associated attributes that contain the query string for a given organism. Results are not restricted to exact matches. Optionally limit results to a specified number per data source, or by the type of attribute. See possible attribute types via /{organism}/attributeSet. 

### Example

```javascript
import BridgedbWebservices from 'bridgedb_webservices';

let apiInstance = new BridgedbWebservices.IdentifiersGenesProteinsMetabolitesInteractionsApi();
let organism = "organism_example"; // String | Organism [Latin name](http://vocabularies.bridgedb.org/#latinName) or [short name](http://vocabularies.bridgedb.org/#shortName).
let query = "query_example"; // String | Text to find in attributes
let opts = {
  'limit': 56, // Number | Number of results
  'attrName': "attrName_example" // String | Restrict search by attribute name (case sensitive). Use GET /{organism}/attributeSet to find out which attributes are supported.
};
apiInstance.organismAttributeSearchQueryGet(organism, query, opts, (error, data, response) => {
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
 **organism** | **String**| Organism [Latin name](http://vocabularies.bridgedb.org/#latinName) or [short name](http://vocabularies.bridgedb.org/#shortName). | 
 **query** | **String**| Text to find in attributes | 
 **limit** | **Number**| Number of results | [optional] 
 **attrName** | **String**| Restrict search by attribute name (case sensitive). Use GET /{organism}/attributeSet to find out which attributes are supported. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## organismAttributeSetGet

> organismAttributeSetGet(organism)



Returns the supported attributes to the given Organism.

### Example

```javascript
import BridgedbWebservices from 'bridgedb_webservices';

let apiInstance = new BridgedbWebservices.IdentifiersGenesProteinsMetabolitesInteractionsApi();
let organism = "organism_example"; // String | Organism [Latin name](http://vocabularies.bridgedb.org/#latinName) or [short name](http://vocabularies.bridgedb.org/#shortName).
apiInstance.organismAttributeSetGet(organism, (error, data, response) => {
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
 **organism** | **String**| Organism [Latin name](http://vocabularies.bridgedb.org/#latinName) or [short name](http://vocabularies.bridgedb.org/#shortName). | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## organismAttributesSystemCodeIdentifierGet

> organismAttributesSystemCodeIdentifierGet(organism, systemCode, identifier, opts)



Returns the attributes for a given identifier, data source, organism. Optionally display only a specified attribute

### Example

```javascript
import BridgedbWebservices from 'bridgedb_webservices';

let apiInstance = new BridgedbWebservices.IdentifiersGenesProteinsMetabolitesInteractionsApi();
let organism = "organism_example"; // String | Organism [Latin name](http://vocabularies.bridgedb.org/#latinName) or [short name](http://vocabularies.bridgedb.org/#shortName).
let systemCode = "'En'"; // String | System
let identifier = "'ENSG00000122375'"; // String | Identifier
let opts = {
  'attrName': "attrName_example" // String | Type of attribute
};
apiInstance.organismAttributesSystemCodeIdentifierGet(organism, systemCode, identifier, opts, (error, data, response) => {
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
 **organism** | **String**| Organism [Latin name](http://vocabularies.bridgedb.org/#latinName) or [short name](http://vocabularies.bridgedb.org/#shortName). | 
 **systemCode** | **String**| System | [default to &#39;En&#39;]
 **identifier** | **String**| Identifier | [default to &#39;ENSG00000122375&#39;]
 **attrName** | **String**| Type of attribute | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## organismIsFreeSearchSupportedGet

> organismIsFreeSearchSupportedGet(organism)



Returns &#x60;true&#x60; or &#x60;false&#x60; based on whether or not /{organism}/search/{query} is supported for a given organism.

### Example

```javascript
import BridgedbWebservices from 'bridgedb_webservices';

let apiInstance = new BridgedbWebservices.IdentifiersGenesProteinsMetabolitesInteractionsApi();
let organism = "organism_example"; // String | Organism [Latin name](http://vocabularies.bridgedb.org/#latinName) or [short name](http://vocabularies.bridgedb.org/#shortName).
apiInstance.organismIsFreeSearchSupportedGet(organism, (error, data, response) => {
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
 **organism** | **String**| Organism [Latin name](http://vocabularies.bridgedb.org/#latinName) or [short name](http://vocabularies.bridgedb.org/#shortName). | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## organismIsMappingSupportedSourceSystemCodeTargetSystemCodeGet

> organismIsMappingSupportedSourceSystemCodeTargetSystemCodeGet(organism, sourceSystemCode, targetSystemCode)



Returns &#x60;true&#x60; or &#x60;false&#x60; based on whether or not /{organism}/xrefs/{systemCode}/{identifier} would possibly return a {targetSystemCode} result given a {sourceSystemCode} query. This function basically combines the results of /{organism}/sourceDataSources and /{organism}/targetDataSources into a single boolean result.

### Example

```javascript
import BridgedbWebservices from 'bridgedb_webservices';

let apiInstance = new BridgedbWebservices.IdentifiersGenesProteinsMetabolitesInteractionsApi();
let organism = "organism_example"; // String | Organism [Latin name](http://vocabularies.bridgedb.org/#latinName) or [short name](http://vocabularies.bridgedb.org/#shortName).
let sourceSystemCode = "'L'"; // String | [System code](http://vocabularies.bridgedb.org/#systemCode) for source (input/query) data source
let targetSystemCode = "targetSystemCode_example"; // String | [System code](http://vocabularies.bridgedb.org/#systemCode) for target (output/result) data source
apiInstance.organismIsMappingSupportedSourceSystemCodeTargetSystemCodeGet(organism, sourceSystemCode, targetSystemCode, (error, data, response) => {
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
 **organism** | **String**| Organism [Latin name](http://vocabularies.bridgedb.org/#latinName) or [short name](http://vocabularies.bridgedb.org/#shortName). | 
 **sourceSystemCode** | **String**| [System code](http://vocabularies.bridgedb.org/#systemCode) for source (input/query) data source | [default to &#39;L&#39;]
 **targetSystemCode** | **String**| [System code](http://vocabularies.bridgedb.org/#systemCode) for target (output/result) data source | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## organismPropertiesGet

> organismPropertiesGet(organism)



Returns the list of properties available for a given organism 

### Example

```javascript
import BridgedbWebservices from 'bridgedb_webservices';

let apiInstance = new BridgedbWebservices.IdentifiersGenesProteinsMetabolitesInteractionsApi();
let organism = "organism_example"; // String | Organism [Latin name](http://vocabularies.bridgedb.org/#latinName) or [short name](http://vocabularies.bridgedb.org/#shortName).
apiInstance.organismPropertiesGet(organism, (error, data, response) => {
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
 **organism** | **String**| Organism [Latin name](http://vocabularies.bridgedb.org/#latinName) or [short name](http://vocabularies.bridgedb.org/#shortName). | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## organismSearchQueryGet

> organismSearchQueryGet(organism, query, opts)



Returns a list of xrefs with identifiers that contain the query string for a given organism. Results are not restricted to exact matches. Optionally limit results to a specified number per data source.

### Example

```javascript
import BridgedbWebservices from 'bridgedb_webservices';

let apiInstance = new BridgedbWebservices.IdentifiersGenesProteinsMetabolitesInteractionsApi();
let organism = "organism_example"; // String | Organism [Latin name](http://vocabularies.bridgedb.org/#latinName) or [short name](http://vocabularies.bridgedb.org/#shortName).
let query = "'1234'"; // String | Identifier query
let opts = {
  'limit': 56 // Number | Number of results per data source
};
apiInstance.organismSearchQueryGet(organism, query, opts, (error, data, response) => {
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
 **organism** | **String**| Organism [Latin name](http://vocabularies.bridgedb.org/#latinName) or [short name](http://vocabularies.bridgedb.org/#shortName). | 
 **query** | **String**| Identifier query | [default to &#39;1234&#39;]
 **limit** | **Number**| Number of results per data source | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## organismSourceDataSourcesGet

> organismSourceDataSourcesGet(organism)



Returns a list of data sources available as xref sources for a given organism.

### Example

```javascript
import BridgedbWebservices from 'bridgedb_webservices';

let apiInstance = new BridgedbWebservices.IdentifiersGenesProteinsMetabolitesInteractionsApi();
let organism = "organism_example"; // String | Organism [Latin name](http://vocabularies.bridgedb.org/#latinName) or [short name](http://vocabularies.bridgedb.org/#shortName).
apiInstance.organismSourceDataSourcesGet(organism, (error, data, response) => {
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
 **organism** | **String**| Organism [Latin name](http://vocabularies.bridgedb.org/#latinName) or [short name](http://vocabularies.bridgedb.org/#shortName). | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## organismTargetDataSourcesGet

> organismTargetDataSourcesGet(organism)



Returns a list of data sources available as xref targets for a given organism.

### Example

```javascript
import BridgedbWebservices from 'bridgedb_webservices';

let apiInstance = new BridgedbWebservices.IdentifiersGenesProteinsMetabolitesInteractionsApi();
let organism = "organism_example"; // String | Organism [Latin name](http://vocabularies.bridgedb.org/#latinName) or [short name](http://vocabularies.bridgedb.org/#shortName).
apiInstance.organismTargetDataSourcesGet(organism, (error, data, response) => {
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
 **organism** | **String**| Organism [Latin name](http://vocabularies.bridgedb.org/#latinName) or [short name](http://vocabularies.bridgedb.org/#shortName). | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## organismXrefExistsSystemCodeIdentifierGet

> organismXrefExistsSystemCodeIdentifierGet(organism, systemCode, identifier)



Returns &#x60;true&#x60; or &#x60;false&#x60; based on whether or not an xref exists in the database given an identifier, data source, and organism.

### Example

```javascript
import BridgedbWebservices from 'bridgedb_webservices';

let apiInstance = new BridgedbWebservices.IdentifiersGenesProteinsMetabolitesInteractionsApi();
let organism = "organism_example"; // String | Organism [Latin name](http://vocabularies.bridgedb.org/#latinName) or [short name](http://vocabularies.bridgedb.org/#shortName).
let systemCode = "'L'"; // String | Source (input) data source [system code](https://bridgedb.github.io/pages/system-codes.html)
let identifier = "'1234'"; // String | Identifier
apiInstance.organismXrefExistsSystemCodeIdentifierGet(organism, systemCode, identifier, (error, data, response) => {
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
 **organism** | **String**| Organism [Latin name](http://vocabularies.bridgedb.org/#latinName) or [short name](http://vocabularies.bridgedb.org/#shortName). | 
 **systemCode** | **String**| Source (input) data source [system code](https://bridgedb.github.io/pages/system-codes.html) | [default to &#39;L&#39;]
 **identifier** | **String**| Identifier | [default to &#39;1234&#39;]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## organismXrefsBatchPost

> organismXrefsBatchPost(organism, body, opts)



Returns a list of xrefs, per identifier, that maps to a given list of identifiers an data source given an organism.

### Example

```javascript
import BridgedbWebservices from 'bridgedb_webservices';

let apiInstance = new BridgedbWebservices.IdentifiersGenesProteinsMetabolitesInteractionsApi();
let organism = "organism_example"; // String | Organism [Latin name](http://vocabularies.bridgedb.org/#latinName) or [short name](http://vocabularies.bridgedb.org/#shortName).
let body = "body_example"; // String | List of tab separated values: id<tab>systemcode\\n
let opts = {
  'dataSource': "dataSource_example" // String | (Optional) Restrict results by data source [system code](https://bridgedb.github.io/pages/system-codes.html)
};
apiInstance.organismXrefsBatchPost(organism, body, opts, (error, data, response) => {
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
 **organism** | **String**| Organism [Latin name](http://vocabularies.bridgedb.org/#latinName) or [short name](http://vocabularies.bridgedb.org/#shortName). | 
 **body** | **String**| List of tab separated values: id&lt;tab&gt;systemcode\\n | 
 **dataSource** | **String**| (Optional) Restrict results by data source [system code](https://bridgedb.github.io/pages/system-codes.html) | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: text/html
- **Accept**: Not defined


## organismXrefsBatchSystemCodePost

> organismXrefsBatchSystemCodePost(organism, systemCode, body, opts)



Returns a list of xrefs, that maps to a given list of identifiers to a given data source and organism.

### Example

```javascript
import BridgedbWebservices from 'bridgedb_webservices';

let apiInstance = new BridgedbWebservices.IdentifiersGenesProteinsMetabolitesInteractionsApi();
let organism = "organism_example"; // String | Organism [Latin name](http://vocabularies.bridgedb.org/#latinName) or [short name](http://vocabularies.bridgedb.org/#shortName).
let systemCode = "'L'"; // String | Source (input) data source [system code](http://vocabularies.bridgedb.org/#systemCode)
let body = "body_example"; // String | List of identifiers. The separator is a new line (\\n)
let opts = {
  'dataSource': "dataSource_example" // String | (Optional) Restrict results by data source [system code](https://bridgedb.github.io/pages/system-codes.html)
};
apiInstance.organismXrefsBatchSystemCodePost(organism, systemCode, body, opts, (error, data, response) => {
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
 **organism** | **String**| Organism [Latin name](http://vocabularies.bridgedb.org/#latinName) or [short name](http://vocabularies.bridgedb.org/#shortName). | 
 **systemCode** | **String**| Source (input) data source [system code](http://vocabularies.bridgedb.org/#systemCode) | [default to &#39;L&#39;]
 **body** | **String**| List of identifiers. The separator is a new line (\\n) | 
 **dataSource** | **String**| (Optional) Restrict results by data source [system code](https://bridgedb.github.io/pages/system-codes.html) | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: text/html
- **Accept**: Not defined


## organismXrefsSystemCodeIdentifierGet

> organismXrefsSystemCodeIdentifierGet(organism, systemCode, identifier, opts)



Returns a list of xrefs that map to a given identifier, data source, and organism.

### Example

```javascript
import BridgedbWebservices from 'bridgedb_webservices';

let apiInstance = new BridgedbWebservices.IdentifiersGenesProteinsMetabolitesInteractionsApi();
let organism = "organism_example"; // String | Organism [Latin name](http://vocabularies.bridgedb.org/#latinName) or [short name](http://vocabularies.bridgedb.org/#shortName).
let systemCode = "'L'"; // String | Source (input) data source [system code](https://bridgedb.github.io/pages/system-codes.html)
let identifier = "'1234'"; // String | Identifier
let opts = {
  'dataSource': "dataSource_example" // String | (Optional) Restrict results by data source [system code](https://bridgedb.github.io/pages/system-codes.html)
};
apiInstance.organismXrefsSystemCodeIdentifierGet(organism, systemCode, identifier, opts, (error, data, response) => {
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
 **organism** | **String**| Organism [Latin name](http://vocabularies.bridgedb.org/#latinName) or [short name](http://vocabularies.bridgedb.org/#shortName). | 
 **systemCode** | **String**| Source (input) data source [system code](https://bridgedb.github.io/pages/system-codes.html) | [default to &#39;L&#39;]
 **identifier** | **String**| Identifier | [default to &#39;1234&#39;]
 **dataSource** | **String**| (Optional) Restrict results by data source [system code](https://bridgedb.github.io/pages/system-codes.html) | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

