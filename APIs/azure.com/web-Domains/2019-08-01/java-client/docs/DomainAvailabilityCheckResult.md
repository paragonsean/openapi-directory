

# DomainAvailabilityCheckResult

Domain availability check result.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**available** | **Boolean** | &lt;code&gt;true&lt;/code&gt; if domain can be purchased using CreateDomain API; otherwise, &lt;code&gt;false&lt;/code&gt;. |  [optional] |
|**domainType** | [**DomainTypeEnum**](#DomainTypeEnum) | Valid values are Regular domain: Azure will charge the full price of domain registration, SoftDeleted: Purchasing this domain will simply restore it and this operation will not cost anything. |  [optional] |
|**name** | **String** | Name of the domain. |  [optional] |



## Enum: DomainTypeEnum

| Name | Value |
|---- | -----|
| REGULAR | &quot;Regular&quot; |
| SOFT_DELETED | &quot;SoftDeleted&quot; |



