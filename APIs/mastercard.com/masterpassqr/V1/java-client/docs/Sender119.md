

# Sender119

Sender information is required for non-tokenized transactions. If a pan number is provided directly, the sender information should be provided. Details- Conditional

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**additionalMerchantData** | [**AdditionalMerchantData121**](AdditionalMerchantData121.md) |  |  [optional] |
|**address** | [**Address120**](Address120.md) |  |  [optional] |
|**dateOfBirth** | **String** | The consumer&#39;s date of birth as an ISO 8601 Full Date. Valid Values- Refer &#39;Date And Time Formats&#39; |  [optional] |
|**email** | **String** | Sender&#39;s email address. Phone number or Email should be provided if the partner is set up to receive notifications. Details- Conditional |  [optional] |
|**firstName** | **String** | Sender’s first name. Details- alpha, 1-40 |  |
|**governmentIds** | [**GovernmentIds122**](GovernmentIds122.md) |  |  [optional] |
|**lastName** | **String** | Sender’s last name. Details- alpha, 1-40 |  |
|**middleName** | **String** | Middle name of the sender. Details- alpha, 40 |  [optional] |
|**nationality** | **String** | The senders home country as an ISO 3166-1 alpha-3 country code, In uppercase. Details- alpha, 3 |  [optional] |
|**phone** | **String** | Sender&#39;s phone number, including country code. Phone number or Email should be provided if the partner is set up to receive notifications. Details- Conditional, 1-15 |  [optional] |



