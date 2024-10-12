# OpenApiDefinition.PeoplegeneratorapiApplicationApi

All URIs are relative to *http://peoplegeneratorapi.live*

Method | HTTP request | Description
------------- | ------------- | -------------
[**age**](PeoplegeneratorapiApplicationApi.md#age) | **GET** /api/person/age/ | 
[**age1**](PeoplegeneratorapiApplicationApi.md#age1) | **GET** /api/person/age | 
[**bloodtype**](PeoplegeneratorapiApplicationApi.md#bloodtype) | **GET** /api/person/bloodtype/ | 
[**bloodtype1**](PeoplegeneratorapiApplicationApi.md#bloodtype1) | **GET** /api/person/bloodtype | 
[**creditcardnumber**](PeoplegeneratorapiApplicationApi.md#creditcardnumber) | **GET** /api/person/creditcardnumber | 
[**creditcardnumber1**](PeoplegeneratorapiApplicationApi.md#creditcardnumber1) | **GET** /api/person/creditcardnumber/ | 
[**creditscore**](PeoplegeneratorapiApplicationApi.md#creditscore) | **GET** /api/person/creditscore/ | 
[**creditscore1**](PeoplegeneratorapiApplicationApi.md#creditscore1) | **GET** /api/person/creditscore | 
[**email**](PeoplegeneratorapiApplicationApi.md#email) | **GET** /api/person/email | 
[**email1**](PeoplegeneratorapiApplicationApi.md#email1) | **GET** /api/person/email/ | 
[**eyecolor**](PeoplegeneratorapiApplicationApi.md#eyecolor) | **GET** /api/person/eyecolor/ | 
[**eyecolor1**](PeoplegeneratorapiApplicationApi.md#eyecolor1) | **GET** /api/person/eyecolor | 
[**gender**](PeoplegeneratorapiApplicationApi.md#gender) | **GET** /api/person/gender | 
[**gender1**](PeoplegeneratorapiApplicationApi.md#gender1) | **GET** /api/person/gender/ | 
[**generateAddress**](PeoplegeneratorapiApplicationApi.md#generateAddress) | **GET** /api/address | 
[**generateAddress1**](PeoplegeneratorapiApplicationApi.md#generateAddress1) | **GET** /api/address/ | 
[**generateLifeStory**](PeoplegeneratorapiApplicationApi.md#generateLifeStory) | **GET** /api/lifestory/ | 
[**generateLifeStory1**](PeoplegeneratorapiApplicationApi.md#generateLifeStory1) | **GET** /api/lifestory | 
[**getCompressedPerson**](PeoplegeneratorapiApplicationApi.md#getCompressedPerson) | **GET** /api/person/{number}/ | 
[**getCompressedPerson1**](PeoplegeneratorapiApplicationApi.md#getCompressedPerson1) | **GET** /api/person/{number} | 
[**getPerson**](PeoplegeneratorapiApplicationApi.md#getPerson) | **GET** /api/person/ | 
[**getPerson1**](PeoplegeneratorapiApplicationApi.md#getPerson1) | **GET** /api/person | 
[**gpa**](PeoplegeneratorapiApplicationApi.md#gpa) | **GET** /api/person/gpa | 
[**gpa1**](PeoplegeneratorapiApplicationApi.md#gpa1) | **GET** /api/person/gpa/ | 
[**haschildren**](PeoplegeneratorapiApplicationApi.md#haschildren) | **GET** /api/person/haschildren/ | 
[**haschildren1**](PeoplegeneratorapiApplicationApi.md#haschildren1) | **GET** /api/person/haschildren | 
[**hasdegree**](PeoplegeneratorapiApplicationApi.md#hasdegree) | **GET** /api/person/hasdegree | 
[**hasdegree1**](PeoplegeneratorapiApplicationApi.md#hasdegree1) | **GET** /api/person/hasdegree/ | 
[**height**](PeoplegeneratorapiApplicationApi.md#height) | **GET** /api/person/height | 
[**height1**](PeoplegeneratorapiApplicationApi.md#height1) | **GET** /api/person/height/ | 
[**income**](PeoplegeneratorapiApplicationApi.md#income) | **GET** /api/person/income | 
[**income1**](PeoplegeneratorapiApplicationApi.md#income1) | **GET** /api/person/income/ | 
[**job**](PeoplegeneratorapiApplicationApi.md#job) | **GET** /api/person/job | 
[**job1**](PeoplegeneratorapiApplicationApi.md#job1) | **GET** /api/person/job/ | 
[**maritalstatus**](PeoplegeneratorapiApplicationApi.md#maritalstatus) | **GET** /api/person/maritalstatus/ | 
[**maritalstatus1**](PeoplegeneratorapiApplicationApi.md#maritalstatus1) | **GET** /api/person/maritalstatus | 
[**name**](PeoplegeneratorapiApplicationApi.md#name) | **GET** /api/person/name/ | 
[**name1**](PeoplegeneratorapiApplicationApi.md#name1) | **GET** /api/person/name | 
[**politicalLeaning**](PeoplegeneratorapiApplicationApi.md#politicalLeaning) | **GET** /api/person/politicalleaning | 
[**politicalLeaning1**](PeoplegeneratorapiApplicationApi.md#politicalLeaning1) | **GET** /api/person/politicalleaning/ | 
[**religion**](PeoplegeneratorapiApplicationApi.md#religion) | **GET** /api/person/religion/ | 
[**religion1**](PeoplegeneratorapiApplicationApi.md#religion1) | **GET** /api/person/religion | 
[**username**](PeoplegeneratorapiApplicationApi.md#username) | **GET** /api/person/username/ | 
[**username1**](PeoplegeneratorapiApplicationApi.md#username1) | **GET** /api/person/username | 
[**weight**](PeoplegeneratorapiApplicationApi.md#weight) | **GET** /api/person/weight | 
[**weight1**](PeoplegeneratorapiApplicationApi.md#weight1) | **GET** /api/person/weight/ | 



## age

> Number age()



### Example

```javascript
import OpenApiDefinition from 'open_api_definition';

let apiInstance = new OpenApiDefinition.PeoplegeneratorapiApplicationApi();
apiInstance.age((error, data, response) => {
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

**Number**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## age1

> Number age1()



### Example

```javascript
import OpenApiDefinition from 'open_api_definition';

let apiInstance = new OpenApiDefinition.PeoplegeneratorapiApplicationApi();
apiInstance.age1((error, data, response) => {
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

**Number**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## bloodtype

> String bloodtype()



### Example

```javascript
import OpenApiDefinition from 'open_api_definition';

let apiInstance = new OpenApiDefinition.PeoplegeneratorapiApplicationApi();
apiInstance.bloodtype((error, data, response) => {
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
- **Accept**: */*


## bloodtype1

> String bloodtype1()



### Example

```javascript
import OpenApiDefinition from 'open_api_definition';

let apiInstance = new OpenApiDefinition.PeoplegeneratorapiApplicationApi();
apiInstance.bloodtype1((error, data, response) => {
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
- **Accept**: */*


## creditcardnumber

> String creditcardnumber()



### Example

```javascript
import OpenApiDefinition from 'open_api_definition';

let apiInstance = new OpenApiDefinition.PeoplegeneratorapiApplicationApi();
apiInstance.creditcardnumber((error, data, response) => {
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
- **Accept**: */*


## creditcardnumber1

> String creditcardnumber1()



### Example

```javascript
import OpenApiDefinition from 'open_api_definition';

let apiInstance = new OpenApiDefinition.PeoplegeneratorapiApplicationApi();
apiInstance.creditcardnumber1((error, data, response) => {
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
- **Accept**: */*


## creditscore

> Number creditscore()



### Example

```javascript
import OpenApiDefinition from 'open_api_definition';

let apiInstance = new OpenApiDefinition.PeoplegeneratorapiApplicationApi();
apiInstance.creditscore((error, data, response) => {
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

**Number**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## creditscore1

> Number creditscore1()



### Example

```javascript
import OpenApiDefinition from 'open_api_definition';

let apiInstance = new OpenApiDefinition.PeoplegeneratorapiApplicationApi();
apiInstance.creditscore1((error, data, response) => {
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

**Number**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## email

> String email()



### Example

```javascript
import OpenApiDefinition from 'open_api_definition';

let apiInstance = new OpenApiDefinition.PeoplegeneratorapiApplicationApi();
apiInstance.email((error, data, response) => {
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
- **Accept**: */*


## email1

> String email1()



### Example

```javascript
import OpenApiDefinition from 'open_api_definition';

let apiInstance = new OpenApiDefinition.PeoplegeneratorapiApplicationApi();
apiInstance.email1((error, data, response) => {
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
- **Accept**: */*


## eyecolor

> String eyecolor()



### Example

```javascript
import OpenApiDefinition from 'open_api_definition';

let apiInstance = new OpenApiDefinition.PeoplegeneratorapiApplicationApi();
apiInstance.eyecolor((error, data, response) => {
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
- **Accept**: */*


## eyecolor1

> String eyecolor1()



### Example

```javascript
import OpenApiDefinition from 'open_api_definition';

let apiInstance = new OpenApiDefinition.PeoplegeneratorapiApplicationApi();
apiInstance.eyecolor1((error, data, response) => {
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
- **Accept**: */*


## gender

> String gender()



### Example

```javascript
import OpenApiDefinition from 'open_api_definition';

let apiInstance = new OpenApiDefinition.PeoplegeneratorapiApplicationApi();
apiInstance.gender((error, data, response) => {
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
- **Accept**: */*


## gender1

> String gender1()



### Example

```javascript
import OpenApiDefinition from 'open_api_definition';

let apiInstance = new OpenApiDefinition.PeoplegeneratorapiApplicationApi();
apiInstance.gender1((error, data, response) => {
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
- **Accept**: */*


## generateAddress

> Address generateAddress()



### Example

```javascript
import OpenApiDefinition from 'open_api_definition';

let apiInstance = new OpenApiDefinition.PeoplegeneratorapiApplicationApi();
apiInstance.generateAddress((error, data, response) => {
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

[**Address**](Address.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## generateAddress1

> Address generateAddress1()



### Example

```javascript
import OpenApiDefinition from 'open_api_definition';

let apiInstance = new OpenApiDefinition.PeoplegeneratorapiApplicationApi();
apiInstance.generateAddress1((error, data, response) => {
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

[**Address**](Address.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## generateLifeStory

> Lifestory generateLifeStory()



### Example

```javascript
import OpenApiDefinition from 'open_api_definition';

let apiInstance = new OpenApiDefinition.PeoplegeneratorapiApplicationApi();
apiInstance.generateLifeStory((error, data, response) => {
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

[**Lifestory**](Lifestory.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## generateLifeStory1

> Lifestory generateLifeStory1()



### Example

```javascript
import OpenApiDefinition from 'open_api_definition';

let apiInstance = new OpenApiDefinition.PeoplegeneratorapiApplicationApi();
apiInstance.generateLifeStory1((error, data, response) => {
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

[**Lifestory**](Lifestory.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getCompressedPerson

> [Blob] getCompressedPerson(number)



### Example

```javascript
import OpenApiDefinition from 'open_api_definition';

let apiInstance = new OpenApiDefinition.PeoplegeneratorapiApplicationApi();
let number = 56; // Number | 
apiInstance.getCompressedPerson(number, (error, data, response) => {
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
 **number** | **Number**|  | 

### Return type

**[Blob]**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getCompressedPerson1

> [Blob] getCompressedPerson1(number)



### Example

```javascript
import OpenApiDefinition from 'open_api_definition';

let apiInstance = new OpenApiDefinition.PeoplegeneratorapiApplicationApi();
let number = 56; // Number | 
apiInstance.getCompressedPerson1(number, (error, data, response) => {
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
 **number** | **Number**|  | 

### Return type

**[Blob]**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPerson

> Person getPerson()



### Example

```javascript
import OpenApiDefinition from 'open_api_definition';

let apiInstance = new OpenApiDefinition.PeoplegeneratorapiApplicationApi();
apiInstance.getPerson((error, data, response) => {
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

[**Person**](Person.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getPerson1

> Person getPerson1()



### Example

```javascript
import OpenApiDefinition from 'open_api_definition';

let apiInstance = new OpenApiDefinition.PeoplegeneratorapiApplicationApi();
apiInstance.getPerson1((error, data, response) => {
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

[**Person**](Person.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## gpa

> Number gpa()



### Example

```javascript
import OpenApiDefinition from 'open_api_definition';

let apiInstance = new OpenApiDefinition.PeoplegeneratorapiApplicationApi();
apiInstance.gpa((error, data, response) => {
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

**Number**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## gpa1

> Number gpa1()



### Example

```javascript
import OpenApiDefinition from 'open_api_definition';

let apiInstance = new OpenApiDefinition.PeoplegeneratorapiApplicationApi();
apiInstance.gpa1((error, data, response) => {
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

**Number**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## haschildren

> Boolean haschildren()



### Example

```javascript
import OpenApiDefinition from 'open_api_definition';

let apiInstance = new OpenApiDefinition.PeoplegeneratorapiApplicationApi();
apiInstance.haschildren((error, data, response) => {
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

**Boolean**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## haschildren1

> Boolean haschildren1()



### Example

```javascript
import OpenApiDefinition from 'open_api_definition';

let apiInstance = new OpenApiDefinition.PeoplegeneratorapiApplicationApi();
apiInstance.haschildren1((error, data, response) => {
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

**Boolean**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## hasdegree

> Boolean hasdegree()



### Example

```javascript
import OpenApiDefinition from 'open_api_definition';

let apiInstance = new OpenApiDefinition.PeoplegeneratorapiApplicationApi();
apiInstance.hasdegree((error, data, response) => {
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

**Boolean**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## hasdegree1

> Boolean hasdegree1()



### Example

```javascript
import OpenApiDefinition from 'open_api_definition';

let apiInstance = new OpenApiDefinition.PeoplegeneratorapiApplicationApi();
apiInstance.hasdegree1((error, data, response) => {
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

**Boolean**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## height

> Number height()



### Example

```javascript
import OpenApiDefinition from 'open_api_definition';

let apiInstance = new OpenApiDefinition.PeoplegeneratorapiApplicationApi();
apiInstance.height((error, data, response) => {
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

**Number**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## height1

> Number height1()



### Example

```javascript
import OpenApiDefinition from 'open_api_definition';

let apiInstance = new OpenApiDefinition.PeoplegeneratorapiApplicationApi();
apiInstance.height1((error, data, response) => {
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

**Number**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## income

> Number income()



### Example

```javascript
import OpenApiDefinition from 'open_api_definition';

let apiInstance = new OpenApiDefinition.PeoplegeneratorapiApplicationApi();
apiInstance.income((error, data, response) => {
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

**Number**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## income1

> Number income1()



### Example

```javascript
import OpenApiDefinition from 'open_api_definition';

let apiInstance = new OpenApiDefinition.PeoplegeneratorapiApplicationApi();
apiInstance.income1((error, data, response) => {
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

**Number**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## job

> String job()



### Example

```javascript
import OpenApiDefinition from 'open_api_definition';

let apiInstance = new OpenApiDefinition.PeoplegeneratorapiApplicationApi();
apiInstance.job((error, data, response) => {
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
- **Accept**: */*


## job1

> String job1()



### Example

```javascript
import OpenApiDefinition from 'open_api_definition';

let apiInstance = new OpenApiDefinition.PeoplegeneratorapiApplicationApi();
apiInstance.job1((error, data, response) => {
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
- **Accept**: */*


## maritalstatus

> Boolean maritalstatus()



### Example

```javascript
import OpenApiDefinition from 'open_api_definition';

let apiInstance = new OpenApiDefinition.PeoplegeneratorapiApplicationApi();
apiInstance.maritalstatus((error, data, response) => {
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

**Boolean**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## maritalstatus1

> Boolean maritalstatus1()



### Example

```javascript
import OpenApiDefinition from 'open_api_definition';

let apiInstance = new OpenApiDefinition.PeoplegeneratorapiApplicationApi();
apiInstance.maritalstatus1((error, data, response) => {
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

**Boolean**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## name

> String name()



### Example

```javascript
import OpenApiDefinition from 'open_api_definition';

let apiInstance = new OpenApiDefinition.PeoplegeneratorapiApplicationApi();
apiInstance.name((error, data, response) => {
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
- **Accept**: */*


## name1

> String name1()



### Example

```javascript
import OpenApiDefinition from 'open_api_definition';

let apiInstance = new OpenApiDefinition.PeoplegeneratorapiApplicationApi();
apiInstance.name1((error, data, response) => {
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
- **Accept**: */*


## politicalLeaning

> Number politicalLeaning()



### Example

```javascript
import OpenApiDefinition from 'open_api_definition';

let apiInstance = new OpenApiDefinition.PeoplegeneratorapiApplicationApi();
apiInstance.politicalLeaning((error, data, response) => {
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

**Number**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## politicalLeaning1

> Number politicalLeaning1()



### Example

```javascript
import OpenApiDefinition from 'open_api_definition';

let apiInstance = new OpenApiDefinition.PeoplegeneratorapiApplicationApi();
apiInstance.politicalLeaning1((error, data, response) => {
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

**Number**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## religion

> String religion()



### Example

```javascript
import OpenApiDefinition from 'open_api_definition';

let apiInstance = new OpenApiDefinition.PeoplegeneratorapiApplicationApi();
apiInstance.religion((error, data, response) => {
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
- **Accept**: */*


## religion1

> String religion1()



### Example

```javascript
import OpenApiDefinition from 'open_api_definition';

let apiInstance = new OpenApiDefinition.PeoplegeneratorapiApplicationApi();
apiInstance.religion1((error, data, response) => {
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
- **Accept**: */*


## username

> String username()



### Example

```javascript
import OpenApiDefinition from 'open_api_definition';

let apiInstance = new OpenApiDefinition.PeoplegeneratorapiApplicationApi();
apiInstance.username((error, data, response) => {
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
- **Accept**: */*


## username1

> String username1()



### Example

```javascript
import OpenApiDefinition from 'open_api_definition';

let apiInstance = new OpenApiDefinition.PeoplegeneratorapiApplicationApi();
apiInstance.username1((error, data, response) => {
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
- **Accept**: */*


## weight

> Number weight()



### Example

```javascript
import OpenApiDefinition from 'open_api_definition';

let apiInstance = new OpenApiDefinition.PeoplegeneratorapiApplicationApi();
apiInstance.weight((error, data, response) => {
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

**Number**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## weight1

> Number weight1()



### Example

```javascript
import OpenApiDefinition from 'open_api_definition';

let apiInstance = new OpenApiDefinition.PeoplegeneratorapiApplicationApi();
apiInstance.weight1((error, data, response) => {
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

**Number**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

