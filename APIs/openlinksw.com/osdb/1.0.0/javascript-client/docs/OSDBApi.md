# OsdbRestApiV1.OSDBApi

All URIs are relative to *https://osdb.openlinksw.com/osdb*

Method | HTTP request | Description
------------- | ------------- | -------------
[**actionHelp**](OSDBApi.md#actionHelp) | **GET** /api/v1/actions/{serviceId}/{actionId}/help | Action help
[**describeAction**](OSDBApi.md#describeAction) | **GET** /api/v1/actions/{serviceId}/{actionId} | Describe action
[**describeService**](OSDBApi.md#describeService) | **GET** /api/v1/services/{serviceId} | Describe service
[**executeAction**](OSDBApi.md#executeAction) | **POST** /api/v1/actions/{serviceId}/{actionId}/exec | Execute action
[**listActions**](OSDBApi.md#listActions) | **GET** /api/v1/actions/{serviceId} | List actions
[**listServices**](OSDBApi.md#listServices) | **GET** /api/v1/services | List services
[**loadService**](OSDBApi.md#loadService) | **POST** /api/v1/services | Load service
[**login**](OSDBApi.md#login) | **GET** /api/v1/login | Login
[**logout**](OSDBApi.md#logout) | **GET** /api/v1/logout | Logout
[**unloadService**](OSDBApi.md#unloadService) | **DELETE** /api/v1/services/{serviceId} | Unload service



## actionHelp

> ActionHelpResponse actionHelp(serviceId, actionId)

Action help

Returns the help text for a given service action

### Example

```javascript
import OsdbRestApiV1 from 'osdb_rest_api_v1';

let apiInstance = new OsdbRestApiV1.OSDBApi();
let serviceId = "serviceId_example"; // String | Service ID of the service supporting the action.
let actionId = "actionId_example"; // String | Action ID of the action for which help text is being requested.
apiInstance.actionHelp(serviceId, actionId, (error, data, response) => {
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
 **serviceId** | **String**| Service ID of the service supporting the action. | 
 **actionId** | **String**| Action ID of the action for which help text is being requested. | 

### Return type

[**ActionHelpResponse**](ActionHelpResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## describeAction

> DescribeActionResponse describeAction(serviceId, actionId)

Describe action

Returns a description of a given service action.

### Example

```javascript
import OsdbRestApiV1 from 'osdb_rest_api_v1';

let apiInstance = new OsdbRestApiV1.OSDBApi();
let serviceId = "serviceId_example"; // String | Service ID of the service supporting the action.
let actionId = "actionId_example"; // String | Action ID of the action to describe.
apiInstance.describeAction(serviceId, actionId, (error, data, response) => {
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
 **serviceId** | **String**| Service ID of the service supporting the action. | 
 **actionId** | **String**| Action ID of the action to describe. | 

### Return type

[**DescribeActionResponse**](DescribeActionResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## describeService

> DescribeServiceResponse describeService(serviceId)

Describe service

Returns a description of a given service

### Example

```javascript
import OsdbRestApiV1 from 'osdb_rest_api_v1';

let apiInstance = new OsdbRestApiV1.OSDBApi();
let serviceId = "serviceId_example"; // String | Service ID of the service to describe.
apiInstance.describeService(serviceId, (error, data, response) => {
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
 **serviceId** | **String**| Service ID of the service to describe. | 

### Return type

[**DescribeServiceResponse**](DescribeServiceResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## executeAction

> executeAction(serviceId, actionId, opts)

Execute action

Executes a registered service action and returns any output from the action. The data returned in the POST response body may be:  * the raw action output,  * a URL encapsulating the action request which executes the action when dereferenced  (only for actions using GET),  * RDF generated from the action output, * a URL to an RDF viewer&#39;s display of the generated RDF.  Any parameters required by the action are supplied as a JSON object in the POST body. The parameter types supported are: \&quot;query\&quot;, \&quot;header\&quot;, \&quot;uri\&quot;, \&quot;path\&quot; and \&quot;body\&quot;.  The parameter type determines where a supplied parameter value is inserted into the HTTP request constructed by OSDB to invoke the target service action. In addition to native parameters required by the service action, &#39;Execute action&#39; accepts some OSDB-specific parameters.&lt;br/&gt;&lt;br/&gt;  **Examples** * &#x60;&#x60;&#x60;curl -ik -X POST -d &#39;{ \&quot;latitude\&quot;:\&quot;37.7759792\&quot;, \&quot;longitude\&quot;:\&quot;-122.41823\&quot; }&#39; -H &#39;Content-Type: application/json&#39; https://osdb.openlinksw.com/osdb/api/v1/actions/uber/products/exec&#x60;&#x60;&#x60;   * &#x60;&#x60;&#x60;curl -ikL -X POST -d &#39;{ \&quot;latitude\&quot;:\&quot;37.7759792\&quot;, \&quot;longitude\&quot;:\&quot;-122.41823\&quot;, \&quot;osdb:output_type\&quot;:\&quot;generate_rdf\&quot;, \&quot;osdb:response_format\&quot;:\&quot;application/rdf+xml\&quot; }&#39; -H &#39;Content-Type: application/json&#39; https://osdb.openlinksw.com/osdb/api/v1/actions/uber/products/exec&#x60;&#x60;&#x60;  * &#x60;&#x60;&#x60;curl -ikL -X POST -d &#39;{ \&quot;latitude\&quot;:\&quot;37.7759792\&quot;, \&quot;longitude\&quot;:\&quot;-122.41823\&quot;, \&quot;osdb:output_type\&quot;:\&quot;display_rdf\&quot; }&#39; -H &#39;Content-Type: application/json&#39; https://osdb.openlinksw.com/osdb/api/v1/actions/uber/products/exec&#x60;&#x60;&#x60;  * &#x60;&#x60;&#x60;curl -ik -X POST -d &#39;{ \&quot;q\&quot;:\&quot;skiing\&quot;, \&quot;osdb:response_format\&quot;: \&quot;application/rdf+xml\&quot; }&#39; -H &#39;Content-Type: application/json&#39; https://osdb.openlinksw.com/osdb/api/v1/actions/facet/search/exec&#x60;&#x60;&#x60;  * &#x60;&#x60;&#x60;curl -ik -X POST -d &#39;{ \&quot;q\&quot;:\&quot;skiing\&quot;, \&quot;osdb:output_type\&quot;: \&quot;url_only\&quot; }&#39; -H &#39;Content-Type: application/json&#39; https://osdb.openlinksw.com/osdb/api/v1/actions/facet/search/exec&#x60;&#x60;&#x60;  * &#x60;&#x60;&#x60;curl -ik -X POST -d &#39;{ \&quot;Content-Location\&quot;: \&quot;http://demo.openlinksw.co.uk/pubs\&quot;, \&quot;osdb:body_data_src_url\&quot;: \&quot;http://ods-qa.openlinksw.com/DAV/home/osdb/pubs.csv\&quot;, \&quot;extractor\&quot;: \&quot;csv\&quot;, \&quot;osdb:response_format\&quot;: \&quot;application/rdf+xml\&quot;, \&quot;osdb:body_data_encoding\&quot;: \&quot;text/csv\&quot; }&#39; -H &#39;Content-Type: application/json&#39; https://osdb.openlinksw.com/osdb/api/v1/actions/csv_transformer/transform/exec&#x60;&#x60;&#x60;

### Example

```javascript
import OsdbRestApiV1 from 'osdb_rest_api_v1';

let apiInstance = new OsdbRestApiV1.OSDBApi();
let serviceId = "serviceId_example"; // String | Service ID of the service supporting the action.
let actionId = "actionId_example"; // String | Action ID of the action to execute.
let opts = {
  'execBody': {"latitude":"37.7759792","longitude":"-122.41823"} // ExecBody | Any parameters required by the action are supplied as a JSON object in the request body. The properties of this object depend on the service action being invoked.
};
apiInstance.executeAction(serviceId, actionId, opts, (error, data, response) => {
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
 **serviceId** | **String**| Service ID of the service supporting the action. | 
 **actionId** | **String**| Action ID of the action to execute. | 
 **execBody** | [**ExecBody**](ExecBody.md)| Any parameters required by the action are supplied as a JSON object in the request body. The properties of this object depend on the service action being invoked. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*, application/json


## listActions

> ListActionsResponse listActions(serviceId)

List actions

Returns an array of action descriptions for the actions supported by the given service

### Example

```javascript
import OsdbRestApiV1 from 'osdb_rest_api_v1';

let apiInstance = new OsdbRestApiV1.OSDBApi();
let serviceId = "serviceId_example"; // String | Service ID of the service for which actions are to be listed
apiInstance.listActions(serviceId, (error, data, response) => {
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
 **serviceId** | **String**| Service ID of the service for which actions are to be listed | 

### Return type

[**ListActionsResponse**](ListActionsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listServices

> ListServicesResponse listServices()

List services

Returns descriptions of all services registered with the OSDB server.

### Example

```javascript
import OsdbRestApiV1 from 'osdb_rest_api_v1';

let apiInstance = new OsdbRestApiV1.OSDBApi();
apiInstance.listServices((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**ListServicesResponse**](ListServicesResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## loadService

> LoadService200Response loadService(opts)

Load service

Loads a service description into the OSDB Service Registry

### Example

```javascript
import OsdbRestApiV1 from 'osdb_rest_api_v1';

let apiInstance = new OsdbRestApiV1.OSDBApi();
let opts = {
  'loadServiceRequest': {"service_description_url":"http://ods-qa.openlinksw.com:8896/DAV/home/nobody/csv_extractor_svc.ods-qa.170109.ttl","service_moniker":"csv_extractor"} // LoadServiceRequest | Service to register with OSDB
};
apiInstance.loadService(opts, (error, data, response) => {
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
 **loadServiceRequest** | [**LoadServiceRequest**](LoadServiceRequest.md)| Service to register with OSDB | [optional] 

### Return type

[**LoadService200Response**](LoadService200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## login

> LoginResponse login()

Login

Logs a user into the OSDB server, authenticating them by their WebID and returning an OSDB session ID in cookie osdb.sid

### Example

```javascript
import OsdbRestApiV1 from 'osdb_rest_api_v1';

let apiInstance = new OsdbRestApiV1.OSDBApi();
apiInstance.login((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**LoginResponse**](LoginResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## logout

> LogoutResponse logout()

Logout

Logs a user out of the OSDB server, ending their OSDB session

### Example

```javascript
import OsdbRestApiV1 from 'osdb_rest_api_v1';

let apiInstance = new OsdbRestApiV1.OSDBApi();
apiInstance.logout((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**LogoutResponse**](LogoutResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## unloadService

> LoadService200Response unloadService(serviceId)

Unload service

Removes a service description from the OSDB Service Registry

### Example

```javascript
import OsdbRestApiV1 from 'osdb_rest_api_v1';

let apiInstance = new OsdbRestApiV1.OSDBApi();
let serviceId = "serviceId_example"; // String | Service ID of the service to be unloaded
apiInstance.unloadService(serviceId, (error, data, response) => {
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
 **serviceId** | **String**| Service ID of the service to be unloaded | 

### Return type

[**LoadService200Response**](LoadService200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

