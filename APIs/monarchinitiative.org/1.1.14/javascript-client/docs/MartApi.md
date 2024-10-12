# BioLinkApi.MartApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getMartCaseAssociationsResource**](MartApi.md#getMartCaseAssociationsResource) | **GET** /mart/case/{object_category}/{taxon} | Bulk download of case associations
[**getMartDiseaseAssociationsResource**](MartApi.md#getMartDiseaseAssociationsResource) | **GET** /mart/disease/{object_category}/{taxon} | Bulk download of disease associations
[**getMartGeneAssociationsResource**](MartApi.md#getMartGeneAssociationsResource) | **GET** /mart/gene/{object_category}/{taxon} | Bulk download of gene associations
[**getMartOrthologAssociationsResource**](MartApi.md#getMartOrthologAssociationsResource) | **GET** /mart/ortholog/{taxon1}/{taxon2} | Bulk download of orthologs
[**getMartParalogAssociationsResource**](MartApi.md#getMartParalogAssociationsResource) | **GET** /mart/paralog/{taxon1}/{taxon2} | Bulk download of paralogs



## getMartCaseAssociationsResource

> getMartCaseAssociationsResource(taxon, objectCategory, opts)

Bulk download of case associations

NOTE: this route has a limiter on it, you may be restricted in the number of downloads per hour. Use carefully.

### Example

```javascript
import BioLinkApi from 'bio_link_api';

let apiInstance = new BioLinkApi.MartApi();
let taxon = "taxon_example"; // String | taxon of case, must be of form NCBITaxon:9606
let objectCategory = "objectCategory_example"; // String | Category of entity at link Subject (target), e.g. phenotype, disease
let opts = {
  'slim': ["null"] // [String] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
};
apiInstance.getMartCaseAssociationsResource(taxon, objectCategory, opts, (error, data, response) => {
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
 **taxon** | **String**| taxon of case, must be of form NCBITaxon:9606 | 
 **objectCategory** | **String**| Category of entity at link Subject (target), e.g. phenotype, disease | 
 **slim** | [**[String]**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getMartDiseaseAssociationsResource

> getMartDiseaseAssociationsResource(taxon, objectCategory, opts)

Bulk download of disease associations

NOTE: this route has a limiter on it, you may be restricted in the number of downloads per hour. Use carefully.

### Example

```javascript
import BioLinkApi from 'bio_link_api';

let apiInstance = new BioLinkApi.MartApi();
let taxon = "taxon_example"; // String | taxon of disease, must be of form NCBITaxon:9606
let objectCategory = "objectCategory_example"; // String | Category of entity at link Object (target), e.g. phenotype, disease
let opts = {
  'slim': ["null"] // [String] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
};
apiInstance.getMartDiseaseAssociationsResource(taxon, objectCategory, opts, (error, data, response) => {
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
 **taxon** | **String**| taxon of disease, must be of form NCBITaxon:9606 | 
 **objectCategory** | **String**| Category of entity at link Object (target), e.g. phenotype, disease | 
 **slim** | [**[String]**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getMartGeneAssociationsResource

> getMartGeneAssociationsResource(taxon, objectCategory, opts)

Bulk download of gene associations

NOTE: this route has a limiter on it, you may be restricted in the number of downloads per hour. Use carefully.

### Example

```javascript
import BioLinkApi from 'bio_link_api';

let apiInstance = new BioLinkApi.MartApi();
let taxon = "taxon_example"; // String | taxon of gene, must be of form NCBITaxon:9606
let objectCategory = "objectCategory_example"; // String | Category of entity at link Object (target), e.g. phenotype, disease
let opts = {
  'slim': ["null"] // [String] | Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID
};
apiInstance.getMartGeneAssociationsResource(taxon, objectCategory, opts, (error, data, response) => {
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
 **taxon** | **String**| taxon of gene, must be of form NCBITaxon:9606 | 
 **objectCategory** | **String**| Category of entity at link Object (target), e.g. phenotype, disease | 
 **slim** | [**[String]**](String.md)| Map objects up (slim) to a higher level category. Value can be ontology class ID or subset ID | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getMartOrthologAssociationsResource

> getMartOrthologAssociationsResource(taxon2, taxon1)

Bulk download of orthologs

### Example

```javascript
import BioLinkApi from 'bio_link_api';

let apiInstance = new BioLinkApi.MartApi();
let taxon2 = "taxon2_example"; // String | object taxon, e.g. NCBITaxon:10090
let taxon1 = "taxon1_example"; // String | subject taxon, e.g. NCBITaxon:9606
apiInstance.getMartOrthologAssociationsResource(taxon2, taxon1, (error, data, response) => {
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
 **taxon2** | **String**| object taxon, e.g. NCBITaxon:10090 | 
 **taxon1** | **String**| subject taxon, e.g. NCBITaxon:9606 | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getMartParalogAssociationsResource

> getMartParalogAssociationsResource(taxon2, taxon1)

Bulk download of paralogs

### Example

```javascript
import BioLinkApi from 'bio_link_api';

let apiInstance = new BioLinkApi.MartApi();
let taxon2 = "taxon2_example"; // String | object taxon, e.g. NCBITaxon:9606
let taxon1 = "taxon1_example"; // String | subject taxon, e.g. NCBITaxon:9606
apiInstance.getMartParalogAssociationsResource(taxon2, taxon1, (error, data, response) => {
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
 **taxon2** | **String**| object taxon, e.g. NCBITaxon:9606 | 
 **taxon1** | **String**| subject taxon, e.g. NCBITaxon:9606 | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

