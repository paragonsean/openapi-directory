# FireBrowseBetaApi.AnalysesApi

All URIs are relative to *http://firebrowse.org/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**all**](AnalysesApi.md#all) | **GET** /Analyses/CopyNumber/Genes/All | Retrieve all data by genes Gistic2 results.
[**amplified**](AnalysesApi.md#amplified) | **GET** /Analyses/CopyNumber/Genes/Amplified | Retrieve Gistic2 significantly amplified genes results.
[**deleted**](AnalysesApi.md#deleted) | **GET** /Analyses/CopyNumber/Genes/Deleted | Retrieve Gistic2 significantly deleted genes results.
[**featureTable**](AnalysesApi.md#featureTable) | **GET** /Analyses/FeatureTable | Retrieve aggregated analysis features table.
[**focal**](AnalysesApi.md#focal) | **GET** /Analyses/CopyNumber/Genes/Focal | Retrieve focal data by genes Gistic2 results.
[**mAF**](AnalysesApi.md#mAF) | **GET** /Analyses/Mutation/MAF | Retrieve MutSig final analysis MAF.
[**mRNASeqQuartiles**](AnalysesApi.md#mRNASeqQuartiles) | **GET** /Analyses/mRNASeq/Quartiles | Returns RNASeq expression quartiles, e.g. suitable for drawing a boxplot.
[**reports**](AnalysesApi.md#reports) | **GET** /Analyses/Reports | Retrieve links to summary reports from Firehose analysis runs.
[**sMG**](AnalysesApi.md#sMG) | **GET** /Analyses/Mutation/SMG | Retrieve Significantly Mutated Genes (SMG).
[**thresholded**](AnalysesApi.md#thresholded) | **GET** /Analyses/CopyNumber/Genes/Thresholded | Retrieve all thresholded by genes Gistic2 results.



## all

> all(opts)

Retrieve all data by genes Gistic2 results.

This service provides access to the Gistic2 all_data_by_genes.txt output data. This data is a gene-level table of copy number values for all samples. The returned copy number values are in units (copy number - 2) so that no amplification or deletion is 0, genes with amplifications have positive values, and genes with deletions are negative values. The data are converted from marker level to gene level using the extreme method: a gene is assigned the greatest amplification or the least deletion value among the markers it covers. Results may be filtered by cohort, gene, or barcode, but at least one gene or barcode must be supplied.

### Example

```javascript
import FireBrowseBetaApi from 'fire_browse_beta_api';

let apiInstance = new FireBrowseBetaApi.AnalysesApi();
let opts = {
  'format': "'json'", // String | Format of result.
  'cohort': ["null"], // [String] | Narrow search to one or more TCGA disease cohorts from the scrollable list.
  'gene': ["null"], // [String] | Comma separated list of gene name(s).
  'tcgaParticipantBarcode': ["null"], // [String] | Comma separated list of TCGA participant barcodes (e.g. TCGA-GF-A4EO).
  'page': [1], // [Number] | Which page (slice) of entire results set should be returned. 
  'pageSize': [250], // [Number] | Number of records per page of results.  Max is 2000.
  'sortBy': "'cohort'" // String | Which column in the results should be used for sorting paginated results?
};
apiInstance.all(opts, (error, data, response) => {
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
 **gene** | [**[String]**](String.md)| Comma separated list of gene name(s). | [optional] 
 **tcgaParticipantBarcode** | [**[String]**](String.md)| Comma separated list of TCGA participant barcodes (e.g. TCGA-GF-A4EO). | [optional] 
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


## amplified

> amplified(opts)

Retrieve Gistic2 significantly amplified genes results.

This service provides access to the Gistic2 amp_genes.conf_99.txt output data.  At least 1 gene or cohort must be supplied.

### Example

```javascript
import FireBrowseBetaApi from 'fire_browse_beta_api';

let apiInstance = new FireBrowseBetaApi.AnalysesApi();
let opts = {
  'format': "'json'", // String | Format of result.
  'cohort': ["null"], // [String] | Narrow search to one or more TCGA disease cohorts from the scrollable list.
  'gene': ["null"], // [String] | Comma separated list of gene name(s).
  'q': 3.4, // Number | Only return results with Q-value <= given threshold.
  'page': [1], // [Number] | Which page (slice) of entire results set should be returned. 
  'pageSize': [250], // [Number] | Number of records per page of results.  Max is 2000.
  'sortBy': "'cohort'" // String | Which column in the results should be used for sorting paginated results?
};
apiInstance.amplified(opts, (error, data, response) => {
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
 **gene** | [**[String]**](String.md)| Comma separated list of gene name(s). | [optional] 
 **q** | **Number**| Only return results with Q-value &lt;&#x3D; given threshold. | [optional] 
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


## deleted

> deleted(opts)

Retrieve Gistic2 significantly deleted genes results.

This service provides access to the Gistic2 del_genes.conf_99.txt output data.  At least 1 gene or cohort must be supplied.

### Example

```javascript
import FireBrowseBetaApi from 'fire_browse_beta_api';

let apiInstance = new FireBrowseBetaApi.AnalysesApi();
let opts = {
  'format': "'json'", // String | Format of result.
  'cohort': ["null"], // [String] | Narrow search to one or more TCGA disease cohorts from the scrollable list.
  'gene': ["null"], // [String] | Comma separated list of gene name(s).
  'q': 3.4, // Number | Only return results with Q-value <= given threshold.
  'page': [1], // [Number] | Which page (slice) of entire results set should be returned. 
  'pageSize': [250], // [Number] | Number of records per page of results.  Max is 2000.
  'sortBy': "'cohort'" // String | Which column in the results should be used for sorting paginated results?
};
apiInstance.deleted(opts, (error, data, response) => {
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
 **gene** | [**[String]**](String.md)| Comma separated list of gene name(s). | [optional] 
 **q** | **Number**| Only return results with Q-value &lt;&#x3D; given threshold. | [optional] 
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


## featureTable

> featureTable(opts)

Retrieve aggregated analysis features table.

This service returns part or all of the so-called &lt;strong&gt;feature table&lt;/strong&gt;; which aggregates the most important findings across ALL pipelines in the GDAC Firehose analysis workflow into a single table for simple access.  One feature table is created per disease cohort.  Results may be filtered by date or cohort, but at least 1 cohort must be specified here. For more details please visit the &lt;a href&#x3D;https://confluence.broadinstitute.org/display/GDAC/Documentation\\#Documentation-FeatureTable&gt;online documentation&lt;/a&gt;.  Please note that the service is still undergoing experimental evaluation and does not return JSON format.

### Example

```javascript
import FireBrowseBetaApi from 'fire_browse_beta_api';

let apiInstance = new FireBrowseBetaApi.AnalysesApi();
let opts = {
  'format': "'tsv'", // String | Format of result.
  'cohort': ["null"], // [String] | Narrow search to one or more TCGA disease cohorts from the scrollable list.
  'date': [new Date("null")], // [Date] | Select one or more date stamps.
  'column': ["null"], // [String] | Comma separated list of which data columns/fields to return.
  'page': [1], // [Number] | Which page (slice) of entire results set should be returned. 
  'pageSize': [250] // [Number] | Number of records per page of results.  Max is 2000.
};
apiInstance.featureTable(opts, (error, data, response) => {
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
 **format** | **String**| Format of result. | [optional] [default to &#39;tsv&#39;]
 **cohort** | [**[String]**](String.md)| Narrow search to one or more TCGA disease cohorts from the scrollable list. | [optional] 
 **date** | [**[Date]**](Date.md)| Select one or more date stamps. | [optional] 
 **column** | [**[String]**](String.md)| Comma separated list of which data columns/fields to return. | [optional] 
 **page** | [**[Number]**](Number.md)| Which page (slice) of entire results set should be returned.  | [optional] 
 **pageSize** | [**[Number]**](Number.md)| Number of records per page of results.  Max is 2000. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## focal

> focal(opts)

Retrieve focal data by genes Gistic2 results.

This service provides access to the Gistic2 focal_data_by_genes.txt output data. This output is similar to the all_data_by_genes.txt output, but using only focal events with lengths greater than the  focal length cutoff. This data is a gene-level table of copy number values for all samples. The returned copy number values are in units (copy number - 2) so that no amplification or deletion is 0, genes with amplifications have positive values, and genes with deletions are negative values. The data are converted from marker level to gene level using the extreme method: a gene is assigned the greatest amplification or the least deletion value among the markers it covers. Results may be filtered by cohort, gene, and/or barcode, but at least one gene or barcode must be supplied.

### Example

```javascript
import FireBrowseBetaApi from 'fire_browse_beta_api';

let apiInstance = new FireBrowseBetaApi.AnalysesApi();
let opts = {
  'format': "'json'", // String | Format of result.
  'cohort': ["null"], // [String] | Narrow search to one or more TCGA disease cohorts from the scrollable list.
  'gene': ["null"], // [String] | Comma separated list of gene name(s).
  'tcgaParticipantBarcode': ["null"], // [String] | Comma separated list of TCGA participant barcodes (e.g. TCGA-GF-A4EO).
  'page': [1], // [Number] | Which page (slice) of entire results set should be returned. 
  'pageSize': [250], // [Number] | Number of records per page of results.  Max is 2000.
  'sortBy': "'cohort'" // String | Which column in the results should be used for sorting paginated results?
};
apiInstance.focal(opts, (error, data, response) => {
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
 **gene** | [**[String]**](String.md)| Comma separated list of gene name(s). | [optional] 
 **tcgaParticipantBarcode** | [**[String]**](String.md)| Comma separated list of TCGA participant barcodes (e.g. TCGA-GF-A4EO). | [optional] 
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


## mAF

> mAF(opts)

Retrieve MutSig final analysis MAF.

This service returns columns from the MAF generated by MutSig. Results may be filtered by gene, cohort, tool, or barcode, but at least one gene OR barcode OR cohort must be given.  By default a subset consisting of the most commonly used columns will be returned, but that can be modified with the column parameter. Specifying &#39;all&#39; in this parameter is a convenient way to return every column of the respective MAF, and has precedence over any any other column selection expression.  The complete list of column names that may be specified is &lt;a href&#x3D;&#39;http://firebrowse.org/api-docs/#!/Metadata/MAFColNames&#39;&gt;given here&lt;/a&gt;.  For more information on the mutation data, and how it is processed by Firehose, please consult the &lt;a href&#x3D;\&quot;https://confluence.broadinstitute.org/display/GDAC/Documentation#Documentation-MutationPipelines\&quot;&gt;pipeline documentation&lt;/a&gt;.

### Example

```javascript
import FireBrowseBetaApi from 'fire_browse_beta_api';

let apiInstance = new FireBrowseBetaApi.AnalysesApi();
let opts = {
  'format': "'json'", // String | Format of result.
  'cohort': ["null"], // [String] | Narrow search to one or more TCGA disease cohorts from the scrollable list.
  'tool': ["'MutSig2CV'"], // [String] | Narrow search to include only data/results produced by the selected Firehose tool.
  'gene': ["null"], // [String] | Comma separated list of gene name(s).
  'tcgaParticipantBarcode': ["null"], // [String] | Comma separated list of TCGA participant barcodes (e.g. TCGA-GF-A4EO).
  'column': ["null"], // [String] | Comma separated list of which data columns/fields to return.
  'page': [1], // [Number] | Which page (slice) of entire results set should be returned. 
  'pageSize': [250], // [Number] | Number of records per page of results.  Max is 2000.
  'sortBy': "'cohort'" // String | Which column in the results should be used for sorting paginated results?
};
apiInstance.mAF(opts, (error, data, response) => {
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
 **tool** | [**[String]**](String.md)| Narrow search to include only data/results produced by the selected Firehose tool. | [optional] 
 **gene** | [**[String]**](String.md)| Comma separated list of gene name(s). | [optional] 
 **tcgaParticipantBarcode** | [**[String]**](String.md)| Comma separated list of TCGA participant barcodes (e.g. TCGA-GF-A4EO). | [optional] 
 **column** | [**[String]**](String.md)| Comma separated list of which data columns/fields to return. | [optional] 
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


## mRNASeqQuartiles

> mRNASeqQuartiles(gene, opts)

Returns RNASeq expression quartiles, e.g. suitable for drawing a boxplot.

For a given gene compute quartiles and extrema, suitable e.g. for drawing a boxplot (Tukey 1977).  Results may be filtered by cohort, sample type, patient barcode  or characterization protocol, and are returned sorted by cohort.  Note that samples for which no expression value was recorded (e.g. &lt;a href&#x3D;\&quot;http://firebrowse.org/api/v1/Samples/mRNASeq?&amp;gene&#x3D;egfr&amp;cohort&#x3D;SKCM&amp;tcga_participant_barcode&#x3D;TCGA-GN-A262\&quot;&gt;the melanoma sample TCGA-GN-262&lt;/a&gt;) are removed prior to calculation.

### Example

```javascript
import FireBrowseBetaApi from 'fire_browse_beta_api';

let apiInstance = new FireBrowseBetaApi.AnalysesApi();
let gene = "gene_example"; // String | Enter a single gene name.
let opts = {
  'format': "'json'", // String | Format of result.
  'cohort': ["null"], // [String] | Narrow search to one or more TCGA disease cohorts from the scrollable list.
  'protocol': ["'RSEM'"], // [String] | Narrow search to one or more sample characterization protocols from the scrollable list.
  'sampleType': ["'tumors'"], // [String] | For which type of sample(s) should quartiles be computed?
  'exclude': ["null"] // [String] | Comma separated list of TCGA participants, identified by barcodes such as TCGA-GF-A4EO, denoting samples to exclude from computation.
};
apiInstance.mRNASeqQuartiles(gene, opts, (error, data, response) => {
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
 **gene** | **String**| Enter a single gene name. | 
 **format** | **String**| Format of result. | [optional] [default to &#39;json&#39;]
 **cohort** | [**[String]**](String.md)| Narrow search to one or more TCGA disease cohorts from the scrollable list. | [optional] 
 **protocol** | [**[String]**](String.md)| Narrow search to one or more sample characterization protocols from the scrollable list. | [optional] 
 **sampleType** | [**[String]**](String.md)| For which type of sample(s) should quartiles be computed? | [optional] 
 **exclude** | [**[String]**](String.md)| Comma separated list of TCGA participants, identified by barcodes such as TCGA-GF-A4EO, denoting samples to exclude from computation. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## reports

> reports(opts)

Retrieve links to summary reports from Firehose analysis runs.

This service returns URLs to the analysis result reports for runs of the Broad Institute GDAC Firehose analysis pipeline. At least one year of run reports are maintained in the database, but the reports from the latest run will be returned by default. The set of &lt;a href&#x3D;\&quot;https://confluence.broadinstitute.org/display/GDAC/Nozzle\&quot;&gt;Nozzle&lt;/a&gt; reports returned may be filtered by disease cohort, report type and report name.

### Example

```javascript
import FireBrowseBetaApi from 'fire_browse_beta_api';

let apiInstance = new FireBrowseBetaApi.AnalysesApi();
let opts = {
  'format': "'json'", // String | Format of result.
  'date': [new Date("null")], // [Date] | Select one or more date stamps.
  'cohort': ["null"], // [String] | Narrow search to one or more TCGA disease cohorts from the scrollable list.
  'name': ["null"], // [String] | Narrow search to one or more report names.
  'type': ["null"], // [String] | Narrow search to one or more report types.
  'page': [1], // [Number] | Which page (slice) of entire results set should be returned. 
  'pageSize': [250], // [Number] | Number of records per page of results.  Max is 2000.
  'sortBy': "'date'" // String | Which column in the results should be used for sorting paginated results?
};
apiInstance.reports(opts, (error, data, response) => {
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
 **date** | [**[Date]**](Date.md)| Select one or more date stamps. | [optional] 
 **cohort** | [**[String]**](String.md)| Narrow search to one or more TCGA disease cohorts from the scrollable list. | [optional] 
 **name** | [**[String]**](String.md)| Narrow search to one or more report names. | [optional] 
 **type** | [**[String]**](String.md)| Narrow search to one or more report types. | [optional] 
 **page** | [**[Number]**](Number.md)| Which page (slice) of entire results set should be returned.  | [optional] 
 **pageSize** | [**[Number]**](Number.md)| Number of records per page of results.  Max is 2000. | [optional] 
 **sortBy** | **String**| Which column in the results should be used for sorting paginated results? | [optional] [default to &#39;date&#39;]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## sMG

> sMG(opts)

Retrieve Significantly Mutated Genes (SMG).

This service provides a list of significantly mutated genes, as scored by MutSig.  It may be filtered by cohort, rank, gene, tool and/or Q-value threshold, but at least one cohort or gene must be supplied.

### Example

```javascript
import FireBrowseBetaApi from 'fire_browse_beta_api';

let apiInstance = new FireBrowseBetaApi.AnalysesApi();
let opts = {
  'format': "'json'", // String | Format of result.
  'cohort': ["null"], // [String] | Narrow search to one or more TCGA disease cohorts from the scrollable list.
  'tool': ["'MutSig2CV'"], // [String] | Narrow search to include only data/results produced by the selected Firehose tool.
  'rank': 56, // Number | Number of significant genes to return.
  'gene': ["null"], // [String] | Comma separated list of gene name(s).
  'q': 3.4, // Number | Only return results with Q-value <= given threshold.
  'page': [1], // [Number] | Which page (slice) of entire results set should be returned. 
  'pageSize': [250], // [Number] | Number of records per page of results.  Max is 2000.
  'sortBy': "'rank'" // String | Which column in the results should be used for sorting paginated results?
};
apiInstance.sMG(opts, (error, data, response) => {
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
 **tool** | [**[String]**](String.md)| Narrow search to include only data/results produced by the selected Firehose tool. | [optional] 
 **rank** | **Number**| Number of significant genes to return. | [optional] 
 **gene** | [**[String]**](String.md)| Comma separated list of gene name(s). | [optional] 
 **q** | **Number**| Only return results with Q-value &lt;&#x3D; given threshold. | [optional] 
 **page** | [**[Number]**](Number.md)| Which page (slice) of entire results set should be returned.  | [optional] 
 **pageSize** | [**[Number]**](Number.md)| Number of records per page of results.  Max is 2000. | [optional] 
 **sortBy** | **String**| Which column in the results should be used for sorting paginated results? | [optional] [default to &#39;rank&#39;]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## thresholded

> thresholded(opts)

Retrieve all thresholded by genes Gistic2 results.

This service provides access to the Gistic2 all_thresholded_by_genes.txt output data. A gene-level table of discrete amplification and deletion indicators for all samples. A table value of 0 means no amplification or deletion above the threshold. Amplifications are positive numbers: 1 means amplification above the amplification threshold; 2 means amplifications larger to the arm level amplifications observed for the sample. Deletions are represented by negative table values: -1 represents deletion beyond the threshold; -2 means deletions greater than the minimum arm-level deletion observed for the sample. Results maybe filtered by cohort, gene or barcode, but at least one gene or barcode must be supplied.

### Example

```javascript
import FireBrowseBetaApi from 'fire_browse_beta_api';

let apiInstance = new FireBrowseBetaApi.AnalysesApi();
let opts = {
  'format': "'json'", // String | Format of result.
  'cohort': ["null"], // [String] | Narrow search to one or more TCGA disease cohorts from the scrollable list.
  'gene': ["null"], // [String] | Comma separated list of gene name(s).
  'tcgaParticipantBarcode': ["null"], // [String] | Comma separated list of TCGA participant barcodes (e.g. TCGA-GF-A4EO).
  'page': [1], // [Number] | Which page (slice) of entire results set should be returned. 
  'pageSize': [250], // [Number] | Number of records per page of results.  Max is 2000.
  'sortBy': "'cohort'" // String | Which column in the results should be used for sorting paginated results?
};
apiInstance.thresholded(opts, (error, data, response) => {
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
 **gene** | [**[String]**](String.md)| Comma separated list of gene name(s). | [optional] 
 **tcgaParticipantBarcode** | [**[String]**](String.md)| Comma separated list of TCGA participant barcodes (e.g. TCGA-GF-A4EO). | [optional] 
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

