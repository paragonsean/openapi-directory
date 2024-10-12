# RelationUsageApi

All URIs are relative to */api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getRelationUsageBetweenResource**](RelationUsageApi.md#getRelationUsageBetweenResource) | **GET** /relation/usage/between/{subject_category}/{object_category} | All relations used plus count of associations |
| [**getRelationUsagePivotLabelResource**](RelationUsageApi.md#getRelationUsagePivotLabelResource) | **GET** /relation/usage/pivot/label | Relation usage count for all subj x obj category combinations, showing label |
| [**getRelationUsagePivotResource**](RelationUsageApi.md#getRelationUsagePivotResource) | **GET** /relation/usage/pivot | Relation usage count for all subj x obj category combinations |
| [**getRelationUsageResource**](RelationUsageApi.md#getRelationUsageResource) | **GET** /relation/usage/ | All relations used plus count of associations |


<a id="getRelationUsageBetweenResource"></a>
# **getRelationUsageBetweenResource**
> List&lt;AssociationResults&gt; getRelationUsageBetweenResource(subjectCategory, objectCategory, subjectTaxon, evidence)

All relations used plus count of associations

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RelationUsageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    RelationUsageApi apiInstance = new RelationUsageApi(defaultClient);
    String subjectCategory = "subjectCategory_example"; // String | 
    String objectCategory = "objectCategory_example"; // String | 
    String subjectTaxon = "subjectTaxon_example"; // String | SUBJECT TAXON id, e.g. NCBITaxon:9606. Includes inferred by default
    String evidence = "evidence_example"; // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                     
    try {
      List<AssociationResults> result = apiInstance.getRelationUsageBetweenResource(subjectCategory, objectCategory, subjectTaxon, evidence);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RelationUsageApi#getRelationUsageBetweenResource");
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
| **subjectCategory** | **String**|  | |
| **objectCategory** | **String**|  | |
| **subjectTaxon** | **String**| SUBJECT TAXON id, e.g. NCBITaxon:9606. Includes inferred by default | [optional] |
| **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                      | [optional] |

### Return type

[**List&lt;AssociationResults&gt;**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="getRelationUsagePivotLabelResource"></a>
# **getRelationUsagePivotLabelResource**
> List&lt;AssociationResults&gt; getRelationUsagePivotLabelResource(subjectTaxon, evidence)

Relation usage count for all subj x obj category combinations, showing label

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RelationUsageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    RelationUsageApi apiInstance = new RelationUsageApi(defaultClient);
    String subjectTaxon = "subjectTaxon_example"; // String | SUBJECT TAXON id, e.g. NCBITaxon:9606. Includes inferred by default
    String evidence = "evidence_example"; // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                     
    try {
      List<AssociationResults> result = apiInstance.getRelationUsagePivotLabelResource(subjectTaxon, evidence);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RelationUsageApi#getRelationUsagePivotLabelResource");
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
| **subjectTaxon** | **String**| SUBJECT TAXON id, e.g. NCBITaxon:9606. Includes inferred by default | [optional] |
| **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                      | [optional] |

### Return type

[**List&lt;AssociationResults&gt;**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="getRelationUsagePivotResource"></a>
# **getRelationUsagePivotResource**
> List&lt;AssociationResults&gt; getRelationUsagePivotResource(subjectTaxon, evidence)

Relation usage count for all subj x obj category combinations

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RelationUsageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    RelationUsageApi apiInstance = new RelationUsageApi(defaultClient);
    String subjectTaxon = "subjectTaxon_example"; // String | SUBJECT TAXON id, e.g. NCBITaxon:9606. Includes inferred by default
    String evidence = "evidence_example"; // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                     
    try {
      List<AssociationResults> result = apiInstance.getRelationUsagePivotResource(subjectTaxon, evidence);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RelationUsageApi#getRelationUsagePivotResource");
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
| **subjectTaxon** | **String**| SUBJECT TAXON id, e.g. NCBITaxon:9606. Includes inferred by default | [optional] |
| **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                      | [optional] |

### Return type

[**List&lt;AssociationResults&gt;**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="getRelationUsageResource"></a>
# **getRelationUsageResource**
> List&lt;AssociationResults&gt; getRelationUsageResource(subjectTaxon, evidence)

All relations used plus count of associations

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RelationUsageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    RelationUsageApi apiInstance = new RelationUsageApi(defaultClient);
    String subjectTaxon = "subjectTaxon_example"; // String | SUBJECT TAXON id, e.g. NCBITaxon:9606. Includes inferred by default
    String evidence = "evidence_example"; // String | Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                     
    try {
      List<AssociationResults> result = apiInstance.getRelationUsageResource(subjectTaxon, evidence);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RelationUsageApi#getRelationUsageResource");
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
| **subjectTaxon** | **String**| SUBJECT TAXON id, e.g. NCBITaxon:9606. Includes inferred by default | [optional] |
| **evidence** | **String**| Object id, e.g. ECO:0000501 (for IEA; Includes inferred by default)                     or a specific publication or other supporting ibject, e.g. ZFIN:ZDB-PUB-060503-2.                      | [optional] |

### Return type

[**List&lt;AssociationResults&gt;**](AssociationResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

