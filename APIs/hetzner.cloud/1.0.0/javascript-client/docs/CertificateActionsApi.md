# HetznerCloudApi.CertificateActionsApi

All URIs are relative to *https://api.hetzner.cloud/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**certificatesIdActionsActionIdGet**](CertificateActionsApi.md#certificatesIdActionsActionIdGet) | **GET** /certificates/{id}/actions/{action_id} | Get an Action for a Certificate
[**certificatesIdActionsGet**](CertificateActionsApi.md#certificatesIdActionsGet) | **GET** /certificates/{id}/actions | Get all Actions for a Certificate
[**certificatesIdActionsRetryPost**](CertificateActionsApi.md#certificatesIdActionsRetryPost) | **POST** /certificates/{id}/actions/retry | Retry Issuance or Renewal



## certificatesIdActionsActionIdGet

> ActionResponse certificatesIdActionsActionIdGet(id, actionId)

Get an Action for a Certificate

Returns a specific Action for a Certificate. Only type &#x60;managed&#x60; Certificates have Actions.

### Example

```javascript
import HetznerCloudApi from 'hetzner_cloud_api';

let apiInstance = new HetznerCloudApi.CertificateActionsApi();
let id = 56; // Number | ID of the Certificate
let actionId = 56; // Number | ID of the Action
apiInstance.certificatesIdActionsActionIdGet(id, actionId, (error, data, response) => {
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
 **id** | **Number**| ID of the Certificate | 
 **actionId** | **Number**| ID of the Action | 

### Return type

[**ActionResponse**](ActionResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## certificatesIdActionsGet

> ActionsResponse certificatesIdActionsGet(id, opts)

Get all Actions for a Certificate

Returns all Action objects for a Certificate. You can sort the results by using the &#x60;sort&#x60; URI parameter, and filter them with the &#x60;status&#x60; parameter.  Only type &#x60;managed&#x60; Certificates can have Actions. For type &#x60;uploaded&#x60; Certificates the &#x60;actions&#x60; key will always contain an empty array. 

### Example

```javascript
import HetznerCloudApi from 'hetzner_cloud_api';

let apiInstance = new HetznerCloudApi.CertificateActionsApi();
let id = 56; // Number | ID of the Resource
let opts = {
  'sort': "sort_example", // String | Can be used multiple times.
  'status': "status_example" // String | Can be used multiple times, the response will contain only Actions with specified statuses
};
apiInstance.certificatesIdActionsGet(id, opts, (error, data, response) => {
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
 **id** | **Number**| ID of the Resource | 
 **sort** | **String**| Can be used multiple times. | [optional] 
 **status** | **String**| Can be used multiple times, the response will contain only Actions with specified statuses | [optional] 

### Return type

[**ActionsResponse**](ActionsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## certificatesIdActionsRetryPost

> ActionResponse certificatesIdActionsRetryPost(id)

Retry Issuance or Renewal

Retry a failed Certificate issuance or renewal.  Only applicable if the type of the Certificate is &#x60;managed&#x60; and the issuance or renewal status is &#x60;failed&#x60;.  #### Call specific error codes  | Code                                                    | Description                                                               | |---------------------------------------------------------|---------------------------------------------------------------------------| | &#x60;caa_record_does_not_allow_ca&#x60;                          | CAA record does not allow certificate authority                           | | &#x60;ca_dns_validation_failed&#x60;                              | Certificate Authority: DNS validation failed                              | | &#x60;ca_too_many_authorizations_failed_recently&#x60;            | Certificate Authority: Too many authorizations failed recently            | | &#x60;ca_too_many_certificates_issued_for_registered_domain&#x60; | Certificate Authority: Too many certificates issued for registered domain | | &#x60;ca_too_many_duplicate_certificates&#x60;                    | Certificate Authority: Too many duplicate certificates                    | | &#x60;could_not_verify_domain_delegated_to_zone&#x60;             | Could not verify domain delegated to zone                                 | | &#x60;dns_zone_not_found&#x60;                                    | DNS zone not found                                                        | | &#x60;dns_zone_is_secondary_zone&#x60;                            | DNS zone is a secondary zone                                              | 

### Example

```javascript
import HetznerCloudApi from 'hetzner_cloud_api';

let apiInstance = new HetznerCloudApi.CertificateActionsApi();
let id = 56; // Number | ID of the Certificate
apiInstance.certificatesIdActionsRetryPost(id, (error, data, response) => {
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
 **id** | **Number**| ID of the Certificate | 

### Return type

[**ActionResponse**](ActionResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

