# NexmoApplicationApi.DefaultApi

All URIs are relative to *https://api.nexmo.com/v1/applications*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createApplication**](DefaultApi.md#createApplication) | **POST** / | Create Application
[**deleteApplication**](DefaultApi.md#deleteApplication) | **DELETE** /{app_id} | Destroy Application
[**retrieveApplication**](DefaultApi.md#retrieveApplication) | **GET** /{app_id} | Retrieve Application
[**retrieveApplications**](DefaultApi.md#retrieveApplications) | **GET** / | Retrieve all Applications
[**updateApplication**](DefaultApi.md#updateApplication) | **PUT** /{app_id} | Update Application



## createApplication

> ApplicationCreated createApplication(opts)

Create Application

You use a &#x60;POST&#x60; request to create a new application.

### Example

```javascript
import NexmoApplicationApi from 'nexmo_application_api';

let apiInstance = new NexmoApplicationApi.DefaultApi();
let opts = {
  'createApplicationRequest': new NexmoApplicationApi.CreateApplicationRequest() // CreateApplicationRequest | 
};
apiInstance.createApplication(opts, (error, data, response) => {
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
 **createApplicationRequest** | [**CreateApplicationRequest**](CreateApplicationRequest.md)|  | [optional] 

### Return type

[**ApplicationCreated**](ApplicationCreated.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteApplication

> deleteApplication(appId)

Destroy Application

You use a &#x60;DELETE&#x60; request to delete a single application.

### Example

```javascript
import NexmoApplicationApi from 'nexmo_application_api';

let apiInstance = new NexmoApplicationApi.DefaultApi();
let appId = "aaaaaaaa-bbbb-cccc-dddd-0123456789ab"; // String | The ID allocated to your application by Nexmo.
apiInstance.deleteApplication(appId, (error, data, response) => {
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
 **appId** | **String**| The ID allocated to your application by Nexmo. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## retrieveApplication

> Application retrieveApplication(apiKey, apiSecret, appId)

Retrieve Application

You use a &#x60;GET&#x60; request to retrieve details about a single application.

### Example

```javascript
import NexmoApplicationApi from 'nexmo_application_api';

let apiInstance = new NexmoApplicationApi.DefaultApi();
let apiKey = "apiKey_example"; // String | You can find your API key in your [account overview](https://dashboard.nexmo.com/account-overview)
let apiSecret = "apiSecret_example"; // String | You can find your API secret in your [account overview](https://dashboard.nexmo.com/account-overview)
let appId = "aaaaaaaa-bbbb-cccc-dddd-0123456789ab"; // String | The ID allocated to your application by Nexmo.
apiInstance.retrieveApplication(apiKey, apiSecret, appId, (error, data, response) => {
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
 **apiKey** | **String**| You can find your API key in your [account overview](https://dashboard.nexmo.com/account-overview) | 
 **apiSecret** | **String**| You can find your API secret in your [account overview](https://dashboard.nexmo.com/account-overview) | 
 **appId** | **String**| The ID allocated to your application by Nexmo. | 

### Return type

[**Application**](Application.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## retrieveApplications

> Applications retrieveApplications(apiKey, apiSecret, opts)

Retrieve all Applications

You use a &#x60;GET&#x60; request to retrieve details of all applications associated with your account.

### Example

```javascript
import NexmoApplicationApi from 'nexmo_application_api';

let apiInstance = new NexmoApplicationApi.DefaultApi();
let apiKey = "apiKey_example"; // String | You can find your API key in your [account overview](https://dashboard.nexmo.com/account-overview)
let apiSecret = "apiSecret_example"; // String | You can find your API secret in your [account overview](https://dashboard.nexmo.com/account-overview)
let opts = {
  'pageSize': 10, // Number | Set the number of items returned on each call to this endpoint. The default is 10 records.
  'pageIndex': 0 // Number | Set the offset from the first page. The default value is `0`.
};
apiInstance.retrieveApplications(apiKey, apiSecret, opts, (error, data, response) => {
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
 **apiKey** | **String**| You can find your API key in your [account overview](https://dashboard.nexmo.com/account-overview) | 
 **apiSecret** | **String**| You can find your API secret in your [account overview](https://dashboard.nexmo.com/account-overview) | 
 **pageSize** | **Number**| Set the number of items returned on each call to this endpoint. The default is 10 records. | [optional] [default to 10]
 **pageIndex** | **Number**| Set the offset from the first page. The default value is &#x60;0&#x60;. | [optional] [default to 0]

### Return type

[**Applications**](Applications.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateApplication

> Application updateApplication(appId, opts)

Update Application

You use a &#x60;PUT&#x60; request to update an existing application.

### Example

```javascript
import NexmoApplicationApi from 'nexmo_application_api';

let apiInstance = new NexmoApplicationApi.DefaultApi();
let appId = "aaaaaaaa-bbbb-cccc-dddd-0123456789ab"; // String | The ID allocated to your application by Nexmo.
let opts = {
  'updateApplicationRequest': new NexmoApplicationApi.UpdateApplicationRequest() // UpdateApplicationRequest | 
};
apiInstance.updateApplication(appId, opts, (error, data, response) => {
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
 **appId** | **String**| The ID allocated to your application by Nexmo. | 
 **updateApplicationRequest** | [**UpdateApplicationRequest**](UpdateApplicationRequest.md)|  | [optional] 

### Return type

[**Application**](Application.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

