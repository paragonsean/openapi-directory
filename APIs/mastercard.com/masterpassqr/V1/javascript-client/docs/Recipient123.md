# SendPersonToMerchant.Recipient123

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | [**Address124**](Address124.md) |  | 
**dateOfBirth** | **String** | The consumer&#39;s date of birth as an ISO 8601 Full Date. Valid Values- Refer &#39;Date And Time Formats&#39; | [optional] 
**email** | **String** | Recipient&#39;s email address. Phone number or Email should be provided if the partner is set up to receive notifications. Details- Conditional | [optional] 
**firstName** | **String** | Recipient’s first name. Details- alpha, 1-40 | 
**governmentIds** | [**GovernmentIds125**](GovernmentIds125.md) |  | [optional] 
**lastName** | **String** | Recipient’s last name. Details- alpha, 1-40 | 
**merchantCategoryCode** | **String** | Mastercard defined merchant category code. This identifies the type of business of the recipient/merchant. This merchant category code should match valid code set by Mastercard rules. \\n\\nType: Numeric [0-9], Length: 1-4 | 
**middleName** | **String** | Recipient middle_name. Details- alpha, 40 | [optional] 
**nationality** | **String** | The recipient home country as an ISO 3166-1 alpha-3 country code, In uppercase. Details- alpha, 3 | [optional] 
**phone** | **String** | Recipient&#39;s phone number, including country code. Phone number or Email should be provided if the partner is set up to receive notifications. Details- Conditional, 1-15 | [optional] 


