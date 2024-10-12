# FilesComApi.AutomationsApi

All URIs are relative to *http://app.files.com/api/rest/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteAutomationsId**](AutomationsApi.md#deleteAutomationsId) | **DELETE** /automations/{id} | Delete Automation
[**getAutomations**](AutomationsApi.md#getAutomations) | **GET** /automations | List Automations
[**getAutomationsId**](AutomationsApi.md#getAutomationsId) | **GET** /automations/{id} | Show Automation
[**patchAutomationsId**](AutomationsApi.md#patchAutomationsId) | **PATCH** /automations/{id} | Update Automation
[**postAutomations**](AutomationsApi.md#postAutomations) | **POST** /automations | Create Automation



## deleteAutomationsId

> deleteAutomationsId(id)

Delete Automation

Delete Automation

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.AutomationsApi();
let id = 56; // Number | Automation ID.
apiInstance.deleteAutomationsId(id, (error, data, response) => {
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
 **id** | **Number**| Automation ID. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getAutomations

> [AutomationEntity] getAutomations(opts)

List Automations

List Automations

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.AutomationsApi();
let opts = {
  'cursor': "cursor_example", // String | Used for pagination.  When a list request has more records available, cursors are provided in the response headers `X-Files-Cursor-Next` and `X-Files-Cursor-Prev`.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination.
  'perPage': 56, // Number | Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended).
  'sortBy': {key: null}, // Object | If set, sort records by the specified field in either `asc` or `desc` direction (e.g. `sort_by[automation]=desc`). Valid fields are `automation`, `disabled`, `last_modified_at` or `name`.
  'automation': "automation_example", // String | If set, return records where the specified field is equal to the supplied value.
  'filter': {key: null}, // Object | If set, return records where the specified field is equal to the supplied value. Valid fields are `disabled`, `last_modified_at` or `automation`. Valid field combinations are `[ automation, disabled ]` and `[ disabled, automation ]`.
  'filterGt': {key: null}, // Object | If set, return records where the specified field is greater than the supplied value. Valid fields are `last_modified_at`.
  'filterGteq': {key: null}, // Object | If set, return records where the specified field is greater than or equal the supplied value. Valid fields are `last_modified_at`.
  'filterLt': {key: null}, // Object | If set, return records where the specified field is less than the supplied value. Valid fields are `last_modified_at`.
  'filterLteq': {key: null}, // Object | If set, return records where the specified field is less than or equal the supplied value. Valid fields are `last_modified_at`.
  'withDeleted': true // Boolean | Set to true to include deleted automations in the results.
};
apiInstance.getAutomations(opts, (error, data, response) => {
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
 **cursor** | **String**| Used for pagination.  When a list request has more records available, cursors are provided in the response headers &#x60;X-Files-Cursor-Next&#x60; and &#x60;X-Files-Cursor-Prev&#x60;.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination. | [optional] 
 **perPage** | **Number**| Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended). | [optional] 
 **sortBy** | [**Object**](.md)| If set, sort records by the specified field in either &#x60;asc&#x60; or &#x60;desc&#x60; direction (e.g. &#x60;sort_by[automation]&#x3D;desc&#x60;). Valid fields are &#x60;automation&#x60;, &#x60;disabled&#x60;, &#x60;last_modified_at&#x60; or &#x60;name&#x60;. | [optional] 
 **automation** | **String**| If set, return records where the specified field is equal to the supplied value. | [optional] 
 **filter** | [**Object**](.md)| If set, return records where the specified field is equal to the supplied value. Valid fields are &#x60;disabled&#x60;, &#x60;last_modified_at&#x60; or &#x60;automation&#x60;. Valid field combinations are &#x60;[ automation, disabled ]&#x60; and &#x60;[ disabled, automation ]&#x60;. | [optional] 
 **filterGt** | [**Object**](.md)| If set, return records where the specified field is greater than the supplied value. Valid fields are &#x60;last_modified_at&#x60;. | [optional] 
 **filterGteq** | [**Object**](.md)| If set, return records where the specified field is greater than or equal the supplied value. Valid fields are &#x60;last_modified_at&#x60;. | [optional] 
 **filterLt** | [**Object**](.md)| If set, return records where the specified field is less than the supplied value. Valid fields are &#x60;last_modified_at&#x60;. | [optional] 
 **filterLteq** | [**Object**](.md)| If set, return records where the specified field is less than or equal the supplied value. Valid fields are &#x60;last_modified_at&#x60;. | [optional] 
 **withDeleted** | **Boolean**| Set to true to include deleted automations in the results. | [optional] 

### Return type

[**[AutomationEntity]**](AutomationEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getAutomationsId

> AutomationEntity getAutomationsId(id)

Show Automation

Show Automation

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.AutomationsApi();
let id = 56; // Number | Automation ID.
apiInstance.getAutomationsId(id, (error, data, response) => {
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
 **id** | **Number**| Automation ID. | 

### Return type

[**AutomationEntity**](AutomationEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## patchAutomationsId

> AutomationEntity patchAutomationsId(id, opts)

Update Automation

Update Automation

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.AutomationsApi();
let id = 56; // Number | Automation ID.
let opts = {
  'automation': "automation_example", // String | Automation type
  'description': "description_example", // String | Description for the this Automation.
  'destination': "destination_example", // String | DEPRECATED: Destination Path. Use `destinations` instead.
  'destinationReplaceFrom': "destinationReplaceFrom_example", // String | If set, this string in the destination path will be replaced with the value in `destination_replace_to`.
  'destinationReplaceTo': "destinationReplaceTo_example", // String | If set, this string will replace the value `destination_replace_from` in the destination filename. You can use special patterns here.
  'destinations': ["null"], // [String] | A list of String destination paths or Hash of folder_path and optional file_path.
  'disabled': true, // Boolean | If true, this automation will not run.
  'groupIds': "groupIds_example", // String | A list of group IDs the automation is associated with. If sent as a string, it should be comma-delimited.
  'interval': "interval_example", // String | How often to run this automation? One of: `day`, `week`, `week_end`, `month`, `month_end`, `quarter`, `quarter_end`, `year`, `year_end`
  'name': "name_example", // String | Name for this automation.
  'path': "path_example", // String | Path on which this Automation runs.  Supports globs.
  'recurringDay': 56, // Number | If trigger type is `daily`, this specifies a day number to run in one of the supported intervals: `week`, `month`, `quarter`, `year`.
  'schedule': {key: null}, // Object | Custom schedule for running this automation.
  'source': "source_example", // String | Source Path
  'syncIds': "syncIds_example", // String | A list of sync IDs the automation is associated with. If sent as a string, it should be comma-delimited.
  'trigger': "trigger_example", // String | How this automation is triggered to run. One of: `realtime`, `daily`, `custom_schedule`, `webhook`, `email`, or `action`.
  'triggerActions': ["null"], // [String] | If trigger is `action`, this is the list of action types on which to trigger the automation. Valid actions are create, read, update, destroy, move, copy
  'userIds': "userIds_example", // String | A list of user IDs the automation is associated with. If sent as a string, it should be comma-delimited.
  'value': {key: null} // Object | A Hash of attributes specific to the automation type.
};
apiInstance.patchAutomationsId(id, opts, (error, data, response) => {
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
 **id** | **Number**| Automation ID. | 
 **automation** | **String**| Automation type | [optional] 
 **description** | **String**| Description for the this Automation. | [optional] 
 **destination** | **String**| DEPRECATED: Destination Path. Use &#x60;destinations&#x60; instead. | [optional] 
 **destinationReplaceFrom** | **String**| If set, this string in the destination path will be replaced with the value in &#x60;destination_replace_to&#x60;. | [optional] 
 **destinationReplaceTo** | **String**| If set, this string will replace the value &#x60;destination_replace_from&#x60; in the destination filename. You can use special patterns here. | [optional] 
 **destinations** | [**[String]**](String.md)| A list of String destination paths or Hash of folder_path and optional file_path. | [optional] 
 **disabled** | **Boolean**| If true, this automation will not run. | [optional] 
 **groupIds** | **String**| A list of group IDs the automation is associated with. If sent as a string, it should be comma-delimited. | [optional] 
 **interval** | **String**| How often to run this automation? One of: &#x60;day&#x60;, &#x60;week&#x60;, &#x60;week_end&#x60;, &#x60;month&#x60;, &#x60;month_end&#x60;, &#x60;quarter&#x60;, &#x60;quarter_end&#x60;, &#x60;year&#x60;, &#x60;year_end&#x60; | [optional] 
 **name** | **String**| Name for this automation. | [optional] 
 **path** | **String**| Path on which this Automation runs.  Supports globs. | [optional] 
 **recurringDay** | **Number**| If trigger type is &#x60;daily&#x60;, this specifies a day number to run in one of the supported intervals: &#x60;week&#x60;, &#x60;month&#x60;, &#x60;quarter&#x60;, &#x60;year&#x60;. | [optional] 
 **schedule** | [**Object**](Object.md)| Custom schedule for running this automation. | [optional] 
 **source** | **String**| Source Path | [optional] 
 **syncIds** | **String**| A list of sync IDs the automation is associated with. If sent as a string, it should be comma-delimited. | [optional] 
 **trigger** | **String**| How this automation is triggered to run. One of: &#x60;realtime&#x60;, &#x60;daily&#x60;, &#x60;custom_schedule&#x60;, &#x60;webhook&#x60;, &#x60;email&#x60;, or &#x60;action&#x60;. | [optional] 
 **triggerActions** | [**[String]**](String.md)| If trigger is &#x60;action&#x60;, this is the list of action types on which to trigger the automation. Valid actions are create, read, update, destroy, move, copy | [optional] 
 **userIds** | **String**| A list of user IDs the automation is associated with. If sent as a string, it should be comma-delimited. | [optional] 
 **value** | [**Object**](Object.md)| A Hash of attributes specific to the automation type. | [optional] 

### Return type

[**AutomationEntity**](AutomationEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json


## postAutomations

> AutomationEntity postAutomations(automation, opts)

Create Automation

Create Automation

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.AutomationsApi();
let automation = "automation_example"; // String | Automation type
let opts = {
  'description': "description_example", // String | Description for the this Automation.
  'destination': "destination_example", // String | DEPRECATED: Destination Path. Use `destinations` instead.
  'destinationReplaceFrom': "destinationReplaceFrom_example", // String | If set, this string in the destination path will be replaced with the value in `destination_replace_to`.
  'destinationReplaceTo': "destinationReplaceTo_example", // String | If set, this string will replace the value `destination_replace_from` in the destination filename. You can use special patterns here.
  'destinations': ["null"], // [String] | A list of String destination paths or Hash of folder_path and optional file_path.
  'disabled': true, // Boolean | If true, this automation will not run.
  'groupIds': "groupIds_example", // String | A list of group IDs the automation is associated with. If sent as a string, it should be comma-delimited.
  'interval': "interval_example", // String | How often to run this automation? One of: `day`, `week`, `week_end`, `month`, `month_end`, `quarter`, `quarter_end`, `year`, `year_end`
  'name': "name_example", // String | Name for this automation.
  'path': "path_example", // String | Path on which this Automation runs.  Supports globs.
  'recurringDay': 56, // Number | If trigger type is `daily`, this specifies a day number to run in one of the supported intervals: `week`, `month`, `quarter`, `year`.
  'schedule': {key: null}, // Object | Custom schedule for running this automation.
  'source': "source_example", // String | Source Path
  'syncIds': "syncIds_example", // String | A list of sync IDs the automation is associated with. If sent as a string, it should be comma-delimited.
  'trigger': "trigger_example", // String | How this automation is triggered to run. One of: `realtime`, `daily`, `custom_schedule`, `webhook`, `email`, or `action`.
  'triggerActions': ["null"], // [String] | If trigger is `action`, this is the list of action types on which to trigger the automation. Valid actions are create, read, update, destroy, move, copy
  'userIds': "userIds_example", // String | A list of user IDs the automation is associated with. If sent as a string, it should be comma-delimited.
  'value': {key: null} // Object | A Hash of attributes specific to the automation type.
};
apiInstance.postAutomations(automation, opts, (error, data, response) => {
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
 **automation** | **String**| Automation type | 
 **description** | **String**| Description for the this Automation. | [optional] 
 **destination** | **String**| DEPRECATED: Destination Path. Use &#x60;destinations&#x60; instead. | [optional] 
 **destinationReplaceFrom** | **String**| If set, this string in the destination path will be replaced with the value in &#x60;destination_replace_to&#x60;. | [optional] 
 **destinationReplaceTo** | **String**| If set, this string will replace the value &#x60;destination_replace_from&#x60; in the destination filename. You can use special patterns here. | [optional] 
 **destinations** | [**[String]**](String.md)| A list of String destination paths or Hash of folder_path and optional file_path. | [optional] 
 **disabled** | **Boolean**| If true, this automation will not run. | [optional] 
 **groupIds** | **String**| A list of group IDs the automation is associated with. If sent as a string, it should be comma-delimited. | [optional] 
 **interval** | **String**| How often to run this automation? One of: &#x60;day&#x60;, &#x60;week&#x60;, &#x60;week_end&#x60;, &#x60;month&#x60;, &#x60;month_end&#x60;, &#x60;quarter&#x60;, &#x60;quarter_end&#x60;, &#x60;year&#x60;, &#x60;year_end&#x60; | [optional] 
 **name** | **String**| Name for this automation. | [optional] 
 **path** | **String**| Path on which this Automation runs.  Supports globs. | [optional] 
 **recurringDay** | **Number**| If trigger type is &#x60;daily&#x60;, this specifies a day number to run in one of the supported intervals: &#x60;week&#x60;, &#x60;month&#x60;, &#x60;quarter&#x60;, &#x60;year&#x60;. | [optional] 
 **schedule** | [**Object**](Object.md)| Custom schedule for running this automation. | [optional] 
 **source** | **String**| Source Path | [optional] 
 **syncIds** | **String**| A list of sync IDs the automation is associated with. If sent as a string, it should be comma-delimited. | [optional] 
 **trigger** | **String**| How this automation is triggered to run. One of: &#x60;realtime&#x60;, &#x60;daily&#x60;, &#x60;custom_schedule&#x60;, &#x60;webhook&#x60;, &#x60;email&#x60;, or &#x60;action&#x60;. | [optional] 
 **triggerActions** | [**[String]**](String.md)| If trigger is &#x60;action&#x60;, this is the list of action types on which to trigger the automation. Valid actions are create, read, update, destroy, move, copy | [optional] 
 **userIds** | **String**| A list of user IDs the automation is associated with. If sent as a string, it should be comma-delimited. | [optional] 
 **value** | [**Object**](Object.md)| A Hash of attributes specific to the automation type. | [optional] 

### Return type

[**AutomationEntity**](AutomationEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json

