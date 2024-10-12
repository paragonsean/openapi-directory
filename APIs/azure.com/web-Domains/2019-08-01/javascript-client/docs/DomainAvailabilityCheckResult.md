# DomainsApiClient.DomainAvailabilityCheckResult

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**available** | **Boolean** | &lt;code&gt;true&lt;/code&gt; if domain can be purchased using CreateDomain API; otherwise, &lt;code&gt;false&lt;/code&gt;. | [optional] 
**domainType** | **String** | Valid values are Regular domain: Azure will charge the full price of domain registration, SoftDeleted: Purchasing this domain will simply restore it and this operation will not cost anything. | [optional] 
**name** | **String** | Name of the domain. | [optional] 



## Enum: DomainTypeEnum


* `Regular` (value: `"Regular"`)

* `SoftDeleted` (value: `"SoftDeleted"`)




