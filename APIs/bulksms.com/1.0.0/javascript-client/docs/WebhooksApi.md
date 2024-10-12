# BulkSmsJsonRestApi.WebhooksApi

All URIs are relative to *https://api.bulksms.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**webhooksGet**](WebhooksApi.md#webhooksGet) | **GET** /webhooks | List webhooks
[**webhooksIdDelete**](WebhooksApi.md#webhooksIdDelete) | **DELETE** /webhooks/{id} | Delete a webhook
[**webhooksIdGet**](WebhooksApi.md#webhooksIdGet) | **GET** /webhooks/{id} | Read a webhook
[**webhooksIdPost**](WebhooksApi.md#webhooksIdPost) | **POST** /webhooks/{id} | Update a webhook
[**webhooksPost**](WebhooksApi.md#webhooksPost) | **POST** /webhooks | Create a webhook



## webhooksGet

> [Webhook] webhooksGet()

List webhooks

Contains a list of your webhooks

### Example

```javascript
import BulkSmsJsonRestApi from 'bulk_sms_json_rest_api';
let defaultClient = BulkSmsJsonRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new BulkSmsJsonRestApi.WebhooksApi();
apiInstance.webhooksGet((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**[Webhook]**](Webhook.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webhooksIdDelete

> webhooksIdDelete(id)

Delete a webhook

### Example

```javascript
import BulkSmsJsonRestApi from 'bulk_sms_json_rest_api';
let defaultClient = BulkSmsJsonRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new BulkSmsJsonRestApi.WebhooksApi();
let id = "id_example"; // String | The `id` of the webhook
apiInstance.webhooksIdDelete(id, (error, data, response) => {
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
 **id** | **String**| The &#x60;id&#x60; of the webhook | 

### Return type

null (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webhooksIdGet

> Webhook webhooksIdGet(id)

Read a webhook

### Example

```javascript
import BulkSmsJsonRestApi from 'bulk_sms_json_rest_api';
let defaultClient = BulkSmsJsonRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new BulkSmsJsonRestApi.WebhooksApi();
let id = "id_example"; // String | The `id` of the webhook
apiInstance.webhooksIdGet(id, (error, data, response) => {
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
 **id** | **String**| The &#x60;id&#x60; of the webhook | 

### Return type

[**Webhook**](Webhook.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webhooksIdPost

> Webhook webhooksIdPost(id, webhookEntry)

Update a webhook

### Example

```javascript
import BulkSmsJsonRestApi from 'bulk_sms_json_rest_api';
let defaultClient = BulkSmsJsonRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new BulkSmsJsonRestApi.WebhooksApi();
let id = "id_example"; // String | The `id` of the webhook
let webhookEntry = new BulkSmsJsonRestApi.WebhookEntry(); // WebhookEntry | Contains the new property values for the webhook 
apiInstance.webhooksIdPost(id, webhookEntry, (error, data, response) => {
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
 **id** | **String**| The &#x60;id&#x60; of the webhook | 
 **webhookEntry** | [**WebhookEntry**](WebhookEntry.md)| Contains the new property values for the webhook  | 

### Return type

[**Webhook**](Webhook.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## webhooksPost

> Webhook webhooksPost(webhookEntry)

Create a webhook

A webhook is an URL that you can register when you want the BulkSMS system to notify you about your messages. You can register multiple webhooks, and each one will be called.  (Note: you can also use our [Web App](https://www.bulksms.com/account/#!/advanced-settings/webhooks) to manage your webhooks interactively.)   If you want to be notified of &#x60;SENT&#x60; messages and &#x60;RECEIVED&#x60; messages you need to create two webhooks.   ### Implementing your webhook  Code samples of Webhook implementations: * [PHP](samples/webhook-php.html)  When you implement your webhook, there are a few rules to be aware of: - Your webhook must process &#x60;POST&#x60; requests that contains an array of messages in the post body.  This input given to your webhook has the same structure as the output produced when you call [Retrieve Messages](#tag/Message%2Fpaths%2F~1messages%2Fget). - When you register or update your webhook, the URL will be tested by invoking it with an empty array (&#x60;[]&#x60;).  - It is possible for your webhook to receive multiple updates for the same message and status. It happens from time to time that the mobile network duplicates status updates. - The order by which the webhook is invoked can be unexpected.  For example, if sender A replies before sender B, your webhook might get the reply from B first. - The webhook is expected to comply with good practices with regard to the status code it responds with.   - A status code in the &#x60;1xx&#x60; and &#x60;2xx&#x60; range is taken as an acknowledgement that the invocation was received and that the webhook host is ready to receive another.   - A status code in the &#x60;4xx&#x60; range is taken as a permanent problem and indicates that the webhook cannot process the message. The specific message that caused the error will be discarded, but your webhook will be invoked again when another message becomes available.   - Any other status code will be taken as a temporary problem; and indicates that the BulkSMS system should retry. The specific message that caused the error will not be discarded and your webhook will be invoked again with this message (see the subsequent section for more details on retry processing). - Your webhook has to respond within &#x60;30&#x60; seconds.  If no response is given in this time, the invocation will be retried. - It is good idea to add a secret to your URL in order to make it more secure. Here is an example: &#x60;https://www.example.com/hook.php?secret&#x3D;pass763265word&#x60; - You can use a non-standard port if necessary, for example: &#x60;https://www.example.com:8321/hook.php?secret&#x3D;pass763265word&#x60; - Your webhook can be called from a dynamic range of IP addresses, and you should be prepared to accept that the source IP can change in the future, without notice. This practice has become common with cloud-hosted solutions. If this is an insurmountable problem for your organisation, please contact support.  ### Testing and troubleshooting          Use &#x60;curl&#x60; to test your webhook.  The command below is a template that shows how the BulkSMS system invokes your code. It must return &#x60;200&#x60; for your URL before you can register it as a webhook.   &#x60;&#x60;&#x60; curl -i -X POST &#39;YOUR_URL_HERE&#39; --header &#39;Content-Type: application/json&#39; --header &#39;User-Agent: BulkSMS Invoker&#39; --data-raw &#39;[]&#39; &#x60;&#x60;&#x60;  When a &#x60;200&#x60; is returned for an empty array, modify the template to post multiple messages by adding JSON between the square brackets (&#39;[]&#39;).  After your webhook is successfully registered, you can send a message to &#x60;1111111&#x60; for an end-to-end test.  The delivery to this test number will fail, but your webhook will be invoked (and there are no charges).    ### The retry process  The process the BulkSMS systems follow to handle retries is roughly the following: - The first retry is scheduled for 90 seconds into the future. - After the first retry, subsequent failures will have longer delays, following this sequence - 3 minutes, 6 minutes, 12 minutes thereafter the message will be retried every 15 minutes for a 2 day period. - When all retries fail, the message will be discarded.  ### Problem reports via email  Your are strongly advised to provide an email address when you register your webhook. A notice will be sent to this email address to keep you in the loop whenever there are problems with your webhook. In order to prevent your inbox from being flooded, the system sends a notice about an observed error no more than once in a 24 hour period.  The following emails can be expected  - A __message retrying__ email is sent after an invocation has failed with a retry-able error.  This email is an early warning, allowing you to investigate your systems.  - A __message discarded__ email is sent after failure email is send when a message is discarded as a consequence of a non-retry-able error. 

### Example

```javascript
import BulkSmsJsonRestApi from 'bulk_sms_json_rest_api';
let defaultClient = BulkSmsJsonRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new BulkSmsJsonRestApi.WebhooksApi();
let webhookEntry = new BulkSmsJsonRestApi.WebhookEntry(); // WebhookEntry | Contains the property values for your new webhook 
apiInstance.webhooksPost(webhookEntry, (error, data, response) => {
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
 **webhookEntry** | [**WebhookEntry**](WebhookEntry.md)| Contains the property values for your new webhook  | 

### Return type

[**Webhook**](Webhook.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

