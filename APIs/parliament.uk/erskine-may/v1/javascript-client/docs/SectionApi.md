# ErskineMayApi.SectionApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiSectionSectionIdGet**](SectionApi.md#apiSectionSectionIdGet) | **GET** /api/Section/{sectionId} | Returns a section by section id.
[**apiSectionSectionIdstepGet**](SectionApi.md#apiSectionSectionIdstepGet) | **GET** /api/Section/{sectionId},{step} | Returns a section overview by section id and step.



## apiSectionSectionIdGet

> ErskineMaySectionDetail apiSectionSectionIdGet(sectionId)

Returns a section by section id.

### Example

```javascript
import ErskineMayApi from 'erskine_may_api';

let apiInstance = new ErskineMayApi.SectionApi();
let sectionId = 56; // Number | Section by id.
apiInstance.apiSectionSectionIdGet(sectionId, (error, data, response) => {
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
 **sectionId** | **Number**| Section by id. | 

### Return type

[**ErskineMaySectionDetail**](ErskineMaySectionDetail.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## apiSectionSectionIdstepGet

> ErskineMaySectionOverview apiSectionSectionIdstepGet(sectionId, step)

Returns a section overview by section id and step.

### Example

```javascript
import ErskineMayApi from 'erskine_may_api';

let apiInstance = new ErskineMayApi.SectionApi();
let sectionId = 56; // Number | Section by id.
let step = 56; // Number | Number of sections to step over from given section.
apiInstance.apiSectionSectionIdstepGet(sectionId, step, (error, data, response) => {
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
 **sectionId** | **Number**| Section by id. | 
 **step** | **Number**| Number of sections to step over from given section. | 

### Return type

[**ErskineMaySectionOverview**](ErskineMaySectionOverview.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain

