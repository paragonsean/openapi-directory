

# AliasTarget

<p> <i>Alias resource record sets only:</i> Information about the Amazon Web Services resource, such as a CloudFront distribution or an Amazon S3 bucket, that you want to route traffic to.</p> <p>When creating resource record sets for a private hosted zone, note the following:</p> <ul> <li> <p>For information about creating failover resource record sets in a private hosted zone, see <a href=\"https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-private-hosted-zones.html\">Configuring Failover in a Private Hosted Zone</a>.</p> </li> </ul>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**hostedZoneId** | [**String**](String.md) |  |  |
|**dnSName** | [**String**](String.md) |  |  |
|**evaluateTargetHealth** | [**Boolean**](Boolean.md) |  |  |



