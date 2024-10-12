# AccountApi.UpdateAccountHolderRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountHolderCode** | **String** | The code of the Account Holder to be updated. | 
**accountHolderDetails** | [**AccountHolderDetails**](AccountHolderDetails.md) | The details to which the Account Holder should be updated.  Required if a processingTier is not provided. | [optional] 
**description** | **String** | A description of the account holder, maximum 256 characters. You can use alphanumeric characters (A-Z, a-z, 0-9), white spaces, and underscores &#x60;_&#x60;. | [optional] 
**primaryCurrency** | **String** | The primary three-character [ISO currency code](https://docs.adyen.com/development-resources/currency-codes), to which the account holder should be updated. | [optional] 
**processingTier** | **Number** | The processing tier to which the Account Holder should be updated. &gt;The processing tier can not be lowered through this request.  &gt;Required if accountHolderDetails are not provided. | [optional] 


