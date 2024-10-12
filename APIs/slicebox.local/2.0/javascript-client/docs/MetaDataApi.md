# SliceboxApi.MetaDataApi

All URIs are relative to *http://slicebox.local/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**metadataFlatseriesGet**](MetaDataApi.md#metadataFlatseriesGet) | **GET** /metadata/flatseries | 
[**metadataFlatseriesIdGet**](MetaDataApi.md#metadataFlatseriesIdGet) | **GET** /metadata/flatseries/{id} | 
[**metadataFlatseriesQueryPost**](MetaDataApi.md#metadataFlatseriesQueryPost) | **POST** /metadata/flatseries/query | 
[**metadataImagesGet**](MetaDataApi.md#metadataImagesGet) | **GET** /metadata/images | 
[**metadataImagesIdGet**](MetaDataApi.md#metadataImagesIdGet) | **GET** /metadata/images/{id} | 
[**metadataImagesQueryPost**](MetaDataApi.md#metadataImagesQueryPost) | **POST** /metadata/images/query | 
[**metadataPatientsGet**](MetaDataApi.md#metadataPatientsGet) | **GET** /metadata/patients | 
[**metadataPatientsIdGet**](MetaDataApi.md#metadataPatientsIdGet) | **GET** /metadata/patients/{id} | 
[**metadataPatientsIdImagesGet**](MetaDataApi.md#metadataPatientsIdImagesGet) | **GET** /metadata/patients/{id}/images | 
[**metadataPatientsQueryPost**](MetaDataApi.md#metadataPatientsQueryPost) | **POST** /metadata/patients/query | 
[**metadataSeriesGet**](MetaDataApi.md#metadataSeriesGet) | **GET** /metadata/series | 
[**metadataSeriesIdGet**](MetaDataApi.md#metadataSeriesIdGet) | **GET** /metadata/series/{id} | 
[**metadataSeriesIdSeriestagsGet**](MetaDataApi.md#metadataSeriesIdSeriestagsGet) | **GET** /metadata/series/{id}/seriestags | 
[**metadataSeriesIdSeriestagsPost**](MetaDataApi.md#metadataSeriesIdSeriestagsPost) | **POST** /metadata/series/{id}/seriestags | 
[**metadataSeriesIdSeriestypesDelete**](MetaDataApi.md#metadataSeriesIdSeriestypesDelete) | **DELETE** /metadata/series/{id}/seriestypes | 
[**metadataSeriesIdSeriestypesGet**](MetaDataApi.md#metadataSeriesIdSeriestypesGet) | **GET** /metadata/series/{id}/seriestypes | 
[**metadataSeriesIdSourceGet**](MetaDataApi.md#metadataSeriesIdSourceGet) | **GET** /metadata/series/{id}/source | 
[**metadataSeriesQueryPost**](MetaDataApi.md#metadataSeriesQueryPost) | **POST** /metadata/series/query | 
[**metadataSeriesSeriesIdSeriestagsSeriesTagIdDelete**](MetaDataApi.md#metadataSeriesSeriesIdSeriestagsSeriesTagIdDelete) | **DELETE** /metadata/series/{seriesId}/seriestags/{seriesTagId} | 
[**metadataSeriesSeriesIdSeriestypesSeriesTypeIdDelete**](MetaDataApi.md#metadataSeriesSeriesIdSeriestypesSeriesTypeIdDelete) | **DELETE** /metadata/series/{seriesId}/seriestypes/{seriesTypeId} | 
[**metadataSeriesSeriesIdSeriestypesSeriesTypeIdPut**](MetaDataApi.md#metadataSeriesSeriesIdSeriestypesSeriesTypeIdPut) | **PUT** /metadata/series/{seriesId}/seriestypes/{seriesTypeId} | 
[**metadataSeriestagsGet**](MetaDataApi.md#metadataSeriestagsGet) | **GET** /metadata/seriestags | 
[**metadataStudiesGet**](MetaDataApi.md#metadataStudiesGet) | **GET** /metadata/studies | 
[**metadataStudiesIdGet**](MetaDataApi.md#metadataStudiesIdGet) | **GET** /metadata/studies/{id} | 
[**metadataStudiesIdImagesGet**](MetaDataApi.md#metadataStudiesIdImagesGet) | **GET** /metadata/studies/{id}/images | 
[**metadataStudiesQueryPost**](MetaDataApi.md#metadataStudiesQueryPost) | **POST** /metadata/studies/query | 
[**seriestypesSeriesQueryPost**](MetaDataApi.md#seriestypesSeriesQueryPost) | **POST** /seriestypes/series/query | 



## metadataFlatseriesGet

> [FlatSeries] metadataFlatseriesGet(opts)



Returns a list of flattened metadata on the patient, study and series levels

### Example

```javascript
import SliceboxApi from 'slicebox_api';

let apiInstance = new SliceboxApi.MetaDataApi();
let opts = {
  'startindex': 0, // Number | start index of returned slice of flat series
  'count': 20, // Number | size of returned slice of flat series
  'orderby': "orderby_example", // String | flat series property to order results by
  'orderascending': true, // Boolean | order result ascendingly if true, descendingly otherwise
  'filter': "filter_example", // String | filter the results by matching substrings of flat series properties against this value
  'sources': "sources_example", // String | filter the results by matching on one or more series sources. Examples of sources are user, box, directory or scp. The list of sources to filter results by must have the form TYPE1:ID1,TYPE2:ID2,...,TYPEN:IDN. For instance, the argument sources=box:1,user:5 shows results either sent from (slice)box with id 1 or uploaded by user with id 5.
  'seriestypes': "seriestypes_example", // String | filter the results by matching on one or more series types. The supplied list of series types must be a comma separated list of series type ids. For instance, the argument seriestypes=3,7,22 shows series assigned to either of the series types with ids 3, 7 and 22.
  'seriestags': "seriestags_example" // String | filter the results by matching on one or more series tags. The supplied list of series tags must be a comma separated list of series tag ids. For instance, the argument seriestags=6,2,11 shows series with either of the series tags with ids 6, 2 and 11.
};
apiInstance.metadataFlatseriesGet(opts, (error, data, response) => {
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
 **startindex** | **Number**| start index of returned slice of flat series | [optional] [default to 0]
 **count** | **Number**| size of returned slice of flat series | [optional] [default to 20]
 **orderby** | **String**| flat series property to order results by | [optional] 
 **orderascending** | **Boolean**| order result ascendingly if true, descendingly otherwise | [optional] [default to true]
 **filter** | **String**| filter the results by matching substrings of flat series properties against this value | [optional] 
 **sources** | **String**| filter the results by matching on one or more series sources. Examples of sources are user, box, directory or scp. The list of sources to filter results by must have the form TYPE1:ID1,TYPE2:ID2,...,TYPEN:IDN. For instance, the argument sources&#x3D;box:1,user:5 shows results either sent from (slice)box with id 1 or uploaded by user with id 5. | [optional] 
 **seriestypes** | **String**| filter the results by matching on one or more series types. The supplied list of series types must be a comma separated list of series type ids. For instance, the argument seriestypes&#x3D;3,7,22 shows series assigned to either of the series types with ids 3, 7 and 22. | [optional] 
 **seriestags** | **String**| filter the results by matching on one or more series tags. The supplied list of series tags must be a comma separated list of series tag ids. For instance, the argument seriestags&#x3D;6,2,11 shows series with either of the series tags with ids 6, 2 and 11. | [optional] 

### Return type

[**[FlatSeries]**](FlatSeries.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/octet-stream


## metadataFlatseriesIdGet

> FlatSeries metadataFlatseriesIdGet(id)



Return the flat series with the supplied ID

### Example

```javascript
import SliceboxApi from 'slicebox_api';

let apiInstance = new SliceboxApi.MetaDataApi();
let id = 789; // Number | ID of flat series
apiInstance.metadataFlatseriesIdGet(id, (error, data, response) => {
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
 **id** | **Number**| ID of flat series | 

### Return type

[**FlatSeries**](FlatSeries.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/octet-stream


## metadataFlatseriesQueryPost

> [FlatSeries] metadataFlatseriesQueryPost(query)



submit a query for flat series

### Example

```javascript
import SliceboxApi from 'slicebox_api';

let apiInstance = new SliceboxApi.MetaDataApi();
let query = new SliceboxApi.Query(); // Query | parameters of flat series query
apiInstance.metadataFlatseriesQueryPost(query, (error, data, response) => {
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
 **query** | [**Query**](Query.md)| parameters of flat series query | 

### Return type

[**[FlatSeries]**](FlatSeries.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/octet-stream, multipart/form-data
- **Accept**: application/json, application/octet-stream


## metadataImagesGet

> [Image] metadataImagesGet(seriesid, opts)



Returns a list of metadata on the image level of the DICOM hierarchy

### Example

```javascript
import SliceboxApi from 'slicebox_api';

let apiInstance = new SliceboxApi.MetaDataApi();
let seriesid = 789; // Number | reference to series to list images for
let opts = {
  'startindex': 0, // Number | start index of returned slice of images
  'count': 20 // Number | size of returned slice of images
};
apiInstance.metadataImagesGet(seriesid, opts, (error, data, response) => {
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
 **seriesid** | **Number**| reference to series to list images for | 
 **startindex** | **Number**| start index of returned slice of images | [optional] [default to 0]
 **count** | **Number**| size of returned slice of images | [optional] [default to 20]

### Return type

[**[Image]**](Image.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/octet-stream


## metadataImagesIdGet

> Image metadataImagesIdGet(id)



Return the image with the supplied ID

### Example

```javascript
import SliceboxApi from 'slicebox_api';

let apiInstance = new SliceboxApi.MetaDataApi();
let id = 789; // Number | ID of image
apiInstance.metadataImagesIdGet(id, (error, data, response) => {
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
 **id** | **Number**| ID of image | 

### Return type

[**Image**](Image.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/octet-stream


## metadataImagesQueryPost

> [Image] metadataImagesQueryPost(query)



submit a query for images

### Example

```javascript
import SliceboxApi from 'slicebox_api';

let apiInstance = new SliceboxApi.MetaDataApi();
let query = new SliceboxApi.Query(); // Query | parameters of images query
apiInstance.metadataImagesQueryPost(query, (error, data, response) => {
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
 **query** | [**Query**](Query.md)| parameters of images query | 

### Return type

[**[Image]**](Image.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/octet-stream, multipart/form-data
- **Accept**: application/json, application/octet-stream


## metadataPatientsGet

> [Patient] metadataPatientsGet(opts)



Returns a list of metadata on the patient level of the DICOM hierarchy

### Example

```javascript
import SliceboxApi from 'slicebox_api';

let apiInstance = new SliceboxApi.MetaDataApi();
let opts = {
  'startindex': 0, // Number | start index of returned slice of patients
  'count': 20, // Number | size of returned slice of patients
  'orderby': "orderby_example", // String | patient property to order results by
  'orderascending': true, // Boolean | order result ascendingly if true, descendingly otherwise
  'filter': "filter_example", // String | filter the results by matching substrings of patient properties against this value
  'sources': "sources_example", // String | filter the results by matching on one or more underlying series sources. Examples of sources are user, box, directory or scp. The list of sources to filter results by must have the form TYPE1:ID1,TYPE2:ID2,...,TYPEN:IDN. For instance, the argument sources=box:1,user:5 shows results either sent from (slice)box with id 1 or uploaded by user with id 5.
  'seriestypes': "seriestypes_example", // String | filter the results by matching on one or more underlying series types. The supplied list of series types must be a comma separated list of series type ids. For instance, the argument seriestypes=3,7,22 shows results including series assigned to either of the series types with ids 3, 7 and 22.
  'seriestags': "seriestags_example" // String | filter the results by matching on one or more underlying series tags. The supplied list of series tags must be a comma separated list of series tag ids. For instance, the argument seriestags=6,2,11 shows results including series with either of the series tags with ids 6, 2 and 11.
};
apiInstance.metadataPatientsGet(opts, (error, data, response) => {
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
 **startindex** | **Number**| start index of returned slice of patients | [optional] [default to 0]
 **count** | **Number**| size of returned slice of patients | [optional] [default to 20]
 **orderby** | **String**| patient property to order results by | [optional] 
 **orderascending** | **Boolean**| order result ascendingly if true, descendingly otherwise | [optional] [default to true]
 **filter** | **String**| filter the results by matching substrings of patient properties against this value | [optional] 
 **sources** | **String**| filter the results by matching on one or more underlying series sources. Examples of sources are user, box, directory or scp. The list of sources to filter results by must have the form TYPE1:ID1,TYPE2:ID2,...,TYPEN:IDN. For instance, the argument sources&#x3D;box:1,user:5 shows results either sent from (slice)box with id 1 or uploaded by user with id 5. | [optional] 
 **seriestypes** | **String**| filter the results by matching on one or more underlying series types. The supplied list of series types must be a comma separated list of series type ids. For instance, the argument seriestypes&#x3D;3,7,22 shows results including series assigned to either of the series types with ids 3, 7 and 22. | [optional] 
 **seriestags** | **String**| filter the results by matching on one or more underlying series tags. The supplied list of series tags must be a comma separated list of series tag ids. For instance, the argument seriestags&#x3D;6,2,11 shows results including series with either of the series tags with ids 6, 2 and 11. | [optional] 

### Return type

[**[Patient]**](Patient.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/octet-stream


## metadataPatientsIdGet

> Patient metadataPatientsIdGet(id)



Return the patient with the supplied ID

### Example

```javascript
import SliceboxApi from 'slicebox_api';

let apiInstance = new SliceboxApi.MetaDataApi();
let id = 789; // Number | ID of patient
apiInstance.metadataPatientsIdGet(id, (error, data, response) => {
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
 **id** | **Number**| ID of patient | 

### Return type

[**Patient**](Patient.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/octet-stream


## metadataPatientsIdImagesGet

> [Image] metadataPatientsIdImagesGet(id, opts)



Returns all images for the patient with the supplied patient ID

### Example

```javascript
import SliceboxApi from 'slicebox_api';

let apiInstance = new SliceboxApi.MetaDataApi();
let id = 789; // Number | ID of patient
let opts = {
  'sources': "sources_example", // String | filter the results by matching on one or more series sources. Examples of sources are user, box, directory or scp. The list of sources to filter results by must have the form TYPE1:ID1,TYPE2:ID2,...,TYPEN:IDN. For instance, the argument sources=box:1,user:5 shows results either sent from (slice)box with id 1 or uploaded by user with id 5.
  'seriestypes': "seriestypes_example", // String | filter the results by matching on one or more series types. The supplied list of series types must be a comma separated list of series type ids. For instance, the argument seriestypes=3,7,22 shows series assigned to either of the series types with ids 3, 7 and 22.
  'seriestags': "seriestags_example" // String | filter the results by matching on one or more series tags. The supplied list of series tags must be a comma separated list of series tag ids. For instance, the argument seriestags=6,2,11 shows series with either of the series tags with ids 6, 2 and 11.
};
apiInstance.metadataPatientsIdImagesGet(id, opts, (error, data, response) => {
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
 **id** | **Number**| ID of patient | 
 **sources** | **String**| filter the results by matching on one or more series sources. Examples of sources are user, box, directory or scp. The list of sources to filter results by must have the form TYPE1:ID1,TYPE2:ID2,...,TYPEN:IDN. For instance, the argument sources&#x3D;box:1,user:5 shows results either sent from (slice)box with id 1 or uploaded by user with id 5. | [optional] 
 **seriestypes** | **String**| filter the results by matching on one or more series types. The supplied list of series types must be a comma separated list of series type ids. For instance, the argument seriestypes&#x3D;3,7,22 shows series assigned to either of the series types with ids 3, 7 and 22. | [optional] 
 **seriestags** | **String**| filter the results by matching on one or more series tags. The supplied list of series tags must be a comma separated list of series tag ids. For instance, the argument seriestags&#x3D;6,2,11 shows series with either of the series tags with ids 6, 2 and 11. | [optional] 

### Return type

[**[Image]**](Image.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/octet-stream


## metadataPatientsQueryPost

> [Patient] metadataPatientsQueryPost(query)



submit a query for patients

### Example

```javascript
import SliceboxApi from 'slicebox_api';

let apiInstance = new SliceboxApi.MetaDataApi();
let query = new SliceboxApi.Query(); // Query | parameters of patient query
apiInstance.metadataPatientsQueryPost(query, (error, data, response) => {
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
 **query** | [**Query**](Query.md)| parameters of patient query | 

### Return type

[**[Patient]**](Patient.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/octet-stream, multipart/form-data
- **Accept**: application/json, application/octet-stream


## metadataSeriesGet

> [Series] metadataSeriesGet(studyid, opts)



Returns a list of metadata on the series level of the DICOM hierarchy

### Example

```javascript
import SliceboxApi from 'slicebox_api';

let apiInstance = new SliceboxApi.MetaDataApi();
let studyid = 789; // Number | reference to study to list series for
let opts = {
  'startindex': 0, // Number | start index of returned slice of series
  'count': 20, // Number | size of returned slice of series
  'sources': "sources_example", // String | filter the results by matching on one or more series sources. Examples of sources are user, box, directory or scp. The list of sources to filter results by must have the form TYPE1:ID1,TYPE2:ID2,...,TYPEN:IDN. For instance, the argument sources=box:1,user:5 shows results either sent from (slice)box with id 1 or uploaded by user with id 5.
  'seriestypes': "seriestypes_example", // String | filter the results by matching on one or more series types. The supplied list of series types must be a comma separated list of series type ids. For instance, the argument seriestypes=3,7,22 shows series assigned to either of the series types with ids 3, 7 and 22.
  'seriestags': "seriestags_example" // String | filter the results by matching on one or more series tags. The supplied list of series tags must be a comma separated list of series tag ids. For instance, the argument seriestags=6,2,11 shows series with either of the series tags with ids 6, 2 and 11.
};
apiInstance.metadataSeriesGet(studyid, opts, (error, data, response) => {
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
 **studyid** | **Number**| reference to study to list series for | 
 **startindex** | **Number**| start index of returned slice of series | [optional] [default to 0]
 **count** | **Number**| size of returned slice of series | [optional] [default to 20]
 **sources** | **String**| filter the results by matching on one or more series sources. Examples of sources are user, box, directory or scp. The list of sources to filter results by must have the form TYPE1:ID1,TYPE2:ID2,...,TYPEN:IDN. For instance, the argument sources&#x3D;box:1,user:5 shows results either sent from (slice)box with id 1 or uploaded by user with id 5. | [optional] 
 **seriestypes** | **String**| filter the results by matching on one or more series types. The supplied list of series types must be a comma separated list of series type ids. For instance, the argument seriestypes&#x3D;3,7,22 shows series assigned to either of the series types with ids 3, 7 and 22. | [optional] 
 **seriestags** | **String**| filter the results by matching on one or more series tags. The supplied list of series tags must be a comma separated list of series tag ids. For instance, the argument seriestags&#x3D;6,2,11 shows series with either of the series tags with ids 6, 2 and 11. | [optional] 

### Return type

[**[Series]**](Series.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/octet-stream


## metadataSeriesIdGet

> Series metadataSeriesIdGet(id)



Return the series with the supplied ID

### Example

```javascript
import SliceboxApi from 'slicebox_api';

let apiInstance = new SliceboxApi.MetaDataApi();
let id = 789; // Number | ID of series
apiInstance.metadataSeriesIdGet(id, (error, data, response) => {
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
 **id** | **Number**| ID of series | 

### Return type

[**Series**](Series.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/octet-stream


## metadataSeriesIdSeriestagsGet

> [Seriestag] metadataSeriesIdSeriestagsGet(id)



get the list of series tags for the series with the supplied ID.

### Example

```javascript
import SliceboxApi from 'slicebox_api';

let apiInstance = new SliceboxApi.MetaDataApi();
let id = 789; // Number | ID of series
apiInstance.metadataSeriesIdSeriestagsGet(id, (error, data, response) => {
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
 **id** | **Number**| ID of series | 

### Return type

[**[Seriestag]**](Seriestag.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/octet-stream


## metadataSeriesIdSeriestagsPost

> Seriestag metadataSeriesIdSeriestagsPost(id, query)



add a series tag to the series with the supplied ID

### Example

```javascript
import SliceboxApi from 'slicebox_api';

let apiInstance = new SliceboxApi.MetaDataApi();
let id = 789; // Number | ID of series
let query = new SliceboxApi.Seriestag(); // Seriestag | series tag to add
apiInstance.metadataSeriesIdSeriestagsPost(id, query, (error, data, response) => {
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
 **id** | **Number**| ID of series | 
 **query** | [**Seriestag**](Seriestag.md)| series tag to add | 

### Return type

[**Seriestag**](Seriestag.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/octet-stream, multipart/form-data
- **Accept**: application/json, application/octet-stream


## metadataSeriesIdSeriestypesDelete

> metadataSeriesIdSeriestypesDelete(id)



Delete all series types for the series with the supplied ID

### Example

```javascript
import SliceboxApi from 'slicebox_api';

let apiInstance = new SliceboxApi.MetaDataApi();
let id = 789; // Number | ID of series
apiInstance.metadataSeriesIdSeriestypesDelete(id, (error, data, response) => {
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
 **id** | **Number**| ID of series | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## metadataSeriesIdSeriestypesGet

> [Seriestype] metadataSeriesIdSeriestypesGet(id)



get the list of series types for the series with the supplied ID.

### Example

```javascript
import SliceboxApi from 'slicebox_api';

let apiInstance = new SliceboxApi.MetaDataApi();
let id = 789; // Number | ID of series
apiInstance.metadataSeriesIdSeriestypesGet(id, (error, data, response) => {
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
 **id** | **Number**| ID of series | 

### Return type

[**[Seriestype]**](Seriestype.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/octet-stream


## metadataSeriesIdSourceGet

> Source metadataSeriesIdSourceGet(id)



Return the source of the series with the supplied ID

### Example

```javascript
import SliceboxApi from 'slicebox_api';

let apiInstance = new SliceboxApi.MetaDataApi();
let id = 789; // Number | ID of series
apiInstance.metadataSeriesIdSourceGet(id, (error, data, response) => {
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
 **id** | **Number**| ID of series | 

### Return type

[**Source**](Source.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/octet-stream


## metadataSeriesQueryPost

> [Series] metadataSeriesQueryPost(query)



submit a query for series

### Example

```javascript
import SliceboxApi from 'slicebox_api';

let apiInstance = new SliceboxApi.MetaDataApi();
let query = new SliceboxApi.Query(); // Query | parameters of series query
apiInstance.metadataSeriesQueryPost(query, (error, data, response) => {
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
 **query** | [**Query**](Query.md)| parameters of series query | 

### Return type

[**[Series]**](Series.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/octet-stream, multipart/form-data
- **Accept**: application/json, application/octet-stream


## metadataSeriesSeriesIdSeriestagsSeriesTagIdDelete

> metadataSeriesSeriesIdSeriestagsSeriesTagIdDelete(seriesId, seriesTagId)



Delete the series tag with the supplied series tag ID from the series with the supplied series ID

### Example

```javascript
import SliceboxApi from 'slicebox_api';

let apiInstance = new SliceboxApi.MetaDataApi();
let seriesId = 789; // Number | ID of series
let seriesTagId = 789; // Number | ID of series tag to remove
apiInstance.metadataSeriesSeriesIdSeriestagsSeriesTagIdDelete(seriesId, seriesTagId, (error, data, response) => {
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
 **seriesId** | **Number**| ID of series | 
 **seriesTagId** | **Number**| ID of series tag to remove | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## metadataSeriesSeriesIdSeriestypesSeriesTypeIdDelete

> metadataSeriesSeriesIdSeriestypesSeriesTypeIdDelete(seriesId, seriesTypeId)



Delete the series type with the supplied series type ID from the series with the supplied series ID

### Example

```javascript
import SliceboxApi from 'slicebox_api';

let apiInstance = new SliceboxApi.MetaDataApi();
let seriesId = 789; // Number | ID of series
let seriesTypeId = 789; // Number | ID of series type to remove
apiInstance.metadataSeriesSeriesIdSeriestypesSeriesTypeIdDelete(seriesId, seriesTypeId, (error, data, response) => {
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
 **seriesId** | **Number**| ID of series | 
 **seriesTypeId** | **Number**| ID of series type to remove | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## metadataSeriesSeriesIdSeriestypesSeriesTypeIdPut

> metadataSeriesSeriesIdSeriestypesSeriesTypeIdPut(seriesId, seriesTypeId)



Add the series type with the supplied series type ID to the series with the supplied series ID

### Example

```javascript
import SliceboxApi from 'slicebox_api';

let apiInstance = new SliceboxApi.MetaDataApi();
let seriesId = 789; // Number | ID of series
let seriesTypeId = 789; // Number | ID of series type to add
apiInstance.metadataSeriesSeriesIdSeriestypesSeriesTypeIdPut(seriesId, seriesTypeId, (error, data, response) => {
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
 **seriesId** | **Number**| ID of series | 
 **seriesTypeId** | **Number**| ID of series type to add | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## metadataSeriestagsGet

> [Seriestag] metadataSeriestagsGet()



Returns a list of series tags currently currently in use.

### Example

```javascript
import SliceboxApi from 'slicebox_api';

let apiInstance = new SliceboxApi.MetaDataApi();
apiInstance.metadataSeriestagsGet((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**[Seriestag]**](Seriestag.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/octet-stream


## metadataStudiesGet

> [Study] metadataStudiesGet(patientid, opts)



Returns a list of metadata on the study level of the DICOM hierarchy

### Example

```javascript
import SliceboxApi from 'slicebox_api';

let apiInstance = new SliceboxApi.MetaDataApi();
let patientid = 789; // Number | reference to patient to list studies for
let opts = {
  'startindex': 0, // Number | start index of returned slice of studies
  'count': 20, // Number | size of returned slice of studies
  'sources': "sources_example", // String | filter the results by matching on one or more underlying series sources. Examples of sources are user, box, directory or scp. The list of sources to filter results by must have the form TYPE1:ID1,TYPE2:ID2,...,TYPEN:IDN. For instance, the argument sources=box:1,user:5 shows results either sent from (slice)box with id 1 or uploaded by user with id 5.
  'seriestypes': "seriestypes_example", // String | filter the results by matching on one or more underlying series types. The supplied list of series types must be a comma separated list of series type ids. For instance, the argument seriestypes=3,7,22 shows results including series assigned to either of the series types with ids 3, 7 and 22.
  'seriestags': "seriestags_example" // String | filter the results by matching on one or more underlying series tags. The supplied list of series tags must be a comma separated list of series tag ids. For instance, the argument seriestags=6,2,11 shows results including series with either of the series tags with ids 6, 2 and 11.
};
apiInstance.metadataStudiesGet(patientid, opts, (error, data, response) => {
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
 **patientid** | **Number**| reference to patient to list studies for | 
 **startindex** | **Number**| start index of returned slice of studies | [optional] [default to 0]
 **count** | **Number**| size of returned slice of studies | [optional] [default to 20]
 **sources** | **String**| filter the results by matching on one or more underlying series sources. Examples of sources are user, box, directory or scp. The list of sources to filter results by must have the form TYPE1:ID1,TYPE2:ID2,...,TYPEN:IDN. For instance, the argument sources&#x3D;box:1,user:5 shows results either sent from (slice)box with id 1 or uploaded by user with id 5. | [optional] 
 **seriestypes** | **String**| filter the results by matching on one or more underlying series types. The supplied list of series types must be a comma separated list of series type ids. For instance, the argument seriestypes&#x3D;3,7,22 shows results including series assigned to either of the series types with ids 3, 7 and 22. | [optional] 
 **seriestags** | **String**| filter the results by matching on one or more underlying series tags. The supplied list of series tags must be a comma separated list of series tag ids. For instance, the argument seriestags&#x3D;6,2,11 shows results including series with either of the series tags with ids 6, 2 and 11. | [optional] 

### Return type

[**[Study]**](Study.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/octet-stream


## metadataStudiesIdGet

> Study metadataStudiesIdGet(id)



Return the study with the supplied ID

### Example

```javascript
import SliceboxApi from 'slicebox_api';

let apiInstance = new SliceboxApi.MetaDataApi();
let id = 789; // Number | ID of study
apiInstance.metadataStudiesIdGet(id, (error, data, response) => {
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
 **id** | **Number**| ID of study | 

### Return type

[**Study**](Study.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/octet-stream


## metadataStudiesIdImagesGet

> [Image] metadataStudiesIdImagesGet(id, opts)



Returns all images for the study with the supplied study ID

### Example

```javascript
import SliceboxApi from 'slicebox_api';

let apiInstance = new SliceboxApi.MetaDataApi();
let id = 789; // Number | ID of study
let opts = {
  'sources': "sources_example", // String | filter the results by matching on one or more series sources. Examples of sources are user, box, directory or scp. The list of sources to filter results by must have the form TYPE1:ID1,TYPE2:ID2,...,TYPEN:IDN. For instance, the argument sources=box:1,user:5 shows results either sent from (slice)box with id 1 or uploaded by user with id 5.
  'seriestypes': "seriestypes_example", // String | filter the results by matching on one or more series types. The supplied list of series types must be a comma separated list of series type ids. For instance, the argument seriestypes=3,7,22 shows series assigned to either of the series types with ids 3, 7 and 22.
  'seriestags': "seriestags_example" // String | filter the results by matching on one or more series tags. The supplied list of series tags must be a comma separated list of series tag ids. For instance, the argument seriestags=6,2,11 shows series with either of the series tags with ids 6, 2 and 11.
};
apiInstance.metadataStudiesIdImagesGet(id, opts, (error, data, response) => {
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
 **id** | **Number**| ID of study | 
 **sources** | **String**| filter the results by matching on one or more series sources. Examples of sources are user, box, directory or scp. The list of sources to filter results by must have the form TYPE1:ID1,TYPE2:ID2,...,TYPEN:IDN. For instance, the argument sources&#x3D;box:1,user:5 shows results either sent from (slice)box with id 1 or uploaded by user with id 5. | [optional] 
 **seriestypes** | **String**| filter the results by matching on one or more series types. The supplied list of series types must be a comma separated list of series type ids. For instance, the argument seriestypes&#x3D;3,7,22 shows series assigned to either of the series types with ids 3, 7 and 22. | [optional] 
 **seriestags** | **String**| filter the results by matching on one or more series tags. The supplied list of series tags must be a comma separated list of series tag ids. For instance, the argument seriestags&#x3D;6,2,11 shows series with either of the series tags with ids 6, 2 and 11. | [optional] 

### Return type

[**[Image]**](Image.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/octet-stream


## metadataStudiesQueryPost

> [Study] metadataStudiesQueryPost(query)



submit a query for studies

### Example

```javascript
import SliceboxApi from 'slicebox_api';

let apiInstance = new SliceboxApi.MetaDataApi();
let query = new SliceboxApi.Query(); // Query | parameters of study query
apiInstance.metadataStudiesQueryPost(query, (error, data, response) => {
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
 **query** | [**Query**](Query.md)| parameters of study query | 

### Return type

[**[Study]**](Study.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/octet-stream, multipart/form-data
- **Accept**: application/json, application/octet-stream


## seriestypesSeriesQueryPost

> Seriesidseriestypesresult seriestypesSeriesQueryPost(query)



submit a query for seriestypes for a list of series

### Example

```javascript
import SliceboxApi from 'slicebox_api';

let apiInstance = new SliceboxApi.MetaDataApi();
let query = new SliceboxApi.Idsquery(); // Idsquery | parameters of series query
apiInstance.seriestypesSeriesQueryPost(query, (error, data, response) => {
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
 **query** | [**Idsquery**](Idsquery.md)| parameters of series query | 

### Return type

[**Seriesidseriestypesresult**](Seriesidseriestypesresult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/octet-stream, multipart/form-data
- **Accept**: application/json, application/octet-stream

