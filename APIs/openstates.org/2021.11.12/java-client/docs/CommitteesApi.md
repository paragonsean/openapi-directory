# CommitteesApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**committeeDetailCommitteesCommitteeIdGet**](CommitteesApi.md#committeeDetailCommitteesCommitteeIdGet) | **GET** /committees/{committee_id} | Committee Detail |
| [**committeeListCommitteesGet**](CommitteesApi.md#committeeListCommitteesGet) | **GET** /committees | Committee List |


<a id="committeeDetailCommitteesCommitteeIdGet"></a>
# **committeeDetailCommitteesCommitteeIdGet**
> Committee committeeDetailCommitteesCommitteeIdGet(committeeId, include, apikey, xApiKey)

Committee Detail

Get details on a single committee by ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CommitteesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    CommitteesApi apiInstance = new CommitteesApi(defaultClient);
    String committeeId = "committeeId_example"; // String | 
    List<CommitteeInclude> include = Arrays.asList(); // List<CommitteeInclude> | Additional includes for the Committee response.
    String apikey = "apikey_example"; // String | 
    String xApiKey = "xApiKey_example"; // String | 
    try {
      Committee result = apiInstance.committeeDetailCommitteesCommitteeIdGet(committeeId, include, apikey, xApiKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CommitteesApi#committeeDetailCommitteesCommitteeIdGet");
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
| **committeeId** | **String**|  | |
| **include** | [**List&lt;CommitteeInclude&gt;**](CommitteeInclude.md)| Additional includes for the Committee response. | [optional] |
| **apikey** | **String**|  | [optional] |
| **xApiKey** | **String**|  | [optional] |

### Return type

[**Committee**](Committee.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

<a id="committeeListCommitteesGet"></a>
# **committeeListCommitteesGet**
> CommitteeList committeeListCommitteesGet(jurisdiction, classification, parent, chamber, include, apikey, page, perPage, xApiKey)

Committee List

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CommitteesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    CommitteesApi apiInstance = new CommitteesApi(defaultClient);
    String jurisdiction = "jurisdiction_example"; // String | Filter by jurisdiction name or ID.
    CommitteeClassification classification = CommitteeClassification.fromValue("committee"); // CommitteeClassification | 
    String parent = "parent_example"; // String | ocd-organization ID of parent committee.
    OrgClassification chamber = OrgClassification.fromValue("legislature"); // OrgClassification | Chamber of committee, generally upper or lower.
    List<CommitteeInclude> include = Arrays.asList(); // List<CommitteeInclude> | Additional includes for the Committee response.
    String apikey = "apikey_example"; // String | 
    Integer page = 1; // Integer | 
    Integer perPage = 20; // Integer | 
    String xApiKey = "xApiKey_example"; // String | 
    try {
      CommitteeList result = apiInstance.committeeListCommitteesGet(jurisdiction, classification, parent, chamber, include, apikey, page, perPage, xApiKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CommitteesApi#committeeListCommitteesGet");
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
| **jurisdiction** | **String**| Filter by jurisdiction name or ID. | [optional] |
| **classification** | [**CommitteeClassification**](.md)|  | [optional] [enum: committee, subcommittee] |
| **parent** | **String**| ocd-organization ID of parent committee. | [optional] |
| **chamber** | [**OrgClassification**](.md)| Chamber of committee, generally upper or lower. | [optional] [enum: legislature, executive, lower, upper, government] |
| **include** | [**List&lt;CommitteeInclude&gt;**](CommitteeInclude.md)| Additional includes for the Committee response. | [optional] |
| **apikey** | **String**|  | [optional] |
| **page** | **Integer**|  | [optional] [default to 1] |
| **perPage** | **Integer**|  | [optional] [default to 20] |
| **xApiKey** | **String**|  | [optional] |

### Return type

[**CommitteeList**](CommitteeList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **422** | Validation Error |  -  |

