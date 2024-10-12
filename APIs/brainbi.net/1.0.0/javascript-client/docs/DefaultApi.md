# Brainbi.DefaultApi

All URIs are relative to *http://,*

Method | HTTP request | Description
------------- | ------------- | -------------
[**loginAndGetBearerToken**](DefaultApi.md#loginAndGetBearerToken) | **POST** /api/login | Login and get bearer token
[**logout**](DefaultApi.md#logout) | **POST** /api/logout | Logout
[**register**](DefaultApi.md#register) | **POST** /api/register | Register
[**registerAndCreateStoreConnectionForWooCommerce**](DefaultApi.md#registerAndCreateStoreConnectionForWooCommerce) | **POST** /api/register_woocommerce | Register and Create Store Connection for WooCommerce



## loginAndGetBearerToken

> loginAndGetBearerToken(opts)

Login and get bearer token

Use this endpoint to make the initial call with your email and password (same as on brainbi.net) and get your bearer token in response.

### Example

```javascript
import Brainbi from 'brainbi';

let apiInstance = new Brainbi.DefaultApi();
let opts = {
  'email': "{{email}}", // String | The same email you use for our platform.
  'password': "{{password}}" // String | The password email you use for our platform.
};
apiInstance.loginAndGetBearerToken(opts, (error, data, response) => {
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
 **email** | **String**| The same email you use for our platform. | [optional] 
 **password** | **String**| The password email you use for our platform. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## logout

> logout(opts)

Logout

Once you are done, call this endpoint to lock your account!

### Example

```javascript
import Brainbi from 'brainbi';

let apiInstance = new Brainbi.DefaultApi();
let opts = {
  'email': "{{email}}" // String | The same email you use for our platform.
};
apiInstance.logout(opts, (error, data, response) => {
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
 **email** | **String**| The same email you use for our platform. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## register

> register(opts)

Register

Use this endpoint to make the initial call with your email and password (same as on brainbi.net) and get your bearer token in response.

### Example

```javascript
import Brainbi from 'brainbi';

let apiInstance = new Brainbi.DefaultApi();
let opts = {
  'firstName': "Felix", // String | required
  'lastName': "Weber", // String | required
  'companyName': "Fiverr", // String | required
  'shopUrl': "https;//www.fiverr.de", // String | required
  'email': "fiverr2@fiverr.de", // String | required
  'storeName': "Fiverr Store", // String | required
  'storeUrl': "https;//www.fiverr.de", // String | required
  'password': "12345678", // String | required
  'fromuser': "1" // String | required (always 1)
};
apiInstance.register(opts, (error, data, response) => {
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
 **firstName** | **String**| required | [optional] 
 **lastName** | **String**| required | [optional] 
 **companyName** | **String**| required | [optional] 
 **shopUrl** | **String**| required | [optional] 
 **email** | **String**| required | [optional] 
 **storeName** | **String**| required | [optional] 
 **storeUrl** | **String**| required | [optional] 
 **password** | **String**| required | [optional] 
 **fromuser** | **String**| required (always 1) | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## registerAndCreateStoreConnectionForWooCommerce

> registerAndCreateStoreConnectionForWooCommerce(opts)

Register and Create Store Connection for WooCommerce

Use this endpoint to make the initial call with your email and password (same as on brainbi.net) and get your bearer token in response.

### Example

```javascript
import Brainbi from 'brainbi';

let apiInstance = new Brainbi.DefaultApi();
let opts = {
  'firstName': "Felix", // String | required
  'lastName': "Weber", // String | required
  'companyName': "Fiverr", // String | required
  'shopUrl': "https;//www.fiverr.de", // String | required
  'email': "fiver3r23@fiverr.de", // String | required
  'storeName': "Fiverr Store", // String | required
  'storeUrl': "https;//www.fiverr.de", // String | required
  'password': "12345678", // String | required
  'fromuser': "1", // String | required (always 1)
  'apiUrl': "https://woocommerce-351439-1090797.cloudwaysapps.com/", // String | required
  'consumerKey': "ck_59b23d313ae372feaf211652c318fbe4501abda2", // String | required
  'consumerSecret': "cs_acc202d648bfa6b69efe553bb25086230ba116a7" // String | required
};
apiInstance.registerAndCreateStoreConnectionForWooCommerce(opts, (error, data, response) => {
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
 **firstName** | **String**| required | [optional] 
 **lastName** | **String**| required | [optional] 
 **companyName** | **String**| required | [optional] 
 **shopUrl** | **String**| required | [optional] 
 **email** | **String**| required | [optional] 
 **storeName** | **String**| required | [optional] 
 **storeUrl** | **String**| required | [optional] 
 **password** | **String**| required | [optional] 
 **fromuser** | **String**| required (always 1) | [optional] 
 **apiUrl** | **String**| required | [optional] 
 **consumerKey** | **String**| required | [optional] 
 **consumerSecret** | **String**| required | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

