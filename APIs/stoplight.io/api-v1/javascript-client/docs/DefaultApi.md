# Stoplight.DefaultApi

All URIs are relative to *https://api.stoplight.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**pOSTVersionsPublishAnon**](DefaultApi.md#pOSTVersionsPublishAnon) | **POST** /versions/publish/anon | Publish Anonymous



## pOSTVersionsPublishAnon

> POSTVersionsPublishAnon200Response pOSTVersionsPublishAnon(opts)

Publish Anonymous

Anonymously publish to API Docs.  This endpoint will take a JSON spec or a URL to a swagger or raml spec.  &#x60;&#x60;&#x60; {   \&quot;specData\&quot;: {...} } &#x60;&#x60;&#x60;  or  &#x60;&#x60;&#x60; {   \&quot;url\&quot;: \&quot;http://petstore.swagger.io/v2/swagger.json\&quot; } &#x60;&#x60;&#x60;  The spec will be published to api-docs.io anonymously, which means you will not be able to update or remove this documentation.  The response will contain a url to the published documentation.  &#x60;&#x60;&#x60; {   \&quot;url\&quot;: \&quot;https://swagger-petstore.api-docs.io/v1.0.0\&quot; } &#x60;&#x60;&#x60;   The limitations of anonymous publishing * Cannot update/remove the documentation * Cannot choose the subdomain * Cannot choose the version * Cannot add theming

### Example

```javascript
import Stoplight from 'stoplight';

let apiInstance = new Stoplight.DefaultApi();
let opts = {
  'pOSTVersionsPublishAnonRequest': new Stoplight.POSTVersionsPublishAnonRequest() // POSTVersionsPublishAnonRequest | 
};
apiInstance.pOSTVersionsPublishAnon(opts, (error, data, response) => {
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
 **pOSTVersionsPublishAnonRequest** | [**POSTVersionsPublishAnonRequest**](POSTVersionsPublishAnonRequest.md)|  | [optional] 

### Return type

[**POSTVersionsPublishAnon200Response**](POSTVersionsPublishAnon200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

