

# Verification


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**account** | [**VerificationAccount**](VerificationAccount.md) |  |  [optional] |
|**accountId** | **Long** | Unique identifier for the account.&lt;br&gt;&lt;br&gt;&lt;b&gt;Endpoints&lt;/b&gt;:&lt;ul&gt;&lt;li&gt;POST verification&lt;/li&gt;&lt;li&gt;GET verification&lt;/li&gt;&lt;li&gt;PUT verification&lt;/li&gt;&lt;/ul&gt; |  [optional] |
|**providerAccountId** | **Long** | Unique identifier for the provider account.&lt;br&gt;&lt;br&gt;&lt;b&gt;Endpoints&lt;/b&gt;:&lt;ul&gt;&lt;li&gt;POST verification&lt;/li&gt;&lt;li&gt;GET verification&lt;/li&gt;&lt;li&gt;PUT verification&lt;/li&gt;&lt;/ul&gt; |  [optional] |
|**reason** | [**ReasonEnum**](#ReasonEnum) | The reason the account verification failed.&lt;br&gt;&lt;br&gt;&lt;b&gt;Endpoints&lt;/b&gt;:&lt;ul&gt;&lt;li&gt;POST verification&lt;/li&gt;&lt;li&gt;GET verification&lt;/li&gt;&lt;li&gt;PUT verification&lt;/li&gt;&lt;/ul&gt; |  [optional] [readonly] |
|**verificationDate** | **String** | The date of the account verification.&lt;br&gt;&lt;br&gt;&lt;b&gt;Endpoints&lt;/b&gt;:&lt;ul&gt;&lt;li&gt;POST verification&lt;/li&gt;&lt;li&gt;GET verification&lt;/li&gt;&lt;li&gt;PUT verification&lt;/li&gt;&lt;/ul&gt; |  [optional] [readonly] |
|**verificationId** | **Long** | Unique identifier for the verification request.&lt;br&gt;&lt;br&gt;&lt;b&gt;Endpoints&lt;/b&gt;:&lt;ul&gt;&lt;li&gt;POST verification&lt;/li&gt;&lt;li&gt;GET verification&lt;/li&gt;&lt;li&gt;PUT verification&lt;/li&gt;&lt;/ul&gt; |  [optional] [readonly] |
|**verificationStatus** | [**VerificationStatusEnum**](#VerificationStatusEnum) | The status of the account verification.&lt;br&gt;&lt;br&gt;&lt;b&gt;Endpoints&lt;/b&gt;:&lt;ul&gt;&lt;li&gt;POST verification&lt;/li&gt;&lt;li&gt;GET verification&lt;/li&gt;&lt;li&gt;PUT verification&lt;/li&gt;&lt;/ul&gt;&lt;br&gt;&lt;b&gt;Applicable Values&lt;/b&gt; |  [optional] [readonly] |
|**verificationType** | [**VerificationTypeEnum**](#VerificationTypeEnum) | The account verification type.&lt;br&gt;&lt;br&gt;&lt;b&gt;Endpoints&lt;/b&gt;:&lt;ul&gt;&lt;li&gt;POST verification&lt;/li&gt;&lt;li&gt;GET verification&lt;/li&gt;&lt;li&gt;PUT verification&lt;/li&gt;&lt;/ul&gt;&lt;br&gt;&lt;b&gt;Applicable Values&lt;/b&gt; |  [optional] |



## Enum: ReasonEnum

| Name | Value |
|---- | -----|
| DATA_NOT_AVAILABLE | &quot;DATA_NOT_AVAILABLE&quot; |
| ACCOUNT_HOLDER_MISMATCH | &quot;ACCOUNT_HOLDER_MISMATCH&quot; |
| FULL_ACCOUNT_NUMBER_AND_BANK_TRANSFER_CODE_NOT_AVAILABLE | &quot;FULL_ACCOUNT_NUMBER_AND_BANK_TRANSFER_CODE_NOT_AVAILABLE&quot; |
| FULL_ACCOUNT_NUMBER_NOT_AVAILABLE | &quot;FULL_ACCOUNT_NUMBER_NOT_AVAILABLE&quot; |
| BANK_TRANSFER_CODE_NOT_AVAILABLE | &quot;BANK_TRANSFER_CODE_NOT_AVAILABLE&quot; |
| EXPIRED | &quot;EXPIRED&quot; |
| DATA_MISMATCH | &quot;DATA_MISMATCH&quot; |
| INSTRUCTION_GENERATION_ERROR | &quot;INSTRUCTION_GENERATION_ERROR&quot; |



## Enum: VerificationStatusEnum

| Name | Value |
|---- | -----|
| INITIATED | &quot;INITIATED&quot; |
| DEPOSITED | &quot;DEPOSITED&quot; |
| SUCCESS | &quot;SUCCESS&quot; |
| FAILED | &quot;FAILED&quot; |



## Enum: VerificationTypeEnum

| Name | Value |
|---- | -----|
| MATCHING | &quot;MATCHING&quot; |
| CHALLENGE_DEPOSIT | &quot;CHALLENGE_DEPOSIT&quot; |



