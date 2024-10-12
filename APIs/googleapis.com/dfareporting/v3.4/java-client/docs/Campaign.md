

# Campaign

Contains properties of a Campaign Manager campaign.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** | Account ID of this campaign. This is a read-only field that can be left blank. |  [optional] |
|**adBlockingConfiguration** | [**AdBlockingConfiguration**](AdBlockingConfiguration.md) |  |  [optional] |
|**additionalCreativeOptimizationConfigurations** | [**List&lt;CreativeOptimizationConfiguration&gt;**](CreativeOptimizationConfiguration.md) | Additional creative optimization configurations for the campaign. |  [optional] |
|**advertiserGroupId** | **String** | Advertiser group ID of the associated advertiser. |  [optional] |
|**advertiserId** | **String** | Advertiser ID of this campaign. This is a required field. |  [optional] |
|**advertiserIdDimensionValue** | [**DimensionValue**](DimensionValue.md) |  |  [optional] |
|**archived** | **Boolean** | Whether this campaign has been archived. |  [optional] |
|**audienceSegmentGroups** | [**List&lt;AudienceSegmentGroup&gt;**](AudienceSegmentGroup.md) | Audience segment groups assigned to this campaign. Cannot have more than 300 segment groups. |  [optional] |
|**billingInvoiceCode** | **String** | Billing invoice code included in the Campaign Manager client billing invoices associated with the campaign. |  [optional] |
|**clickThroughUrlSuffixProperties** | [**ClickThroughUrlSuffixProperties**](ClickThroughUrlSuffixProperties.md) |  |  [optional] |
|**comment** | **String** | Arbitrary comments about this campaign. Must be less than 256 characters long. |  [optional] |
|**createInfo** | [**LastModifiedInfo**](LastModifiedInfo.md) |  |  [optional] |
|**creativeGroupIds** | **List&lt;String&gt;** | List of creative group IDs that are assigned to the campaign. |  [optional] |
|**creativeOptimizationConfiguration** | [**CreativeOptimizationConfiguration**](CreativeOptimizationConfiguration.md) |  |  [optional] |
|**defaultClickThroughEventTagProperties** | [**DefaultClickThroughEventTagProperties**](DefaultClickThroughEventTagProperties.md) |  |  [optional] |
|**defaultLandingPageId** | **String** | The default landing page ID for this campaign. |  [optional] |
|**endDate** | **LocalDate** |  |  [optional] |
|**eventTagOverrides** | [**List&lt;EventTagOverride&gt;**](EventTagOverride.md) | Overrides that can be used to activate or deactivate advertiser event tags. |  [optional] |
|**externalId** | **String** | External ID for this campaign. |  [optional] |
|**id** | **String** | ID of this campaign. This is a read-only auto-generated field. |  [optional] |
|**idDimensionValue** | [**DimensionValue**](DimensionValue.md) |  |  [optional] |
|**kind** | **String** | Identifies what kind of resource this is. Value: the fixed string \&quot;dfareporting#campaign\&quot;. |  [optional] |
|**lastModifiedInfo** | [**LastModifiedInfo**](LastModifiedInfo.md) |  |  [optional] |
|**name** | **String** | Name of this campaign. This is a required field and must be less than 512 characters long and unique among campaigns of the same advertiser. |  [optional] |
|**nielsenOcrEnabled** | **Boolean** | Whether Nielsen reports are enabled for this campaign. |  [optional] |
|**startDate** | **LocalDate** |  |  [optional] |
|**subaccountId** | **String** | Subaccount ID of this campaign. This is a read-only field that can be left blank. |  [optional] |
|**traffickerEmails** | **List&lt;String&gt;** | Campaign trafficker contact emails. |  [optional] |



