# TwilioFax.DefaultApi

All URIs are relative to *https://fax.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteFax**](DefaultApi.md#deleteFax) | **DELETE** /v1/Faxes/{Sid} | 
[**deleteFaxMedia**](DefaultApi.md#deleteFaxMedia) | **DELETE** /v1/Faxes/{FaxSid}/Media/{Sid} | 
[**fetchFax**](DefaultApi.md#fetchFax) | **GET** /v1/Faxes/{Sid} | 
[**fetchFaxMedia**](DefaultApi.md#fetchFaxMedia) | **GET** /v1/Faxes/{FaxSid}/Media/{Sid} | 
[**listFax**](DefaultApi.md#listFax) | **GET** /v1/Faxes | 
[**listFaxMedia**](DefaultApi.md#listFaxMedia) | **GET** /v1/Faxes/{FaxSid}/Media | 



## deleteFax

> deleteFax(sid)



Delete a specific fax and its associated media.

### Example

```javascript
import TwilioFax from 'twilio_fax';
let defaultClient = TwilioFax.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioFax.DefaultApi();
let sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the Fax resource to delete.
apiInstance.deleteFax(sid, (error, data, response) => {
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
 **sid** | **String**| The Twilio-provided string that uniquely identifies the Fax resource to delete. | 

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteFaxMedia

> deleteFaxMedia(faxSid, sid)



Delete a specific fax media instance.

### Example

```javascript
import TwilioFax from 'twilio_fax';
let defaultClient = TwilioFax.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioFax.DefaultApi();
let faxSid = "faxSid_example"; // String | The SID of the fax with the FaxMedia resource to delete.
let sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the FaxMedia resource to delete.
apiInstance.deleteFaxMedia(faxSid, sid, (error, data, response) => {
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
 **faxSid** | **String**| The SID of the fax with the FaxMedia resource to delete. | 
 **sid** | **String**| The Twilio-provided string that uniquely identifies the FaxMedia resource to delete. | 

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## fetchFax

> FaxV1Fax fetchFax(sid)



Fetch a specific fax.

### Example

```javascript
import TwilioFax from 'twilio_fax';
let defaultClient = TwilioFax.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioFax.DefaultApi();
let sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the Fax resource to fetch.
apiInstance.fetchFax(sid, (error, data, response) => {
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
 **sid** | **String**| The Twilio-provided string that uniquely identifies the Fax resource to fetch. | 

### Return type

[**FaxV1Fax**](FaxV1Fax.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## fetchFaxMedia

> FaxV1FaxFaxMedia fetchFaxMedia(faxSid, sid)



Fetch a specific fax media instance.

### Example

```javascript
import TwilioFax from 'twilio_fax';
let defaultClient = TwilioFax.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioFax.DefaultApi();
let faxSid = "faxSid_example"; // String | The SID of the fax with the FaxMedia resource to fetch.
let sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the FaxMedia resource to fetch.
apiInstance.fetchFaxMedia(faxSid, sid, (error, data, response) => {
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
 **faxSid** | **String**| The SID of the fax with the FaxMedia resource to fetch. | 
 **sid** | **String**| The Twilio-provided string that uniquely identifies the FaxMedia resource to fetch. | 

### Return type

[**FaxV1FaxFaxMedia**](FaxV1FaxFaxMedia.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listFax

> ListFaxResponse listFax(opts)



Retrieve a list of all faxes.

### Example

```javascript
import TwilioFax from 'twilio_fax';
let defaultClient = TwilioFax.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioFax.DefaultApi();
let opts = {
  'from': "from_example", // String | Retrieve only those faxes sent from this phone number, specified in [E.164](https://www.twilio.com/docs/glossary/what-e164) format.
  'to': "to_example", // String | Retrieve only those faxes sent to this phone number, specified in [E.164](https://www.twilio.com/docs/glossary/what-e164) format.
  'dateCreatedOnOrBefore': new Date("2013-10-20T19:20:30+01:00"), // Date | Retrieve only those faxes with a `date_created` that is before or equal to this value, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
  'dateCreatedAfter': new Date("2013-10-20T19:20:30+01:00"), // Date | Retrieve only those faxes with a `date_created` that is later than this value, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
  'pageSize': 56 // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
};
apiInstance.listFax(opts, (error, data, response) => {
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
 **from** | **String**| Retrieve only those faxes sent from this phone number, specified in [E.164](https://www.twilio.com/docs/glossary/what-e164) format. | [optional] 
 **to** | **String**| Retrieve only those faxes sent to this phone number, specified in [E.164](https://www.twilio.com/docs/glossary/what-e164) format. | [optional] 
 **dateCreatedOnOrBefore** | **Date**| Retrieve only those faxes with a &#x60;date_created&#x60; that is before or equal to this value, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. | [optional] 
 **dateCreatedAfter** | **Date**| Retrieve only those faxes with a &#x60;date_created&#x60; that is later than this value, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. | [optional] 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 

### Return type

[**ListFaxResponse**](ListFaxResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listFaxMedia

> ListFaxMediaResponse listFaxMedia(faxSid, opts)



Retrieve a list of all fax media instances for the specified fax.

### Example

```javascript
import TwilioFax from 'twilio_fax';
let defaultClient = TwilioFax.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioFax.DefaultApi();
let faxSid = "faxSid_example"; // String | The SID of the fax with the FaxMedia resources to read.
let opts = {
  'pageSize': 56 // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
};
apiInstance.listFaxMedia(faxSid, opts, (error, data, response) => {
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
 **faxSid** | **String**| The SID of the fax with the FaxMedia resources to read. | 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 

### Return type

[**ListFaxMediaResponse**](ListFaxMediaResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

