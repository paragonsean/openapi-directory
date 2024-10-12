

# UpdateAccountHolderRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountHolderCode** | **String** | The code of the Account Holder to be updated. |  |
|**accountHolderDetails** | [**AccountHolderDetails**](AccountHolderDetails.md) | The details to which the Account Holder should be updated.  Required if a processingTier is not provided. |  [optional] |
|**processingTier** | **Integer** | The processing tier to which the Account Holder should be updated. &gt;The processing tier can not be lowered through this request.  &gt;Required if accountHolderDetails are not provided. |  [optional] |



