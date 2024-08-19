# FireBrowseBetaApi.SamplesApi

All URIs are relative to *http://firebrowse.org/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**clinical**](SamplesApi.md#clinical) | **GET** /Samples/Clinical | Retrieve TCGA CDEs verbatim, i.e. not normalized by Firehose.
[**clinicalFH**](SamplesApi.md#clinicalFH) | **GET** /Samples/Clinical_FH | Retrieve CDEs normalized by Firehose and selected for analyses.
[**mRNASeq**](SamplesApi.md#mRNASeq) | **GET** /Samples/mRNASeq | Retrieve mRNASeq data.
[**miRSeq**](SamplesApi.md#miRSeq) | **GET** /Samples/miRSeq | Retrieve miRSeq data.



## clinical

> clinical(opts)

Retrieve TCGA CDEs verbatim, i.e. not normalized by Firehose.

This service returns patient clinical data from TCGA, verbatim. It differs from the Samples/Clinical_FH method by providing access to all TCGA CDEs in their original form, not merely the subset of CDEs normalized by Firehose for analyses.  Results may be selected by disease cohort, patient barcode or CDE name, but at least one cohort, barcode, or CDE must be provided. When filtering by CDE note that only when a patient record contains one or more of the selected CDEs will it be returned. Visit the Metadata/ClinicalNames api function to see the entire list of TCGA CDEs that may be queried via this method. For more information on how clinical data are processed, see our &lt;a href&#x3D;\&quot;https://confluence.broadinstitute.org/display/GDAC/Documentation#Documentation-ClinicalPipeline\&quot;&gt;pipeline documentation&lt;/a&gt;.

### Example

```javascript
import FireBrowseBetaApi from 'fire_browse_beta_api';

let apiInstance = new FireBrowseBetaApi.SamplesApi();
let opts = {
  'format': "'json'", // String | Format of result.
  'cohort': ["null"], // [String] | Narrow search to one or more TCGA disease cohorts from the scrollable list.
  'tcgaParticipantBarcode': ["null"], // [String] | Comma separated list of TCGA participant barcodes (e.g. TCGA-GF-A4EO).
  'cdeName': ["null"], // [String] | Retrieve results only for specified CDEs, per the Metadata/ClinicalNames function
  'page': [1], // [Number] | Which page (slice) of entire results set should be returned. 
  'pageSize': [150], // [Number] | Number of records per page of results.  Max is 2000.
  'sortBy': "'cohort'" // String | Which column in the results should be used for sorting paginated results?
};
apiInstance.clinical(opts, (error, data, response) => {
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
 **format** | **String**| Format of result. | [optional] [default to &#39;json&#39;]
 **cohort** | [**[String]**](String.md)| Narrow search to one or more TCGA disease cohorts from the scrollable list. | [optional] 
 **tcgaParticipantBarcode** | [**[String]**](String.md)| Comma separated list of TCGA participant barcodes (e.g. TCGA-GF-A4EO). | [optional] 
 **cdeName** | [**[String]**](String.md)| Retrieve results only for specified CDEs, per the Metadata/ClinicalNames function | [optional] 
 **page** | [**[Number]**](Number.md)| Which page (slice) of entire results set should be returned.  | [optional] 
 **pageSize** | [**[Number]**](Number.md)| Number of records per page of results.  Max is 2000. | [optional] 
 **sortBy** | **String**| Which column in the results should be used for sorting paginated results? | [optional] [default to &#39;cohort&#39;]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## clinicalFH

> clinicalFH(opts)

Retrieve CDEs normalized by Firehose and selected for analyses.

This service returns patient-level clinical data elements (CDEs) that have been normalized by Firehose for use in analyses. Results may be selected by disease cohort, patient barcode or CDE name, but at least one cohort, barcode or CDE must be provided. When filtering by CDE note that only when a  patient record contains one or more of the selected CDEs will it be returned. Visit &lt;a href&#x3D;\&quot;http://gdac.broadinstitute.org/runs/info/clinical\&quot;&gt;this table of CDEs&lt;/a&gt; to see what&#39;s available for every disase cohort; for more information on how these CDEs are processed see our &lt;a href&#x3D;\&quot;https://confluence.broadinstitute.org/display/GDAC/Documentation#Documentation-ClinicalPipeline\&quot;&gt;pipeline documentation&lt;/a&gt;.

### Example

```javascript
import FireBrowseBetaApi from 'fire_browse_beta_api';

let apiInstance = new FireBrowseBetaApi.SamplesApi();
let opts = {
  'format': "'json'", // String | Format of result.
  'cohort': ["null"], // [String] | Narrow search to one or more TCGA disease cohorts from the scrollable list.
  'tcgaParticipantBarcode': ["null"], // [String] | Comma separated list of TCGA participant barcodes (e.g. TCGA-GF-A4EO).
  'fhCdeName': ["null"], // [String] | Retrieve results only for the CDEs specified from the scrollable list.
  'page': [1], // [Number] | Which page (slice) of entire results set should be returned. 
  'pageSize': [250], // [Number] | Number of records per page of results.  Max is 2000.
  'sortBy': "'cohort'" // String | Which column in the results should be used for sorting paginated results?
};
apiInstance.clinicalFH(opts, (error, data, response) => {
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
 **format** | **String**| Format of result. | [optional] [default to &#39;json&#39;]
 **cohort** | [**[String]**](String.md)| Narrow search to one or more TCGA disease cohorts from the scrollable list. | [optional] 
 **tcgaParticipantBarcode** | [**[String]**](String.md)| Comma separated list of TCGA participant barcodes (e.g. TCGA-GF-A4EO). | [optional] 
 **fhCdeName** | [**[String]**](String.md)| Retrieve results only for the CDEs specified from the scrollable list. | [optional] 
 **page** | [**[Number]**](Number.md)| Which page (slice) of entire results set should be returned.  | [optional] 
 **pageSize** | [**[Number]**](Number.md)| Number of records per page of results.  Max is 2000. | [optional] 
 **sortBy** | **String**| Which column in the results should be used for sorting paginated results? | [optional] [default to &#39;cohort&#39;]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## mRNASeq

> mRNASeq(opts)

Retrieve mRNASeq data.

This service returns sample-level log2 mRNASeq expression values. Results may be filtered by gene, cohort, barcode, sample type or characterization protocol, but at least one gene must be supplied.

### Example

```javascript
import FireBrowseBetaApi from 'fire_browse_beta_api';

let apiInstance = new FireBrowseBetaApi.SamplesApi();
let opts = {
  'format': "'json'", // String | Format of result.
  'gene': ["null"], // [String] | Comma separated list of gene name(s).
  'cohort': ["null"], // [String] | Narrow search to one or more TCGA disease cohorts from the scrollable list.
  'tcgaParticipantBarcode': ["null"], // [String] | Comma separated list of TCGA participant barcodes (e.g. TCGA-GF-A4EO).
  'sampleType': ["null"], // [String] | Narrow search to one or more TCGA sample types from the scrollable list.
  'protocol': ["'RSEM'"], // [String] | Narrow search to one or more sample characterization protocols from the scrollable list.
  'page': [1], // [Number] | Which page (slice) of entire results set should be returned. 
  'pageSize': [250], // [Number] | Number of records per page of results.  Max is 2000.
  'sortBy': "'cohort'" // String | Which column in the results should be used for sorting paginated results?
};
apiInstance.mRNASeq(opts, (error, data, response) => {
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
 **format** | **String**| Format of result. | [optional] [default to &#39;json&#39;]
 **gene** | [**[String]**](String.md)| Comma separated list of gene name(s). | [optional] 
 **cohort** | [**[String]**](String.md)| Narrow search to one or more TCGA disease cohorts from the scrollable list. | [optional] 
 **tcgaParticipantBarcode** | [**[String]**](String.md)| Comma separated list of TCGA participant barcodes (e.g. TCGA-GF-A4EO). | [optional] 
 **sampleType** | [**[String]**](String.md)| Narrow search to one or more TCGA sample types from the scrollable list. | [optional] 
 **protocol** | [**[String]**](String.md)| Narrow search to one or more sample characterization protocols from the scrollable list. | [optional] 
 **page** | [**[Number]**](Number.md)| Which page (slice) of entire results set should be returned.  | [optional] 
 **pageSize** | [**[Number]**](Number.md)| Number of records per page of results.  Max is 2000. | [optional] 
 **sortBy** | **String**| Which column in the results should be used for sorting paginated results? | [optional] [default to &#39;cohort&#39;]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## miRSeq

> miRSeq(opts)

Retrieve miRSeq data.

This service returns sample-level log2 miRSeq expression values. Results may be filtered by miR, cohort, barcode, sample type or Firehose preprocessing tool, but at least one miR must be supplied.

### Example

```javascript
import FireBrowseBetaApi from 'fire_browse_beta_api';

let apiInstance = new FireBrowseBetaApi.SamplesApi();
let opts = {
  'format': "'json'", // String | Format of result.
  'mir': ["null"], // [String] | Comma separated list of miR names (e.g. hsa-let-7b-5p,hsa-let-7a-1).
  'cohort': ["null"], // [String] | Narrow search to one or more TCGA disease cohorts from the scrollable list.
  'tcgaParticipantBarcode': ["null"], // [String] | Comma separated list of TCGA participant barcodes (e.g. TCGA-GF-A4EO).
  'tool': ["'miRseq_Mature_Preprocess'"], // [String] | Narrow search to include only data/results produced by the selected Firehose tool.
  'sampleType': ["null"], // [String] | Narrow search to one or more TCGA sample types from the scrollable list.
  'page': [1], // [Number] | Which page (slice) of entire results set should be returned. 
  'pageSize': [250], // [Number] | Number of records per page of results.  Max is 2000.
  'sortBy': "'cohort'" // String | Which column in the results should be used for sorting paginated results?
};
apiInstance.miRSeq(opts, (error, data, response) => {
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
 **format** | **String**| Format of result. | [optional] [default to &#39;json&#39;]
 **mir** | [**[String]**](String.md)| Comma separated list of miR names (e.g. hsa-let-7b-5p,hsa-let-7a-1). | [optional] 
 **cohort** | [**[String]**](String.md)| Narrow search to one or more TCGA disease cohorts from the scrollable list. | [optional] 
 **tcgaParticipantBarcode** | [**[String]**](String.md)| Comma separated list of TCGA participant barcodes (e.g. TCGA-GF-A4EO). | [optional] 
 **tool** | [**[String]**](String.md)| Narrow search to include only data/results produced by the selected Firehose tool. | [optional] 
 **sampleType** | [**[String]**](String.md)| Narrow search to one or more TCGA sample types from the scrollable list. | [optional] 
 **page** | [**[Number]**](Number.md)| Which page (slice) of entire results set should be returned.  | [optional] 
 **pageSize** | [**[Number]**](Number.md)| Number of records per page of results.  Max is 2000. | [optional] 
 **sortBy** | **String**| Which column in the results should be used for sorting paginated results? | [optional] [default to &#39;cohort&#39;]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

