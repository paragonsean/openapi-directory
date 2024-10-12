

# AccountBusinessInformation


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**address** | [**AccountAddress**](AccountAddress.md) |  |  [optional] |
|**customerService** | [**AccountCustomerService**](AccountCustomerService.md) |  |  [optional] |
|**koreanBusinessRegistrationNumber** | **String** | The 10-digit [Korean business registration number](https://support.google.com/merchants/answer/9037766) separated with dashes in the format: XXX-XX-XXXXX. This field will only be updated if explicitly set. |  [optional] |
|**phoneNumber** | **String** | The phone number of the business in [E.164](https://en.wikipedia.org/wiki/E.164) format. This can only be updated if a verified phone number is not already set. To replace a verified phone number use the &#x60;Accounts.requestphoneverification&#x60; and &#x60;Accounts.verifyphonenumber&#x60;. |  [optional] |
|**phoneVerificationStatus** | **String** | Verification status of the phone number of the business. This status is read only and can be updated only by successful phone verification. Acceptable values are: - \&quot;&#x60;verified&#x60;\&quot; - \&quot;&#x60;unverified&#x60;\&quot;  |  [optional] |



