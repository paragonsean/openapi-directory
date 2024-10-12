# NetBoxApi.WirelessApi

All URIs are relative to *https://demo.netbox.dev/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**wirelessWirelessLanGroupsBulkDelete**](WirelessApi.md#wirelessWirelessLanGroupsBulkDelete) | **DELETE** /wireless/wireless-lan-groups/ | 
[**wirelessWirelessLanGroupsBulkPartialUpdate**](WirelessApi.md#wirelessWirelessLanGroupsBulkPartialUpdate) | **PATCH** /wireless/wireless-lan-groups/ | 
[**wirelessWirelessLanGroupsBulkUpdate**](WirelessApi.md#wirelessWirelessLanGroupsBulkUpdate) | **PUT** /wireless/wireless-lan-groups/ | 
[**wirelessWirelessLanGroupsCreate**](WirelessApi.md#wirelessWirelessLanGroupsCreate) | **POST** /wireless/wireless-lan-groups/ | 
[**wirelessWirelessLanGroupsDelete**](WirelessApi.md#wirelessWirelessLanGroupsDelete) | **DELETE** /wireless/wireless-lan-groups/{id}/ | 
[**wirelessWirelessLanGroupsList**](WirelessApi.md#wirelessWirelessLanGroupsList) | **GET** /wireless/wireless-lan-groups/ | 
[**wirelessWirelessLanGroupsPartialUpdate**](WirelessApi.md#wirelessWirelessLanGroupsPartialUpdate) | **PATCH** /wireless/wireless-lan-groups/{id}/ | 
[**wirelessWirelessLanGroupsRead**](WirelessApi.md#wirelessWirelessLanGroupsRead) | **GET** /wireless/wireless-lan-groups/{id}/ | 
[**wirelessWirelessLanGroupsUpdate**](WirelessApi.md#wirelessWirelessLanGroupsUpdate) | **PUT** /wireless/wireless-lan-groups/{id}/ | 
[**wirelessWirelessLansBulkDelete**](WirelessApi.md#wirelessWirelessLansBulkDelete) | **DELETE** /wireless/wireless-lans/ | 
[**wirelessWirelessLansBulkPartialUpdate**](WirelessApi.md#wirelessWirelessLansBulkPartialUpdate) | **PATCH** /wireless/wireless-lans/ | 
[**wirelessWirelessLansBulkUpdate**](WirelessApi.md#wirelessWirelessLansBulkUpdate) | **PUT** /wireless/wireless-lans/ | 
[**wirelessWirelessLansCreate**](WirelessApi.md#wirelessWirelessLansCreate) | **POST** /wireless/wireless-lans/ | 
[**wirelessWirelessLansDelete**](WirelessApi.md#wirelessWirelessLansDelete) | **DELETE** /wireless/wireless-lans/{id}/ | 
[**wirelessWirelessLansList**](WirelessApi.md#wirelessWirelessLansList) | **GET** /wireless/wireless-lans/ | 
[**wirelessWirelessLansPartialUpdate**](WirelessApi.md#wirelessWirelessLansPartialUpdate) | **PATCH** /wireless/wireless-lans/{id}/ | 
[**wirelessWirelessLansRead**](WirelessApi.md#wirelessWirelessLansRead) | **GET** /wireless/wireless-lans/{id}/ | 
[**wirelessWirelessLansUpdate**](WirelessApi.md#wirelessWirelessLansUpdate) | **PUT** /wireless/wireless-lans/{id}/ | 
[**wirelessWirelessLinksBulkDelete**](WirelessApi.md#wirelessWirelessLinksBulkDelete) | **DELETE** /wireless/wireless-links/ | 
[**wirelessWirelessLinksBulkPartialUpdate**](WirelessApi.md#wirelessWirelessLinksBulkPartialUpdate) | **PATCH** /wireless/wireless-links/ | 
[**wirelessWirelessLinksBulkUpdate**](WirelessApi.md#wirelessWirelessLinksBulkUpdate) | **PUT** /wireless/wireless-links/ | 
[**wirelessWirelessLinksCreate**](WirelessApi.md#wirelessWirelessLinksCreate) | **POST** /wireless/wireless-links/ | 
[**wirelessWirelessLinksDelete**](WirelessApi.md#wirelessWirelessLinksDelete) | **DELETE** /wireless/wireless-links/{id}/ | 
[**wirelessWirelessLinksList**](WirelessApi.md#wirelessWirelessLinksList) | **GET** /wireless/wireless-links/ | 
[**wirelessWirelessLinksPartialUpdate**](WirelessApi.md#wirelessWirelessLinksPartialUpdate) | **PATCH** /wireless/wireless-links/{id}/ | 
[**wirelessWirelessLinksRead**](WirelessApi.md#wirelessWirelessLinksRead) | **GET** /wireless/wireless-links/{id}/ | 
[**wirelessWirelessLinksUpdate**](WirelessApi.md#wirelessWirelessLinksUpdate) | **PUT** /wireless/wireless-links/{id}/ | 



## wirelessWirelessLanGroupsBulkDelete

> wirelessWirelessLanGroupsBulkDelete()





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.WirelessApi();
apiInstance.wirelessWirelessLanGroupsBulkDelete((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## wirelessWirelessLanGroupsBulkPartialUpdate

> WirelessLANGroup wirelessWirelessLanGroupsBulkPartialUpdate(writableWirelessLANGroup)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.WirelessApi();
let writableWirelessLANGroup = new NetBoxApi.WritableWirelessLANGroup(); // WritableWirelessLANGroup | 
apiInstance.wirelessWirelessLanGroupsBulkPartialUpdate(writableWirelessLANGroup, (error, data, response) => {
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
 **writableWirelessLANGroup** | [**WritableWirelessLANGroup**](WritableWirelessLANGroup.md)|  | 

### Return type

[**WirelessLANGroup**](WirelessLANGroup.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## wirelessWirelessLanGroupsBulkUpdate

> WirelessLANGroup wirelessWirelessLanGroupsBulkUpdate(writableWirelessLANGroup)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.WirelessApi();
let writableWirelessLANGroup = new NetBoxApi.WritableWirelessLANGroup(); // WritableWirelessLANGroup | 
apiInstance.wirelessWirelessLanGroupsBulkUpdate(writableWirelessLANGroup, (error, data, response) => {
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
 **writableWirelessLANGroup** | [**WritableWirelessLANGroup**](WritableWirelessLANGroup.md)|  | 

### Return type

[**WirelessLANGroup**](WirelessLANGroup.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## wirelessWirelessLanGroupsCreate

> WirelessLANGroup wirelessWirelessLanGroupsCreate(writableWirelessLANGroup)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.WirelessApi();
let writableWirelessLANGroup = new NetBoxApi.WritableWirelessLANGroup(); // WritableWirelessLANGroup | 
apiInstance.wirelessWirelessLanGroupsCreate(writableWirelessLANGroup, (error, data, response) => {
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
 **writableWirelessLANGroup** | [**WritableWirelessLANGroup**](WritableWirelessLANGroup.md)|  | 

### Return type

[**WirelessLANGroup**](WirelessLANGroup.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## wirelessWirelessLanGroupsDelete

> wirelessWirelessLanGroupsDelete(id)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.WirelessApi();
let id = 56; // Number | A unique integer value identifying this Wireless LAN Group.
apiInstance.wirelessWirelessLanGroupsDelete(id, (error, data, response) => {
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
 **id** | **Number**| A unique integer value identifying this Wireless LAN Group. | 

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## wirelessWirelessLanGroupsList

> WirelessWirelessLanGroupsList200Response wirelessWirelessLanGroupsList(opts)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.WirelessApi();
let opts = {
  'id': "id_example", // String | 
  'name': "name_example", // String | 
  'slug': "slug_example", // String | 
  'description': "description_example", // String | 
  'created': "created_example", // String | 
  'lastUpdated': "lastUpdated_example", // String | 
  'q': "q_example", // String | 
  'tag': "tag_example", // String | 
  'parentId': "parentId_example", // String | 
  'parent': "parent_example", // String | 
  'idN': "idN_example", // String | 
  'idLte': "idLte_example", // String | 
  'idLt': "idLt_example", // String | 
  'idGte': "idGte_example", // String | 
  'idGt': "idGt_example", // String | 
  'nameN': "nameN_example", // String | 
  'nameIc': "nameIc_example", // String | 
  'nameNic': "nameNic_example", // String | 
  'nameIew': "nameIew_example", // String | 
  'nameNiew': "nameNiew_example", // String | 
  'nameIsw': "nameIsw_example", // String | 
  'nameNisw': "nameNisw_example", // String | 
  'nameIe': "nameIe_example", // String | 
  'nameNie': "nameNie_example", // String | 
  'nameEmpty': "nameEmpty_example", // String | 
  'slugN': "slugN_example", // String | 
  'slugIc': "slugIc_example", // String | 
  'slugNic': "slugNic_example", // String | 
  'slugIew': "slugIew_example", // String | 
  'slugNiew': "slugNiew_example", // String | 
  'slugIsw': "slugIsw_example", // String | 
  'slugNisw': "slugNisw_example", // String | 
  'slugIe': "slugIe_example", // String | 
  'slugNie': "slugNie_example", // String | 
  'slugEmpty': "slugEmpty_example", // String | 
  'descriptionN': "descriptionN_example", // String | 
  'descriptionIc': "descriptionIc_example", // String | 
  'descriptionNic': "descriptionNic_example", // String | 
  'descriptionIew': "descriptionIew_example", // String | 
  'descriptionNiew': "descriptionNiew_example", // String | 
  'descriptionIsw': "descriptionIsw_example", // String | 
  'descriptionNisw': "descriptionNisw_example", // String | 
  'descriptionIe': "descriptionIe_example", // String | 
  'descriptionNie': "descriptionNie_example", // String | 
  'descriptionEmpty': "descriptionEmpty_example", // String | 
  'createdN': "createdN_example", // String | 
  'createdLte': "createdLte_example", // String | 
  'createdLt': "createdLt_example", // String | 
  'createdGte': "createdGte_example", // String | 
  'createdGt': "createdGt_example", // String | 
  'lastUpdatedN': "lastUpdatedN_example", // String | 
  'lastUpdatedLte': "lastUpdatedLte_example", // String | 
  'lastUpdatedLt': "lastUpdatedLt_example", // String | 
  'lastUpdatedGte': "lastUpdatedGte_example", // String | 
  'lastUpdatedGt': "lastUpdatedGt_example", // String | 
  'tagN': "tagN_example", // String | 
  'parentIdN': "parentIdN_example", // String | 
  'parentN': "parentN_example", // String | 
  'ordering': "ordering_example", // String | Which field to use when ordering the results.
  'limit': 56, // Number | Number of results to return per page.
  'offset': 56 // Number | The initial index from which to return the results.
};
apiInstance.wirelessWirelessLanGroupsList(opts, (error, data, response) => {
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
 **id** | **String**|  | [optional] 
 **name** | **String**|  | [optional] 
 **slug** | **String**|  | [optional] 
 **description** | **String**|  | [optional] 
 **created** | **String**|  | [optional] 
 **lastUpdated** | **String**|  | [optional] 
 **q** | **String**|  | [optional] 
 **tag** | **String**|  | [optional] 
 **parentId** | **String**|  | [optional] 
 **parent** | **String**|  | [optional] 
 **idN** | **String**|  | [optional] 
 **idLte** | **String**|  | [optional] 
 **idLt** | **String**|  | [optional] 
 **idGte** | **String**|  | [optional] 
 **idGt** | **String**|  | [optional] 
 **nameN** | **String**|  | [optional] 
 **nameIc** | **String**|  | [optional] 
 **nameNic** | **String**|  | [optional] 
 **nameIew** | **String**|  | [optional] 
 **nameNiew** | **String**|  | [optional] 
 **nameIsw** | **String**|  | [optional] 
 **nameNisw** | **String**|  | [optional] 
 **nameIe** | **String**|  | [optional] 
 **nameNie** | **String**|  | [optional] 
 **nameEmpty** | **String**|  | [optional] 
 **slugN** | **String**|  | [optional] 
 **slugIc** | **String**|  | [optional] 
 **slugNic** | **String**|  | [optional] 
 **slugIew** | **String**|  | [optional] 
 **slugNiew** | **String**|  | [optional] 
 **slugIsw** | **String**|  | [optional] 
 **slugNisw** | **String**|  | [optional] 
 **slugIe** | **String**|  | [optional] 
 **slugNie** | **String**|  | [optional] 
 **slugEmpty** | **String**|  | [optional] 
 **descriptionN** | **String**|  | [optional] 
 **descriptionIc** | **String**|  | [optional] 
 **descriptionNic** | **String**|  | [optional] 
 **descriptionIew** | **String**|  | [optional] 
 **descriptionNiew** | **String**|  | [optional] 
 **descriptionIsw** | **String**|  | [optional] 
 **descriptionNisw** | **String**|  | [optional] 
 **descriptionIe** | **String**|  | [optional] 
 **descriptionNie** | **String**|  | [optional] 
 **descriptionEmpty** | **String**|  | [optional] 
 **createdN** | **String**|  | [optional] 
 **createdLte** | **String**|  | [optional] 
 **createdLt** | **String**|  | [optional] 
 **createdGte** | **String**|  | [optional] 
 **createdGt** | **String**|  | [optional] 
 **lastUpdatedN** | **String**|  | [optional] 
 **lastUpdatedLte** | **String**|  | [optional] 
 **lastUpdatedLt** | **String**|  | [optional] 
 **lastUpdatedGte** | **String**|  | [optional] 
 **lastUpdatedGt** | **String**|  | [optional] 
 **tagN** | **String**|  | [optional] 
 **parentIdN** | **String**|  | [optional] 
 **parentN** | **String**|  | [optional] 
 **ordering** | **String**| Which field to use when ordering the results. | [optional] 
 **limit** | **Number**| Number of results to return per page. | [optional] 
 **offset** | **Number**| The initial index from which to return the results. | [optional] 

### Return type

[**WirelessWirelessLanGroupsList200Response**](WirelessWirelessLanGroupsList200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## wirelessWirelessLanGroupsPartialUpdate

> WirelessLANGroup wirelessWirelessLanGroupsPartialUpdate(id, writableWirelessLANGroup)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.WirelessApi();
let id = 56; // Number | A unique integer value identifying this Wireless LAN Group.
let writableWirelessLANGroup = new NetBoxApi.WritableWirelessLANGroup(); // WritableWirelessLANGroup | 
apiInstance.wirelessWirelessLanGroupsPartialUpdate(id, writableWirelessLANGroup, (error, data, response) => {
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
 **id** | **Number**| A unique integer value identifying this Wireless LAN Group. | 
 **writableWirelessLANGroup** | [**WritableWirelessLANGroup**](WritableWirelessLANGroup.md)|  | 

### Return type

[**WirelessLANGroup**](WirelessLANGroup.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## wirelessWirelessLanGroupsRead

> WirelessLANGroup wirelessWirelessLanGroupsRead(id)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.WirelessApi();
let id = 56; // Number | A unique integer value identifying this Wireless LAN Group.
apiInstance.wirelessWirelessLanGroupsRead(id, (error, data, response) => {
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
 **id** | **Number**| A unique integer value identifying this Wireless LAN Group. | 

### Return type

[**WirelessLANGroup**](WirelessLANGroup.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## wirelessWirelessLanGroupsUpdate

> WirelessLANGroup wirelessWirelessLanGroupsUpdate(id, writableWirelessLANGroup)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.WirelessApi();
let id = 56; // Number | A unique integer value identifying this Wireless LAN Group.
let writableWirelessLANGroup = new NetBoxApi.WritableWirelessLANGroup(); // WritableWirelessLANGroup | 
apiInstance.wirelessWirelessLanGroupsUpdate(id, writableWirelessLANGroup, (error, data, response) => {
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
 **id** | **Number**| A unique integer value identifying this Wireless LAN Group. | 
 **writableWirelessLANGroup** | [**WritableWirelessLANGroup**](WritableWirelessLANGroup.md)|  | 

### Return type

[**WirelessLANGroup**](WirelessLANGroup.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## wirelessWirelessLansBulkDelete

> wirelessWirelessLansBulkDelete()





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.WirelessApi();
apiInstance.wirelessWirelessLansBulkDelete((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## wirelessWirelessLansBulkPartialUpdate

> WirelessLAN wirelessWirelessLansBulkPartialUpdate(writableWirelessLAN)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.WirelessApi();
let writableWirelessLAN = new NetBoxApi.WritableWirelessLAN(); // WritableWirelessLAN | 
apiInstance.wirelessWirelessLansBulkPartialUpdate(writableWirelessLAN, (error, data, response) => {
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
 **writableWirelessLAN** | [**WritableWirelessLAN**](WritableWirelessLAN.md)|  | 

### Return type

[**WirelessLAN**](WirelessLAN.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## wirelessWirelessLansBulkUpdate

> WirelessLAN wirelessWirelessLansBulkUpdate(writableWirelessLAN)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.WirelessApi();
let writableWirelessLAN = new NetBoxApi.WritableWirelessLAN(); // WritableWirelessLAN | 
apiInstance.wirelessWirelessLansBulkUpdate(writableWirelessLAN, (error, data, response) => {
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
 **writableWirelessLAN** | [**WritableWirelessLAN**](WritableWirelessLAN.md)|  | 

### Return type

[**WirelessLAN**](WirelessLAN.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## wirelessWirelessLansCreate

> WirelessLAN wirelessWirelessLansCreate(writableWirelessLAN)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.WirelessApi();
let writableWirelessLAN = new NetBoxApi.WritableWirelessLAN(); // WritableWirelessLAN | 
apiInstance.wirelessWirelessLansCreate(writableWirelessLAN, (error, data, response) => {
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
 **writableWirelessLAN** | [**WritableWirelessLAN**](WritableWirelessLAN.md)|  | 

### Return type

[**WirelessLAN**](WirelessLAN.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## wirelessWirelessLansDelete

> wirelessWirelessLansDelete(id)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.WirelessApi();
let id = 56; // Number | A unique integer value identifying this Wireless LAN.
apiInstance.wirelessWirelessLansDelete(id, (error, data, response) => {
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
 **id** | **Number**| A unique integer value identifying this Wireless LAN. | 

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## wirelessWirelessLansList

> WirelessWirelessLansList200Response wirelessWirelessLansList(opts)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.WirelessApi();
let opts = {
  'id': "id_example", // String | 
  'ssid': "ssid_example", // String | 
  'authPsk': "authPsk_example", // String | 
  'description': "description_example", // String | 
  'created': "created_example", // String | 
  'lastUpdated': "lastUpdated_example", // String | 
  'q': "q_example", // String | 
  'tag': "tag_example", // String | 
  'tenantGroupId': "tenantGroupId_example", // String | 
  'tenantGroup': "tenantGroup_example", // String | 
  'tenantId': "tenantId_example", // String | 
  'tenant': "tenant_example", // String | 
  'groupId': "groupId_example", // String | 
  'group': "group_example", // String | 
  'status': "status_example", // String | 
  'vlanId': "vlanId_example", // String | 
  'authType': "authType_example", // String | 
  'authCipher': "authCipher_example", // String | 
  'idN': "idN_example", // String | 
  'idLte': "idLte_example", // String | 
  'idLt': "idLt_example", // String | 
  'idGte': "idGte_example", // String | 
  'idGt': "idGt_example", // String | 
  'ssidN': "ssidN_example", // String | 
  'ssidIc': "ssidIc_example", // String | 
  'ssidNic': "ssidNic_example", // String | 
  'ssidIew': "ssidIew_example", // String | 
  'ssidNiew': "ssidNiew_example", // String | 
  'ssidIsw': "ssidIsw_example", // String | 
  'ssidNisw': "ssidNisw_example", // String | 
  'ssidIe': "ssidIe_example", // String | 
  'ssidNie': "ssidNie_example", // String | 
  'ssidEmpty': "ssidEmpty_example", // String | 
  'authPskN': "authPskN_example", // String | 
  'authPskIc': "authPskIc_example", // String | 
  'authPskNic': "authPskNic_example", // String | 
  'authPskIew': "authPskIew_example", // String | 
  'authPskNiew': "authPskNiew_example", // String | 
  'authPskIsw': "authPskIsw_example", // String | 
  'authPskNisw': "authPskNisw_example", // String | 
  'authPskIe': "authPskIe_example", // String | 
  'authPskNie': "authPskNie_example", // String | 
  'authPskEmpty': "authPskEmpty_example", // String | 
  'descriptionN': "descriptionN_example", // String | 
  'descriptionIc': "descriptionIc_example", // String | 
  'descriptionNic': "descriptionNic_example", // String | 
  'descriptionIew': "descriptionIew_example", // String | 
  'descriptionNiew': "descriptionNiew_example", // String | 
  'descriptionIsw': "descriptionIsw_example", // String | 
  'descriptionNisw': "descriptionNisw_example", // String | 
  'descriptionIe': "descriptionIe_example", // String | 
  'descriptionNie': "descriptionNie_example", // String | 
  'descriptionEmpty': "descriptionEmpty_example", // String | 
  'createdN': "createdN_example", // String | 
  'createdLte': "createdLte_example", // String | 
  'createdLt': "createdLt_example", // String | 
  'createdGte': "createdGte_example", // String | 
  'createdGt': "createdGt_example", // String | 
  'lastUpdatedN': "lastUpdatedN_example", // String | 
  'lastUpdatedLte': "lastUpdatedLte_example", // String | 
  'lastUpdatedLt': "lastUpdatedLt_example", // String | 
  'lastUpdatedGte': "lastUpdatedGte_example", // String | 
  'lastUpdatedGt': "lastUpdatedGt_example", // String | 
  'tagN': "tagN_example", // String | 
  'tenantGroupIdN': "tenantGroupIdN_example", // String | 
  'tenantGroupN': "tenantGroupN_example", // String | 
  'tenantIdN': "tenantIdN_example", // String | 
  'tenantN': "tenantN_example", // String | 
  'groupIdN': "groupIdN_example", // String | 
  'groupN': "groupN_example", // String | 
  'statusN': "statusN_example", // String | 
  'vlanIdN': "vlanIdN_example", // String | 
  'authTypeN': "authTypeN_example", // String | 
  'authCipherN': "authCipherN_example", // String | 
  'ordering': "ordering_example", // String | Which field to use when ordering the results.
  'limit': 56, // Number | Number of results to return per page.
  'offset': 56 // Number | The initial index from which to return the results.
};
apiInstance.wirelessWirelessLansList(opts, (error, data, response) => {
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
 **id** | **String**|  | [optional] 
 **ssid** | **String**|  | [optional] 
 **authPsk** | **String**|  | [optional] 
 **description** | **String**|  | [optional] 
 **created** | **String**|  | [optional] 
 **lastUpdated** | **String**|  | [optional] 
 **q** | **String**|  | [optional] 
 **tag** | **String**|  | [optional] 
 **tenantGroupId** | **String**|  | [optional] 
 **tenantGroup** | **String**|  | [optional] 
 **tenantId** | **String**|  | [optional] 
 **tenant** | **String**|  | [optional] 
 **groupId** | **String**|  | [optional] 
 **group** | **String**|  | [optional] 
 **status** | **String**|  | [optional] 
 **vlanId** | **String**|  | [optional] 
 **authType** | **String**|  | [optional] 
 **authCipher** | **String**|  | [optional] 
 **idN** | **String**|  | [optional] 
 **idLte** | **String**|  | [optional] 
 **idLt** | **String**|  | [optional] 
 **idGte** | **String**|  | [optional] 
 **idGt** | **String**|  | [optional] 
 **ssidN** | **String**|  | [optional] 
 **ssidIc** | **String**|  | [optional] 
 **ssidNic** | **String**|  | [optional] 
 **ssidIew** | **String**|  | [optional] 
 **ssidNiew** | **String**|  | [optional] 
 **ssidIsw** | **String**|  | [optional] 
 **ssidNisw** | **String**|  | [optional] 
 **ssidIe** | **String**|  | [optional] 
 **ssidNie** | **String**|  | [optional] 
 **ssidEmpty** | **String**|  | [optional] 
 **authPskN** | **String**|  | [optional] 
 **authPskIc** | **String**|  | [optional] 
 **authPskNic** | **String**|  | [optional] 
 **authPskIew** | **String**|  | [optional] 
 **authPskNiew** | **String**|  | [optional] 
 **authPskIsw** | **String**|  | [optional] 
 **authPskNisw** | **String**|  | [optional] 
 **authPskIe** | **String**|  | [optional] 
 **authPskNie** | **String**|  | [optional] 
 **authPskEmpty** | **String**|  | [optional] 
 **descriptionN** | **String**|  | [optional] 
 **descriptionIc** | **String**|  | [optional] 
 **descriptionNic** | **String**|  | [optional] 
 **descriptionIew** | **String**|  | [optional] 
 **descriptionNiew** | **String**|  | [optional] 
 **descriptionIsw** | **String**|  | [optional] 
 **descriptionNisw** | **String**|  | [optional] 
 **descriptionIe** | **String**|  | [optional] 
 **descriptionNie** | **String**|  | [optional] 
 **descriptionEmpty** | **String**|  | [optional] 
 **createdN** | **String**|  | [optional] 
 **createdLte** | **String**|  | [optional] 
 **createdLt** | **String**|  | [optional] 
 **createdGte** | **String**|  | [optional] 
 **createdGt** | **String**|  | [optional] 
 **lastUpdatedN** | **String**|  | [optional] 
 **lastUpdatedLte** | **String**|  | [optional] 
 **lastUpdatedLt** | **String**|  | [optional] 
 **lastUpdatedGte** | **String**|  | [optional] 
 **lastUpdatedGt** | **String**|  | [optional] 
 **tagN** | **String**|  | [optional] 
 **tenantGroupIdN** | **String**|  | [optional] 
 **tenantGroupN** | **String**|  | [optional] 
 **tenantIdN** | **String**|  | [optional] 
 **tenantN** | **String**|  | [optional] 
 **groupIdN** | **String**|  | [optional] 
 **groupN** | **String**|  | [optional] 
 **statusN** | **String**|  | [optional] 
 **vlanIdN** | **String**|  | [optional] 
 **authTypeN** | **String**|  | [optional] 
 **authCipherN** | **String**|  | [optional] 
 **ordering** | **String**| Which field to use when ordering the results. | [optional] 
 **limit** | **Number**| Number of results to return per page. | [optional] 
 **offset** | **Number**| The initial index from which to return the results. | [optional] 

### Return type

[**WirelessWirelessLansList200Response**](WirelessWirelessLansList200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## wirelessWirelessLansPartialUpdate

> WirelessLAN wirelessWirelessLansPartialUpdate(id, writableWirelessLAN)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.WirelessApi();
let id = 56; // Number | A unique integer value identifying this Wireless LAN.
let writableWirelessLAN = new NetBoxApi.WritableWirelessLAN(); // WritableWirelessLAN | 
apiInstance.wirelessWirelessLansPartialUpdate(id, writableWirelessLAN, (error, data, response) => {
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
 **id** | **Number**| A unique integer value identifying this Wireless LAN. | 
 **writableWirelessLAN** | [**WritableWirelessLAN**](WritableWirelessLAN.md)|  | 

### Return type

[**WirelessLAN**](WirelessLAN.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## wirelessWirelessLansRead

> WirelessLAN wirelessWirelessLansRead(id)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.WirelessApi();
let id = 56; // Number | A unique integer value identifying this Wireless LAN.
apiInstance.wirelessWirelessLansRead(id, (error, data, response) => {
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
 **id** | **Number**| A unique integer value identifying this Wireless LAN. | 

### Return type

[**WirelessLAN**](WirelessLAN.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## wirelessWirelessLansUpdate

> WirelessLAN wirelessWirelessLansUpdate(id, writableWirelessLAN)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.WirelessApi();
let id = 56; // Number | A unique integer value identifying this Wireless LAN.
let writableWirelessLAN = new NetBoxApi.WritableWirelessLAN(); // WritableWirelessLAN | 
apiInstance.wirelessWirelessLansUpdate(id, writableWirelessLAN, (error, data, response) => {
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
 **id** | **Number**| A unique integer value identifying this Wireless LAN. | 
 **writableWirelessLAN** | [**WritableWirelessLAN**](WritableWirelessLAN.md)|  | 

### Return type

[**WirelessLAN**](WirelessLAN.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## wirelessWirelessLinksBulkDelete

> wirelessWirelessLinksBulkDelete()





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.WirelessApi();
apiInstance.wirelessWirelessLinksBulkDelete((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## wirelessWirelessLinksBulkPartialUpdate

> WirelessLink wirelessWirelessLinksBulkPartialUpdate(writableWirelessLink)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.WirelessApi();
let writableWirelessLink = new NetBoxApi.WritableWirelessLink(); // WritableWirelessLink | 
apiInstance.wirelessWirelessLinksBulkPartialUpdate(writableWirelessLink, (error, data, response) => {
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
 **writableWirelessLink** | [**WritableWirelessLink**](WritableWirelessLink.md)|  | 

### Return type

[**WirelessLink**](WirelessLink.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## wirelessWirelessLinksBulkUpdate

> WirelessLink wirelessWirelessLinksBulkUpdate(writableWirelessLink)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.WirelessApi();
let writableWirelessLink = new NetBoxApi.WritableWirelessLink(); // WritableWirelessLink | 
apiInstance.wirelessWirelessLinksBulkUpdate(writableWirelessLink, (error, data, response) => {
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
 **writableWirelessLink** | [**WritableWirelessLink**](WritableWirelessLink.md)|  | 

### Return type

[**WirelessLink**](WirelessLink.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## wirelessWirelessLinksCreate

> WirelessLink wirelessWirelessLinksCreate(writableWirelessLink)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.WirelessApi();
let writableWirelessLink = new NetBoxApi.WritableWirelessLink(); // WritableWirelessLink | 
apiInstance.wirelessWirelessLinksCreate(writableWirelessLink, (error, data, response) => {
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
 **writableWirelessLink** | [**WritableWirelessLink**](WritableWirelessLink.md)|  | 

### Return type

[**WirelessLink**](WirelessLink.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## wirelessWirelessLinksDelete

> wirelessWirelessLinksDelete(id)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.WirelessApi();
let id = 56; // Number | A unique integer value identifying this wireless link.
apiInstance.wirelessWirelessLinksDelete(id, (error, data, response) => {
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
 **id** | **Number**| A unique integer value identifying this wireless link. | 

### Return type

null (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## wirelessWirelessLinksList

> WirelessWirelessLinksList200Response wirelessWirelessLinksList(opts)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.WirelessApi();
let opts = {
  'id': "id_example", // String | 
  'ssid': "ssid_example", // String | 
  'authPsk': "authPsk_example", // String | 
  'description': "description_example", // String | 
  'created': "created_example", // String | 
  'lastUpdated': "lastUpdated_example", // String | 
  'q': "q_example", // String | 
  'tag': "tag_example", // String | 
  'tenantGroupId': "tenantGroupId_example", // String | 
  'tenantGroup': "tenantGroup_example", // String | 
  'tenantId': "tenantId_example", // String | 
  'tenant': "tenant_example", // String | 
  'interfaceAId': "interfaceAId_example", // String | 
  'interfaceBId': "interfaceBId_example", // String | 
  'status': "status_example", // String | 
  'authType': "authType_example", // String | 
  'authCipher': "authCipher_example", // String | 
  'idN': "idN_example", // String | 
  'idLte': "idLte_example", // String | 
  'idLt': "idLt_example", // String | 
  'idGte': "idGte_example", // String | 
  'idGt': "idGt_example", // String | 
  'ssidN': "ssidN_example", // String | 
  'ssidIc': "ssidIc_example", // String | 
  'ssidNic': "ssidNic_example", // String | 
  'ssidIew': "ssidIew_example", // String | 
  'ssidNiew': "ssidNiew_example", // String | 
  'ssidIsw': "ssidIsw_example", // String | 
  'ssidNisw': "ssidNisw_example", // String | 
  'ssidIe': "ssidIe_example", // String | 
  'ssidNie': "ssidNie_example", // String | 
  'ssidEmpty': "ssidEmpty_example", // String | 
  'authPskN': "authPskN_example", // String | 
  'authPskIc': "authPskIc_example", // String | 
  'authPskNic': "authPskNic_example", // String | 
  'authPskIew': "authPskIew_example", // String | 
  'authPskNiew': "authPskNiew_example", // String | 
  'authPskIsw': "authPskIsw_example", // String | 
  'authPskNisw': "authPskNisw_example", // String | 
  'authPskIe': "authPskIe_example", // String | 
  'authPskNie': "authPskNie_example", // String | 
  'authPskEmpty': "authPskEmpty_example", // String | 
  'descriptionN': "descriptionN_example", // String | 
  'descriptionIc': "descriptionIc_example", // String | 
  'descriptionNic': "descriptionNic_example", // String | 
  'descriptionIew': "descriptionIew_example", // String | 
  'descriptionNiew': "descriptionNiew_example", // String | 
  'descriptionIsw': "descriptionIsw_example", // String | 
  'descriptionNisw': "descriptionNisw_example", // String | 
  'descriptionIe': "descriptionIe_example", // String | 
  'descriptionNie': "descriptionNie_example", // String | 
  'descriptionEmpty': "descriptionEmpty_example", // String | 
  'createdN': "createdN_example", // String | 
  'createdLte': "createdLte_example", // String | 
  'createdLt': "createdLt_example", // String | 
  'createdGte': "createdGte_example", // String | 
  'createdGt': "createdGt_example", // String | 
  'lastUpdatedN': "lastUpdatedN_example", // String | 
  'lastUpdatedLte': "lastUpdatedLte_example", // String | 
  'lastUpdatedLt': "lastUpdatedLt_example", // String | 
  'lastUpdatedGte': "lastUpdatedGte_example", // String | 
  'lastUpdatedGt': "lastUpdatedGt_example", // String | 
  'tagN': "tagN_example", // String | 
  'tenantGroupIdN': "tenantGroupIdN_example", // String | 
  'tenantGroupN': "tenantGroupN_example", // String | 
  'tenantIdN': "tenantIdN_example", // String | 
  'tenantN': "tenantN_example", // String | 
  'interfaceAIdN': "interfaceAIdN_example", // String | 
  'interfaceAIdLte': "interfaceAIdLte_example", // String | 
  'interfaceAIdLt': "interfaceAIdLt_example", // String | 
  'interfaceAIdGte': "interfaceAIdGte_example", // String | 
  'interfaceAIdGt': "interfaceAIdGt_example", // String | 
  'interfaceBIdN': "interfaceBIdN_example", // String | 
  'interfaceBIdLte': "interfaceBIdLte_example", // String | 
  'interfaceBIdLt': "interfaceBIdLt_example", // String | 
  'interfaceBIdGte': "interfaceBIdGte_example", // String | 
  'interfaceBIdGt': "interfaceBIdGt_example", // String | 
  'statusN': "statusN_example", // String | 
  'authTypeN': "authTypeN_example", // String | 
  'authCipherN': "authCipherN_example", // String | 
  'ordering': "ordering_example", // String | Which field to use when ordering the results.
  'limit': 56, // Number | Number of results to return per page.
  'offset': 56 // Number | The initial index from which to return the results.
};
apiInstance.wirelessWirelessLinksList(opts, (error, data, response) => {
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
 **id** | **String**|  | [optional] 
 **ssid** | **String**|  | [optional] 
 **authPsk** | **String**|  | [optional] 
 **description** | **String**|  | [optional] 
 **created** | **String**|  | [optional] 
 **lastUpdated** | **String**|  | [optional] 
 **q** | **String**|  | [optional] 
 **tag** | **String**|  | [optional] 
 **tenantGroupId** | **String**|  | [optional] 
 **tenantGroup** | **String**|  | [optional] 
 **tenantId** | **String**|  | [optional] 
 **tenant** | **String**|  | [optional] 
 **interfaceAId** | **String**|  | [optional] 
 **interfaceBId** | **String**|  | [optional] 
 **status** | **String**|  | [optional] 
 **authType** | **String**|  | [optional] 
 **authCipher** | **String**|  | [optional] 
 **idN** | **String**|  | [optional] 
 **idLte** | **String**|  | [optional] 
 **idLt** | **String**|  | [optional] 
 **idGte** | **String**|  | [optional] 
 **idGt** | **String**|  | [optional] 
 **ssidN** | **String**|  | [optional] 
 **ssidIc** | **String**|  | [optional] 
 **ssidNic** | **String**|  | [optional] 
 **ssidIew** | **String**|  | [optional] 
 **ssidNiew** | **String**|  | [optional] 
 **ssidIsw** | **String**|  | [optional] 
 **ssidNisw** | **String**|  | [optional] 
 **ssidIe** | **String**|  | [optional] 
 **ssidNie** | **String**|  | [optional] 
 **ssidEmpty** | **String**|  | [optional] 
 **authPskN** | **String**|  | [optional] 
 **authPskIc** | **String**|  | [optional] 
 **authPskNic** | **String**|  | [optional] 
 **authPskIew** | **String**|  | [optional] 
 **authPskNiew** | **String**|  | [optional] 
 **authPskIsw** | **String**|  | [optional] 
 **authPskNisw** | **String**|  | [optional] 
 **authPskIe** | **String**|  | [optional] 
 **authPskNie** | **String**|  | [optional] 
 **authPskEmpty** | **String**|  | [optional] 
 **descriptionN** | **String**|  | [optional] 
 **descriptionIc** | **String**|  | [optional] 
 **descriptionNic** | **String**|  | [optional] 
 **descriptionIew** | **String**|  | [optional] 
 **descriptionNiew** | **String**|  | [optional] 
 **descriptionIsw** | **String**|  | [optional] 
 **descriptionNisw** | **String**|  | [optional] 
 **descriptionIe** | **String**|  | [optional] 
 **descriptionNie** | **String**|  | [optional] 
 **descriptionEmpty** | **String**|  | [optional] 
 **createdN** | **String**|  | [optional] 
 **createdLte** | **String**|  | [optional] 
 **createdLt** | **String**|  | [optional] 
 **createdGte** | **String**|  | [optional] 
 **createdGt** | **String**|  | [optional] 
 **lastUpdatedN** | **String**|  | [optional] 
 **lastUpdatedLte** | **String**|  | [optional] 
 **lastUpdatedLt** | **String**|  | [optional] 
 **lastUpdatedGte** | **String**|  | [optional] 
 **lastUpdatedGt** | **String**|  | [optional] 
 **tagN** | **String**|  | [optional] 
 **tenantGroupIdN** | **String**|  | [optional] 
 **tenantGroupN** | **String**|  | [optional] 
 **tenantIdN** | **String**|  | [optional] 
 **tenantN** | **String**|  | [optional] 
 **interfaceAIdN** | **String**|  | [optional] 
 **interfaceAIdLte** | **String**|  | [optional] 
 **interfaceAIdLt** | **String**|  | [optional] 
 **interfaceAIdGte** | **String**|  | [optional] 
 **interfaceAIdGt** | **String**|  | [optional] 
 **interfaceBIdN** | **String**|  | [optional] 
 **interfaceBIdLte** | **String**|  | [optional] 
 **interfaceBIdLt** | **String**|  | [optional] 
 **interfaceBIdGte** | **String**|  | [optional] 
 **interfaceBIdGt** | **String**|  | [optional] 
 **statusN** | **String**|  | [optional] 
 **authTypeN** | **String**|  | [optional] 
 **authCipherN** | **String**|  | [optional] 
 **ordering** | **String**| Which field to use when ordering the results. | [optional] 
 **limit** | **Number**| Number of results to return per page. | [optional] 
 **offset** | **Number**| The initial index from which to return the results. | [optional] 

### Return type

[**WirelessWirelessLinksList200Response**](WirelessWirelessLinksList200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## wirelessWirelessLinksPartialUpdate

> WirelessLink wirelessWirelessLinksPartialUpdate(id, writableWirelessLink)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.WirelessApi();
let id = 56; // Number | A unique integer value identifying this wireless link.
let writableWirelessLink = new NetBoxApi.WritableWirelessLink(); // WritableWirelessLink | 
apiInstance.wirelessWirelessLinksPartialUpdate(id, writableWirelessLink, (error, data, response) => {
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
 **id** | **Number**| A unique integer value identifying this wireless link. | 
 **writableWirelessLink** | [**WritableWirelessLink**](WritableWirelessLink.md)|  | 

### Return type

[**WirelessLink**](WirelessLink.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## wirelessWirelessLinksRead

> WirelessLink wirelessWirelessLinksRead(id)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.WirelessApi();
let id = 56; // Number | A unique integer value identifying this wireless link.
apiInstance.wirelessWirelessLinksRead(id, (error, data, response) => {
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
 **id** | **Number**| A unique integer value identifying this wireless link. | 

### Return type

[**WirelessLink**](WirelessLink.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## wirelessWirelessLinksUpdate

> WirelessLink wirelessWirelessLinksUpdate(id, writableWirelessLink)





### Example

```javascript
import NetBoxApi from 'net_box_api';
let defaultClient = NetBoxApi.ApiClient.instance;
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new NetBoxApi.WirelessApi();
let id = 56; // Number | A unique integer value identifying this wireless link.
let writableWirelessLink = new NetBoxApi.WritableWirelessLink(); // WritableWirelessLink | 
apiInstance.wirelessWirelessLinksUpdate(id, writableWirelessLink, (error, data, response) => {
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
 **id** | **Number**| A unique integer value identifying this wireless link. | 
 **writableWirelessLink** | [**WritableWirelessLink**](WritableWirelessLink.md)|  | 

### Return type

[**WirelessLink**](WirelessLink.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

