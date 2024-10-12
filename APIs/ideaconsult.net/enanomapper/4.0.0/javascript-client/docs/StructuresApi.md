# ENanoMapperDatabase.StructuresApi

All URIs are relative to *https://api.ideaconsult.net/enanomapper*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getSubstanceComposition**](StructuresApi.md#getSubstanceComposition) | **GET** /enm/{db}/substance/{uuid}/composition | Substance composition
[**getSubstanceStructures**](StructuresApi.md#getSubstanceStructures) | **GET** /enm/{db}/substance/{uuid}/structures | Get substance composition as a dataset
[**searchByIdentifier**](StructuresApi.md#searchByIdentifier) | **GET** /enm/{db}/query/compound/{term}/{representation} | Exact chemical structure search
[**searchBySimilarity**](StructuresApi.md#searchBySimilarity) | **GET** /enm/{db}/query/similarity | Exact similarity search
[**searchBySmarts**](StructuresApi.md#searchBySmarts) | **GET** /enm/{db}/query/smarts | Substructure search



## getSubstanceComposition

> SubstanceComposition getSubstanceComposition(db, uuid, opts)

Substance composition

Returns substance composition

### Example

```javascript
import ENanoMapperDatabase from 'e_nano_mapper_database';

let apiInstance = new ENanoMapperDatabase.StructuresApi();
let db = "'nanoreg1'"; // String | Database ID
let uuid = "uuid_example"; // String | Substance UUID
let opts = {
  'all': true, // Boolean | true (Show all compositions) false (do not show hidden compositions)
  'page': 0, // Number | Starting page
  'pagesize': 10 // Number | Page size
};
apiInstance.getSubstanceComposition(db, uuid, opts, (error, data, response) => {
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
 **db** | **String**| Database ID | [default to &#39;nanoreg1&#39;]
 **uuid** | **String**| Substance UUID | 
 **all** | **Boolean**| true (Show all compositions) false (do not show hidden compositions) | [optional] 
 **page** | **Number**| Starting page | [optional] 
 **pagesize** | **Number**| Page size | [optional] 

### Return type

[**SubstanceComposition**](SubstanceComposition.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSubstanceStructures

> Dataset getSubstanceStructures(db, uuid, opts)

Get substance composition as a dataset

Returns substance composition

### Example

```javascript
import ENanoMapperDatabase from 'e_nano_mapper_database';

let apiInstance = new ENanoMapperDatabase.StructuresApi();
let db = "'nanoreg1'"; // String | Database ID
let uuid = "uuid_example"; // String | Substance UUID
let opts = {
  'page': 0, // Number | Starting page
  'pagesize': 10 // Number | Page size
};
apiInstance.getSubstanceStructures(db, uuid, opts, (error, data, response) => {
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
 **db** | **String**| Database ID | [default to &#39;nanoreg1&#39;]
 **uuid** | **String**| Substance UUID | 
 **page** | **Number**| Starting page | [optional] 
 **pagesize** | **Number**| Page size | [optional] 

### Return type

[**Dataset**](Dataset.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## searchByIdentifier

> Dataset searchByIdentifier(db, term, representation, opts)

Exact chemical structure search

Returns compounds found

### Example

```javascript
import ENanoMapperDatabase from 'e_nano_mapper_database';

let apiInstance = new ENanoMapperDatabase.StructuresApi();
let db = "'nanoreg1'"; // String | Database ID
let term = "term_example"; // String | search term type
let representation = "representation_example"; // String | 
let opts = {
  'search': "search_example", // String | Compound identifier (SMILES, InChI, name, registry identifiers)
  'b64search': "b64search_example", // String | Base64 encoded mol file; if included, will be used instead of the 'search' parameter
  'casesens': true, // Boolean | Case sensitive search if yes
  'bundleUri': "bundleUri_example", // String | Bundle URI
  'sameas': "sameas_example", // String | Ontology URI to define groups of columns
  'page': 0, // Number | Starting page
  'pagesize': 10 // Number | Page size
};
apiInstance.searchByIdentifier(db, term, representation, opts, (error, data, response) => {
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
 **db** | **String**| Database ID | [default to &#39;nanoreg1&#39;]
 **term** | **String**| search term type | 
 **representation** | **String**|  | 
 **search** | **String**| Compound identifier (SMILES, InChI, name, registry identifiers) | [optional] 
 **b64search** | **String**| Base64 encoded mol file; if included, will be used instead of the &#39;search&#39; parameter | [optional] 
 **casesens** | **Boolean**| Case sensitive search if yes | [optional] 
 **bundleUri** | **String**| Bundle URI | [optional] 
 **sameas** | **String**| Ontology URI to define groups of columns | [optional] 
 **page** | **Number**| Starting page | [optional] 
 **pagesize** | **Number**| Page size | [optional] 

### Return type

[**Dataset**](Dataset.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## searchBySimilarity

> Dataset searchBySimilarity(db, opts)

Exact similarity search

Returns similar compounds

### Example

```javascript
import ENanoMapperDatabase from 'e_nano_mapper_database';

let apiInstance = new ENanoMapperDatabase.StructuresApi();
let db = "'nanoreg1'"; // String | Database ID
let opts = {
  'search': "search_example", // String | Compound identifier (SMILES, InChI, name, registry identifiers)
  'b64search': "b64search_example", // String | Base64 encoded mol file; if included, will be used instead of the 'search' parameter
  'type': "type_example", // String | Defines the expected content of the search parameter
  'threshold': 3.4, // Number | Similarity threshold
  'datasetUri': "datasetUri_example", // String | Restrict the search within the AMBIT dataset specified with the URI
  'filterBySubstance': true, // Boolean | Restrict the search within the set of structures with assigned substances
  'bundleUri': "bundleUri_example", // String | If the structure is used in the specified bundle URI, the selection tag will be returned
  'sameas': "sameas_example", // String | Ontology URI to define groups of columns
  'mol': true, // Boolean | Only for application/json; to include mol as JSON field
  'page': 0, // Number | Starting page
  'pagesize': 10 // Number | Page size
};
apiInstance.searchBySimilarity(db, opts, (error, data, response) => {
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
 **db** | **String**| Database ID | [default to &#39;nanoreg1&#39;]
 **search** | **String**| Compound identifier (SMILES, InChI, name, registry identifiers) | [optional] 
 **b64search** | **String**| Base64 encoded mol file; if included, will be used instead of the &#39;search&#39; parameter | [optional] 
 **type** | **String**| Defines the expected content of the search parameter | [optional] 
 **threshold** | **Number**| Similarity threshold | [optional] 
 **datasetUri** | **String**| Restrict the search within the AMBIT dataset specified with the URI | [optional] 
 **filterBySubstance** | **Boolean**| Restrict the search within the set of structures with assigned substances | [optional] 
 **bundleUri** | **String**| If the structure is used in the specified bundle URI, the selection tag will be returned | [optional] 
 **sameas** | **String**| Ontology URI to define groups of columns | [optional] 
 **mol** | **Boolean**| Only for application/json; to include mol as JSON field | [optional] 
 **page** | **Number**| Starting page | [optional] 
 **pagesize** | **Number**| Page size | [optional] 

### Return type

[**Dataset**](Dataset.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## searchBySmarts

> Dataset searchBySmarts(db, opts)

Substructure search

Returns compounds with the specified substructure

### Example

```javascript
import ENanoMapperDatabase from 'e_nano_mapper_database';

let apiInstance = new ENanoMapperDatabase.StructuresApi();
let db = "'nanoreg1'"; // String | Database ID
let opts = {
  'search': "search_example", // String | Compound identifier (SMILES, InChI, name, registry identifiers)
  'b64search': "b64search_example", // String | Base64 encoded mol file; if included, will be used instead of the 'search' parameter
  'type': "type_example", // String | Defines the expected content of the search parameter
  'datasetUri': "datasetUri_example", // String | Restrict the search within the AMBIT dataset specified with the URI
  'filterBySubstance': true, // Boolean | Restrict the search within the set of structures with assigned substances
  'bundleUri': "bundleUri_example", // String | If the structure is used in the specified bundle URI, the selection tag will be returned
  'sameas': "sameas_example", // String | Ontology URI to define groups of columns
  'mol': true, // Boolean | Only for application/json; to include mol as JSON field
  'page': 0, // Number | Starting page
  'pagesize': 10 // Number | Page size
};
apiInstance.searchBySmarts(db, opts, (error, data, response) => {
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
 **db** | **String**| Database ID | [default to &#39;nanoreg1&#39;]
 **search** | **String**| Compound identifier (SMILES, InChI, name, registry identifiers) | [optional] 
 **b64search** | **String**| Base64 encoded mol file; if included, will be used instead of the &#39;search&#39; parameter | [optional] 
 **type** | **String**| Defines the expected content of the search parameter | [optional] 
 **datasetUri** | **String**| Restrict the search within the AMBIT dataset specified with the URI | [optional] 
 **filterBySubstance** | **Boolean**| Restrict the search within the set of structures with assigned substances | [optional] 
 **bundleUri** | **String**| If the structure is used in the specified bundle URI, the selection tag will be returned | [optional] 
 **sameas** | **String**| Ontology URI to define groups of columns | [optional] 
 **mol** | **Boolean**| Only for application/json; to include mol as JSON field | [optional] 
 **page** | **Number**| Starting page | [optional] 
 **pagesize** | **Number**| Page size | [optional] 

### Return type

[**Dataset**](Dataset.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

