# AgcoApi.AuthorizationContactInformationApi

All URIs are relative to *https://secure.agco-ats.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**authorizationContactInformationGet**](AuthorizationContactInformationApi.md#authorizationContactInformationGet) | **GET** /api/v2/AuthorizationContactInformation | Get contact information for authorization codes.
[**authorizationContactInformationPost**](AuthorizationContactInformationApi.md#authorizationContactInformationPost) | **POST** /api/v2/AuthorizationContactInformation | Add contact information for authorization code.



## authorizationContactInformationGet

> APIIPagedResponseAuthorizationCodesSharedModelsAuthorizationContactInformation authorizationContactInformationGet(opts)

Get contact information for authorization codes.

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.AuthorizationContactInformationApi();
let opts = {
  'limit': 56, // Number | Optional. The page limit.  If not specified, the default page limit is 10.
  'offset': 56, // Number | Optional. The page offset.  If not specified, the default page offset is 0.
  'authorizationCode': "authorizationCode_example", // String | Optional. Search by authorization code.
  'afterDate': new Date("2013-10-20T19:20:30+01:00"), // Date | Optional. Include only data for authorization codes created after a provided date.
  'beforeDate': new Date("2013-10-20T19:20:30+01:00"), // Date | Optional. Include only data for authorization codes created before a provided date.
  'dealerCode': "dealerCode_example" // String | Optional. Search by dealer code.
};
apiInstance.authorizationContactInformationGet(opts, (error, data, response) => {
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
 **limit** | **Number**| Optional. The page limit.  If not specified, the default page limit is 10. | [optional] 
 **offset** | **Number**| Optional. The page offset.  If not specified, the default page offset is 0. | [optional] 
 **authorizationCode** | **String**| Optional. Search by authorization code. | [optional] 
 **afterDate** | **Date**| Optional. Include only data for authorization codes created after a provided date. | [optional] 
 **beforeDate** | **Date**| Optional. Include only data for authorization codes created before a provided date. | [optional] 
 **dealerCode** | **String**| Optional. Search by dealer code. | [optional] 

### Return type

[**APIIPagedResponseAuthorizationCodesSharedModelsAuthorizationContactInformation**](APIIPagedResponseAuthorizationCodesSharedModelsAuthorizationContactInformation.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## authorizationContactInformationPost

> Number authorizationContactInformationPost(authorizationCodesSharedModelsAuthorizationContactInformation)

Add contact information for authorization code.

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.AuthorizationContactInformationApi();
let authorizationCodesSharedModelsAuthorizationContactInformation = new AgcoApi.AuthorizationCodesSharedModelsAuthorizationContactInformation(); // AuthorizationCodesSharedModelsAuthorizationContactInformation | A contact information.
apiInstance.authorizationContactInformationPost(authorizationCodesSharedModelsAuthorizationContactInformation, (error, data, response) => {
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
 **authorizationCodesSharedModelsAuthorizationContactInformation** | [**AuthorizationCodesSharedModelsAuthorizationContactInformation**](AuthorizationCodesSharedModelsAuthorizationContactInformation.md)| A contact information. | 

### Return type

**Number**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: application/json, application/xml, text/json, text/xml

