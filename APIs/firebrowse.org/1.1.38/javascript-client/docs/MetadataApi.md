# FireBrowseBetaApi.MetadataApi

All URIs are relative to *http://firebrowse.org/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**barcode**](MetadataApi.md#barcode) | **GET** /Metadata/SampleType/Barcode/{TCGA_Barcode} | Given a TCGA barcode, return its short letter sample type code.
[**centers**](MetadataApi.md#centers) | **GET** /Metadata/Centers | Obtain identities of TCGA consortium member centers.
[**clinicalNames**](MetadataApi.md#clinicalNames) | **GET** /Metadata/ClinicalNames | Retrieve names of all TCGA clinical data elements (CDEs).
[**clinicalNamesFH**](MetadataApi.md#clinicalNamesFH) | **GET** /Metadata/ClinicalNames_FH | Retrieve names of CDEs normalized by Firehose and selected for analyses.
[**code**](MetadataApi.md#code) | **GET** /Metadata/SampleType/Code/{code} | Translate from numeric to symbolic TCGA sample codes.
[**cohorts**](MetadataApi.md#cohorts) | **GET** /Metadata/Cohorts | Translate TCGA cohort abbreviations to full disease names.
[**counts**](MetadataApi.md#counts) | **GET** /Metadata/Counts | Retrieve sample counts.
[**dates**](MetadataApi.md#dates) | **GET** /Metadata/Dates | Retrieve dates of all GDAC Firehose stddata &amp; analyses runs that have been ingested into FireBrowse.
[**heartBeat**](MetadataApi.md#heartBeat) | **GET** /Metadata/HeartBeat | Simple way to discern whether API server is up and running
[**mAFColNames**](MetadataApi.md#mAFColNames) | **GET** /Metadata/MAFColNames | Retrieve names of all columns in the mutation annotation files (MAFs) served by FireBrowse.
[**patients**](MetadataApi.md#patients) | **GET** /Metadata/Patients | Retrieve list of all TCGA patients.
[**platforms**](MetadataApi.md#platforms) | **GET** /Metadata/Platforms | Translate TCGA platform codes to full platform names.
[**sampleTypes**](MetadataApi.md#sampleTypes) | **GET** /Metadata/SampleTypes | Return all TCGA sample type codes, both numeric and symbolic.
[**shortLetterCode**](MetadataApi.md#shortLetterCode) | **GET** /Metadata/SampleType/ShortLetterCode/{short_letter_code} | Translate from symbolic to numeric TCGA sample codes.
[**tSSites**](MetadataApi.md#tSSites) | **GET** /Metadata/TSSites | Obtain identities of tissue source sites in TCGA.



## barcode

> barcode(tCGABarcode, opts)

Given a TCGA barcode, return its short letter sample type code.

### Example

```javascript
import FireBrowseBetaApi from 'fire_browse_beta_api';

let apiInstance = new FireBrowseBetaApi.MetadataApi();
let tCGABarcode = "tCGABarcode_example"; // String | Enter a single TCGA barcode, of any form: e.g. TCGA-GF-A4EO-06 or TCGA-EL-A3D5-01A-22D-A202-08
let opts = {
  'format': "'json'" // String | Format of result.
};
apiInstance.barcode(tCGABarcode, opts, (error, data, response) => {
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
 **tCGABarcode** | **String**| Enter a single TCGA barcode, of any form: e.g. TCGA-GF-A4EO-06 or TCGA-EL-A3D5-01A-22D-A202-08 | 
 **format** | **String**| Format of result. | [optional] [default to &#39;json&#39;]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## centers

> centers(opts)

Obtain identities of TCGA consortium member centers.

By default this function returns a table of all consortium members in TCGA, aka centers; it provides both the HTTP domain and full organizational name of each center.  A subset of this table may be obtained by explicitly specifying one or more domain names.

### Example

```javascript
import FireBrowseBetaApi from 'fire_browse_beta_api';

let apiInstance = new FireBrowseBetaApi.MetadataApi();
let opts = {
  'format': "'json'", // String | Format of result.
  'center': ["null"] // [String] | Narrow search to one or more TCGA centers from the scrollable list.
};
apiInstance.centers(opts, (error, data, response) => {
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
 **center** | [**[String]**](String.md)| Narrow search to one or more TCGA centers from the scrollable list. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## clinicalNames

> clinicalNames(opts)

Retrieve names of all TCGA clinical data elements (CDEs).

Retrieve names of all patient-level clinical data elements (CDES) available in TCGA, unioned across all disease cohorts. A CDE will be listed here only when it has a value other than NA for at least 1 patient case in any disease cohort. For more information on how these CDEs are processed see our &lt;a href&#x3D;\&quot;https://confluence.broadinstitute.org/display/GDAC/Documentation\&quot;&gt;pipeline documentation&lt;/a&gt;.

### Example

```javascript
import FireBrowseBetaApi from 'fire_browse_beta_api';

let apiInstance = new FireBrowseBetaApi.MetadataApi();
let opts = {
  'format': "'json'" // String | Format of result.
};
apiInstance.clinicalNames(opts, (error, data, response) => {
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

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## clinicalNamesFH

> clinicalNamesFH(opts)

Retrieve names of CDEs normalized by Firehose and selected for analyses.

This service returns the names of patient-level clinical data elements (CDEs) that have been normalized by Firehose for use in analyses, unioned across all disease cohorts. For more information on how these CDEs are processed, see our &lt;a href&#x3D;\&quot;https://confluence.broadinstitute.org/display/GDAC/Documentation\&quot;&gt;pipeline documentation&lt;/a&gt;.

### Example

```javascript
import FireBrowseBetaApi from 'fire_browse_beta_api';

let apiInstance = new FireBrowseBetaApi.MetadataApi();
let opts = {
  'format': "'json'" // String | Format of result.
};
apiInstance.clinicalNamesFH(opts, (error, data, response) => {
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

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## code

> code(code, opts)

Translate from numeric to symbolic TCGA sample codes.

Convert a TCGA numeric sample type code (e.g. 01, 02) to its corresponding symbolic (short letter) code (e.g. TP, TR).

### Example

```javascript
import FireBrowseBetaApi from 'fire_browse_beta_api';

let apiInstance = new FireBrowseBetaApi.MetadataApi();
let code = ["null"]; // [String] | Narrow search to one or more TCGA sample type codes.
let opts = {
  'format': "'json'" // String | Format of result.
};
apiInstance.code(code, opts, (error, data, response) => {
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
 **code** | [**[String]**](String.md)| Narrow search to one or more TCGA sample type codes. | 
 **format** | **String**| Format of result. | [optional] [default to &#39;json&#39;]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## cohorts

> cohorts(opts)

Translate TCGA cohort abbreviations to full disease names.

By default this function returns a table containing all TCGA cohort abbreviations and their corresponding disease names.  A subset of that table may be obtained by explicitly specifying one or more cohort abbreviations.

### Example

```javascript
import FireBrowseBetaApi from 'fire_browse_beta_api';

let apiInstance = new FireBrowseBetaApi.MetadataApi();
let opts = {
  'format': "'json'", // String | Format of result.
  'cohort': ["null"] // [String] | Narrow search to one or more TCGA disease cohorts from the scrollable list.
};
apiInstance.cohorts(opts, (error, data, response) => {
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

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## counts

> counts(opts)

Retrieve sample counts.

Returns the aliquot counts for each disease cohort, per sample type and data type.  The sample type designation of \&quot;Tumor\&quot; may be used to aggregate the count of all tumor aliquots into a single number per disease and data type. See the SampleTypes function for a complete description of sample types.

### Example

```javascript
import FireBrowseBetaApi from 'fire_browse_beta_api';

let apiInstance = new FireBrowseBetaApi.MetadataApi();
let opts = {
  'format': "'json'", // String | Format of result.
  'date': [new Date("null")], // [Date] | Select one or more date stamps.
  'cohort': ["null"], // [String] | Narrow search to one or more TCGA disease cohorts from the scrollable list.
  'sampleType': ["null"], // [String] | Narrow search to one or more TCGA sample types from the scrollable list.
  'dataType': ["null"], // [String] | Narrow search to one or more TCGA data types from the scrollable list.
  'totals': true, // Boolean | Output an entry providing the totals for each data type.
  'sortBy': "'cohort'" // String | Which column in the results should be used for sorting paginated results?
};
apiInstance.counts(opts, (error, data, response) => {
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
 **sampleType** | [**[String]**](String.md)| Narrow search to one or more TCGA sample types from the scrollable list. | [optional] 
 **dataType** | [**[String]**](String.md)| Narrow search to one or more TCGA data types from the scrollable list. | [optional] 
 **totals** | **Boolean**| Output an entry providing the totals for each data type. | [optional] [default to true]
 **sortBy** | **String**| Which column in the results should be used for sorting paginated results? | [optional] [default to &#39;cohort&#39;]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## dates

> dates(opts)

Retrieve dates of all GDAC Firehose stddata &amp; analyses runs that have been ingested into FireBrowse.

### Example

```javascript
import FireBrowseBetaApi from 'fire_browse_beta_api';

let apiInstance = new FireBrowseBetaApi.MetadataApi();
let opts = {
  'format': "'json'" // String | Format of result.
};
apiInstance.dates(opts, (error, data, response) => {
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

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## heartBeat

> heartBeat(opts)

Simple way to discern whether API server is up and running

Returns a message to indicate that API (server) is up and running, or times out if not.

### Example

```javascript
import FireBrowseBetaApi from 'fire_browse_beta_api';

let apiInstance = new FireBrowseBetaApi.MetadataApi();
let opts = {
  'format': "'json'" // String | Format of result.
};
apiInstance.heartBeat(opts, (error, data, response) => {
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

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## mAFColNames

> mAFColNames(opts)

Retrieve names of all columns in the mutation annotation files (MAFs) served by FireBrowse.

Retrieve the names of all columns in the mutation annotation files (MAFs) hosted by FireBrowse.  For more information on the mutation data, and how it is processed by Firehose, please consult the &lt;a href&#x3D;\&quot;https://confluence.broadinstitute.org/display/GDAC/Documentation#Documentation-MutationPipelines\&quot;&gt;pipeline documentation&lt;/a&gt;.

### Example

```javascript
import FireBrowseBetaApi from 'fire_browse_beta_api';

let apiInstance = new FireBrowseBetaApi.MetadataApi();
let opts = {
  'format': "'json'" // String | Format of result.
};
apiInstance.mAFColNames(opts, (error, data, response) => {
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

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## patients

> patients(opts)

Retrieve list of all TCGA patients.

This service returns a list of all TCGA patient barcodes in FireBrowse, optionally filtered by disease cohort.  The barcodes are obtained directy from the clinical data.

### Example

```javascript
import FireBrowseBetaApi from 'fire_browse_beta_api';

let apiInstance = new FireBrowseBetaApi.MetadataApi();
let opts = {
  'format': "'json'", // String | Format of result.
  'cohort': ["null"], // [String] | Narrow search to one or more TCGA disease cohorts from the scrollable list.
  'page': [1], // [Number] | Which page (slice) of entire results set should be returned. 
  'pageSize': [250], // [Number] | Number of records per page of results.  Max is 2000.
  'sortBy': "'cohort'" // String | Which column in the results should be used for sorting paginated results?
};
apiInstance.patients(opts, (error, data, response) => {
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


## platforms

> platforms(opts)

Translate TCGA platform codes to full platform names.

By default this function returns a table of all of the technology platforms used to sequence or characterize samples in TCGA--both their short platform codes and full names.  A subset of this table may be obtained by explicitly specifying one or more platform codes.

### Example

```javascript
import FireBrowseBetaApi from 'fire_browse_beta_api';

let apiInstance = new FireBrowseBetaApi.MetadataApi();
let opts = {
  'format': "'json'", // String | Format of result.
  'platform': ["null"] // [String] | Narrow search to one or more TCGA data generation platforms from the scrollable list.
};
apiInstance.platforms(opts, (error, data, response) => {
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
 **platform** | [**[String]**](String.md)| Narrow search to one or more TCGA data generation platforms from the scrollable list. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## sampleTypes

> sampleTypes(opts)

Return all TCGA sample type codes, both numeric and symbolic.

### Example

```javascript
import FireBrowseBetaApi from 'fire_browse_beta_api';

let apiInstance = new FireBrowseBetaApi.MetadataApi();
let opts = {
  'format': "'json'" // String | Format of result.
};
apiInstance.sampleTypes(opts, (error, data, response) => {
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

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## shortLetterCode

> shortLetterCode(shortLetterCode, opts)

Translate from symbolic to numeric TCGA sample codes.

Convert a TCGA sample type code in symbolic form (or &#39;short letter code&#39; like TP, TR) to its corresponding numeric form (e.g. 01, 02).

### Example

```javascript
import FireBrowseBetaApi from 'fire_browse_beta_api';

let apiInstance = new FireBrowseBetaApi.MetadataApi();
let shortLetterCode = ["null"]; // [String] | TCGA sample type short letter code(s) (e.g. TP, NB, etc.). 
let opts = {
  'format': "'json'" // String | Format of result.
};
apiInstance.shortLetterCode(shortLetterCode, opts, (error, data, response) => {
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
 **shortLetterCode** | [**[String]**](String.md)| TCGA sample type short letter code(s) (e.g. TP, NB, etc.).  | 
 **format** | **String**| Format of result. | [optional] [default to &#39;json&#39;]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## tSSites

> tSSites(opts)

Obtain identities of tissue source sites in TCGA.

By default this function returns a table of all sites which contributed source tissue to TCGA, aka TSS&#39;s. A subset of this table may be obtained by explicitly specifying one or more sites.

### Example

```javascript
import FireBrowseBetaApi from 'fire_browse_beta_api';

let apiInstance = new FireBrowseBetaApi.MetadataApi();
let opts = {
  'format': "'json'", // String | Format of result.
  'tssCode': ["null"] // [String] | Narrow search to one or more TSS codes
};
apiInstance.tSSites(opts, (error, data, response) => {
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
 **tssCode** | [**[String]**](String.md)| Narrow search to one or more TSS codes | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

