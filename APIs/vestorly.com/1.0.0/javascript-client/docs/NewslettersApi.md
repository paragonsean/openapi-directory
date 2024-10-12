# VestorlyApi.NewslettersApi

All URIs are relative to *https://staging.vestorly.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**findNewsletters**](NewslettersApi.md#findNewsletters) | **GET** /newsletters | 
[**getNewsletterByID**](NewslettersApi.md#getNewsletterByID) | **GET** /newsletters/{id} | 
[**updateNewsletterByID**](NewslettersApi.md#updateNewsletterByID) | **PUT** /newsletters/{id} | 



## findNewsletters

> Newsletters findNewsletters(vestorlyAuth, opts)



Returns all newsletters

### Example

```javascript
import VestorlyApi from 'vestorly_api';
let defaultClient = VestorlyApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VestorlyApi.NewslettersApi();
let vestorlyAuth = "vestorlyAuth_example"; // String | Vestorly Auth Token
let opts = {
  'accessToken': "accessToken_example" // String | OAuth Token
};
apiInstance.findNewsletters(vestorlyAuth, opts, (error, data, response) => {
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
 **vestorlyAuth** | **String**| Vestorly Auth Token | 
 **accessToken** | **String**| OAuth Token | [optional] 

### Return type

[**Newsletters**](Newsletters.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getNewsletterByID

> Newsletterresponse getNewsletterByID(vestorlyAuth, id, opts)



Get a newsletter by ID

### Example

```javascript
import VestorlyApi from 'vestorly_api';
let defaultClient = VestorlyApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VestorlyApi.NewslettersApi();
let vestorlyAuth = "vestorlyAuth_example"; // String | Vestorly Auth Token
let id = "id_example"; // String | Mongo ID of event to get
let opts = {
  'accessToken': "accessToken_example" // String | OAuth Token
};
apiInstance.getNewsletterByID(vestorlyAuth, id, opts, (error, data, response) => {
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
 **vestorlyAuth** | **String**| Vestorly Auth Token | 
 **id** | **String**| Mongo ID of event to get | 
 **accessToken** | **String**| OAuth Token | [optional] 

### Return type

[**Newsletterresponse**](Newsletterresponse.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## updateNewsletterByID

> Newsletterresponse updateNewsletterByID(vestorlyAuth, id, newsletter, opts)



Updates a newsletter

### Example

```javascript
import VestorlyApi from 'vestorly_api';
let defaultClient = VestorlyApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VestorlyApi.NewslettersApi();
let vestorlyAuth = "vestorlyAuth_example"; // String | Vestorly Auth Token
let id = "id_example"; // String | Mongo ID of event to update
let newsletter = new VestorlyApi.NewsletterInput(); // NewsletterInput | Newsletter
let opts = {
  'accessToken': "accessToken_example" // String | OAuth Token
};
apiInstance.updateNewsletterByID(vestorlyAuth, id, newsletter, opts, (error, data, response) => {
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
 **vestorlyAuth** | **String**| Vestorly Auth Token | 
 **id** | **String**| Mongo ID of event to update | 
 **newsletter** | [**NewsletterInput**](NewsletterInput.md)| Newsletter | 
 **accessToken** | **String**| OAuth Token | [optional] 

### Return type

[**Newsletterresponse**](Newsletterresponse.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

