# ThreatJammerComUserApi.DenylistDataQueryAndManagementApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**changeStatusOfTheDenylistV1DenylistPublicDenylistIdPut**](DenylistDataQueryAndManagementApi.md#changeStatusOfTheDenylistV1DenylistPublicDenylistIdPut) | **PUT** /v1/denylist/public/{denylist_id} | Toogle the status of an deny list.
[**changeStatusOfTheOriginDenylistV1DenylistPrivateDenylistIdOriginPut**](DenylistDataQueryAndManagementApi.md#changeStatusOfTheOriginDenylistV1DenylistPrivateDenylistIdOriginPut) | **PUT** /v1/denylist/private/{denylist_id}/origin | Toogle the status of the origin in a deny list.
[**changeStatusOfTheOriginDenylistV1DenylistPublicDenylistIdOriginPut**](DenylistDataQueryAndManagementApi.md#changeStatusOfTheOriginDenylistV1DenylistPublicDenylistIdOriginPut) | **PUT** /v1/denylist/public/{denylist_id}/origin | Toogle the status of the origin in a deny list.
[**createPrivateDenylistOfTheUserV1DenylistPrivatePost**](DenylistDataQueryAndManagementApi.md#createPrivateDenylistOfTheUserV1DenylistPrivatePost) | **POST** /v1/denylist/private | Creates a new private denylist binded to the user.
[**deleteAllIpAddressesReportedByTheUserV1DenylistReportedIpAllDelete**](DenylistDataQueryAndManagementApi.md#deleteAllIpAddressesReportedByTheUserV1DenylistReportedIpAllDelete) | **DELETE** /v1/denylist/reported/ip/all | Delete all the automatically reported IP addresses by the user.
[**deleteAnIpAddressReportedByTheUserV1DenylistReportedIpIpAddressDelete**](DenylistDataQueryAndManagementApi.md#deleteAnIpAddressReportedByTheUserV1DenylistReportedIpIpAddressDelete) | **DELETE** /v1/denylist/reported/ip/{ip_address} | Delete the automatically reported IP address by the user.
[**deleteTheDenylistContentV1DenylistPrivateDenylistIdContentDelete**](DenylistDataQueryAndManagementApi.md#deleteTheDenylistContentV1DenylistPrivateDenylistIdContentDelete) | **DELETE** /v1/denylist/private/{denylist_id}/content | Delete all the content of a private denylist of the user.
[**deleteTheDenylistV1DenylistPrivateDenylistIdDelete**](DenylistDataQueryAndManagementApi.md#deleteTheDenylistV1DenylistPrivateDenylistIdDelete) | **DELETE** /v1/denylist/private/{denylist_id} | Delete all the bindings between a user and a private denylist.
[**deleteTheDenylistV1DenylistPublicDenylistIdDelete**](DenylistDataQueryAndManagementApi.md#deleteTheDenylistV1DenylistPublicDenylistIdDelete) | **DELETE** /v1/denylist/public/{denylist_id} | Delete all the bindings between a user and an denylist.
[**getAllOwnedDenylistsByResourceTypeV1DenylistPublicOwnedResourceTypeGet**](DenylistDataQueryAndManagementApi.md#getAllOwnedDenylistsByResourceTypeV1DenylistPublicOwnedResourceTypeGet) | **GET** /v1/denylist/public/owned/{resource_type} | Get the set of public denylists of a user by resource type.
[**getAllPrivateDenylistsByResourceTypeV1DenylistPrivateAllResourceTypeGet**](DenylistDataQueryAndManagementApi.md#getAllPrivateDenylistsByResourceTypeV1DenylistPrivateAllResourceTypeGet) | **GET** /v1/denylist/private/all/{resource_type} | Get the set of private denylists of the user by resource type.
[**getAllPrivateDenylistsV1DenylistPrivateAllGet**](DenylistDataQueryAndManagementApi.md#getAllPrivateDenylistsV1DenylistPrivateAllGet) | **GET** /v1/denylist/private/all | Get the set of private denylists of the user.
[**getAllPublicDenylistsByResourceTypeV1DenylistPublicAllResourceTypeGet**](DenylistDataQueryAndManagementApi.md#getAllPublicDenylistsByResourceTypeV1DenylistPublicAllResourceTypeGet) | **GET** /v1/denylist/public/all/{resource_type} | Get the set of public denylists by resource type.
[**getAllPublicDenylistsV1DenylistPublicAllGet**](DenylistDataQueryAndManagementApi.md#getAllPublicDenylistsV1DenylistPublicAllGet) | **GET** /v1/denylist/public/all | Get the set of public denylists.
[**getDenylistContentV1DenylistPrivateDenylistIdContentGet**](DenylistDataQueryAndManagementApi.md#getDenylistContentV1DenylistPrivateDenylistIdContentGet) | **GET** /v1/denylist/private/{denylist_id}/content | Get the content of a private denylist of the user.
[**getPublicDenylistsOwnedByTheUserV1DenylistPublicOwnedGet**](DenylistDataQueryAndManagementApi.md#getPublicDenylistsOwnedByTheUserV1DenylistPublicOwnedGet) | **GET** /v1/denylist/public/owned | Get the set of owned denylists.
[**getSingleDenylistV1DenylistPrivateDenylistIdGet**](DenylistDataQueryAndManagementApi.md#getSingleDenylistV1DenylistPrivateDenylistIdGet) | **GET** /v1/denylist/private/{denylist_id} | Get the details of a specific private denylist of the user.
[**getSingleDenylistV1DenylistPublicDenylistIdGet**](DenylistDataQueryAndManagementApi.md#getSingleDenylistV1DenylistPublicDenylistIdGet) | **GET** /v1/denylist/public/{denylist_id} | Get the details of the denylist.
[**queryAllTheIpAddressesReportedByTheUserV1DenylistReportedIpGet**](DenylistDataQueryAndManagementApi.md#queryAllTheIpAddressesReportedByTheUserV1DenylistReportedIpGet) | **GET** /v1/denylist/reported/ip | Get the list of automatically reported IP addresses by the user.
[**queryAnIpAddressesReportedByTheUserV1DenylistReportedIpIpAddressGet**](DenylistDataQueryAndManagementApi.md#queryAnIpAddressesReportedByTheUserV1DenylistReportedIpIpAddressGet) | **GET** /v1/denylist/reported/ip/{ip_address} | Get the details of an automatically reported IP addresses by the user.
[**queryResourceDenylistsV1DenylistPrivateIpAddressGet**](DenylistDataQueryAndManagementApi.md#queryResourceDenylistsV1DenylistPrivateIpAddressGet) | **GET** /v1/denylist/private/ip/{address} | Get the different denylists where the IP address was found.
[**queryResourceDenylistsV1DenylistPublicIpAddressGet**](DenylistDataQueryAndManagementApi.md#queryResourceDenylistsV1DenylistPublicIpAddressGet) | **GET** /v1/denylist/public/ip/{address} | Get the different public denylists where the IP address was found.
[**updatePrivateContentOfTheDenylistOfTheUserV1DenylistPrivateDenylistIdContentPut**](DenylistDataQueryAndManagementApi.md#updatePrivateContentOfTheDenylistOfTheUserV1DenylistPrivateDenylistIdContentPut) | **PUT** /v1/denylist/private/{denylist_id}/content | Add or remove content of a private denylist of the user.
[**updatePrivateDenylistOfTheUserV1DenylistPrivateDenylistIdPut**](DenylistDataQueryAndManagementApi.md#updatePrivateDenylistOfTheUserV1DenylistPrivateDenylistIdPut) | **PUT** /v1/denylist/private/{denylist_id} | Update the information of an existing private denylist of the user.



## changeStatusOfTheDenylistV1DenylistPublicDenylistIdPut

> Object changeStatusOfTheDenylistV1DenylistPublicDenylistIdPut(denylistId, bodyChangeStatusOfTheDenylistV1DenylistPublicDenylistIdPut)

Toogle the status of an deny list.

### What Change the status of an deny list to &#x60;&#x60;ACTIVE&#x60;&#x60; or &#x60;&#x60;INACTIVE&#x60;&#x60;. An &#x60;&#x60;INACTIVE&#x60;&#x60; list will not be used by the service. An &#x60;&#x60;ACTIVE&#x60;&#x60; list will be used by the service. As an optional parameter it can be provided an &#x60;&#x60;expiry&#x60;&#x60; date in seconds since epoch. If not provided, the list will never expire.   This is an asynchronous operation. It can take several seconds until the operation completes, but the request will  immediately return a 202 Accepted response.  ### Parameters In the query string the ID of the deny list to change the status. In the body the JSON object with the following fields: - &#x60;&#x60;status&#x60;&#x60;: The status of the list. It can be &#x60;&#x60;ACTIVE&#x60;&#x60; or &#x60;&#x60;INACTIVE&#x60;&#x60;. - &#x60;&#x60;expiry&#x60;&#x60;: Unix timestamp in seconds when the list will expire. If it does not exist, it will never expire.  ### Result It should always return a 202 Accepted response with an empty body.  ### Errors  If the list does not exist, it will return a 404 error. If the status is not &#x60;&#x60;ACTIVE&#x60;&#x60; or &#x60;&#x60;INACTIVE&#x60;&#x60;, it will return a 422 error. If the expiry is not a valid timestamp, it will return a 422 error. If the deny list is not a valid UUID, it will return a 422 error.  It will return the API Global errors described in the API description.

### Example

```javascript
import ThreatJammerComUserApi from 'threat_jammer_com_user_api';
let defaultClient = ThreatJammerComUserApi.ApiClient.instance;
// Configure Bearer access token for authorization: HTTPBearer
let HTTPBearer = defaultClient.authentications['HTTPBearer'];
HTTPBearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new ThreatJammerComUserApi.DenylistDataQueryAndManagementApi();
let denylistId = "denylistId_example"; // String | 
let bodyChangeStatusOfTheDenylistV1DenylistPublicDenylistIdPut = new ThreatJammerComUserApi.BodyChangeStatusOfTheDenylistV1DenylistPublicDenylistIdPut(); // BodyChangeStatusOfTheDenylistV1DenylistPublicDenylistIdPut | 
apiInstance.changeStatusOfTheDenylistV1DenylistPublicDenylistIdPut(denylistId, bodyChangeStatusOfTheDenylistV1DenylistPublicDenylistIdPut, (error, data, response) => {
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
 **denylistId** | **String**|  | 
 **bodyChangeStatusOfTheDenylistV1DenylistPublicDenylistIdPut** | [**BodyChangeStatusOfTheDenylistV1DenylistPublicDenylistIdPut**](BodyChangeStatusOfTheDenylistV1DenylistPublicDenylistIdPut.md)|  | 

### Return type

**Object**

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## changeStatusOfTheOriginDenylistV1DenylistPrivateDenylistIdOriginPut

> Object changeStatusOfTheOriginDenylistV1DenylistPrivateDenylistIdOriginPut(denylistId, bodyChangeStatusOfTheOriginDenylistV1DenylistPrivateDenylistIdOriginPut)

Toogle the status of the origin in a deny list.

### What Change the status of the origin of a deny list to &#x60;&#x60;ACTIVE&#x60;&#x60;, &#x60;&#x60;INACTIVE&#x60;&#x60; or &#x60;&#x60;DELETED&#x60;&#x60;.  An &#x60;&#x60;ACTIVE&#x60;&#x60; origin will apply the deny list to the protocol and domain of the origin. An origin can be created and activated simply toogling the &#x60;&#x60;ACTIVE&#x60;&#x60; status. As an optional parameter it can be provided an &#x60;&#x60;ttl&#x60;&#x60; or Time To Live parameter of the origin in the list in seconds. After the TTL expires, the origin will be removed from the list.  If the TTL is not provided, the origin will never expire.  An &#x60;&#x60;INACTIVE&#x60;&#x60; origin will not apply the deny list to the protocol and domain of the origin.  A &#x60;&#x60;DELETED&#x60;&#x60; origin will be removed from the list. It will not be used by the service anymore. The user can activate it again with the &#x60;&#x60;ACTIVE&#x60;&#x60; status.  This is an asynchronous operation. It can take several seconds until the operation completes, but the request will  immediately return a 202 Accepted response.  *This operation is not available in the Freemium plan.*  ### Parameters In the query string the ID of the deny list to change the status. In the body the JSON object with the following fields: - &#x60;&#x60;origin&#x60;&#x60;: The protocol and domain of the origin. It can be &#x60;&#x60;http://example.com&#x60;&#x60; or &#x60;&#x60;https://example.com&#x60;&#x60;. - &#x60;&#x60;status&#x60;&#x60;: The status of the list. It can be &#x60;&#x60;ACTIVE&#x60;&#x60;, &#x60;&#x60;INACTIVE&#x60;&#x60; or &#x60;&#x60;DELETED&#x60;&#x60;.  ### Result It should always return a 202 Accepted response with an empty body.  ### Errors  If the list does not exist, it will return a 404 error. If the status is not &#x60;&#x60;ACTIVE&#x60;&#x60; or &#x60;&#x60;INACTIVE&#x60;&#x60;, it will return a 422 error. If the TTL is negative in the past, it will return a 422 error. If the deny list is not a valid UUID, it will return a 422 error. If the origin is not a valid URL, it will return a 400 error. If the denylist is not active, it will returna 409 error. If the origin is not found in the set owned by the user, it will return a 404 error.  It will return the API Global errors described in the API description.

### Example

```javascript
import ThreatJammerComUserApi from 'threat_jammer_com_user_api';
let defaultClient = ThreatJammerComUserApi.ApiClient.instance;
// Configure Bearer access token for authorization: HTTPBearer
let HTTPBearer = defaultClient.authentications['HTTPBearer'];
HTTPBearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new ThreatJammerComUserApi.DenylistDataQueryAndManagementApi();
let denylistId = "denylistId_example"; // String | 
let bodyChangeStatusOfTheOriginDenylistV1DenylistPrivateDenylistIdOriginPut = new ThreatJammerComUserApi.BodyChangeStatusOfTheOriginDenylistV1DenylistPrivateDenylistIdOriginPut(); // BodyChangeStatusOfTheOriginDenylistV1DenylistPrivateDenylistIdOriginPut | 
apiInstance.changeStatusOfTheOriginDenylistV1DenylistPrivateDenylistIdOriginPut(denylistId, bodyChangeStatusOfTheOriginDenylistV1DenylistPrivateDenylistIdOriginPut, (error, data, response) => {
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
 **denylistId** | **String**|  | 
 **bodyChangeStatusOfTheOriginDenylistV1DenylistPrivateDenylistIdOriginPut** | [**BodyChangeStatusOfTheOriginDenylistV1DenylistPrivateDenylistIdOriginPut**](BodyChangeStatusOfTheOriginDenylistV1DenylistPrivateDenylistIdOriginPut.md)|  | 

### Return type

**Object**

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## changeStatusOfTheOriginDenylistV1DenylistPublicDenylistIdOriginPut

> Object changeStatusOfTheOriginDenylistV1DenylistPublicDenylistIdOriginPut(denylistId, bodyChangeStatusOfTheOriginDenylistV1DenylistPublicDenylistIdOriginPut)

Toogle the status of the origin in a deny list.

### What Change the status of the origin of a deny list to &#x60;&#x60;ACTIVE&#x60;&#x60;, &#x60;&#x60;INACTIVE&#x60;&#x60; or &#x60;&#x60;DELETED&#x60;&#x60;.  An &#x60;&#x60;ACTIVE&#x60;&#x60; origin will apply the deny list to the protocol and domain of the origin. An origin can be created and activated simply toogling the &#x60;&#x60;ACTIVE&#x60;&#x60; status. As an optional parameter it can be provided an &#x60;&#x60;ttl&#x60;&#x60; or Time To Live parameter of the origin in the list in seconds. After the TTL expires, the origin will be removed from the list.  If the TTL is not provided, the origin will never expire.  An &#x60;&#x60;INACTIVE&#x60;&#x60; origin will not apply the deny list to the protocol and domain of the origin.  A &#x60;&#x60;DELETED&#x60;&#x60; origin will be removed from the list. It will not be used by the service anymore. The user can activate it again with the &#x60;&#x60;ACTIVE&#x60;&#x60; status.  This is an asynchronous operation. It can take several seconds until the operation completes, but the request will  immediately return a 202 Accepted response.  *This operation is not available in the Freemium plan.*  ### Parameters In the query string the ID of the deny list to change the status. In the body the JSON object with the following fields: - &#x60;&#x60;origin&#x60;&#x60;: The protocol and domain of the origin. It can be &#x60;&#x60;http://example.com&#x60;&#x60; or &#x60;&#x60;https://example.com&#x60;&#x60;. - &#x60;&#x60;status&#x60;&#x60;: The status of the list. It can be &#x60;&#x60;ACTIVE&#x60;&#x60;, &#x60;&#x60;INACTIVE&#x60;&#x60; or &#x60;&#x60;DELETED&#x60;&#x60;.  ### Result It should always return a 202 Accepted response with an empty body.  ### Errors  If the list does not exist, it will return a 404 error. If the status is not &#x60;&#x60;ACTIVE&#x60;&#x60; or &#x60;&#x60;INACTIVE&#x60;&#x60;, it will return a 422 error. If the TTL is negative in the past, it will return a 422 error. If the deny list is not a valid UUID, it will return a 422 error. If the origin is not a valid URL, it will return a 400 error. If the denylist is not active, it will returna 409 error. If the origin is not found in the set owned by the user, it will return a 404 error.  It will return the API Global errors described in the API description.

### Example

```javascript
import ThreatJammerComUserApi from 'threat_jammer_com_user_api';
let defaultClient = ThreatJammerComUserApi.ApiClient.instance;
// Configure Bearer access token for authorization: HTTPBearer
let HTTPBearer = defaultClient.authentications['HTTPBearer'];
HTTPBearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new ThreatJammerComUserApi.DenylistDataQueryAndManagementApi();
let denylistId = "denylistId_example"; // String | 
let bodyChangeStatusOfTheOriginDenylistV1DenylistPublicDenylistIdOriginPut = new ThreatJammerComUserApi.BodyChangeStatusOfTheOriginDenylistV1DenylistPublicDenylistIdOriginPut(); // BodyChangeStatusOfTheOriginDenylistV1DenylistPublicDenylistIdOriginPut | 
apiInstance.changeStatusOfTheOriginDenylistV1DenylistPublicDenylistIdOriginPut(denylistId, bodyChangeStatusOfTheOriginDenylistV1DenylistPublicDenylistIdOriginPut, (error, data, response) => {
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
 **denylistId** | **String**|  | 
 **bodyChangeStatusOfTheOriginDenylistV1DenylistPublicDenylistIdOriginPut** | [**BodyChangeStatusOfTheOriginDenylistV1DenylistPublicDenylistIdOriginPut**](BodyChangeStatusOfTheOriginDenylistV1DenylistPublicDenylistIdOriginPut.md)|  | 

### Return type

**Object**

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createPrivateDenylistOfTheUserV1DenylistPrivatePost

> String createPrivateDenylistOfTheUserV1DenylistPrivatePost(bodyCreatePrivateDenylistOfTheUserV1DenylistPrivatePost)

Creates a new private denylist binded to the user.

### What Creates a new denylist with the information given and binded to the current user. The parameters are:  - name  - description  - tags  - expiry  - Time to Live (TTL)  - Resource Type (&#x60;CIDR&#x60;, &#x60;AS&#x60;, &#x60;COUNTRY&#x60;, &#x60;CONTINENT&#x60;, &#x60;DATACENTER_ID&#x60; and &#x60;USER AGENT&#x60;)  This is an asynchronous operation. It can take several seconds until the operation completes, but the request will immediately return a 202 Accepted response. The operation will also return the UUID of the list.  ### Parameters In the query string the ID of the private deny list to delete.  In the body the following parameters: - &#x60;&#x60;name&#x60;&#x60;: A human readable name of the list. - &#x60;&#x60;description&#x60;&#x60;: A long detailed information about what the list contains and how it is used. - &#x60;&#x60;tags&#x60;&#x60;: A list of tags that describe the list. - &#x60;&#x60;ttl&#x60;&#x60;: (Optional) The Time To Live of the list, in seconds. If it does not exist, it will never expire. - &#x60;&#x60;resource_type&#x60;&#x60;: The type of resource that the list contains. It can be &#x60;&#x60;CIDR&#x60;&#x60;, &#x60;&#x60;AS&#x60;&#x60;, &#x60;&#x60;COUNTRY&#x60;&#x60;, &#x60;&#x60;CONTINENT&#x60;&#x60;,    &#x60;&#x60;DATACENTER_ID&#x60;&#x60; or &#x60;&#x60;USER AGENT&#x60;&#x60;.  ### Result It should always return a 202 Accepted response with the UUID of the new list in the body.  ### Errors  - If the information is not valid, it will return a &#x60;422&#x60; (Unprocessable Entity) error. - If the ttl is negative, it will return a &#x60;400&#x60; (Bad Request) error.  It will return the API Global errors described in the API description.

### Example

```javascript
import ThreatJammerComUserApi from 'threat_jammer_com_user_api';
let defaultClient = ThreatJammerComUserApi.ApiClient.instance;
// Configure Bearer access token for authorization: HTTPBearer
let HTTPBearer = defaultClient.authentications['HTTPBearer'];
HTTPBearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new ThreatJammerComUserApi.DenylistDataQueryAndManagementApi();
let bodyCreatePrivateDenylistOfTheUserV1DenylistPrivatePost = new ThreatJammerComUserApi.BodyCreatePrivateDenylistOfTheUserV1DenylistPrivatePost(); // BodyCreatePrivateDenylistOfTheUserV1DenylistPrivatePost | 
apiInstance.createPrivateDenylistOfTheUserV1DenylistPrivatePost(bodyCreatePrivateDenylistOfTheUserV1DenylistPrivatePost, (error, data, response) => {
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
 **bodyCreatePrivateDenylistOfTheUserV1DenylistPrivatePost** | [**BodyCreatePrivateDenylistOfTheUserV1DenylistPrivatePost**](BodyCreatePrivateDenylistOfTheUserV1DenylistPrivatePost.md)|  | 

### Return type

**String**

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteAllIpAddressesReportedByTheUserV1DenylistReportedIpAllDelete

> Object deleteAllIpAddressesReportedByTheUserV1DenylistReportedIpAllDelete()

Delete all the automatically reported IP addresses by the user.

### What Delete all the IP addresses that have been automatically reported by the user. This option cannot be reverted.  ### Parameters No parameters are required.  ### Result A successful result is an empty response with the the HTTP status code &#x60;&#x60;204 No Content&#x60;&#x60;.  ### Errors It will return the API Global errors described in the API description.

### Example

```javascript
import ThreatJammerComUserApi from 'threat_jammer_com_user_api';
let defaultClient = ThreatJammerComUserApi.ApiClient.instance;
// Configure Bearer access token for authorization: HTTPBearer
let HTTPBearer = defaultClient.authentications['HTTPBearer'];
HTTPBearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new ThreatJammerComUserApi.DenylistDataQueryAndManagementApi();
apiInstance.deleteAllIpAddressesReportedByTheUserV1DenylistReportedIpAllDelete((error, data, response) => {
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

**Object**

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteAnIpAddressReportedByTheUserV1DenylistReportedIpIpAddressDelete

> Object deleteAnIpAddressReportedByTheUserV1DenylistReportedIpIpAddressDelete(ipAddress)

Delete the automatically reported IP address by the user.

### What Delete an IP address that was automatically reported by the user. This option cannot be reverted.  ### Parameters The endpoint accepts the following parameters in the path: - &#x60;&#x60;ip_address&#x60;&#x60;: (Mandatory) The public IPv4 or IPv6 addresses to be deleted.  ### Result A successful result is an empty response with the the HTTP status code &#x60;&#x60;204 No Content&#x60;&#x60;.  ### Errors - a &#x60;422 Unprocessable Entity&#x60; error if the IP address is malformed.  It will also return the API Global errors described in the API description.

### Example

```javascript
import ThreatJammerComUserApi from 'threat_jammer_com_user_api';
let defaultClient = ThreatJammerComUserApi.ApiClient.instance;
// Configure Bearer access token for authorization: HTTPBearer
let HTTPBearer = defaultClient.authentications['HTTPBearer'];
HTTPBearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new ThreatJammerComUserApi.DenylistDataQueryAndManagementApi();
let ipAddress = "ipAddress_example"; // String | 
apiInstance.deleteAnIpAddressReportedByTheUserV1DenylistReportedIpIpAddressDelete(ipAddress, (error, data, response) => {
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
 **ipAddress** | **String**|  | 

### Return type

**Object**

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteTheDenylistContentV1DenylistPrivateDenylistIdContentDelete

> Object deleteTheDenylistContentV1DenylistPrivateDenylistIdContentDelete(denylistId)

Delete all the content of a private denylist of the user.

### What Delete all the content of a private denylist of the user. This will remove all the elements, and there is no way to recover them.  ### Parameters Pass the private denylist ID as query parameter.  ### Result If successful, it will return a &#x60;&#x60;202&#x60;&#x60; (Accepted) response with an empty body. The operation is asynchronous,and can take several seconds to complete.  ### Errors  - If the deny list is not a valid UUID, it will return a &#x60;&#x60;422&#x60;&#x60; (Unprocessable Entity) error. - If the private denylist ID does not exist, it will return a &#x60;&#x60;404&#x60;&#x60; (Not found) error.  It will also return the API Global errors described in the API description.

### Example

```javascript
import ThreatJammerComUserApi from 'threat_jammer_com_user_api';
let defaultClient = ThreatJammerComUserApi.ApiClient.instance;
// Configure Bearer access token for authorization: HTTPBearer
let HTTPBearer = defaultClient.authentications['HTTPBearer'];
HTTPBearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new ThreatJammerComUserApi.DenylistDataQueryAndManagementApi();
let denylistId = "denylistId_example"; // String | 
apiInstance.deleteTheDenylistContentV1DenylistPrivateDenylistIdContentDelete(denylistId, (error, data, response) => {
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
 **denylistId** | **String**|  | 

### Return type

**Object**

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteTheDenylistV1DenylistPrivateDenylistIdDelete

> Object deleteTheDenylistV1DenylistPrivateDenylistIdDelete(denylistId)

Delete all the bindings between a user and a private denylist.

### What Delete all the bindings between a user and a private denylist. This will remove the content of the denylist, the denylist from the user and also all the origins that are using the denylist.  This is an asynchronous operation. It can take several seconds until the operation completes, but the request willimmediately return a 202 Accepted response.  The default lists &#x60;&#x60;External sources reported CIDRs&#x60;&#x60; and &#x60;&#x60;Default denylist&#x60;&#x60; cannot be deleted, but can be emptied. Please refer to the documentation to delete the content.  ### Parameters In the query string the ID of the private deny list to delete.  ### Result It should always return a 202 Accepted response with an empty body.  ### Errors  - If the list does not exist, it will return a &#x60;404&#x60; (Not found) error. - If the list is a default list, it will return a &#x60;403&#x60; (Forbidden) error. - If the deny list is not a valid UUID, it will return a &#x60;422&#x60; (Unprocessable Entity) error.  It will return the API Global errors described in the API description.

### Example

```javascript
import ThreatJammerComUserApi from 'threat_jammer_com_user_api';
let defaultClient = ThreatJammerComUserApi.ApiClient.instance;
// Configure Bearer access token for authorization: HTTPBearer
let HTTPBearer = defaultClient.authentications['HTTPBearer'];
HTTPBearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new ThreatJammerComUserApi.DenylistDataQueryAndManagementApi();
let denylistId = "denylistId_example"; // String | 
apiInstance.deleteTheDenylistV1DenylistPrivateDenylistIdDelete(denylistId, (error, data, response) => {
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
 **denylistId** | **String**|  | 

### Return type

**Object**

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteTheDenylistV1DenylistPublicDenylistIdDelete

> Object deleteTheDenylistV1DenylistPublicDenylistIdDelete(denylistId)

Delete all the bindings between a user and an denylist.

### What Delete all the bindings between a user and an denylist. This will remove the denylist from the user and also all the origins that are using the denylist.   This is an asynchronous operation. It can take several seconds until the operation completes, but the request will  immediately return a 202 Accepted response.  ### Parameters In the query string the ID of the deny list to change the status.  ### Result It should always return a 202 Accepted response with an empty body.  ### Errors  If the list does not exist, it will return a 404 error. If the deny list is not a valid UUID, it will return a 422 error.  It will return the API Global errors described in the API description.

### Example

```javascript
import ThreatJammerComUserApi from 'threat_jammer_com_user_api';
let defaultClient = ThreatJammerComUserApi.ApiClient.instance;
// Configure Bearer access token for authorization: HTTPBearer
let HTTPBearer = defaultClient.authentications['HTTPBearer'];
HTTPBearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new ThreatJammerComUserApi.DenylistDataQueryAndManagementApi();
let denylistId = "denylistId_example"; // String | 
apiInstance.deleteTheDenylistV1DenylistPublicDenylistIdDelete(denylistId, (error, data, response) => {
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
 **denylistId** | **String**|  | 

### Return type

**Object**

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getAllOwnedDenylistsByResourceTypeV1DenylistPublicOwnedResourceTypeGet

> PublicAclGroupListCollectionOutput getAllOwnedDenylistsByResourceTypeV1DenylistPublicOwnedResourceTypeGet(resourceType)

Get the set of public denylists of a user by resource type.

### What Obtain the set of public deny lists selected by the user and wich ones are not filtering by the resource type.  ### Parameters The &#x60;&#x60;resource type&#x60;&#x60; to filter. The values can be &#x60;&#x60;CIDR&#x60;&#x60;, &#x60;&#x60;AS&#x60;&#x60;, &#x60;&#x60;COUNTRY&#x60;&#x60;, &#x60;&#x60;CONTINENT&#x60;&#x60; or &#x60;&#x60;DATACENTER_ID&#x60;&#x60;.  ### Result The result is a JSON object with a list of the following JSON objects: - &#x60;&#x60;self&#x60;&#x60;: the URI to the status of all the lists. - &#x60;&#x60;lists&#x60;&#x60;: a list of JSON objects with the available lists:     - &#x60;&#x60;self&#x60;&#x60;: the URI to individual information of the list.     - &#x60;&#x60;name&#x60;&#x60;: A human readable name of the list.     - &#x60;&#x60;description&#x60;&#x60;: A long detailed information about what the list contains and how it is used.     - &#x60;&#x60;resource_type&#x60;&#x60;: The type of the list. It can be &#x60;&#x60;CIDR&#x60;&#x60;, &#x60;&#x60;AS&#x60;&#x60;, &#x60;&#x60;COUNTRY&#x60;&#x60;, &#x60;&#x60;CONTINENT&#x60;&#x60; or &#x60;&#x60;DATACENTER_ID&#x60;&#x60;.     - &#x60;&#x60;list_type&#x60;&#x60;: The type of the list. It can be &#x60;&#x60;ALLOW&#x60;&#x60; or &#x60;&#x60;DENY&#x60;&#x60;.     - &#x60;&#x60;status&#x60;&#x60;: The status of the list. It can be &#x60;&#x60;ACTIVE&#x60;&#x60; or &#x60;&#x60;INACTIVE&#x60;&#x60; or &#x60;&#x60;EXPIRED&#x60;&#x60;. If the list is &#x60;&#x60;EXPIRED&#x60;&#x60;    it means that the list is not available anymore if not renewed.     - &#x60;&#x60;created_at&#x60;&#x60;: Unix timestamp in seconds when the list was created.     - &#x60;&#x60;updated_at&#x60;&#x60;: Unix timestamp in seconds when the list was updated.     - &#x60;&#x60;expiry&#x60;&#x60;: Unix timestamp in seconds when the list will expire. If it does not exist, it will never expire.     - &#x60;&#x60;origins&#x60;&#x60;: list of websites that are using the list as an denylist.         - &#x60;&#x60;self&#x60;&#x60;: the URI to all the list of origins.         - &#x60;&#x60;lists&#x60;&#x60;: list of lists that the origin is using.             - &#x60;&#x60;self&#x60;&#x60;: the URI to the individual information of the list.             - &#x60;&#x60;origin&#x60;&#x60;: the protocol and domain of the website that is using the list.             - &#x60;&#x60;status&#x60;&#x60;: the status of the list. It can be &#x60;&#x60;ACTIVE&#x60;&#x60; or &#x60;&#x60;INACTIVE&#x60;&#x60; or &#x60;&#x60;EXPIRED&#x60;&#x60;. If the list is &#x60;&#x60;EXPIRED&#x60;&#x60;            it means that the list is not available anymore if not renewed.             - &#x60;&#x60;expiry&#x60;&#x60;: Unix timestamp in seconds when the list will expire. If it does not exist, it will never expire.             - &#x60;&#x60;created_at&#x60;&#x60;: Unix timestamp in seconds when the list was created.             - &#x60;&#x60;updated_at&#x60;&#x60;: Unix timestamp in seconds when the list was updated.  ### Errors  It will return the API Global errors described in the API description.

### Example

```javascript
import ThreatJammerComUserApi from 'threat_jammer_com_user_api';
let defaultClient = ThreatJammerComUserApi.ApiClient.instance;
// Configure Bearer access token for authorization: HTTPBearer
let HTTPBearer = defaultClient.authentications['HTTPBearer'];
HTTPBearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new ThreatJammerComUserApi.DenylistDataQueryAndManagementApi();
let resourceType = "resourceType_example"; // String | 
apiInstance.getAllOwnedDenylistsByResourceTypeV1DenylistPublicOwnedResourceTypeGet(resourceType, (error, data, response) => {
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
 **resourceType** | **String**|  | 

### Return type

[**PublicAclGroupListCollectionOutput**](PublicAclGroupListCollectionOutput.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getAllPrivateDenylistsByResourceTypeV1DenylistPrivateAllResourceTypeGet

> PrivateAclGroupListCollectionOutput getAllPrivateDenylistsByResourceTypeV1DenylistPrivateAllResourceTypeGet(resourceType)

Get the set of private denylists of the user by resource type.

### What Obtain the set of private deny lists of the user available in the service filtering by resource type. It can be &#x60;&#x60;CIDR&#x60;&#x60;, &#x60;&#x60;AS&#x60;&#x60;, &#x60;&#x60;COUNTRY&#x60;&#x60;, &#x60;&#x60;CONTINENT&#x60;&#x60; or &#x60;&#x60;DATACENTER_ID&#x60;&#x60;   These lists are different datasets: - Lists that are part of the automatically reported data from the Report IP, focused on honeypots and automaticreporting from external sources. The name is &#x60;External sources reported CIDRs&#x60;. The resource type is &#x60;&#x60;CIDR&#x60;&#x60;. - Lists that are part of the automatically denylisted by the Threat Jammer service. The name is &#x60;Default denylist&#x60;. The resource type is &#x60;&#x60;CIDR&#x60;&#x60;. - Lists that are created by the user.  ### Parameters The &#x60;&#x60;resource type&#x60;&#x60; to filter. The values can be &#x60;&#x60;CIDR&#x60;&#x60;, &#x60;&#x60;AS&#x60;&#x60;, &#x60;&#x60;COUNTRY&#x60;&#x60;, &#x60;&#x60;CONTINENT&#x60;&#x60; or &#x60;&#x60;DATACENTER_ID&#x60;&#x60;.  ### Result The result is a JSON object with a list of the following JSON objects: - &#x60;&#x60;self&#x60;&#x60;: the URI to the status of all the lists. - &#x60;&#x60;lists&#x60;&#x60;: a list of JSON objects with the available lists:     - &#x60;&#x60;self&#x60;&#x60;: the URI to individual information of the list.     - &#x60;&#x60;name&#x60;&#x60;: A human readable name of the list.     - &#x60;&#x60;description&#x60;&#x60;: A long detailed information about what the list contains and how it is used.     - &#x60;&#x60;resource_type&#x60;&#x60;: The type of the list. It can be &#x60;&#x60;CIDR&#x60;&#x60;, &#x60;&#x60;AS&#x60;&#x60;, &#x60;&#x60;COUNTRY&#x60;&#x60;, &#x60;&#x60;CONTINENT&#x60;&#x60; or &#x60;&#x60;DATACENTER_ID&#x60;&#x60;.     - &#x60;&#x60;list_type&#x60;&#x60;: The type of the list. It can be &#x60;&#x60;ALLOW&#x60;&#x60; or &#x60;&#x60;DENY&#x60;&#x60;.     - &#x60;&#x60;created_at&#x60;&#x60;: Unix timestamp in seconds when the list was created.     - &#x60;&#x60;updated_at&#x60;&#x60;: Unix timestamp in seconds when the list was updated.     - &#x60;&#x60;expiry&#x60;&#x60;: Unix timestamp in seconds when the list will expire. If it does not exist, it will never expire.     - &#x60;&#x60;origins&#x60;&#x60;: list of websites that are using the list as a denylist.         - &#x60;&#x60;self&#x60;&#x60;: the URI to all the list of origins.         - &#x60;&#x60;lists&#x60;&#x60;: list of lists that the origin is using.             - &#x60;&#x60;self&#x60;&#x60;: the URI to the individual information of the list.             - &#x60;&#x60;origin&#x60;&#x60;: the protocol and domain of the website that is using the list.             - &#x60;&#x60;status&#x60;&#x60;: the status of the list. It can be &#x60;&#x60;ACTIVE&#x60;&#x60; or &#x60;&#x60;INACTIVE&#x60;&#x60; or &#x60;&#x60;EXPIRED&#x60;&#x60;. If the list is &#x60;&#x60;EXPIRED&#x60;&#x60; it means that the list is not available anymore if not renewed.             - &#x60;&#x60;expiry&#x60;&#x60;: Unix timestamp in seconds when the list will expire. If it does not exist, it will never expire.             - &#x60;&#x60;created_at&#x60;&#x60;: Unix timestamp in seconds when the list was created.             - &#x60;&#x60;updated_at&#x60;&#x60;: Unix timestamp in seconds when the list was updated.  ### Errors  - If the resource type is not valid, it will return a &#x60;&#x60;422&#x60;&#x60; (Unprocessable Entity) error.  It will also return the API Global errors described in the API description.

### Example

```javascript
import ThreatJammerComUserApi from 'threat_jammer_com_user_api';
let defaultClient = ThreatJammerComUserApi.ApiClient.instance;
// Configure Bearer access token for authorization: HTTPBearer
let HTTPBearer = defaultClient.authentications['HTTPBearer'];
HTTPBearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new ThreatJammerComUserApi.DenylistDataQueryAndManagementApi();
let resourceType = "resourceType_example"; // String | 
apiInstance.getAllPrivateDenylistsByResourceTypeV1DenylistPrivateAllResourceTypeGet(resourceType, (error, data, response) => {
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
 **resourceType** | **String**|  | 

### Return type

[**PrivateAclGroupListCollectionOutput**](PrivateAclGroupListCollectionOutput.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getAllPrivateDenylistsV1DenylistPrivateAllGet

> PrivateAclGroupListCollectionOutput getAllPrivateDenylistsV1DenylistPrivateAllGet()

Get the set of private denylists of the user.

### What Obtain the set of private deny lists of the user available in the service. These lists are different datasets: - Lists that are part of the automatically reported data from the Report IP, focused on honeypots and automaticreporting from external sources. The name is &#x60;External sources reported CIDRs&#x60;. - Lists that are part of the automatically denylisted by the Threat Jammer service. The name is &#x60;Default denylist&#x60;. - Lists that are created by the user.  ### Parameters No parameters  ### Result The result is a JSON object with a list of the following JSON objects: - &#x60;&#x60;self&#x60;&#x60;: the URI to the status of all the lists. - &#x60;&#x60;lists&#x60;&#x60;: a list of JSON objects with the available lists:     - &#x60;&#x60;self&#x60;&#x60;: the URI to individual information of the list.     - &#x60;&#x60;name&#x60;&#x60;: A human readable name of the list.     - &#x60;&#x60;description&#x60;&#x60;: A long detailed information about what the list contains and how it is used.     - &#x60;&#x60;resource_type&#x60;&#x60;: The type of the list. It can be &#x60;&#x60;CIDR&#x60;&#x60;, &#x60;&#x60;AS&#x60;&#x60;, &#x60;&#x60;COUNTRY&#x60;&#x60;, &#x60;&#x60;CONTINENT&#x60;&#x60; or &#x60;&#x60;DATACENTER_ID&#x60;&#x60;.     - &#x60;&#x60;list_type&#x60;&#x60;: The type of the list. It can be &#x60;&#x60;ALLOW&#x60;&#x60; or &#x60;&#x60;DENY&#x60;&#x60;.     - &#x60;&#x60;created_at&#x60;&#x60;: Unix timestamp in seconds when the list was created.     - &#x60;&#x60;updated_at&#x60;&#x60;: Unix timestamp in seconds when the list was updated.     - &#x60;&#x60;expiry&#x60;&#x60;: Unix timestamp in seconds when the list will expire. If it does not exist, it will never expire.     - &#x60;&#x60;origins&#x60;&#x60;: list of websites that are using the list as a denylist.         - &#x60;&#x60;self&#x60;&#x60;: the URI to all the list of origins.         - &#x60;&#x60;lists&#x60;&#x60;: list of lists that the origin is using.             - &#x60;&#x60;self&#x60;&#x60;: the URI to the individual information of the list.             - &#x60;&#x60;origin&#x60;&#x60;: the protocol and domain of the website that is using the list.             - &#x60;&#x60;status&#x60;&#x60;: the status of the list. It can be &#x60;&#x60;ACTIVE&#x60;&#x60; or &#x60;&#x60;INACTIVE&#x60;&#x60; or &#x60;&#x60;EXPIRED&#x60;&#x60;. If the list is &#x60;&#x60;EXPIRED&#x60;&#x60; it means that the list is not available anymore if not renewed.             - &#x60;&#x60;expiry&#x60;&#x60;: Unix timestamp in seconds when the list will expire. If it does not exist, it will never expire.             - &#x60;&#x60;created_at&#x60;&#x60;: Unix timestamp in seconds when the list was created.             - &#x60;&#x60;updated_at&#x60;&#x60;: Unix timestamp in seconds when the list was updated.  ### Errors  It will return the API Global errors described in the API description.

### Example

```javascript
import ThreatJammerComUserApi from 'threat_jammer_com_user_api';
let defaultClient = ThreatJammerComUserApi.ApiClient.instance;
// Configure Bearer access token for authorization: HTTPBearer
let HTTPBearer = defaultClient.authentications['HTTPBearer'];
HTTPBearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new ThreatJammerComUserApi.DenylistDataQueryAndManagementApi();
apiInstance.getAllPrivateDenylistsV1DenylistPrivateAllGet((error, data, response) => {
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

[**PrivateAclGroupListCollectionOutput**](PrivateAclGroupListCollectionOutput.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getAllPublicDenylistsByResourceTypeV1DenylistPublicAllResourceTypeGet

> PublicAclGroupListCollectionOutput getAllPublicDenylistsByResourceTypeV1DenylistPublicAllResourceTypeGet(resourceType)

Get the set of public denylists by resource type.

### What Obtain the set of public deny lists available in the service and also which ones are already selected by the user and wich ones are not filtering by the resource type.  ### Parameters The &#x60;&#x60;resource type&#x60;&#x60; to filter. The values can be &#x60;&#x60;CIDR&#x60;&#x60;, &#x60;&#x60;AS&#x60;&#x60;, &#x60;&#x60;COUNTRY&#x60;&#x60;, &#x60;&#x60;CONTINENT&#x60;&#x60; or &#x60;&#x60;DATACENTER_ID&#x60;&#x60;.  ### Result The result is a JSON object with a list of the following JSON objects: - &#x60;&#x60;self&#x60;&#x60;: the URI to the status of all the lists. - &#x60;&#x60;lists&#x60;&#x60;: a list of JSON objects with the available lists:     - &#x60;&#x60;self&#x60;&#x60;: the URI to individual information of the list.     - &#x60;&#x60;name&#x60;&#x60;: A human readable name of the list.     - &#x60;&#x60;description&#x60;&#x60;: A long detailed information about what the list contains and how it is used.     - &#x60;&#x60;resource_type&#x60;&#x60;: The type of the list. It can be &#x60;&#x60;CIDR&#x60;&#x60;, &#x60;&#x60;AS&#x60;&#x60;, &#x60;&#x60;COUNTRY&#x60;&#x60;, &#x60;&#x60;CONTINENT&#x60;&#x60; or &#x60;&#x60;DATACENTER_ID&#x60;&#x60;.     - &#x60;&#x60;list_type&#x60;&#x60;: The type of the list. It can be &#x60;&#x60;ALLOW&#x60;&#x60; or &#x60;&#x60;DENY&#x60;&#x60;.     - &#x60;&#x60;status&#x60;&#x60;: The status of the list. It can be &#x60;&#x60;ACTIVE&#x60;&#x60; or &#x60;&#x60;INACTIVE&#x60;&#x60; or &#x60;&#x60;EXPIRED&#x60;&#x60;. If the list is &#x60;&#x60;EXPIRED&#x60;&#x60;    it means that the list is not available anymore if not renewed.     - &#x60;&#x60;created_at&#x60;&#x60;: Unix timestamp in seconds when the list was created.     - &#x60;&#x60;updated_at&#x60;&#x60;: Unix timestamp in seconds when the list was updated.  If the list is already selected by the user, the JSON object will also contain the following fields: - &#x60;&#x60;expiry&#x60;&#x60;: Unix timestamp in seconds when the list will expire. If it does not exist, it will never expire. - &#x60;&#x60;origins&#x60;&#x60;: list of websites that are using the list as an denylist.     - &#x60;&#x60;self&#x60;&#x60;: the URI to all the list of origins.     - &#x60;&#x60;lists&#x60;&#x60;: list of lists that the origin is using.         - &#x60;&#x60;self&#x60;&#x60;: the URI to the individual information of the list.         - &#x60;&#x60;origin&#x60;&#x60;: the protocol and domain of the website that is using the list.         - &#x60;&#x60;status&#x60;&#x60;: the status of the list. It can be &#x60;&#x60;ACTIVE&#x60;&#x60; or &#x60;&#x60;INACTIVE&#x60;&#x60; or &#x60;&#x60;EXPIRED&#x60;&#x60;. If the list is &#x60;&#x60;EXPIRED&#x60;&#x60;        it means that the list is not available anymore if not renewed.         - &#x60;&#x60;expiry&#x60;&#x60;: Unix timestamp in seconds when the list will expire. If it does not exist, it will never expire.         - &#x60;&#x60;created_at&#x60;&#x60;: Unix timestamp in seconds when the list was created.         - &#x60;&#x60;updated_at&#x60;&#x60;: Unix timestamp in seconds when the list was updated.  ### Errors  It will return the API Global errors described in the API description.

### Example

```javascript
import ThreatJammerComUserApi from 'threat_jammer_com_user_api';
let defaultClient = ThreatJammerComUserApi.ApiClient.instance;
// Configure Bearer access token for authorization: HTTPBearer
let HTTPBearer = defaultClient.authentications['HTTPBearer'];
HTTPBearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new ThreatJammerComUserApi.DenylistDataQueryAndManagementApi();
let resourceType = "resourceType_example"; // String | 
apiInstance.getAllPublicDenylistsByResourceTypeV1DenylistPublicAllResourceTypeGet(resourceType, (error, data, response) => {
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
 **resourceType** | **String**|  | 

### Return type

[**PublicAclGroupListCollectionOutput**](PublicAclGroupListCollectionOutput.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getAllPublicDenylistsV1DenylistPublicAllGet

> PublicAclGroupListCollectionOutput getAllPublicDenylistsV1DenylistPublicAllGet()

Get the set of public denylists.

### What Obtain the set of public deny lists available in the service and also which ones are already selected by the user and wich ones are not.  ### Parameters No parameters  ### Result The result is a JSON object with a list of the following JSON objects: - &#x60;&#x60;self&#x60;&#x60;: the URI to the status of all the lists. - &#x60;&#x60;lists&#x60;&#x60;: a list of JSON objects with the available lists:     - &#x60;&#x60;self&#x60;&#x60;: the URI to individual information of the list.     - &#x60;&#x60;name&#x60;&#x60;: A human readable name of the list.     - &#x60;&#x60;description&#x60;&#x60;: A long detailed information about what the list contains and how it is used.     - &#x60;&#x60;resource_type&#x60;&#x60;: The type of the list. It can be &#x60;&#x60;CIDR&#x60;&#x60;, &#x60;&#x60;AS&#x60;&#x60;, &#x60;&#x60;COUNTRY&#x60;&#x60;, &#x60;&#x60;CONTINENT&#x60;&#x60; or &#x60;&#x60;DATACENTER_ID&#x60;&#x60;.     - &#x60;&#x60;list_type&#x60;&#x60;: The type of the list. It can be &#x60;&#x60;ALLOW&#x60;&#x60; or &#x60;&#x60;DENY&#x60;&#x60;.     - &#x60;&#x60;status&#x60;&#x60;: The status of the list. It can be &#x60;&#x60;ACTIVE&#x60;&#x60; or &#x60;&#x60;INACTIVE&#x60;&#x60; or &#x60;&#x60;EXPIRED&#x60;&#x60;. If the list is &#x60;&#x60;EXPIRED&#x60;&#x60;    it means that the list is not available anymore if not renewed.     - &#x60;&#x60;created_at&#x60;&#x60;: Unix timestamp in seconds when the list was created.     - &#x60;&#x60;updated_at&#x60;&#x60;: Unix timestamp in seconds when the list was updated.  If the list is already selected by the user, the JSON object will also contain the following fields: - &#x60;&#x60;expiry&#x60;&#x60;: Unix timestamp in seconds when the list will expire. If it does not exist, it will never expire. - &#x60;&#x60;origins&#x60;&#x60;: list of websites that are using the list as an denylist.     - &#x60;&#x60;self&#x60;&#x60;: the URI to all the list of origins.     - &#x60;&#x60;lists&#x60;&#x60;: list of lists that the origin is using.         - &#x60;&#x60;self&#x60;&#x60;: the URI to the individual information of the list.         - &#x60;&#x60;origin&#x60;&#x60;: the protocol and domain of the website that is using the list.         - &#x60;&#x60;status&#x60;&#x60;: the status of the list. It can be &#x60;&#x60;ACTIVE&#x60;&#x60; or &#x60;&#x60;INACTIVE&#x60;&#x60; or &#x60;&#x60;EXPIRED&#x60;&#x60;. If the list is &#x60;&#x60;EXPIRED&#x60;&#x60;        it means that the list is not available anymore if not renewed.         - &#x60;&#x60;expiry&#x60;&#x60;: Unix timestamp in seconds when the list will expire. If it does not exist, it will never expire.         - &#x60;&#x60;created_at&#x60;&#x60;: Unix timestamp in seconds when the list was created.         - &#x60;&#x60;updated_at&#x60;&#x60;: Unix timestamp in seconds when the list was updated.  ### Errors  It will return the API Global errors described in the API description.

### Example

```javascript
import ThreatJammerComUserApi from 'threat_jammer_com_user_api';
let defaultClient = ThreatJammerComUserApi.ApiClient.instance;
// Configure Bearer access token for authorization: HTTPBearer
let HTTPBearer = defaultClient.authentications['HTTPBearer'];
HTTPBearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new ThreatJammerComUserApi.DenylistDataQueryAndManagementApi();
apiInstance.getAllPublicDenylistsV1DenylistPublicAllGet((error, data, response) => {
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

[**PublicAclGroupListCollectionOutput**](PublicAclGroupListCollectionOutput.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDenylistContentV1DenylistPrivateDenylistIdContentGet

> PrivateAclListCollectionOutput getDenylistContentV1DenylistPrivateDenylistIdContentGet(denylistId, opts)

Get the content of a private denylist of the user.

### What Returns the content of the private denylist of the user. The content can be CIDRs, ASNs, countries, continents or    datacenter IDs.  ### Parameters Pass the private denylist ID as query parameter.  The following pagination parameters are required as query string parameters: - &#x60;&#x60;page&#x60;&#x60;: (Optional) the page number to retrieve. The first page is 1. Default is 1. - &#x60;&#x60;page_size&#x60;&#x60;: (Optional) the number of items per page. Default is 20.   ### Result The result is a JSON object with the following structure: - &#x60;&#x60;self&#x60;&#x60;: the URI to the content of the list. - &#x60;&#x60;cidrs&#x60;&#x60;: (Optional) list of CIDRs in the list. - &#x60;&#x60;asns&#x60;&#x60;: (Optional) list of ASNs in the list. - &#x60;&#x60;countries&#x60;&#x60;: (Optional) list of countries in the list. - &#x60;&#x60;continents&#x60;&#x60;: (Optional) list of continents in the list. - &#x60;&#x60;datacenters&#x60;&#x60;: (Optional) list of datacenters in the list.  ### Errors  - If the deny list is not a valid UUID, it will return a &#x60;&#x60;422&#x60;&#x60; (Unprocessable Entity) error. - If the private denylist ID does not exist, it will return a &#x60;&#x60;404&#x60;&#x60; (Not found) error.  It will also return the API Global errors described in the API description.

### Example

```javascript
import ThreatJammerComUserApi from 'threat_jammer_com_user_api';
let defaultClient = ThreatJammerComUserApi.ApiClient.instance;
// Configure Bearer access token for authorization: HTTPBearer
let HTTPBearer = defaultClient.authentications['HTTPBearer'];
HTTPBearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new ThreatJammerComUserApi.DenylistDataQueryAndManagementApi();
let denylistId = "denylistId_example"; // String | 
let opts = {
  'page': 1, // Number | The page to be returned
  'pageSize': 20 // Number | The number of items per page
};
apiInstance.getDenylistContentV1DenylistPrivateDenylistIdContentGet(denylistId, opts, (error, data, response) => {
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
 **denylistId** | **String**|  | 
 **page** | **Number**| The page to be returned | [optional] [default to 1]
 **pageSize** | **Number**| The number of items per page | [optional] [default to 20]

### Return type

[**PrivateAclListCollectionOutput**](PrivateAclListCollectionOutput.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPublicDenylistsOwnedByTheUserV1DenylistPublicOwnedGet

> PublicAclGroupListCollectionOutput getPublicDenylistsOwnedByTheUserV1DenylistPublicOwnedGet()

Get the set of owned denylists.

### What Obtain the set of public deny lists available in the service selected by the user.  ### Parameters No parameters  ### Result The result is a JSON object with a list of the following JSON objects: - &#x60;&#x60;self&#x60;&#x60;: the URI to the status of all the lists. - &#x60;&#x60;lists&#x60;&#x60;: a list of JSON objects with the available lists:     - &#x60;&#x60;self&#x60;&#x60;: the URI to individual information of the list.     - &#x60;&#x60;name&#x60;&#x60;: A human readable name of the list.     - &#x60;&#x60;description&#x60;&#x60;: A long detailed information about what the list contains and how it is used.     - &#x60;&#x60;resource_type&#x60;&#x60;: The type of the list. It can be &#x60;&#x60;CIDR&#x60;&#x60;, &#x60;&#x60;AS&#x60;&#x60;, &#x60;&#x60;COUNTRY&#x60;&#x60;, &#x60;&#x60;CONTINENT&#x60;&#x60; or &#x60;&#x60;DATACENTER_ID&#x60;&#x60;.     - &#x60;&#x60;list_type&#x60;&#x60;: The type of the list. It can be &#x60;&#x60;ALLOW&#x60;&#x60; or &#x60;&#x60;DENY&#x60;&#x60;.     - &#x60;&#x60;status&#x60;&#x60;: The status of the list. It can be &#x60;&#x60;ACTIVE&#x60;&#x60; or &#x60;&#x60;INACTIVE&#x60;&#x60; or &#x60;&#x60;EXPIRED&#x60;&#x60;. If the list is &#x60;&#x60;EXPIRED&#x60;&#x60;    it means that the list is not available anymore if not renewed.     - &#x60;&#x60;created_at&#x60;&#x60;: Unix timestamp in seconds when the list was created.     - &#x60;&#x60;updated_at&#x60;&#x60;: Unix timestamp in seconds when the list was updated.     - &#x60;&#x60;expiry&#x60;&#x60;: Unix timestamp in seconds when the list will expire. If it does not exist, it will never expire.     - &#x60;&#x60;origins&#x60;&#x60;: list of websites that are using the list as an denylist.         - &#x60;&#x60;self&#x60;&#x60;: the URI to all the list of origins.         - &#x60;&#x60;lists&#x60;&#x60;: list of lists that the origin is using.             - &#x60;&#x60;self&#x60;&#x60;: the URI to the individual information of the list.             - &#x60;&#x60;origin&#x60;&#x60;: the protocol and domain of the website that is using the list.             - &#x60;&#x60;status&#x60;&#x60;: the status of the list. It can be &#x60;&#x60;ACTIVE&#x60;&#x60; or &#x60;&#x60;INACTIVE&#x60;&#x60; or &#x60;&#x60;EXPIRED&#x60;&#x60;. If the list is &#x60;&#x60;EXPIRED&#x60;&#x60;            it means that the list is not available anymore if not renewed.             - &#x60;&#x60;expiry&#x60;&#x60;: Unix timestamp in seconds when the list will expire. If it does not exist, it will never expire.             - &#x60;&#x60;created_at&#x60;&#x60;: Unix timestamp in seconds when the list was created.             - &#x60;&#x60;updated_at&#x60;&#x60;: Unix timestamp in seconds when the list was updated.  ### Errors  It will return the API Global errors described in the API description.

### Example

```javascript
import ThreatJammerComUserApi from 'threat_jammer_com_user_api';
let defaultClient = ThreatJammerComUserApi.ApiClient.instance;
// Configure Bearer access token for authorization: HTTPBearer
let HTTPBearer = defaultClient.authentications['HTTPBearer'];
HTTPBearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new ThreatJammerComUserApi.DenylistDataQueryAndManagementApi();
apiInstance.getPublicDenylistsOwnedByTheUserV1DenylistPublicOwnedGet((error, data, response) => {
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

[**PublicAclGroupListCollectionOutput**](PublicAclGroupListCollectionOutput.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSingleDenylistV1DenylistPrivateDenylistIdGet

> PrivateAclGroupListOutput getSingleDenylistV1DenylistPrivateDenylistIdGet(denylistId)

Get the details of a specific private denylist of the user.

### What Obtain the details of the private deny list of the user available in the service.  ### Parameters Pass the private denylist ID as query parameter.  ### Result The result is a JSON object with the following structure: - &#x60;&#x60;self&#x60;&#x60;: the URI to individual information of the list. - &#x60;&#x60;name&#x60;&#x60;: A human readable name of the list. - &#x60;&#x60;description&#x60;&#x60;: A long detailed information about what the list contains and how it is used. - &#x60;&#x60;resource_type&#x60;&#x60;: The type of the list. It can be &#x60;&#x60;CIDR&#x60;&#x60;, &#x60;&#x60;AS&#x60;&#x60;, &#x60;&#x60;COUNTRY&#x60;&#x60;, &#x60;&#x60;CONTINENT&#x60;&#x60; or &#x60;&#x60;DATACENTER_ID&#x60;&#x60;. - &#x60;&#x60;list_type&#x60;&#x60;: The type of the list. It can be &#x60;&#x60;ALLOW&#x60;&#x60; or &#x60;&#x60;DENY&#x60;&#x60;. - &#x60;&#x60;created_at&#x60;&#x60;: Unix timestamp in seconds when the list was created. - &#x60;&#x60;updated_at&#x60;&#x60;: Unix timestamp in seconds when the list was updated. - &#x60;&#x60;expiry&#x60;&#x60;: Unix timestamp in seconds when the list will expire. If it does not exist, it will never expire. - &#x60;&#x60;origins&#x60;&#x60;: list of websites that are using the list as a denylist.     - &#x60;&#x60;self&#x60;&#x60;: the URI to all the list of origins.     - &#x60;&#x60;lists&#x60;&#x60;: list of lists that the origin is using.         - &#x60;&#x60;self&#x60;&#x60;: the URI to the individual information of the list.         - &#x60;&#x60;origin&#x60;&#x60;: the protocol and domain of the website that is using the list.         - &#x60;&#x60;status&#x60;&#x60;: the status of the list. It can be &#x60;&#x60;ACTIVE&#x60;&#x60; or &#x60;&#x60;INACTIVE&#x60;&#x60; or &#x60;&#x60;EXPIRED&#x60;&#x60;. If the list is &#x60;&#x60;EXPIRED&#x60;&#x60; it means that the list is not available anymore if not renewed.         - &#x60;&#x60;expiry&#x60;&#x60;: Unix timestamp in seconds when the list will expire. If it does not exist, it will never expire.         - &#x60;&#x60;created_at&#x60;&#x60;: Unix timestamp in seconds when the list was created.         - &#x60;&#x60;updated_at&#x60;&#x60;: Unix timestamp in seconds when the list was updated.  ### Errors  - If the deny list is not a valid UUID, it will return a &#x60;&#x60;422&#x60;&#x60; (Unprocessable Entity) error. - If the private denylist ID does not exist, it will return a &#x60;&#x60;404&#x60;&#x60; (Not found) error.  It will also return the API Global errors described in the API description.

### Example

```javascript
import ThreatJammerComUserApi from 'threat_jammer_com_user_api';
let defaultClient = ThreatJammerComUserApi.ApiClient.instance;
// Configure Bearer access token for authorization: HTTPBearer
let HTTPBearer = defaultClient.authentications['HTTPBearer'];
HTTPBearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new ThreatJammerComUserApi.DenylistDataQueryAndManagementApi();
let denylistId = "denylistId_example"; // String | 
apiInstance.getSingleDenylistV1DenylistPrivateDenylistIdGet(denylistId, (error, data, response) => {
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
 **denylistId** | **String**|  | 

### Return type

[**PrivateAclGroupListOutput**](PrivateAclGroupListOutput.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSingleDenylistV1DenylistPublicDenylistIdGet

> PublicAclGroupListOutput getSingleDenylistV1DenylistPublicDenylistIdGet(denylistId)

Get the details of the denylist.

### What Obtain the details of an deny list available in the service.  ### Parameters No parameters  ### Result The result is a JSON object with a list of the following JSON objects: - &#x60;&#x60;self&#x60;&#x60;: the URI to individual information of the list. - &#x60;&#x60;name&#x60;&#x60;: A human readable name of the list. - &#x60;&#x60;description&#x60;&#x60;: A long detailed information about what the list contains and how it is used. - &#x60;&#x60;resource_type&#x60;&#x60;: The type of the list. It can be &#x60;&#x60;CIDR&#x60;&#x60;, &#x60;&#x60;AS&#x60;&#x60;, &#x60;&#x60;COUNTRY&#x60;&#x60;, &#x60;&#x60;CONTINENT&#x60;&#x60; or &#x60;&#x60;DATACENTER_ID&#x60;&#x60;. - &#x60;&#x60;list_type&#x60;&#x60;: The type of the list. It can be &#x60;&#x60;ALLOW&#x60;&#x60; or &#x60;&#x60;DENY&#x60;&#x60;. - &#x60;&#x60;status&#x60;&#x60;: The status of the list. It can be &#x60;&#x60;ACTIVE&#x60;&#x60; or &#x60;&#x60;INACTIVE&#x60;&#x60; or &#x60;&#x60;EXPIRED&#x60;&#x60;. If the list is &#x60;&#x60;EXPIRED&#x60;&#x60;it means that the list is not available anymore if not renewed. - &#x60;&#x60;created_at&#x60;&#x60;: Unix timestamp in seconds when the list was created. - &#x60;&#x60;updated_at&#x60;&#x60;: Unix timestamp in seconds when the list was updated.  If the list is already selected by the user, the JSON object will also contain the following fields:     - &#x60;&#x60;expiry&#x60;&#x60;: Unix timestamp in seconds when the list will expire. If it does not exist, it will never expire.     - &#x60;&#x60;origins&#x60;&#x60;: list of websites that are using the list as an denylist.         - &#x60;&#x60;self&#x60;&#x60;: the URI to all the list of origins.         - &#x60;&#x60;lists&#x60;&#x60;: list of lists that the origin is using.             - &#x60;&#x60;self&#x60;&#x60;: the URI to the individual information of the list.             - &#x60;&#x60;origin&#x60;&#x60;: the protocol and domain of the website that is using the list.             - &#x60;&#x60;status&#x60;&#x60;: the status of the list. It can be &#x60;&#x60;ACTIVE&#x60;&#x60; or &#x60;&#x60;INACTIVE&#x60;&#x60; or &#x60;&#x60;EXPIRED&#x60;&#x60;. If the list is &#x60;&#x60;EXPIRED&#x60;&#x60;            it means that the list is not available anymore if not renewed.             - &#x60;&#x60;expiry&#x60;&#x60;: Unix timestamp in seconds when the list will expire. If it does not exist, it will never expire.             - &#x60;&#x60;created_at&#x60;&#x60;: Unix timestamp in seconds when the list was created.             - &#x60;&#x60;updated_at&#x60;&#x60;: Unix timestamp in seconds when the list was updated.  ### Errors  If the list does not exist, it will return a 404 error.  It will return the API Global errors described in the API description.

### Example

```javascript
import ThreatJammerComUserApi from 'threat_jammer_com_user_api';
let defaultClient = ThreatJammerComUserApi.ApiClient.instance;
// Configure Bearer access token for authorization: HTTPBearer
let HTTPBearer = defaultClient.authentications['HTTPBearer'];
HTTPBearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new ThreatJammerComUserApi.DenylistDataQueryAndManagementApi();
let denylistId = "denylistId_example"; // String | 
apiInstance.getSingleDenylistV1DenylistPublicDenylistIdGet(denylistId, (error, data, response) => {
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
 **denylistId** | **String**|  | 

### Return type

[**PublicAclGroupListOutput**](PublicAclGroupListOutput.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## queryAllTheIpAddressesReportedByTheUserV1DenylistReportedIpGet

> IPListCollectionOutput queryAllTheIpAddressesReportedByTheUserV1DenylistReportedIpGet(opts)

Get the list of automatically reported IP addresses by the user.

### What Obtain the list of all the IPv4 or IPv6 addresses that have been automatically reported by the user. A user can report automatically an IP address with the asynchronous API. The reported IP addresses differ from the ones managed with the endpoint &#x60;&#x60;/v1/denylist/private/ip/%s&#x60;&#x60;. As a rule of thumb,  the reported IP addresses are the ones submitted by devices like honeypots, firewalls, log engines, etc. The denylisted IP addresses are the ones submitted manually by the user from files or indidual items.  ### Parameters The endpoint accepts the following parameters in the query string: - &#x60;&#x60;dataset&#x60;&#x60;: (Optional) Name of the dataset to filter the query. If not given, then all datasets are queried. If given, then only the changes logged in the given dataset are returned. The list of datasets is obtained from the &#x60;&#x60;/v1/dataset/ip&#x60;&#x60; endpoint. - &#x60;&#x60;reported_before&#x60;&#x60;: (Optional) The UNIX timestamp in milliseconds of the earliest reported date to be included in the query. If not given, then the earliest date is current time. - &#x60;&#x60;reported_after&#x60;&#x60;: (Optional) The UNIX timestamp in milliseconds of the oldest reported date to be included in the query. If not given, then the oldest date is the first event logged. - &#x60;&#x60;expires_before&#x60;&#x60;: (Optional) The UNIX timestamp in milliseconds of the earliest expiry date to be included in the query. If not given, then the earliest date is current time. - &#x60;&#x60;expires_after&#x60;&#x60;: (Optional) The UNIX timestamp in milliseconds of the oldest expiry date to be included in the query. If not given, then the oldest date is the first event logged. - &#x60;&#x60;greater_than&#x60;&#x60;: (Optional) Restricts the result displaying only the IP addresses reported more times than the given value. It must be an integer greater than 0. - &#x60;&#x60;less_than&#x60;&#x60;: (Optional) Restricts the result displaying only the IP addresses reported less times than the given value. It must be an integer greater than 0. - &#x60;&#x60;ip_protocol_version&#x60;&#x60;: (Optional) Restricts the result displaying only the IP addresses with the given IP protocol version. Values are: ALL, IPV4, IPV6. If not given, then all IP addresses are returned. - &#x60;&#x60;output_format&#x60;&#x60;: (Optional) The format of the output. Values are: JSON, CSV, AWS-WAF. If not given, then the default format is JSON. AWS-WAF is the format used by AWS WAF to import ipsets in the service. You can find more information about AWS WAF import [here](https://docs.aws.amazon.com/waf/latest/APIReference/API_CreateIPSet.html).  ### Result The result is a JSON object with a list of the following JSON objects: - &#x60;&#x60;self&#x60;&#x60;: the URI to individual status. - &#x60;&#x60;addresses&#x60;&#x60;: a list of JSON objects with the following fields:     - &#x60;&#x60;self&#x60;&#x60;: the URI to individual reported IP information.     - &#x60;&#x60;last_report&#x60;&#x60;: Unix timestamp in milliseconds when the IP address was last reported.     - &#x60;&#x60;expiry&#x60;&#x60;: Unix timestamp in milliseconds when the IP address will expire and be removed.     - &#x60;&#x60;total_reports&#x60;&#x60;: Total number of reports for the IP address.     - &#x60;&#x60;protocol&#x60;&#x60;: IP protocol version of the IP address. Same value as the &#x60;&#x60;ip_protocol_version&#x60;&#x60; parameter if given.     - &#x60;&#x60;dataset&#x60;&#x60;: Name of the dataset where the IP address was reported. Must be a value from the &#x60;&#x60;/v1/dataset/ip&#x60;&#x60; endpoint.     - &#x60;&#x60;tags&#x60;&#x60;: A list of strings with the tags associated to the IP address at the origin device. It helps to classify the origin of the report.  ### Errors - a &#x60;400 Bad Request&#x60; error if any timestamp is in the future. - a &#x60;400 Bad Request&#x60; error if the dataset is not a string that can have numbers, upper and lower case letters, and underscores. - a &#x60;404 Not Found&#x60; error if the dataset was not found. - a &#x60;422 Unprocessable Entity&#x60; error if some of the parameters are malformed.  It will also return the API Global errors described in the API description.

### Example

```javascript
import ThreatJammerComUserApi from 'threat_jammer_com_user_api';
let defaultClient = ThreatJammerComUserApi.ApiClient.instance;
// Configure Bearer access token for authorization: HTTPBearer
let HTTPBearer = defaultClient.authentications['HTTPBearer'];
HTTPBearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new ThreatJammerComUserApi.DenylistDataQueryAndManagementApi();
let opts = {
  'dataset': "dataset_example", // String | The dataset list type to filter for. Must be uppercase, numbers and underscore
  'reportedBefore': 56, // Number | Restricts the result displaying only the IP addresses reported before `reported_before`. It must be a UNIX timestamp in seconds.
  'reportedAfter': 56, // Number | Restricts the result displaying only the IP addresses reported after `reported_after`. It must be a UNIX timestamp in seconds.
  'expiresBefore': 56, // Number | Restricts the result displaying only the IP addresses that will expire before `expires_before`. It must be a UNIX timestamp in seconds greater than the current UNIX timestamp.
  'expiresAfter': 56, // Number | Restricts the result displaying only the IP addresses that will expire after `expires_after`. It must be a UNIX timestamp in seconds greater than the current UNIX timestamp.
  'greaterThan': 56, // Number | Restricts the result displaying only the IP addresses reported more times than `greater_than`. It must be an integer greater than 0.
  'lessThan': 56, // Number | Restricts the result displaying only the IP addresses reported less times than `less_than`. It must be an integer greater than 1.
  'ipProtocolVersion': "'ALL'", // String | Restrict the result displaying the IP protocol version requested (IPV4 or IPV6) or both (ALL). Some output formats MUST filter by IP protocol version first.
  'outputFormat': "'JSON'" // String | The output format of the datasets.
};
apiInstance.queryAllTheIpAddressesReportedByTheUserV1DenylistReportedIpGet(opts, (error, data, response) => {
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
 **dataset** | **String**| The dataset list type to filter for. Must be uppercase, numbers and underscore | [optional] 
 **reportedBefore** | **Number**| Restricts the result displaying only the IP addresses reported before &#x60;reported_before&#x60;. It must be a UNIX timestamp in seconds. | [optional] 
 **reportedAfter** | **Number**| Restricts the result displaying only the IP addresses reported after &#x60;reported_after&#x60;. It must be a UNIX timestamp in seconds. | [optional] 
 **expiresBefore** | **Number**| Restricts the result displaying only the IP addresses that will expire before &#x60;expires_before&#x60;. It must be a UNIX timestamp in seconds greater than the current UNIX timestamp. | [optional] 
 **expiresAfter** | **Number**| Restricts the result displaying only the IP addresses that will expire after &#x60;expires_after&#x60;. It must be a UNIX timestamp in seconds greater than the current UNIX timestamp. | [optional] 
 **greaterThan** | **Number**| Restricts the result displaying only the IP addresses reported more times than &#x60;greater_than&#x60;. It must be an integer greater than 0. | [optional] 
 **lessThan** | **Number**| Restricts the result displaying only the IP addresses reported less times than &#x60;less_than&#x60;. It must be an integer greater than 1. | [optional] 
 **ipProtocolVersion** | **String**| Restrict the result displaying the IP protocol version requested (IPV4 or IPV6) or both (ALL). Some output formats MUST filter by IP protocol version first. | [optional] [default to &#39;ALL&#39;]
 **outputFormat** | **String**| The output format of the datasets. | [optional] [default to &#39;JSON&#39;]

### Return type

[**IPListCollectionOutput**](IPListCollectionOutput.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## queryAnIpAddressesReportedByTheUserV1DenylistReportedIpIpAddressGet

> IPListOutput queryAnIpAddressesReportedByTheUserV1DenylistReportedIpIpAddressGet(ipAddress)

Get the details of an automatically reported IP addresses by the user.

### What Obtain the details of an IPv4 or IPv6 addresses that have been automatically reported by the user. A user can report automatically an IP address with the asynchronous API. The reported IP address differs from the ones managed with the endpoint &#x60;&#x60;/v1/denylist/private/ip/%s&#x60;&#x60;. As a rule of thumb,  the reported IP addresses are the ones submitted by devices like honeypots, firewalls, log engines, etc. The denylisted IP addresses are the ones submitted manually by the user from files or indidual items.  ### Parameters The endpoint accepts the following parameters in the path: - &#x60;&#x60;ip_address&#x60;&#x60;: (Mandatory) The public IPv4 or IPv6 addresses to be queried.  ### Result The result is a JSON object with the following fields: - &#x60;&#x60;self&#x60;&#x60;: the URI to individual reported IP information. - &#x60;&#x60;last_report&#x60;&#x60;: Unix timestamp in milliseconds when the IP address was last reported. - &#x60;&#x60;expiry&#x60;&#x60;: Unix timestamp in milliseconds when the IP address will expire and be removed. - &#x60;&#x60;total_reports&#x60;&#x60;: Total number of reports for the IP address. - &#x60;&#x60;protocol&#x60;&#x60;: IP protocol version of the IP address. Values can be IPV4 or IPV6. - &#x60;&#x60;dataset&#x60;&#x60;: Name of the dataset where the IP address was reported. Must be a value from the &#x60;&#x60;/v1/dataset/ip&#x60;&#x60; endpoint. - &#x60;&#x60;tags&#x60;&#x60;: A list of strings with the tags associated to the IP address at the origin device. It helps to classify the origin of the report.  ### Errors - a &#x60;422 Unprocessable Entity&#x60; error if the IP address is malformed.  It will also return the API Global errors described in the API description.

### Example

```javascript
import ThreatJammerComUserApi from 'threat_jammer_com_user_api';
let defaultClient = ThreatJammerComUserApi.ApiClient.instance;
// Configure Bearer access token for authorization: HTTPBearer
let HTTPBearer = defaultClient.authentications['HTTPBearer'];
HTTPBearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new ThreatJammerComUserApi.DenylistDataQueryAndManagementApi();
let ipAddress = "ipAddress_example"; // String | 
apiInstance.queryAnIpAddressesReportedByTheUserV1DenylistReportedIpIpAddressGet(ipAddress, (error, data, response) => {
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
 **ipAddress** | **String**|  | 

### Return type

[**IPListOutput**](IPListOutput.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## queryResourceDenylistsV1DenylistPrivateIpAddressGet

> AclListCollectionOutput queryResourceDenylistsV1DenylistPrivateIpAddressGet(address)

Get the different denylists where the IP address was found.

### What Obtain the list of all the different denylists where the IP address entered by the user. The denylisted forbidden datasets are the ones submitted manually by the user from files or indidual items.  ### Parameters The endpoint accepts the &#x60;address&#x60; parameter as query string.  ### Result The result is a JSON object with a list of the following JSON objects: - &#x60;&#x60;self&#x60;&#x60;: the URI to individual status. - &#x60;&#x60;cidrs&#x60;&#x60;: the URI of the lists of CIDRs where the IP was found. - &#x60;&#x60;country&#x60;&#x60;: the URIs where the lists of countries where the IP address was found - &#x60;&#x60;continent&#x60;&#x60;: the URI where the continent where the IP address was found. - &#x60;&#x60;asn&#x60;&#x60;: the URIs where the list of continents of the ASN where the IP address was found. - &#x60;&#x60;datacenter&#x60;&#x60;: the URIs of the lists of datacenters where the IP address was found. If not found, the result is an empty string. - &#x60;&#x60;reported&#x60;&#x60;: the URI of the information of the IP address reported by the user.  ### Errors - a &#x60;422 Unprocessable Entity&#x60; error if the IP address was malformed.  It will also return the API Global errors described in the API description.

### Example

```javascript
import ThreatJammerComUserApi from 'threat_jammer_com_user_api';
let defaultClient = ThreatJammerComUserApi.ApiClient.instance;
// Configure Bearer access token for authorization: HTTPBearer
let HTTPBearer = defaultClient.authentications['HTTPBearer'];
HTTPBearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new ThreatJammerComUserApi.DenylistDataQueryAndManagementApi();
let address = new ThreatJammerComUserApi.Address(); // Address | 
apiInstance.queryResourceDenylistsV1DenylistPrivateIpAddressGet(address, (error, data, response) => {
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
 **address** | [**Address**](.md)|  | 

### Return type

[**AclListCollectionOutput**](AclListCollectionOutput.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## queryResourceDenylistsV1DenylistPublicIpAddressGet

> AclListCollectionOutput queryResourceDenylistsV1DenylistPublicIpAddressGet(address)

Get the different public denylists where the IP address was found.

### What Obtain the list of all the different public denylists where the IP address entered by the user is. The public denylists are the ones activated by the user, but managed by Threatjammer administrators.  ### Parameters The endpoint accepts the &#x60;address&#x60; parameter as query string.  ### Result The result is a JSON object with a list of the following JSON objects: - &#x60;&#x60;self&#x60;&#x60;: the URI to individual status. - &#x60;&#x60;cidrs&#x60;&#x60;: the URI of the lists of CIDRs where the IP was found. - &#x60;&#x60;country&#x60;&#x60;: the URIs where the lists of countries where the IP address was found - &#x60;&#x60;continent&#x60;&#x60;: the URI where the continent where the IP address was found. - &#x60;&#x60;asn&#x60;&#x60;: the URIs where the list of continents of the ASN where the IP address was found. - &#x60;&#x60;datacenter&#x60;&#x60;: the URIs of the lists of datacenters where the IP address was found. If not found, the result is an empty string.  ### Errors - a &#x60;422 Unprocessable Entity&#x60; error if the IP address was malformed.  It will also return the API Global errors described in the API description.

### Example

```javascript
import ThreatJammerComUserApi from 'threat_jammer_com_user_api';
let defaultClient = ThreatJammerComUserApi.ApiClient.instance;
// Configure Bearer access token for authorization: HTTPBearer
let HTTPBearer = defaultClient.authentications['HTTPBearer'];
HTTPBearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new ThreatJammerComUserApi.DenylistDataQueryAndManagementApi();
let address = new ThreatJammerComUserApi.Address(); // Address | 
apiInstance.queryResourceDenylistsV1DenylistPublicIpAddressGet(address, (error, data, response) => {
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
 **address** | [**Address**](.md)|  | 

### Return type

[**AclListCollectionOutput**](AclListCollectionOutput.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updatePrivateContentOfTheDenylistOfTheUserV1DenylistPrivateDenylistIdContentPut

> Object updatePrivateContentOfTheDenylistOfTheUserV1DenylistPrivateDenylistIdContentPut(denylistId, opts)

Add or remove content of a private denylist of the user.

### What Add or remove content of a private denylist of the user. The content can be CIDRs, ASNs, countries, continents or datacenter IDs.   The number of elements allowed in all the lists are limited depending on the plan of the user: - Free: 100 elements - Basic: 1000 elements - Pro: 10000 elements  ### Parameters Pass the private denylist ID as query parameter.  In the body the following parameters: - &#x60;&#x60;append&#x60;&#x60;: (Optional) Add CIDRs, ASNs, countries, continents or datacenter IDs to add to the list. It&#39;s not possible to mix different resource types in the same list. - &#x60;&#x60;remove&#x60;&#x60;: (Optional) Extract CIDRs, ASNs, countries, continents or datacenter IDs to add to the list. It&#39;s not possible to mix different resource types in the same list.   ### Result If successful, it will return a &#x60;&#x60;202&#x60;&#x60; (Accepted) response with an empty body. The operation is asynchronous,and can take several seconds to complete.  ### Errors  - If the deny list is not a valid UUID, it will return a &#x60;&#x60;422&#x60;&#x60; (Unprocessable Entity) error. - If the private denylist ID does not exist, it will return a &#x60;&#x60;404&#x60;&#x60; (Not found) error. - If the &#x60;&#x60;append&#x60;&#x60; or &#x60;&#x60;remove&#x60;&#x60; parameters are not processable, it will return a &#x60;&#x60;422&#x60;&#x60; (Unprocessable Entity) error. - If the number of elements in the lists is over the limit, it will return a &#x60;&#x60;413&#x60;&#x60; (Payload Too Large) error.  It will also return the API Global errors described in the API description.

### Example

```javascript
import ThreatJammerComUserApi from 'threat_jammer_com_user_api';
let defaultClient = ThreatJammerComUserApi.ApiClient.instance;
// Configure Bearer access token for authorization: HTTPBearer
let HTTPBearer = defaultClient.authentications['HTTPBearer'];
HTTPBearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new ThreatJammerComUserApi.DenylistDataQueryAndManagementApi();
let denylistId = "denylistId_example"; // String | 
let opts = {
  'bodyUpdatePrivateContentOfTheDenylistOfTheUserV1DenylistPrivateDenylistIdContentPut': new ThreatJammerComUserApi.BodyUpdatePrivateContentOfTheDenylistOfTheUserV1DenylistPrivateDenylistIdContentPut() // BodyUpdatePrivateContentOfTheDenylistOfTheUserV1DenylistPrivateDenylistIdContentPut | 
};
apiInstance.updatePrivateContentOfTheDenylistOfTheUserV1DenylistPrivateDenylistIdContentPut(denylistId, opts, (error, data, response) => {
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
 **denylistId** | **String**|  | 
 **bodyUpdatePrivateContentOfTheDenylistOfTheUserV1DenylistPrivateDenylistIdContentPut** | [**BodyUpdatePrivateContentOfTheDenylistOfTheUserV1DenylistPrivateDenylistIdContentPut**](BodyUpdatePrivateContentOfTheDenylistOfTheUserV1DenylistPrivateDenylistIdContentPut.md)|  | [optional] 

### Return type

**Object**

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updatePrivateDenylistOfTheUserV1DenylistPrivateDenylistIdPut

> Object updatePrivateDenylistOfTheUserV1DenylistPrivateDenylistIdPut(denylistId, opts)

Update the information of an existing private denylist of the user.

### What Updates the information that describes the denylist of the user in the system. The parameters that can be modified are:  - name  - description  - tags  - expiry  This is an asynchronous operation. It can take several seconds until the operation completes, but the request will immediately return a 202 Accepted response.  The default lists &#x60;&#x60;External sources reported CIDRs&#x60;&#x60; and &#x60;&#x60;Default denylist&#x60;&#x60; cannot be updated.  ### Parameters In the query string the ID of the private deny list to delete.  In the body the following parameters: - &#x60;&#x60;name&#x60;&#x60;: (Optional) A human readable name of the list. - &#x60;&#x60;description&#x60;&#x60;: (Optional) A long detailed information about what the list contains and how it is used. - &#x60;&#x60;tags&#x60;&#x60;: (Optional) A list of tags that describe the list. - &#x60;&#x60;expiry&#x60;&#x60;: (Optional) Unix timestamp in seconds when the list will expire. If it does not exist, it will never expire.  ### Result It should always return a 202 Accepted response with an empty body.  ### Errors  - If the list does not exist, it will return a &#x60;404&#x60; (Not found) error. - If the list is a default list, it will return a &#x60;403&#x60; (Forbidden) error. - If the deny list is not a valid UUID, it will return a &#x60;422&#x60; (Unprocessable Entity) error. - If the expiry is not a valid timestamp, it will return a &#x60;422&#x60; (Unprocessable Entity) error. - If the expiry is in the past, it will return a &#x60;400&#x60; (Bad Request) error. - If the name is not a string, it will return a &#x60;422&#x60; (Unprocessable Entity) error. - If the description is not a string, it will return a &#x60;422&#x60; (Unprocessable Entity) error.  It will return the API Global errors described in the API description.

### Example

```javascript
import ThreatJammerComUserApi from 'threat_jammer_com_user_api';
let defaultClient = ThreatJammerComUserApi.ApiClient.instance;
// Configure Bearer access token for authorization: HTTPBearer
let HTTPBearer = defaultClient.authentications['HTTPBearer'];
HTTPBearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new ThreatJammerComUserApi.DenylistDataQueryAndManagementApi();
let denylistId = "denylistId_example"; // String | 
let opts = {
  'bodyUpdatePrivateDenylistOfTheUserV1DenylistPrivateDenylistIdPut': new ThreatJammerComUserApi.BodyUpdatePrivateDenylistOfTheUserV1DenylistPrivateDenylistIdPut() // BodyUpdatePrivateDenylistOfTheUserV1DenylistPrivateDenylistIdPut | 
};
apiInstance.updatePrivateDenylistOfTheUserV1DenylistPrivateDenylistIdPut(denylistId, opts, (error, data, response) => {
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
 **denylistId** | **String**|  | 
 **bodyUpdatePrivateDenylistOfTheUserV1DenylistPrivateDenylistIdPut** | [**BodyUpdatePrivateDenylistOfTheUserV1DenylistPrivateDenylistIdPut**](BodyUpdatePrivateDenylistOfTheUserV1DenylistPrivateDenylistIdPut.md)|  | [optional] 

### Return type

**Object**

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

