# EventlogApi

All URIs are relative to */api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**requestAuditNodeInfo**](EventlogApi.md#requestAuditNodeInfo) | **GET** /v4/eventlog/audits/node_info | Request nodes |
| [**requestAuditNodeUserData**](EventlogApi.md#requestAuditNodeUserData) | **GET** /v4/eventlog/audits/nodes | Request node assigned users with permissions |
| [**requestLogEventsAsJson**](EventlogApi.md#requestLogEventsAsJson) | **GET** /v4/eventlog/events | Request system events |
| [**requestLogOperations**](EventlogApi.md#requestLogOperations) | **GET** /v4/eventlog/operations | Request allowed Log Operations |


<a id="requestAuditNodeInfo"></a>
# **requestAuditNodeInfo**
> AuditNodeInfoResponse requestAuditNodeInfo(parentId, offset, limit, filter, sort, xSdsAuthToken)

Request nodes

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.31.0&lt;/h3&gt;  ### Description:  Retrieve a list of all nodes of type room under a certain parent.  ### Precondition: Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; read audit log&lt;/span&gt; required.  ### Postcondition: List of rooms.  ### Further Information: For rooms on root level, use parent_id &#x3D; 0.  ### Filtering: All filter fields are connected via logical conjunction (**AND**)   Filter string syntax: &#x60;FIELD_NAME:OPERATOR:VALUE[:VALUE...]&#x60;  &lt;details style&#x3D;\&quot;padding-left: 10px\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Example&lt;/strong&gt;&lt;/summary&gt;  &#x60;nodeName:cn:searchString_1|nodeIsEncrypted:eq:true&#x60;   Filter by node name containing &#x60;searchString_1&#x60; **AND** node is encrypted .  &lt;/details&gt;  ### Filtering options: &lt;details style&#x3D;\&quot;padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Expand&lt;/strong&gt;&lt;/summary&gt;  | &#x60;FIELD_NAME&#x60; | Filter Description | &#x60;OPERATOR&#x60; | Operator Description | &#x60;VALUE&#x60; | | :--- | :--- | :--- | :--- | :--- | | &#x60;nodeId&#x60; | Node ID filter | &#x60;eq&#x60; | Node ID equals value. | &#x60;positive Integer&#x60; | | &#x60;nodeName&#x60; | Node name filter | &#x60;cn, eq, sw&#x60; | Node name contains / equals / starts with value. | &#x60;search String&#x60; | | &#x60;nodeIsEncrypted&#x60; | Encrypted node filter | &#x60;eq&#x60; |  | &#x60;true or false&#x60; |  &lt;/details&gt;   ---  ### Sorting: Sort string syntax: &#x60;FIELD_NAME:ORDER&#x60;   &#x60;ORDER&#x60; can be &#x60;asc&#x60; or &#x60;desc&#x60;.   Multiple sort fields are supported.  &lt;details style&#x3D;\&quot;padding-left: 10px\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Example&lt;/strong&gt;&lt;/summary&gt;  &#x60;nodeName:asc&#x60;   Sort by &#x60;nodeName&#x60; ascending.  &lt;/details&gt;  ### Sorting options: &lt;details style&#x3D;\&quot;padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Expand&lt;/strong&gt;&lt;/summary&gt;  | &#x60;FIELD_NAME&#x60; | Description | | :--- | :--- | | &#x60;nodeId&#x60; | Node ID | | &#x60;nodeName&#x60; | Node name |  &lt;/details&gt; 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventlogApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    EventlogApi apiInstance = new EventlogApi(defaultClient);
    Long parentId = 56L; // Long | Parent node ID.  Only rooms can be parents.  Parent ID `0` or empty is the root node.
    Integer offset = 56; // Integer | Range offset
    Integer limit = 56; // Integer | Range limit.  Maximum 500.   For more results please use paging (`offset` + `limit`).
    String filter = "filter_example"; // String | Filter string
    String sort = "sort_example"; // String | Sort string
    String xSdsAuthToken = "xSdsAuthToken_example"; // String | Authentication token
    try {
      AuditNodeInfoResponse result = apiInstance.requestAuditNodeInfo(parentId, offset, limit, filter, sort, xSdsAuthToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventlogApi#requestAuditNodeInfo");
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
| **parentId** | **Long**| Parent node ID.  Only rooms can be parents.  Parent ID &#x60;0&#x60; or empty is the root node. | [optional] |
| **offset** | **Integer**| Range offset | [optional] |
| **limit** | **Integer**| Range limit.  Maximum 500.   For more results please use paging (&#x60;offset&#x60; + &#x60;limit&#x60;). | [optional] |
| **filter** | **String**| Filter string | [optional] |
| **sort** | **String**| Sort string | [optional] |
| **xSdsAuthToken** | **String**| Authentication token | [optional] |

### Return type

[**AuditNodeInfoResponse**](AuditNodeInfoResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **406** | Not Acceptable |  -  |
| **412** | Precondition Failed |  -  |

<a id="requestAuditNodeUserData"></a>
# **requestAuditNodeUserData**
> List&lt;AuditNodeResponse&gt; requestAuditNodeUserData(xSdsDateFormat, offset, limit, filter, sort, xSdsAuthToken)

Request node assigned users with permissions

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128679; Deprecated since v4.32.0&lt;/h3&gt;  ### Description:  Retrieve a list of all nodes of type room, and the room assignment users with permissions.  ### Precondition: Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; read audit log&lt;/span&gt; required.  ### Postcondition: List of rooms and their assigned users is returned.  ### Further Information:  Output is limited to **500** entries.   For more results please use filter criteria and the &#x60;limit&#x60; parameter.  ### Filtering: All filter fields are connected via logical conjunction (**AND**)   Except for &#x60;userName&#x60;, &#x60;userFirstName&#x60; and  &#x60;userLastName&#x60; - these are connected via logical disjunction (**OR**)   Filter string syntax: &#x60;FIELD_NAME:OPERATOR:VALUE[:VALUE...]&#x60;  &lt;details style&#x3D;\&quot;padding-left: 10px\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Example&lt;/strong&gt;&lt;/summary&gt;  &#x60;userName:cn:searchString_1|userFirstName:cn:searchString_2|nodeId:eq:2&#x60;   Filter by user login containing &#x60;searchString_1&#x60; **OR** first name containing &#x60;searchString_2&#x60; **AND** node ID equals &#x60;2&#x60;.  &lt;/details&gt;  ### Filtering options: &lt;details style&#x3D;\&quot;padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Expand&lt;/strong&gt;&lt;/summary&gt;  | &#x60;FIELD_NAME&#x60; | Filter Description | &#x60;OPERATOR&#x60; | Operator Description | &#x60;VALUE&#x60; | | :--- | :--- | :--- | :--- | :--- | | &#x60;nodeId&#x60; | Node ID filter | &#x60;eq&#x60; | Node ID equals value. | &#x60;positive Integer&#x60; | | &#x60;nodeName&#x60; | Node name filter | &#x60;cn, eq&#x60; | Node name contains / equals value. | &#x60;search String&#x60; | | &#x60;nodeParentId&#x60; | Node parent ID filter | &#x60;eq&#x60; | Parent ID equals value. | &#x60;positive Integer&#x60;&lt;br&gt;Parent ID &#x60;0&#x60; is the root node. | | &#x60;userId&#x60; | User ID filter | &#x60;eq&#x60; | User ID equals value. | &#x60;positive Integer&#x60; | | &#x60;userName&#x60; | Username (login) filter | &#x60;cn, eq&#x60; | Username contains / equals value. | &#x60;search String&#x60; | | &#x60;userFirstName&#x60; | User first name filter | &#x60;cn, eq&#x60; | User first name contains / equals value. | &#x60;search String&#x60; | | &#x60;userLastName&#x60; | User last name filter | &#x60;cn, eq&#x60; | User last name contains / equals value. | &#x60;search String&#x60; | | &#x60;permissionsManage&#x60; | Filter the users that do (not) have &#x60;manage&#x60; permissions in this room | &#x60;eq&#x60; |  | &#x60;true or false&#x60; | | &#x60;nodeIsEncrypted&#x60; | Encrypted node filter | &#x60;eq&#x60; |  | &#x60;true or false&#x60; | | &#x60;nodeHasActivitiesLog&#x60; | Activities log filter | &#x60;eq&#x60; |  | &#x60;true or false&#x60; |  &lt;/details&gt;  ### Deprecated filtering options: &lt;details style&#x3D;\&quot;padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Expand&lt;/strong&gt;&lt;/summary&gt;  | &#x60;FIELD_NAME&#x60; | Filter Description | &#x60;OPERATOR&#x60; | Operator Description | &#x60;VALUE&#x60; | | :--- | :--- | :--- | :--- | :--- | | &lt;del&gt;&#x60;nodeHasRecycleBin&#x60;&lt;/del&gt; | Recycle bin filter&lt;br&gt;**Filter has no effect!** | &#x60;eq&#x60; |  | &#x60;true or false&#x60; |  &lt;/details&gt;  ---  ### Sorting: Sort string syntax: &#x60;FIELD_NAME:ORDER&#x60;   &#x60;ORDER&#x60; can be &#x60;asc&#x60; or &#x60;desc&#x60;.   Multiple sort fields are supported.  &lt;details style&#x3D;\&quot;padding-left: 10px\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Example&lt;/strong&gt;&lt;/summary&gt;  &#x60;nodeName:asc&#x60;   Sort by &#x60;nodeName&#x60; ascending.  &lt;/details&gt;  ### Sorting options: &lt;details style&#x3D;\&quot;padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Expand&lt;/strong&gt;&lt;/summary&gt;  | &#x60;FIELD_NAME&#x60; | Description | | :--- | :--- | | &#x60;nodeId&#x60; | Node ID | | &#x60;nodeName&#x60; | Node name | | &#x60;nodeParentId&#x60; | Node parent ID | | &#x60;nodeSize&#x60; | Node size | | &#x60;nodeQuota&#x60; | Node quota |  &lt;/details&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventlogApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    EventlogApi apiInstance = new EventlogApi(defaultClient);
    String xSdsDateFormat = "UTC"; // String | Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) & [leettime.de](http://leettime.de/))
    Integer offset = 56; // Integer | Range offset
    Integer limit = 56; // Integer | Range limit.  Maximum 500.   For more results please use paging (`offset` + `limit`).
    String filter = "filter_example"; // String | Filter string
    String sort = "sort_example"; // String | Sort string
    String xSdsAuthToken = "xSdsAuthToken_example"; // String | Authentication token
    try {
      List<AuditNodeResponse> result = apiInstance.requestAuditNodeUserData(xSdsDateFormat, offset, limit, filter, sort, xSdsAuthToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventlogApi#requestAuditNodeUserData");
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
| **xSdsDateFormat** | **String**| Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) &amp; [leettime.de](http://leettime.de/)) | [optional] [enum: UTC, LOCAL, OFFSET, EPOCH, LEET] |
| **offset** | **Integer**| Range offset | [optional] |
| **limit** | **Integer**| Range limit.  Maximum 500.   For more results please use paging (&#x60;offset&#x60; + &#x60;limit&#x60;). | [optional] |
| **filter** | **String**| Filter string | [optional] |
| **sort** | **String**| Sort string | [optional] |
| **xSdsAuthToken** | **String**| Authentication token | [optional] |

### Return type

[**List&lt;AuditNodeResponse&gt;**](AuditNodeResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **406** | Not Acceptable |  -  |
| **412** | Precondition Failed |  -  |

<a id="requestLogEventsAsJson"></a>
# **requestLogEventsAsJson**
> LogEventList requestLogEventsAsJson(xSdsDateFormat, sort, offset, limit, dateStart, dateEnd, type, userId, status, userClient, xSdsAuthToken)

Request system events

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.3.0&lt;/h3&gt;  ### Description:  Retrieve eventlog (audit log) events.  ### Precondition: Role &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128100; Log Auditor&lt;/span&gt; required.  ### Postcondition: List of audit log events is returned.  ### Further Information: Output is limited to **500** entries.   For more results please use filter criteria and paging (&#x60;offset&#x60; + &#x60;limit&#x60;).   Allowed &#x60;Accept-Header&#x60;: * &#x60;Accept: application/json&#x60; * &#x60;Accept: text/csv&#x60;    ---  Sort string syntax: &#x60;FIELD_NAME:ORDER&#x60;   &#x60;ORDER&#x60; can be &#x60;asc&#x60; or &#x60;desc&#x60;.   Multiple sort fields are supported.    &lt;details style&#x3D;\&quot;padding-left: 10px\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Example&lt;/strong&gt;&lt;/summary&gt;  &#x60;time:desc&#x60;   Sort by &#x60;time&#x60; descending (default sort option).  &lt;/details&gt;  ### Sorting options: &lt;details style&#x3D;\&quot;padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Expand&lt;/strong&gt;&lt;/summary&gt;  | &#x60;FIELD_NAME&#x60; | Description | | :--- | :--- | | &#x60;time&#x60; | Event timestamp |  &lt;/details&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventlogApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    EventlogApi apiInstance = new EventlogApi(defaultClient);
    String xSdsDateFormat = "UTC"; // String | Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) & [leettime.de](http://leettime.de/))
    String sort = "sort_example"; // String | Sort string
    Integer offset = 56; // Integer | Range offset
    Integer limit = 56; // Integer | Range limit.  Maximum 500.   For more results please use paging (`offset` + `limit`).
    String dateStart = "dateStart_example"; // String | Filter events from given date   e.g. `2015-12-31T23:59:00`
    String dateEnd = "dateEnd_example"; // String | Filter events until given date   e.g. `2015-12-31T23:59:00`
    Integer type = 56; // Integer | Operation ID   cf. `GET /eventlog/operations`
    Long userId = 56L; // Long | User ID
    String status = "0"; // String | Operation status:  * `0` - Success  * `2` - Error
    String userClient = "userClient_example"; // String | User client
    String xSdsAuthToken = "xSdsAuthToken_example"; // String | Authentication token
    try {
      LogEventList result = apiInstance.requestLogEventsAsJson(xSdsDateFormat, sort, offset, limit, dateStart, dateEnd, type, userId, status, userClient, xSdsAuthToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventlogApi#requestLogEventsAsJson");
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
| **xSdsDateFormat** | **String**| Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) &amp; [leettime.de](http://leettime.de/)) | [optional] [enum: UTC, LOCAL, OFFSET, EPOCH, LEET] |
| **sort** | **String**| Sort string | [optional] |
| **offset** | **Integer**| Range offset | [optional] |
| **limit** | **Integer**| Range limit.  Maximum 500.   For more results please use paging (&#x60;offset&#x60; + &#x60;limit&#x60;). | [optional] |
| **dateStart** | **String**| Filter events from given date   e.g. &#x60;2015-12-31T23:59:00&#x60; | [optional] |
| **dateEnd** | **String**| Filter events until given date   e.g. &#x60;2015-12-31T23:59:00&#x60; | [optional] |
| **type** | **Integer**| Operation ID   cf. &#x60;GET /eventlog/operations&#x60; | [optional] |
| **userId** | **Long**| User ID | [optional] |
| **status** | **String**| Operation status:  * &#x60;0&#x60; - Success  * &#x60;2&#x60; - Error | [optional] [enum: 0, 2] |
| **userClient** | **String**| User client | [optional] |
| **xSdsAuthToken** | **String**| Authentication token | [optional] |

### Return type

[**LogEventList**](LogEventList.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **406** | Not Acceptable |  -  |
| **412** | Precondition Failed |  -  |

<a id="requestLogOperations"></a>
# **requestLogOperations**
> LogOperationList requestLogOperations(isDeprecated, xSdsAuthToken)

Request allowed Log Operations

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.3.0&lt;/h3&gt;  ### Description:  Retrieve eventlog (audit log) operation IDs and the associated log operation description.  ### Precondition: Role &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128100; Log Auditor&lt;/span&gt; required.  ### Postcondition: List of available log operations is returned.  ### Further Information: None.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventlogApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    EventlogApi apiInstance = new EventlogApi(defaultClient);
    Boolean isDeprecated = true; // Boolean | Show only deprecated operations
    String xSdsAuthToken = "xSdsAuthToken_example"; // String | Authentication token
    try {
      LogOperationList result = apiInstance.requestLogOperations(isDeprecated, xSdsAuthToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventlogApi#requestLogOperations");
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
| **isDeprecated** | **Boolean**| Show only deprecated operations | [optional] |
| **xSdsAuthToken** | **String**| Authentication token | [optional] |

### Return type

[**LogOperationList**](LogOperationList.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **406** | Not Acceptable |  -  |
| **412** | Precondition Failed |  -  |

