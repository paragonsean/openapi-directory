

# PhoneNumbers

A collection of phone numbers for the business. During updates, both fields must be set. Clients may not update just the primary or additional phone numbers using the update mask. International phone format is preferred, such as \"+1 415 555 0132\", see more in (https://developers.google.com/style/phone-numbers#international-phone-numbers).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**additionalPhones** | **List&lt;String&gt;** | Optional. Up to two phone numbers (mobile or landline, no fax) at which your business can be called, in addition to your primary phone number. |  [optional] |
|**primaryPhone** | **String** | Required. A phone number that connects to your individual business location as directly as possible. Use a local phone number instead of a central, call center helpline number whenever possible. |  [optional] |



