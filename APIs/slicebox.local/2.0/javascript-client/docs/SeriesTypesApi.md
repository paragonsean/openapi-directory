# SliceboxApi.SeriesTypesApi

All URIs are relative to *http://slicebox.local/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**seriestypesGet**](SeriesTypesApi.md#seriestypesGet) | **GET** /seriestypes | 
[**seriestypesIdDelete**](SeriesTypesApi.md#seriestypesIdDelete) | **DELETE** /seriestypes/{id} | 
[**seriestypesIdPut**](SeriesTypesApi.md#seriestypesIdPut) | **PUT** /seriestypes/{id} | 
[**seriestypesPost**](SeriesTypesApi.md#seriestypesPost) | **POST** /seriestypes | 
[**seriestypesRulesGet**](SeriesTypesApi.md#seriestypesRulesGet) | **GET** /seriestypes/rules | 
[**seriestypesRulesIdAttributesGet**](SeriesTypesApi.md#seriestypesRulesIdAttributesGet) | **GET** /seriestypes/rules/{id}/attributes | 
[**seriestypesRulesIdAttributesPost**](SeriesTypesApi.md#seriestypesRulesIdAttributesPost) | **POST** /seriestypes/rules/{id}/attributes | 
[**seriestypesRulesIdDelete**](SeriesTypesApi.md#seriestypesRulesIdDelete) | **DELETE** /seriestypes/rules/{id} | 
[**seriestypesRulesPost**](SeriesTypesApi.md#seriestypesRulesPost) | **POST** /seriestypes/rules | 
[**seriestypesRulesRuleIdAttributesAttributeIdDelete**](SeriesTypesApi.md#seriestypesRulesRuleIdAttributesAttributeIdDelete) | **DELETE** /seriestypes/rules/{ruleId}/attributes/{attributeId} | 
[**seriestypesRulesUpdatestatusGet**](SeriesTypesApi.md#seriestypesRulesUpdatestatusGet) | **GET** /seriestypes/rules/updatestatus | 



## seriestypesGet

> [Seriestype] seriestypesGet(opts)



get a list of all added series types. By filtering search results for certain series types, it is easier for applications to ensure that they read images of applicable types.

### Example

```javascript
import SliceboxApi from 'slicebox_api';

let apiInstance = new SliceboxApi.SeriesTypesApi();
let opts = {
  'startindex': 0, // Number | start index of returned slice of series types
  'count': 20 // Number | size of returned slice of series types
};
apiInstance.seriestypesGet(opts, (error, data, response) => {
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
 **startindex** | **Number**| start index of returned slice of series types | [optional] [default to 0]
 **count** | **Number**| size of returned slice of series types | [optional] [default to 20]

### Return type

[**[Seriestype]**](Seriestype.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/octet-stream


## seriestypesIdDelete

> seriestypesIdDelete(id)



remove the series type corresponding to the supplied ID

### Example

```javascript
import SliceboxApi from 'slicebox_api';

let apiInstance = new SliceboxApi.SeriesTypesApi();
let id = 789; // Number | id of series type to remove
apiInstance.seriestypesIdDelete(id, (error, data, response) => {
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
 **id** | **Number**| id of series type to remove | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## seriestypesIdPut

> seriestypesIdPut(id)



request an asynchronous update of all series, labelling appropriate series with the series type corresponding to the supplied ID.

### Example

```javascript
import SliceboxApi from 'slicebox_api';

let apiInstance = new SliceboxApi.SeriesTypesApi();
let id = 789; // Number | id of series type to update series labels for
apiInstance.seriestypesIdPut(id, (error, data, response) => {
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
 **id** | **Number**| id of series type to update series labels for | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## seriestypesPost

> Seriestype seriestypesPost(opts)



add a new series type

### Example

```javascript
import SliceboxApi from 'slicebox_api';

let apiInstance = new SliceboxApi.SeriesTypesApi();
let opts = {
  'seriesType': new SliceboxApi.Seriestype() // Seriestype | Series type information. The ID property is irrelevant, the ID of the inserted record is present in the returned data.
};
apiInstance.seriestypesPost(opts, (error, data, response) => {
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
 **seriesType** | [**Seriestype**](Seriestype.md)| Series type information. The ID property is irrelevant, the ID of the inserted record is present in the returned data. | [optional] 

### Return type

[**Seriestype**](Seriestype.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/octet-stream, multipart/form-data
- **Accept**: application/json, application/octet-stream


## seriestypesRulesGet

> [Seriestyperule] seriestypesRulesGet(seriestypeid)



get a list of rules for assigning series types to series. A rule connects to a series of attributes with values and a resulting series type. If a series has the required values of the listed attributes, it is assigned to the series type of the rule.

### Example

```javascript
import SliceboxApi from 'slicebox_api';

let apiInstance = new SliceboxApi.SeriesTypesApi();
let seriestypeid = 789; // Number | ID of series type to list rules for
apiInstance.seriestypesRulesGet(seriestypeid, (error, data, response) => {
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
 **seriestypeid** | **Number**| ID of series type to list rules for | 

### Return type

[**[Seriestyperule]**](Seriestyperule.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/octet-stream


## seriestypesRulesIdAttributesGet

> [Seriestyperuleattribute] seriestypesRulesIdAttributesGet(id)



get the list of attributes for the series type rule with the supplied ID.

### Example

```javascript
import SliceboxApi from 'slicebox_api';

let apiInstance = new SliceboxApi.SeriesTypesApi();
let id = 789; // Number | index of series type rule to list rule attributes for
apiInstance.seriestypesRulesIdAttributesGet(id, (error, data, response) => {
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
 **id** | **Number**| index of series type rule to list rule attributes for | 

### Return type

[**[Seriestyperuleattribute]**](Seriestyperuleattribute.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/octet-stream


## seriestypesRulesIdAttributesPost

> Seriestyperuleattribute seriestypesRulesIdAttributesPost(id, opts)



add a new series type rule attribute

### Example

```javascript
import SliceboxApi from 'slicebox_api';

let apiInstance = new SliceboxApi.SeriesTypesApi();
let id = 789; // Number | ID of rule
let opts = {
  'seriesTypeRuleAttribute': new SliceboxApi.Seriestyperuleattribute() // Seriestyperuleattribute | Series type rule attribute information. The ID property is irrelevant, the ID of the inserted record is present in the returned data.
};
apiInstance.seriestypesRulesIdAttributesPost(id, opts, (error, data, response) => {
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
 **id** | **Number**| ID of rule | 
 **seriesTypeRuleAttribute** | [**Seriestyperuleattribute**](Seriestyperuleattribute.md)| Series type rule attribute information. The ID property is irrelevant, the ID of the inserted record is present in the returned data. | [optional] 

### Return type

[**Seriestyperuleattribute**](Seriestyperuleattribute.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/octet-stream, multipart/form-data
- **Accept**: application/json, application/octet-stream


## seriestypesRulesIdDelete

> seriestypesRulesIdDelete(id)



remove the series type rule corresponding to the supplied ID

### Example

```javascript
import SliceboxApi from 'slicebox_api';

let apiInstance = new SliceboxApi.SeriesTypesApi();
let id = 789; // Number | id of series type rule to remove
apiInstance.seriestypesRulesIdDelete(id, (error, data, response) => {
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
 **id** | **Number**| id of series type rule to remove | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## seriestypesRulesPost

> Seriestyperule seriestypesRulesPost(opts)



add a new series type rule

### Example

```javascript
import SliceboxApi from 'slicebox_api';

let apiInstance = new SliceboxApi.SeriesTypesApi();
let opts = {
  'seriesTypeRule': new SliceboxApi.Seriestyperule() // Seriestyperule | Series type rule information. The ID property is irrelevant, the ID of the inserted record is present in the returned data.
};
apiInstance.seriestypesRulesPost(opts, (error, data, response) => {
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
 **seriesTypeRule** | [**Seriestyperule**](Seriestyperule.md)| Series type rule information. The ID property is irrelevant, the ID of the inserted record is present in the returned data. | [optional] 

### Return type

[**Seriestyperule**](Seriestyperule.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/octet-stream, multipart/form-data
- **Accept**: application/json, application/octet-stream


## seriestypesRulesRuleIdAttributesAttributeIdDelete

> seriestypesRulesRuleIdAttributesAttributeIdDelete(ruleId, attributeId)



remove the series type rule attribute corresponding to the supplied series type and attribute IDs

### Example

```javascript
import SliceboxApi from 'slicebox_api';

let apiInstance = new SliceboxApi.SeriesTypesApi();
let ruleId = 789; // Number | id of series type rule for which to remove an attribute
let attributeId = 789; // Number | id of attribute to remove
apiInstance.seriestypesRulesRuleIdAttributesAttributeIdDelete(ruleId, attributeId, (error, data, response) => {
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
 **ruleId** | **Number**| id of series type rule for which to remove an attribute | 
 **attributeId** | **Number**| id of attribute to remove | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## seriestypesRulesUpdatestatusGet

> Seriestypeupdatestatus seriestypesRulesUpdatestatusGet()



get the status of the internal process of updating series types for series following a change of series types, rules or attributes.

### Example

```javascript
import SliceboxApi from 'slicebox_api';

let apiInstance = new SliceboxApi.SeriesTypesApi();
apiInstance.seriestypesRulesUpdatestatusGet((error, data, response) => {
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

[**Seriestypeupdatestatus**](Seriestypeupdatestatus.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/octet-stream

