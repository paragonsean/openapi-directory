# AttestationClient.AttestationApi

All URIs are relative to *https://azure.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**certsGet**](AttestationApi.md#certsGet) | **GET** /certs | Retrieves the OpenID Configuration data for the Azure Attestation Service
[**metadataConfigurationGet**](AttestationApi.md#metadataConfigurationGet) | **GET** /.well-known/openid-configuration | Retrieves the OpenID Configuration data for the Azure Attestation Service



## certsGet

> Object certsGet()

Retrieves the OpenID Configuration data for the Azure Attestation Service

Retrieves attestation signing keys in use by the attestation service

### Example

```javascript
import AttestationClient from 'attestation_client';

let apiInstance = new AttestationClient.AttestationApi();
apiInstance.certsGet((error, data, response) => {
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

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## metadataConfigurationGet

> Object metadataConfigurationGet()

Retrieves the OpenID Configuration data for the Azure Attestation Service

Retrieves metadata about the attestation signing keys in use by the  attestation service

### Example

```javascript
import AttestationClient from 'attestation_client';

let apiInstance = new AttestationClient.AttestationApi();
apiInstance.metadataConfigurationGet((error, data, response) => {
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

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

