

# Deal

A deal represents a segment of inventory for displaying ads on. A proposal can contain multiple deals. A deal contains the terms and targeting information that is used for serving.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**availableEndTime** | **String** | Proposed flight end time of the deal. This will generally be stored in a granularity of a second. A value is not required for Private Auction deals or Preferred Deals. |  [optional] |
|**availableStartTime** | **String** | Optional. Proposed flight start time of the deal. This will generally be stored in the granularity of one second since deal serving starts at seconds boundary. Any time specified with more granularity (for example, in milliseconds) will be truncated towards the start of time in seconds. |  [optional] |
|**buyerPrivateData** | [**PrivateData**](PrivateData.md) |  |  [optional] |
|**createProductId** | **String** | The product ID from which this deal was created. Note: This field may be set only when creating the resource. Modifying this field while updating the resource will result in an error. |  [optional] |
|**createProductRevision** | **String** | Optional. Revision number of the product that the deal was created from. If present on create, and the server &#x60;product_revision&#x60; has advanced since the passed-in &#x60;create_product_revision&#x60;, an &#x60;ABORTED&#x60; error will be returned. Note: This field may be set only when creating the resource. Modifying this field while updating the resource will result in an error. |  [optional] |
|**createTime** | **String** | Output only. The time of the deal creation. |  [optional] [readonly] |
|**creativePreApprovalPolicy** | [**CreativePreApprovalPolicyEnum**](#CreativePreApprovalPolicyEnum) | Output only. Specifies the creative pre-approval policy. |  [optional] [readonly] |
|**creativeRestrictions** | [**CreativeRestrictions**](CreativeRestrictions.md) |  |  [optional] |
|**creativeSafeFrameCompatibility** | [**CreativeSafeFrameCompatibilityEnum**](#CreativeSafeFrameCompatibilityEnum) | Output only. Specifies whether the creative is safeFrame compatible. |  [optional] [readonly] |
|**dealId** | **String** | Output only. A unique deal ID for the deal (server-assigned). |  [optional] [readonly] |
|**dealServingMetadata** | [**DealServingMetadata**](DealServingMetadata.md) |  |  [optional] |
|**dealTerms** | [**DealTerms**](DealTerms.md) |  |  [optional] |
|**deliveryControl** | [**DeliveryControl**](DeliveryControl.md) |  |  [optional] |
|**description** | **String** | Description for the deal terms. |  [optional] |
|**displayName** | **String** | The name of the deal. |  [optional] |
|**externalDealId** | **String** | Output only. The external deal ID assigned to this deal once the deal is finalized. This is the deal ID that shows up in serving/reporting etc. |  [optional] [readonly] |
|**isSetupComplete** | **Boolean** | Output only. True, if the buyside inventory setup is complete for this deal. |  [optional] [readonly] |
|**programmaticCreativeSource** | [**ProgrammaticCreativeSourceEnum**](#ProgrammaticCreativeSourceEnum) | Output only. Specifies the creative source for programmatic deals. PUBLISHER means creative is provided by seller and ADVERTISER means creative is provided by buyer. |  [optional] [readonly] |
|**proposalId** | **String** | Output only. ID of the proposal that this deal is part of. |  [optional] [readonly] |
|**sellerContacts** | [**List&lt;ContactInformation&gt;**](ContactInformation.md) | Output only. Seller contact information for the deal. |  [optional] [readonly] |
|**syndicationProduct** | [**SyndicationProductEnum**](#SyndicationProductEnum) | The syndication product associated with the deal. Note: This field may be set only when creating the resource. Modifying this field while updating the resource will result in an error. |  [optional] |
|**targeting** | [**MarketplaceTargeting**](MarketplaceTargeting.md) |  |  [optional] |
|**targetingCriterion** | [**List&lt;TargetingCriteria&gt;**](TargetingCriteria.md) | The shared targeting visible to buyers and sellers. Each shared targeting entity is AND&#39;d together. |  [optional] |
|**updateTime** | **String** | Output only. The time when the deal was last updated. |  [optional] [readonly] |
|**webPropertyCode** | **String** | The web property code for the seller copied over from the product. |  [optional] |



## Enum: CreativePreApprovalPolicyEnum

| Name | Value |
|---- | -----|
| CREATIVE_PRE_APPROVAL_POLICY_UNSPECIFIED | &quot;CREATIVE_PRE_APPROVAL_POLICY_UNSPECIFIED&quot; |
| SELLER_PRE_APPROVAL_REQUIRED | &quot;SELLER_PRE_APPROVAL_REQUIRED&quot; |
| SELLER_PRE_APPROVAL_NOT_REQUIRED | &quot;SELLER_PRE_APPROVAL_NOT_REQUIRED&quot; |



## Enum: CreativeSafeFrameCompatibilityEnum

| Name | Value |
|---- | -----|
| CREATIVE_SAFE_FRAME_COMPATIBILITY_UNSPECIFIED | &quot;CREATIVE_SAFE_FRAME_COMPATIBILITY_UNSPECIFIED&quot; |
| COMPATIBLE | &quot;COMPATIBLE&quot; |
| INCOMPATIBLE | &quot;INCOMPATIBLE&quot; |



## Enum: ProgrammaticCreativeSourceEnum

| Name | Value |
|---- | -----|
| PROGRAMMATIC_CREATIVE_SOURCE_UNSPECIFIED | &quot;PROGRAMMATIC_CREATIVE_SOURCE_UNSPECIFIED&quot; |
| ADVERTISER | &quot;ADVERTISER&quot; |
| PUBLISHER | &quot;PUBLISHER&quot; |



## Enum: SyndicationProductEnum

| Name | Value |
|---- | -----|
| SYNDICATION_PRODUCT_UNSPECIFIED | &quot;SYNDICATION_PRODUCT_UNSPECIFIED&quot; |
| CONTENT | &quot;CONTENT&quot; |
| MOBILE | &quot;MOBILE&quot; |
| VIDEO | &quot;VIDEO&quot; |
| GAMES | &quot;GAMES&quot; |



