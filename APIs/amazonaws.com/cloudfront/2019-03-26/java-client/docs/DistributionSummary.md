

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
|**aliases** | [**CreateDistribution20190326RequestDistributionConfigAliases**](CreateDistribution20190326RequestDistributionConfigAliases.md) |  |  |
|**origins** | [**DistributionSummaryOrigins**](DistributionSummaryOrigins.md) |  |  |
|**originGroups** | [**CreateDistribution20190326RequestDistributionConfigOriginGroups**](CreateDistribution20190326RequestDistributionConfigOriginGroups.md) |  |  [optional] |
|**defaultCacheBehavior** | [**CreateDistribution20190326RequestDistributionConfigDefaultCacheBehavior**](CreateDistribution20190326RequestDistributionConfigDefaultCacheBehavior.md) |  |  |
|**cacheBehaviors** | [**DistributionSummaryCacheBehaviors**](DistributionSummaryCacheBehaviors.md) |  |  |
|**customErrorResponses** | [**DistributionSummaryCustomErrorResponses**](DistributionSummaryCustomErrorResponses.md) |  |  |
|**comment** | [**String**](String.md) |  |  |
|**priceClass** | [**PriceClass**](PriceClass.md) |  |  |
|**enabled** | [**Boolean**](Boolean.md) |  |  |
|**viewerCertificate** | [**CreateDistribution20190326RequestDistributionConfigViewerCertificate**](CreateDistribution20190326RequestDistributionConfigViewerCertificate.md) |  |  |
|**restrictions** | [**CreateDistribution20190326RequestDistributionConfigRestrictions**](CreateDistribution20190326RequestDistributionConfigRestrictions.md) |  |  |
|**webACLId** | [**String**](String.md) |  |  |
|**httpVersion** | [**HttpVersion**](HttpVersion.md) |  |  |
|**isIPV6Enabled** | [**Boolean**](Boolean.md) |  |  |
|**aliasICPRecordals** | [**List**](List.md) |  |  [optional] |



