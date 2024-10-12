# Healthcare.DefaultApi

All URIs are relative to *https://www.healthcare.gov*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiArticlesmediaTypeExtensionGet**](DefaultApi.md#apiArticlesmediaTypeExtensionGet) | **GET** /api/articles{mediaTypeExtension} | 
[**apiBlogmediaTypeExtensionGet**](DefaultApi.md#apiBlogmediaTypeExtensionGet) | **GET** /api/blog{mediaTypeExtension} | 
[**apiGlossarymediaTypeExtensionGet**](DefaultApi.md#apiGlossarymediaTypeExtensionGet) | **GET** /api/glossary{mediaTypeExtension} | 
[**apiQuestionsmediaTypeExtensionGet**](DefaultApi.md#apiQuestionsmediaTypeExtensionGet) | **GET** /api/questions{mediaTypeExtension} | 
[**apiStatesmediaTypeExtensionGet**](DefaultApi.md#apiStatesmediaTypeExtensionGet) | **GET** /api/states{mediaTypeExtension} | 
[**apiTopicsmediaTypeExtensionGet**](DefaultApi.md#apiTopicsmediaTypeExtensionGet) | **GET** /api/topics{mediaTypeExtension} | 
[**blogPageNamemediaTypeExtensionGet**](DefaultApi.md#blogPageNamemediaTypeExtensionGet) | **GET** /blog/{pageName}{mediaTypeExtension} | 
[**esBlogPageNamemediaTypeExtensionGet**](DefaultApi.md#esBlogPageNamemediaTypeExtensionGet) | **GET** /es/blog/{pageName}{mediaTypeExtension} | 
[**esGlossaryPageNamemediaTypeExtensionGet**](DefaultApi.md#esGlossaryPageNamemediaTypeExtensionGet) | **GET** /es/glossary/{pageName}{mediaTypeExtension} | 
[**esPageNamemediaTypeExtensionGet**](DefaultApi.md#esPageNamemediaTypeExtensionGet) | **GET** /es/{pageName}{mediaTypeExtension} | 
[**esQuestionPageNamemediaTypeExtensionGet**](DefaultApi.md#esQuestionPageNamemediaTypeExtensionGet) | **GET** /es/question/{pageName}{mediaTypeExtension} | 
[**esStateNamemediaTypeExtensionGet**](DefaultApi.md#esStateNamemediaTypeExtensionGet) | **GET** /es/{stateName}{mediaTypeExtension} | 
[**glossaryPageNamemediaTypeExtensionGet**](DefaultApi.md#glossaryPageNamemediaTypeExtensionGet) | **GET** /glossary/{pageName}{mediaTypeExtension} | 
[**pageNamemediaTypeExtensionGet**](DefaultApi.md#pageNamemediaTypeExtensionGet) | **GET** /{pageName}{mediaTypeExtension} | 
[**questionPageNamemediaTypeExtensionGet**](DefaultApi.md#questionPageNamemediaTypeExtensionGet) | **GET** /question/{pageName}{mediaTypeExtension} | 
[**stateNamemediaTypeExtensionGet**](DefaultApi.md#stateNamemediaTypeExtensionGet) | **GET** /{stateName}{mediaTypeExtension} | 



## apiArticlesmediaTypeExtensionGet

> ArticlesList apiArticlesmediaTypeExtensionGet(mediaTypeExtension)



Returns pages content.

### Example

```javascript
import Healthcare from 'healthcare';

let apiInstance = new Healthcare.DefaultApi();
let mediaTypeExtension = "mediaTypeExtension_example"; // String | Omiting the param causes html to be returned.
apiInstance.apiArticlesmediaTypeExtensionGet(mediaTypeExtension, (error, data, response) => {
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
 **mediaTypeExtension** | **String**| Omiting the param causes html to be returned. | 

### Return type

[**ArticlesList**](ArticlesList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## apiBlogmediaTypeExtensionGet

> BlogList apiBlogmediaTypeExtensionGet(mediaTypeExtension)



Returns pages content.

### Example

```javascript
import Healthcare from 'healthcare';

let apiInstance = new Healthcare.DefaultApi();
let mediaTypeExtension = "mediaTypeExtension_example"; // String | Omiting the param causes html to be returned.
apiInstance.apiBlogmediaTypeExtensionGet(mediaTypeExtension, (error, data, response) => {
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
 **mediaTypeExtension** | **String**| Omiting the param causes html to be returned. | 

### Return type

[**BlogList**](BlogList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## apiGlossarymediaTypeExtensionGet

> GlossaryList apiGlossarymediaTypeExtensionGet(mediaTypeExtension)



Returns pages content.

### Example

```javascript
import Healthcare from 'healthcare';

let apiInstance = new Healthcare.DefaultApi();
let mediaTypeExtension = "mediaTypeExtension_example"; // String | Omiting the param causes html to be returned.
apiInstance.apiGlossarymediaTypeExtensionGet(mediaTypeExtension, (error, data, response) => {
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
 **mediaTypeExtension** | **String**| Omiting the param causes html to be returned. | 

### Return type

[**GlossaryList**](GlossaryList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## apiQuestionsmediaTypeExtensionGet

> QuestionsList apiQuestionsmediaTypeExtensionGet(mediaTypeExtension)



Returns pages content.

### Example

```javascript
import Healthcare from 'healthcare';

let apiInstance = new Healthcare.DefaultApi();
let mediaTypeExtension = "mediaTypeExtension_example"; // String | Omiting the param causes html to be returned.
apiInstance.apiQuestionsmediaTypeExtensionGet(mediaTypeExtension, (error, data, response) => {
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
 **mediaTypeExtension** | **String**| Omiting the param causes html to be returned. | 

### Return type

[**QuestionsList**](QuestionsList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## apiStatesmediaTypeExtensionGet

> StatesList apiStatesmediaTypeExtensionGet(mediaTypeExtension)



Returns pages content.

### Example

```javascript
import Healthcare from 'healthcare';

let apiInstance = new Healthcare.DefaultApi();
let mediaTypeExtension = "mediaTypeExtension_example"; // String | Omiting the param causes html to be returned.
apiInstance.apiStatesmediaTypeExtensionGet(mediaTypeExtension, (error, data, response) => {
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
 **mediaTypeExtension** | **String**| Omiting the param causes html to be returned. | 

### Return type

[**StatesList**](StatesList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## apiTopicsmediaTypeExtensionGet

> TopicsList apiTopicsmediaTypeExtensionGet(mediaTypeExtension)



Returns pages content.

### Example

```javascript
import Healthcare from 'healthcare';

let apiInstance = new Healthcare.DefaultApi();
let mediaTypeExtension = "mediaTypeExtension_example"; // String | Omiting the param causes html to be returned.
apiInstance.apiTopicsmediaTypeExtensionGet(mediaTypeExtension, (error, data, response) => {
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
 **mediaTypeExtension** | **String**| Omiting the param causes html to be returned. | 

### Return type

[**TopicsList**](TopicsList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## blogPageNamemediaTypeExtensionGet

> BlogPage blogPageNamemediaTypeExtensionGet(mediaTypeExtension, pageName)



Returns pages content.

### Example

```javascript
import Healthcare from 'healthcare';

let apiInstance = new Healthcare.DefaultApi();
let mediaTypeExtension = "mediaTypeExtension_example"; // String | Omiting the param causes html to be returned.
let pageName = "pageName_example"; // String | 
apiInstance.blogPageNamemediaTypeExtensionGet(mediaTypeExtension, pageName, (error, data, response) => {
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
 **mediaTypeExtension** | **String**| Omiting the param causes html to be returned. | 
 **pageName** | **String**|  | 

### Return type

[**BlogPage**](BlogPage.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/html


## esBlogPageNamemediaTypeExtensionGet

> BlogPage esBlogPageNamemediaTypeExtensionGet(mediaTypeExtension, pageName)



Returns pages content.

### Example

```javascript
import Healthcare from 'healthcare';

let apiInstance = new Healthcare.DefaultApi();
let mediaTypeExtension = "mediaTypeExtension_example"; // String | Omiting the param causes html to be returned.
let pageName = "pageName_example"; // String | 
apiInstance.esBlogPageNamemediaTypeExtensionGet(mediaTypeExtension, pageName, (error, data, response) => {
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
 **mediaTypeExtension** | **String**| Omiting the param causes html to be returned. | 
 **pageName** | **String**|  | 

### Return type

[**BlogPage**](BlogPage.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/html


## esGlossaryPageNamemediaTypeExtensionGet

> GlossaryPage esGlossaryPageNamemediaTypeExtensionGet(mediaTypeExtension, pageName)



Returns pages content.

### Example

```javascript
import Healthcare from 'healthcare';

let apiInstance = new Healthcare.DefaultApi();
let mediaTypeExtension = "mediaTypeExtension_example"; // String | Omiting the param causes html to be returned.
let pageName = "pageName_example"; // String | 
apiInstance.esGlossaryPageNamemediaTypeExtensionGet(mediaTypeExtension, pageName, (error, data, response) => {
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
 **mediaTypeExtension** | **String**| Omiting the param causes html to be returned. | 
 **pageName** | **String**|  | 

### Return type

[**GlossaryPage**](GlossaryPage.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/html


## esPageNamemediaTypeExtensionGet

> Page esPageNamemediaTypeExtensionGet(mediaTypeExtension, pageName)



Returns pages content.

### Example

```javascript
import Healthcare from 'healthcare';

let apiInstance = new Healthcare.DefaultApi();
let mediaTypeExtension = "mediaTypeExtension_example"; // String | Omiting the param causes html to be returned.
let pageName = "pageName_example"; // String | 
apiInstance.esPageNamemediaTypeExtensionGet(mediaTypeExtension, pageName, (error, data, response) => {
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
 **mediaTypeExtension** | **String**| Omiting the param causes html to be returned. | 
 **pageName** | **String**|  | 

### Return type

[**Page**](Page.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/html


## esQuestionPageNamemediaTypeExtensionGet

> QuestionPage esQuestionPageNamemediaTypeExtensionGet(mediaTypeExtension, pageName)



Returns pages content.

### Example

```javascript
import Healthcare from 'healthcare';

let apiInstance = new Healthcare.DefaultApi();
let mediaTypeExtension = "mediaTypeExtension_example"; // String | Omiting the param causes html to be returned.
let pageName = "pageName_example"; // String | 
apiInstance.esQuestionPageNamemediaTypeExtensionGet(mediaTypeExtension, pageName, (error, data, response) => {
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
 **mediaTypeExtension** | **String**| Omiting the param causes html to be returned. | 
 **pageName** | **String**|  | 

### Return type

[**QuestionPage**](QuestionPage.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## esStateNamemediaTypeExtensionGet

> StatePage esStateNamemediaTypeExtensionGet(mediaTypeExtension, stateName)



Returns pages content.

### Example

```javascript
import Healthcare from 'healthcare';

let apiInstance = new Healthcare.DefaultApi();
let mediaTypeExtension = "mediaTypeExtension_example"; // String | Omiting the param causes html to be returned.
let stateName = "stateName_example"; // String | 
apiInstance.esStateNamemediaTypeExtensionGet(mediaTypeExtension, stateName, (error, data, response) => {
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
 **mediaTypeExtension** | **String**| Omiting the param causes html to be returned. | 
 **stateName** | **String**|  | 

### Return type

[**StatePage**](StatePage.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## glossaryPageNamemediaTypeExtensionGet

> GlossaryPage glossaryPageNamemediaTypeExtensionGet(mediaTypeExtension, pageName)



Returns pages content.

### Example

```javascript
import Healthcare from 'healthcare';

let apiInstance = new Healthcare.DefaultApi();
let mediaTypeExtension = "mediaTypeExtension_example"; // String | Omiting the param causes html to be returned.
let pageName = "pageName_example"; // String | 
apiInstance.glossaryPageNamemediaTypeExtensionGet(mediaTypeExtension, pageName, (error, data, response) => {
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
 **mediaTypeExtension** | **String**| Omiting the param causes html to be returned. | 
 **pageName** | **String**|  | 

### Return type

[**GlossaryPage**](GlossaryPage.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/html


## pageNamemediaTypeExtensionGet

> Page pageNamemediaTypeExtensionGet(mediaTypeExtension, pageName)



Returns pages content.

### Example

```javascript
import Healthcare from 'healthcare';

let apiInstance = new Healthcare.DefaultApi();
let mediaTypeExtension = "mediaTypeExtension_example"; // String | Omiting the param causes html to be returned.
let pageName = "pageName_example"; // String | 
apiInstance.pageNamemediaTypeExtensionGet(mediaTypeExtension, pageName, (error, data, response) => {
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
 **mediaTypeExtension** | **String**| Omiting the param causes html to be returned. | 
 **pageName** | **String**|  | 

### Return type

[**Page**](Page.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/html


## questionPageNamemediaTypeExtensionGet

> QuestionPage questionPageNamemediaTypeExtensionGet(mediaTypeExtension, pageName)



Returns pages content.

### Example

```javascript
import Healthcare from 'healthcare';

let apiInstance = new Healthcare.DefaultApi();
let mediaTypeExtension = "mediaTypeExtension_example"; // String | Omiting the param causes html to be returned.
let pageName = "pageName_example"; // String | 
apiInstance.questionPageNamemediaTypeExtensionGet(mediaTypeExtension, pageName, (error, data, response) => {
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
 **mediaTypeExtension** | **String**| Omiting the param causes html to be returned. | 
 **pageName** | **String**|  | 

### Return type

[**QuestionPage**](QuestionPage.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## stateNamemediaTypeExtensionGet

> StatePage stateNamemediaTypeExtensionGet(mediaTypeExtension, stateName)



Returns pages content.

### Example

```javascript
import Healthcare from 'healthcare';

let apiInstance = new Healthcare.DefaultApi();
let mediaTypeExtension = "mediaTypeExtension_example"; // String | Omiting the param causes html to be returned.
let stateName = "stateName_example"; // String | 
apiInstance.stateNamemediaTypeExtensionGet(mediaTypeExtension, stateName, (error, data, response) => {
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
 **mediaTypeExtension** | **String**| Omiting the param causes html to be returned. | 
 **stateName** | **String**|  | 

### Return type

[**StatePage**](StatePage.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

