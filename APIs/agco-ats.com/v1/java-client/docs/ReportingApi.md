# ReportingApi

All URIs are relative to *https://secure.agco-ats.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**reportingBundleStatusSummary**](ReportingApi.md#reportingBundleStatusSummary) | **GET** /api/v2/Reporting/BundleStatusSummary | Get a summary of all Packages in a Bundle |
| [**reportingBundlesInUpdateGroup**](ReportingApi.md#reportingBundlesInUpdateGroup) | **GET** /api/v2/Reporting/BundlesInUpdateGroup | Get a list of bundles for UpdateGroup. |
| [**reportingClientInfo**](ReportingApi.md#reportingClientInfo) | **GET** /api/v2/Reporting/ClientInfo | Get Client Information |
| [**reportingCurrentPackagesInUpdateGroup**](ReportingApi.md#reportingCurrentPackagesInUpdateGroup) | **GET** /api/v2/Reporting/CurrentPackagesInUpdateGroup | Get the current packages for an update group. |
| [**reportingGetClient**](ReportingApi.md#reportingGetClient) | **GET** /api/v2/Reporting/GetClient | Get a Client in the Update System. |
| [**reportingGetSubscriptions**](ReportingApi.md#reportingGetSubscriptions) | **GET** /api/v2/Reporting/GetSubscriptions | Get a list of current Client Subscriptions. |
| [**reportingPackageStatusSummary**](ReportingApi.md#reportingPackageStatusSummary) | **GET** /api/v2/Reporting/PackageStatusSummary | Get a summary report for a Specific Package |
| [**reportingRegisteredClients**](ReportingApi.md#reportingRegisteredClients) | **GET** /api/v2/Reporting/RegisteredClients | Get a list of subscribed clients |
| [**reportingUpdateGroups**](ReportingApi.md#reportingUpdateGroups) | **GET** /api/v2/Reporting/UpdateGroups | Get a list of Update Groups.  Update Groups are used by the client to register for a specific type of update. |
| [**reportingUpdateMetrics**](ReportingApi.md#reportingUpdateMetrics) | **GET** /api/v2/Reporting/UpdateMetrics | Get data for pie charts in UpdateMetrics. |


<a id="reportingBundleStatusSummary"></a>
# **reportingBundleStatusSummary**
> APIPagedResponseUpdateSystemModelsPackageStatusSummary reportingBundleStatusSummary(bundleID, limit, offset)

Get a summary of all Packages in a Bundle

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReportingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    ReportingApi apiInstance = new ReportingApi(defaultClient);
    String bundleID = "bundleID_example"; // String | The BundleID
    Integer limit = 56; // Integer | Optional. The page limit. The default page limit is 10.
    Integer offset = 56; // Integer | Optional. The page offset. The default page offset is 0.
    try {
      APIPagedResponseUpdateSystemModelsPackageStatusSummary result = apiInstance.reportingBundleStatusSummary(bundleID, limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReportingApi#reportingBundleStatusSummary");
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
| **bundleID** | **String**| The BundleID | |
| **limit** | **Integer**| Optional. The page limit. The default page limit is 10. | [optional] |
| **offset** | **Integer**| Optional. The page offset. The default page offset is 0. | [optional] |

### Return type

[**APIPagedResponseUpdateSystemModelsPackageStatusSummary**](APIPagedResponseUpdateSystemModelsPackageStatusSummary.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | API Error Response |  -  |

<a id="reportingBundlesInUpdateGroup"></a>
# **reportingBundlesInUpdateGroup**
> APIPagedResponseUpdateSystemModelsBundle reportingBundlesInUpdateGroup(ID, includeInactive, limit, offset)

Get a list of bundles for UpdateGroup.

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReportingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    ReportingApi apiInstance = new ReportingApi(defaultClient);
    String ID = "ID_example"; // String | The UpdateGroupID
    Boolean includeInactive = true; // Boolean | Include Inactive Bundles (true|false)
    Integer limit = 56; // Integer | Optional. The page limit. The default page limit is 10.
    Integer offset = 56; // Integer | Optional. The page offset. The default page offset is 0.
    try {
      APIPagedResponseUpdateSystemModelsBundle result = apiInstance.reportingBundlesInUpdateGroup(ID, includeInactive, limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReportingApi#reportingBundlesInUpdateGroup");
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
| **ID** | **String**| The UpdateGroupID | |
| **includeInactive** | **Boolean**| Include Inactive Bundles (true|false) | |
| **limit** | **Integer**| Optional. The page limit. The default page limit is 10. | [optional] |
| **offset** | **Integer**| Optional. The page offset. The default page offset is 0. | [optional] |

### Return type

[**APIPagedResponseUpdateSystemModelsBundle**](APIPagedResponseUpdateSystemModelsBundle.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | API Error Response |  -  |

<a id="reportingClientInfo"></a>
# **reportingClientInfo**
> UpdateSystemModelsClientInfo reportingClientInfo(clientID)

Get Client Information

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReportingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    ReportingApi apiInstance = new ReportingApi(defaultClient);
    String clientID = "clientID_example"; // String | The Client ID
    try {
      UpdateSystemModelsClientInfo result = apiInstance.reportingClientInfo(clientID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReportingApi#reportingClientInfo");
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
| **clientID** | **String**| The Client ID | |

### Return type

[**UpdateSystemModelsClientInfo**](UpdateSystemModelsClientInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | API Error Response |  -  |

<a id="reportingCurrentPackagesInUpdateGroup"></a>
# **reportingCurrentPackagesInUpdateGroup**
> List&lt;UpdateSystemModelsPackage&gt; reportingCurrentPackagesInUpdateGroup(ID, subscriptionTypeFilter)

Get the current packages for an update group.

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReportingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    ReportingApi apiInstance = new ReportingApi(defaultClient);
    String ID = "ID_example"; // String | The UpdateGroupID
    String subscriptionTypeFilter = "RequiredOnly"; // String | Optional.  The subscription type filter to use.  By default the Default packages (Required and IncludeByDefault) will be returned.
    try {
      List<UpdateSystemModelsPackage> result = apiInstance.reportingCurrentPackagesInUpdateGroup(ID, subscriptionTypeFilter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReportingApi#reportingCurrentPackagesInUpdateGroup");
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
| **ID** | **String**| The UpdateGroupID | |
| **subscriptionTypeFilter** | **String**| Optional.  The subscription type filter to use.  By default the Default packages (Required and IncludeByDefault) will be returned. | [optional] [enum: RequiredOnly, Default, All] |

### Return type

[**List&lt;UpdateSystemModelsPackage&gt;**](UpdateSystemModelsPackage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | API Error Response |  -  |

<a id="reportingGetClient"></a>
# **reportingGetClient**
> UpdateSystemModelsClient reportingGetClient(ID)

Get a Client in the Update System.

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReportingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    ReportingApi apiInstance = new ReportingApi(defaultClient);
    String ID = "ID_example"; // String | The Client ID
    try {
      UpdateSystemModelsClient result = apiInstance.reportingGetClient(ID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReportingApi#reportingGetClient");
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
| **ID** | **String**| The Client ID | |

### Return type

[**UpdateSystemModelsClient**](UpdateSystemModelsClient.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | API Error Response |  -  |

<a id="reportingGetSubscriptions"></a>
# **reportingGetSubscriptions**
> APIPagedResponseUpdateSystemModelsUpdateGroupClientRelationship reportingGetSubscriptions(clientID, updateGroupID, limit, offset)

Get a list of current Client Subscriptions.

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReportingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    ReportingApi apiInstance = new ReportingApi(defaultClient);
    String clientID = "clientID_example"; // String | Optional. Filter by Client ID
    String updateGroupID = "updateGroupID_example"; // String | Optional. Filter by Update Group ID
    Integer limit = 56; // Integer | Optional. The page limit. The default page limit is 10.
    Integer offset = 56; // Integer | Optional. The page offset. The default page offset is 0.
    try {
      APIPagedResponseUpdateSystemModelsUpdateGroupClientRelationship result = apiInstance.reportingGetSubscriptions(clientID, updateGroupID, limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReportingApi#reportingGetSubscriptions");
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
| **clientID** | **String**| Optional. Filter by Client ID | [optional] |
| **updateGroupID** | **String**| Optional. Filter by Update Group ID | [optional] |
| **limit** | **Integer**| Optional. The page limit. The default page limit is 10. | [optional] |
| **offset** | **Integer**| Optional. The page offset. The default page offset is 0. | [optional] |

### Return type

[**APIPagedResponseUpdateSystemModelsUpdateGroupClientRelationship**](APIPagedResponseUpdateSystemModelsUpdateGroupClientRelationship.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | API Error Response |  -  |

<a id="reportingPackageStatusSummary"></a>
# **reportingPackageStatusSummary**
> UpdateSystemModelsPackageStatusSummary reportingPackageStatusSummary(packageID)

Get a summary report for a Specific Package

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReportingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    ReportingApi apiInstance = new ReportingApi(defaultClient);
    String packageID = "packageID_example"; // String | The Package ID
    try {
      UpdateSystemModelsPackageStatusSummary result = apiInstance.reportingPackageStatusSummary(packageID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReportingApi#reportingPackageStatusSummary");
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
| **packageID** | **String**| The Package ID | |

### Return type

[**UpdateSystemModelsPackageStatusSummary**](UpdateSystemModelsPackageStatusSummary.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | API Error Response |  -  |

<a id="reportingRegisteredClients"></a>
# **reportingRegisteredClients**
> APIPagedResponseUpdateSystemModelsClientStatusUpdateSystemModelsPagedClientStatusMetadata reportingRegisteredClients(updateGroupID, clientID, tag, reportResult, reportResultIsValid, reportValue, lastCheckInBefore, lastCheckInAfter, orderBy, limit, offset)

Get a list of subscribed clients

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReportingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    ReportingApi apiInstance = new ReportingApi(defaultClient);
    String updateGroupID = "updateGroupID_example"; // String | Optional but required when including any or all of following parameters: ReportValue, ReportResult, ReportResultIsValid. The Update Group ID. If not provided, all clients will be returned.
    String clientID = "clientID_example"; // String | Optional. Filter where ClientID matches a value. Wildcards are supported (*).
    String tag = "tag_example"; // String | Optional. Filter where Tag matches a value. Wildcards are supported (*).
    String reportResult = "reportResult_example"; // String | Optional and UpdateGroupID must be included. Filter where ReportResult matches a value. Wildcards are supported (*).
    Boolean reportResultIsValid = true; // Boolean | Optional and UpdateGroupID must be included. When 'true' filters results where ReportResult equals ReportResultExpected.  When 'false' filters results where ValueToValidate does not equal ReportResults.
    String reportValue = "reportValue_example"; // String | Optional and UpdateGroupID must be included. Filter where ReportValue matches a value. Wildcards are supported (*).
    OffsetDateTime lastCheckInBefore = OffsetDateTime.now(); // OffsetDateTime | Optional. Filter where LastCheckIn occured before the provided date.
    OffsetDateTime lastCheckInAfter = OffsetDateTime.now(); // OffsetDateTime | Optional. Filter where LastCheckIn occured after the provided date.
    String orderBy = "orderBy_example"; // String | Optional. Specify the order in which results should be returned. Use this format: [FieldName] [ASC|ASCENDING|DESC|DESCENDING],...                 If sort direction is not provided for a field, it will be sorted ascending.
    Integer limit = 56; // Integer | Optional. The page limit. The default page limit is 10.
    Integer offset = 56; // Integer | Optional. The page offset. The default page offset is 0.
    try {
      APIPagedResponseUpdateSystemModelsClientStatusUpdateSystemModelsPagedClientStatusMetadata result = apiInstance.reportingRegisteredClients(updateGroupID, clientID, tag, reportResult, reportResultIsValid, reportValue, lastCheckInBefore, lastCheckInAfter, orderBy, limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReportingApi#reportingRegisteredClients");
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
| **updateGroupID** | **String**| Optional but required when including any or all of following parameters: ReportValue, ReportResult, ReportResultIsValid. The Update Group ID. If not provided, all clients will be returned. | [optional] |
| **clientID** | **String**| Optional. Filter where ClientID matches a value. Wildcards are supported (*). | [optional] |
| **tag** | **String**| Optional. Filter where Tag matches a value. Wildcards are supported (*). | [optional] |
| **reportResult** | **String**| Optional and UpdateGroupID must be included. Filter where ReportResult matches a value. Wildcards are supported (*). | [optional] |
| **reportResultIsValid** | **Boolean**| Optional and UpdateGroupID must be included. When &#39;true&#39; filters results where ReportResult equals ReportResultExpected.  When &#39;false&#39; filters results where ValueToValidate does not equal ReportResults. | [optional] |
| **reportValue** | **String**| Optional and UpdateGroupID must be included. Filter where ReportValue matches a value. Wildcards are supported (*). | [optional] |
| **lastCheckInBefore** | **OffsetDateTime**| Optional. Filter where LastCheckIn occured before the provided date. | [optional] |
| **lastCheckInAfter** | **OffsetDateTime**| Optional. Filter where LastCheckIn occured after the provided date. | [optional] |
| **orderBy** | **String**| Optional. Specify the order in which results should be returned. Use this format: [FieldName] [ASC|ASCENDING|DESC|DESCENDING],...                 If sort direction is not provided for a field, it will be sorted ascending. | [optional] |
| **limit** | **Integer**| Optional. The page limit. The default page limit is 10. | [optional] |
| **offset** | **Integer**| Optional. The page offset. The default page offset is 0. | [optional] |

### Return type

[**APIPagedResponseUpdateSystemModelsClientStatusUpdateSystemModelsPagedClientStatusMetadata**](APIPagedResponseUpdateSystemModelsClientStatusUpdateSystemModelsPagedClientStatusMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | API Error Response |  -  |

<a id="reportingUpdateGroups"></a>
# **reportingUpdateGroups**
> APIPagedResponseUpdateSystemModelsUpdateGroup reportingUpdateGroups(limit, offset)

Get a list of Update Groups.  Update Groups are used by the client to register for a specific type of update.

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReportingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    ReportingApi apiInstance = new ReportingApi(defaultClient);
    Integer limit = 56; // Integer | Optional. The page limit. The default page limit is 10.
    Integer offset = 56; // Integer | Optional. The page offset. The default page offset is 0.
    try {
      APIPagedResponseUpdateSystemModelsUpdateGroup result = apiInstance.reportingUpdateGroups(limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReportingApi#reportingUpdateGroups");
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
| **limit** | **Integer**| Optional. The page limit. The default page limit is 10. | [optional] |
| **offset** | **Integer**| Optional. The page offset. The default page offset is 0. | [optional] |

### Return type

[**APIPagedResponseUpdateSystemModelsUpdateGroup**](APIPagedResponseUpdateSystemModelsUpdateGroup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | API Error Response |  -  |

<a id="reportingUpdateMetrics"></a>
# **reportingUpdateMetrics**
> UpdateSystemModelsUpdateMetricsData reportingUpdateMetrics(updateGroupID, bundleNumber)

Get data for pie charts in UpdateMetrics.

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReportingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    ReportingApi apiInstance = new ReportingApi(defaultClient);
    String updateGroupID = "updateGroupID_example"; // String | The UpdateType in which clients must be for the report to include them.
    Integer bundleNumber = 56; // Integer | Optional. Tells us which chart to show based upon filter.
    try {
      UpdateSystemModelsUpdateMetricsData result = apiInstance.reportingUpdateMetrics(updateGroupID, bundleNumber);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReportingApi#reportingUpdateMetrics");
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
| **updateGroupID** | **String**| The UpdateType in which clients must be for the report to include them. | |
| **bundleNumber** | **Integer**| Optional. Tells us which chart to show based upon filter. | [optional] |

### Return type

[**UpdateSystemModelsUpdateMetricsData**](UpdateSystemModelsUpdateMetricsData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | API Error Response |  -  |

