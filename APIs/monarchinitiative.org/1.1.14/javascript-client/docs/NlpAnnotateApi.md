# BioLinkApi.NlpAnnotateApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getAnnotate**](NlpAnnotateApi.md#getAnnotate) | **GET** /nlp/annotate/ | Annotate a given text using SciGraph annotator
[**getAnnotateEntities**](NlpAnnotateApi.md#getAnnotateEntities) | **GET** /nlp/annotate/entities | Annotate a given content using SciGraph annotator and get all entities from content
[**postAnnotate**](NlpAnnotateApi.md#postAnnotate) | **POST** /nlp/annotate/ | Annotate a given text using SciGraph annotator
[**postAnnotateEntities**](NlpAnnotateApi.md#postAnnotateEntities) | **POST** /nlp/annotate/entities | Annotate a given content using SciGraph annotator and get all entities from content



## getAnnotate

> getAnnotate(opts)

Annotate a given text using SciGraph annotator

### Example

```javascript
import BioLinkApi from 'bio_link_api';

let apiInstance = new BioLinkApi.NlpAnnotateApi();
let opts = {
  'content': "content_example", // String | The text content to annotate
  'includeCategory': ["null"], // [String] | Categories to include for annotation
  'excludeCategory': ["null"], // [String] | Categories to exclude for annotation
  'minLength': "'4'", // String | The minimum number of characters in the annotated entity
  'longestOnly': false, // Boolean | Should only the longest entity be returned for an overlapping group
  'includeAbbreviation': false, // Boolean | Should abbreviations be included
  'includeAcronym': false, // Boolean | Should acronyms be included
  'includeNumbers': false // Boolean | Should numbers be included
};
apiInstance.getAnnotate(opts, (error, data, response) => {
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
 **content** | **String**| The text content to annotate | [optional] 
 **includeCategory** | [**[String]**](String.md)| Categories to include for annotation | [optional] 
 **excludeCategory** | [**[String]**](String.md)| Categories to exclude for annotation | [optional] 
 **minLength** | **String**| The minimum number of characters in the annotated entity | [optional] [default to &#39;4&#39;]
 **longestOnly** | **Boolean**| Should only the longest entity be returned for an overlapping group | [optional] [default to false]
 **includeAbbreviation** | **Boolean**| Should abbreviations be included | [optional] [default to false]
 **includeAcronym** | **Boolean**| Should acronyms be included | [optional] [default to false]
 **includeNumbers** | **Boolean**| Should numbers be included | [optional] [default to false]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getAnnotateEntities

> EntityAnnotationResult getAnnotateEntities(opts)

Annotate a given content using SciGraph annotator and get all entities from content

### Example

```javascript
import BioLinkApi from 'bio_link_api';

let apiInstance = new BioLinkApi.NlpAnnotateApi();
let opts = {
  'content': "content_example", // String | The text content to annotate
  'includeCategory': ["null"], // [String] | Categories to include for annotation
  'excludeCategory': ["null"], // [String] | Categories to exclude for annotation
  'minLength': "'4'", // String | The minimum number of characters in the annotated entity
  'longestOnly': false, // Boolean | Should only the longest entity be returned for an overlapping group
  'includeAbbreviation': false, // Boolean | Should abbreviations be included
  'includeAcronym': false, // Boolean | Should acronyms be included
  'includeNumbers': false // Boolean | Should numbers be included
};
apiInstance.getAnnotateEntities(opts, (error, data, response) => {
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
 **content** | **String**| The text content to annotate | [optional] 
 **includeCategory** | [**[String]**](String.md)| Categories to include for annotation | [optional] 
 **excludeCategory** | [**[String]**](String.md)| Categories to exclude for annotation | [optional] 
 **minLength** | **String**| The minimum number of characters in the annotated entity | [optional] [default to &#39;4&#39;]
 **longestOnly** | **Boolean**| Should only the longest entity be returned for an overlapping group | [optional] [default to false]
 **includeAbbreviation** | **Boolean**| Should abbreviations be included | [optional] [default to false]
 **includeAcronym** | **Boolean**| Should acronyms be included | [optional] [default to false]
 **includeNumbers** | **Boolean**| Should numbers be included | [optional] [default to false]

### Return type

[**EntityAnnotationResult**](EntityAnnotationResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## postAnnotate

> postAnnotate(opts)

Annotate a given text using SciGraph annotator

### Example

```javascript
import BioLinkApi from 'bio_link_api';

let apiInstance = new BioLinkApi.NlpAnnotateApi();
let opts = {
  'content': "content_example", // String | The text content to annotate
  'includeCategory': ["null"], // [String] | Categories to include for annotation
  'excludeCategory': ["null"], // [String] | Categories to exclude for annotation
  'minLength': "'4'", // String | The minimum number of characters in the annotated entity
  'longestOnly': false, // Boolean | Should only the longest entity be returned for an overlapping group
  'includeAbbreviation': false, // Boolean | Should abbreviations be included
  'includeAcronym': false, // Boolean | Should acronyms be included
  'includeNumbers': false // Boolean | Should numbers be included
};
apiInstance.postAnnotate(opts, (error, data, response) => {
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
 **content** | **String**| The text content to annotate | [optional] 
 **includeCategory** | [**[String]**](String.md)| Categories to include for annotation | [optional] 
 **excludeCategory** | [**[String]**](String.md)| Categories to exclude for annotation | [optional] 
 **minLength** | **String**| The minimum number of characters in the annotated entity | [optional] [default to &#39;4&#39;]
 **longestOnly** | **Boolean**| Should only the longest entity be returned for an overlapping group | [optional] [default to false]
 **includeAbbreviation** | **Boolean**| Should abbreviations be included | [optional] [default to false]
 **includeAcronym** | **Boolean**| Should acronyms be included | [optional] [default to false]
 **includeNumbers** | **Boolean**| Should numbers be included | [optional] [default to false]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## postAnnotateEntities

> EntityAnnotationResult postAnnotateEntities(opts)

Annotate a given content using SciGraph annotator and get all entities from content

### Example

```javascript
import BioLinkApi from 'bio_link_api';

let apiInstance = new BioLinkApi.NlpAnnotateApi();
let opts = {
  'content': "content_example", // String | The text content to annotate
  'includeCategory': ["null"], // [String] | Categories to include for annotation
  'excludeCategory': ["null"], // [String] | Categories to exclude for annotation
  'minLength': "'4'", // String | The minimum number of characters in the annotated entity
  'longestOnly': false, // Boolean | Should only the longest entity be returned for an overlapping group
  'includeAbbreviation': false, // Boolean | Should abbreviations be included
  'includeAcronym': false, // Boolean | Should acronyms be included
  'includeNumbers': false // Boolean | Should numbers be included
};
apiInstance.postAnnotateEntities(opts, (error, data, response) => {
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
 **content** | **String**| The text content to annotate | [optional] 
 **includeCategory** | [**[String]**](String.md)| Categories to include for annotation | [optional] 
 **excludeCategory** | [**[String]**](String.md)| Categories to exclude for annotation | [optional] 
 **minLength** | **String**| The minimum number of characters in the annotated entity | [optional] [default to &#39;4&#39;]
 **longestOnly** | **Boolean**| Should only the longest entity be returned for an overlapping group | [optional] [default to false]
 **includeAbbreviation** | **Boolean**| Should abbreviations be included | [optional] [default to false]
 **includeAcronym** | **Boolean**| Should acronyms be included | [optional] [default to false]
 **includeNumbers** | **Boolean**| Should numbers be included | [optional] [default to false]

### Return type

[**EntityAnnotationResult**](EntityAnnotationResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

