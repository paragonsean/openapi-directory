# BillsApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**billDetailBillsJurisdictionSessionBillIdGet**](BillsApi.md#billDetailBillsJurisdictionSessionBillIdGet) | **GET** /bills/{jurisdiction}/{session}/{bill_id} | Bill Detail |
| [**billDetailByIdBillsOcdBillOpenstatesBillIdGet**](BillsApi.md#billDetailByIdBillsOcdBillOpenstatesBillIdGet) | **GET** /bills/ocd-bill/{openstates_bill_id} | Bill Detail By Id |
| [**billsSearchBillsGet**](BillsApi.md#billsSearchBillsGet) | **GET** /bills | Bills Search |


<a id="billDetailBillsJurisdictionSessionBillIdGet"></a>
# **billDetailBillsJurisdictionSessionBillIdGet**
> Bill billDetailBillsJurisdictionSessionBillIdGet(jurisdiction, session, billId, include, apikey, xApiKey)

Bill Detail

Obtain bill information based on (state, session, bill_id).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BillsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    BillsApi apiInstance = new BillsApi(defaultClient);
    String jurisdiction = "jurisdiction_example"; // String | 
    String session = "session_example"; // String | 
    String billId = "billId_example"; // String | 
    List<BillInclude> include = Arrays.asList(); // List<BillInclude> | 
    String apikey = "apikey_example"; // String | 
    String xApiKey = "xApiKey_example"; // String | 
    try {
      Bill result = apiInstance.billDetailBillsJurisdictionSessionBillIdGet(jurisdiction, session, billId, include, apikey, xApiKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BillsApi#billDetailBillsJurisdictionSessionBillIdGet");
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
| **jurisdiction** | **String**|  | |
| **session** | **String**|  | |
| **billId** | **String**|  | |
| **include** | [**List&lt;BillInclude&gt;**](BillInclude.md)|  | [optional] |
| **apikey** | **String**|  | [optional] |
| **xApiKey** | **String**|  | [optional] |

### Return type

[**Bill**](Bill.md)

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

<a id="billDetailByIdBillsOcdBillOpenstatesBillIdGet"></a>
# **billDetailByIdBillsOcdBillOpenstatesBillIdGet**
> Bill billDetailByIdBillsOcdBillOpenstatesBillIdGet(openstatesBillId, include, apikey, xApiKey)

Bill Detail By Id

Obtain bill information by internal ID in the format ocd-bill/_*uuid*.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BillsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    BillsApi apiInstance = new BillsApi(defaultClient);
    String openstatesBillId = "openstatesBillId_example"; // String | 
    List<BillInclude> include = Arrays.asList(); // List<BillInclude> | 
    String apikey = "apikey_example"; // String | 
    String xApiKey = "xApiKey_example"; // String | 
    try {
      Bill result = apiInstance.billDetailByIdBillsOcdBillOpenstatesBillIdGet(openstatesBillId, include, apikey, xApiKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BillsApi#billDetailByIdBillsOcdBillOpenstatesBillIdGet");
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
| **openstatesBillId** | **String**|  | |
| **include** | [**List&lt;BillInclude&gt;**](BillInclude.md)|  | [optional] |
| **apikey** | **String**|  | [optional] |
| **xApiKey** | **String**|  | [optional] |

### Return type

[**Bill**](Bill.md)

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

<a id="billsSearchBillsGet"></a>
# **billsSearchBillsGet**
> BillList billsSearchBillsGet(jurisdiction, session, chamber, identifier, classification, subject, updatedSince, createdSince, actionSince, sort, sponsor, sponsorClassification, q, include, page, perPage, apikey, xApiKey)

Bills Search

Search for bills matching given criteria.  Must either specify a jurisdiction or a full text query (q).  Additional parameters will futher restrict bills returned.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BillsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    BillsApi apiInstance = new BillsApi(defaultClient);
    String jurisdiction = "jurisdiction_example"; // String | Filter by jurisdiction name or ID.
    String session = "session_example"; // String | Filter by session identifier.
    String chamber = "chamber_example"; // String | Filter by chamber of origination.
    List<String> identifier = Arrays.asList(); // List<String> | Filter to only include bills with this identifier.
    String classification = "classification_example"; // String | Filter by classification, e.g. bill or resolution
    List<String> subject = Arrays.asList(); // List<String> | Filter by one or more subjects.
    String updatedSince = "updatedSince_example"; // String | Filter to only include bills with updates since a given date.
    String createdSince = "createdSince_example"; // String | Filter to only include bills created since a given date.
    String actionSince = "actionSince_example"; // String | Filter to only include bills with an action since a given date.
    BillSortOption sort = BillSortOption.fromValue("updated_asc"); // BillSortOption | Desired sort order for bill results.
    String sponsor = "sponsor_example"; // String | Filter to only include bills sponsored by a given name or person ID.
    String sponsorClassification = "sponsorClassification_example"; // String | Filter matched sponsors to only include particular types of sponsorships.
    String q = "q_example"; // String | Filter by full text search term.
    List<BillInclude> include = Arrays.asList(); // List<BillInclude> | Additional information to include in response.
    Integer page = 1; // Integer | 
    Integer perPage = 10; // Integer | 
    String apikey = "apikey_example"; // String | 
    String xApiKey = "xApiKey_example"; // String | 
    try {
      BillList result = apiInstance.billsSearchBillsGet(jurisdiction, session, chamber, identifier, classification, subject, updatedSince, createdSince, actionSince, sort, sponsor, sponsorClassification, q, include, page, perPage, apikey, xApiKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BillsApi#billsSearchBillsGet");
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
| **session** | **String**| Filter by session identifier. | [optional] |
| **chamber** | **String**| Filter by chamber of origination. | [optional] |
| **identifier** | [**List&lt;String&gt;**](String.md)| Filter to only include bills with this identifier. | [optional] |
| **classification** | **String**| Filter by classification, e.g. bill or resolution | [optional] |
| **subject** | [**List&lt;String&gt;**](String.md)| Filter by one or more subjects. | [optional] |
| **updatedSince** | **String**| Filter to only include bills with updates since a given date. | [optional] |
| **createdSince** | **String**| Filter to only include bills created since a given date. | [optional] |
| **actionSince** | **String**| Filter to only include bills with an action since a given date. | [optional] |
| **sort** | [**BillSortOption**](.md)| Desired sort order for bill results. | [optional] [default to updated_desc] [enum: updated_asc, updated_desc, first_action_asc, first_action_desc, latest_action_asc, latest_action_desc] |
| **sponsor** | **String**| Filter to only include bills sponsored by a given name or person ID. | [optional] |
| **sponsorClassification** | **String**| Filter matched sponsors to only include particular types of sponsorships. | [optional] |
| **q** | **String**| Filter by full text search term. | [optional] |
| **include** | [**List&lt;BillInclude&gt;**](BillInclude.md)| Additional information to include in response. | [optional] |
| **page** | **Integer**|  | [optional] [default to 1] |
| **perPage** | **Integer**|  | [optional] [default to 10] |
| **apikey** | **String**|  | [optional] |
| **xApiKey** | **String**|  | [optional] |

### Return type

[**BillList**](BillList.md)

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

