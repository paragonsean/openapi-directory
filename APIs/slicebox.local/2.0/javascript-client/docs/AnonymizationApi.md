# SliceboxApi.AnonymizationApi

All URIs are relative to *http://slicebox.local/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**anonymizationAnonymizePost**](AnonymizationApi.md#anonymizationAnonymizePost) | **POST** /anonymization/anonymize | 
[**anonymizationKeysExportCsvGet**](AnonymizationApi.md#anonymizationKeysExportCsvGet) | **GET** /anonymization/keys/export/csv | 
[**anonymizationKeysGet**](AnonymizationApi.md#anonymizationKeysGet) | **GET** /anonymization/keys | 
[**anonymizationKeysIdDelete**](AnonymizationApi.md#anonymizationKeysIdDelete) | **DELETE** /anonymization/keys/{id} | 
[**anonymizationKeysIdGet**](AnonymizationApi.md#anonymizationKeysIdGet) | **GET** /anonymization/keys/{id} | 
[**anonymizationKeysIdKeyvaluesGet**](AnonymizationApi.md#anonymizationKeysIdKeyvaluesGet) | **GET** /anonymization/keys/{id}/keyvalues | 
[**anonymizationKeysQueryPost**](AnonymizationApi.md#anonymizationKeysQueryPost) | **POST** /anonymization/keys/query | 
[**anonymizationOptionsGet**](AnonymizationApi.md#anonymizationOptionsGet) | **GET** /anonymization/options | 
[**imagesIdAnonymizePut**](AnonymizationApi.md#imagesIdAnonymizePut) | **PUT** /images/{id}/anonymize | 
[**imagesIdAnonymizedPost**](AnonymizationApi.md#imagesIdAnonymizedPost) | **POST** /images/{id}/anonymized | 



## anonymizationAnonymizePost

> [Image] anonymizationAnonymizePost(query)



anonymize the images corresponding to the supplied list of image IDs (each paired with a list of DICOM tag translation). This route corresponds to repeated use of the route /images/{id}/anonymize.

### Example

```javascript
import SliceboxApi from 'slicebox_api';

let apiInstance = new SliceboxApi.AnonymizationApi();
let query = [new SliceboxApi.ImageTagValues()]; // [ImageTagValues] | parameters of anonymization key query
apiInstance.anonymizationAnonymizePost(query, (error, data, response) => {
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
 **query** | [**[ImageTagValues]**](ImageTagValues.md)| parameters of anonymization key query | 

### Return type

[**[Image]**](Image.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/octet-stream, multipart/form-data
- **Accept**: application/json, application/octet-stream


## anonymizationKeysExportCsvGet

> String anonymizationKeysExportCsvGet()



export all anonymization keys as a csv file

### Example

```javascript
import SliceboxApi from 'slicebox_api';

let apiInstance = new SliceboxApi.AnonymizationApi();
apiInstance.anonymizationKeysExportCsvGet((error, data, response) => {
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

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/octet-stream


## anonymizationKeysGet

> [AnonymizationKey] anonymizationKeysGet(opts)



get a list of anonymization keys, each specifying how vital DICOM attributes have been anonymized for a particular image

### Example

```javascript
import SliceboxApi from 'slicebox_api';

let apiInstance = new SliceboxApi.AnonymizationApi();
let opts = {
  'startindex': 0, // Number | start index of returned slice of anonymization keys
  'count': 20, // Number | size of returned slice of anonymization keys
  'orderby': "orderby_example", // String | property to order results by
  'orderascending': true, // Boolean | order result ascendingly if true, descendingly otherwise
  'filter': "filter_example" // String | filter the results by matching substrings of properties against this value
};
apiInstance.anonymizationKeysGet(opts, (error, data, response) => {
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
 **startindex** | **Number**| start index of returned slice of anonymization keys | [optional] [default to 0]
 **count** | **Number**| size of returned slice of anonymization keys | [optional] [default to 20]
 **orderby** | **String**| property to order results by | [optional] 
 **orderascending** | **Boolean**| order result ascendingly if true, descendingly otherwise | [optional] [default to true]
 **filter** | **String**| filter the results by matching substrings of properties against this value | [optional] 

### Return type

[**[AnonymizationKey]**](AnonymizationKey.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/octet-stream


## anonymizationKeysIdDelete

> anonymizationKeysIdDelete(id)



delete an anonymization key that is no longer of interest

### Example

```javascript
import SliceboxApi from 'slicebox_api';

let apiInstance = new SliceboxApi.AnonymizationApi();
let id = 789; // Number | ID of anonymization key
apiInstance.anonymizationKeysIdDelete(id, (error, data, response) => {
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
 **id** | **Number**| ID of anonymization key | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## anonymizationKeysIdGet

> AnonymizationKey anonymizationKeysIdGet(id)



get the anonymization key with the supplied ID

### Example

```javascript
import SliceboxApi from 'slicebox_api';

let apiInstance = new SliceboxApi.AnonymizationApi();
let id = 789; // Number | ID of anonymization key
apiInstance.anonymizationKeysIdGet(id, (error, data, response) => {
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
 **id** | **Number**| ID of anonymization key | 

### Return type

[**AnonymizationKey**](AnonymizationKey.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/octet-stream


## anonymizationKeysIdKeyvaluesGet

> [AnonymizationKeyValue] anonymizationKeysIdKeyvaluesGet(id)



get pointers to the images corresponding to the anonymization key with the supplied ID

### Example

```javascript
import SliceboxApi from 'slicebox_api';

let apiInstance = new SliceboxApi.AnonymizationApi();
let id = 789; // Number | ID of anonymization key
apiInstance.anonymizationKeysIdKeyvaluesGet(id, (error, data, response) => {
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
 **id** | **Number**| ID of anonymization key | 

### Return type

[**[AnonymizationKeyValue]**](AnonymizationKeyValue.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/octet-stream


## anonymizationKeysQueryPost

> [AnonymizationKey] anonymizationKeysQueryPost(query)



submit a query for anonymization keys

### Example

```javascript
import SliceboxApi from 'slicebox_api';

let apiInstance = new SliceboxApi.AnonymizationApi();
let query = new SliceboxApi.AnonymizationKeyQuery(); // AnonymizationKeyQuery | parameters of anonymization key query
apiInstance.anonymizationKeysQueryPost(query, (error, data, response) => {
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
 **query** | [**AnonymizationKeyQuery**](AnonymizationKeyQuery.md)| parameters of anonymization key query | 

### Return type

[**[AnonymizationKey]**](AnonymizationKey.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/octet-stream, multipart/form-data
- **Accept**: application/json, application/octet-stream


## anonymizationOptionsGet

> [ConfidentialityOption] anonymizationOptionsGet()



list all supported anonymization options defining an anonymization profile

### Example

```javascript
import SliceboxApi from 'slicebox_api';

let apiInstance = new SliceboxApi.AnonymizationApi();
apiInstance.anonymizationOptionsGet((error, data, response) => {
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

[**[ConfidentialityOption]**](ConfidentialityOption.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/octet-stream


## imagesIdAnonymizePut

> Image imagesIdAnonymizePut(id, tagValues)



delete the selected image and replace it with an anonymized version

### Example

```javascript
import SliceboxApi from 'slicebox_api';

let apiInstance = new SliceboxApi.AnonymizationApi();
let id = 789; // Number | ID of image to anonymize
let tagValues = new SliceboxApi.AnonymizationData(); // AnonymizationData | specification of values for anonymous DICOM attributes
apiInstance.imagesIdAnonymizePut(id, tagValues, (error, data, response) => {
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
 **id** | **Number**| ID of image to anonymize | 
 **tagValues** | [**AnonymizationData**](AnonymizationData.md)| specification of values for anonymous DICOM attributes | 

### Return type

[**Image**](Image.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/octet-stream, multipart/form-data
- **Accept**: application/json, application/octet-stream


## imagesIdAnonymizedPost

> imagesIdAnonymizedPost(id, tagValues)



get an anonymized version of the image with the supplied ID

### Example

```javascript
import SliceboxApi from 'slicebox_api';

let apiInstance = new SliceboxApi.AnonymizationApi();
let id = 789; // Number | ID of image for which to get anonymized dataset
let tagValues = new SliceboxApi.AnonymizationData(); // AnonymizationData | specification of values for anonymous DICOM attributes
apiInstance.imagesIdAnonymizedPost(id, tagValues, (error, data, response) => {
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
 **id** | **Number**| ID of image for which to get anonymized dataset | 
 **tagValues** | [**AnonymizationData**](AnonymizationData.md)| specification of values for anonymous DICOM attributes | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/octet-stream, multipart/form-data
- **Accept**: Not defined

