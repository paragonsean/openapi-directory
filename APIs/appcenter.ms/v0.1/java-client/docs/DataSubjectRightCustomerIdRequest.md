

# DataSubjectRightCustomerIdRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dataSubjectIdentifier** | **String** | customer account id (b2c identifier) / customer user id (free form text) depending on the value of the fied &#x60;type&#x60; |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | type of the customer dataSubjectIdentifier |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| CUSTOMER_ACCOUNT_ID | &quot;CustomerAccountId&quot; |
| CUSTOMER_USER_ID | &quot;CustomerUserId&quot; |



