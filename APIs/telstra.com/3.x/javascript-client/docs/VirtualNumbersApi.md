# MessagingApiV3X.VirtualNumbersApi

All URIs are relative to *https://products.api.telstra.com/messaging/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assignNumber**](VirtualNumbersApi.md#assignNumber) | **POST** /virtual-numbers | assign a virtual number
[**deleteNumber**](VirtualNumbersApi.md#deleteNumber) | **DELETE** /virtual-numbers/{virtual-number} | delete a virtual number
[**getNumbers**](VirtualNumbersApi.md#getNumbers) | **GET** /virtual-numbers | fetch all virtual numbers
[**getRecipientOptouts**](VirtualNumbersApi.md#getRecipientOptouts) | **GET** /virtual-numbers/{virtual-number}/optouts | Get recipient optouts list
[**getVirtualNumber**](VirtualNumbersApi.md#getVirtualNumber) | **GET** /virtual-numbers/{virtual-number} | fetch a virtual number
[**updateNumber**](VirtualNumbersApi.md#updateNumber) | **PUT** /virtual-numbers/{virtual-number} | update a virtual number



## assignNumber

> VirtualNumber assignNumber(contentLanguage, authorization, accept, acceptCharset, contentType, assignNumberRequest, opts)

assign a virtual number

When a recipient receives your message, you can choose whether they&#39;ll see a privateNumber, Virtual Number or senderName (paid plans only) in the **from** field. If you want to use a Virtual Number, use this endpoint to assign one. Free Trial users can assign one Virtual Number, and those on a paid plan can assign up to 100.   Virtual Numbers that have not sent a message in 30 days (Free Trial) or sent/received a message in 18 months (paid plans) will be automatically unassigned from your account. You can check the **lastUse** date of your Virtual Number at any time using GET /virtual-numbers/{virtual-number}.  Note that Virtual Numbers used in v2 of the Messaging API cannot be used to send messages in v3. Please assign a new Virtual Number instead. 

### Example

```javascript
import MessagingApiV3X from 'messaging_api_v3_x';
let defaultClient = MessagingApiV3X.ApiClient.instance;
// Configure OAuth2 access token for authorization: bearer_auth
let bearer_auth = defaultClient.authentications['bearer_auth'];
bearer_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MessagingApiV3X.VirtualNumbersApi();
let contentLanguage = "en-au"; // String | 
let authorization = "Bearer <access_token>"; // String | 
let accept = "application/json"; // String | 
let acceptCharset = "utf-8"; // String | 
let contentType = "application/json"; // String | 
let assignNumberRequest = new MessagingApiV3X.AssignNumberRequest(); // AssignNumberRequest | 
let opts = {
  'telstraApiVersion': "3.1.0" // String | 
};
apiInstance.assignNumber(contentLanguage, authorization, accept, acceptCharset, contentType, assignNumberRequest, opts, (error, data, response) => {
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
 **contentLanguage** | **String**|  | 
 **authorization** | **String**|  | 
 **accept** | **String**|  | 
 **acceptCharset** | **String**|  | 
 **contentType** | **String**|  | 
 **assignNumberRequest** | [**AssignNumberRequest**](AssignNumberRequest.md)|  | 
 **telstraApiVersion** | **String**|  | [optional] 

### Return type

[**VirtualNumber**](VirtualNumber.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteNumber

> deleteNumber(contentLanguage, authorization, accept, acceptCharset, contentType, virtualNumber, opts)

delete a virtual number

Use **virtual-number** to remove a Virtual Number that&#39;s been assigned to your account. 

### Example

```javascript
import MessagingApiV3X from 'messaging_api_v3_x';
let defaultClient = MessagingApiV3X.ApiClient.instance;
// Configure OAuth2 access token for authorization: bearer_auth
let bearer_auth = defaultClient.authentications['bearer_auth'];
bearer_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MessagingApiV3X.VirtualNumbersApi();
let contentLanguage = "en-au"; // String | 
let authorization = "Bearer <access_token>"; // String | 
let accept = "application/json"; // String | 
let acceptCharset = "utf-8"; // String | 
let contentType = "application/json"; // String | 
let virtualNumber = "0412345678"; // String | Write the Virtual Number here, using national format (e.g. 0412345678). 
let opts = {
  'telstraApiVersion': "3.1.0" // String | 
};
apiInstance.deleteNumber(contentLanguage, authorization, accept, acceptCharset, contentType, virtualNumber, opts, (error, data, response) => {
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
 **contentLanguage** | **String**|  | 
 **authorization** | **String**|  | 
 **accept** | **String**|  | 
 **acceptCharset** | **String**|  | 
 **contentType** | **String**|  | 
 **virtualNumber** | **String**| Write the Virtual Number here, using national format (e.g. 0412345678).  | 
 **telstraApiVersion** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNumbers

> GetNumbers200Response getNumbers(contentLanguage, authorization, accept, acceptCharset, contentType, opts)

fetch all virtual numbers

Use this endpoint to fetch all Virtual Numbers currently assigned to your account. 

### Example

```javascript
import MessagingApiV3X from 'messaging_api_v3_x';
let defaultClient = MessagingApiV3X.ApiClient.instance;
// Configure OAuth2 access token for authorization: bearer_auth
let bearer_auth = defaultClient.authentications['bearer_auth'];
bearer_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MessagingApiV3X.VirtualNumbersApi();
let contentLanguage = "en-au"; // String | 
let authorization = "Bearer <access_token>"; // String | 
let accept = "application/json"; // String | 
let acceptCharset = "utf-8"; // String | 
let contentType = "application/json"; // String | 
let opts = {
  'telstraApiVersion': "3.1.0", // String | 
  'limit': 10, // Number | Tell us how many results you want us to return, up to a maximum of 50. 
  'offset': 0, // Number | Use the offset to navigate between the response results. An offset of 0 will display the first page of results, and so on. 
  'filter': "filter_example" // String | Filter your Virtual Numbers by tag or by number.
};
apiInstance.getNumbers(contentLanguage, authorization, accept, acceptCharset, contentType, opts, (error, data, response) => {
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
 **contentLanguage** | **String**|  | 
 **authorization** | **String**|  | 
 **accept** | **String**|  | 
 **acceptCharset** | **String**|  | 
 **contentType** | **String**|  | 
 **telstraApiVersion** | **String**|  | [optional] 
 **limit** | **Number**| Tell us how many results you want us to return, up to a maximum of 50.  | [optional] [default to 10]
 **offset** | **Number**| Use the offset to navigate between the response results. An offset of 0 will display the first page of results, and so on.  | [optional] [default to 0]
 **filter** | **String**| Filter your Virtual Numbers by tag or by number. | [optional] 

### Return type

[**GetNumbers200Response**](GetNumbers200Response.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getRecipientOptouts

> GetRecipientOptouts200Response getRecipientOptouts(contentLanguage, authorization, accept, acceptCharset, contentType, virtualNumber, opts)

Get recipient optouts list

Use this endpoint to fetch any mobile number(s) that have opted out of receiving messages from a Virtual Number assigned to your account.  Recipients can opt out at any time by sending a message with industry standard keywords such as STOP, STOPALL, UNSUBSCRIBE, QUIT, END and CANCEL. 

### Example

```javascript
import MessagingApiV3X from 'messaging_api_v3_x';
let defaultClient = MessagingApiV3X.ApiClient.instance;
// Configure OAuth2 access token for authorization: bearer_auth
let bearer_auth = defaultClient.authentications['bearer_auth'];
bearer_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MessagingApiV3X.VirtualNumbersApi();
let contentLanguage = "en-au"; // String | 
let authorization = "Bearer <access_token>"; // String | 
let accept = "application/json"; // String | 
let acceptCharset = "utf-8"; // String | 
let contentType = "application/json"; // String | 
let virtualNumber = "0412345678"; // String | Write the Virtual Number here, using national format (e.g. 0412345678). 
let opts = {
  'telstraApiVersion': "3.1.0", // String | 
  'limit': 10, // Number | Tell us how many results you want us to return, up to a maximum of 50. 
  'offset': 0 // Number | Use the offset to navigate between the response results. An offset of 0 will display the first page of results, and so on. 
};
apiInstance.getRecipientOptouts(contentLanguage, authorization, accept, acceptCharset, contentType, virtualNumber, opts, (error, data, response) => {
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
 **contentLanguage** | **String**|  | 
 **authorization** | **String**|  | 
 **accept** | **String**|  | 
 **acceptCharset** | **String**|  | 
 **contentType** | **String**|  | 
 **virtualNumber** | **String**| Write the Virtual Number here, using national format (e.g. 0412345678).  | 
 **telstraApiVersion** | **String**|  | [optional] 
 **limit** | **Number**| Tell us how many results you want us to return, up to a maximum of 50.  | [optional] [default to 10]
 **offset** | **Number**| Use the offset to navigate between the response results. An offset of 0 will display the first page of results, and so on.  | [optional] [default to 0]

### Return type

[**GetRecipientOptouts200Response**](GetRecipientOptouts200Response.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getVirtualNumber

> VirtualNumber getVirtualNumber(contentLanguage, authorization, accept, acceptCharset, contentType, virtualNumber, opts)

fetch a virtual number

Fetch the tags, replyCallbackUrl and lastUse date for a Virtual Number.

### Example

```javascript
import MessagingApiV3X from 'messaging_api_v3_x';
let defaultClient = MessagingApiV3X.ApiClient.instance;
// Configure OAuth2 access token for authorization: bearer_auth
let bearer_auth = defaultClient.authentications['bearer_auth'];
bearer_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MessagingApiV3X.VirtualNumbersApi();
let contentLanguage = "en-au"; // String | 
let authorization = "Bearer <access_token>"; // String | 
let accept = "application/json"; // String | 
let acceptCharset = "utf-8"; // String | 
let contentType = "application/json"; // String | 
let virtualNumber = "0412345678"; // String | Write the Virtual Number here, using national format (e.g. 0412345678). 
let opts = {
  'telstraApiVersion': "3.1.0" // String | 
};
apiInstance.getVirtualNumber(contentLanguage, authorization, accept, acceptCharset, contentType, virtualNumber, opts, (error, data, response) => {
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
 **contentLanguage** | **String**|  | 
 **authorization** | **String**|  | 
 **accept** | **String**|  | 
 **acceptCharset** | **String**|  | 
 **contentType** | **String**|  | 
 **virtualNumber** | **String**| Write the Virtual Number here, using national format (e.g. 0412345678).  | 
 **telstraApiVersion** | **String**|  | [optional] 

### Return type

[**VirtualNumber**](VirtualNumber.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateNumber

> VirtualNumber updateNumber(contentLanguage, authorization, accept, acceptCharset, contentType, virtualNumber, updateNumberRequest, opts)

update a virtual number

Use **virtual-number** to update the tags and/or replyCallbackUrl of a Virtual Number.  This request body will override the original POST/ virtual-numbers call. 

### Example

```javascript
import MessagingApiV3X from 'messaging_api_v3_x';
let defaultClient = MessagingApiV3X.ApiClient.instance;
// Configure OAuth2 access token for authorization: bearer_auth
let bearer_auth = defaultClient.authentications['bearer_auth'];
bearer_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MessagingApiV3X.VirtualNumbersApi();
let contentLanguage = "en-au"; // String | 
let authorization = "Bearer <access_token>"; // String | 
let accept = "application/json"; // String | 
let acceptCharset = "utf-8"; // String | 
let contentType = "application/json"; // String | 
let virtualNumber = "0412345678"; // String | Write the Virtual Number here, using national format (e.g. 0412345678). 
let updateNumberRequest = new MessagingApiV3X.UpdateNumberRequest(); // UpdateNumberRequest | 
let opts = {
  'telstraApiVersion': "3.1.0" // String | 
};
apiInstance.updateNumber(contentLanguage, authorization, accept, acceptCharset, contentType, virtualNumber, updateNumberRequest, opts, (error, data, response) => {
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
 **contentLanguage** | **String**|  | 
 **authorization** | **String**|  | 
 **accept** | **String**|  | 
 **acceptCharset** | **String**|  | 
 **contentType** | **String**|  | 
 **virtualNumber** | **String**| Write the Virtual Number here, using national format (e.g. 0412345678).  | 
 **updateNumberRequest** | [**UpdateNumberRequest**](UpdateNumberRequest.md)|  | 
 **telstraApiVersion** | **String**|  | [optional] 

### Return type

[**VirtualNumber**](VirtualNumber.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

