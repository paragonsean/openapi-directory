# AucklandMuseumApi.SubjectApi

All URIs are relative to *http://api.aucklandmuseum.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getSubject**](SubjectApi.md#getSubject) | **GET** /id/{identifier} | Explore details about a given subject node



## getSubject

> getSubject(identifier)

Explore details about a given subject node

Gets information about a &#x60;subject&#x60; identified by the &#x60;identifier&#x60;.  The response format depends upon the &#x60;Accept&#x60; header.   - &#x60;text/html&#x60; - the default response type. Returned data can be easily viewed in any modern Internet Browser   - &#x60;application/ld+json&#x60; - the response will be in [JSON-LD](http://json-ld.org/)   - &#x60;application/json&#x60; - the response will be a simple JSON Object with keys (predicates) and values (objects). 

### Example

```javascript
import AucklandMuseumApi from 'auckland_museum_api';

let apiInstance = new AucklandMuseumApi.SubjectApi();
let identifier = "identifier_example"; // String | The identifier path of the `subject` you're looking for 
apiInstance.getSubject(identifier, (error, data, response) => {
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
 **identifier** | **String**| The identifier path of the &#x60;subject&#x60; you&#39;re looking for  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

