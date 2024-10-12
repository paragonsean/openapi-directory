# OpenapiJsClient.V1Api

All URIs are relative to *http://api.ote-godaddy.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**callDelete**](V1Api.md#callDelete) | **DELETE** /v1/shoppers/{shopperId} | Request the deletion of a shopper profile
[**changePassword**](V1Api.md#changePassword) | **PUT** /v1/shoppers/{shopperId}/factors/password | Set subaccount&#39;s password
[**createSubaccount**](V1Api.md#createSubaccount) | **POST** /v1/shoppers/subaccount | Create a Subaccount owned by the authenticated Reseller
[**get**](V1Api.md#get) | **GET** /v1/shoppers/{shopperId} | Get details for the specified Shopper
[**getStatus**](V1Api.md#getStatus) | **GET** /v1/shoppers/{shopperId}/status | Get details for the specified Shopper
[**update**](V1Api.md#update) | **POST** /v1/shoppers/{shopperId} | Update details for the specified Shopper



## callDelete

> callDelete(shopperId, auditClientIp)

Request the deletion of a shopper profile

&lt;strong&gt;Notes:&lt;/strong&gt;&lt;ul&gt;&lt;li&gt;Shopper deletion is not supported in OTE&lt;/li&gt;&lt;li&gt;**shopperId** is **not the same** as **customerId**.  **shopperId** is a number of max length 10 digits (*ex:* 1234567890) whereas **customerId** is a UUIDv4 (*ex:* 295e3bc3-b3b9-4d95-aae5-ede41a994d13)&lt;/li&gt;&lt;/ul&gt;

### Example

```javascript
import OpenapiJsClient from 'openapi-js-client';

let apiInstance = new OpenapiJsClient.V1Api();
let shopperId = "shopperId_example"; // String | The ID of the shopper to delete. Must agree with the shopper id on the token or header, if present. *Note*: **shopperId** is **not the same** as **customerId**.  **shopperId** is a number of max length 10 digits (*ex:* 1234567890) whereas **customerId** is a UUIDv4 (*ex:* 295e3bc3-b3b9-4d95-aae5-ede41a994d13)
let auditClientIp = "auditClientIp_example"; // String | The client IP of the user who originated the request leading to this call.
apiInstance.callDelete(shopperId, auditClientIp, (error, data, response) => {
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
 **shopperId** | **String**| The ID of the shopper to delete. Must agree with the shopper id on the token or header, if present. *Note*: **shopperId** is **not the same** as **customerId**.  **shopperId** is a number of max length 10 digits (*ex:* 1234567890) whereas **customerId** is a UUIDv4 (*ex:* 295e3bc3-b3b9-4d95-aae5-ede41a994d13) | 
 **auditClientIp** | **String**| The client IP of the user who originated the request leading to this call. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/javascript, application/json, application/xml, text/javascript, text/xml


## changePassword

> ShopperId changePassword(shopperId, secret)

Set subaccount&#39;s password

&lt;strong&gt;Notes:&lt;/strong&gt;&lt;ul&gt;&lt;li&gt;Password set is only supported by API Resellers setting subaccount passwords.&lt;/li&gt;&lt;li&gt;**shopperId** is **not the same** as **customerId**.  **shopperId** is a number of max length 10 digits (*ex:* 1234567890) whereas **customerId** is a UUIDv4 (*ex:* 295e3bc3-b3b9-4d95-aae5-ede41a994d13)&lt;/li&gt;&lt;/ul&gt;

### Example

```javascript
import OpenapiJsClient from 'openapi-js-client';

let apiInstance = new OpenapiJsClient.V1Api();
let shopperId = "shopperId_example"; // String | Shopper whose password will be set
let secret = new OpenapiJsClient.Secret(); // Secret | The value to set the subaccount's password to
apiInstance.changePassword(shopperId, secret, (error, data, response) => {
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
 **shopperId** | **String**| Shopper whose password will be set | 
 **secret** | [**Secret**](Secret.md)| The value to set the subaccount&#39;s password to | 

### Return type

[**ShopperId**](ShopperId.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createSubaccount

> ShopperId createSubaccount(subaccountCreate)

Create a Subaccount owned by the authenticated Reseller

### Example

```javascript
import OpenapiJsClient from 'openapi-js-client';

let apiInstance = new OpenapiJsClient.V1Api();
let subaccountCreate = new OpenapiJsClient.SubaccountCreate(); // SubaccountCreate | The subaccount to create
apiInstance.createSubaccount(subaccountCreate, (error, data, response) => {
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
 **subaccountCreate** | [**SubaccountCreate**](SubaccountCreate.md)| The subaccount to create | 

### Return type

[**ShopperId**](ShopperId.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml, text/xml
- **Accept**: application/javascript, application/json, application/xml, text/javascript, text/xml


## get

> Shopper get(shopperId, opts)

Get details for the specified Shopper

&lt;strong&gt;Notes:&lt;/strong&gt;&lt;ul&gt;&lt;li&gt;**shopperId** is **not the same** as **customerId**.  **shopperId** is a number of max length 10 digits (*ex:* 1234567890) whereas **customerId** is a UUIDv4 (*ex:* 295e3bc3-b3b9-4d95-aae5-ede41a994d13)&lt;/li&gt;&lt;/ul&gt;

### Example

```javascript
import OpenapiJsClient from 'openapi-js-client';

let apiInstance = new OpenapiJsClient.V1Api();
let shopperId = "shopperId_example"; // String | Shopper whose details are to be retrieved
let opts = {
  'includes': ["null"] // [String] | Additional properties to be included in the response shopper object
};
apiInstance.get(shopperId, opts, (error, data, response) => {
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
 **shopperId** | **String**| Shopper whose details are to be retrieved | 
 **includes** | [**[String]**](String.md)| Additional properties to be included in the response shopper object | [optional] 

### Return type

[**Shopper**](Shopper.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/javascript, application/json, application/xml, text/javascript, text/xml


## getStatus

> ShopperStatus getStatus(shopperId, auditClientIp)

Get details for the specified Shopper

&lt;strong&gt;Notes:&lt;/strong&gt;&lt;ul&gt;&lt;li&gt;**shopperId** is **not the same** as **customerId**. **shopperId** is a number of max length 10 digits (*ex:* 1234567890) whereas **customerId** is a UUIDv4 (*ex:* 295e3bc3-b3b9-4d95-aae5-ede41a994d13)&lt;/li&gt;&lt;/ul&gt;

### Example

```javascript
import OpenapiJsClient from 'openapi-js-client';

let apiInstance = new OpenapiJsClient.V1Api();
let shopperId = "shopperId_example"; // String | The ID of the shopper to retrieve. Must agree with the shopper id on the token or header, if present
let auditClientIp = "auditClientIp_example"; // String | The client IP of the user who originated the request leading to this call.
apiInstance.getStatus(shopperId, auditClientIp, (error, data, response) => {
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
 **shopperId** | **String**| The ID of the shopper to retrieve. Must agree with the shopper id on the token or header, if present | 
 **auditClientIp** | **String**| The client IP of the user who originated the request leading to this call. | 

### Return type

[**ShopperStatus**](ShopperStatus.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/javascript, application/json, application/xml, text/javascript, text/xml


## update

> ShopperId update(shopperId, shopperUpdate)

Update details for the specified Shopper

&lt;strong&gt;Notes:&lt;/strong&gt;&lt;ul&gt;&lt;li&gt;**shopperId** is **not the same** as **customerId**.  **shopperId** is a number of max length 10 digits (*ex:* 1234567890) whereas **customerId** is a UUIDv4 (*ex:* 295e3bc3-b3b9-4d95-aae5-ede41a994d13)&lt;/li&gt;&lt;/ul&gt;

### Example

```javascript
import OpenapiJsClient from 'openapi-js-client';

let apiInstance = new OpenapiJsClient.V1Api();
let shopperId = "shopperId_example"; // String | The ID of the Shopper to update
let shopperUpdate = new OpenapiJsClient.ShopperUpdate(); // ShopperUpdate | The Shopper details to update
apiInstance.update(shopperId, shopperUpdate, (error, data, response) => {
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
 **shopperId** | **String**| The ID of the Shopper to update | 
 **shopperUpdate** | [**ShopperUpdate**](ShopperUpdate.md)| The Shopper details to update | 

### Return type

[**ShopperId**](ShopperId.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml, text/xml
- **Accept**: application/javascript, application/json, application/xml, text/javascript, text/xml

