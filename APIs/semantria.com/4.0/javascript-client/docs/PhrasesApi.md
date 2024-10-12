# Semantria.PhrasesApi

All URIs are relative to *https://api.semantria.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addPhrases**](PhrasesApi.md#addPhrases) | **POST** /phrases.{content_type} | Add sentiment-bearing phrases
[**deletePhrases**](PhrasesApi.md#deletePhrases) | **DELETE** /phrases.{content_type} | Remove sentiment-bearing phrases
[**getPhrases**](PhrasesApi.md#getPhrases) | **GET** /phrases.{content_type} | Retrieve sentiment-bearing phrases
[**updatePhrases**](PhrasesApi.md#updatePhrases) | **PUT** /phrases.{content_type} | Updates sentiment-bearing phrases



## addPhrases

> [PhraseResponseVersion] addPhrases(contentType, sentimentPhrases, opts)

Add sentiment-bearing phrases

This method adds sentiment-bearing phrases on Semantria side.

### Example

```javascript
import Semantria from 'semantria';

let apiInstance = new Semantria.PhrasesApi();
let contentType = "contentType_example"; // String | 
let sentimentPhrases = {key: null}; // Object | List of parametrized JSON or XML objects.
let opts = {
  'configId': "configId_example" // String | Identifier of configuration phrases linked to.
};
apiInstance.addPhrases(contentType, sentimentPhrases, opts, (error, data, response) => {
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
 **contentType** | **String**|  | 
 **sentimentPhrases** | **Object**| List of parametrized JSON or XML objects. | 
 **configId** | **String**| Identifier of configuration phrases linked to. | [optional] 

### Return type

[**[PhraseResponseVersion]**](PhraseResponseVersion.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## deletePhrases

> deletePhrases(contentType, sentimentPhraseIDs, opts)

Remove sentiment-bearing phrases

This method removes certain sentiment-bearing phrases by their names on Semantria side.

### Example

```javascript
import Semantria from 'semantria';

let apiInstance = new Semantria.PhrasesApi();
let contentType = "contentType_example"; // String | 
let sentimentPhraseIDs = ["null"]; // [String] | List of sentiment-bearing phrase identifiers.
let opts = {
  'configId': "configId_example" // String | Identifier of configuration phrases linked to.
};
apiInstance.deletePhrases(contentType, sentimentPhraseIDs, opts, (error, data, response) => {
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
 **contentType** | **String**|  | 
 **sentimentPhraseIDs** | [**[String]**](String.md)| List of sentiment-bearing phrase identifiers. | 
 **configId** | **String**| Identifier of configuration phrases linked to. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getPhrases

> [PhraseResponseVersion] getPhrases(contentType, opts)

Retrieve sentiment-bearing phrases

This method retrieves list of sentiment-bearing phrases available on Semantria side.

### Example

```javascript
import Semantria from 'semantria';

let apiInstance = new Semantria.PhrasesApi();
let contentType = "contentType_example"; // String | 
let opts = {
  'configId': "configId_example" // String | Identifier of configuration phrases linked to.
};
apiInstance.getPhrases(contentType, opts, (error, data, response) => {
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
 **contentType** | **String**|  | 
 **configId** | **String**| Identifier of configuration phrases linked to. | [optional] 

### Return type

[**[PhraseResponseVersion]**](PhraseResponseVersion.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## updatePhrases

> [PhraseResponseVersion] updatePhrases(contentType, sentimentPhrases, opts)

Updates sentiment-bearing phrases

This method updates sentiment-bearing phrases by unique IDs on Semantria side.

### Example

```javascript
import Semantria from 'semantria';

let apiInstance = new Semantria.PhrasesApi();
let contentType = "contentType_example"; // String | 
let sentimentPhrases = {key: null}; // Object | List of parametrized JSON or XML objects.
let opts = {
  'configId': "configId_example" // String | Identifier of configuration phrases linked to.
};
apiInstance.updatePhrases(contentType, sentimentPhrases, opts, (error, data, response) => {
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
 **contentType** | **String**|  | 
 **sentimentPhrases** | **Object**| List of parametrized JSON or XML objects. | 
 **configId** | **String**| Identifier of configuration phrases linked to. | [optional] 

### Return type

[**[PhraseResponseVersion]**](PhraseResponseVersion.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

