

# ExternalAccount

External Accounts represent accounts at financial institutions other than Increase. You can use this API to store their details for reuse.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountNumber** | **String** | The destination account number. |  |
|**createdAt** | **OffsetDateTime** | The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time at which the External Account was created. |  |
|**description** | **String** | The External Account&#39;s description for display purposes. |  |
|**funding** | [**FundingEnum**](#FundingEnum) | The type of the account to which the transfer will be sent. |  |
|**id** | **String** | The External Account&#39;s identifier. |  |
|**routingNumber** | **String** | The American Bankers&#39; Association (ABA) Routing Transit Number (RTN). |  |
|**status** | [**StatusEnum**](#StatusEnum) | The External Account&#39;s status. |  |
|**type** | [**TypeEnum**](#TypeEnum) | A constant representing the object&#39;s type. For this resource it will always be &#x60;external_account&#x60;. |  |
|**verificationStatus** | [**VerificationStatusEnum**](#VerificationStatusEnum) | If you have verified ownership of the External Account. |  |



## Enum: FundingEnum

| Name | Value |
|---- | -----|
| CHECKING | &quot;checking&quot; |
| SAVINGS | &quot;savings&quot; |
| OTHER | &quot;other&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;active&quot; |
| ARCHIVED | &quot;archived&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| EXTERNAL_ACCOUNT | &quot;external_account&quot; |



## Enum: VerificationStatusEnum

| Name | Value |
|---- | -----|
| UNVERIFIED | &quot;unverified&quot; |
| PENDING | &quot;pending&quot; |
| VERIFIED | &quot;verified&quot; |



