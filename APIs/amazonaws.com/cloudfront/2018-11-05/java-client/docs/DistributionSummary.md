

# DistributionSummary

A summary of the information about a CloudFront distribution.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | [**String**](String.md) |  |  |
|**ARN** | [**String**](String.md) |  |  |
|**status** | [**String**](String.md) |  |  |
|**lastModifiedTime** | [**OffsetDateTime**](OffsetDateTime.md) |  |  |
|**domainName** | [**String**](String.md) |  |  |
|**aliases** | [**CreateDistribution20181105RequestDistributionConfigAliases**](CreateDistribution20181105RequestDistributionConfigAliases.md) |  |  |
|**origins** | [**DistributionSummaryOrigins**](DistributionSummaryOrigins.md) |  |  |
|**originGroups** | [**CreateDistribution20181105RequestDistributionConfigOriginGroups**](CreateDistribution20181105RequestDistributionConfigOriginGroups.md) |  |  [optional] |
|**defaultCacheBehavior** | [**CreateDistribution20181105RequestDistributionConfigDefaultCacheBehavior**](CreateDistribution20181105RequestDistributionConfigDefaultCacheBehavior.md) |  |  |
|**cacheBehaviors** | [**DistributionSummaryCacheBehaviors**](DistributionSummaryCacheBehaviors.md) |  |  |
|**customErrorResponses** | [**DistributionSummaryCustomErrorResponses**](DistributionSummaryCustomErrorResponses.md) |  |  |
|**comment** | [**String**](String.md) |  |  |
|**priceClass** | [**PriceClass**](PriceClass.md) |  |  |
|**enabled** | [**Boolean**](Boolean.md) |  |  |
|**viewerCertificate** | [**CreateDistribution20181105RequestDistributionConfigViewerCertificate**](CreateDistribution20181105RequestDistributionConfigViewerCertificate.md) |  |  |
|**restrictions** | [**CreateDistribution20181105RequestDistributionConfigRestrictions**](CreateDistribution20181105RequestDistributionConfigRestrictions.md) |  |  |
|**webACLId** | [**String**](String.md) |  |  |
|**httpVersion** | [**HttpVersion**](HttpVersion.md) |  |  |
|**isIPV6Enabled** | [**Boolean**](Boolean.md) |  |  |



