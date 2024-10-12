

# Sender130

Information about the sender of the transaction.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**additionalMerchantData** | [**AdditionalMerchantData132**](AdditionalMerchantData132.md) |  |  [optional] |
|**address** | [**Address131**](Address131.md) |  |  [optional] |
|**dateOfBirth** | **String** | Date of birth of the sender as an ISO 8601 Full Date. |  [optional] |
|**email** | **String** | Email address of the sender. |  [optional] |
|**firstName** | **String** | Sender’s first name. Details- alpha, 1-40 |  [optional] |
|**governmentIds** | [**GovernmentIds133**](GovernmentIds133.md) |  |  [optional] |
|**lastName** | **String** | Sender’s last name. |  [optional] |
|**middleName** | **String** | Middle name of the sender. Details- alpha, 40 |  [optional] |
|**nationality** | **String** | The senders home country as an ISO 3166-1 alpha-3 country code. |  [optional] |
|**phone** | **String** | Phone number of the sender. |  [optional] |
|**sanctionScore** | **String** | A value ranging from 0 to 100. A higher score indicates a closer match to names on the applicable screening list, while lower scores indicate a less likely match.  Available in response when partner is enabled for Sanction Screening validation and sanction_screening_override value is “false”. |  [optional] |



