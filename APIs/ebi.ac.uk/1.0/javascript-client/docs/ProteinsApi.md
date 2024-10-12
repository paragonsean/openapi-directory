# CrOssBarDataApi.ProteinsApi

All URIs are relative to *http://www.ebi.ac.uk/Tools/crossbar*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getProteinsUsingGET**](ProteinsApi.md#getProteinsUsingGET) | **GET** /proteins | Proteins collected from Uniprot for selective tax ids  HUMAN(9606), MOUSE(10090), RAT(10116), BOVINE(9913), ESCHERICHIA_COLI(83333), SUS_SCROFA(9823), MYCOBACTERIUM_TUBERCULOSIS(83332), ORYCTOLAGUS_CUNICULUS(9986), SACCHAROMYCES_CEREVISIAE(559292), CVHSA(694009) &amp; SARS2(2697049)



## getProteinsUsingGET

> Proteins getProteinsUsingGET(opts)

Proteins collected from Uniprot for selective tax ids  HUMAN(9606), MOUSE(10090), RAT(10116), BOVINE(9913), ESCHERICHIA_COLI(83333), SUS_SCROFA(9823), MYCOBACTERIUM_TUBERCULOSIS(83332), ORYCTOLAGUS_CUNICULUS(9986), SACCHAROMYCES_CEREVISIAE(559292), CVHSA(694009) &amp; SARS2(2697049)

### Example

```javascript
import CrOssBarDataApi from 'cr_oss_bar_data_api';

let apiInstance = new CrOssBarDataApi.ProteinsApi();
let opts = {
  'accession': ["null"], // [String] | accession
  'ec': ["null"], // [String] | ec
  'fullName': ["null"], // [String] | fullName
  'gene': ["null"], // [String] | gene
  'go': ["null"], // [String] | go
  'interpro': ["null"], // [String] | interpro
  'limit': 10, // Number | limit
  'omim': ["null"], // [String] | omim
  'orphanet': ["null"], // [String] | orphanet
  'page': 0, // Number | page
  'pfam': ["null"], // [String] | pfam
  'reactome': ["null"], // [String] | reactome
  'taxId': [null] // [Number] | taxId
};
apiInstance.getProteinsUsingGET(opts, (error, data, response) => {
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
 **accession** | [**[String]**](String.md)| accession | [optional] 
 **ec** | [**[String]**](String.md)| ec | [optional] 
 **fullName** | [**[String]**](String.md)| fullName | [optional] 
 **gene** | [**[String]**](String.md)| gene | [optional] 
 **go** | [**[String]**](String.md)| go | [optional] 
 **interpro** | [**[String]**](String.md)| interpro | [optional] 
 **limit** | **Number**| limit | [optional] [default to 10]
 **omim** | [**[String]**](String.md)| omim | [optional] 
 **orphanet** | [**[String]**](String.md)| orphanet | [optional] 
 **page** | **Number**| page | [optional] [default to 0]
 **pfam** | [**[String]**](String.md)| pfam | [optional] 
 **reactome** | [**[String]**](String.md)| reactome | [optional] 
 **taxId** | [**[Number]**](Number.md)| taxId | [optional] 

### Return type

[**Proteins**](Proteins.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

