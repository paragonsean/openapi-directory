# FileMigrationsApi

All URIs are relative to *http://app.files.com/api/rest/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getFileMigrationsId**](FileMigrationsApi.md#getFileMigrationsId) | **GET** /file_migrations/{id} | Show File Migration |


<a id="getFileMigrationsId"></a>
# **getFileMigrationsId**
> FileMigrationEntity getFileMigrationsId(id)

Show File Migration

Show File Migration

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FileMigrationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://app.files.com/api/rest/v1");

    FileMigrationsApi apiInstance = new FileMigrationsApi(defaultClient);
    Integer id = 56; // Integer | File Migration ID.
    try {
      FileMigrationEntity result = apiInstance.getFileMigrationsId(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FileMigrationsApi#getFileMigrationsId");
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
| **id** | **Integer**| File Migration ID. | |

### Return type

[**FileMigrationEntity**](FileMigrationEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The FileMigrations object. |  -  |
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

