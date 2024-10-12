

# Recipient134

Information about the recipient of the transaction.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**address** | [**Address135**](Address135.md) |  |  [optional] |
|**dateOfBirth** | **String** | Date of birth of the recipient as an ISO 8601 Full Date. Valid Values- Refer &#39;Date And Time Formats&#39; |  [optional] |
|**email** | **String** | Email address of the recipient. |  [optional] |
|**firstName** | **String** | Recipient’s first name. |  [optional] |
|**governmentIds** | [**GovernmentIds136**](GovernmentIds136.md) |  |  [optional] |
|**lastName** | **String** | Recipient’s last name. |  [optional] |
|**merchantCategoryCode** | **String** | Mastercard defined merchant category code. This identifies the type of business of the recipient/merchant. \\n\\nType: Numeric [0-9], Maximum Length: 4 |  [optional] |
|**middleName** | **String** | Recipient middle_name. Details- alpha, 40 |  [optional] |
|**nationality** | **String** | The recipient home country as an ISO 3166-1 alpha-3 country code. |  [optional] |
|**phone** | **String** | Phone number of the recipient. |  [optional] |
|**sanctionScore** | **String** | A value ranging from 0 to 100. A higher score indicates a closer match to names on the applicable screening list, while lower scores indicate a less likely match.  Available in response when partner is enabled for Sanction Screening validation and sanction_screening_override value is “false”. |  [optional] |



