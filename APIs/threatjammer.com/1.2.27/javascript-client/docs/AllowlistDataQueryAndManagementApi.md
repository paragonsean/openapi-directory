# ThreatJammerComUserApi.AllowlistDataQueryAndManagementApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**changeStatusOfTheAllowlistV1AllowlistPublicAllowlistIdPut**](AllowlistDataQueryAndManagementApi.md#changeStatusOfTheAllowlistV1AllowlistPublicAllowlistIdPut) | **PUT** /v1/allowlist/public/{allowlist_id} | Toogle the status of an allow list.
[**changeStatusOfTheOriginAllowlistV1AllowlistPrivateAllowlistIdOriginPut**](AllowlistDataQueryAndManagementApi.md#changeStatusOfTheOriginAllowlistV1AllowlistPrivateAllowlistIdOriginPut) | **PUT** /v1/allowlist/private/{allowlist_id}/origin | Toogle the status of the origin in an allow list.
[**changeStatusOfTheOriginAllowlistV1AllowlistPublicAllowlistIdOriginPut**](AllowlistDataQueryAndManagementApi.md#changeStatusOfTheOriginAllowlistV1AllowlistPublicAllowlistIdOriginPut) | **PUT** /v1/allowlist/public/{allowlist_id}/origin | Toogle the status of the origin in an allow list.
[**createPrivateAllowlistOfTheUserV1AllowlistPrivatePost**](AllowlistDataQueryAndManagementApi.md#createPrivateAllowlistOfTheUserV1AllowlistPrivatePost) | **POST** /v1/allowlist/private | Creates a new private allowlist binded to the user.
[**deleteTheAllowlistContentV1AllowlistPrivateAllowlistIdContentDelete**](AllowlistDataQueryAndManagementApi.md#deleteTheAllowlistContentV1AllowlistPrivateAllowlistIdContentDelete) | **DELETE** /v1/allowlist/private/{allowlist_id}/content | Delete all the content of a private allowlist of the user.
[**deleteTheAllowlistV1AllowlistPrivateAllowlistIdDelete**](AllowlistDataQueryAndManagementApi.md#deleteTheAllowlistV1AllowlistPrivateAllowlistIdDelete) | **DELETE** /v1/allowlist/private/{allowlist_id} | Delete all the bindings between a user and a private allowlist.
[**deleteTheAllowlistV1AllowlistPublicAllowlistIdDelete**](AllowlistDataQueryAndManagementApi.md#deleteTheAllowlistV1AllowlistPublicAllowlistIdDelete) | **DELETE** /v1/allowlist/public/{allowlist_id} | Delete all the bindings between a user and an allowlist.
[**getAllOwnedAllowlistsByResourceTypeV1AllowlistPublicOwnedResourceTypeGet**](AllowlistDataQueryAndManagementApi.md#getAllOwnedAllowlistsByResourceTypeV1AllowlistPublicOwnedResourceTypeGet) | **GET** /v1/allowlist/public/owned/{resource_type} | Get the set of public allowlists of a user by resource type.
[**getAllPrivateAllowlistsByResourceTypeV1AllowlistPrivateAllResourceTypeGet**](AllowlistDataQueryAndManagementApi.md#getAllPrivateAllowlistsByResourceTypeV1AllowlistPrivateAllResourceTypeGet) | **GET** /v1/allowlist/private/all/{resource_type} | Get the set of private allowlists of the user by resource type.
[**getAllPrivateAllowlistsV1AllowlistPrivateAllGet**](AllowlistDataQueryAndManagementApi.md#getAllPrivateAllowlistsV1AllowlistPrivateAllGet) | **GET** /v1/allowlist/private/all | Get the set of private allowlists of the user.
[**getAllPublicAllowlistsByResourceTypeV1AllowlistPublicAllResourceTypeGet**](AllowlistDataQueryAndManagementApi.md#getAllPublicAllowlistsByResourceTypeV1AllowlistPublicAllResourceTypeGet) | **GET** /v1/allowlist/public/all/{resource_type} | Get the set of public allowlists by resource type.
[**getAllPublicAllowlistsV1AllowlistPublicAllGet**](AllowlistDataQueryAndManagementApi.md#getAllPublicAllowlistsV1AllowlistPublicAllGet) | **GET** /v1/allowlist/public/all | Get the set of public allowlists.
[**getAllowlistContentV1AllowlistPrivateAllowlistIdContentGet**](AllowlistDataQueryAndManagementApi.md#getAllowlistContentV1AllowlistPrivateAllowlistIdContentGet) | **GET** /v1/allowlist/private/{allowlist_id}/content | Get the content of a private allowlist of the user.
[**getPublicAllowlistsOwnedByTheUserV1AllowlistPublicOwnedGet**](AllowlistDataQueryAndManagementApi.md#getPublicAllowlistsOwnedByTheUserV1AllowlistPublicOwnedGet) | **GET** /v1/allowlist/public/owned | Get the set of owned allowlists.
[**getSingleAllowlistV1AllowlistPrivateAllowlistIdGet**](AllowlistDataQueryAndManagementApi.md#getSingleAllowlistV1AllowlistPrivateAllowlistIdGet) | **GET** /v1/allowlist/private/{allowlist_id} | Get the details of a specific private allowlist of the user.
[**getSingleAllowlistV1AllowlistPublicAllowlistIdGet**](AllowlistDataQueryAndManagementApi.md#getSingleAllowlistV1AllowlistPublicAllowlistIdGet) | **GET** /v1/allowlist/public/{allowlist_id} | Get the details of the allowlist.
[**queryResourceAllowlistsV1AllowlistPublicIpAddressGet**](AllowlistDataQueryAndManagementApi.md#queryResourceAllowlistsV1AllowlistPublicIpAddressGet) | **GET** /v1/allowlist/public/ip/{address} | Get the different public allowlists where the IP address was found.
[**queryResourceDenylistsV1AllowlistPrivateIpAddressGet**](AllowlistDataQueryAndManagementApi.md#queryResourceDenylistsV1AllowlistPrivateIpAddressGet) | **GET** /v1/allowlist/private/ip/{address} | Get the different private allowlists where the IP address was found.
[**updatePrivateAllowlistOfTheUserV1AllowlistPrivateAllowlistIdPut**](AllowlistDataQueryAndManagementApi.md#updatePrivateAllowlistOfTheUserV1AllowlistPrivateAllowlistIdPut) | **PUT** /v1/allowlist/private/{allowlist_id} | Update the information of an existing private allowlist of the user.
[**updatePrivateContentOfTheAllowlistOfTheUserV1AllowlistPrivateAllowlistIdContentPut**](AllowlistDataQueryAndManagementApi.md#updatePrivateContentOfTheAllowlistOfTheUserV1AllowlistPrivateAllowlistIdContentPut) | **PUT** /v1/allowlist/private/{allowlist_id}/content | Add or remove content of a private allowlist of the user.



## changeStatusOfTheAllowlistV1AllowlistPublicAllowlistIdPut

> Object changeStatusOfTheAllowlistV1AllowlistPublicAllowlistIdPut(allowlistId, bodyChangeStatusOfTheAllowlistV1AllowlistPublicAllowlistIdPut)

Toogle the status of an allow list.

### What Change the status of an allow list to &#x60;&#x60;ACTIVE&#x60;&#x60; or &#x60;&#x60;INACTIVE&#x60;&#x60;. An &#x60;&#x60;INACTIVE&#x60;&#x60; list will not be used by the service. An &#x60;&#x60;ACTIVE&#x60;&#x60; list will be used by the service. As an optional parameter it can be provided an &#x60;&#x60;expiry&#x60;&#x60; date in seconds since epoch. If not provided, the list will never expire.   This is an asynchronous operation. It can take several seconds until the operation completes, but the request will  immediately return a 202 Accepted response.  ### Parameters In the query string the ID of the allow list to change the status. In the body the JSON object with the following fields: - &#x60;&#x60;status&#x60;&#x60;: The status of the list. It can be &#x60;&#x60;ACTIVE&#x60;&#x60; or &#x60;&#x60;INACTIVE&#x60;&#x60;. - &#x60;&#x60;expiry&#x60;&#x60;: Unix timestamp in seconds when the list will expire. If it does not exist, it will never expire.  ### Result It should always return a 202 Accepted response with an empty body.  ### Errors  If the list does not exist, it will return a 404 error. If the status is not &#x60;&#x60;ACTIVE&#x60;&#x60; or &#x60;&#x60;INACTIVE&#x60;&#x60;, it will return a 422 error. If the expiry is not a valid timestamp, it will return a 422 error. If the allow list is not a valid UUID, it will return a 422 error.  It will return the API Global errors described in the API description.

### Example

```javascript
import ThreatJammerComUserApi from 'threat_jammer_com_user_api';
let defaultClient = ThreatJammerComUserApi.ApiClient.instance;
// Configure Bearer access token for authorization: HTTPBearer
let HTTPBearer = defaultClient.authentications['HTTPBearer'];
HTTPBearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new ThreatJammerComUserApi.AllowlistDataQueryAndManagementApi();
let allowlistId = "allowlistId_example"; // String | 
let bodyChangeStatusOfTheAllowlistV1AllowlistPublicAllowlistIdPut = new ThreatJammerComUserApi.BodyChangeStatusOfTheAllowlistV1AllowlistPublicAllowlistIdPut(); // BodyChangeStatusOfTheAllowlistV1AllowlistPublicAllowlistIdPut | 
apiInstance.changeStatusOfTheAllowlistV1AllowlistPublicAllowlistIdPut(allowlistId, bodyChangeStatusOfTheAllowlistV1AllowlistPublicAllowlistIdPut, (error, data, response) => {
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
 **allowlistId** | **String**|  | 
 **bodyChangeStatusOfTheAllowlistV1AllowlistPublicAllowlistIdPut** | [**BodyChangeStatusOfTheAllowlistV1AllowlistPublicAllowlistIdPut**](BodyChangeStatusOfTheAllowlistV1AllowlistPublicAllowlistIdPut.md)|  | 

### Return type

**Object**

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## changeStatusOfTheOriginAllowlistV1AllowlistPrivateAllowlistIdOriginPut

> Object changeStatusOfTheOriginAllowlistV1AllowlistPrivateAllowlistIdOriginPut(allowlistId, bodyChangeStatusOfTheOriginAllowlistV1AllowlistPrivateAllowlistIdOriginPut)

Toogle the status of the origin in an allow list.

### What Change the status of the origin of an allow list to &#x60;&#x60;ACTIVE&#x60;&#x60;, &#x60;&#x60;INACTIVE&#x60;&#x60; or &#x60;&#x60;DELETED&#x60;&#x60;.  An &#x60;&#x60;ACTIVE&#x60;&#x60; origin will apply the allow list to the protocol and domain of the origin. An origin can be created and activated simply toogling the &#x60;&#x60;ACTIVE&#x60;&#x60; status. As an optional parameter it can be provided an &#x60;&#x60;ttl&#x60;&#x60; or Time To Live parameter of the origin in the list in seconds. After the TTL expires, the origin will be removed from the list.  If the TTL is not provided, the origin will never expire.  An &#x60;&#x60;INACTIVE&#x60;&#x60; origin will not apply the allow list to the protocol and domain of the origin.  A &#x60;&#x60;DELETED&#x60;&#x60; origin will be removed from the list. It will not be used by the service anymore. The user can activate it again with the &#x60;&#x60;ACTIVE&#x60;&#x60; status.  This is an asynchronous operation. It can take several seconds until the operation completes, but the request will  immediately return a 202 Accepted response.  *This operation is not available in the Freemium plan.*  ### Parameters In the query string the ID of the allow list to change the status. In the body the JSON object with the following fields: - &#x60;&#x60;origin&#x60;&#x60;: The protocol and domain of the origin. It can be &#x60;&#x60;http://example.com&#x60;&#x60; or &#x60;&#x60;https://example.com&#x60;&#x60;. - &#x60;&#x60;status&#x60;&#x60;: The status of the list. It can be &#x60;&#x60;ACTIVE&#x60;&#x60;, &#x60;&#x60;INACTIVE&#x60;&#x60; or &#x60;&#x60;DELETED&#x60;&#x60;.  ### Result It should always return a 202 Accepted response with an empty body.  ### Errors  If the list does not exist, it will return a 404 error. If the status is not &#x60;&#x60;ACTIVE&#x60;&#x60; or &#x60;&#x60;INACTIVE&#x60;&#x60;, it will return a 422 error. If the TTL is negative in the past, it will return a 422 error. If the allow list is not a valid UUID, it will return a 422 error. If the origin is not a valid URL, it will return a 400 error. If the allowlist is not active, it will returna 409 error. If the origin is not found in the set owned by the user, it will return a 404 error.  It will return the API Global errors described in the API description.

### Example

```javascript
import ThreatJammerComUserApi from 'threat_jammer_com_user_api';
let defaultClient = ThreatJammerComUserApi.ApiClient.instance;
// Configure Bearer access token for authorization: HTTPBearer
let HTTPBearer = defaultClient.authentications['HTTPBearer'];
HTTPBearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new ThreatJammerComUserApi.AllowlistDataQueryAndManagementApi();
let allowlistId = "allowlistId_example"; // String | 
let bodyChangeStatusOfTheOriginAllowlistV1AllowlistPrivateAllowlistIdOriginPut = new ThreatJammerComUserApi.BodyChangeStatusOfTheOriginAllowlistV1AllowlistPrivateAllowlistIdOriginPut(); // BodyChangeStatusOfTheOriginAllowlistV1AllowlistPrivateAllowlistIdOriginPut | 
apiInstance.changeStatusOfTheOriginAllowlistV1AllowlistPrivateAllowlistIdOriginPut(allowlistId, bodyChangeStatusOfTheOriginAllowlistV1AllowlistPrivateAllowlistIdOriginPut, (error, data, response) => {
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
 **allowlistId** | **String**|  | 
 **bodyChangeStatusOfTheOriginAllowlistV1AllowlistPrivateAllowlistIdOriginPut** | [**BodyChangeStatusOfTheOriginAllowlistV1AllowlistPrivateAllowlistIdOriginPut**](BodyChangeStatusOfTheOriginAllowlistV1AllowlistPrivateAllowlistIdOriginPut.md)|  | 

### Return type

**Object**

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## changeStatusOfTheOriginAllowlistV1AllowlistPublicAllowlistIdOriginPut

> Object changeStatusOfTheOriginAllowlistV1AllowlistPublicAllowlistIdOriginPut(allowlistId, bodyChangeStatusOfTheOriginAllowlistV1AllowlistPublicAllowlistIdOriginPut)

Toogle the status of the origin in an allow list.

### What Change the status of the origin of an allow list to &#x60;&#x60;ACTIVE&#x60;&#x60;, &#x60;&#x60;INACTIVE&#x60;&#x60; or &#x60;&#x60;DELETED&#x60;&#x60;.  An &#x60;&#x60;ACTIVE&#x60;&#x60; origin will apply the allow list to the protocol and domain of the origin. An origin can be created and activated simply toogling the &#x60;&#x60;ACTIVE&#x60;&#x60; status. As an optional parameter it can be provided an &#x60;&#x60;ttl&#x60;&#x60; or Time To Live parameter of the origin in the list in seconds. After the TTL expires, the origin will be removed from the list.  If the TTL is not provided, the origin will never expire.  An &#x60;&#x60;INACTIVE&#x60;&#x60; origin will not apply the allow list to the protocol and domain of the origin.  A &#x60;&#x60;DELETED&#x60;&#x60; origin will be removed from the list. It will not be used by the service anymore. The user can activate it again with the &#x60;&#x60;ACTIVE&#x60;&#x60; status.  This is an asynchronous operation. It can take several seconds until the operation completes, but the request will  immediately return a 202 Accepted response.  *This operation is not available in the Freemium plan.*  ### Parameters In the query string the ID of the allow list to change the status. In the body the JSON object with the following fields: - &#x60;&#x60;origin&#x60;&#x60;: The protocol and domain of the origin. It can be &#x60;&#x60;http://example.com&#x60;&#x60; or &#x60;&#x60;https://example.com&#x60;&#x60;. - &#x60;&#x60;status&#x60;&#x60;: The status of the list. It can be &#x60;&#x60;ACTIVE&#x60;&#x60;, &#x60;&#x60;INACTIVE&#x60;&#x60; or &#x60;&#x60;DELETED&#x60;&#x60;.  ### Result It should always return a 202 Accepted response with an empty body.  ### Errors  If the list does not exist, it will return a 404 error. If the status is not &#x60;&#x60;ACTIVE&#x60;&#x60; or &#x60;&#x60;INACTIVE&#x60;&#x60;, it will return a 422 error. If the TTL is negative in the past, it will return a 422 error. If the allow list is not a valid UUID, it will return a 422 error. If the origin is not a valid URL, it will return a 400 error. If the allowlist is not active, it will returna 409 error. If the origin is not found in the set owned by the user, it will return a 404 error.  It will return the API Global errors described in the API description.

### Example

```javascript
import ThreatJammerComUserApi from 'threat_jammer_com_user_api';
let defaultClient = ThreatJammerComUserApi.ApiClient.instance;
// Configure Bearer access token for authorization: HTTPBearer
let HTTPBearer = defaultClient.authentications['HTTPBearer'];
HTTPBearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new ThreatJammerComUserApi.AllowlistDataQueryAndManagementApi();
let allowlistId = "allowlistId_example"; // String | 
let bodyChangeStatusOfTheOriginAllowlistV1AllowlistPublicAllowlistIdOriginPut = new ThreatJammerComUserApi.BodyChangeStatusOfTheOriginAllowlistV1AllowlistPublicAllowlistIdOriginPut(); // BodyChangeStatusOfTheOriginAllowlistV1AllowlistPublicAllowlistIdOriginPut | 
apiInstance.changeStatusOfTheOriginAllowlistV1AllowlistPublicAllowlistIdOriginPut(allowlistId, bodyChangeStatusOfTheOriginAllowlistV1AllowlistPublicAllowlistIdOriginPut, (error, data, response) => {
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
 **allowlistId** | **String**|  | 
 **bodyChangeStatusOfTheOriginAllowlistV1AllowlistPublicAllowlistIdOriginPut** | [**BodyChangeStatusOfTheOriginAllowlistV1AllowlistPublicAllowlistIdOriginPut**](BodyChangeStatusOfTheOriginAllowlistV1AllowlistPublicAllowlistIdOriginPut.md)|  | 

### Return type

**Object**

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createPrivateAllowlistOfTheUserV1AllowlistPrivatePost

> String createPrivateAllowlistOfTheUserV1AllowlistPrivatePost(bodyCreatePrivateAllowlistOfTheUserV1AllowlistPrivatePost)

Creates a new private allowlist binded to the user.

### What Creates a new allowlist with the information given and binded to the current user. The parameters are:  - name  - description  - tags  - expiry  - Time to Live (TTL)  - Resource Type (&#x60;CIDR&#x60;, &#x60;AS&#x60;, &#x60;COUNTRY&#x60;, &#x60;CONTINENT&#x60;, &#x60;DATACENTER_ID&#x60; and &#x60;USER AGENT&#x60;)  This is an asynchronous operation. It can take several seconds until the operation completes, but the request will immediately return a 202 Accepted response. The operation will also return the UUID of the list.  ### Parameters In the query string the ID of the private allow list to delete.  In the body the following parameters: - &#x60;&#x60;name&#x60;&#x60;: A human readable name of the list. - &#x60;&#x60;description&#x60;&#x60;: A long detailed information about what the list contains and how it is used. - &#x60;&#x60;tags&#x60;&#x60;: A list of tags that describe the list. - &#x60;&#x60;ttl&#x60;&#x60;: (Optional) The Time To Live of the list, in seconds. If it does not exist, it will never expire. - &#x60;&#x60;resource_type&#x60;&#x60;: The type of resource that the list contains. It can be &#x60;&#x60;CIDR&#x60;&#x60;, &#x60;&#x60;AS&#x60;&#x60;, &#x60;&#x60;COUNTRY&#x60;&#x60;, &#x60;&#x60;CONTINENT&#x60;&#x60;,    &#x60;&#x60;DATACENTER_ID&#x60;&#x60; or &#x60;&#x60;USER AGENT&#x60;&#x60;.  ### Result It should always return a 202 Accepted response with the UUID of the new list in the body.  ### Errors  - If the information is not valid, it will return a &#x60;422&#x60; (Unprocessable Entity) error. - If the ttl is negative, it will return a &#x60;400&#x60; (Bad Request) error.  It will return the API Global errors described in the API description.

### Example

```javascript
import ThreatJammerComUserApi from 'threat_jammer_com_user_api';
let defaultClient = ThreatJammerComUserApi.ApiClient.instance;
// Configure Bearer access token for authorization: HTTPBearer
let HTTPBearer = defaultClient.authentications['HTTPBearer'];
HTTPBearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new ThreatJammerComUserApi.AllowlistDataQueryAndManagementApi();
let bodyCreatePrivateAllowlistOfTheUserV1AllowlistPrivatePost = new ThreatJammerComUserApi.BodyCreatePrivateAllowlistOfTheUserV1AllowlistPrivatePost(); // BodyCreatePrivateAllowlistOfTheUserV1AllowlistPrivatePost | 
apiInstance.createPrivateAllowlistOfTheUserV1AllowlistPrivatePost(bodyCreatePrivateAllowlistOfTheUserV1AllowlistPrivatePost, (error, data, response) => {
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
 **bodyCreatePrivateAllowlistOfTheUserV1AllowlistPrivatePost** | [**BodyCreatePrivateAllowlistOfTheUserV1AllowlistPrivatePost**](BodyCreatePrivateAllowlistOfTheUserV1AllowlistPrivatePost.md)|  | 

### Return type

**String**

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteTheAllowlistContentV1AllowlistPrivateAllowlistIdContentDelete

> Object deleteTheAllowlistContentV1AllowlistPrivateAllowlistIdContentDelete(allowlistId)

Delete all the content of a private allowlist of the user.

### What Delete all the content of a private allowlist of the user. This will remove all the elements, and there is no way to recover them.  ### Parameters Pass the private allowlist ID as query parameter.  ### Result If successful, it will return a &#x60;&#x60;202&#x60;&#x60; (Accepted) response with an empty body. The operation is asynchronous,and can take several seconds to complete.  ### Errors  - If the allow list is not a valid UUID, it will return a &#x60;&#x60;422&#x60;&#x60; (Unprocessable Entity) error. - If the private allowlist ID does not exist, it will return a &#x60;&#x60;404&#x60;&#x60; (Not found) error.  It will also return the API Global errors described in the API description.

### Example

```javascript
import ThreatJammerComUserApi from 'threat_jammer_com_user_api';
let defaultClient = ThreatJammerComUserApi.ApiClient.instance;
// Configure Bearer access token for authorization: HTTPBearer
let HTTPBearer = defaultClient.authentications['HTTPBearer'];
HTTPBearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new ThreatJammerComUserApi.AllowlistDataQueryAndManagementApi();
let allowlistId = "allowlistId_example"; // String | 
apiInstance.deleteTheAllowlistContentV1AllowlistPrivateAllowlistIdContentDelete(allowlistId, (error, data, response) => {
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
 **allowlistId** | **String**|  | 

### Return type

**Object**

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteTheAllowlistV1AllowlistPrivateAllowlistIdDelete

> Object deleteTheAllowlistV1AllowlistPrivateAllowlistIdDelete(allowlistId)

Delete all the bindings between a user and a private allowlist.

### What Delete all the bindings between a user and a private allowlist. This will remove the content of the allowlist, the allowlist from the user and also all the origins that are using the allowlist.  This is an asynchronous operation. It can take several seconds until the operation completes, but the request willimmediately return a 202 Accepted response.  ### Parameters In the query string the ID of the private allow list to delete.  ### Result It should always return a 202 Accepted response with an empty body.  ### Errors  - If the list does not exist, it will return a 404 error. - If the allow list is not a valid UUID, it will return a 422 error.  It will return the API Global errors described in the API description.

### Example

```javascript
import ThreatJammerComUserApi from 'threat_jammer_com_user_api';
let defaultClient = ThreatJammerComUserApi.ApiClient.instance;
// Configure Bearer access token for authorization: HTTPBearer
let HTTPBearer = defaultClient.authentications['HTTPBearer'];
HTTPBearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new ThreatJammerComUserApi.AllowlistDataQueryAndManagementApi();
let allowlistId = "allowlistId_example"; // String | 
apiInstance.deleteTheAllowlistV1AllowlistPrivateAllowlistIdDelete(allowlistId, (error, data, response) => {
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
 **allowlistId** | **String**|  | 

### Return type

**Object**

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteTheAllowlistV1AllowlistPublicAllowlistIdDelete

> Object deleteTheAllowlistV1AllowlistPublicAllowlistIdDelete(allowlistId)

Delete all the bindings between a user and an allowlist.

### What Delete all the bindings between a user and an allowlist. This will remove the allowlist from the user and also all the origins that are using the allowlist.   This is an asynchronous operation. It can take several seconds until the operation completes, but the request will  immediately return a 202 Accepted response.  ### Parameters In the query string the ID of the allow list to change the status.  ### Result It should always return a 202 Accepted response with an empty body.  ### Errors  If the list does not exist, it will return a 404 error. If the allow list is not a valid UUID, it will return a 422 error.  It will return the API Global errors described in the API description.

### Example

```javascript
import ThreatJammerComUserApi from 'threat_jammer_com_user_api';
let defaultClient = ThreatJammerComUserApi.ApiClient.instance;
// Configure Bearer access token for authorization: HTTPBearer
let HTTPBearer = defaultClient.authentications['HTTPBearer'];
HTTPBearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new ThreatJammerComUserApi.AllowlistDataQueryAndManagementApi();
let allowlistId = "allowlistId_example"; // String | 
apiInstance.deleteTheAllowlistV1AllowlistPublicAllowlistIdDelete(allowlistId, (error, data, response) => {
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
 **allowlistId** | **String**|  | 

### Return type

**Object**

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getAllOwnedAllowlistsByResourceTypeV1AllowlistPublicOwnedResourceTypeGet

> PublicAclGroupListCollectionOutput getAllOwnedAllowlistsByResourceTypeV1AllowlistPublicOwnedResourceTypeGet(resourceType)

Get the set of public allowlists of a user by resource type.

### What Obtain the set of public allow lists selected by the user and wich ones are not filtering by the resource type.  ### Parameters The &#x60;&#x60;resource type&#x60;&#x60; to filter. The values can be &#x60;&#x60;CIDR&#x60;&#x60;, &#x60;&#x60;AS&#x60;&#x60;, &#x60;&#x60;COUNTRY&#x60;&#x60;, &#x60;&#x60;CONTINENT&#x60;&#x60; or &#x60;&#x60;DATACENTER_ID&#x60;&#x60;.  ### Result The result is a JSON object with a list of the following JSON objects: - &#x60;&#x60;self&#x60;&#x60;: the URI to the status of all the lists. - &#x60;&#x60;lists&#x60;&#x60;: a list of JSON objects with the available lists:     - &#x60;&#x60;self&#x60;&#x60;: the URI to individual information of the list.     - &#x60;&#x60;name&#x60;&#x60;: A human readable name of the list.     - &#x60;&#x60;description&#x60;&#x60;: A long detailed information about what the list contains and how it is used.     - &#x60;&#x60;resource_type&#x60;&#x60;: The type of the list. It can be &#x60;&#x60;CIDR&#x60;&#x60;, &#x60;&#x60;AS&#x60;&#x60;, &#x60;&#x60;COUNTRY&#x60;&#x60;, &#x60;&#x60;CONTINENT&#x60;&#x60; or &#x60;&#x60;DATACENTER_ID&#x60;&#x60;.     - &#x60;&#x60;list_type&#x60;&#x60;: The type of the list. It can be &#x60;&#x60;ALLOW&#x60;&#x60; or &#x60;&#x60;DENY&#x60;&#x60;.     - &#x60;&#x60;status&#x60;&#x60;: The status of the list. It can be &#x60;&#x60;ACTIVE&#x60;&#x60; or &#x60;&#x60;INACTIVE&#x60;&#x60; or &#x60;&#x60;EXPIRED&#x60;&#x60;. If the list is &#x60;&#x60;EXPIRED&#x60;&#x60;    it means that the list is not available anymore if not renewed.     - &#x60;&#x60;created_at&#x60;&#x60;: Unix timestamp in seconds when the list was created.     - &#x60;&#x60;updated_at&#x60;&#x60;: Unix timestamp in seconds when the list was updated.     - &#x60;&#x60;expiry&#x60;&#x60;: Unix timestamp in seconds when the list will expire. If it does not exist, it will never expire.     - &#x60;&#x60;origins&#x60;&#x60;: list of websites that are using the list as an allowlist.         - &#x60;&#x60;self&#x60;&#x60;: the URI to all the list of origins.         - &#x60;&#x60;lists&#x60;&#x60;: list of lists that the origin is using.             - &#x60;&#x60;self&#x60;&#x60;: the URI to the individual information of the list.             - &#x60;&#x60;origin&#x60;&#x60;: the protocol and domain of the website that is using the list.             - &#x60;&#x60;status&#x60;&#x60;: the status of the list. It can be &#x60;&#x60;ACTIVE&#x60;&#x60; or &#x60;&#x60;INACTIVE&#x60;&#x60; or &#x60;&#x60;EXPIRED&#x60;&#x60;. If the list is &#x60;&#x60;EXPIRED&#x60;&#x60;            it means that the list is not available anymore if not renewed.             - &#x60;&#x60;expiry&#x60;&#x60;: Unix timestamp in seconds when the list will expire. If it does not exist, it will never expire.             - &#x60;&#x60;created_at&#x60;&#x60;: Unix timestamp in seconds when the list was created.             - &#x60;&#x60;updated_at&#x60;&#x60;: Unix timestamp in seconds when the list was updated.  ### Errors  It will return the API Global errors described in the API description.

### Example

```javascript
import ThreatJammerComUserApi from 'threat_jammer_com_user_api';
let defaultClient = ThreatJammerComUserApi.ApiClient.instance;
// Configure Bearer access token for authorization: HTTPBearer
let HTTPBearer = defaultClient.authentications['HTTPBearer'];
HTTPBearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new ThreatJammerComUserApi.AllowlistDataQueryAndManagementApi();
let resourceType = "resourceType_example"; // String | 
apiInstance.getAllOwnedAllowlistsByResourceTypeV1AllowlistPublicOwnedResourceTypeGet(resourceType, (error, data, response) => {
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


## getAllPrivateAllowlistsByResourceTypeV1AllowlistPrivateAllResourceTypeGet

> PrivateAclGroupListCollectionOutput getAllPrivateAllowlistsByResourceTypeV1AllowlistPrivateAllResourceTypeGet(resourceType)

Get the set of private allowlists of the user by resource type.

### What Obtain the set of private allow lists of the user available in the service filtering by resource type. It can be &#x60;&#x60;CIDR&#x60;&#x60;, &#x60;&#x60;AS&#x60;&#x60;, &#x60;&#x60;COUNTRY&#x60;&#x60;, &#x60;&#x60;CONTINENT&#x60;&#x60; or &#x60;&#x60;DATACENTER_ID&#x60;&#x60;  ### Parameters The &#x60;&#x60;resource type&#x60;&#x60; to filter. The values can be &#x60;&#x60;CIDR&#x60;&#x60;, &#x60;&#x60;AS&#x60;&#x60;, &#x60;&#x60;COUNTRY&#x60;&#x60;, &#x60;&#x60;CONTINENT&#x60;&#x60; or &#x60;&#x60;DATACENTER_ID&#x60;&#x60;.  ### Result The result is a JSON object with a list of the following JSON objects: - &#x60;&#x60;self&#x60;&#x60;: the URI to the status of all the lists. - &#x60;&#x60;lists&#x60;&#x60;: a list of JSON objects with the available lists:     - &#x60;&#x60;self&#x60;&#x60;: the URI to individual information of the list.     - &#x60;&#x60;name&#x60;&#x60;: A human readable name of the list.     - &#x60;&#x60;description&#x60;&#x60;: A long detailed information about what the list contains and how it is used.     - &#x60;&#x60;resource_type&#x60;&#x60;: The type of the list. It can be &#x60;&#x60;CIDR&#x60;&#x60;, &#x60;&#x60;AS&#x60;&#x60;, &#x60;&#x60;COUNTRY&#x60;&#x60;, &#x60;&#x60;CONTINENT&#x60;&#x60; or &#x60;&#x60;DATACENTER_ID&#x60;&#x60;.     - &#x60;&#x60;list_type&#x60;&#x60;: The type of the list. It can be &#x60;&#x60;ALLOW&#x60;&#x60; or &#x60;&#x60;DENY&#x60;&#x60;.     - &#x60;&#x60;created_at&#x60;&#x60;: Unix timestamp in seconds when the list was created.     - &#x60;&#x60;updated_at&#x60;&#x60;: Unix timestamp in seconds when the list was updated.     - &#x60;&#x60;expiry&#x60;&#x60;: Unix timestamp in seconds when the list will expire. If it does not exist, it will never expire.     - &#x60;&#x60;origins&#x60;&#x60;: list of websites that are using the list as a allowlist.         - &#x60;&#x60;self&#x60;&#x60;: the URI to all the list of origins.         - &#x60;&#x60;lists&#x60;&#x60;: list of lists that the origin is using.             - &#x60;&#x60;self&#x60;&#x60;: the URI to the individual information of the list.             - &#x60;&#x60;origin&#x60;&#x60;: the protocol and domain of the website that is using the list.             - &#x60;&#x60;status&#x60;&#x60;: the status of the list. It can be &#x60;&#x60;ACTIVE&#x60;&#x60; or &#x60;&#x60;INACTIVE&#x60;&#x60; or &#x60;&#x60;EXPIRED&#x60;&#x60;. If the list is &#x60;&#x60;EXPIRED&#x60;&#x60; it means that the list is not available anymore if not renewed.             - &#x60;&#x60;expiry&#x60;&#x60;: Unix timestamp in seconds when the list will expire. If it does not exist, it will never expire.             - &#x60;&#x60;created_at&#x60;&#x60;: Unix timestamp in seconds when the list was created.             - &#x60;&#x60;updated_at&#x60;&#x60;: Unix timestamp in seconds when the list was updated.  ### Errors  - If the resource type is not valid, it will return a &#x60;&#x60;400&#x60;&#x60; error.  It will also return the API Global errors described in the API description.

### Example

```javascript
import ThreatJammerComUserApi from 'threat_jammer_com_user_api';
let defaultClient = ThreatJammerComUserApi.ApiClient.instance;
// Configure Bearer access token for authorization: HTTPBearer
let HTTPBearer = defaultClient.authentications['HTTPBearer'];
HTTPBearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new ThreatJammerComUserApi.AllowlistDataQueryAndManagementApi();
let resourceType = "resourceType_example"; // String | 
apiInstance.getAllPrivateAllowlistsByResourceTypeV1AllowlistPrivateAllResourceTypeGet(resourceType, (error, data, response) => {
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


## getAllPrivateAllowlistsV1AllowlistPrivateAllGet

> PrivateAclGroupListCollectionOutput getAllPrivateAllowlistsV1AllowlistPrivateAllGet()

Get the set of private allowlists of the user.

### What Obtain the set of private allow lists of the user available in the service.  ### Parameters No parameters  ### Result The result is a JSON object with a list of the following JSON objects: - &#x60;&#x60;self&#x60;&#x60;: the URI to the status of all the lists. - &#x60;&#x60;lists&#x60;&#x60;: a list of JSON objects with the available lists:     - &#x60;&#x60;self&#x60;&#x60;: the URI to individual information of the list.     - &#x60;&#x60;name&#x60;&#x60;: A human readable name of the list.     - &#x60;&#x60;description&#x60;&#x60;: A long detailed information about what the list contains and how it is used.     - &#x60;&#x60;resource_type&#x60;&#x60;: The type of the list. It can be &#x60;&#x60;CIDR&#x60;&#x60;, &#x60;&#x60;AS&#x60;&#x60;, &#x60;&#x60;COUNTRY&#x60;&#x60;, &#x60;&#x60;CONTINENT&#x60;&#x60; or &#x60;&#x60;DATACENTER_ID&#x60;&#x60;.     - &#x60;&#x60;list_type&#x60;&#x60;: The type of the list. It can be &#x60;&#x60;ALLOW&#x60;&#x60; or &#x60;&#x60;DENY&#x60;&#x60;.     - &#x60;&#x60;created_at&#x60;&#x60;: Unix timestamp in seconds when the list was created.     - &#x60;&#x60;updated_at&#x60;&#x60;: Unix timestamp in seconds when the list was updated.     - &#x60;&#x60;expiry&#x60;&#x60;: Unix timestamp in seconds when the list will expire. If it does not exist, it will never expire.     - &#x60;&#x60;origins&#x60;&#x60;: list of websites that are using the list as a allowlist.         - &#x60;&#x60;self&#x60;&#x60;: the URI to all the list of origins.         - &#x60;&#x60;lists&#x60;&#x60;: list of lists that the origin is using.             - &#x60;&#x60;self&#x60;&#x60;: the URI to the individual information of the list.             - &#x60;&#x60;origin&#x60;&#x60;: the protocol and domain of the website that is using the list.             - &#x60;&#x60;status&#x60;&#x60;: the status of the list. It can be &#x60;&#x60;ACTIVE&#x60;&#x60; or &#x60;&#x60;INACTIVE&#x60;&#x60; or &#x60;&#x60;EXPIRED&#x60;&#x60;. If the list is &#x60;&#x60;EXPIRED&#x60;&#x60; it means that the list is not available anymore if not renewed.             - &#x60;&#x60;expiry&#x60;&#x60;: Unix timestamp in seconds when the list will expire. If it does not exist, it will never expire.             - &#x60;&#x60;created_at&#x60;&#x60;: Unix timestamp in seconds when the list was created.             - &#x60;&#x60;updated_at&#x60;&#x60;: Unix timestamp in seconds when the list was updated.  ### Errors  It will return the API Global errors described in the API description.

### Example

```javascript
import ThreatJammerComUserApi from 'threat_jammer_com_user_api';
let defaultClient = ThreatJammerComUserApi.ApiClient.instance;
// Configure Bearer access token for authorization: HTTPBearer
let HTTPBearer = defaultClient.authentications['HTTPBearer'];
HTTPBearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new ThreatJammerComUserApi.AllowlistDataQueryAndManagementApi();
apiInstance.getAllPrivateAllowlistsV1AllowlistPrivateAllGet((error, data, response) => {
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


## getAllPublicAllowlistsByResourceTypeV1AllowlistPublicAllResourceTypeGet

> PublicAclGroupListCollectionOutput getAllPublicAllowlistsByResourceTypeV1AllowlistPublicAllResourceTypeGet(resourceType)

Get the set of public allowlists by resource type.

### What Obtain the set of public allow lists available in the service and also which ones are already selected by the user and wich ones are not filtering by the resource type.  ### Parameters The &#x60;&#x60;resource type&#x60;&#x60; to filter. The values can be &#x60;&#x60;CIDR&#x60;&#x60;, &#x60;&#x60;AS&#x60;&#x60;, &#x60;&#x60;COUNTRY&#x60;&#x60;, &#x60;&#x60;CONTINENT&#x60;&#x60; or &#x60;&#x60;DATACENTER_ID&#x60;&#x60;.  ### Result The result is a JSON object with a list of the following JSON objects: - &#x60;&#x60;self&#x60;&#x60;: the URI to the status of all the lists. - &#x60;&#x60;lists&#x60;&#x60;: a list of JSON objects with the available lists:     - &#x60;&#x60;self&#x60;&#x60;: the URI to individual information of the list.     - &#x60;&#x60;name&#x60;&#x60;: A human readable name of the list.     - &#x60;&#x60;description&#x60;&#x60;: A long detailed information about what the list contains and how it is used.     - &#x60;&#x60;resource_type&#x60;&#x60;: The type of the list. It can be &#x60;&#x60;CIDR&#x60;&#x60;, &#x60;&#x60;AS&#x60;&#x60;, &#x60;&#x60;COUNTRY&#x60;&#x60;, &#x60;&#x60;CONTINENT&#x60;&#x60; or &#x60;&#x60;DATACENTER_ID&#x60;&#x60;.     - &#x60;&#x60;list_type&#x60;&#x60;: The type of the list. It can be &#x60;&#x60;ALLOW&#x60;&#x60; or &#x60;&#x60;DENY&#x60;&#x60;.     - &#x60;&#x60;status&#x60;&#x60;: The status of the list. It can be &#x60;&#x60;ACTIVE&#x60;&#x60; or &#x60;&#x60;INACTIVE&#x60;&#x60; or &#x60;&#x60;EXPIRED&#x60;&#x60;. If the list is &#x60;&#x60;EXPIRED&#x60;&#x60;    it means that the list is not available anymore if not renewed.     - &#x60;&#x60;created_at&#x60;&#x60;: Unix timestamp in seconds when the list was created.     - &#x60;&#x60;updated_at&#x60;&#x60;: Unix timestamp in seconds when the list was updated.  If the list is already selected by the user, the JSON object will also contain the following fields: - &#x60;&#x60;expiry&#x60;&#x60;: Unix timestamp in seconds when the list will expire. If it does not exist, it will never expire. - &#x60;&#x60;origins&#x60;&#x60;: list of websites that are using the list as an allowlist.     - &#x60;&#x60;self&#x60;&#x60;: the URI to all the list of origins.     - &#x60;&#x60;lists&#x60;&#x60;: list of lists that the origin is using.         - &#x60;&#x60;self&#x60;&#x60;: the URI to the individual information of the list.         - &#x60;&#x60;origin&#x60;&#x60;: the protocol and domain of the website that is using the list.         - &#x60;&#x60;status&#x60;&#x60;: the status of the list. It can be &#x60;&#x60;ACTIVE&#x60;&#x60; or &#x60;&#x60;INACTIVE&#x60;&#x60; or &#x60;&#x60;EXPIRED&#x60;&#x60;. If the list is &#x60;&#x60;EXPIRED&#x60;&#x60;        it means that the list is not available anymore if not renewed.         - &#x60;&#x60;expiry&#x60;&#x60;: Unix timestamp in seconds when the list will expire. If it does not exist, it will never expire.         - &#x60;&#x60;created_at&#x60;&#x60;: Unix timestamp in seconds when the list was created.         - &#x60;&#x60;updated_at&#x60;&#x60;: Unix timestamp in seconds when the list was updated.  ### Errors  It will return the API Global errors described in the API description.

### Example

```javascript
import ThreatJammerComUserApi from 'threat_jammer_com_user_api';
let defaultClient = ThreatJammerComUserApi.ApiClient.instance;
// Configure Bearer access token for authorization: HTTPBearer
let HTTPBearer = defaultClient.authentications['HTTPBearer'];
HTTPBearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new ThreatJammerComUserApi.AllowlistDataQueryAndManagementApi();
let resourceType = "resourceType_example"; // String | 
apiInstance.getAllPublicAllowlistsByResourceTypeV1AllowlistPublicAllResourceTypeGet(resourceType, (error, data, response) => {
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


## getAllPublicAllowlistsV1AllowlistPublicAllGet

> PublicAclGroupListCollectionOutput getAllPublicAllowlistsV1AllowlistPublicAllGet()

Get the set of public allowlists.

### What Obtain the set of public allow lists available in the service and also which ones are already selected by the user and wich ones are not.  ### Parameters No parameters  ### Result The result is a JSON object with a list of the following JSON objects: - &#x60;&#x60;self&#x60;&#x60;: the URI to the status of all the lists. - &#x60;&#x60;lists&#x60;&#x60;: a list of JSON objects with the available lists:     - &#x60;&#x60;self&#x60;&#x60;: the URI to individual information of the list.     - &#x60;&#x60;name&#x60;&#x60;: A human readable name of the list.     - &#x60;&#x60;description&#x60;&#x60;: A long detailed information about what the list contains and how it is used.     - &#x60;&#x60;resource_type&#x60;&#x60;: The type of the list. It can be &#x60;&#x60;CIDR&#x60;&#x60;, &#x60;&#x60;AS&#x60;&#x60;, &#x60;&#x60;COUNTRY&#x60;&#x60;, &#x60;&#x60;CONTINENT&#x60;&#x60; or &#x60;&#x60;DATACENTER_ID&#x60;&#x60;.     - &#x60;&#x60;list_type&#x60;&#x60;: The type of the list. It can be &#x60;&#x60;ALLOW&#x60;&#x60; or &#x60;&#x60;DENY&#x60;&#x60;.     - &#x60;&#x60;status&#x60;&#x60;: The status of the list. It can be &#x60;&#x60;ACTIVE&#x60;&#x60; or &#x60;&#x60;INACTIVE&#x60;&#x60; or &#x60;&#x60;EXPIRED&#x60;&#x60;. If the list is &#x60;&#x60;EXPIRED&#x60;&#x60;    it means that the list is not available anymore if not renewed.     - &#x60;&#x60;created_at&#x60;&#x60;: Unix timestamp in seconds when the list was created.     - &#x60;&#x60;updated_at&#x60;&#x60;: Unix timestamp in seconds when the list was updated.  If the list is already selected by the user, the JSON object will also contain the following fields: - &#x60;&#x60;expiry&#x60;&#x60;: Unix timestamp in seconds when the list will expire. If it does not exist, it will never expire. - &#x60;&#x60;origins&#x60;&#x60;: list of websites that are using the list as an allowlist.     - &#x60;&#x60;self&#x60;&#x60;: the URI to all the list of origins.     - &#x60;&#x60;lists&#x60;&#x60;: list of lists that the origin is using.         - &#x60;&#x60;self&#x60;&#x60;: the URI to the individual information of the list.         - &#x60;&#x60;origin&#x60;&#x60;: the protocol and domain of the website that is using the list.         - &#x60;&#x60;status&#x60;&#x60;: the status of the list. It can be &#x60;&#x60;ACTIVE&#x60;&#x60; or &#x60;&#x60;INACTIVE&#x60;&#x60; or &#x60;&#x60;EXPIRED&#x60;&#x60;. If the list is &#x60;&#x60;EXPIRED&#x60;&#x60;        it means that the list is not available anymore if not renewed.         - &#x60;&#x60;expiry&#x60;&#x60;: Unix timestamp in seconds when the list will expire. If it does not exist, it will never expire.         - &#x60;&#x60;created_at&#x60;&#x60;: Unix timestamp in seconds when the list was created.         - &#x60;&#x60;updated_at&#x60;&#x60;: Unix timestamp in seconds when the list was updated.  ### Errors  It will return the API Global errors described in the API description.

### Example

```javascript
import ThreatJammerComUserApi from 'threat_jammer_com_user_api';
let defaultClient = ThreatJammerComUserApi.ApiClient.instance;
// Configure Bearer access token for authorization: HTTPBearer
let HTTPBearer = defaultClient.authentications['HTTPBearer'];
HTTPBearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new ThreatJammerComUserApi.AllowlistDataQueryAndManagementApi();
apiInstance.getAllPublicAllowlistsV1AllowlistPublicAllGet((error, data, response) => {
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


## getAllowlistContentV1AllowlistPrivateAllowlistIdContentGet

> PrivateAclListCollectionOutput getAllowlistContentV1AllowlistPrivateAllowlistIdContentGet(allowlistId, opts)

Get the content of a private allowlist of the user.

### What Returns the content of the private allowlist of the user. The content can be CIDRs, ASNs, countries, continents or    datacenter IDs.  ### Parameters Pass the private allowlist ID as query parameter.  The following pagination parameters are required as query string parameters: - &#x60;&#x60;page&#x60;&#x60;: (Optional) the page number to retrieve. The first page is 1. Default is 1. - &#x60;&#x60;page_size&#x60;&#x60;: (Optional) the number of items per page. Default is 20.   ### Result The result is a JSON object with the following structure: - &#x60;&#x60;self&#x60;&#x60;: the URI to the content of the list. - &#x60;&#x60;cidrs&#x60;&#x60;: (Optional) list of CIDRs in the list. - &#x60;&#x60;asns&#x60;&#x60;: (Optional) list of ASNs in the list. - &#x60;&#x60;countries&#x60;&#x60;: (Optional) list of countries in the list. - &#x60;&#x60;continents&#x60;&#x60;: (Optional) list of continents in the list. - &#x60;&#x60;datacenters&#x60;&#x60;: (Optional) list of datacenters in the list.  ### Errors  - If the allow list is not a valid UUID, it will return a &#x60;&#x60;422&#x60;&#x60; (Unprocessable Entity) error. - If the private allowlist ID does not exist, it will return a &#x60;&#x60;404&#x60;&#x60; (Not found) error.  It will also return the API Global errors described in the API description.

### Example

```javascript
import ThreatJammerComUserApi from 'threat_jammer_com_user_api';
let defaultClient = ThreatJammerComUserApi.ApiClient.instance;
// Configure Bearer access token for authorization: HTTPBearer
let HTTPBearer = defaultClient.authentications['HTTPBearer'];
HTTPBearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new ThreatJammerComUserApi.AllowlistDataQueryAndManagementApi();
let allowlistId = "allowlistId_example"; // String | 
let opts = {
  'page': 1, // Number | The page to be returned
  'pageSize': 20 // Number | The number of items per page
};
apiInstance.getAllowlistContentV1AllowlistPrivateAllowlistIdContentGet(allowlistId, opts, (error, data, response) => {
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
 **allowlistId** | **String**|  | 
 **page** | **Number**| The page to be returned | [optional] [default to 1]
 **pageSize** | **Number**| The number of items per page | [optional] [default to 20]

### Return type

[**PrivateAclListCollectionOutput**](PrivateAclListCollectionOutput.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPublicAllowlistsOwnedByTheUserV1AllowlistPublicOwnedGet

> PublicAclGroupListCollectionOutput getPublicAllowlistsOwnedByTheUserV1AllowlistPublicOwnedGet()

Get the set of owned allowlists.

### What Obtain the set of public allow lists available in the service selected by the user.  ### Parameters No parameters  ### Result The result is a JSON object with a list of the following JSON objects: - &#x60;&#x60;self&#x60;&#x60;: the URI to the status of all the lists. - &#x60;&#x60;lists&#x60;&#x60;: a list of JSON objects with the available lists:     - &#x60;&#x60;self&#x60;&#x60;: the URI to individual information of the list.     - &#x60;&#x60;name&#x60;&#x60;: A human readable name of the list.     - &#x60;&#x60;description&#x60;&#x60;: A long detailed information about what the list contains and how it is used.     - &#x60;&#x60;resource_type&#x60;&#x60;: The type of the list. It can be &#x60;&#x60;CIDR&#x60;&#x60;, &#x60;&#x60;AS&#x60;&#x60;, &#x60;&#x60;COUNTRY&#x60;&#x60;, &#x60;&#x60;CONTINENT&#x60;&#x60; or &#x60;&#x60;DATACENTER_ID&#x60;&#x60;.     - &#x60;&#x60;list_type&#x60;&#x60;: The type of the list. It can be &#x60;&#x60;ALLOW&#x60;&#x60; or &#x60;&#x60;DENY&#x60;&#x60;.     - &#x60;&#x60;status&#x60;&#x60;: The status of the list. It can be &#x60;&#x60;ACTIVE&#x60;&#x60; or &#x60;&#x60;INACTIVE&#x60;&#x60; or &#x60;&#x60;EXPIRED&#x60;&#x60;. If the list is &#x60;&#x60;EXPIRED&#x60;&#x60;    it means that the list is not available anymore if not renewed.     - &#x60;&#x60;created_at&#x60;&#x60;: Unix timestamp in seconds when the list was created.     - &#x60;&#x60;updated_at&#x60;&#x60;: Unix timestamp in seconds when the list was updated.     - &#x60;&#x60;expiry&#x60;&#x60;: Unix timestamp in seconds when the list will expire. If it does not exist, it will never expire.     - &#x60;&#x60;origins&#x60;&#x60;: list of websites that are using the list as an allowlist.         - &#x60;&#x60;self&#x60;&#x60;: the URI to all the list of origins.         - &#x60;&#x60;lists&#x60;&#x60;: list of lists that the origin is using.             - &#x60;&#x60;self&#x60;&#x60;: the URI to the individual information of the list.             - &#x60;&#x60;origin&#x60;&#x60;: the protocol and domain of the website that is using the list.             - &#x60;&#x60;status&#x60;&#x60;: the status of the list. It can be &#x60;&#x60;ACTIVE&#x60;&#x60; or &#x60;&#x60;INACTIVE&#x60;&#x60; or &#x60;&#x60;EXPIRED&#x60;&#x60;. If the list is &#x60;&#x60;EXPIRED&#x60;&#x60;            it means that the list is not available anymore if not renewed.             - &#x60;&#x60;expiry&#x60;&#x60;: Unix timestamp in seconds when the list will expire. If it does not exist, it will never expire.             - &#x60;&#x60;created_at&#x60;&#x60;: Unix timestamp in seconds when the list was created.             - &#x60;&#x60;updated_at&#x60;&#x60;: Unix timestamp in seconds when the list was updated.  ### Errors  It will return the API Global errors described in the API description.

### Example

```javascript
import ThreatJammerComUserApi from 'threat_jammer_com_user_api';
let defaultClient = ThreatJammerComUserApi.ApiClient.instance;
// Configure Bearer access token for authorization: HTTPBearer
let HTTPBearer = defaultClient.authentications['HTTPBearer'];
HTTPBearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new ThreatJammerComUserApi.AllowlistDataQueryAndManagementApi();
apiInstance.getPublicAllowlistsOwnedByTheUserV1AllowlistPublicOwnedGet((error, data, response) => {
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


## getSingleAllowlistV1AllowlistPrivateAllowlistIdGet

> PrivateAclGroupListOutput getSingleAllowlistV1AllowlistPrivateAllowlistIdGet(allowlistId)

Get the details of a specific private allowlist of the user.

### What Obtain the details of the private allow list of the user available in the service.  ### Parameters Pass the private allowlist ID as query parameter.  ### Result The result is a JSON object with the following structure: - &#x60;&#x60;self&#x60;&#x60;: the URI to individual information of the list. - &#x60;&#x60;name&#x60;&#x60;: A human readable name of the list. - &#x60;&#x60;description&#x60;&#x60;: A long detailed information about what the list contains and how it is used. - &#x60;&#x60;resource_type&#x60;&#x60;: The type of the list. It can be &#x60;&#x60;CIDR&#x60;&#x60;, &#x60;&#x60;AS&#x60;&#x60;, &#x60;&#x60;COUNTRY&#x60;&#x60;, &#x60;&#x60;CONTINENT&#x60;&#x60; or &#x60;&#x60;DATACENTER_ID&#x60;&#x60;. - &#x60;&#x60;list_type&#x60;&#x60;: The type of the list. It can be &#x60;&#x60;ALLOW&#x60;&#x60; or &#x60;&#x60;DENY&#x60;&#x60;. - &#x60;&#x60;created_at&#x60;&#x60;: Unix timestamp in seconds when the list was created. - &#x60;&#x60;updated_at&#x60;&#x60;: Unix timestamp in seconds when the list was updated. - &#x60;&#x60;expiry&#x60;&#x60;: Unix timestamp in seconds when the list will expire. If it does not exist, it will never expire. - &#x60;&#x60;origins&#x60;&#x60;: list of websites that are using the list as a allowlist.     - &#x60;&#x60;self&#x60;&#x60;: the URI to all the list of origins.     - &#x60;&#x60;lists&#x60;&#x60;: list of lists that the origin is using.         - &#x60;&#x60;self&#x60;&#x60;: the URI to the individual information of the list.         - &#x60;&#x60;origin&#x60;&#x60;: the protocol and domain of the website that is using the list.         - &#x60;&#x60;status&#x60;&#x60;: the status of the list. It can be &#x60;&#x60;ACTIVE&#x60;&#x60; or &#x60;&#x60;INACTIVE&#x60;&#x60; or &#x60;&#x60;EXPIRED&#x60;&#x60;. If the list is &#x60;&#x60;EXPIRED&#x60;&#x60; it means that the list is not available anymore if not renewed.         - &#x60;&#x60;expiry&#x60;&#x60;: Unix timestamp in seconds when the list will expire. If it does not exist, it will never expire.         - &#x60;&#x60;created_at&#x60;&#x60;: Unix timestamp in seconds when the list was created.         - &#x60;&#x60;updated_at&#x60;&#x60;: Unix timestamp in seconds when the list was updated.  ### Errors  - If the allow list is not a valid UUID, it will return a 422 error. - If the private allowlist ID does not exist, it will return a &#x60;&#x60;404&#x60;&#x60; error.  It will also return the API Global errors described in the API description.

### Example

```javascript
import ThreatJammerComUserApi from 'threat_jammer_com_user_api';
let defaultClient = ThreatJammerComUserApi.ApiClient.instance;
// Configure Bearer access token for authorization: HTTPBearer
let HTTPBearer = defaultClient.authentications['HTTPBearer'];
HTTPBearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new ThreatJammerComUserApi.AllowlistDataQueryAndManagementApi();
let allowlistId = "allowlistId_example"; // String | 
apiInstance.getSingleAllowlistV1AllowlistPrivateAllowlistIdGet(allowlistId, (error, data, response) => {
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
 **allowlistId** | **String**|  | 

### Return type

[**PrivateAclGroupListOutput**](PrivateAclGroupListOutput.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSingleAllowlistV1AllowlistPublicAllowlistIdGet

> PublicAclGroupListOutput getSingleAllowlistV1AllowlistPublicAllowlistIdGet(allowlistId)

Get the details of the allowlist.

### What Obtain the details of an allow list available in the service.  ### Parameters No parameters  ### Result The result is a JSON object with a list of the following JSON objects: - &#x60;&#x60;self&#x60;&#x60;: the URI to individual information of the list. - &#x60;&#x60;name&#x60;&#x60;: A human readable name of the list. - &#x60;&#x60;description&#x60;&#x60;: A long detailed information about what the list contains and how it is used. - &#x60;&#x60;resource_type&#x60;&#x60;: The type of the list. It can be &#x60;&#x60;CIDR&#x60;&#x60;, &#x60;&#x60;AS&#x60;&#x60;, &#x60;&#x60;COUNTRY&#x60;&#x60;, &#x60;&#x60;CONTINENT&#x60;&#x60; or &#x60;&#x60;DATACENTER_ID&#x60;&#x60;. - &#x60;&#x60;list_type&#x60;&#x60;: The type of the list. It can be &#x60;&#x60;ALLOW&#x60;&#x60; or &#x60;&#x60;DENY&#x60;&#x60;. - &#x60;&#x60;status&#x60;&#x60;: The status of the list. It can be &#x60;&#x60;ACTIVE&#x60;&#x60; or &#x60;&#x60;INACTIVE&#x60;&#x60; or &#x60;&#x60;EXPIRED&#x60;&#x60;. If the list is &#x60;&#x60;EXPIRED&#x60;&#x60;it means that the list is not available anymore if not renewed. - &#x60;&#x60;created_at&#x60;&#x60;: Unix timestamp in seconds when the list was created. - &#x60;&#x60;updated_at&#x60;&#x60;: Unix timestamp in seconds when the list was updated.  If the list is already selected by the user, the JSON object will also contain the following fields:     - &#x60;&#x60;expiry&#x60;&#x60;: Unix timestamp in seconds when the list will expire. If it does not exist, it will never expire.     - &#x60;&#x60;origins&#x60;&#x60;: list of websites that are using the list as an allowlist.         - &#x60;&#x60;self&#x60;&#x60;: the URI to all the list of origins.         - &#x60;&#x60;lists&#x60;&#x60;: list of lists that the origin is using.             - &#x60;&#x60;self&#x60;&#x60;: the URI to the individual information of the list.             - &#x60;&#x60;origin&#x60;&#x60;: the protocol and domain of the website that is using the list.             - &#x60;&#x60;status&#x60;&#x60;: the status of the list. It can be &#x60;&#x60;ACTIVE&#x60;&#x60; or &#x60;&#x60;INACTIVE&#x60;&#x60; or &#x60;&#x60;EXPIRED&#x60;&#x60;. If the list is &#x60;&#x60;EXPIRED&#x60;&#x60;            it means that the list is not available anymore if not renewed.             - &#x60;&#x60;expiry&#x60;&#x60;: Unix timestamp in seconds when the list will expire. If it does not exist, it will never expire.             - &#x60;&#x60;created_at&#x60;&#x60;: Unix timestamp in seconds when the list was created.             - &#x60;&#x60;updated_at&#x60;&#x60;: Unix timestamp in seconds when the list was updated.  ### Errors  If the list does not exist, it will return a 404 error.  It will return the API Global errors described in the API description.

### Example

```javascript
import ThreatJammerComUserApi from 'threat_jammer_com_user_api';
let defaultClient = ThreatJammerComUserApi.ApiClient.instance;
// Configure Bearer access token for authorization: HTTPBearer
let HTTPBearer = defaultClient.authentications['HTTPBearer'];
HTTPBearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new ThreatJammerComUserApi.AllowlistDataQueryAndManagementApi();
let allowlistId = "allowlistId_example"; // String | 
apiInstance.getSingleAllowlistV1AllowlistPublicAllowlistIdGet(allowlistId, (error, data, response) => {
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
 **allowlistId** | **String**|  | 

### Return type

[**PublicAclGroupListOutput**](PublicAclGroupListOutput.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## queryResourceAllowlistsV1AllowlistPublicIpAddressGet

> AclListCollectionOutput queryResourceAllowlistsV1AllowlistPublicIpAddressGet(address)

Get the different public allowlists where the IP address was found.

### What Obtain the list of all the different public allowlists where the IP address entered by the user is. The public allowlists are the ones activated by the user, but managed by Threatjammer administrators.  ### Parameters The endpoint accepts the &#x60;address&#x60; parameter as query string.  ### Result The result is a JSON object with a list of the following JSON objects: - &#x60;&#x60;self&#x60;&#x60;: the URI to individual status. - &#x60;&#x60;cidrs&#x60;&#x60;: the URI of the lists of CIDRs where the IP was found. - &#x60;&#x60;country&#x60;&#x60;: the URIs where the lists of countries where the IP address was found - &#x60;&#x60;continent&#x60;&#x60;: the URI where the continent where the IP address was found. - &#x60;&#x60;asn&#x60;&#x60;: the URIs where the list of continents of the ASN where the IP address was found. - &#x60;&#x60;datacenter&#x60;&#x60;: the URIs of the lists of datacenters where the IP address was found. If not found, the result is an empty string.  ### Errors - a &#x60;422 Unprocessable Entity&#x60; error if the IP address was malformed.  It will also return the API Global errors described in the API description.

### Example

```javascript
import ThreatJammerComUserApi from 'threat_jammer_com_user_api';
let defaultClient = ThreatJammerComUserApi.ApiClient.instance;
// Configure Bearer access token for authorization: HTTPBearer
let HTTPBearer = defaultClient.authentications['HTTPBearer'];
HTTPBearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new ThreatJammerComUserApi.AllowlistDataQueryAndManagementApi();
let address = new ThreatJammerComUserApi.Address(); // Address | 
apiInstance.queryResourceAllowlistsV1AllowlistPublicIpAddressGet(address, (error, data, response) => {
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


## queryResourceDenylistsV1AllowlistPrivateIpAddressGet

> AclListCollectionOutput queryResourceDenylistsV1AllowlistPrivateIpAddressGet(address)

Get the different private allowlists where the IP address was found.

### What Obtain the list of all the different private allowlists where the IP address entered by the user. The allowlisted forbidden datasets are the ones submitted manually by the user from files or indidual items.  ### Parameters The endpoint accepts the &#x60;address&#x60; parameter as query string.  ### Result The result is a JSON object with a list of the following JSON objects: - &#x60;&#x60;self&#x60;&#x60;: the URI to individual status. - &#x60;&#x60;cidrs&#x60;&#x60;: the URI of the lists of CIDRs where the IP was found. - &#x60;&#x60;country&#x60;&#x60;: the URIs where the lists of countries where the IP address was found - &#x60;&#x60;continent&#x60;&#x60;: the URI where the continent where the IP address was found. - &#x60;&#x60;asn&#x60;&#x60;: the URIs where the list of continents of the ASN where the IP address was found. - &#x60;&#x60;datacenter&#x60;&#x60;: the URIs of the lists of datacenters where the IP address was found. If not found, the result is an empty string. - &#x60;&#x60;reported&#x60;&#x60;: the URI of the information of the IP address reported by the user. For allowlist should be empty.  ### Errors - a &#x60;422 Unprocessable Entity&#x60; error if the IP address was malformed.  It will also return the API Global errors described in the API description.

### Example

```javascript
import ThreatJammerComUserApi from 'threat_jammer_com_user_api';
let defaultClient = ThreatJammerComUserApi.ApiClient.instance;
// Configure Bearer access token for authorization: HTTPBearer
let HTTPBearer = defaultClient.authentications['HTTPBearer'];
HTTPBearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new ThreatJammerComUserApi.AllowlistDataQueryAndManagementApi();
let address = new ThreatJammerComUserApi.Address(); // Address | 
apiInstance.queryResourceDenylistsV1AllowlistPrivateIpAddressGet(address, (error, data, response) => {
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


## updatePrivateAllowlistOfTheUserV1AllowlistPrivateAllowlistIdPut

> Object updatePrivateAllowlistOfTheUserV1AllowlistPrivateAllowlistIdPut(allowlistId, opts)

Update the information of an existing private allowlist of the user.

### What Updates the information that describes the allowlist of the user in the system. The parameters that can be modified are:  - name  - description  - tags  - expiry  This is an asynchronous operation. It can take several seconds until the operation completes, but the request will immediately return a 202 Accepted response.  ### Parameters In the query string the ID of the private allow list to delete.  In the body the following parameters: - &#x60;&#x60;name&#x60;&#x60;: (Optional) A human readable name of the list. - &#x60;&#x60;description&#x60;&#x60;: (Optional) A long detailed information about what the list contains and how it is used. - &#x60;&#x60;tags&#x60;&#x60;: (Optional) A list of tags that describe the list. - &#x60;&#x60;expiry&#x60;&#x60;: (Optional) Unix timestamp in seconds when the list will expire. If it does not exist, it will never expire.  ### Result It should always return a 202 Accepted response with an empty body.  ### Errors  - If the list does not exist, it will return a &#x60;404&#x60; (Not found) error. - If the list is a default list, it will return a &#x60;403&#x60; (Forbidden) error. - If the allow list is not a valid UUID, it will return a &#x60;422&#x60; (Unprocessable Entity) error. - If the expiry is not a valid timestamp, it will return a &#x60;422&#x60; (Unprocessable Entity) error. - If the expiry is in the past, it will return a &#x60;400&#x60; (Bad Request) error. - If the name is not a string, it will return a &#x60;422&#x60; (Unprocessable Entity) error. - If the description is not a string, it will return a &#x60;422&#x60; (Unprocessable Entity) error.  It will return the API Global errors described in the API description.

### Example

```javascript
import ThreatJammerComUserApi from 'threat_jammer_com_user_api';
let defaultClient = ThreatJammerComUserApi.ApiClient.instance;
// Configure Bearer access token for authorization: HTTPBearer
let HTTPBearer = defaultClient.authentications['HTTPBearer'];
HTTPBearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new ThreatJammerComUserApi.AllowlistDataQueryAndManagementApi();
let allowlistId = "allowlistId_example"; // String | 
let opts = {
  'bodyUpdatePrivateAllowlistOfTheUserV1AllowlistPrivateAllowlistIdPut': new ThreatJammerComUserApi.BodyUpdatePrivateAllowlistOfTheUserV1AllowlistPrivateAllowlistIdPut() // BodyUpdatePrivateAllowlistOfTheUserV1AllowlistPrivateAllowlistIdPut | 
};
apiInstance.updatePrivateAllowlistOfTheUserV1AllowlistPrivateAllowlistIdPut(allowlistId, opts, (error, data, response) => {
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
 **allowlistId** | **String**|  | 
 **bodyUpdatePrivateAllowlistOfTheUserV1AllowlistPrivateAllowlistIdPut** | [**BodyUpdatePrivateAllowlistOfTheUserV1AllowlistPrivateAllowlistIdPut**](BodyUpdatePrivateAllowlistOfTheUserV1AllowlistPrivateAllowlistIdPut.md)|  | [optional] 

### Return type

**Object**

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updatePrivateContentOfTheAllowlistOfTheUserV1AllowlistPrivateAllowlistIdContentPut

> Object updatePrivateContentOfTheAllowlistOfTheUserV1AllowlistPrivateAllowlistIdContentPut(allowlistId, opts)

Add or remove content of a private allowlist of the user.

### What Add or remove content of a private allowlist of the user. The content can be CIDRs, ASNs, countries, continents or datacenter IDs.  The number of elements allowed in all the lists are limited depending on the plan of the user: - Free: 100 elements - Basic: 1000 elements - Pro: 10000 elements  ### Parameters Pass the private allowlist ID as query parameter.  In the body the following parameters: - &#x60;&#x60;append&#x60;&#x60;: (Optional) Add CIDRs, ASNs, countries, continents or datacenter IDs to add to the list. It&#39;s not possible to mix different resource types in the same list. - &#x60;&#x60;remove&#x60;&#x60;: (Optional) Extract CIDRs, ASNs, countries, continents or datacenter IDs to add to the list. It&#39;s not possible to mix different resource types in the same list.   ### Result If successful, it will return a &#x60;&#x60;202&#x60;&#x60; (Accepted) response with an empty body. The operation is asynchronous,and can take several seconds to complete.  ### Errors  - If the allow list is not a valid UUID, it will return a &#x60;&#x60;422&#x60;&#x60; (Unprocessable Entity) error. - If the private allowlist ID does not exist, it will return a &#x60;&#x60;404&#x60;&#x60; (Not found) error. - If the &#x60;&#x60;append&#x60;&#x60; or &#x60;&#x60;remove&#x60;&#x60; parameters are not processable, it will return a &#x60;&#x60;422&#x60;&#x60; (Unprocessable Entity) error. - If the number of elements in the lists is over the limit, it will return a &#x60;&#x60;413&#x60;&#x60; (Payload Too Large) error.  It will also return the API Global errors described in the API description.

### Example

```javascript
import ThreatJammerComUserApi from 'threat_jammer_com_user_api';
let defaultClient = ThreatJammerComUserApi.ApiClient.instance;
// Configure Bearer access token for authorization: HTTPBearer
let HTTPBearer = defaultClient.authentications['HTTPBearer'];
HTTPBearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new ThreatJammerComUserApi.AllowlistDataQueryAndManagementApi();
let allowlistId = "allowlistId_example"; // String | 
let opts = {
  'bodyUpdatePrivateContentOfTheAllowlistOfTheUserV1AllowlistPrivateAllowlistIdContentPut': new ThreatJammerComUserApi.BodyUpdatePrivateContentOfTheAllowlistOfTheUserV1AllowlistPrivateAllowlistIdContentPut() // BodyUpdatePrivateContentOfTheAllowlistOfTheUserV1AllowlistPrivateAllowlistIdContentPut | 
};
apiInstance.updatePrivateContentOfTheAllowlistOfTheUserV1AllowlistPrivateAllowlistIdContentPut(allowlistId, opts, (error, data, response) => {
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
 **allowlistId** | **String**|  | 
 **bodyUpdatePrivateContentOfTheAllowlistOfTheUserV1AllowlistPrivateAllowlistIdContentPut** | [**BodyUpdatePrivateContentOfTheAllowlistOfTheUserV1AllowlistPrivateAllowlistIdContentPut**](BodyUpdatePrivateContentOfTheAllowlistOfTheUserV1AllowlistPrivateAllowlistIdContentPut.md)|  | [optional] 

### Return type

**Object**

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

