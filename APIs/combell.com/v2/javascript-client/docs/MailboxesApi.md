# PublicApi.MailboxesApi

All URIs are relative to */v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**changeMailboxPassword**](MailboxesApi.md#changeMailboxPassword) | **PUT** /mailboxes/{mailboxName}/password | Change password for mailbox
[**configureMailboxAutoForward**](MailboxesApi.md#configureMailboxAutoForward) | **PUT** /mailboxes/{mailboxName}/autoforward | Configure auto-forward for mailbox
[**configureMailboxAutoReply**](MailboxesApi.md#configureMailboxAutoReply) | **PUT** /mailboxes/{mailboxName}/autoreply | Configure auto-reply for mailbox
[**createMailbox**](MailboxesApi.md#createMailbox) | **POST** /mailboxes | Create a new mailbox.
[**deleteMailbox**](MailboxesApi.md#deleteMailbox) | **DELETE** /mailboxes/{mailboxName} | Delete a mailbox
[**getMailbox**](MailboxesApi.md#getMailbox) | **GET** /mailboxes/{mailboxName} | Get a specific mailbox
[**getMailboxes**](MailboxesApi.md#getMailboxes) | **GET** /mailboxes | Gets your mailboxes.



## changeMailboxPassword

> changeMailboxPassword(mailboxName, mailboxName2, opts)

Change password for mailbox

### Example

```javascript
import PublicApi from 'public_api';

let apiInstance = new PublicApi.MailboxesApi();
let mailboxName = "mailboxName_example"; // String | Mailbox name.
let mailboxName2 = "mailboxName_example"; // String | Automatically added
let opts = {
  'updateMailboxPasswordRequest': new PublicApi.UpdateMailboxPasswordRequest() // UpdateMailboxPasswordRequest | Contains the new password.
};
apiInstance.changeMailboxPassword(mailboxName, mailboxName2, opts, (error, data, response) => {
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
 **mailboxName** | **String**| Mailbox name. | 
 **mailboxName2** | **String**| Automatically added | 
 **updateMailboxPasswordRequest** | [**UpdateMailboxPasswordRequest**](UpdateMailboxPasswordRequest.md)| Contains the new password. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## configureMailboxAutoForward

> configureMailboxAutoForward(mailboxName, mailboxName2, opts)

Configure auto-forward for mailbox

### Example

```javascript
import PublicApi from 'public_api';

let apiInstance = new PublicApi.MailboxesApi();
let mailboxName = "mailboxName_example"; // String | Mailbox name.
let mailboxName2 = "mailboxName_example"; // String | Automatically added
let opts = {
  'autoForward': new PublicApi.AutoForward() // AutoForward | Contains the auto-forward information.
};
apiInstance.configureMailboxAutoForward(mailboxName, mailboxName2, opts, (error, data, response) => {
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
 **mailboxName** | **String**| Mailbox name. | 
 **mailboxName2** | **String**| Automatically added | 
 **autoForward** | [**AutoForward**](AutoForward.md)| Contains the auto-forward information. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## configureMailboxAutoReply

> configureMailboxAutoReply(mailboxName, mailboxName2, opts)

Configure auto-reply for mailbox

### Example

```javascript
import PublicApi from 'public_api';

let apiInstance = new PublicApi.MailboxesApi();
let mailboxName = "mailboxName_example"; // String | Mailbox name.
let mailboxName2 = "mailboxName_example"; // String | Automatically added
let opts = {
  'autoReply': new PublicApi.AutoReply() // AutoReply | Contains the auto-reply information.
};
apiInstance.configureMailboxAutoReply(mailboxName, mailboxName2, opts, (error, data, response) => {
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
 **mailboxName** | **String**| Mailbox name. | 
 **mailboxName2** | **String**| Automatically added | 
 **autoReply** | [**AutoReply**](AutoReply.md)| Contains the auto-reply information. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## createMailbox

> createMailbox(opts)

Create a new mailbox.

### Example

```javascript
import PublicApi from 'public_api';

let apiInstance = new PublicApi.MailboxesApi();
let opts = {
  'createMailboxRequest': new PublicApi.CreateMailboxRequest() // CreateMailboxRequest | The add mailbox request.
};
apiInstance.createMailbox(opts, (error, data, response) => {
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
 **createMailboxRequest** | [**CreateMailboxRequest**](CreateMailboxRequest.md)| The add mailbox request. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## deleteMailbox

> deleteMailbox(mailboxName, mailboxName2)

Delete a mailbox

### Example

```javascript
import PublicApi from 'public_api';

let apiInstance = new PublicApi.MailboxesApi();
let mailboxName = "mailboxName_example"; // String | Mailbox name.
let mailboxName2 = "mailboxName_example"; // String | Automatically added
apiInstance.deleteMailbox(mailboxName, mailboxName2, (error, data, response) => {
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
 **mailboxName** | **String**| Mailbox name. | 
 **mailboxName2** | **String**| Automatically added | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getMailbox

> MailboxDetail getMailbox(mailboxName, mailboxName2)

Get a specific mailbox

### Example

```javascript
import PublicApi from 'public_api';

let apiInstance = new PublicApi.MailboxesApi();
let mailboxName = "mailboxName_example"; // String | Mailbox name.
let mailboxName2 = "mailboxName_example"; // String | Automatically added
apiInstance.getMailbox(mailboxName, mailboxName2, (error, data, response) => {
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
 **mailboxName** | **String**| Mailbox name. | 
 **mailboxName2** | **String**| Automatically added | 

### Return type

[**MailboxDetail**](MailboxDetail.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getMailboxes

> [Mailbox] getMailboxes(opts)

Gets your mailboxes.

Currently only supports getting the mailboxes filtered by domain name.

### Example

```javascript
import PublicApi from 'public_api';

let apiInstance = new PublicApi.MailboxesApi();
let opts = {
  'domainName': "domainName_example" // String | Obligated domain name for getting mailboxes.
};
apiInstance.getMailboxes(opts, (error, data, response) => {
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
 **domainName** | **String**| Obligated domain name for getting mailboxes. | [optional] 

### Return type

[**[Mailbox]**](Mailbox.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

