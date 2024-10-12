# PeeringManagementClient.LegacyPeeringsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**legacyPeeringsList**](LegacyPeeringsApi.md#legacyPeeringsList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Peering/legacyPeerings | 



## legacyPeeringsList

> PeeringListResult legacyPeeringsList(peeringLocation, kind, subscriptionId, apiVersion, opts)



Lists all of the legacy peerings under the given subscription matching the specified kind and location.

### Example

```javascript
import PeeringManagementClient from 'peering_management_client';
let defaultClient = PeeringManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeeringManagementClient.LegacyPeeringsApi();
let peeringLocation = "peeringLocation_example"; // String | The location of the peering.
let kind = "kind_example"; // String | The kind of the peering.
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID.
let apiVersion = "apiVersion_example"; // String | The client API version.
let opts = {
  'asn': 56 // Number | The ASN number associated with a legacy peering.
};
apiInstance.legacyPeeringsList(peeringLocation, kind, subscriptionId, apiVersion, opts, (error, data, response) => {
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
 **peeringLocation** | **String**| The location of the peering. | 
 **kind** | **String**| The kind of the peering. | 
 **subscriptionId** | **String**| The Azure subscription ID. | 
 **apiVersion** | **String**| The client API version. | 
 **asn** | **Number**| The ASN number associated with a legacy peering. | [optional] 

### Return type

[**PeeringListResult**](PeeringListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

