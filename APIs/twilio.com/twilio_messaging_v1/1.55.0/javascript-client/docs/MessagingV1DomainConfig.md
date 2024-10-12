# TwilioMessaging.MessagingV1DomainConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**callbackUrl** | **String** | URL to receive click events to your webhook whenever the recipients click on the shortened links. | [optional] 
**configSid** | **String** | The unique string that we created to identify the Domain config (prefix ZK). | [optional] 
**continueOnFailure** | **Boolean** | Boolean field to set customer delivery preference when there is a failure in linkShortening service | [optional] 
**dateCreated** | **Date** | Date this Domain Config was created. | [optional] 
**dateUpdated** | **Date** | Date that this Domain Config was last updated. | [optional] 
**disableHttps** | **Boolean** | Customer&#39;s choice to send links with/without \&quot;https://\&quot; attached to shortened url. If true, messages will not be sent with https:// at the beginning of the url. If false, messages will be sent with https:// at the beginning of the url. False is the default behavior if it is not specified. | [optional] 
**domainSid** | **String** | The unique string that we created to identify the Domain resource. | [optional] 
**fallbackUrl** | **String** | Any requests we receive to this domain that do not match an existing shortened message will be redirected to the fallback url. These will likely be either expired messages, random misdirected traffic, or intentional scraping. | [optional] 
**url** | **String** |  | [optional] 


