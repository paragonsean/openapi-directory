

# LiasettingsCustomBatchRequestEntry


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** | The ID of the account for which to get/update account LIA settings. |  [optional] |
|**batchId** | **Integer** | An entry ID, unique within the batch request. |  [optional] |
|**contactEmail** | **String** | Inventory validation contact email. Required only for SetInventoryValidationContact. |  [optional] |
|**contactName** | **String** | Inventory validation contact name. Required only for SetInventoryValidationContact. |  [optional] |
|**country** | **String** | The country code. Required only for RequestInventoryVerification. |  [optional] |
|**gmbEmail** | **String** | The Business Profile. Required only for RequestGmbAccess. |  [optional] |
|**liaSettings** | [**LiaSettings**](LiaSettings.md) |  |  [optional] |
|**merchantId** | **String** | The ID of the managing account. |  [optional] |
|**method** | **String** | The method of the batch entry. Acceptable values are: - \&quot;&#x60;get&#x60;\&quot; - \&quot;&#x60;getAccessibleGmbAccounts&#x60;\&quot; - \&quot;&#x60;requestGmbAccess&#x60;\&quot; - \&quot;&#x60;requestInventoryVerification&#x60;\&quot; - \&quot;&#x60;setInventoryVerificationContact&#x60;\&quot; - \&quot;&#x60;update&#x60;\&quot;  |  [optional] |
|**omnichannelExperience** | [**LiaOmnichannelExperience**](LiaOmnichannelExperience.md) |  |  [optional] |
|**posDataProviderId** | **String** | The ID of POS data provider. Required only for SetPosProvider. |  [optional] |
|**posExternalAccountId** | **String** | The account ID by which this merchant is known to the POS provider. |  [optional] |



