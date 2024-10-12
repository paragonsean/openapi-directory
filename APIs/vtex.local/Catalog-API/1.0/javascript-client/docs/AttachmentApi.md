# CatalogApi.AttachmentApi

All URIs are relative to *https://vtex.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiCatalogPvtAttachmentAttachmentidDelete**](AttachmentApi.md#apiCatalogPvtAttachmentAttachmentidDelete) | **DELETE** /api/catalog/pvt/attachment/{attachmentid} | Delete attachment
[**apiCatalogPvtAttachmentAttachmentidGet**](AttachmentApi.md#apiCatalogPvtAttachmentAttachmentidGet) | **GET** /api/catalog/pvt/attachment/{attachmentid} | Get attachment
[**apiCatalogPvtAttachmentAttachmentidPut**](AttachmentApi.md#apiCatalogPvtAttachmentAttachmentidPut) | **PUT** /api/catalog/pvt/attachment/{attachmentid} | Update attachment
[**apiCatalogPvtAttachmentPost**](AttachmentApi.md#apiCatalogPvtAttachmentPost) | **POST** /api/catalog/pvt/attachment | Create attachment
[**apiCatalogPvtAttachmentsGet**](AttachmentApi.md#apiCatalogPvtAttachmentsGet) | **GET** /api/catalog/pvt/attachments | Get all attachments



## apiCatalogPvtAttachmentAttachmentidDelete

> apiCatalogPvtAttachmentAttachmentidDelete(attachmentid, contentType, accept)

Delete attachment

Deletes a previously existing SKU attachment.

### Example

```javascript
import CatalogApi from 'catalog_api';
let defaultClient = CatalogApi.ApiClient.instance;
// Configure API key authorization: appToken
let appToken = defaultClient.authentications['appToken'];
appToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appToken.apiKeyPrefix = 'Token';
// Configure API key authorization: appKey
let appKey = defaultClient.authentications['appKey'];
appKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appKey.apiKeyPrefix = 'Token';

let apiInstance = new CatalogApi.AttachmentApi();
let attachmentid = "vtexcommercestable"; // String | Attachment ID.
let contentType = "'application/json'"; // String | Type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
apiInstance.apiCatalogPvtAttachmentAttachmentidDelete(attachmentid, contentType, accept, (error, data, response) => {
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
 **attachmentid** | **String**| Attachment ID. | 
 **contentType** | **String**| Type of the content being sent. | [default to &#39;application/json&#39;]
 **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | [default to &#39;application/json&#39;]

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiCatalogPvtAttachmentAttachmentidGet

> AttachmentResponse apiCatalogPvtAttachmentAttachmentidGet(attachmentid, contentType, accept)

Get attachment

Gets information about a registered attachment.    &gt;⚠️ To understand the specific syntax for Assembly Options attachments, read the [Assembly Options](https://help.vtex.com/en/tutorial/assembly-options--5x5FhNr4f5RUGDEGWzV1nH#assembly-options-syntax) documentation.  ## Response body example    &#x60;&#x60;&#x60;json  {    \&quot;Id\&quot;: 8,    \&quot;Name\&quot;: \&quot;Test\&quot;,    \&quot;IsRequired\&quot;: true,    \&quot;IsActive\&quot;: true,    \&quot;Domains\&quot;: [      {        \&quot;FieldName\&quot;: \&quot;Basic test\&quot;,        \&quot;MaxCaracters\&quot;: \&quot;\&quot;,        \&quot;DomainValues\&quot;: \&quot;[1-2]#9[1-1][1]basic;#11[0-1][1]basic\&quot;      },      {        \&quot;FieldName\&quot;: \&quot;teste\&quot;,        \&quot;MaxCaracters\&quot;: \&quot;\&quot;,        \&quot;DomainValues\&quot;: \&quot;[0-10]#8[0-3][0]medium;#9[0-3][0]medium;#10[0-3][0]medium;#11[0-3][0]medium;#36[0-3][0]medium;#37[0-3][0]medium;#38[0-3][0]medium\&quot;      }    ]  }  &#x60;&#x60;&#x60;

### Example

```javascript
import CatalogApi from 'catalog_api';
let defaultClient = CatalogApi.ApiClient.instance;
// Configure API key authorization: appToken
let appToken = defaultClient.authentications['appToken'];
appToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appToken.apiKeyPrefix = 'Token';
// Configure API key authorization: appKey
let appKey = defaultClient.authentications['appKey'];
appKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appKey.apiKeyPrefix = 'Token';

let apiInstance = new CatalogApi.AttachmentApi();
let attachmentid = "8"; // String | Attachment ID.
let contentType = "'application/json'"; // String | Type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
apiInstance.apiCatalogPvtAttachmentAttachmentidGet(attachmentid, contentType, accept, (error, data, response) => {
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
 **attachmentid** | **String**| Attachment ID. | 
 **contentType** | **String**| Type of the content being sent. | [default to &#39;application/json&#39;]
 **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | [default to &#39;application/json&#39;]

### Return type

[**AttachmentResponse**](AttachmentResponse.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiCatalogPvtAttachmentAttachmentidPut

> AttachmentResponse apiCatalogPvtAttachmentAttachmentidPut(attachmentid, contentType, accept, opts)

Update attachment

Updates a previously existing SKU attachment with new information.    &gt;⚠️ To understand the specific syntax for Assembly Options attachments, read the [Assembly Options](https://help.vtex.com/en/tutorial/assembly-options--5x5FhNr4f5RUGDEGWzV1nH#assembly-options-syntax) documentation.   ## Request body example    &#x60;&#x60;&#x60;json  {    \&quot;Name\&quot;: \&quot;Test\&quot;,    \&quot;IsRequired\&quot;: true,    \&quot;IsActive\&quot;: true,    \&quot;Domains\&quot;: [      {        \&quot;FieldName\&quot;: \&quot;Basic test\&quot;,        \&quot;MaxCaracters\&quot;: \&quot;\&quot;,        \&quot;DomainValues\&quot;: \&quot;[1-2]#9[1-1][1]basic;#11[0-1][1]basic\&quot;      },      {        \&quot;FieldName\&quot;: \&quot;teste\&quot;,        \&quot;MaxCaracters\&quot;: \&quot;\&quot;,        \&quot;DomainValues\&quot;: \&quot;[0-10]#8[0-3][0]medium;#9[0-3][0]medium;#10[0-3][0]medium;#11[0-3][0]medium;#36[0-3][0]medium;#37[0-3][0]medium;#38[0-3][0]medium\&quot;      }    ]  }  &#x60;&#x60;&#x60;  ## Response body example    &#x60;&#x60;&#x60;json  {    \&quot;Id\&quot;: 8,    \&quot;Name\&quot;: \&quot;Test\&quot;,    \&quot;IsRequired\&quot;: true,    \&quot;IsActive\&quot;: true,    \&quot;Domains\&quot;: [      {        \&quot;FieldName\&quot;: \&quot;Basic test\&quot;,        \&quot;MaxCaracters\&quot;: \&quot;\&quot;,        \&quot;DomainValues\&quot;: \&quot;[1-2]#9[1-1][1]basic;#11[0-1][1]basic\&quot;      },      {        \&quot;FieldName\&quot;: \&quot;teste\&quot;,        \&quot;MaxCaracters\&quot;: \&quot;\&quot;,        \&quot;DomainValues\&quot;: \&quot;[0-10]#8[0-3][0]medium;#9[0-3][0]medium;#10[0-3][0]medium;#11[0-3][0]medium;#36[0-3][0]medium;#37[0-3][0]medium;#38[0-3][0]medium\&quot;      }    ]  }  &#x60;&#x60;&#x60;

### Example

```javascript
import CatalogApi from 'catalog_api';
let defaultClient = CatalogApi.ApiClient.instance;
// Configure API key authorization: appToken
let appToken = defaultClient.authentications['appToken'];
appToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appToken.apiKeyPrefix = 'Token';
// Configure API key authorization: appKey
let appKey = defaultClient.authentications['appKey'];
appKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appKey.apiKeyPrefix = 'Token';

let apiInstance = new CatalogApi.AttachmentApi();
let attachmentid = "vtexcommercestable"; // String | Attachment ID.
let contentType = "'application/json'"; // String | Type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let opts = {
  'attachmentRequest': new CatalogApi.AttachmentRequest() // AttachmentRequest | 
};
apiInstance.apiCatalogPvtAttachmentAttachmentidPut(attachmentid, contentType, accept, opts, (error, data, response) => {
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
 **attachmentid** | **String**| Attachment ID. | 
 **contentType** | **String**| Type of the content being sent. | [default to &#39;application/json&#39;]
 **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | [default to &#39;application/json&#39;]
 **attachmentRequest** | [**AttachmentRequest**](AttachmentRequest.md)|  | [optional] 

### Return type

[**AttachmentResponse**](AttachmentResponse.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## apiCatalogPvtAttachmentPost

> AttachmentResponse apiCatalogPvtAttachmentPost(contentType, accept, opts)

Create attachment

Creates a new SKU attachment.   &gt;⚠️ To understand the specific syntax for Assembly Options attachments, read the [Assembly Options](https://help.vtex.com/en/tutorial/assembly-options--5x5FhNr4f5RUGDEGWzV1nH#assembly-options-syntax) documentation.   ## Request body example    &#x60;&#x60;&#x60;json  {    \&quot;Name\&quot;: \&quot;Test\&quot;,    \&quot;IsRequired\&quot;: true,    \&quot;IsActive\&quot;: true,    \&quot;Domains\&quot;: [      {        \&quot;FieldName\&quot;: \&quot;Basic test\&quot;,        \&quot;MaxCaracters\&quot;: \&quot;\&quot;,        \&quot;DomainValues\&quot;: \&quot;[1-2]#9[1-1][1]basic;#11[0-1][1]basic\&quot;      },      {        \&quot;FieldName\&quot;: \&quot;teste\&quot;,        \&quot;MaxCaracters\&quot;: \&quot;\&quot;,        \&quot;DomainValues\&quot;: \&quot;[0-10]#8[0-3][0]medium;#9[0-3][0]medium;#10[0-3][0]medium;#11[0-3][0]medium;#36[0-3][0]medium;#37[0-3][0]medium;#38[0-3][0]medium\&quot;      }    ]  }  &#x60;&#x60;&#x60;  ## Response body example    &#x60;&#x60;&#x60;json  {    \&quot;Id\&quot;: 8,    \&quot;Name\&quot;: \&quot;Test\&quot;,    \&quot;IsRequired\&quot;: true,    \&quot;IsActive\&quot;: true,    \&quot;Domains\&quot;: [      {        \&quot;FieldName\&quot;: \&quot;Basic test\&quot;,        \&quot;MaxCaracters\&quot;: \&quot;\&quot;,        \&quot;DomainValues\&quot;: \&quot;[1-2]#9[1-1][1]basic;#11[0-1][1]basic\&quot;      },      {        \&quot;FieldName\&quot;: \&quot;teste\&quot;,        \&quot;MaxCaracters\&quot;: \&quot;\&quot;,        \&quot;DomainValues\&quot;: \&quot;[0-10]#8[0-3][0]medium;#9[0-3][0]medium;#10[0-3][0]medium;#11[0-3][0]medium;#36[0-3][0]medium;#37[0-3][0]medium;#38[0-3][0]medium\&quot;      }    ]  }  &#x60;&#x60;&#x60;

### Example

```javascript
import CatalogApi from 'catalog_api';
let defaultClient = CatalogApi.ApiClient.instance;
// Configure API key authorization: appToken
let appToken = defaultClient.authentications['appToken'];
appToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appToken.apiKeyPrefix = 'Token';
// Configure API key authorization: appKey
let appKey = defaultClient.authentications['appKey'];
appKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appKey.apiKeyPrefix = 'Token';

let apiInstance = new CatalogApi.AttachmentApi();
let contentType = "'application/json'"; // String | Type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let opts = {
  'attachmentRequest': new CatalogApi.AttachmentRequest() // AttachmentRequest | 
};
apiInstance.apiCatalogPvtAttachmentPost(contentType, accept, opts, (error, data, response) => {
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
 **contentType** | **String**| Type of the content being sent. | [default to &#39;application/json&#39;]
 **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | [default to &#39;application/json&#39;]
 **attachmentRequest** | [**AttachmentRequest**](AttachmentRequest.md)|  | [optional] 

### Return type

[**AttachmentResponse**](AttachmentResponse.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## apiCatalogPvtAttachmentsGet

> ApiCatalogPvtAttachmentsGet200Response apiCatalogPvtAttachmentsGet(contentType, accept)

Get all attachments

Retrieves information about all registered attachments.    &gt;⚠️ To understand the specific syntax for Assembly Options attachments, read the [Assembly Options](https://help.vtex.com/en/tutorial/assembly-options--5x5FhNr4f5RUGDEGWzV1nH#assembly-options-syntax) documentation.   ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;Page\&quot;: 1,      \&quot;Size\&quot;: 11,      \&quot;TotalRows\&quot;: 11,      \&quot;TotalPage\&quot;: 1,      \&quot;Data\&quot;: [          {              \&quot;Id\&quot;: 1,              \&quot;Name\&quot;: \&quot;Acessórios do bicho\&quot;,              \&quot;IsRequired\&quot;: true,              \&quot;IsActive\&quot;: true,              \&quot;Domains\&quot;: [                  {                      \&quot;FieldName\&quot;: \&quot;extra\&quot;,                      \&quot;MaxCaracters\&quot;: \&quot;\&quot;,                      \&quot;DomainValues\&quot;: \&quot;[0-3]#1[1-2][1]pricetable1;#3[0-2][0]pricetable2;#5[0-2][0]pricetable3\&quot;                  }              ]          },          {              \&quot;Id\&quot;: 2,              \&quot;Name\&quot;: \&quot;Sobrenome\&quot;,              \&quot;IsRequired\&quot;: false,              \&quot;IsActive\&quot;: true,              \&quot;Domains\&quot;: []          },          {              \&quot;Id\&quot;: 3,              \&quot;Name\&quot;: \&quot;Assinatura Teste\&quot;,              \&quot;IsRequired\&quot;: false,              \&quot;IsActive\&quot;: true,              \&quot;Domains\&quot;: [                  {                      \&quot;FieldName\&quot;: \&quot; vtex.subscription.key.frequency\&quot;,                      \&quot;MaxCaracters\&quot;: \&quot;\&quot;,                      \&quot;DomainValues\&quot;: \&quot;1 day, 7 day, 1 month, 6 month\&quot;                  },                  {                      \&quot;FieldName\&quot;: \&quot;vtex.subscription.key.validity.begin\&quot;,                      \&quot;MaxCaracters\&quot;: \&quot;\&quot;,                      \&quot;DomainValues\&quot;: \&quot;1\&quot;                  },                  {                      \&quot;FieldName\&quot;: \&quot;vtex.subscription.key.validity.end\&quot;,                      \&quot;MaxCaracters\&quot;: \&quot;\&quot;,                      \&quot;DomainValues\&quot;: \&quot;31\&quot;                  },                  {                      \&quot;FieldName\&quot;: \&quot;vtex.subscription.key.purchaseday\&quot;,                      \&quot;MaxCaracters\&quot;: \&quot;\&quot;,                      \&quot;DomainValues\&quot;: \&quot;1, 2, 20, 31\&quot;                  }              ]          },          {              \&quot;Id\&quot;: 5,              \&quot;Name\&quot;: \&quot;teste\&quot;,              \&quot;IsRequired\&quot;: false,              \&quot;IsActive\&quot;: true,              \&quot;Domains\&quot;: []          },          {              \&quot;Id\&quot;: 6,              \&quot;Name\&quot;: \&quot;teste2\&quot;,              \&quot;IsRequired\&quot;: false,              \&quot;IsActive\&quot;: true,              \&quot;Domains\&quot;: []          },          {              \&quot;Id\&quot;: 7,              \&quot;Name\&quot;: \&quot;vtex.subscription.teste3\&quot;,              \&quot;IsRequired\&quot;: false,              \&quot;IsActive\&quot;: true,              \&quot;Domains\&quot;: []          },          {              \&quot;Id\&quot;: 8,              \&quot;Name\&quot;: \&quot;teste api nova\&quot;,              \&quot;IsRequired\&quot;: true,              \&quot;IsActive\&quot;: true,              \&quot;Domains\&quot;: [                  {                      \&quot;FieldName\&quot;: \&quot;Basic teste\&quot;,                      \&quot;MaxCaracters\&quot;: \&quot;\&quot;,                      \&quot;DomainValues\&quot;: \&quot;[1-2]#9[1-1][1]basic;#11[0-1][1]basic\&quot;                  },                  {                      \&quot;FieldName\&quot;: \&quot;teste\&quot;,                      \&quot;MaxCaracters\&quot;: \&quot;\&quot;,                      \&quot;DomainValues\&quot;: \&quot;[0-10]#8[0-3][0]medium;#9[0-3][0]medium;#10[0-3][0]medium;#11[0-3][0]medium;#36[0-3][0]medium;#37[0-3][0]medium;#38[0-3][0]medium\&quot;                  }              ]          },          {              \&quot;Id\&quot;: 9,              \&quot;Name\&quot;: \&quot;vtex.subscription.teste\&quot;,              \&quot;IsRequired\&quot;: false,              \&quot;IsActive\&quot;: true,              \&quot;Domains\&quot;: []          },          {              \&quot;Id\&quot;: 10,              \&quot;Name\&quot;: \&quot;Montagens\&quot;,              \&quot;IsRequired\&quot;: false,              \&quot;IsActive\&quot;: true,              \&quot;Domains\&quot;: []          },          {              \&quot;Id\&quot;: 11,              \&quot;Name\&quot;: \&quot;vtex.subscription.subscription\&quot;,              \&quot;IsRequired\&quot;: false,              \&quot;IsActive\&quot;: true,              \&quot;Domains\&quot;: [                  {                      \&quot;FieldName\&quot;: \&quot;vtex.subscription.key.frequency\&quot;,                      \&quot;MaxCaracters\&quot;: \&quot;15\&quot;,                      \&quot;DomainValues\&quot;: \&quot;1 month\&quot;                  },                  {                      \&quot;FieldName\&quot;: \&quot;vtex.subscription.key.purchaseday\&quot;,                      \&quot;MaxCaracters\&quot;: \&quot;15\&quot;,                      \&quot;DomainValues\&quot;: \&quot;1,15,28\&quot;                  }              ]          },          {              \&quot;Id\&quot;: 12,              \&quot;Name\&quot;: \&quot;T-Shirt Customization\&quot;,              \&quot;IsRequired\&quot;: false,              \&quot;IsActive\&quot;: true,              \&quot;Domains\&quot;: [                  {                      \&quot;FieldName\&quot;: \&quot;T-Shirt Name\&quot;,                      \&quot;MaxCaracters\&quot;: \&quot;15\&quot;,                      \&quot;DomainValues\&quot;: \&quot;[]\&quot;                  }              ]          }      ]  }  &#x60;&#x60;&#x60;

### Example

```javascript
import CatalogApi from 'catalog_api';
let defaultClient = CatalogApi.ApiClient.instance;
// Configure API key authorization: appToken
let appToken = defaultClient.authentications['appToken'];
appToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appToken.apiKeyPrefix = 'Token';
// Configure API key authorization: appKey
let appKey = defaultClient.authentications['appKey'];
appKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appKey.apiKeyPrefix = 'Token';

let apiInstance = new CatalogApi.AttachmentApi();
let contentType = "'application/json'"; // String | Type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
apiInstance.apiCatalogPvtAttachmentsGet(contentType, accept, (error, data, response) => {
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
 **contentType** | **String**| Type of the content being sent. | [default to &#39;application/json&#39;]
 **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | [default to &#39;application/json&#39;]

### Return type

[**ApiCatalogPvtAttachmentsGet200Response**](ApiCatalogPvtAttachmentsGet200Response.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

