

# UpdateDomainRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**defaultExpirationDays** | **Integer** | The default number of days until the data within the domain expires. |  [optional] |
|**defaultEncryptionKey** | **String** | The default encryption key, which is an AWS managed key, is used when no specific type of encryption key is specified. It is used to encrypt all data before it is placed in permanent or semi-permanent storage. If specified as an empty string, it will clear any existing value. |  [optional] |
|**deadLetterQueueUrl** | **String** | The URL of the SQS dead letter queue, which is used for reporting errors associated with ingesting data from third party applications. If specified as an empty string, it will clear any existing value. You must set up a policy on the DeadLetterQueue for the SendMessage operation to enable Amazon Connect Customer Profiles to send messages to the DeadLetterQueue. |  [optional] |
|**matching** | [**UpdateDomainRequestMatching**](UpdateDomainRequestMatching.md) |  |  [optional] |
|**ruleBasedMatching** | [**UpdateDomainRequestRuleBasedMatching**](UpdateDomainRequestRuleBasedMatching.md) |  |  [optional] |
|**tags** | **Map&lt;String, String&gt;** | The tags used to organize, track, or control access for this resource. |  [optional] |



