# HistoryExportsApi

All URIs are relative to *http://app.files.com/api/rest/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getHistoryExportsId**](HistoryExportsApi.md#getHistoryExportsId) | **GET** /history_exports/{id} | Show History Export |
| [**postHistoryExports**](HistoryExportsApi.md#postHistoryExports) | **POST** /history_exports | Create History Export |


<a id="getHistoryExportsId"></a>
# **getHistoryExportsId**
> HistoryExportEntity getHistoryExportsId(id)

Show History Export

Show History Export

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HistoryExportsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://app.files.com/api/rest/v1");

    HistoryExportsApi apiInstance = new HistoryExportsApi(defaultClient);
    Integer id = 56; // Integer | History Export ID.
    try {
      HistoryExportEntity result = apiInstance.getHistoryExportsId(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HistoryExportsApi#getHistoryExportsId");
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
| **id** | **Integer**| History Export ID. | |

### Return type

[**HistoryExportEntity**](HistoryExportEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The HistoryExports object. |  -  |
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

<a id="postHistoryExports"></a>
# **postHistoryExports**
> HistoryExportEntity postHistoryExports(endAt, queryAction, queryDestination, queryFailureType, queryFileId, queryFolder, queryInterface, queryIp, queryParentId, queryPath, querySrc, queryTargetId, queryTargetName, queryTargetPermission, queryTargetPermissionSet, queryTargetPlatform, queryTargetUserId, queryTargetUsername, queryUserId, queryUsername, startAt, userId)

Create History Export

Create History Export

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HistoryExportsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://app.files.com/api/rest/v1");

    HistoryExportsApi apiInstance = new HistoryExportsApi(defaultClient);
    OffsetDateTime endAt = OffsetDateTime.now(); // OffsetDateTime | End date/time of export range.
    String queryAction = "queryAction_example"; // String | Filter results by this this action type. Valid values: `create`, `read`, `update`, `destroy`, `move`, `login`, `failedlogin`, `copy`, `user_create`, `user_update`, `user_destroy`, `group_create`, `group_update`, `group_destroy`, `permission_create`, `permission_destroy`, `api_key_create`, `api_key_update`, `api_key_destroy`
    String queryDestination = "queryDestination_example"; // String | Return results that are file moves with this path as destination.
    String queryFailureType = "queryFailureType_example"; // String | If searching for Histories about login failures, this parameter restricts results to failures of this specific type.  Valid values: `expired_trial`, `account_overdue`, `locked_out`, `ip_mismatch`, `password_mismatch`, `site_mismatch`, `username_not_found`, `none`, `no_ftp_permission`, `no_web_permission`, `no_directory`, `errno_enoent`, `no_sftp_permission`, `no_dav_permission`, `no_restapi_permission`, `key_mismatch`, `region_mismatch`, `expired_access`, `desktop_ip_mismatch`, `desktop_api_key_not_used_quickly_enough`, `disabled`, `country_mismatch`
    String queryFileId = "queryFileId_example"; // String | Return results that are file actions related to the file indicated by this File ID
    String queryFolder = "queryFolder_example"; // String | Return results that are file actions related to files or folders inside this folder path.
    String queryInterface = "queryInterface_example"; // String | Filter results by this this interface type. Valid values: `web`, `ftp`, `robot`, `jsapi`, `webdesktopapi`, `sftp`, `dav`, `desktop`, `restapi`, `scim`, `office`, `mobile`, `as2`, `inbound_email`, `remote`
    String queryIp = "queryIp_example"; // String | Filter results by this IP address.
    String queryParentId = "queryParentId_example"; // String | Return results that are file actions inside the parent folder specified by this folder ID
    String queryPath = "queryPath_example"; // String | Return results that are file actions related to this path.
    String querySrc = "querySrc_example"; // String | Return results that are file moves originating from this path.
    String queryTargetId = "queryTargetId_example"; // String | If searching for Histories about specific objects (such as Users, or API Keys), this paremeter restricts results to objects that match this ID.
    String queryTargetName = "queryTargetName_example"; // String | If searching for Histories about Users, Groups or other objects with names, this parameter restricts results to objects with this name/username.
    String queryTargetPermission = "queryTargetPermission_example"; // String | If searching for Histories about Permisisons, this parameter restricts results to permissions of this level.
    String queryTargetPermissionSet = "queryTargetPermissionSet_example"; // String | If searching for Histories about API keys, this parameter restricts results to API keys with this permission set.
    String queryTargetPlatform = "queryTargetPlatform_example"; // String | If searching for Histories about API keys, this parameter restricts results to API keys associated with this platform.
    String queryTargetUserId = "queryTargetUserId_example"; // String | If searching for Histories about API keys, this parameter restricts results to API keys created by/for this user ID.
    String queryTargetUsername = "queryTargetUsername_example"; // String | If searching for Histories about API keys, this parameter restricts results to API keys created by/for this username.
    String queryUserId = "queryUserId_example"; // String | Return results that are actions performed by the user indiciated by this User ID
    String queryUsername = "queryUsername_example"; // String | Filter results by this username.
    OffsetDateTime startAt = OffsetDateTime.now(); // OffsetDateTime | Start date/time of export range.
    Integer userId = 56; // Integer | User ID.  Provide a value of `0` to operate the current session's user.
    try {
      HistoryExportEntity result = apiInstance.postHistoryExports(endAt, queryAction, queryDestination, queryFailureType, queryFileId, queryFolder, queryInterface, queryIp, queryParentId, queryPath, querySrc, queryTargetId, queryTargetName, queryTargetPermission, queryTargetPermissionSet, queryTargetPlatform, queryTargetUserId, queryTargetUsername, queryUserId, queryUsername, startAt, userId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HistoryExportsApi#postHistoryExports");
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
| **endAt** | **OffsetDateTime**| End date/time of export range. | [optional] |
| **queryAction** | **String**| Filter results by this this action type. Valid values: &#x60;create&#x60;, &#x60;read&#x60;, &#x60;update&#x60;, &#x60;destroy&#x60;, &#x60;move&#x60;, &#x60;login&#x60;, &#x60;failedlogin&#x60;, &#x60;copy&#x60;, &#x60;user_create&#x60;, &#x60;user_update&#x60;, &#x60;user_destroy&#x60;, &#x60;group_create&#x60;, &#x60;group_update&#x60;, &#x60;group_destroy&#x60;, &#x60;permission_create&#x60;, &#x60;permission_destroy&#x60;, &#x60;api_key_create&#x60;, &#x60;api_key_update&#x60;, &#x60;api_key_destroy&#x60; | [optional] |
| **queryDestination** | **String**| Return results that are file moves with this path as destination. | [optional] |
| **queryFailureType** | **String**| If searching for Histories about login failures, this parameter restricts results to failures of this specific type.  Valid values: &#x60;expired_trial&#x60;, &#x60;account_overdue&#x60;, &#x60;locked_out&#x60;, &#x60;ip_mismatch&#x60;, &#x60;password_mismatch&#x60;, &#x60;site_mismatch&#x60;, &#x60;username_not_found&#x60;, &#x60;none&#x60;, &#x60;no_ftp_permission&#x60;, &#x60;no_web_permission&#x60;, &#x60;no_directory&#x60;, &#x60;errno_enoent&#x60;, &#x60;no_sftp_permission&#x60;, &#x60;no_dav_permission&#x60;, &#x60;no_restapi_permission&#x60;, &#x60;key_mismatch&#x60;, &#x60;region_mismatch&#x60;, &#x60;expired_access&#x60;, &#x60;desktop_ip_mismatch&#x60;, &#x60;desktop_api_key_not_used_quickly_enough&#x60;, &#x60;disabled&#x60;, &#x60;country_mismatch&#x60; | [optional] |
| **queryFileId** | **String**| Return results that are file actions related to the file indicated by this File ID | [optional] |
| **queryFolder** | **String**| Return results that are file actions related to files or folders inside this folder path. | [optional] |
| **queryInterface** | **String**| Filter results by this this interface type. Valid values: &#x60;web&#x60;, &#x60;ftp&#x60;, &#x60;robot&#x60;, &#x60;jsapi&#x60;, &#x60;webdesktopapi&#x60;, &#x60;sftp&#x60;, &#x60;dav&#x60;, &#x60;desktop&#x60;, &#x60;restapi&#x60;, &#x60;scim&#x60;, &#x60;office&#x60;, &#x60;mobile&#x60;, &#x60;as2&#x60;, &#x60;inbound_email&#x60;, &#x60;remote&#x60; | [optional] |
| **queryIp** | **String**| Filter results by this IP address. | [optional] |
| **queryParentId** | **String**| Return results that are file actions inside the parent folder specified by this folder ID | [optional] |
| **queryPath** | **String**| Return results that are file actions related to this path. | [optional] |
| **querySrc** | **String**| Return results that are file moves originating from this path. | [optional] |
| **queryTargetId** | **String**| If searching for Histories about specific objects (such as Users, or API Keys), this paremeter restricts results to objects that match this ID. | [optional] |
| **queryTargetName** | **String**| If searching for Histories about Users, Groups or other objects with names, this parameter restricts results to objects with this name/username. | [optional] |
| **queryTargetPermission** | **String**| If searching for Histories about Permisisons, this parameter restricts results to permissions of this level. | [optional] |
| **queryTargetPermissionSet** | **String**| If searching for Histories about API keys, this parameter restricts results to API keys with this permission set. | [optional] |
| **queryTargetPlatform** | **String**| If searching for Histories about API keys, this parameter restricts results to API keys associated with this platform. | [optional] |
| **queryTargetUserId** | **String**| If searching for Histories about API keys, this parameter restricts results to API keys created by/for this user ID. | [optional] |
| **queryTargetUsername** | **String**| If searching for Histories about API keys, this parameter restricts results to API keys created by/for this username. | [optional] |
| **queryUserId** | **String**| Return results that are actions performed by the user indiciated by this User ID | [optional] |
| **queryUsername** | **String**| Filter results by this username. | [optional] |
| **startAt** | **OffsetDateTime**| Start date/time of export range. | [optional] |
| **userId** | **Integer**| User ID.  Provide a value of &#x60;0&#x60; to operate the current session&#39;s user. | [optional] |

### Return type

[**HistoryExportEntity**](HistoryExportEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The HistoryExports object. |  -  |
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

