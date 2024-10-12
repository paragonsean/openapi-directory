# AutomationsApi

All URIs are relative to *http://app.files.com/api/rest/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deleteAutomationsId**](AutomationsApi.md#deleteAutomationsId) | **DELETE** /automations/{id} | Delete Automation |
| [**getAutomations**](AutomationsApi.md#getAutomations) | **GET** /automations | List Automations |
| [**getAutomationsId**](AutomationsApi.md#getAutomationsId) | **GET** /automations/{id} | Show Automation |
| [**patchAutomationsId**](AutomationsApi.md#patchAutomationsId) | **PATCH** /automations/{id} | Update Automation |
| [**postAutomations**](AutomationsApi.md#postAutomations) | **POST** /automations | Create Automation |


<a id="deleteAutomationsId"></a>
# **deleteAutomationsId**
> deleteAutomationsId(id)

Delete Automation

Delete Automation

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AutomationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://app.files.com/api/rest/v1");

    AutomationsApi apiInstance = new AutomationsApi(defaultClient);
    Integer id = 56; // Integer | Automation ID.
    try {
      apiInstance.deleteAutomationsId(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling AutomationsApi#deleteAutomationsId");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| Automation ID. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No body. |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **405** | Method Not Allowed |  -  |
| **409** | Conflict |  -  |
| **412** | Precondition Failed |  -  |
| **422** | Unprocessable Entity |  -  |
| **423** | Locked |  -  |
| **429** | Too Many Requests |  -  |

<a id="getAutomations"></a>
# **getAutomations**
> List&lt;AutomationEntity&gt; getAutomations(cursor, perPage, sortBy, automation, filter, filterGt, filterGteq, filterLt, filterLteq, withDeleted)

List Automations

List Automations

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AutomationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://app.files.com/api/rest/v1");

    AutomationsApi apiInstance = new AutomationsApi(defaultClient);
    String cursor = "cursor_example"; // String | Used for pagination.  When a list request has more records available, cursors are provided in the response headers `X-Files-Cursor-Next` and `X-Files-Cursor-Prev`.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination.
    Integer perPage = 56; // Integer | Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended).
    Object sortBy = null; // Object | If set, sort records by the specified field in either `asc` or `desc` direction (e.g. `sort_by[automation]=desc`). Valid fields are `automation`, `disabled`, `last_modified_at` or `name`.
    String automation = "automation_example"; // String | If set, return records where the specified field is equal to the supplied value.
    Object filter = null; // Object | If set, return records where the specified field is equal to the supplied value. Valid fields are `disabled`, `last_modified_at` or `automation`. Valid field combinations are `[ automation, disabled ]` and `[ disabled, automation ]`.
    Object filterGt = null; // Object | If set, return records where the specified field is greater than the supplied value. Valid fields are `last_modified_at`.
    Object filterGteq = null; // Object | If set, return records where the specified field is greater than or equal the supplied value. Valid fields are `last_modified_at`.
    Object filterLt = null; // Object | If set, return records where the specified field is less than the supplied value. Valid fields are `last_modified_at`.
    Object filterLteq = null; // Object | If set, return records where the specified field is less than or equal the supplied value. Valid fields are `last_modified_at`.
    Boolean withDeleted = true; // Boolean | Set to true to include deleted automations in the results.
    try {
      List<AutomationEntity> result = apiInstance.getAutomations(cursor, perPage, sortBy, automation, filter, filterGt, filterGteq, filterLt, filterLteq, withDeleted);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AutomationsApi#getAutomations");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **cursor** | **String**| Used for pagination.  When a list request has more records available, cursors are provided in the response headers &#x60;X-Files-Cursor-Next&#x60; and &#x60;X-Files-Cursor-Prev&#x60;.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination. | [optional] |
| **perPage** | **Integer**| Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended). | [optional] |
| **sortBy** | [**Object**](.md)| If set, sort records by the specified field in either &#x60;asc&#x60; or &#x60;desc&#x60; direction (e.g. &#x60;sort_by[automation]&#x3D;desc&#x60;). Valid fields are &#x60;automation&#x60;, &#x60;disabled&#x60;, &#x60;last_modified_at&#x60; or &#x60;name&#x60;. | [optional] |
| **automation** | **String**| If set, return records where the specified field is equal to the supplied value. | [optional] |
| **filter** | [**Object**](.md)| If set, return records where the specified field is equal to the supplied value. Valid fields are &#x60;disabled&#x60;, &#x60;last_modified_at&#x60; or &#x60;automation&#x60;. Valid field combinations are &#x60;[ automation, disabled ]&#x60; and &#x60;[ disabled, automation ]&#x60;. | [optional] |
| **filterGt** | [**Object**](.md)| If set, return records where the specified field is greater than the supplied value. Valid fields are &#x60;last_modified_at&#x60;. | [optional] |
| **filterGteq** | [**Object**](.md)| If set, return records where the specified field is greater than or equal the supplied value. Valid fields are &#x60;last_modified_at&#x60;. | [optional] |
| **filterLt** | [**Object**](.md)| If set, return records where the specified field is less than the supplied value. Valid fields are &#x60;last_modified_at&#x60;. | [optional] |
| **filterLteq** | [**Object**](.md)| If set, return records where the specified field is less than or equal the supplied value. Valid fields are &#x60;last_modified_at&#x60;. | [optional] |
| **withDeleted** | **Boolean**| Set to true to include deleted automations in the results. | [optional] |

### Return type

[**List&lt;AutomationEntity&gt;**](AutomationEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of Automations objects. |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **405** | Method Not Allowed |  -  |
| **409** | Conflict |  -  |
| **412** | Precondition Failed |  -  |
| **422** | Unprocessable Entity |  -  |
| **423** | Locked |  -  |
| **429** | Too Many Requests |  -  |

<a id="getAutomationsId"></a>
# **getAutomationsId**
> AutomationEntity getAutomationsId(id)

Show Automation

Show Automation

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AutomationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://app.files.com/api/rest/v1");

    AutomationsApi apiInstance = new AutomationsApi(defaultClient);
    Integer id = 56; // Integer | Automation ID.
    try {
      AutomationEntity result = apiInstance.getAutomationsId(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AutomationsApi#getAutomationsId");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| Automation ID. | |

### Return type

[**AutomationEntity**](AutomationEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The Automations object. |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **405** | Method Not Allowed |  -  |
| **409** | Conflict |  -  |
| **412** | Precondition Failed |  -  |
| **422** | Unprocessable Entity |  -  |
| **423** | Locked |  -  |
| **429** | Too Many Requests |  -  |

<a id="patchAutomationsId"></a>
# **patchAutomationsId**
> AutomationEntity patchAutomationsId(id, automation, description, destination, destinationReplaceFrom, destinationReplaceTo, destinations, disabled, groupIds, interval, name, path, recurringDay, schedule, source, syncIds, trigger, triggerActions, userIds, value)

Update Automation

Update Automation

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AutomationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://app.files.com/api/rest/v1");

    AutomationsApi apiInstance = new AutomationsApi(defaultClient);
    Integer id = 56; // Integer | Automation ID.
    String automation = "create_folder"; // String | Automation type
    String description = "description_example"; // String | Description for the this Automation.
    String destination = "destination_example"; // String | DEPRECATED: Destination Path. Use `destinations` instead.
    String destinationReplaceFrom = "destinationReplaceFrom_example"; // String | If set, this string in the destination path will be replaced with the value in `destination_replace_to`.
    String destinationReplaceTo = "destinationReplaceTo_example"; // String | If set, this string will replace the value `destination_replace_from` in the destination filename. You can use special patterns here.
    List<String> destinations = Arrays.asList(); // List<String> | A list of String destination paths or Hash of folder_path and optional file_path.
    Boolean disabled = true; // Boolean | If true, this automation will not run.
    String groupIds = "groupIds_example"; // String | A list of group IDs the automation is associated with. If sent as a string, it should be comma-delimited.
    String interval = "interval_example"; // String | How often to run this automation? One of: `day`, `week`, `week_end`, `month`, `month_end`, `quarter`, `quarter_end`, `year`, `year_end`
    String name = "name_example"; // String | Name for this automation.
    String path = "path_example"; // String | Path on which this Automation runs.  Supports globs.
    Integer recurringDay = 56; // Integer | If trigger type is `daily`, this specifies a day number to run in one of the supported intervals: `week`, `month`, `quarter`, `year`.
    Object schedule = null; // Object | Custom schedule for running this automation.
    String source = "source_example"; // String | Source Path
    String syncIds = "syncIds_example"; // String | A list of sync IDs the automation is associated with. If sent as a string, it should be comma-delimited.
    String trigger = "realtime"; // String | How this automation is triggered to run. One of: `realtime`, `daily`, `custom_schedule`, `webhook`, `email`, or `action`.
    List<String> triggerActions = Arrays.asList(); // List<String> | If trigger is `action`, this is the list of action types on which to trigger the automation. Valid actions are create, read, update, destroy, move, copy
    String userIds = "userIds_example"; // String | A list of user IDs the automation is associated with. If sent as a string, it should be comma-delimited.
    Object value = null; // Object | A Hash of attributes specific to the automation type.
    try {
      AutomationEntity result = apiInstance.patchAutomationsId(id, automation, description, destination, destinationReplaceFrom, destinationReplaceTo, destinations, disabled, groupIds, interval, name, path, recurringDay, schedule, source, syncIds, trigger, triggerActions, userIds, value);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AutomationsApi#patchAutomationsId");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **Integer**| Automation ID. | |
| **automation** | **String**| Automation type | [optional] [enum: create_folder, request_file, request_move, copy_newest_file, delete_file, copy_file, move_file, as2_send, run_sync] |
| **description** | **String**| Description for the this Automation. | [optional] |
| **destination** | **String**| DEPRECATED: Destination Path. Use &#x60;destinations&#x60; instead. | [optional] |
| **destinationReplaceFrom** | **String**| If set, this string in the destination path will be replaced with the value in &#x60;destination_replace_to&#x60;. | [optional] |
| **destinationReplaceTo** | **String**| If set, this string will replace the value &#x60;destination_replace_from&#x60; in the destination filename. You can use special patterns here. | [optional] |
| **destinations** | [**List&lt;String&gt;**](String.md)| A list of String destination paths or Hash of folder_path and optional file_path. | [optional] |
| **disabled** | **Boolean**| If true, this automation will not run. | [optional] |
| **groupIds** | **String**| A list of group IDs the automation is associated with. If sent as a string, it should be comma-delimited. | [optional] |
| **interval** | **String**| How often to run this automation? One of: &#x60;day&#x60;, &#x60;week&#x60;, &#x60;week_end&#x60;, &#x60;month&#x60;, &#x60;month_end&#x60;, &#x60;quarter&#x60;, &#x60;quarter_end&#x60;, &#x60;year&#x60;, &#x60;year_end&#x60; | [optional] |
| **name** | **String**| Name for this automation. | [optional] |
| **path** | **String**| Path on which this Automation runs.  Supports globs. | [optional] |
| **recurringDay** | **Integer**| If trigger type is &#x60;daily&#x60;, this specifies a day number to run in one of the supported intervals: &#x60;week&#x60;, &#x60;month&#x60;, &#x60;quarter&#x60;, &#x60;year&#x60;. | [optional] |
| **schedule** | [**Object**](Object.md)| Custom schedule for running this automation. | [optional] |
| **source** | **String**| Source Path | [optional] |
| **syncIds** | **String**| A list of sync IDs the automation is associated with. If sent as a string, it should be comma-delimited. | [optional] |
| **trigger** | **String**| How this automation is triggered to run. One of: &#x60;realtime&#x60;, &#x60;daily&#x60;, &#x60;custom_schedule&#x60;, &#x60;webhook&#x60;, &#x60;email&#x60;, or &#x60;action&#x60;. | [optional] [enum: realtime, daily, custom_schedule, webhook, email, action] |
| **triggerActions** | [**List&lt;String&gt;**](String.md)| If trigger is &#x60;action&#x60;, this is the list of action types on which to trigger the automation. Valid actions are create, read, update, destroy, move, copy | [optional] |
| **userIds** | **String**| A list of user IDs the automation is associated with. If sent as a string, it should be comma-delimited. | [optional] |
| **value** | [**Object**](Object.md)| A Hash of attributes specific to the automation type. | [optional] |

### Return type

[**AutomationEntity**](AutomationEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The Automations object. |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **405** | Method Not Allowed |  -  |
| **409** | Conflict |  -  |
| **412** | Precondition Failed |  -  |
| **422** | Unprocessable Entity |  -  |
| **423** | Locked |  -  |
| **429** | Too Many Requests |  -  |

<a id="postAutomations"></a>
# **postAutomations**
> AutomationEntity postAutomations(automation, description, destination, destinationReplaceFrom, destinationReplaceTo, destinations, disabled, groupIds, interval, name, path, recurringDay, schedule, source, syncIds, trigger, triggerActions, userIds, value)

Create Automation

Create Automation

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AutomationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://app.files.com/api/rest/v1");

    AutomationsApi apiInstance = new AutomationsApi(defaultClient);
    String automation = "create_folder"; // String | Automation type
    String description = "description_example"; // String | Description for the this Automation.
    String destination = "destination_example"; // String | DEPRECATED: Destination Path. Use `destinations` instead.
    String destinationReplaceFrom = "destinationReplaceFrom_example"; // String | If set, this string in the destination path will be replaced with the value in `destination_replace_to`.
    String destinationReplaceTo = "destinationReplaceTo_example"; // String | If set, this string will replace the value `destination_replace_from` in the destination filename. You can use special patterns here.
    List<String> destinations = Arrays.asList(); // List<String> | A list of String destination paths or Hash of folder_path and optional file_path.
    Boolean disabled = true; // Boolean | If true, this automation will not run.
    String groupIds = "groupIds_example"; // String | A list of group IDs the automation is associated with. If sent as a string, it should be comma-delimited.
    String interval = "interval_example"; // String | How often to run this automation? One of: `day`, `week`, `week_end`, `month`, `month_end`, `quarter`, `quarter_end`, `year`, `year_end`
    String name = "name_example"; // String | Name for this automation.
    String path = "path_example"; // String | Path on which this Automation runs.  Supports globs.
    Integer recurringDay = 56; // Integer | If trigger type is `daily`, this specifies a day number to run in one of the supported intervals: `week`, `month`, `quarter`, `year`.
    Object schedule = null; // Object | Custom schedule for running this automation.
    String source = "source_example"; // String | Source Path
    String syncIds = "syncIds_example"; // String | A list of sync IDs the automation is associated with. If sent as a string, it should be comma-delimited.
    String trigger = "realtime"; // String | How this automation is triggered to run. One of: `realtime`, `daily`, `custom_schedule`, `webhook`, `email`, or `action`.
    List<String> triggerActions = Arrays.asList(); // List<String> | If trigger is `action`, this is the list of action types on which to trigger the automation. Valid actions are create, read, update, destroy, move, copy
    String userIds = "userIds_example"; // String | A list of user IDs the automation is associated with. If sent as a string, it should be comma-delimited.
    Object value = null; // Object | A Hash of attributes specific to the automation type.
    try {
      AutomationEntity result = apiInstance.postAutomations(automation, description, destination, destinationReplaceFrom, destinationReplaceTo, destinations, disabled, groupIds, interval, name, path, recurringDay, schedule, source, syncIds, trigger, triggerActions, userIds, value);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AutomationsApi#postAutomations");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **automation** | **String**| Automation type | [enum: create_folder, request_file, request_move, copy_newest_file, delete_file, copy_file, move_file, as2_send, run_sync] |
| **description** | **String**| Description for the this Automation. | [optional] |
| **destination** | **String**| DEPRECATED: Destination Path. Use &#x60;destinations&#x60; instead. | [optional] |
| **destinationReplaceFrom** | **String**| If set, this string in the destination path will be replaced with the value in &#x60;destination_replace_to&#x60;. | [optional] |
| **destinationReplaceTo** | **String**| If set, this string will replace the value &#x60;destination_replace_from&#x60; in the destination filename. You can use special patterns here. | [optional] |
| **destinations** | [**List&lt;String&gt;**](String.md)| A list of String destination paths or Hash of folder_path and optional file_path. | [optional] |
| **disabled** | **Boolean**| If true, this automation will not run. | [optional] |
| **groupIds** | **String**| A list of group IDs the automation is associated with. If sent as a string, it should be comma-delimited. | [optional] |
| **interval** | **String**| How often to run this automation? One of: &#x60;day&#x60;, &#x60;week&#x60;, &#x60;week_end&#x60;, &#x60;month&#x60;, &#x60;month_end&#x60;, &#x60;quarter&#x60;, &#x60;quarter_end&#x60;, &#x60;year&#x60;, &#x60;year_end&#x60; | [optional] |
| **name** | **String**| Name for this automation. | [optional] |
| **path** | **String**| Path on which this Automation runs.  Supports globs. | [optional] |
| **recurringDay** | **Integer**| If trigger type is &#x60;daily&#x60;, this specifies a day number to run in one of the supported intervals: &#x60;week&#x60;, &#x60;month&#x60;, &#x60;quarter&#x60;, &#x60;year&#x60;. | [optional] |
| **schedule** | [**Object**](Object.md)| Custom schedule for running this automation. | [optional] |
| **source** | **String**| Source Path | [optional] |
| **syncIds** | **String**| A list of sync IDs the automation is associated with. If sent as a string, it should be comma-delimited. | [optional] |
| **trigger** | **String**| How this automation is triggered to run. One of: &#x60;realtime&#x60;, &#x60;daily&#x60;, &#x60;custom_schedule&#x60;, &#x60;webhook&#x60;, &#x60;email&#x60;, or &#x60;action&#x60;. | [optional] [enum: realtime, daily, custom_schedule, webhook, email, action] |
| **triggerActions** | [**List&lt;String&gt;**](String.md)| If trigger is &#x60;action&#x60;, this is the list of action types on which to trigger the automation. Valid actions are create, read, update, destroy, move, copy | [optional] |
| **userIds** | **String**| A list of user IDs the automation is associated with. If sent as a string, it should be comma-delimited. | [optional] |
| **value** | [**Object**](Object.md)| A Hash of attributes specific to the automation type. | [optional] |

### Return type

[**AutomationEntity**](AutomationEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The Automations object. |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **405** | Method Not Allowed |  -  |
| **409** | Conflict |  -  |
| **412** | Precondition Failed |  -  |
| **422** | Unprocessable Entity |  -  |
| **423** | Locked |  -  |
| **429** | Too Many Requests |  -  |

