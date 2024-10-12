

# SetIdentityMailFromDomainRequest

Represents a request to enable or disable the Amazon SES custom MAIL FROM domain setup for a verified identity. For information about using a custom MAIL FROM domain, see the <a href=\"https://docs.aws.amazon.com/ses/latest/DeveloperGuide/mail-from.html\">Amazon SES Developer Guide</a>.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**identity** | [**String**](String.md) |  |  |
|**mailFromDomain** | [**String**](String.md) |  |  [optional] |
|**behaviorOnMXFailure** | [**BehaviorOnMXFailure**](BehaviorOnMXFailure.md) |  |  [optional] |



