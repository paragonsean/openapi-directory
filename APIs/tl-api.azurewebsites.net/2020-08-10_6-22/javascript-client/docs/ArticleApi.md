# Api.ArticleApi

All URIs are relative to *https://tl-api.azurewebsites.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**articleAddMeasureUnit**](ArticleApi.md#articleAddMeasureUnit) | **POST** /api/Article/MeasureUnit | Add measure unit
[**articleDelete**](ArticleApi.md#articleDelete) | **DELETE** /api/Article | Delete article from the system             
[**articleGet**](ArticleApi.md#articleGet) | **GET** /api/Article/{articleID} | Get article details This will return all properties related to article entity             
[**articleGetAddons**](ArticleApi.md#articleGetAddons) | **GET** /api/Article/GetAddons | 
[**articleGetMeasureUnits**](ArticleApi.md#articleGetMeasureUnits) | **GET** /api/Article/MeasureUnits | Get mesure units
[**articleGetRevenueAccounts**](ArticleApi.md#articleGetRevenueAccounts) | **GET** /api/Article/RevenueAccounts | Get Revenue Accounts 
[**articleGymArticleDetails**](ArticleApi.md#articleGymArticleDetails) | **GET** /api/Article/GymArticle/{articleId}/{gymId} | Get Gym specific properties for article             
[**articlePost**](ArticleApi.md#articlePost) | **POST** /api/Article | Add new article             
[**articlePut**](ArticleApi.md#articlePut) | **PUT** /api/Article | update existing article             
[**articleSearch**](ArticleApi.md#articleSearch) | **GET** /api/Article/Search | Search articles It will only return basic information of article             
[**articleUpdateArticleGymDetails**](ArticleApi.md#articleUpdateArticleGymDetails) | **PUT** /api/Article/ArticleGymDetails | Add article details that associate with a Gym             
[**articleUpdateStatus**](ArticleApi.md#articleUpdateStatus) | **PUT** /api/Article/UpdateStatus | Deactivate existing article 



## articleAddMeasureUnit

> DefaultResponseDTOOfStatusDTO articleAddMeasureUnit(measureUnitDTO)

Add measure unit

### Example

```javascript
import Api from 'api';
let defaultClient = Api.ApiClient.instance;
// Configure OAuth2 access token for authorization: bearer
let bearer = defaultClient.authentications['bearer'];
bearer.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Api.ArticleApi();
let measureUnitDTO = [new Api.MeasureUnitDTO()]; // [MeasureUnitDTO] | list of measureUnit
apiInstance.articleAddMeasureUnit(measureUnitDTO, (error, data, response) => {
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
 **measureUnitDTO** | [**[MeasureUnitDTO]**](MeasureUnitDTO.md)| list of measureUnit | 

### Return type

[**DefaultResponseDTOOfStatusDTO**](DefaultResponseDTOOfStatusDTO.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## articleDelete

> DefaultResponseDTOOfInteger articleDelete(opts)

Delete article from the system             

### Example

```javascript
import Api from 'api';
let defaultClient = Api.ApiClient.instance;
// Configure OAuth2 access token for authorization: bearer
let bearer = defaultClient.authentications['bearer'];
bearer.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Api.ArticleApi();
let opts = {
  'articleId': 56 // Number | indentity number(primary key) for article object
};
apiInstance.articleDelete(opts, (error, data, response) => {
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
 **articleId** | **Number**| indentity number(primary key) for article object | [optional] 

### Return type

[**DefaultResponseDTOOfInteger**](DefaultResponseDTOOfInteger.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## articleGet

> DefaultResponseDTOOfArticleDTO articleGet(articleID)

Get article details This will return all properties related to article entity             

### Example

```javascript
import Api from 'api';
let defaultClient = Api.ApiClient.instance;
// Configure OAuth2 access token for authorization: bearer
let bearer = defaultClient.authentications['bearer'];
bearer.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Api.ArticleApi();
let articleID = 56; // Number | indentity number (primary key) for article object
apiInstance.articleGet(articleID, (error, data, response) => {
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
 **articleID** | **Number**| indentity number (primary key) for article object | 

### Return type

[**DefaultResponseDTOOfArticleDTO**](DefaultResponseDTOOfArticleDTO.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## articleGetAddons

> DefaultResponseDTOOfListOfArticleSearchDTO articleGetAddons(opts)



### Example

```javascript
import Api from 'api';
let defaultClient = Api.ApiClient.instance;
// Configure OAuth2 access token for authorization: bearer
let bearer = defaultClient.authentications['bearer'];
bearer.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Api.ArticleApi();
let opts = {
  'searchText': "searchText_example", // String | Search text - will be search by the name
  'gymIds': "'-1'", // String | Comma separated gymIds deafult \"-1\" for all gyms
  'type': "'all'", // String | 
  'limit': 100, // Number | 
  'offset': 0 // Number | 
};
apiInstance.articleGetAddons(opts, (error, data, response) => {
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
 **searchText** | **String**| Search text - will be search by the name | [optional] 
 **gymIds** | **String**| Comma separated gymIds deafult \&quot;-1\&quot; for all gyms | [optional] [default to &#39;-1&#39;]
 **type** | **String**|  | [optional] [default to &#39;all&#39;]
 **limit** | **Number**|  | [optional] [default to 100]
 **offset** | **Number**|  | [optional] [default to 0]

### Return type

[**DefaultResponseDTOOfListOfArticleSearchDTO**](DefaultResponseDTOOfListOfArticleSearchDTO.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## articleGetMeasureUnits

> DefaultResponseDTOOfStatusDTO articleGetMeasureUnits(opts)

Get mesure units

### Example

```javascript
import Api from 'api';
let defaultClient = Api.ApiClient.instance;
// Configure OAuth2 access token for authorization: bearer
let bearer = defaultClient.authentications['bearer'];
bearer.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Api.ArticleApi();
let opts = {
  'type': "type_example" // String | type of the measure unit (all, item, service)
};
apiInstance.articleGetMeasureUnits(opts, (error, data, response) => {
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
 **type** | **String**| type of the measure unit (all, item, service) | [optional] 

### Return type

[**DefaultResponseDTOOfStatusDTO**](DefaultResponseDTOOfStatusDTO.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## articleGetRevenueAccounts

> DefaultResponseDTOOfStatusDTO articleGetRevenueAccounts()

Get Revenue Accounts 

### Example

```javascript
import Api from 'api';
let defaultClient = Api.ApiClient.instance;
// Configure OAuth2 access token for authorization: bearer
let bearer = defaultClient.authentications['bearer'];
bearer.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Api.ArticleApi();
apiInstance.articleGetRevenueAccounts((error, data, response) => {
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

[**DefaultResponseDTOOfStatusDTO**](DefaultResponseDTOOfStatusDTO.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## articleGymArticleDetails

> GymArticleDetailsDTO articleGymArticleDetails(articleId, gymId)

Get Gym specific properties for article             

### Example

```javascript
import Api from 'api';
let defaultClient = Api.ApiClient.instance;
// Configure OAuth2 access token for authorization: bearer
let bearer = defaultClient.authentications['bearer'];
bearer.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Api.ArticleApi();
let articleId = 56; // Number | indentity number(primary key) for article object
let gymId = 56; // Number | indentity number(primary key) for gym object
apiInstance.articleGymArticleDetails(articleId, gymId, (error, data, response) => {
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
 **articleId** | **Number**| indentity number(primary key) for article object | 
 **gymId** | **Number**| indentity number(primary key) for gym object | 

### Return type

[**GymArticleDetailsDTO**](GymArticleDetailsDTO.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## articlePost

> DefaultResponseDTOOfStatusDTO articlePost(articleDTO)

Add new article             

### Example

```javascript
import Api from 'api';
let defaultClient = Api.ApiClient.instance;
// Configure OAuth2 access token for authorization: bearer
let bearer = defaultClient.authentications['bearer'];
bearer.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Api.ArticleApi();
let articleDTO = new Api.ArticleDTO(); // ArticleDTO | article object
apiInstance.articlePost(articleDTO, (error, data, response) => {
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
 **articleDTO** | [**ArticleDTO**](ArticleDTO.md)| article object | 

### Return type

[**DefaultResponseDTOOfStatusDTO**](DefaultResponseDTOOfStatusDTO.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## articlePut

> DefaultResponseDTOOfStatusDTO articlePut(articleDTO)

update existing article             

### Example

```javascript
import Api from 'api';
let defaultClient = Api.ApiClient.instance;
// Configure OAuth2 access token for authorization: bearer
let bearer = defaultClient.authentications['bearer'];
bearer.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Api.ArticleApi();
let articleDTO = new Api.ArticleDTO(); // ArticleDTO | article object
apiInstance.articlePut(articleDTO, (error, data, response) => {
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
 **articleDTO** | [**ArticleDTO**](ArticleDTO.md)| article object | 

### Return type

[**DefaultResponseDTOOfStatusDTO**](DefaultResponseDTOOfStatusDTO.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## articleSearch

> DefaultResponseDTOOfListOfArticleSearchDTO articleSearch(opts)

Search articles It will only return basic information of article             

### Example

```javascript
import Api from 'api';
let defaultClient = Api.ApiClient.instance;
// Configure OAuth2 access token for authorization: bearer
let bearer = defaultClient.authentications['bearer'];
bearer.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Api.ArticleApi();
let opts = {
  'searchText': "searchText_example", // String | part of article name
  'gymId': -1, // Number | -1 for all gyms 
  'type': "'all'", // String | filter article type. default is 'all'
  'orderBy': "'1'", // String | order by column.!-- invalid column will give internal server error
  'limit': 100, // Number | number of recode in result and default is 100. use negative numbers to order by desc
  'offset': 0, // Number | number of recodes to skip
  'activeStatus': 1 // Number | Active Status 1 : Active, 2: Inactive, 3: All, Default : 1
};
apiInstance.articleSearch(opts, (error, data, response) => {
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
 **searchText** | **String**| part of article name | [optional] 
 **gymId** | **Number**| -1 for all gyms  | [optional] [default to -1]
 **type** | **String**| filter article type. default is &#39;all&#39; | [optional] [default to &#39;all&#39;]
 **orderBy** | **String**| order by column.!-- invalid column will give internal server error | [optional] [default to &#39;1&#39;]
 **limit** | **Number**| number of recode in result and default is 100. use negative numbers to order by desc | [optional] [default to 100]
 **offset** | **Number**| number of recodes to skip | [optional] [default to 0]
 **activeStatus** | **Number**| Active Status 1 : Active, 2: Inactive, 3: All, Default : 1 | [optional] [default to 1]

### Return type

[**DefaultResponseDTOOfListOfArticleSearchDTO**](DefaultResponseDTOOfListOfArticleSearchDTO.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## articleUpdateArticleGymDetails

> DefaultResponseDTOOfStatusDTO articleUpdateArticleGymDetails(gymArticleDetailsDTO)

Add article details that associate with a Gym             

### Example

```javascript
import Api from 'api';
let defaultClient = Api.ApiClient.instance;
// Configure OAuth2 access token for authorization: bearer
let bearer = defaultClient.authentications['bearer'];
bearer.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Api.ArticleApi();
let gymArticleDetailsDTO = [new Api.GymArticleDetailsDTO()]; // [GymArticleDetailsDTO] | 
apiInstance.articleUpdateArticleGymDetails(gymArticleDetailsDTO, (error, data, response) => {
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
 **gymArticleDetailsDTO** | [**[GymArticleDetailsDTO]**](GymArticleDetailsDTO.md)|  | 

### Return type

[**DefaultResponseDTOOfStatusDTO**](DefaultResponseDTOOfStatusDTO.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## articleUpdateStatus

> DefaultResponseDTOOfInteger articleUpdateStatus(opts)

Deactivate existing article 

### Example

```javascript
import Api from 'api';
let defaultClient = Api.ApiClient.instance;
// Configure OAuth2 access token for authorization: bearer
let bearer = defaultClient.authentications['bearer'];
bearer.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Api.ArticleApi();
let opts = {
  'articleId': 56, // Number | 
  'status': 56, // Number | 1 : activate , 2 deactivate
  'userName': "userName_example" // String | Updating user
};
apiInstance.articleUpdateStatus(opts, (error, data, response) => {
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
 **articleId** | **Number**|  | [optional] 
 **status** | **Number**| 1 : activate , 2 deactivate | [optional] 
 **userName** | **String**| Updating user | [optional] 

### Return type

[**DefaultResponseDTOOfInteger**](DefaultResponseDTOOfInteger.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

