# InfluxOssApiService.ScraperTargetsApi

All URIs are relative to */api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteScrapersID**](ScraperTargetsApi.md#deleteScrapersID) | **DELETE** /scrapers/{scraperTargetID} | Delete a scraper target
[**deleteScrapersIDLabelsID**](ScraperTargetsApi.md#deleteScrapersIDLabelsID) | **DELETE** /scrapers/{scraperTargetID}/labels/{labelID} | Delete a label from a scraper target
[**deleteScrapersIDMembersID**](ScraperTargetsApi.md#deleteScrapersIDMembersID) | **DELETE** /scrapers/{scraperTargetID}/members/{userID} | Remove a member from a scraper target
[**deleteScrapersIDOwnersID**](ScraperTargetsApi.md#deleteScrapersIDOwnersID) | **DELETE** /scrapers/{scraperTargetID}/owners/{userID} | Remove an owner from a scraper target
[**getScrapers**](ScraperTargetsApi.md#getScrapers) | **GET** /scrapers | List all scraper targets
[**getScrapersID**](ScraperTargetsApi.md#getScrapersID) | **GET** /scrapers/{scraperTargetID} | Retrieve a scraper target
[**getScrapersIDLabels**](ScraperTargetsApi.md#getScrapersIDLabels) | **GET** /scrapers/{scraperTargetID}/labels | List all labels for a scraper target
[**getScrapersIDMembers**](ScraperTargetsApi.md#getScrapersIDMembers) | **GET** /scrapers/{scraperTargetID}/members | List all users with member privileges for a scraper target
[**getScrapersIDOwners**](ScraperTargetsApi.md#getScrapersIDOwners) | **GET** /scrapers/{scraperTargetID}/owners | List all owners of a scraper target
[**patchScrapersID**](ScraperTargetsApi.md#patchScrapersID) | **PATCH** /scrapers/{scraperTargetID} | Update a scraper target
[**postScrapers**](ScraperTargetsApi.md#postScrapers) | **POST** /scrapers | Create a scraper target
[**postScrapersIDLabels**](ScraperTargetsApi.md#postScrapersIDLabels) | **POST** /scrapers/{scraperTargetID}/labels | Add a label to a scraper target
[**postScrapersIDMembers**](ScraperTargetsApi.md#postScrapersIDMembers) | **POST** /scrapers/{scraperTargetID}/members | Add a member to a scraper target
[**postScrapersIDOwners**](ScraperTargetsApi.md#postScrapersIDOwners) | **POST** /scrapers/{scraperTargetID}/owners | Add an owner to a scraper target



## deleteScrapersID

> deleteScrapersID(scraperTargetID, opts)

Delete a scraper target

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.ScraperTargetsApi();
let scraperTargetID = "scraperTargetID_example"; // String | The identifier of the scraper target.
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}" // String | OpenTracing span context
};
apiInstance.deleteScrapersID(scraperTargetID, opts, (error, data, response) => {
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
 **scraperTargetID** | **String**| The identifier of the scraper target. | 
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteScrapersIDLabelsID

> deleteScrapersIDLabelsID(scraperTargetID, labelID, opts)

Delete a label from a scraper target

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.ScraperTargetsApi();
let scraperTargetID = "scraperTargetID_example"; // String | The scraper target ID.
let labelID = "labelID_example"; // String | The label ID.
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}" // String | OpenTracing span context
};
apiInstance.deleteScrapersIDLabelsID(scraperTargetID, labelID, opts, (error, data, response) => {
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
 **scraperTargetID** | **String**| The scraper target ID. | 
 **labelID** | **String**| The label ID. | 
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteScrapersIDMembersID

> deleteScrapersIDMembersID(userID, scraperTargetID, opts)

Remove a member from a scraper target

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.ScraperTargetsApi();
let userID = "userID_example"; // String | The ID of member to remove.
let scraperTargetID = "scraperTargetID_example"; // String | The scraper target ID.
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}" // String | OpenTracing span context
};
apiInstance.deleteScrapersIDMembersID(userID, scraperTargetID, opts, (error, data, response) => {
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
 **userID** | **String**| The ID of member to remove. | 
 **scraperTargetID** | **String**| The scraper target ID. | 
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteScrapersIDOwnersID

> deleteScrapersIDOwnersID(userID, scraperTargetID, opts)

Remove an owner from a scraper target

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.ScraperTargetsApi();
let userID = "userID_example"; // String | The ID of owner to remove.
let scraperTargetID = "scraperTargetID_example"; // String | The scraper target ID.
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}" // String | OpenTracing span context
};
apiInstance.deleteScrapersIDOwnersID(userID, scraperTargetID, opts, (error, data, response) => {
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
 **userID** | **String**| The ID of owner to remove. | 
 **scraperTargetID** | **String**| The scraper target ID. | 
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getScrapers

> ScraperTargetResponses getScrapers(opts)

List all scraper targets

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.ScraperTargetsApi();
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}", // String | OpenTracing span context
  'name': "name_example", // String | Specifies the name of the scraper target.
  'id': ["null"], // [String] | List of scraper target IDs to return. If both `id` and `owner` are specified, only `id` is used.
  'orgID': "orgID_example", // String | Specifies the organization ID of the scraper target.
  'org': "org_example" // String | Specifies the organization name of the scraper target.
};
apiInstance.getScrapers(opts, (error, data, response) => {
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
 **name** | **String**| Specifies the name of the scraper target. | [optional] 
 **id** | [**[String]**](String.md)| List of scraper target IDs to return. If both &#x60;id&#x60; and &#x60;owner&#x60; are specified, only &#x60;id&#x60; is used. | [optional] 
 **orgID** | **String**| Specifies the organization ID of the scraper target. | [optional] 
 **org** | **String**| Specifies the organization name of the scraper target. | [optional] 

### Return type

[**ScraperTargetResponses**](ScraperTargetResponses.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getScrapersID

> ScraperTargetResponse getScrapersID(scraperTargetID, opts)

Retrieve a scraper target

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.ScraperTargetsApi();
let scraperTargetID = "scraperTargetID_example"; // String | The identifier of the scraper target.
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}" // String | OpenTracing span context
};
apiInstance.getScrapersID(scraperTargetID, opts, (error, data, response) => {
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
 **scraperTargetID** | **String**| The identifier of the scraper target. | 
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 

### Return type

[**ScraperTargetResponse**](ScraperTargetResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getScrapersIDLabels

> LabelsResponse getScrapersIDLabels(scraperTargetID, opts)

List all labels for a scraper target

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.ScraperTargetsApi();
let scraperTargetID = "scraperTargetID_example"; // String | The scraper target ID.
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}" // String | OpenTracing span context
};
apiInstance.getScrapersIDLabels(scraperTargetID, opts, (error, data, response) => {
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
 **scraperTargetID** | **String**| The scraper target ID. | 
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 

### Return type

[**LabelsResponse**](LabelsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getScrapersIDMembers

> ResourceMembers getScrapersIDMembers(scraperTargetID, opts)

List all users with member privileges for a scraper target

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.ScraperTargetsApi();
let scraperTargetID = "scraperTargetID_example"; // String | The scraper target ID.
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}" // String | OpenTracing span context
};
apiInstance.getScrapersIDMembers(scraperTargetID, opts, (error, data, response) => {
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
 **scraperTargetID** | **String**| The scraper target ID. | 
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 

### Return type

[**ResourceMembers**](ResourceMembers.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getScrapersIDOwners

> ResourceOwners getScrapersIDOwners(scraperTargetID, opts)

List all owners of a scraper target

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.ScraperTargetsApi();
let scraperTargetID = "scraperTargetID_example"; // String | The scraper target ID.
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}" // String | OpenTracing span context
};
apiInstance.getScrapersIDOwners(scraperTargetID, opts, (error, data, response) => {
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
 **scraperTargetID** | **String**| The scraper target ID. | 
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 

### Return type

[**ResourceOwners**](ResourceOwners.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## patchScrapersID

> ScraperTargetResponse patchScrapersID(scraperTargetID, scraperTargetRequest, opts)

Update a scraper target

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.ScraperTargetsApi();
let scraperTargetID = "scraperTargetID_example"; // String | The identifier of the scraper target.
let scraperTargetRequest = new InfluxOssApiService.ScraperTargetRequest(); // ScraperTargetRequest | Scraper target update to apply
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}" // String | OpenTracing span context
};
apiInstance.patchScrapersID(scraperTargetID, scraperTargetRequest, opts, (error, data, response) => {
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
 **scraperTargetID** | **String**| The identifier of the scraper target. | 
 **scraperTargetRequest** | [**ScraperTargetRequest**](ScraperTargetRequest.md)| Scraper target update to apply | 
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 

### Return type

[**ScraperTargetResponse**](ScraperTargetResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postScrapers

> ScraperTargetResponse postScrapers(scraperTargetRequest, opts)

Create a scraper target

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.ScraperTargetsApi();
let scraperTargetRequest = new InfluxOssApiService.ScraperTargetRequest(); // ScraperTargetRequest | Scraper target to create
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}" // String | OpenTracing span context
};
apiInstance.postScrapers(scraperTargetRequest, opts, (error, data, response) => {
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
 **scraperTargetRequest** | [**ScraperTargetRequest**](ScraperTargetRequest.md)| Scraper target to create | 
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 

### Return type

[**ScraperTargetResponse**](ScraperTargetResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postScrapersIDLabels

> LabelResponse postScrapersIDLabels(scraperTargetID, labelMapping, opts)

Add a label to a scraper target

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.ScraperTargetsApi();
let scraperTargetID = "scraperTargetID_example"; // String | The scraper target ID.
let labelMapping = new InfluxOssApiService.LabelMapping(); // LabelMapping | Label to add
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}" // String | OpenTracing span context
};
apiInstance.postScrapersIDLabels(scraperTargetID, labelMapping, opts, (error, data, response) => {
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
 **scraperTargetID** | **String**| The scraper target ID. | 
 **labelMapping** | [**LabelMapping**](LabelMapping.md)| Label to add | 
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 

### Return type

[**LabelResponse**](LabelResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postScrapersIDMembers

> ResourceMember postScrapersIDMembers(scraperTargetID, addResourceMemberRequestBody, opts)

Add a member to a scraper target

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.ScraperTargetsApi();
let scraperTargetID = "scraperTargetID_example"; // String | The scraper target ID.
let addResourceMemberRequestBody = new InfluxOssApiService.AddResourceMemberRequestBody(); // AddResourceMemberRequestBody | User to add as member
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}" // String | OpenTracing span context
};
apiInstance.postScrapersIDMembers(scraperTargetID, addResourceMemberRequestBody, opts, (error, data, response) => {
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
 **scraperTargetID** | **String**| The scraper target ID. | 
 **addResourceMemberRequestBody** | [**AddResourceMemberRequestBody**](AddResourceMemberRequestBody.md)| User to add as member | 
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 

### Return type

[**ResourceMember**](ResourceMember.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postScrapersIDOwners

> ResourceOwner postScrapersIDOwners(scraperTargetID, addResourceMemberRequestBody, opts)

Add an owner to a scraper target

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.ScraperTargetsApi();
let scraperTargetID = "scraperTargetID_example"; // String | The scraper target ID.
let addResourceMemberRequestBody = new InfluxOssApiService.AddResourceMemberRequestBody(); // AddResourceMemberRequestBody | User to add as owner
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}" // String | OpenTracing span context
};
apiInstance.postScrapersIDOwners(scraperTargetID, addResourceMemberRequestBody, opts, (error, data, response) => {
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
 **scraperTargetID** | **String**| The scraper target ID. | 
 **addResourceMemberRequestBody** | [**AddResourceMemberRequestBody**](AddResourceMemberRequestBody.md)| User to add as owner | 
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 

### Return type

[**ResourceOwner**](ResourceOwner.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

