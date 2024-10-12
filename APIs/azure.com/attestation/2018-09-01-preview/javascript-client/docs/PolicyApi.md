# AttestationClient.PolicyApi

All URIs are relative to *https://azure.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**policyGet**](PolicyApi.md#policyGet) | **GET** /operations/policy/current | Retrieves the current policy for a given kind of TEE.
[**policyPrepareToSet**](PolicyApi.md#policyPrepareToSet) | **POST** /operations/policy/updatepolicy | Accepts a new policy document and returns a JWT which expresses  used in preparation to set attestation policy.
[**policyReset**](PolicyApi.md#policyReset) | **POST** /operations/policy/current | Resets the attestation policy for the specified tenant and reverts to the default policy.
[**policySet**](PolicyApi.md#policySet) | **PUT** /operations/policy/current | Sets the policy for a given kind of TEE.



## policyGet

> AttestationPolicy policyGet(apiVersion, tee)

Retrieves the current policy for a given kind of TEE.

### Example

```javascript
import AttestationClient from 'attestation_client';

let apiInstance = new AttestationClient.PolicyApi();
let apiVersion = "apiVersion_example"; // String | Client API version.
let tee = "tee_example"; // String | Specifies the trusted execution environment to be used to validate the evidence
apiInstance.policyGet(apiVersion, tee, (error, data, response) => {
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
 **apiVersion** | **String**| Client API version. | 
 **tee** | **String**| Specifies the trusted execution environment to be used to validate the evidence | 

### Return type

[**AttestationPolicy**](AttestationPolicy.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## policyPrepareToSet

> String policyPrepareToSet(apiVersion, tee, policyJws)

Accepts a new policy document and returns a JWT which expresses  used in preparation to set attestation policy.

### Example

```javascript
import AttestationClient from 'attestation_client';

let apiInstance = new AttestationClient.PolicyApi();
let apiVersion = "apiVersion_example"; // String | Client API version.
let tee = "tee_example"; // String | Specifies the trusted execution environment to be used to validate the evidence
let policyJws = "policyJws_example"; // String | JSON Web Signature (See RFC7515) expressing the new policy
apiInstance.policyPrepareToSet(apiVersion, tee, policyJws, (error, data, response) => {
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
 **apiVersion** | **String**| Client API version. | 
 **tee** | **String**| Specifies the trusted execution environment to be used to validate the evidence | 
 **policyJws** | **String**| JSON Web Signature (See RFC7515) expressing the new policy | 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: text/plain
- **Accept**: text/plain, application/json


## policyReset

> String policyReset(apiVersion, tee, policyJws)

Resets the attestation policy for the specified tenant and reverts to the default policy.

### Example

```javascript
import AttestationClient from 'attestation_client';

let apiInstance = new AttestationClient.PolicyApi();
let apiVersion = "apiVersion_example"; // String | Client API version.
let tee = "tee_example"; // String | Specifies the trusted execution environment to be used to validate the evidence
let policyJws = "policyJws_example"; // String | JSON Web Signature with an empty policy document
apiInstance.policyReset(apiVersion, tee, policyJws, (error, data, response) => {
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
 **apiVersion** | **String**| Client API version. | 
 **tee** | **String**| Specifies the trusted execution environment to be used to validate the evidence | 
 **policyJws** | **String**| JSON Web Signature with an empty policy document | 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: text/plain
- **Accept**: application/json


## policySet

> policySet(apiVersion, tee, newAttestationPolicy)

Sets the policy for a given kind of TEE.

### Example

```javascript
import AttestationClient from 'attestation_client';

let apiInstance = new AttestationClient.PolicyApi();
let apiVersion = "apiVersion_example"; // String | Client API version.
let tee = "tee_example"; // String | Specifies the trusted execution environment to be used to validate the evidence
let newAttestationPolicy = "newAttestationPolicy_example"; // String | JWT Expressing the new policy
apiInstance.policySet(apiVersion, tee, newAttestationPolicy, (error, data, response) => {
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
 **apiVersion** | **String**| Client API version. | 
 **tee** | **String**| Specifies the trusted execution environment to be used to validate the evidence | 
 **newAttestationPolicy** | **String**| JWT Expressing the new policy | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: text/plain
- **Accept**: application/json

