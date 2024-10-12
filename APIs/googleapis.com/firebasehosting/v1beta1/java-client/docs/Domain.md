

# Domain

The intended behavior and status information of a domain.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**domainName** | **String** | Required. The domain name of the association. |  [optional] |
|**domainRedirect** | [**DomainRedirect**](DomainRedirect.md) |  |  [optional] |
|**provisioning** | [**DomainProvisioning**](DomainProvisioning.md) |  |  [optional] |
|**site** | **String** | Required. The site name of the association. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | Output only. Additional status of the domain association. |  [optional] |
|**updateTime** | **String** | Output only. The time at which the domain was last updated. |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| STATUS_UNSPECIFIED | &quot;DOMAIN_STATUS_UNSPECIFIED&quot; |
| CHANGE_PENDING | &quot;DOMAIN_CHANGE_PENDING&quot; |
| ACTIVE | &quot;DOMAIN_ACTIVE&quot; |
| VERIFICATION_REQUIRED | &quot;DOMAIN_VERIFICATION_REQUIRED&quot; |
| VERIFICATION_LOST | &quot;DOMAIN_VERIFICATION_LOST&quot; |



