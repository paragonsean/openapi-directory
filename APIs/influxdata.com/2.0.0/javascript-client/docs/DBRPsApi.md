# InfluxOssApiService.DBRPsApi

All URIs are relative to */api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteDBRPID**](DBRPsApi.md#deleteDBRPID) | **DELETE** /dbrps/{dbrpID} | Delete a database retention policy
[**getDBRPs**](DBRPsApi.md#getDBRPs) | **GET** /dbrps | List all database retention policy mappings
[**getDBRPsID**](DBRPsApi.md#getDBRPsID) | **GET** /dbrps/{dbrpID} | Retrieve a database retention policy mapping
[**patchDBRPID**](DBRPsApi.md#patchDBRPID) | **PATCH** /dbrps/{dbrpID} | Update a database retention policy mapping
[**postDBRP**](DBRPsApi.md#postDBRP) | **POST** /dbrps | Add a database retention policy mapping



## deleteDBRPID

> deleteDBRPID(orgID, dbrpID, opts)

Delete a database retention policy

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.DBRPsApi();
let orgID = "orgID_example"; // String | Specifies the organization ID of the mapping
let dbrpID = "dbrpID_example"; // String | The database retention policy mapping
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}" // String | OpenTracing span context
};
apiInstance.deleteDBRPID(orgID, dbrpID, opts, (error, data, response) => {
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
 **orgID** | **String**| Specifies the organization ID of the mapping | 
 **dbrpID** | **String**| The database retention policy mapping | 
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDBRPs

> DBRPs getDBRPs(orgID, opts)

List all database retention policy mappings

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.DBRPsApi();
let orgID = "orgID_example"; // String | Specifies the organization ID to filter on
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}", // String | OpenTracing span context
  'id': "id_example", // String | Specifies the mapping ID to filter on
  'bucketID': "bucketID_example", // String | Specifies the bucket ID to filter on
  '_default': true, // Boolean | Specifies filtering on default
  'db': "db_example", // String | Specifies the database to filter on
  'rp': "rp_example" // String | Specifies the retention policy to filter on
};
apiInstance.getDBRPs(orgID, opts, (error, data, response) => {
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
 **orgID** | **String**| Specifies the organization ID to filter on | 
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 
 **id** | **String**| Specifies the mapping ID to filter on | [optional] 
 **bucketID** | **String**| Specifies the bucket ID to filter on | [optional] 
 **_default** | **Boolean**| Specifies filtering on default | [optional] 
 **db** | **String**| Specifies the database to filter on | [optional] 
 **rp** | **String**| Specifies the retention policy to filter on | [optional] 

### Return type

[**DBRPs**](DBRPs.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDBRPsID

> DBRP getDBRPsID(orgID, dbrpID, opts)

Retrieve a database retention policy mapping

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.DBRPsApi();
let orgID = "orgID_example"; // String | Specifies the organization ID of the mapping
let dbrpID = "dbrpID_example"; // String | The database retention policy mapping ID
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}" // String | OpenTracing span context
};
apiInstance.getDBRPsID(orgID, dbrpID, opts, (error, data, response) => {
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
 **orgID** | **String**| Specifies the organization ID of the mapping | 
 **dbrpID** | **String**| The database retention policy mapping ID | 
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 

### Return type

[**DBRP**](DBRP.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## patchDBRPID

> DBRP patchDBRPID(orgID, dbrpID, dBRPUpdate, opts)

Update a database retention policy mapping

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.DBRPsApi();
let orgID = "orgID_example"; // String | Specifies the organization ID of the mapping
let dbrpID = "dbrpID_example"; // String | The database retention policy mapping.
let dBRPUpdate = new InfluxOssApiService.DBRPUpdate(); // DBRPUpdate | Database retention policy update to apply
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}" // String | OpenTracing span context
};
apiInstance.patchDBRPID(orgID, dbrpID, dBRPUpdate, opts, (error, data, response) => {
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
 **orgID** | **String**| Specifies the organization ID of the mapping | 
 **dbrpID** | **String**| The database retention policy mapping. | 
 **dBRPUpdate** | [**DBRPUpdate**](DBRPUpdate.md)| Database retention policy update to apply | 
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 

### Return type

[**DBRP**](DBRP.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postDBRP

> DBRP postDBRP(DBRP, opts)

Add a database retention policy mapping

### Example

```javascript
import InfluxOssApiService from 'influx_oss_api_service';

let apiInstance = new InfluxOssApiService.DBRPsApi();
let DBRP = new InfluxOssApiService.DBRP(); // DBRP | The database retention policy mapping to add
let opts = {
  'zapTraceSpan': "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}" // String | OpenTracing span context
};
apiInstance.postDBRP(DBRP, opts, (error, data, response) => {
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
 **DBRP** | [**DBRP**](DBRP.md)| The database retention policy mapping to add | 
 **zapTraceSpan** | **String**| OpenTracing span context | [optional] 

### Return type

[**DBRP**](DBRP.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

