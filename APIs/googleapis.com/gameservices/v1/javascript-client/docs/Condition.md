# GameServicesApi.Condition

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**iam** | **String** | Trusted attributes supplied by the IAM system. | [optional] 
**op** | **String** | An operator to apply the subject with. | [optional] 
**svc** | **String** | Trusted attributes discharged by the service. | [optional] 
**sys** | **String** | Trusted attributes supplied by any service that owns resources and uses the IAM system for access control. | [optional] 
**values** | **[String]** | The objects of the condition. | [optional] 



## Enum: IamEnum


* `NO_ATTR` (value: `"NO_ATTR"`)

* `AUTHORITY` (value: `"AUTHORITY"`)

* `ATTRIBUTION` (value: `"ATTRIBUTION"`)

* `SECURITY_REALM` (value: `"SECURITY_REALM"`)

* `APPROVER` (value: `"APPROVER"`)

* `JUSTIFICATION_TYPE` (value: `"JUSTIFICATION_TYPE"`)

* `CREDENTIALS_TYPE` (value: `"CREDENTIALS_TYPE"`)

* `CREDS_ASSERTION` (value: `"CREDS_ASSERTION"`)





## Enum: OpEnum


* `NO_OP` (value: `"NO_OP"`)

* `EQUALS` (value: `"EQUALS"`)

* `NOT_EQUALS` (value: `"NOT_EQUALS"`)

* `IN` (value: `"IN"`)

* `NOT_IN` (value: `"NOT_IN"`)

* `DISCHARGED` (value: `"DISCHARGED"`)





## Enum: SysEnum


* `NO_ATTR` (value: `"NO_ATTR"`)

* `REGION` (value: `"REGION"`)

* `SERVICE` (value: `"SERVICE"`)

* `NAME` (value: `"NAME"`)

* `IP` (value: `"IP"`)




