

# NewCustomerResponse

Customer information

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**activationCode** | **String** | &amp;#128679; Deprecated since v4.8.0  Customer activation code string:  * valid only for types &#x60;free&#x60; and &#x60;demo&#x60;  * for &#x60;pay&#x60; customers it is empty |  [optional] |
|**companyName** | **String** | Company name |  |
|**createdAt** | **OffsetDateTime** | Creation date |  [optional] |
|**customerAttributes** | [**CustomerAttributes**](CustomerAttributes.md) |  |  [optional] |
|**customerContractType** | [**CustomerContractTypeEnum**](#CustomerContractTypeEnum) | Customer type |  |
|**customerUuid** | **String** | &amp;#128640; Since v4.21.0  Customer UUID |  |
|**firstAdminUser** | [**FirstAdminUser**](FirstAdminUser.md) |  |  |
|**id** | **Long** | Unique identifier for the customer |  [optional] |
|**isLocked** | **Boolean** | Customer is locked:  * &#x60;false&#x60; - unlocked  * &#x60;true&#x60; - locked    All users of this customer will be blocked and can not login anymore. |  [optional] |
|**lockStatus** | **Boolean** | &amp;#128679; Deprecated since v4.7.0  Customer lock status:  * &#x60;false&#x60; - unlocked  * &#x60;true&#x60; - locked    Please use &#x60;isLocked&#x60; instead.  All users of this customer will be blocked and can not login anymore. |  |
|**providerCustomerId** | **String** | Provider customer ID |  [optional] |
|**quotaMax** | **Long** | Maximal disc space which can be allocated by customer in bytes. -1 for unlimited |  |
|**trialDays** | **Integer** | Number of days left for trial period (relevant only for type &#x60;demo&#x60;)  (not used) |  [optional] |
|**userMax** | **Integer** | Maximal number of users |  |
|**webhooksMax** | **Long** | &amp;#128640; Since v4.19.0  Maximal number of webhooks |  [optional] |



## Enum: CustomerContractTypeEnum

| Name | Value |
|---- | -----|
| DEMO | &quot;demo&quot; |
| FREE | &quot;free&quot; |
| PAY | &quot;pay&quot; |



