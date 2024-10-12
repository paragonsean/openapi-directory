

# HostedZoneSummary

In the response to a <code>ListHostedZonesByVPC</code> request, the <code>HostedZoneSummaries</code> element contains one <code>HostedZoneSummary</code> element for each hosted zone that the specified Amazon VPC is associated with. Each <code>HostedZoneSummary</code> element contains the hosted zone name and ID, and information about who owns the hosted zone.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**hostedZoneId** | [**String**](String.md) |  |  |
|**name** | [**String**](String.md) |  |  |
|**owner** | [**HostedZoneSummaryOwner**](HostedZoneSummaryOwner.md) |  |  |



