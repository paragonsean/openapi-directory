

# BeneficiarySetupNotificationContent


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**destinationAccountCode** | **String** | The code of the beneficiary account. |  [optional] |
|**destinationAccountHolderCode** | **String** | The code of the beneficiary Account Holder. |  [optional] |
|**invalidFields** | [**List&lt;ErrorFieldType&gt;**](ErrorFieldType.md) | A listing of the invalid fields which have caused the Setup Beneficiary request to fail. If this is empty, the Setup Beneficiary request has succeeded. |  [optional] |
|**merchantReference** | **String** | The reference provided by the merchant. |  [optional] |
|**sourceAccountCode** | **String** | The code of the benefactor account. |  [optional] |
|**sourceAccountHolderCode** | **String** | The code of the benefactor Account Holder. |  [optional] |
|**transferDate** | **OffsetDateTime** | The date on which the beneficiary was set up and funds transferred from benefactor to beneficiary. |  [optional] |



