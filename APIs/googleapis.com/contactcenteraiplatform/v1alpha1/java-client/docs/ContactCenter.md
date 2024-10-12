

# ContactCenter

Message describing ContactCenter object Next ID: 20

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**adminUser** | [**AdminUser**](AdminUser.md) |  |  [optional] |
|**ccaipManagedUsers** | **Boolean** | Optional. Whether to enable users to be created in the CCAIP-instance concurrently to having users in Cloud identity |  [optional] |
|**createTime** | **String** | Output only. [Output only] Create time stamp |  [optional] [readonly] |
|**customerDomainPrefix** | **String** | Required. Immutable. At least 2 and max 16 char long, must conform to [RFC 1035](https://www.ietf.org/rfc/rfc1035.txt). |  [optional] |
|**displayName** | **String** | Required. A user friendly name for the ContactCenter. |  [optional] |
|**instanceConfig** | [**InstanceConfig**](InstanceConfig.md) |  |  [optional] |
|**kmsKey** | **String** | Immutable. The KMS key name to encrypt the user input (&#x60;ContactCenter&#x60;). |  [optional] |
|**labels** | **Map&lt;String, String&gt;** | Labels as key value pairs |  [optional] |
|**name** | **String** | name of resource |  [optional] |
|**privateComponents** | **List&lt;String&gt;** | Output only. A list of UJET components that should be privately accessed. This field is set by reading settings from the data plane. For more information about the format of the component please refer to go/ccaip-vpc-sc-org-policy. This field is must be fully populated only for Create/Update resource operations. The main use case for this field is OrgPolicy checks via CPE. |  [optional] [readonly] |
|**samlParams** | [**SAMLParams**](SAMLParams.md) |  |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | Output only. The state of this contact center. |  [optional] [readonly] |
|**updateTime** | **String** | Output only. [Output only] Update time stamp |  [optional] [readonly] |
|**uris** | [**URIs**](URIs.md) |  |  [optional] |
|**userEmail** | **String** | Optional. Email address of the first admin user. |  [optional] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| DEPLOYING | &quot;STATE_DEPLOYING&quot; |
| DEPLOYED | &quot;STATE_DEPLOYED&quot; |
| TERMINATING | &quot;STATE_TERMINATING&quot; |
| FAILED | &quot;STATE_FAILED&quot; |
| TERMINATING_FAILED | &quot;STATE_TERMINATING_FAILED&quot; |
| TERMINATED | &quot;STATE_TERMINATED&quot; |
| IN_GRACE_PERIOD | &quot;STATE_IN_GRACE_PERIOD&quot; |



