

# DomainDeliverabilityCampaign

An object that contains the deliverability data for a specific campaign. This data is available for a campaign only if the campaign sent email by using a domain that the Deliverability dashboard is enabled for (<code>PutDeliverabilityDashboardOption</code> operation).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**campaignId** | [**String**](String.md) |  |  [optional] |
|**imageUrl** | [**String**](String.md) |  |  [optional] |
|**subject** | [**String**](String.md) |  |  [optional] |
|**fromAddress** | [**String**](String.md) |  |  [optional] |
|**sendingIps** | [**List**](List.md) |  |  [optional] |
|**firstSeenDateTime** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**lastSeenDateTime** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**inboxCount** | [**Integer**](Integer.md) |  |  [optional] |
|**spamCount** | [**Integer**](Integer.md) |  |  [optional] |
|**readRate** | [**Double**](Double.md) |  |  [optional] |
|**deleteRate** | [**Double**](Double.md) |  |  [optional] |
|**readDeleteRate** | [**Double**](Double.md) |  |  [optional] |
|**projectedVolume** | [**Integer**](Integer.md) |  |  [optional] |
|**esps** | [**List**](List.md) |  |  [optional] |



