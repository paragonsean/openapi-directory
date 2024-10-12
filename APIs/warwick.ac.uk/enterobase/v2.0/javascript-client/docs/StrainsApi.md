# EnterobaseApi.StrainsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiV20DatabaseStrainsBarcodeGet**](StrainsApi.md#apiV20DatabaseStrainsBarcodeGet) | **GET** /api/v2.0/{database}/strains/{barcode} | 
[**apiV20DatabaseStrainsBarcodePost**](StrainsApi.md#apiV20DatabaseStrainsBarcodePost) | **POST** /api/v2.0/{database}/strains/{barcode} | 
[**apiV20DatabaseStrainsBarcodePut**](StrainsApi.md#apiV20DatabaseStrainsBarcodePut) | **PUT** /api/v2.0/{database}/strains/{barcode} | 
[**apiV20DatabaseStrainsGet**](StrainsApi.md#apiV20DatabaseStrainsGet) | **GET** /api/v2.0/{database}/strains | 



## apiV20DatabaseStrainsBarcodeGet

> apiV20DatabaseStrainsBarcodeGet(database, barcode, opts)



Strain metadata

### Example

```javascript
import EnterobaseApi from 'enterobase_api';

let apiInstance = new EnterobaseApi.StrainsApi();
let database = "database_example"; // String | Species database name (senterica, ecoli, yersinia, mcatarrhalis) for Salmonella, Escherichia, Yersinia, Moraxella respectively
let barcode = "barcode_example"; // String | Unique barcode for Strain records, <database prefix>_<ID code> e.g. SAL_AA0001AA
let opts = {
  'apiV20DatabaseStrainsBarcodeGetRequest': new EnterobaseApi.ApiV20DatabaseStrainsBarcodeGetRequest() // ApiV20DatabaseStrainsBarcodeGetRequest | 
};
apiInstance.apiV20DatabaseStrainsBarcodeGet(database, barcode, opts, (error, data, response) => {
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
 **database** | **String**| Species database name (senterica, ecoli, yersinia, mcatarrhalis) for Salmonella, Escherichia, Yersinia, Moraxella respectively | 
 **barcode** | **String**| Unique barcode for Strain records, &lt;database prefix&gt;_&lt;ID code&gt; e.g. SAL_AA0001AA | 
 **apiV20DatabaseStrainsBarcodeGetRequest** | [**ApiV20DatabaseStrainsBarcodeGetRequest**](ApiV20DatabaseStrainsBarcodeGetRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## apiV20DatabaseStrainsBarcodePost

> apiV20DatabaseStrainsBarcodePost(database, barcode, opts)



Strain metadata

### Example

```javascript
import EnterobaseApi from 'enterobase_api';

let apiInstance = new EnterobaseApi.StrainsApi();
let database = "database_example"; // String | Species database name (senterica, ecoli, yersinia, mcatarrhalis) for Salmonella, Escherichia, Yersinia, Moraxella respectively
let barcode = "barcode_example"; // String | Unique barcode for Strain records, <database prefix>_<ID code> e.g. SAL_AA0001AA
let opts = {
  'apiV20DatabaseStrainsBarcodeGetRequest': new EnterobaseApi.ApiV20DatabaseStrainsBarcodeGetRequest() // ApiV20DatabaseStrainsBarcodeGetRequest | 
};
apiInstance.apiV20DatabaseStrainsBarcodePost(database, barcode, opts, (error, data, response) => {
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
 **database** | **String**| Species database name (senterica, ecoli, yersinia, mcatarrhalis) for Salmonella, Escherichia, Yersinia, Moraxella respectively | 
 **barcode** | **String**| Unique barcode for Strain records, &lt;database prefix&gt;_&lt;ID code&gt; e.g. SAL_AA0001AA | 
 **apiV20DatabaseStrainsBarcodeGetRequest** | [**ApiV20DatabaseStrainsBarcodeGetRequest**](ApiV20DatabaseStrainsBarcodeGetRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## apiV20DatabaseStrainsBarcodePut

> apiV20DatabaseStrainsBarcodePut(database, barcode, opts)



Strain metadata

### Example

```javascript
import EnterobaseApi from 'enterobase_api';

let apiInstance = new EnterobaseApi.StrainsApi();
let database = "database_example"; // String | Species database name (senterica, ecoli, yersinia, mcatarrhalis) for Salmonella, Escherichia, Yersinia, Moraxella respectively
let barcode = "barcode_example"; // String | Unique barcode for Strain records, <database prefix>_<ID code> e.g. SAL_AA0001AA
let opts = {
  'apiV20DatabaseStrainsBarcodeGetRequest': new EnterobaseApi.ApiV20DatabaseStrainsBarcodeGetRequest() // ApiV20DatabaseStrainsBarcodeGetRequest | 
};
apiInstance.apiV20DatabaseStrainsBarcodePut(database, barcode, opts, (error, data, response) => {
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
 **database** | **String**| Species database name (senterica, ecoli, yersinia, mcatarrhalis) for Salmonella, Escherichia, Yersinia, Moraxella respectively | 
 **barcode** | **String**| Unique barcode for Strain records, &lt;database prefix&gt;_&lt;ID code&gt; e.g. SAL_AA0001AA | 
 **apiV20DatabaseStrainsBarcodeGetRequest** | [**ApiV20DatabaseStrainsBarcodeGetRequest**](ApiV20DatabaseStrainsBarcodeGetRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## apiV20DatabaseStrainsGet

> apiV20DatabaseStrainsGet(database, opts)



Strain metadata

### Example

```javascript
import EnterobaseApi from 'enterobase_api';

let apiInstance = new EnterobaseApi.StrainsApi();
let database = "database_example"; // String | Species database name (senterica, ecoli, yersinia, mcatarrhalis) for Salmonella, Escherichia, Yersinia, Moraxella respectively
let opts = {
  'continent': "continent_example", // String | 
  'offset': 0, // Number | Cursor position in results
  'sampleAccession': "sampleAccession_example", // String | 
  'latitude': 3.4, // Number | 
  'collectionMonth': 56, // Number | 
  'antigenicFormulas': "antigenicFormulas_example", // String | 
  'strainName': "strainName_example", // String | 
  'labContact': "labContact_example", // String | 
  'sortorder': "'asc'", // String | Order of search results: asc or desc
  'limit': 50, // Number | Number of results per page
  'serotype': "serotype_example", // String | 
  'region': "region_example", // String | 
  'country': "country_example", // String | 
  'collectionDate': 56, // Number | 
  'returnAll': true, // Boolean | 
  'onlyFields': ["null"], // [String] | 
  'sourceNiche': "sourceNiche_example", // String | 
  'collectionYear': 56, // Number | 
  'secondarySampleAccession': "secondarySampleAccession_example", // String | 
  'sourceDetails': "sourceDetails_example", // String | 
  'substrains': true, // Boolean | 
  'version': 56, // Number | 
  'sourceType': "sourceType_example", // String | 
  'orderby': "'barcode'", // String | Field to order by. Default: barcode
  'myStrains': true, // Boolean | 
  'collectionTime': "collectionTime_example", // String | 
  'county': "county_example", // String | 
  'uberstrain': "uberstrain_example", // String | 
  'comment': "comment_example", // String | 
  'longitude': 3.4, // Number | 
  'reldate': 56, // Number | 
  'assemblyBarcode': "assemblyBarcode_example", // String | 
  'barcode': ["null"], // [String] | Unique barcode for Strain records, <database prefix>_<ID code> e.g. SAL_AA0001AA
  'postcode': "postcode_example", // String | 
  'city': "city_example" // String | 
};
apiInstance.apiV20DatabaseStrainsGet(database, opts, (error, data, response) => {
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
 **database** | **String**| Species database name (senterica, ecoli, yersinia, mcatarrhalis) for Salmonella, Escherichia, Yersinia, Moraxella respectively | 
 **continent** | **String**|  | [optional] 
 **offset** | **Number**| Cursor position in results | [optional] [default to 0]
 **sampleAccession** | **String**|  | [optional] 
 **latitude** | **Number**|  | [optional] 
 **collectionMonth** | **Number**|  | [optional] 
 **antigenicFormulas** | **String**|  | [optional] 
 **strainName** | **String**|  | [optional] 
 **labContact** | **String**|  | [optional] 
 **sortorder** | **String**| Order of search results: asc or desc | [optional] [default to &#39;asc&#39;]
 **limit** | **Number**| Number of results per page | [optional] [default to 50]
 **serotype** | **String**|  | [optional] 
 **region** | **String**|  | [optional] 
 **country** | **String**|  | [optional] 
 **collectionDate** | **Number**|  | [optional] 
 **returnAll** | **Boolean**|  | [optional] 
 **onlyFields** | [**[String]**](String.md)|  | [optional] 
 **sourceNiche** | **String**|  | [optional] 
 **collectionYear** | **Number**|  | [optional] 
 **secondarySampleAccession** | **String**|  | [optional] 
 **sourceDetails** | **String**|  | [optional] 
 **substrains** | **Boolean**|  | [optional] 
 **version** | **Number**|  | [optional] 
 **sourceType** | **String**|  | [optional] 
 **orderby** | **String**| Field to order by. Default: barcode | [optional] [default to &#39;barcode&#39;]
 **myStrains** | **Boolean**|  | [optional] 
 **collectionTime** | **String**|  | [optional] 
 **county** | **String**|  | [optional] 
 **uberstrain** | **String**|  | [optional] 
 **comment** | **String**|  | [optional] 
 **longitude** | **Number**|  | [optional] 
 **reldate** | **Number**|  | [optional] 
 **assemblyBarcode** | **String**|  | [optional] 
 **barcode** | [**[String]**](String.md)| Unique barcode for Strain records, &lt;database prefix&gt;_&lt;ID code&gt; e.g. SAL_AA0001AA | [optional] 
 **postcode** | **String**|  | [optional] 
 **city** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

