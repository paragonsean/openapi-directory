# DracoonApi.EventlogApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**requestAuditNodeInfo**](EventlogApi.md#requestAuditNodeInfo) | **GET** /v4/eventlog/audits/node_info | Request nodes
[**requestAuditNodeUserData**](EventlogApi.md#requestAuditNodeUserData) | **GET** /v4/eventlog/audits/nodes | Request node assigned users with permissions
[**requestLogEventsAsJson**](EventlogApi.md#requestLogEventsAsJson) | **GET** /v4/eventlog/events | Request system events
[**requestLogOperations**](EventlogApi.md#requestLogOperations) | **GET** /v4/eventlog/operations | Request allowed Log Operations



## requestAuditNodeInfo

> AuditNodeInfoResponse requestAuditNodeInfo(opts)

Request nodes

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.31.0&lt;/h3&gt;  ### Description:  Retrieve a list of all nodes of type room under a certain parent.  ### Precondition: Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; read audit log&lt;/span&gt; required.  ### Postcondition: List of rooms.  ### Further Information: For rooms on root level, use parent_id &#x3D; 0.  ### Filtering: All filter fields are connected via logical conjunction (**AND**)   Filter string syntax: &#x60;FIELD_NAME:OPERATOR:VALUE[:VALUE...]&#x60;  &lt;details style&#x3D;\&quot;padding-left: 10px\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Example&lt;/strong&gt;&lt;/summary&gt;  &#x60;nodeName:cn:searchString_1|nodeIsEncrypted:eq:true&#x60;   Filter by node name containing &#x60;searchString_1&#x60; **AND** node is encrypted .  &lt;/details&gt;  ### Filtering options: &lt;details style&#x3D;\&quot;padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Expand&lt;/strong&gt;&lt;/summary&gt;  | &#x60;FIELD_NAME&#x60; | Filter Description | &#x60;OPERATOR&#x60; | Operator Description | &#x60;VALUE&#x60; | | :--- | :--- | :--- | :--- | :--- | | &#x60;nodeId&#x60; | Node ID filter | &#x60;eq&#x60; | Node ID equals value. | &#x60;positive Integer&#x60; | | &#x60;nodeName&#x60; | Node name filter | &#x60;cn, eq, sw&#x60; | Node name contains / equals / starts with value. | &#x60;search String&#x60; | | &#x60;nodeIsEncrypted&#x60; | Encrypted node filter | &#x60;eq&#x60; |  | &#x60;true or false&#x60; |  &lt;/details&gt;   ---  ### Sorting: Sort string syntax: &#x60;FIELD_NAME:ORDER&#x60;   &#x60;ORDER&#x60; can be &#x60;asc&#x60; or &#x60;desc&#x60;.   Multiple sort fields are supported.  &lt;details style&#x3D;\&quot;padding-left: 10px\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Example&lt;/strong&gt;&lt;/summary&gt;  &#x60;nodeName:asc&#x60;   Sort by &#x60;nodeName&#x60; ascending.  &lt;/details&gt;  ### Sorting options: &lt;details style&#x3D;\&quot;padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Expand&lt;/strong&gt;&lt;/summary&gt;  | &#x60;FIELD_NAME&#x60; | Description | | :--- | :--- | | &#x60;nodeId&#x60; | Node ID | | &#x60;nodeName&#x60; | Node name |  &lt;/details&gt; 

### Example

```javascript
import DracoonApi from 'dracoon_api';
let defaultClient = DracoonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DracoonApi.EventlogApi();
let opts = {
  'parentId': 789, // Number | Parent node ID.  Only rooms can be parents.  Parent ID `0` or empty is the root node.
  'offset': 56, // Number | Range offset
  'limit': 56, // Number | Range limit.  Maximum 500.   For more results please use paging (`offset` + `limit`).
  'filter': "filter_example", // String | Filter string
  'sort': "sort_example", // String | Sort string
  'xSdsAuthToken': "xSdsAuthToken_example" // String | Authentication token
};
apiInstance.requestAuditNodeInfo(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parentId** | **Number**| Parent node ID.  Only rooms can be parents.  Parent ID &#x60;0&#x60; or empty is the root node. | [optional] 
 **offset** | **Number**| Range offset | [optional] 
 **limit** | **Number**| Range limit.  Maximum 500.   For more results please use paging (&#x60;offset&#x60; + &#x60;limit&#x60;). | [optional] 
 **filter** | **String**| Filter string | [optional] 
 **sort** | **String**| Sort string | [optional] 
 **xSdsAuthToken** | **String**| Authentication token | [optional] 

### Return type

[**AuditNodeInfoResponse**](AuditNodeInfoResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## requestAuditNodeUserData

> [AuditNodeResponse] requestAuditNodeUserData(opts)

Request node assigned users with permissions

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128679; Deprecated since v4.32.0&lt;/h3&gt;  ### Description:  Retrieve a list of all nodes of type room, and the room assignment users with permissions.  ### Precondition: Right &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128275; read audit log&lt;/span&gt; required.  ### Postcondition: List of rooms and their assigned users is returned.  ### Further Information:  Output is limited to **500** entries.   For more results please use filter criteria and the &#x60;limit&#x60; parameter.  ### Filtering: All filter fields are connected via logical conjunction (**AND**)   Except for &#x60;userName&#x60;, &#x60;userFirstName&#x60; and  &#x60;userLastName&#x60; - these are connected via logical disjunction (**OR**)   Filter string syntax: &#x60;FIELD_NAME:OPERATOR:VALUE[:VALUE...]&#x60;  &lt;details style&#x3D;\&quot;padding-left: 10px\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Example&lt;/strong&gt;&lt;/summary&gt;  &#x60;userName:cn:searchString_1|userFirstName:cn:searchString_2|nodeId:eq:2&#x60;   Filter by user login containing &#x60;searchString_1&#x60; **OR** first name containing &#x60;searchString_2&#x60; **AND** node ID equals &#x60;2&#x60;.  &lt;/details&gt;  ### Filtering options: &lt;details style&#x3D;\&quot;padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Expand&lt;/strong&gt;&lt;/summary&gt;  | &#x60;FIELD_NAME&#x60; | Filter Description | &#x60;OPERATOR&#x60; | Operator Description | &#x60;VALUE&#x60; | | :--- | :--- | :--- | :--- | :--- | | &#x60;nodeId&#x60; | Node ID filter | &#x60;eq&#x60; | Node ID equals value. | &#x60;positive Integer&#x60; | | &#x60;nodeName&#x60; | Node name filter | &#x60;cn, eq&#x60; | Node name contains / equals value. | &#x60;search String&#x60; | | &#x60;nodeParentId&#x60; | Node parent ID filter | &#x60;eq&#x60; | Parent ID equals value. | &#x60;positive Integer&#x60;&lt;br&gt;Parent ID &#x60;0&#x60; is the root node. | | &#x60;userId&#x60; | User ID filter | &#x60;eq&#x60; | User ID equals value. | &#x60;positive Integer&#x60; | | &#x60;userName&#x60; | Username (login) filter | &#x60;cn, eq&#x60; | Username contains / equals value. | &#x60;search String&#x60; | | &#x60;userFirstName&#x60; | User first name filter | &#x60;cn, eq&#x60; | User first name contains / equals value. | &#x60;search String&#x60; | | &#x60;userLastName&#x60; | User last name filter | &#x60;cn, eq&#x60; | User last name contains / equals value. | &#x60;search String&#x60; | | &#x60;permissionsManage&#x60; | Filter the users that do (not) have &#x60;manage&#x60; permissions in this room | &#x60;eq&#x60; |  | &#x60;true or false&#x60; | | &#x60;nodeIsEncrypted&#x60; | Encrypted node filter | &#x60;eq&#x60; |  | &#x60;true or false&#x60; | | &#x60;nodeHasActivitiesLog&#x60; | Activities log filter | &#x60;eq&#x60; |  | &#x60;true or false&#x60; |  &lt;/details&gt;  ### Deprecated filtering options: &lt;details style&#x3D;\&quot;padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Expand&lt;/strong&gt;&lt;/summary&gt;  | &#x60;FIELD_NAME&#x60; | Filter Description | &#x60;OPERATOR&#x60; | Operator Description | &#x60;VALUE&#x60; | | :--- | :--- | :--- | :--- | :--- | | &lt;del&gt;&#x60;nodeHasRecycleBin&#x60;&lt;/del&gt; | Recycle bin filter&lt;br&gt;**Filter has no effect!** | &#x60;eq&#x60; |  | &#x60;true or false&#x60; |  &lt;/details&gt;  ---  ### Sorting: Sort string syntax: &#x60;FIELD_NAME:ORDER&#x60;   &#x60;ORDER&#x60; can be &#x60;asc&#x60; or &#x60;desc&#x60;.   Multiple sort fields are supported.  &lt;details style&#x3D;\&quot;padding-left: 10px\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Example&lt;/strong&gt;&lt;/summary&gt;  &#x60;nodeName:asc&#x60;   Sort by &#x60;nodeName&#x60; ascending.  &lt;/details&gt;  ### Sorting options: &lt;details style&#x3D;\&quot;padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Expand&lt;/strong&gt;&lt;/summary&gt;  | &#x60;FIELD_NAME&#x60; | Description | | :--- | :--- | | &#x60;nodeId&#x60; | Node ID | | &#x60;nodeName&#x60; | Node name | | &#x60;nodeParentId&#x60; | Node parent ID | | &#x60;nodeSize&#x60; | Node size | | &#x60;nodeQuota&#x60; | Node quota |  &lt;/details&gt;

### Example

```javascript
import DracoonApi from 'dracoon_api';
let defaultClient = DracoonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DracoonApi.EventlogApi();
let opts = {
  'xSdsDateFormat': "xSdsDateFormat_example", // String | Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) & [leettime.de](http://leettime.de/))
  'offset': 56, // Number | Range offset
  'limit': 56, // Number | Range limit.  Maximum 500.   For more results please use paging (`offset` + `limit`).
  'filter': "filter_example", // String | Filter string
  'sort': "sort_example", // String | Sort string
  'xSdsAuthToken': "xSdsAuthToken_example" // String | Authentication token
};
apiInstance.requestAuditNodeUserData(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xSdsDateFormat** | **String**| Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) &amp; [leettime.de](http://leettime.de/)) | [optional] 
 **offset** | **Number**| Range offset | [optional] 
 **limit** | **Number**| Range limit.  Maximum 500.   For more results please use paging (&#x60;offset&#x60; + &#x60;limit&#x60;). | [optional] 
 **filter** | **String**| Filter string | [optional] 
 **sort** | **String**| Sort string | [optional] 
 **xSdsAuthToken** | **String**| Authentication token | [optional] 

### Return type

[**[AuditNodeResponse]**](AuditNodeResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## requestLogEventsAsJson

> LogEventList requestLogEventsAsJson(opts)

Request system events

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.3.0&lt;/h3&gt;  ### Description:  Retrieve eventlog (audit log) events.  ### Precondition: Role &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128100; Log Auditor&lt;/span&gt; required.  ### Postcondition: List of audit log events is returned.  ### Further Information: Output is limited to **500** entries.   For more results please use filter criteria and paging (&#x60;offset&#x60; + &#x60;limit&#x60;).   Allowed &#x60;Accept-Header&#x60;: * &#x60;Accept: application/json&#x60; * &#x60;Accept: text/csv&#x60;    ---  Sort string syntax: &#x60;FIELD_NAME:ORDER&#x60;   &#x60;ORDER&#x60; can be &#x60;asc&#x60; or &#x60;desc&#x60;.   Multiple sort fields are supported.    &lt;details style&#x3D;\&quot;padding-left: 10px\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Example&lt;/strong&gt;&lt;/summary&gt;  &#x60;time:desc&#x60;   Sort by &#x60;time&#x60; descending (default sort option).  &lt;/details&gt;  ### Sorting options: &lt;details style&#x3D;\&quot;padding: 10px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px;\&quot;&gt; &lt;summary style&#x3D;\&quot;cursor: pointer; outline: none\&quot;&gt;&lt;strong&gt;Expand&lt;/strong&gt;&lt;/summary&gt;  | &#x60;FIELD_NAME&#x60; | Description | | :--- | :--- | | &#x60;time&#x60; | Event timestamp |  &lt;/details&gt;

### Example

```javascript
import DracoonApi from 'dracoon_api';
let defaultClient = DracoonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DracoonApi.EventlogApi();
let opts = {
  'xSdsDateFormat': "xSdsDateFormat_example", // String | Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) & [leettime.de](http://leettime.de/))
  'sort': "sort_example", // String | Sort string
  'offset': 56, // Number | Range offset
  'limit': 56, // Number | Range limit.  Maximum 500.   For more results please use paging (`offset` + `limit`).
  'dateStart': "dateStart_example", // String | Filter events from given date   e.g. `2015-12-31T23:59:00`
  'dateEnd': "dateEnd_example", // String | Filter events until given date   e.g. `2015-12-31T23:59:00`
  'type': 56, // Number | Operation ID   cf. `GET /eventlog/operations`
  'userId': 789, // Number | User ID
  'status': "status_example", // String | Operation status:  * `0` - Success  * `2` - Error
  'userClient': "userClient_example", // String | User client
  'xSdsAuthToken': "xSdsAuthToken_example" // String | Authentication token
};
apiInstance.requestLogEventsAsJson(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **xSdsDateFormat** | **String**| Date time format (cf. [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) &amp; [leettime.de](http://leettime.de/)) | [optional] 
 **sort** | **String**| Sort string | [optional] 
 **offset** | **Number**| Range offset | [optional] 
 **limit** | **Number**| Range limit.  Maximum 500.   For more results please use paging (&#x60;offset&#x60; + &#x60;limit&#x60;). | [optional] 
 **dateStart** | **String**| Filter events from given date   e.g. &#x60;2015-12-31T23:59:00&#x60; | [optional] 
 **dateEnd** | **String**| Filter events until given date   e.g. &#x60;2015-12-31T23:59:00&#x60; | [optional] 
 **type** | **Number**| Operation ID   cf. &#x60;GET /eventlog/operations&#x60; | [optional] 
 **userId** | **Number**| User ID | [optional] 
 **status** | **String**| Operation status:  * &#x60;0&#x60; - Success  * &#x60;2&#x60; - Error | [optional] 
 **userClient** | **String**| User client | [optional] 
 **xSdsAuthToken** | **String**| Authentication token | [optional] 

### Return type

[**LogEventList**](LogEventList.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## requestLogOperations

> LogOperationList requestLogOperations(opts)

Request allowed Log Operations

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.3.0&lt;/h3&gt;  ### Description:  Retrieve eventlog (audit log) operation IDs and the associated log operation description.  ### Precondition: Role &lt;span style&#x3D;&#39;padding: 3px; background-color: #F6F7F8; border: 1px solid #000; border-radius: 5px; display: inline;&#39;&gt;&amp;#128100; Log Auditor&lt;/span&gt; required.  ### Postcondition: List of available log operations is returned.  ### Further Information: None.

### Example

```javascript
import DracoonApi from 'dracoon_api';
let defaultClient = DracoonApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DracoonApi.EventlogApi();
let opts = {
  'isDeprecated': true, // Boolean | Show only deprecated operations
  'xSdsAuthToken': "xSdsAuthToken_example" // String | Authentication token
};
apiInstance.requestLogOperations(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **isDeprecated** | **Boolean**| Show only deprecated operations | [optional] 
 **xSdsAuthToken** | **String**| Authentication token | [optional] 

### Return type

[**LogOperationList**](LogOperationList.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

