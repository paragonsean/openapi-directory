# AndroidDeviceProvisioningPartnerApi.PartnersApi

All URIs are relative to *https://androiddeviceprovisioning.googleapis.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**androiddeviceprovisioningPartnersCustomersCreate**](PartnersApi.md#androiddeviceprovisioningPartnersCustomersCreate) | **POST** /v1/{parent}/customers | 
[**androiddeviceprovisioningPartnersCustomersList**](PartnersApi.md#androiddeviceprovisioningPartnersCustomersList) | **GET** /v1/partners/{partnerId}/customers | 
[**androiddeviceprovisioningPartnersDevicesClaim**](PartnersApi.md#androiddeviceprovisioningPartnersDevicesClaim) | **POST** /v1/partners/{partnerId}/devices:claim | 
[**androiddeviceprovisioningPartnersDevicesClaimAsync**](PartnersApi.md#androiddeviceprovisioningPartnersDevicesClaimAsync) | **POST** /v1/partners/{partnerId}/devices:claimAsync | 
[**androiddeviceprovisioningPartnersDevicesFindByIdentifier**](PartnersApi.md#androiddeviceprovisioningPartnersDevicesFindByIdentifier) | **POST** /v1/partners/{partnerId}/devices:findByIdentifier | 
[**androiddeviceprovisioningPartnersDevicesFindByOwner**](PartnersApi.md#androiddeviceprovisioningPartnersDevicesFindByOwner) | **POST** /v1/partners/{partnerId}/devices:findByOwner | 
[**androiddeviceprovisioningPartnersDevicesGet**](PartnersApi.md#androiddeviceprovisioningPartnersDevicesGet) | **GET** /v1/{name} | 
[**androiddeviceprovisioningPartnersDevicesGetSimLockState**](PartnersApi.md#androiddeviceprovisioningPartnersDevicesGetSimLockState) | **POST** /v1/partners/{partnerId}/devices:getSimLockState | 
[**androiddeviceprovisioningPartnersDevicesMetadata**](PartnersApi.md#androiddeviceprovisioningPartnersDevicesMetadata) | **POST** /v1/partners/{metadataOwnerId}/devices/{deviceId}/metadata | 
[**androiddeviceprovisioningPartnersDevicesUnclaim**](PartnersApi.md#androiddeviceprovisioningPartnersDevicesUnclaim) | **POST** /v1/partners/{partnerId}/devices:unclaim | 
[**androiddeviceprovisioningPartnersDevicesUnclaimAsync**](PartnersApi.md#androiddeviceprovisioningPartnersDevicesUnclaimAsync) | **POST** /v1/partners/{partnerId}/devices:unclaimAsync | 
[**androiddeviceprovisioningPartnersDevicesUpdateMetadataAsync**](PartnersApi.md#androiddeviceprovisioningPartnersDevicesUpdateMetadataAsync) | **POST** /v1/partners/{partnerId}/devices:updateMetadataAsync | 
[**androiddeviceprovisioningPartnersVendorsCustomersList**](PartnersApi.md#androiddeviceprovisioningPartnersVendorsCustomersList) | **GET** /v1/{parent}/customers | 
[**androiddeviceprovisioningPartnersVendorsList**](PartnersApi.md#androiddeviceprovisioningPartnersVendorsList) | **GET** /v1/{parent}/vendors | 



## androiddeviceprovisioningPartnersCustomersCreate

> Company androiddeviceprovisioningPartnersCustomersCreate(parent, opts)



Creates a customer for zero-touch enrollment. After the method returns successfully, admin and owner roles can manage devices and EMM configs by calling API methods or using their zero-touch enrollment portal. The customer receives an email that welcomes them to zero-touch enrollment and explains how to sign into the portal.

### Example

```javascript
import AndroidDeviceProvisioningPartnerApi from 'android_device_provisioning_partner_api';

let apiInstance = new AndroidDeviceProvisioningPartnerApi.PartnersApi();
let parent = "parent_example"; // String | Required. The parent resource ID in the format `partners/[PARTNER_ID]` that identifies the reseller.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'createCustomerRequest': new AndroidDeviceProvisioningPartnerApi.CreateCustomerRequest() // CreateCustomerRequest | 
};
apiInstance.androiddeviceprovisioningPartnersCustomersCreate(parent, opts, (error, data, response) => {
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
 **parent** | **String**| Required. The parent resource ID in the format &#x60;partners/[PARTNER_ID]&#x60; that identifies the reseller. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **createCustomerRequest** | [**CreateCustomerRequest**](CreateCustomerRequest.md)|  | [optional] 

### Return type

[**Company**](Company.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## androiddeviceprovisioningPartnersCustomersList

> ListCustomersResponse androiddeviceprovisioningPartnersCustomersList(partnerId, opts)



Lists the customers that are enrolled to the reseller identified by the &#x60;partnerId&#x60; argument. This list includes customers that the reseller created and customers that enrolled themselves using the portal.

### Example

```javascript
import AndroidDeviceProvisioningPartnerApi from 'android_device_provisioning_partner_api';

let apiInstance = new AndroidDeviceProvisioningPartnerApi.PartnersApi();
let partnerId = "partnerId_example"; // String | Required. The ID of the reseller partner.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'pageSize': 56, // Number | The maximum number of results to be returned. If not specified or 0, all the records are returned.
  'pageToken': "pageToken_example" // String | A token identifying a page of results returned by the server.
};
apiInstance.androiddeviceprovisioningPartnersCustomersList(partnerId, opts, (error, data, response) => {
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
 **partnerId** | **String**| Required. The ID of the reseller partner. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **pageSize** | **Number**| The maximum number of results to be returned. If not specified or 0, all the records are returned. | [optional] 
 **pageToken** | **String**| A token identifying a page of results returned by the server. | [optional] 

### Return type

[**ListCustomersResponse**](ListCustomersResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## androiddeviceprovisioningPartnersDevicesClaim

> ClaimDeviceResponse androiddeviceprovisioningPartnersDevicesClaim(partnerId, opts)



Claims a device for a customer and adds it to zero-touch enrollment. If the device is already claimed by another customer, the call returns an error.

### Example

```javascript
import AndroidDeviceProvisioningPartnerApi from 'android_device_provisioning_partner_api';

let apiInstance = new AndroidDeviceProvisioningPartnerApi.PartnersApi();
let partnerId = "partnerId_example"; // String | Required. The ID of the reseller partner.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'claimDeviceRequest': new AndroidDeviceProvisioningPartnerApi.ClaimDeviceRequest() // ClaimDeviceRequest | 
};
apiInstance.androiddeviceprovisioningPartnersDevicesClaim(partnerId, opts, (error, data, response) => {
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
 **partnerId** | **String**| Required. The ID of the reseller partner. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **claimDeviceRequest** | [**ClaimDeviceRequest**](ClaimDeviceRequest.md)|  | [optional] 

### Return type

[**ClaimDeviceResponse**](ClaimDeviceResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## androiddeviceprovisioningPartnersDevicesClaimAsync

> Operation androiddeviceprovisioningPartnersDevicesClaimAsync(partnerId, opts)



Claims a batch of devices for a customer asynchronously. Adds the devices to zero-touch enrollment. To learn more, read [Long‑running batch operations](/zero-touch/guides/how-it-works#operations).

### Example

```javascript
import AndroidDeviceProvisioningPartnerApi from 'android_device_provisioning_partner_api';

let apiInstance = new AndroidDeviceProvisioningPartnerApi.PartnersApi();
let partnerId = "partnerId_example"; // String | Required. The ID of the reseller partner.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'claimDevicesRequest': new AndroidDeviceProvisioningPartnerApi.ClaimDevicesRequest() // ClaimDevicesRequest | 
};
apiInstance.androiddeviceprovisioningPartnersDevicesClaimAsync(partnerId, opts, (error, data, response) => {
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
 **partnerId** | **String**| Required. The ID of the reseller partner. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **claimDevicesRequest** | [**ClaimDevicesRequest**](ClaimDevicesRequest.md)|  | [optional] 

### Return type

[**Operation**](Operation.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## androiddeviceprovisioningPartnersDevicesFindByIdentifier

> FindDevicesByDeviceIdentifierResponse androiddeviceprovisioningPartnersDevicesFindByIdentifier(partnerId, opts)



Finds devices by hardware identifiers, such as IMEI.

### Example

```javascript
import AndroidDeviceProvisioningPartnerApi from 'android_device_provisioning_partner_api';

let apiInstance = new AndroidDeviceProvisioningPartnerApi.PartnersApi();
let partnerId = "partnerId_example"; // String | Required. The ID of the reseller partner.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'findDevicesByDeviceIdentifierRequest': new AndroidDeviceProvisioningPartnerApi.FindDevicesByDeviceIdentifierRequest() // FindDevicesByDeviceIdentifierRequest | 
};
apiInstance.androiddeviceprovisioningPartnersDevicesFindByIdentifier(partnerId, opts, (error, data, response) => {
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
 **partnerId** | **String**| Required. The ID of the reseller partner. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **findDevicesByDeviceIdentifierRequest** | [**FindDevicesByDeviceIdentifierRequest**](FindDevicesByDeviceIdentifierRequest.md)|  | [optional] 

### Return type

[**FindDevicesByDeviceIdentifierResponse**](FindDevicesByDeviceIdentifierResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## androiddeviceprovisioningPartnersDevicesFindByOwner

> FindDevicesByOwnerResponse androiddeviceprovisioningPartnersDevicesFindByOwner(partnerId, opts)



Finds devices claimed for customers. The results only contain devices registered to the reseller that&#39;s identified by the &#x60;partnerId&#x60; argument. The customer&#39;s devices purchased from other resellers don&#39;t appear in the results.

### Example

```javascript
import AndroidDeviceProvisioningPartnerApi from 'android_device_provisioning_partner_api';

let apiInstance = new AndroidDeviceProvisioningPartnerApi.PartnersApi();
let partnerId = "partnerId_example"; // String | Required. The ID of the reseller partner.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'findDevicesByOwnerRequest': new AndroidDeviceProvisioningPartnerApi.FindDevicesByOwnerRequest() // FindDevicesByOwnerRequest | 
};
apiInstance.androiddeviceprovisioningPartnersDevicesFindByOwner(partnerId, opts, (error, data, response) => {
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
 **partnerId** | **String**| Required. The ID of the reseller partner. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **findDevicesByOwnerRequest** | [**FindDevicesByOwnerRequest**](FindDevicesByOwnerRequest.md)|  | [optional] 

### Return type

[**FindDevicesByOwnerResponse**](FindDevicesByOwnerResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## androiddeviceprovisioningPartnersDevicesGet

> Device androiddeviceprovisioningPartnersDevicesGet(name, opts)



Gets a device.

### Example

```javascript
import AndroidDeviceProvisioningPartnerApi from 'android_device_provisioning_partner_api';

let apiInstance = new AndroidDeviceProvisioningPartnerApi.PartnersApi();
let name = "name_example"; // String | Required. The device API resource name in the format `partners/[PARTNER_ID]/devices/[DEVICE_ID]`.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example" // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
};
apiInstance.androiddeviceprovisioningPartnersDevicesGet(name, opts, (error, data, response) => {
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
 **name** | **String**| Required. The device API resource name in the format &#x60;partners/[PARTNER_ID]/devices/[DEVICE_ID]&#x60;. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 

### Return type

[**Device**](Device.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## androiddeviceprovisioningPartnersDevicesGetSimLockState

> GetDeviceSimLockStateResponse androiddeviceprovisioningPartnersDevicesGetSimLockState(partnerId, opts)



Gets a device&#39;s SIM lock state.

### Example

```javascript
import AndroidDeviceProvisioningPartnerApi from 'android_device_provisioning_partner_api';

let apiInstance = new AndroidDeviceProvisioningPartnerApi.PartnersApi();
let partnerId = "partnerId_example"; // String | Required. The ID of the partner.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'getDeviceSimLockStateRequest': new AndroidDeviceProvisioningPartnerApi.GetDeviceSimLockStateRequest() // GetDeviceSimLockStateRequest | 
};
apiInstance.androiddeviceprovisioningPartnersDevicesGetSimLockState(partnerId, opts, (error, data, response) => {
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
 **partnerId** | **String**| Required. The ID of the partner. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **getDeviceSimLockStateRequest** | [**GetDeviceSimLockStateRequest**](GetDeviceSimLockStateRequest.md)|  | [optional] 

### Return type

[**GetDeviceSimLockStateResponse**](GetDeviceSimLockStateResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## androiddeviceprovisioningPartnersDevicesMetadata

> DeviceMetadata androiddeviceprovisioningPartnersDevicesMetadata(metadataOwnerId, deviceId, opts)



Updates reseller metadata associated with the device. Android devices only.

### Example

```javascript
import AndroidDeviceProvisioningPartnerApi from 'android_device_provisioning_partner_api';

let apiInstance = new AndroidDeviceProvisioningPartnerApi.PartnersApi();
let metadataOwnerId = "metadataOwnerId_example"; // String | Required. The owner of the newly set metadata. Set this to the partner ID.
let deviceId = "deviceId_example"; // String | Required. The ID of the device.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'updateDeviceMetadataRequest': new AndroidDeviceProvisioningPartnerApi.UpdateDeviceMetadataRequest() // UpdateDeviceMetadataRequest | 
};
apiInstance.androiddeviceprovisioningPartnersDevicesMetadata(metadataOwnerId, deviceId, opts, (error, data, response) => {
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
 **metadataOwnerId** | **String**| Required. The owner of the newly set metadata. Set this to the partner ID. | 
 **deviceId** | **String**| Required. The ID of the device. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **updateDeviceMetadataRequest** | [**UpdateDeviceMetadataRequest**](UpdateDeviceMetadataRequest.md)|  | [optional] 

### Return type

[**DeviceMetadata**](DeviceMetadata.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## androiddeviceprovisioningPartnersDevicesUnclaim

> Object androiddeviceprovisioningPartnersDevicesUnclaim(partnerId, opts)



Unclaims a device from a customer and removes it from zero-touch enrollment.

### Example

```javascript
import AndroidDeviceProvisioningPartnerApi from 'android_device_provisioning_partner_api';

let apiInstance = new AndroidDeviceProvisioningPartnerApi.PartnersApi();
let partnerId = "partnerId_example"; // String | Required. The ID of the reseller partner.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'unclaimDeviceRequest': new AndroidDeviceProvisioningPartnerApi.UnclaimDeviceRequest() // UnclaimDeviceRequest | 
};
apiInstance.androiddeviceprovisioningPartnersDevicesUnclaim(partnerId, opts, (error, data, response) => {
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
 **partnerId** | **String**| Required. The ID of the reseller partner. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **unclaimDeviceRequest** | [**UnclaimDeviceRequest**](UnclaimDeviceRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## androiddeviceprovisioningPartnersDevicesUnclaimAsync

> Operation androiddeviceprovisioningPartnersDevicesUnclaimAsync(partnerId, opts)



Unclaims a batch of devices for a customer asynchronously. Removes the devices from zero-touch enrollment. To learn more, read [Long‑running batch operations](/zero-touch/guides/how-it-works#operations).

### Example

```javascript
import AndroidDeviceProvisioningPartnerApi from 'android_device_provisioning_partner_api';

let apiInstance = new AndroidDeviceProvisioningPartnerApi.PartnersApi();
let partnerId = "partnerId_example"; // String | Required. The reseller partner ID.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'unclaimDevicesRequest': new AndroidDeviceProvisioningPartnerApi.UnclaimDevicesRequest() // UnclaimDevicesRequest | 
};
apiInstance.androiddeviceprovisioningPartnersDevicesUnclaimAsync(partnerId, opts, (error, data, response) => {
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
 **partnerId** | **String**| Required. The reseller partner ID. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **unclaimDevicesRequest** | [**UnclaimDevicesRequest**](UnclaimDevicesRequest.md)|  | [optional] 

### Return type

[**Operation**](Operation.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## androiddeviceprovisioningPartnersDevicesUpdateMetadataAsync

> Operation androiddeviceprovisioningPartnersDevicesUpdateMetadataAsync(partnerId, opts)



Updates the reseller metadata attached to a batch of devices. This method updates devices asynchronously and returns an &#x60;Operation&#x60; that can be used to track progress. Read [Long‑running batch operations](/zero-touch/guides/how-it-works#operations). Android Devices only.

### Example

```javascript
import AndroidDeviceProvisioningPartnerApi from 'android_device_provisioning_partner_api';

let apiInstance = new AndroidDeviceProvisioningPartnerApi.PartnersApi();
let partnerId = "partnerId_example"; // String | Required. The reseller partner ID.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'updateDeviceMetadataInBatchRequest': new AndroidDeviceProvisioningPartnerApi.UpdateDeviceMetadataInBatchRequest() // UpdateDeviceMetadataInBatchRequest | 
};
apiInstance.androiddeviceprovisioningPartnersDevicesUpdateMetadataAsync(partnerId, opts, (error, data, response) => {
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
 **partnerId** | **String**| Required. The reseller partner ID. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **updateDeviceMetadataInBatchRequest** | [**UpdateDeviceMetadataInBatchRequest**](UpdateDeviceMetadataInBatchRequest.md)|  | [optional] 

### Return type

[**Operation**](Operation.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## androiddeviceprovisioningPartnersVendorsCustomersList

> ListVendorCustomersResponse androiddeviceprovisioningPartnersVendorsCustomersList(parent, opts)



Lists the customers of the vendor.

### Example

```javascript
import AndroidDeviceProvisioningPartnerApi from 'android_device_provisioning_partner_api';

let apiInstance = new AndroidDeviceProvisioningPartnerApi.PartnersApi();
let parent = "parent_example"; // String | Required. The resource name in the format `partners/[PARTNER_ID]/vendors/[VENDOR_ID]`.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'pageSize': 56, // Number | The maximum number of results to be returned.
  'pageToken': "pageToken_example" // String | A token identifying a page of results returned by the server.
};
apiInstance.androiddeviceprovisioningPartnersVendorsCustomersList(parent, opts, (error, data, response) => {
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
 **parent** | **String**| Required. The resource name in the format &#x60;partners/[PARTNER_ID]/vendors/[VENDOR_ID]&#x60;. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **pageSize** | **Number**| The maximum number of results to be returned. | [optional] 
 **pageToken** | **String**| A token identifying a page of results returned by the server. | [optional] 

### Return type

[**ListVendorCustomersResponse**](ListVendorCustomersResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## androiddeviceprovisioningPartnersVendorsList

> ListVendorsResponse androiddeviceprovisioningPartnersVendorsList(parent, opts)



Lists the vendors of the partner.

### Example

```javascript
import AndroidDeviceProvisioningPartnerApi from 'android_device_provisioning_partner_api';

let apiInstance = new AndroidDeviceProvisioningPartnerApi.PartnersApi();
let parent = "parent_example"; // String | Required. The resource name in the format `partners/[PARTNER_ID]`.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'pageSize': 56, // Number | The maximum number of results to be returned.
  'pageToken': "pageToken_example" // String | A token identifying a page of results returned by the server.
};
apiInstance.androiddeviceprovisioningPartnersVendorsList(parent, opts, (error, data, response) => {
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
 **parent** | **String**| Required. The resource name in the format &#x60;partners/[PARTNER_ID]&#x60;. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **pageSize** | **Number**| The maximum number of results to be returned. | [optional] 
 **pageToken** | **String**| A token identifying a page of results returned by the server. | [optional] 

### Return type

[**ListVendorsResponse**](ListVendorsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

