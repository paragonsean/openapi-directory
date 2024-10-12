# ENanoMapperDatabase.StudiesApi

All URIs are relative to *https://api.ideaconsult.net/enanomapper*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getEndpointSummary**](StudiesApi.md#getEndpointSummary) | **GET** /enm/{db}/query/study | Search endpoint summary
[**getInvestigationResults**](StudiesApi.md#getInvestigationResults) | **GET** /enm/{db}/investigation | Details of multiple studies
[**getSubstanceStudy**](StudiesApi.md#getSubstanceStudy) | **GET** /enm/{db}/substance/{uuid}/study | get substance study
[**getSubstanceStudySummary**](StudiesApi.md#getSubstanceStudySummary) | **GET** /enm/{db}/substance/{uuid}/studySummary | Get study summary for the substance



## getEndpointSummary

> Facet getEndpointSummary(db, opts)

Search endpoint summary

Returns endpoint summary

### Example

```javascript
import ENanoMapperDatabase from 'e_nano_mapper_database';

let apiInstance = new ENanoMapperDatabase.StudiesApi();
let db = "'nanoreg1'"; // String | Database ID
let opts = {
  'top': "top_example", // String | Top endpoint category
  'category': "category_example" // String | Endpoint category (The value in the protocol.category.code field)
};
apiInstance.getEndpointSummary(db, opts, (error, data, response) => {
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
 **top** | **String**| Top endpoint category | [optional] 
 **category** | **String**| Endpoint category (The value in the protocol.category.code field) | [optional] 

### Return type

[**Facet**](Facet.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getInvestigationResults

> Investigation getInvestigationResults(db, type, search, opts)

Details of multiple studies

Multiple studies in tabular form

### Example

```javascript
import ENanoMapperDatabase from 'e_nano_mapper_database';

let apiInstance = new ENanoMapperDatabase.StudiesApi();
let db = "'nanoreg1'"; // String | Database ID
let type = "bystudytype"; // String | query type
let search = "PC_GRANULOMETRY_SECTION"; // String | Search parameter, UUID of the investigation or a substance
let opts = {
  'inchikey': "YUYCVXFAYWRXLS-UHFFFAOYSA-N", // String | Search parameter, InChI key(s) of the substance component(s), comma delimited
  'id': "id_example", // String | Search parameter, chemical structure or substance identifier(s), comma delimited
  'page': 0, // Number | Starting page
  'pagesize': 10 // Number | Page size
};
apiInstance.getInvestigationResults(db, type, search, opts, (error, data, response) => {
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
 **type** | **String**| query type | 
 **search** | **String**| Search parameter, UUID of the investigation or a substance | 
 **inchikey** | **String**| Search parameter, InChI key(s) of the substance component(s), comma delimited | [optional] 
 **id** | **String**| Search parameter, chemical structure or substance identifier(s), comma delimited | [optional] 
 **page** | **Number**| Starting page | [optional] 
 **pagesize** | **Number**| Page size | [optional] 

### Return type

[**Investigation**](Investigation.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet, application/x-javascript, text/csv, text/plain


## getSubstanceStudy

> SubstanceStudy getSubstanceStudy(db, uuid, opts)

get substance study

Returns substance study representation

### Example

```javascript
import ENanoMapperDatabase from 'e_nano_mapper_database';

let apiInstance = new ENanoMapperDatabase.StudiesApi();
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
apiInstance.getSubstanceStudy(db, uuid, opts, (error, data, response) => {
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


## getSubstanceStudySummary

> SubstanceStudySummary getSubstanceStudySummary(db, uuid, opts)

Get study summary for the substance

Study summary

### Example

```javascript
import ENanoMapperDatabase from 'e_nano_mapper_database';

let apiInstance = new ENanoMapperDatabase.StudiesApi();
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
apiInstance.getSubstanceStudySummary(db, uuid, opts, (error, data, response) => {
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

