# EnterobaseApi.StraindataApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiV20DatabaseStraindataGet**](StraindataApi.md#apiV20DatabaseStraindataGet) | **GET** /api/v2.0/{database}/straindata | 



## apiV20DatabaseStraindataGet

> apiV20DatabaseStraindataGet(database, opts)



Strain data

### Example

```javascript
import EnterobaseApi from 'enterobase_api';

let apiInstance = new EnterobaseApi.StraindataApi();
let database = "database_example"; // String | Species database name (senterica, ecoli, yersinia, mcatarrhalis) for Salmonella, Escherichia, Yersinia, Moraxella respectively
let opts = {
  'continent': "continent_example", // String | 
  'offset': 0, // Number | Cursor position in results
  'sampleAccession': "sampleAccession_example", // String | 
  'latitude': 3.4, // Number | 
  'collectionMonth': 56, // Number | 
  'strainName': "strainName_example", // String | 
  'labContact': "labContact_example", // String | 
  'sortorder': "'asc'", // String | Order of search results: asc or desc
  'n50': 56, // Number | 
  'limit': 50, // Number | Number of results per page
  'serotype': "serotype_example", // String | 
  'region': "region_example", // String | 
  'country': "country_example", // String | 
  'collectionDate': 56, // Number | 
  'customFields': "customFields_example", // String | 
  'onlyFields': ["null"], // [String] | 
  'sourceNiche': "sourceNiche_example", // String | 
  'collectionYear': 56, // Number | 
  'secondarySampleAccession': "secondarySampleAccession_example", // String | 
  'sourceDetails': "sourceDetails_example", // String | 
  'substrains': true, // Boolean | 
  'version': 56, // Number | 
  'sourceType': "sourceType_example", // String | 
  'orderby': "orderby_example", // String | Field to order by. Default: strain barcode
  'myStrains': true, // Boolean | 
  'collectionTime': "collectionTime_example", // String | 
  'county': "county_example", // String | 
  'uberstrain': "uberstrain_example", // String | 
  'topSpecies': "topSpecies_example", // String | 
  'comment': "comment_example", // String | 
  'longitude': 3.4, // Number | 
  'reldate': 56, // Number | 
  'barcode': ["null"], // [String] | Unique barcode for Traces records, <database prefix>_<ID code>_AS e.g. SAL_AA0001AA_AS
  'postcode': "postcode_example", // String | 
  'email': "email_example", // String | 
  'assemblyStatus': "assemblyStatus_example", // String | 
  'city': "city_example" // String | 
};
apiInstance.apiV20DatabaseStraindataGet(database, opts, (error, data, response) => {
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
 **strainName** | **String**|  | [optional] 
 **labContact** | **String**|  | [optional] 
 **sortorder** | **String**| Order of search results: asc or desc | [optional] [default to &#39;asc&#39;]
 **n50** | **Number**|  | [optional] 
 **limit** | **Number**| Number of results per page | [optional] [default to 50]
 **serotype** | **String**|  | [optional] 
 **region** | **String**|  | [optional] 
 **country** | **String**|  | [optional] 
 **collectionDate** | **Number**|  | [optional] 
 **customFields** | **String**|  | [optional] 
 **onlyFields** | [**[String]**](String.md)|  | [optional] 
 **sourceNiche** | **String**|  | [optional] 
 **collectionYear** | **Number**|  | [optional] 
 **secondarySampleAccession** | **String**|  | [optional] 
 **sourceDetails** | **String**|  | [optional] 
 **substrains** | **Boolean**|  | [optional] 
 **version** | **Number**|  | [optional] 
 **sourceType** | **String**|  | [optional] 
 **orderby** | **String**| Field to order by. Default: strain barcode | [optional] 
 **myStrains** | **Boolean**|  | [optional] 
 **collectionTime** | **String**|  | [optional] 
 **county** | **String**|  | [optional] 
 **uberstrain** | **String**|  | [optional] 
 **topSpecies** | **String**|  | [optional] 
 **comment** | **String**|  | [optional] 
 **longitude** | **Number**|  | [optional] 
 **reldate** | **Number**|  | [optional] 
 **barcode** | [**[String]**](String.md)| Unique barcode for Traces records, &lt;database prefix&gt;_&lt;ID code&gt;_AS e.g. SAL_AA0001AA_AS | [optional] 
 **postcode** | **String**|  | [optional] 
 **email** | **String**|  | [optional] 
 **assemblyStatus** | **String**|  | [optional] 
 **city** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

