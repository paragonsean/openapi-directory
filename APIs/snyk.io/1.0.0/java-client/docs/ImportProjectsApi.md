# ImportProjectsApi

All URIs are relative to *https://api.snyk.io/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getImportJobDetails**](ImportProjectsApi.md#getImportJobDetails) | **GET** /org/{orgId}/integrations/{integrationId}/import/{jobId} | Get import job details |
| [**importTargets**](ImportProjectsApi.md#importTargets) | **POST** /org/{orgId}/integrations/{integrationId}/import | Import targets |


<a id="getImportJobDetails"></a>
# **getImportJobDetails**
> GetImportJobDetails200Response getImportJobDetails(orgId, integrationId, jobId)

Get import job details



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ImportProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.snyk.io/v1");

    ImportProjectsApi apiInstance = new ImportProjectsApi(defaultClient);
    String orgId = "4a18d42f-0706-4ad0-b127-24078731fbed"; // String | The organization ID. The `API_KEY` must have admin access to this organization.
    String integrationId = "9a3e5d90-b782-468a-a042-9a2073736f0b"; // String | The unique identifier for the configured integration. This can be found on the [Integration page in the Settings area](https://app.snyk.io/manage/integrations) for all integrations that have been configured.
    String jobId = "1a325d9d-b782-468a-a242-9a2073734f0b"; // String | The ID of the job. This can be found in the Location response header from the corresponding POST request that triggered the import job.
    try {
      GetImportJobDetails200Response result = apiInstance.getImportJobDetails(orgId, integrationId, jobId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImportProjectsApi#getImportJobDetails");
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
| **orgId** | **String**| The organization ID. The &#x60;API_KEY&#x60; must have admin access to this organization. | |
| **integrationId** | **String**| The unique identifier for the configured integration. This can be found on the [Integration page in the Settings area](https://app.snyk.io/manage/integrations) for all integrations that have been configured. | |
| **jobId** | **String**| The ID of the job. This can be found in the Location response header from the corresponding POST request that triggered the import job. | |

### Return type

[**GetImportJobDetails200Response**](GetImportJobDetails200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="importTargets"></a>
# **importTargets**
> importTargets(orgId, integrationId, importTargetsRequest)

Import targets



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ImportProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.snyk.io/v1");

    ImportProjectsApi apiInstance = new ImportProjectsApi(defaultClient);
    String orgId = "4a18d42f-0706-4ad0-b127-24078731fbed"; // String | The organization ID. The `API_KEY` must have admin access to this organization.
    String integrationId = "9a3e5d90-b782-468a-a042-9a2073736f0b"; // String | The unique identifier for the configured integration. This can be found on the [Integration page in the Settings area](https://app.snyk.io/manage/integrations) for all integrations that have been configured.
    ImportTargetsRequest importTargetsRequest = new ImportTargetsRequest(); // ImportTargetsRequest | 
    try {
      apiInstance.importTargets(orgId, integrationId, importTargetsRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImportProjectsApi#importTargets");
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
| **orgId** | **String**| The organization ID. The &#x60;API_KEY&#x60; must have admin access to this organization. | |
| **integrationId** | **String**| The unique identifier for the configured integration. This can be found on the [Integration page in the Settings area](https://app.snyk.io/manage/integrations) for all integrations that have been configured. | |
| **importTargetsRequest** | [**ImportTargetsRequest**](ImportTargetsRequest.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  * Location -  <br>  |

