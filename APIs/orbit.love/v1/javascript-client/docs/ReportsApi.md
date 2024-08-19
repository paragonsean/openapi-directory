# OrbitApi.ReportsApi

All URIs are relative to *https://app.orbit.love/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**workspaceSlugReportsGet**](ReportsApi.md#workspaceSlugReportsGet) | **GET** /{workspace_slug}/reports | Get a workspace stats



## workspaceSlugReportsGet

> workspaceSlugReportsGet(workspaceSlug, opts)

Get a workspace stats

### Example

```javascript
import OrbitApi from 'orbit_api';
let defaultClient = OrbitApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearer
let bearer = defaultClient.authentications['bearer'];
bearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new OrbitApi.ReportsApi();
let workspaceSlug = "workspaceSlug_example"; // String | 
let opts = {
  'startDate': "startDate_example", // String | Filter activities after this date. Format: YYYY-MM-DD.
  'endDate': "endDate_example", // String | Filter activities before this date. Format: YYYY-MM-DD.
  'relative': "relative_example", // String | Relative timeframes. Format: this_<integer>_<period>, with period in [days, weeks, months, years]. For example, this_30_days.
  'properties': "properties_example", // String | 
  'activityType': "activityType_example", // String | 
  'type': "type_example" // String | Deprecated in favor of the activity_type parameter.
};
apiInstance.workspaceSlugReportsGet(workspaceSlug, opts, (error, data, response) => {
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
 **workspaceSlug** | **String**|  | 
 **startDate** | **String**| Filter activities after this date. Format: YYYY-MM-DD. | [optional] 
 **endDate** | **String**| Filter activities before this date. Format: YYYY-MM-DD. | [optional] 
 **relative** | **String**| Relative timeframes. Format: this_&lt;integer&gt;_&lt;period&gt;, with period in [days, weeks, months, years]. For example, this_30_days. | [optional] 
 **properties** | **String**|  | [optional] 
 **activityType** | **String**|  | [optional] 
 **type** | **String**| Deprecated in favor of the activity_type parameter. | [optional] 

### Return type

null (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

