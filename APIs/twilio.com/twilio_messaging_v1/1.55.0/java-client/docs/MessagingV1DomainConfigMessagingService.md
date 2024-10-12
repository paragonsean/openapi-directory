

# MessagingV1DomainConfigMessagingService


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**callbackUrl** | **URI** | URL to receive click events to your webhook whenever the recipients click on the shortened links. |  [optional] |
|**configSid** | **String** | The unique string that we created to identify the Domain config (prefix ZK). |  [optional] |
|**continueOnFailure** | **Boolean** | Boolean field to set customer delivery preference when there is a failure in linkShortening service |  [optional] |
|**dateCreated** | **OffsetDateTime** | Date this Domain Config was created. |  [optional] |
|**dateUpdated** | **OffsetDateTime** | Date that this Domain Config was last updated. |  [optional] |
|**domainSid** | **String** | The unique string that we created to identify the Domain resource. |  [optional] |
|**fallbackUrl** | **URI** | Any requests we receive to this domain that do not match an existing shortened message will be redirected to the fallback url. These will likely be either expired messages, random misdirected traffic, or intentional scraping. |  [optional] |
|**messagingServiceSid** | **String** | The unique string that identifies the messaging service |  [optional] |
|**url** | **URI** |  |  [optional] |



