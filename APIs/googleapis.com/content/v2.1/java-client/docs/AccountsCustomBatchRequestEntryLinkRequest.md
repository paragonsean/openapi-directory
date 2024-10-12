

# AccountsCustomBatchRequestEntryLinkRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**action** | **String** | Action to perform for this link. The &#x60;\&quot;request\&quot;&#x60; action is only available to select merchants. Acceptable values are: - \&quot;&#x60;approve&#x60;\&quot; - \&quot;&#x60;remove&#x60;\&quot; - \&quot;&#x60;request&#x60;\&quot;  |  [optional] |
|**linkType** | **String** | Type of the link between the two accounts. Acceptable values are: - \&quot;&#x60;channelPartner&#x60;\&quot; - \&quot;&#x60;eCommercePlatform&#x60;\&quot; - \&quot;&#x60;paymentServiceProvider&#x60;\&quot; - \&quot;&#x60;localProductManager&#x60;\&quot;  |  [optional] |
|**linkedAccountId** | **String** | The ID of the linked account. |  [optional] |
|**services** | **List&lt;String&gt;** | Provided services. Acceptable values are: - \&quot;&#x60;shoppingAdsProductManagement&#x60;\&quot; - \&quot;&#x60;shoppingActionsProductManagement&#x60;\&quot; - \&quot;&#x60;shoppingActionsOrderManagement&#x60;\&quot; - \&quot;&#x60;paymentProcessing&#x60;\&quot; - \&quot;&#x60;localProductManagement&#x60;\&quot;  |  [optional] |



