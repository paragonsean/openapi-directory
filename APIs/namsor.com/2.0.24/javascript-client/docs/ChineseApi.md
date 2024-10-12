# NamSorApiV2.ChineseApi

All URIs are relative to *https://v2.namsor.com/NamSorAPIv2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**chineseNameCandidates**](ChineseApi.md#chineseNameCandidates) | **GET** /api2/json/chineseNameCandidates/{chineseSurnameLatin}/{chineseGivenNameLatin} | Identify Chinese name candidates, based on the romanized name ex. Wang Xiaoming
[**chineseNameCandidatesBatch**](ChineseApi.md#chineseNameCandidatesBatch) | **POST** /api2/json/chineseNameCandidatesBatch | Identify Chinese name candidates, based on the romanized name (firstName &#x3D; chineseGivenName; lastName&#x3D;chineseSurname), ex. Wang Xiaoming
[**chineseNameCandidatesGenderBatch**](ChineseApi.md#chineseNameCandidatesGenderBatch) | **POST** /api2/json/chineseNameCandidatesGenderBatch | Identify Chinese name candidates, based on the romanized name (firstName &#x3D; chineseGivenName; lastName&#x3D;chineseSurname) ex. Wang Xiaoming.
[**chineseNameGenderCandidates**](ChineseApi.md#chineseNameGenderCandidates) | **GET** /api2/json/chineseNameGenderCandidates/{chineseSurnameLatin}/{chineseGivenNameLatin}/{knownGender} | Identify Chinese name candidates, based on the romanized name ex. Wang Xiaoming - having a known gender (&#39;male&#39; or &#39;female&#39;)
[**chineseNameMatch**](ChineseApi.md#chineseNameMatch) | **GET** /api2/json/chineseNameMatch/{chineseSurnameLatin}/{chineseGivenNameLatin}/{chineseName} | Return a score for matching Chinese name ex. 王晓明 with a romanized name ex. Wang Xiaoming
[**chineseNameMatchBatch**](ChineseApi.md#chineseNameMatchBatch) | **POST** /api2/json/chineseNameMatchBatch | Identify Chinese name candidates, based on the romanized name (firstName &#x3D; chineseGivenName; lastName&#x3D;chineseSurname), ex. Wang Xiaoming
[**genderChineseName**](ChineseApi.md#genderChineseName) | **GET** /api2/json/genderChineseName/{chineseName} | Infer the likely gender of a Chinese full name ex. 王晓明
[**genderChineseNameBatch**](ChineseApi.md#genderChineseNameBatch) | **POST** /api2/json/genderChineseNameBatch | Infer the likely gender of up to 100 full names ex. 王晓明
[**genderChineseNamePinyin**](ChineseApi.md#genderChineseNamePinyin) | **GET** /api2/json/genderChineseNamePinyin/{chineseSurnameLatin}/{chineseGivenNameLatin} | Infer the likely gender of a Chinese name in LATIN (Pinyin).
[**genderChineseNamePinyinBatch**](ChineseApi.md#genderChineseNamePinyinBatch) | **POST** /api2/json/genderChineseNamePinyinBatch | Infer the likely gender of up to 100 Chinese names in LATIN (Pinyin).
[**parseChineseName**](ChineseApi.md#parseChineseName) | **GET** /api2/json/parseChineseName/{chineseName} | Infer the likely first/last name structure of a name, ex. 王晓明 -&gt; 王(surname) 晓明(given name)
[**parseChineseNameBatch**](ChineseApi.md#parseChineseNameBatch) | **POST** /api2/json/parseChineseNameBatch | Infer the likely first/last name structure of a name, ex. 王晓明 -&gt; 王(surname) 晓明(given name).
[**pinyinChineseName**](ChineseApi.md#pinyinChineseName) | **GET** /api2/json/pinyinChineseName/{chineseName} | Romanize the Chinese name to Pinyin, ex. 王晓明 -&gt; Wang (surname) Xiaoming (given name)
[**pinyinChineseNameBatch**](ChineseApi.md#pinyinChineseNameBatch) | **POST** /api2/json/pinyinChineseNameBatch | Romanize a list of Chinese name to Pinyin, ex. 王晓明 -&gt; Wang (surname) Xiaoming (given name).



## chineseNameCandidates

> NameMatchCandidatesOut chineseNameCandidates(chineseSurnameLatin, chineseGivenNameLatin)

Identify Chinese name candidates, based on the romanized name ex. Wang Xiaoming

### Example

```javascript
import NamSorApiV2 from 'nam_sor_api_v2';
let defaultClient = NamSorApiV2.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new NamSorApiV2.ChineseApi();
let chineseSurnameLatin = "chineseSurnameLatin_example"; // String | 
let chineseGivenNameLatin = "chineseGivenNameLatin_example"; // String | 
apiInstance.chineseNameCandidates(chineseSurnameLatin, chineseGivenNameLatin, (error, data, response) => {
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
 **chineseSurnameLatin** | **String**|  | 
 **chineseGivenNameLatin** | **String**|  | 

### Return type

[**NameMatchCandidatesOut**](NameMatchCandidatesOut.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## chineseNameCandidatesBatch

> BatchNameMatchCandidatesOut chineseNameCandidatesBatch(opts)

Identify Chinese name candidates, based on the romanized name (firstName &#x3D; chineseGivenName; lastName&#x3D;chineseSurname), ex. Wang Xiaoming

### Example

```javascript
import NamSorApiV2 from 'nam_sor_api_v2';
let defaultClient = NamSorApiV2.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new NamSorApiV2.ChineseApi();
let opts = {
  'batchFirstLastNameIn': new NamSorApiV2.BatchFirstLastNameIn() // BatchFirstLastNameIn | A list of personal Chinese names in LATIN, firstName = chineseGivenName; lastName=chineseSurname
};
apiInstance.chineseNameCandidatesBatch(opts, (error, data, response) => {
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
 **batchFirstLastNameIn** | [**BatchFirstLastNameIn**](BatchFirstLastNameIn.md)| A list of personal Chinese names in LATIN, firstName &#x3D; chineseGivenName; lastName&#x3D;chineseSurname | [optional] 

### Return type

[**BatchNameMatchCandidatesOut**](BatchNameMatchCandidatesOut.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## chineseNameCandidatesGenderBatch

> BatchNameMatchCandidatesOut chineseNameCandidatesGenderBatch(opts)

Identify Chinese name candidates, based on the romanized name (firstName &#x3D; chineseGivenName; lastName&#x3D;chineseSurname) ex. Wang Xiaoming.

### Example

```javascript
import NamSorApiV2 from 'nam_sor_api_v2';
let defaultClient = NamSorApiV2.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new NamSorApiV2.ChineseApi();
let opts = {
  'batchFirstLastNameGenderIn': new NamSorApiV2.BatchFirstLastNameGenderIn() // BatchFirstLastNameGenderIn | A list of personal Chinese names in LATIN, firstName = chineseGivenName; lastName=chineseSurname
};
apiInstance.chineseNameCandidatesGenderBatch(opts, (error, data, response) => {
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
 **batchFirstLastNameGenderIn** | [**BatchFirstLastNameGenderIn**](BatchFirstLastNameGenderIn.md)| A list of personal Chinese names in LATIN, firstName &#x3D; chineseGivenName; lastName&#x3D;chineseSurname | [optional] 

### Return type

[**BatchNameMatchCandidatesOut**](BatchNameMatchCandidatesOut.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## chineseNameGenderCandidates

> NameMatchCandidatesOut chineseNameGenderCandidates(chineseSurnameLatin, chineseGivenNameLatin, knownGender)

Identify Chinese name candidates, based on the romanized name ex. Wang Xiaoming - having a known gender (&#39;male&#39; or &#39;female&#39;)

### Example

```javascript
import NamSorApiV2 from 'nam_sor_api_v2';
let defaultClient = NamSorApiV2.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new NamSorApiV2.ChineseApi();
let chineseSurnameLatin = "chineseSurnameLatin_example"; // String | 
let chineseGivenNameLatin = "chineseGivenNameLatin_example"; // String | 
let knownGender = "knownGender_example"; // String | 
apiInstance.chineseNameGenderCandidates(chineseSurnameLatin, chineseGivenNameLatin, knownGender, (error, data, response) => {
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
 **chineseSurnameLatin** | **String**|  | 
 **chineseGivenNameLatin** | **String**|  | 
 **knownGender** | **String**|  | 

### Return type

[**NameMatchCandidatesOut**](NameMatchCandidatesOut.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## chineseNameMatch

> NameMatchedOut chineseNameMatch(chineseSurnameLatin, chineseGivenNameLatin, chineseName)

Return a score for matching Chinese name ex. 王晓明 with a romanized name ex. Wang Xiaoming

### Example

```javascript
import NamSorApiV2 from 'nam_sor_api_v2';
let defaultClient = NamSorApiV2.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new NamSorApiV2.ChineseApi();
let chineseSurnameLatin = "chineseSurnameLatin_example"; // String | 
let chineseGivenNameLatin = "chineseGivenNameLatin_example"; // String | 
let chineseName = "chineseName_example"; // String | 
apiInstance.chineseNameMatch(chineseSurnameLatin, chineseGivenNameLatin, chineseName, (error, data, response) => {
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
 **chineseSurnameLatin** | **String**|  | 
 **chineseGivenNameLatin** | **String**|  | 
 **chineseName** | **String**|  | 

### Return type

[**NameMatchedOut**](NameMatchedOut.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## chineseNameMatchBatch

> BatchNameMatchedOut chineseNameMatchBatch(opts)

Identify Chinese name candidates, based on the romanized name (firstName &#x3D; chineseGivenName; lastName&#x3D;chineseSurname), ex. Wang Xiaoming

### Example

```javascript
import NamSorApiV2 from 'nam_sor_api_v2';
let defaultClient = NamSorApiV2.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new NamSorApiV2.ChineseApi();
let opts = {
  'batchMatchPersonalFirstLastNameIn': new NamSorApiV2.BatchMatchPersonalFirstLastNameIn() // BatchMatchPersonalFirstLastNameIn | A list of personal Chinese names in LATIN, firstName = chineseGivenName; lastName=chineseSurname
};
apiInstance.chineseNameMatchBatch(opts, (error, data, response) => {
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
 **batchMatchPersonalFirstLastNameIn** | [**BatchMatchPersonalFirstLastNameIn**](BatchMatchPersonalFirstLastNameIn.md)| A list of personal Chinese names in LATIN, firstName &#x3D; chineseGivenName; lastName&#x3D;chineseSurname | [optional] 

### Return type

[**BatchNameMatchedOut**](BatchNameMatchedOut.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## genderChineseName

> PersonalNameGenderedOut genderChineseName(chineseName)

Infer the likely gender of a Chinese full name ex. 王晓明

### Example

```javascript
import NamSorApiV2 from 'nam_sor_api_v2';
let defaultClient = NamSorApiV2.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new NamSorApiV2.ChineseApi();
let chineseName = "chineseName_example"; // String | 
apiInstance.genderChineseName(chineseName, (error, data, response) => {
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
 **chineseName** | **String**|  | 

### Return type

[**PersonalNameGenderedOut**](PersonalNameGenderedOut.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## genderChineseNameBatch

> BatchPersonalNameGenderedOut genderChineseNameBatch(opts)

Infer the likely gender of up to 100 full names ex. 王晓明

### Example

```javascript
import NamSorApiV2 from 'nam_sor_api_v2';
let defaultClient = NamSorApiV2.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new NamSorApiV2.ChineseApi();
let opts = {
  'batchPersonalNameIn': new NamSorApiV2.BatchPersonalNameIn() // BatchPersonalNameIn | A list of personal names, with a country ISO2 code
};
apiInstance.genderChineseNameBatch(opts, (error, data, response) => {
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
 **batchPersonalNameIn** | [**BatchPersonalNameIn**](BatchPersonalNameIn.md)| A list of personal names, with a country ISO2 code | [optional] 

### Return type

[**BatchPersonalNameGenderedOut**](BatchPersonalNameGenderedOut.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## genderChineseNamePinyin

> FirstLastNameGenderedOut genderChineseNamePinyin(chineseSurnameLatin, chineseGivenNameLatin)

Infer the likely gender of a Chinese name in LATIN (Pinyin).

### Example

```javascript
import NamSorApiV2 from 'nam_sor_api_v2';
let defaultClient = NamSorApiV2.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new NamSorApiV2.ChineseApi();
let chineseSurnameLatin = "chineseSurnameLatin_example"; // String | 
let chineseGivenNameLatin = "chineseGivenNameLatin_example"; // String | 
apiInstance.genderChineseNamePinyin(chineseSurnameLatin, chineseGivenNameLatin, (error, data, response) => {
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
 **chineseSurnameLatin** | **String**|  | 
 **chineseGivenNameLatin** | **String**|  | 

### Return type

[**FirstLastNameGenderedOut**](FirstLastNameGenderedOut.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## genderChineseNamePinyinBatch

> BatchFirstLastNameGenderedOut genderChineseNamePinyinBatch(opts)

Infer the likely gender of up to 100 Chinese names in LATIN (Pinyin).

### Example

```javascript
import NamSorApiV2 from 'nam_sor_api_v2';
let defaultClient = NamSorApiV2.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new NamSorApiV2.ChineseApi();
let opts = {
  'batchFirstLastNameIn': new NamSorApiV2.BatchFirstLastNameIn() // BatchFirstLastNameIn | A list of names, with country code.
};
apiInstance.genderChineseNamePinyinBatch(opts, (error, data, response) => {
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
 **batchFirstLastNameIn** | [**BatchFirstLastNameIn**](BatchFirstLastNameIn.md)| A list of names, with country code. | [optional] 

### Return type

[**BatchFirstLastNameGenderedOut**](BatchFirstLastNameGenderedOut.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## parseChineseName

> PersonalNameParsedOut parseChineseName(chineseName)

Infer the likely first/last name structure of a name, ex. 王晓明 -&gt; 王(surname) 晓明(given name)

### Example

```javascript
import NamSorApiV2 from 'nam_sor_api_v2';
let defaultClient = NamSorApiV2.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new NamSorApiV2.ChineseApi();
let chineseName = "chineseName_example"; // String | 
apiInstance.parseChineseName(chineseName, (error, data, response) => {
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
 **chineseName** | **String**|  | 

### Return type

[**PersonalNameParsedOut**](PersonalNameParsedOut.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## parseChineseNameBatch

> BatchPersonalNameParsedOut parseChineseNameBatch(opts)

Infer the likely first/last name structure of a name, ex. 王晓明 -&gt; 王(surname) 晓明(given name).

### Example

```javascript
import NamSorApiV2 from 'nam_sor_api_v2';
let defaultClient = NamSorApiV2.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new NamSorApiV2.ChineseApi();
let opts = {
  'batchPersonalNameIn': new NamSorApiV2.BatchPersonalNameIn() // BatchPersonalNameIn | A list of personal names
};
apiInstance.parseChineseNameBatch(opts, (error, data, response) => {
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
 **batchPersonalNameIn** | [**BatchPersonalNameIn**](BatchPersonalNameIn.md)| A list of personal names | [optional] 

### Return type

[**BatchPersonalNameParsedOut**](BatchPersonalNameParsedOut.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## pinyinChineseName

> PersonalNameParsedOut pinyinChineseName(chineseName)

Romanize the Chinese name to Pinyin, ex. 王晓明 -&gt; Wang (surname) Xiaoming (given name)

### Example

```javascript
import NamSorApiV2 from 'nam_sor_api_v2';
let defaultClient = NamSorApiV2.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new NamSorApiV2.ChineseApi();
let chineseName = "chineseName_example"; // String | 
apiInstance.pinyinChineseName(chineseName, (error, data, response) => {
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
 **chineseName** | **String**|  | 

### Return type

[**PersonalNameParsedOut**](PersonalNameParsedOut.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## pinyinChineseNameBatch

> BatchPersonalNameParsedOut pinyinChineseNameBatch(opts)

Romanize a list of Chinese name to Pinyin, ex. 王晓明 -&gt; Wang (surname) Xiaoming (given name).

### Example

```javascript
import NamSorApiV2 from 'nam_sor_api_v2';
let defaultClient = NamSorApiV2.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new NamSorApiV2.ChineseApi();
let opts = {
  'batchPersonalNameIn': new NamSorApiV2.BatchPersonalNameIn() // BatchPersonalNameIn | A list of Chinese names
};
apiInstance.pinyinChineseNameBatch(opts, (error, data, response) => {
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
 **batchPersonalNameIn** | [**BatchPersonalNameIn**](BatchPersonalNameIn.md)| A list of Chinese names | [optional] 

### Return type

[**BatchPersonalNameParsedOut**](BatchPersonalNameParsedOut.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

