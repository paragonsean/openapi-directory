# InfluxOssApiService.TelegrafsApi

All URIs are relative to */api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteTelegrafsID**](TelegrafsApi.md#deleteTelegrafsID) | **DELETE** /telegrafs/{telegrafID} | Delete a Telegraf configuration
[**deleteTelegrafsIDLabelsID**](TelegrafsApi.md#deleteTelegrafsIDLabelsID) | **DELETE** /telegrafs/{telegrafID}/labels/{labelID} | Delete a label from a Telegraf config
[**deleteTelegrafsIDMembersID**](TelegrafsApi.md#deleteTelegrafsIDMembersID) | **DELETE** /telegrafs/{telegrafID}/members/{userID} | Remove a member from a Telegraf config
[**deleteTelegrafsIDOwnersID**](TelegrafsApi.md#deleteTelegrafsIDOwnersID) | **DELETE** /telegrafs/{telegrafID}/owners/{userID} | Remove an owner from a Telegraf config
[**getTelegrafs**](TelegrafsApi.md#getTelegrafs) | **GET** /telegrafs | List all Telegraf configurations
[**getTelegrafsID**](TelegrafsApi.md#getTelegrafsID) | **GET** /telegrafs/{telegrafID} | Retrieve a Telegraf configuration
[**getTelegrafsIDLabels**](TelegrafsApi.md#getTelegrafsIDLabels) | **GET** /telegrafs/{telegrafID}/labels | List all labels for a Telegraf config
[**getTelegrafsIDMembers**](TelegrafsApi.md#getTelegrafsIDMembers) | **GET** /telegrafs/{telegrafID}/members | List all users with member privileges for a Telegraf config
[**getTelegrafsIDOwners**](TelegrafsApi.md#getTelegrafsIDOwners) | **GET** /telegrafs/{telegrafID}/owners | List all owners of a Telegraf configuration
[**postTelegrafs**](TelegrafsApi.md#postTelegrafs) | **POST** /telegrafs | Create a Telegraf configuration
[**postTelegrafsIDLabels**](TelegrafsApi.md#postTelegrafsIDLabels) | **POST** /telegrafs/{telegrafID}/labels | Add a label to a Telegraf config
[**postTelegrafsIDMembers**](TelegrafsApi.md#postTelegrafsIDMembers) | **POST** /telegrafs/{telegrafID}/members | Add a member to a Telegraf config
[**postTelegrafsIDOwners**](TelegrafsApi.md#postTelegrafsIDOwners) | **POST** /telegrafs/{telegrafID}/owners | Add an owner to a Telegraf configuration
[**putTelegrafsID**](TelegrafsApi.md#putTelegrafsID) | **PUT** /telegrafs/{telegrafID} | Update a Telegraf configuration



## deleteTelegrafsID

> deleteTelegrafsID(telegrafID, opts)

Delete a Telegraf configuration

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.TelegrafsApi();
let telegrafID = "telegrafID_example"; // String | The Telegraf configuration ID.
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}" // String | OpenTracing span context
};
apiInstance.deleteTelegrafsID(telegrafID, opts, (error, data, response) => {
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
 **telegrafID** | **String**| The Telegraf configuration ID. | 
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteTelegrafsIDLabelsID

> deleteTelegrafsIDLabelsID(telegrafID, labelID, opts)

Delete a label from a Telegraf config

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.TelegrafsApi();
let telegrafID = "telegrafID_example"; // String | The Telegraf config ID.
let labelID = "labelID_example"; // String | The label ID.
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}" // String | OpenTracing span context
};
apiInstance.deleteTelegrafsIDLabelsID(telegrafID, labelID, opts, (error, data, response) => {
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
 **telegrafID** | **String**| The Telegraf config ID. | 
 **labelID** | **String**| The label ID. | 
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteTelegrafsIDMembersID

> deleteTelegrafsIDMembersID(userID, telegrafID, opts)

Remove a member from a Telegraf config

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.TelegrafsApi();
let userID = "userID_example"; // String | The ID of the member to remove.
let telegrafID = "telegrafID_example"; // String | The Telegraf config ID.
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}" // String | OpenTracing span context
};
apiInstance.deleteTelegrafsIDMembersID(userID, telegrafID, opts, (error, data, response) => {
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
 **userID** | **String**| The ID of the member to remove. | 
 **telegrafID** | **String**| The Telegraf config ID. | 
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteTelegrafsIDOwnersID

> deleteTelegrafsIDOwnersID(userID, telegrafID, opts)

Remove an owner from a Telegraf config

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.TelegrafsApi();
let userID = "userID_example"; // String | The ID of the owner to remove.
let telegrafID = "telegrafID_example"; // String | The Telegraf config ID.
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}" // String | OpenTracing span context
};
apiInstance.deleteTelegrafsIDOwnersID(userID, telegrafID, opts, (error, data, response) => {
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
 **userID** | **String**| The ID of the owner to remove. | 
 **telegrafID** | **String**| The Telegraf config ID. | 
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTelegrafs

> Telegrafs getTelegrafs(opts)

List all Telegraf configurations

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.TelegrafsApi();
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}", // String | OpenTracing span context
  'orgID': "orgID_example" // String | The organization ID the Telegraf config belongs to.
};
apiInstance.getTelegrafs(opts, (error, data, response) => {
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
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 
 **orgID** | **String**| The organization ID the Telegraf config belongs to. | [optional] 

### Return type

[**Telegrafs**](Telegrafs.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTelegrafsID

> Telegraf getTelegrafsID(telegrafID, opts)

Retrieve a Telegraf configuration

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.TelegrafsApi();
let telegrafID = "telegrafID_example"; // String | The Telegraf configuration ID.
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}", // String | OpenTracing span context
  'accept': "'application/toml'" // String | 
};
apiInstance.getTelegrafsID(telegrafID, opts, (error, data, response) => {
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
 **telegrafID** | **String**| The Telegraf configuration ID. | 
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 
 **accept** | **String**|  | [optional] [default to &#39;application/toml&#39;]

### Return type

[**Telegraf**](Telegraf.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/octet-stream, application/toml


## getTelegrafsIDLabels

> LabelsResponse getTelegrafsIDLabels(telegrafID, opts)

List all labels for a Telegraf config

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.TelegrafsApi();
let telegrafID = "telegrafID_example"; // String | The Telegraf config ID.
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}" // String | OpenTracing span context
};
apiInstance.getTelegrafsIDLabels(telegrafID, opts, (error, data, response) => {
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
 **telegrafID** | **String**| The Telegraf config ID. | 
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 

### Return type

[**LabelsResponse**](LabelsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTelegrafsIDMembers

> ResourceMembers getTelegrafsIDMembers(telegrafID, opts)

List all users with member privileges for a Telegraf config

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.TelegrafsApi();
let telegrafID = "telegrafID_example"; // String | The Telegraf config ID.
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}" // String | OpenTracing span context
};
apiInstance.getTelegrafsIDMembers(telegrafID, opts, (error, data, response) => {
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
 **telegrafID** | **String**| The Telegraf config ID. | 
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 

### Return type

[**ResourceMembers**](ResourceMembers.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTelegrafsIDOwners

> ResourceOwners getTelegrafsIDOwners(telegrafID, opts)

List all owners of a Telegraf configuration

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.TelegrafsApi();
let telegrafID = "telegrafID_example"; // String | The Telegraf configuration ID.
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}" // String | OpenTracing span context
};
apiInstance.getTelegrafsIDOwners(telegrafID, opts, (error, data, response) => {
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
 **telegrafID** | **String**| The Telegraf configuration ID. | 
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 

### Return type

[**ResourceOwners**](ResourceOwners.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## postTelegrafs

> Telegraf postTelegrafs(telegrafRequest, opts)

Create a Telegraf configuration

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.TelegrafsApi();
let telegrafRequest = new InfluxOssApiService.TelegrafRequest(); // TelegrafRequest | Telegraf configuration to create
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}" // String | OpenTracing span context
};
apiInstance.postTelegrafs(telegrafRequest, opts, (error, data, response) => {
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
 **telegrafRequest** | [**TelegrafRequest**](TelegrafRequest.md)| Telegraf configuration to create | 
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 

### Return type

[**Telegraf**](Telegraf.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postTelegrafsIDLabels

> LabelResponse postTelegrafsIDLabels(telegrafID, labelMapping, opts)

Add a label to a Telegraf config

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.TelegrafsApi();
let telegrafID = "telegrafID_example"; // String | The Telegraf config ID.
let labelMapping = new InfluxOssApiService.LabelMapping(); // LabelMapping | Label to add
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}" // String | OpenTracing span context
};
apiInstance.postTelegrafsIDLabels(telegrafID, labelMapping, opts, (error, data, response) => {
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
 **telegrafID** | **String**| The Telegraf config ID. | 
 **labelMapping** | [**LabelMapping**](LabelMapping.md)| Label to add | 
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 

### Return type

[**LabelResponse**](LabelResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postTelegrafsIDMembers

> ResourceMember postTelegrafsIDMembers(telegrafID, addResourceMemberRequestBody, opts)

Add a member to a Telegraf config

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.TelegrafsApi();
let telegrafID = "telegrafID_example"; // String | The Telegraf config ID.
let addResourceMemberRequestBody = new InfluxOssApiService.AddResourceMemberRequestBody(); // AddResourceMemberRequestBody | User to add as member
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}" // String | OpenTracing span context
};
apiInstance.postTelegrafsIDMembers(telegrafID, addResourceMemberRequestBody, opts, (error, data, response) => {
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
 **telegrafID** | **String**| The Telegraf config ID. | 
 **addResourceMemberRequestBody** | [**AddResourceMemberRequestBody**](AddResourceMemberRequestBody.md)| User to add as member | 
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 

### Return type

[**ResourceMember**](ResourceMember.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postTelegrafsIDOwners

> ResourceOwner postTelegrafsIDOwners(telegrafID, addResourceMemberRequestBody, opts)

Add an owner to a Telegraf configuration

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.TelegrafsApi();
let telegrafID = "telegrafID_example"; // String | The Telegraf configuration ID.
let addResourceMemberRequestBody = new InfluxOssApiService.AddResourceMemberRequestBody(); // AddResourceMemberRequestBody | User to add as owner
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}" // String | OpenTracing span context
};
apiInstance.postTelegrafsIDOwners(telegrafID, addResourceMemberRequestBody, opts, (error, data, response) => {
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
 **telegrafID** | **String**| The Telegraf configuration ID. | 
 **addResourceMemberRequestBody** | [**AddResourceMemberRequestBody**](AddResourceMemberRequestBody.md)| User to add as owner | 
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 

### Return type

[**ResourceOwner**](ResourceOwner.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## putTelegrafsID

> Telegraf putTelegrafsID(telegrafID, telegrafRequest, opts)

Update a Telegraf configuration

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.TelegrafsApi();
let telegrafID = "telegrafID_example"; // String | The Telegraf config ID.
let telegrafRequest = new InfluxOssApiService.TelegrafRequest(); // TelegrafRequest | Telegraf configuration update to apply
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}" // String | OpenTracing span context
};
apiInstance.putTelegrafsID(telegrafID, telegrafRequest, opts, (error, data, response) => {
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
 **telegrafID** | **String**| The Telegraf config ID. | 
 **telegrafRequest** | [**TelegrafRequest**](TelegrafRequest.md)| Telegraf configuration update to apply | 
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 

### Return type

[**Telegraf**](Telegraf.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

