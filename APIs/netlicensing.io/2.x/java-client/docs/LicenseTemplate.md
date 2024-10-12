

# LicenseTemplate


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**active** | **Boolean** | If set to &#39;false&#39;, the License Template is disabled. Licensee can not obtain any new Licenses off this License Template. |  [optional] |
|**automatic** | **Boolean** | If set to &#39;true&#39;, every new Licensee automatically gets one License out of this License Template on creation. Automatic Licenses must have their price set to 0. |  [optional] |
|**currency** | **String** | Specifies currency for the License price. Check data types to discover which currencies are supported. |  [optional] |
|**hidden** | **Boolean** | If set to &#39;true&#39;, this License Template is not shown in NetLicensing Shop as offered for purchase. |  [optional] |
|**hiddenLicenses** | **Boolean** | If set to &#39;true&#39;, Licenses from this License Template are not visible to the end customer, but participate in validation. |  [optional] |
|**licenseType** | [**LicenseTypeEnum**](#LicenseTypeEnum) | Type of Licenses created from this License Template |  [optional] |
|**name** | **String** | Name for the Licensed item. |  [optional] |
|**number** | **String** | Unique number (across all Product of a Vendor) that identifies the License Template. Vendor can assign this number when creating a License Template or let NetLicensing generate one. Read-only after creation of the first License from this License Template. |  [optional] |
|**price** | **Double** | &#39;price&#39; for the License. If &gt;0, it must always be accompanied by the currency specification. |  [optional] |



## Enum: LicenseTypeEnum

| Name | Value |
|---- | -----|
| FEATURE | &quot;FEATURE&quot; |
| TIMEVOLUME | &quot;TIMEVOLUME&quot; |



