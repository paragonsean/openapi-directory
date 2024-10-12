# ENanoMapperDatabase.SubstancesApi

All URIs are relative to *https://api.ideaconsult.net/enanomapper*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getSubstanceByUUID**](SubstancesApi.md#getSubstanceByUUID) | **GET** /enm/{db}/substance/{uuid} | Get a substance
[**getSubstanceComposition_0**](SubstancesApi.md#getSubstanceComposition_0) | **GET** /enm/{db}/substance/{uuid}/composition | Substance composition
[**getSubstanceStructures_0**](SubstancesApi.md#getSubstanceStructures_0) | **GET** /enm/{db}/substance/{uuid}/structures | Get substance composition as a dataset
[**getSubstanceStudySummary_0**](SubstancesApi.md#getSubstanceStudySummary_0) | **GET** /enm/{db}/substance/{uuid}/studySummary | Get study summary for the substance
[**getSubstanceStudy_0**](SubstancesApi.md#getSubstanceStudy_0) | **GET** /enm/{db}/substance/{uuid}/study | get substance study
[**getSubstances**](SubstancesApi.md#getSubstances) | **GET** /enm/{db}/substance | List substances



## getSubstanceByUUID

> Substance getSubstanceByUUID(db, uuid, opts)

Get a substance

Returns substance representation

### Example

```javascript
import ENanoMapperDatabase from 'e_nano_mapper_database';

let apiInstance = new ENanoMapperDatabase.SubstancesApi();
let db = "'nanoreg1'"; // String | Database ID
let uuid = "uuid_example"; // String | Substance UUID
let opts = {
  'propertyUris': "propertyUris_example", // String | Property URIs
  'page': 0, // Number | Starting page
  'pagesize': 10 // Number | Page size
};
apiInstance.getSubstanceByUUID(db, uuid, opts, (error, data, response) => {
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
 **propertyUris** | **String**| Property URIs | [optional] 
 **page** | **Number**| Starting page | [optional] 
 **pagesize** | **Number**| Page size | [optional] 

### Return type

[**Substance**](Substance.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSubstanceComposition_0

> SubstanceComposition getSubstanceComposition_0(db, uuid, opts)

Substance composition

Returns substance composition

### Example

```javascript
import ENanoMapperDatabase from 'e_nano_mapper_database';

let apiInstance = new ENanoMapperDatabase.SubstancesApi();
let db = "'nanoreg1'"; // String | Database ID
let uuid = "uuid_example"; // String | Substance UUID
let opts = {
  'all': true, // Boolean | true (Show all compositions) false (do not show hidden compositions)
  'page': 0, // Number | Starting page
  'pagesize': 10 // Number | Page size
};
apiInstance.getSubstanceComposition_0(db, uuid, opts, (error, data, response) => {
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


## getSubstanceStructures_0

> Dataset getSubstanceStructures_0(db, uuid, opts)

Get substance composition as a dataset

Returns substance composition

### Example

```javascript
import ENanoMapperDatabase from 'e_nano_mapper_database';

let apiInstance = new ENanoMapperDatabase.SubstancesApi();
let db = "'nanoreg1'"; // String | Database ID
let uuid = "uuid_example"; // String | Substance UUID
let opts = {
  'page': 0, // Number | Starting page
  'pagesize': 10 // Number | Page size
};
apiInstance.getSubstanceStructures_0(db, uuid, opts, (error, data, response) => {
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


## getSubstanceStudySummary_0

> SubstanceStudySummary getSubstanceStudySummary_0(db, uuid, opts)

Get study summary for the substance

Study summary

### Example

```javascript
import ENanoMapperDatabase from 'e_nano_mapper_database';

let apiInstance = new ENanoMapperDatabase.SubstancesApi();
let db = "'nanoreg1'"; // String | Database ID
let uuid = "uuid_example"; // String | Substance UUID
let opts = {
  'top': "top_example", // String | Top endpoint category
  'category': "category_example", // String | Endpoint category (The value in the protocol.category.code field)
  'propertyUri': "propertyUri_example", // String | Property URI https://data.enanomapper.net/property/{UUID} , see Property service
  'property': "property_example", // String | Property UUID, see Property service
  'result': true, // Boolean | If true will group by topcategory,endpointcategory,interpretation result
  'page': 0, // Number | Starting page
  'pagesize': 10 // Number | Page size
};
apiInstance.getSubstanceStudySummary_0(db, uuid, opts, (error, data, response) => {
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
 **top** | **String**| Top endpoint category | [optional] 
 **category** | **String**| Endpoint category (The value in the protocol.category.code field) | [optional] 
 **propertyUri** | **String**| Property URI https://data.enanomapper.net/property/{UUID} , see Property service | [optional] 
 **property** | **String**| Property UUID, see Property service | [optional] 
 **result** | **Boolean**| If true will group by topcategory,endpointcategory,interpretation result | [optional] 
 **page** | **Number**| Starting page | [optional] 
 **pagesize** | **Number**| Page size | [optional] 

### Return type

[**SubstanceStudySummary**](SubstanceStudySummary.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSubstanceStudy_0

> SubstanceStudy getSubstanceStudy_0(db, uuid, opts)

get substance study

Returns substance study representation

### Example

```javascript
import ENanoMapperDatabase from 'e_nano_mapper_database';

let apiInstance = new ENanoMapperDatabase.SubstancesApi();
let db = "'nanoreg1'"; // String | Database ID
let uuid = "uuid_example"; // String | Substance UUID
let opts = {
  'top': "top_example", // String | Top endpoint category
  'category': "category_example", // String | Endpoint category (The value in the protocol.category.code field)
  'propertyUri': "propertyUri_example", // String | Property URI https://data.enanomapper.net/property/{UUID} , see Property service
  'property': "property_example", // String | Property UUID
  'investigationUuid': "investigationUuid_example", // String | Investigation UUID, a code to link different studies
  'page': 0, // Number | Starting page
  'pagesize': 10 // Number | Page size
};
apiInstance.getSubstanceStudy_0(db, uuid, opts, (error, data, response) => {
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
 **top** | **String**| Top endpoint category | [optional] 
 **category** | **String**| Endpoint category (The value in the protocol.category.code field) | [optional] 
 **propertyUri** | **String**| Property URI https://data.enanomapper.net/property/{UUID} , see Property service | [optional] 
 **property** | **String**| Property UUID | [optional] 
 **investigationUuid** | **String**| Investigation UUID, a code to link different studies | [optional] 
 **page** | **Number**| Starting page | [optional] 
 **pagesize** | **Number**| Page size | [optional] 

### Return type

[**SubstanceStudy**](SubstanceStudy.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSubstances

> Substance getSubstances(db, opts)

List substances

Returns a list of substances, according to the search criteria

### Example

```javascript
import ENanoMapperDatabase from 'e_nano_mapper_database';

let apiInstance = new ENanoMapperDatabase.SubstancesApi();
let db = "'nanoreg1'"; // String | Database ID
let opts = {
  'search': "search_example", // String | Search parameter
  'type': "type_example", // String | 
  'compoundUri': "compoundUri_example", // String | If type=related finds all substances containing this compound; if typ =reference - finds all substances with this compound as reference structure
  'bundleUri': "bundleUri_example", // String | Retrieves if selected in this bundle
  'addDummySubstance': true, // Boolean | Adds a compound record as substance in JSON; only if type=related
  'studysummary': true, // Boolean | If true retrieves study summary for each substance
  'page': 0, // Number | Starting page
  'pagesize': 10 // Number | Page size
};
apiInstance.getSubstances(db, opts, (error, data, response) => {
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
 **search** | **String**| Search parameter | [optional] 
 **type** | **String**|  | [optional] 
 **compoundUri** | **String**| If type&#x3D;related finds all substances containing this compound; if typ &#x3D;reference - finds all substances with this compound as reference structure | [optional] 
 **bundleUri** | **String**| Retrieves if selected in this bundle | [optional] 
 **addDummySubstance** | **Boolean**| Adds a compound record as substance in JSON; only if type&#x3D;related | [optional] 
 **studysummary** | **Boolean**| If true retrieves study summary for each substance | [optional] 
 **page** | **Number**| Starting page | [optional] 
 **pagesize** | **Number**| Page size | [optional] 

### Return type

[**Substance**](Substance.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

