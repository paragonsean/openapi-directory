

# License


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**active** | **Boolean** | If set to &#39;false&#39;, the License is disabled. License can be re-enabled, but as long as it is disabled, the License is excluded from the validation process. |  [optional] |
|**currency** | **String** | Specifies currency for the License price. Check data types to discover which currencies are supported. Read-only, set from License Template on creation. |  [optional] |
|**hidden** | **Boolean** | If set to &#39;true&#39;, this License is not shown in NetLicensing Shop as purchased License. Set from License Template on creation, if not specified explicitly. |  [optional] |
|**name** | **String** | Name for the Licensed item. Set from License Template on creation, if not specified explicitly. |  [optional] |
|**number** | **String** | Unique number (across all Products/Licensees of a Vendor) that identifies the License. Vendor can assign this number when creating a License or let NetLicensing generate one. Read-only after corresponding creation Transaction status is set to closed. |  [optional] |
|**price** | **Double** | &#39;price&#39; for the License. If &gt;0, it must always be accompanied by the currency specification. Read-only, set from License Template on creation. |  [optional] |



