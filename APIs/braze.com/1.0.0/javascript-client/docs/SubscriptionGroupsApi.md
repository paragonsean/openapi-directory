# BrazeEndpoints.SubscriptionGroupsApi

All URIs are relative to *https://rest.iad-01.braze.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**listUsersSubscriptionGroupSms**](SubscriptionGroupsApi.md#listUsersSubscriptionGroupSms) | **GET** /subscription/user/status | List User&#39;s Subscription Group - SMS
[**listUsersSubscriptionGroupStatusSms**](SubscriptionGroupsApi.md#listUsersSubscriptionGroupStatusSms) | **GET** /subscription/status/get | List User&#39;s  Subscription Group Status - SMS



## listUsersSubscriptionGroupSms

> listUsersSubscriptionGroupSms(opts)

List User&#39;s Subscription Group - SMS

Use the endpoint below to list and get the subscription groups of a certain user.  &gt; If there are multiple users (multiple external ids) who share the same email address, all users will be returned as a separate user (even if they have the same email address or subscription group).

### Example

```javascript
import BrazeEndpoints from 'braze_endpoints';

let apiInstance = new BrazeEndpoints.SubscriptionGroupsApi();
let opts = {
  'externalId': "{{external_id}}", // String | (Required*) String  The external_id of the user. Must include at least one and at most 50 `external_ids`.
  'limit': "100", // String | (Optional) Integer  The limit on the maximum number of results returned. Default (and max) limit is 100.
  'offset': "1", // String | (Optional) Integer  Number of templates to skip before returning rest of the templates that fit the search criteria.
  'phone': "+11112223333" // String | (Required*) String  The phone number of the user (must include at least one phone number and at most 50 phone numbers). The recommendation is to provide this in the E.164 format. 
};
apiInstance.listUsersSubscriptionGroupSms(opts, (error, data, response) => {
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
 **externalId** | **String**| (Required*) String  The external_id of the user. Must include at least one and at most 50 &#x60;external_ids&#x60;. | [optional] 
 **limit** | **String**| (Optional) Integer  The limit on the maximum number of results returned. Default (and max) limit is 100. | [optional] 
 **offset** | **String**| (Optional) Integer  Number of templates to skip before returning rest of the templates that fit the search criteria. | [optional] 
 **phone** | **String**| (Required*) String  The phone number of the user (must include at least one phone number and at most 50 phone numbers). The recommendation is to provide this in the E.164 format.  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## listUsersSubscriptionGroupStatusSms

> listUsersSubscriptionGroupStatusSms(opts)

List User&#39;s  Subscription Group Status - SMS

Use the endpoint below to get the subscription state of a user in a subscription group. The response from this endpoint will include the external ID and either subscribed, unsubscribed, or unknown for the specific subscription group requested in the API call. This can be used to update the subscription group state in subsequent API calls or to be displayed on a hosted web page.  &gt; *Either &#x60;external_id&#x60; or &#x60;email&#x60; are required.  ## Response  All successful responses will return &#x60;subscribed&#x60;, &#x60;unsubscribed&#x60;, or &#x60;unknown&#x60; depending on status and user history with the subscription group.  &#x60;&#x60;&#x60;json Content-Type: application/json Authorization: Bearer YOUR-REST-API-KEY {   \&quot;status\&quot;: {     \&quot;1\&quot;: \&quot;Unsubscribed\&quot;,     \&quot;2\&quot;: \&quot;Subscribed\&quot;   },   \&quot;message\&quot;: \&quot;success\&quot; } &#x60;&#x60;&#x60;

### Example

```javascript
import BrazeEndpoints from 'braze_endpoints';

let apiInstance = new BrazeEndpoints.SubscriptionGroupsApi();
let opts = {
  'subscriptionGroupId': "{{subscription_group_id}}", // String | (Required) String  The `id` of your subscription group.
  'externalId': "{{external_identifier}}", // String | (Required*) String  The `external_id` of the user (must include at least one and at most 50 `external_ids`).  Only external_id or phone is accepted for SMS subscription groups 
  'phone': "+11112223333" // String | (Required*) String  The phone number of the user (must include at least one phone number and at most 50 phone numbers). The recommendation is to provide this in the E.164 format.  Only external_id or phone is accepted for SMS subscription groups 
};
apiInstance.listUsersSubscriptionGroupStatusSms(opts, (error, data, response) => {
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
 **subscriptionGroupId** | **String**| (Required) String  The &#x60;id&#x60; of your subscription group. | [optional] 
 **externalId** | **String**| (Required*) String  The &#x60;external_id&#x60; of the user (must include at least one and at most 50 &#x60;external_ids&#x60;).  Only external_id or phone is accepted for SMS subscription groups  | [optional] 
 **phone** | **String**| (Required*) String  The phone number of the user (must include at least one phone number and at most 50 phone numbers). The recommendation is to provide this in the E.164 format.  Only external_id or phone is accepted for SMS subscription groups  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

