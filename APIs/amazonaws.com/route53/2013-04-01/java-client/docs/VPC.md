

# VPC

<p>(Private hosted zones only) A complex type that contains information about an Amazon VPC.</p> <p>If you associate a private hosted zone with an Amazon VPC when you make a <a href=\"https://docs.aws.amazon.com/Route53/latest/APIReference/API_CreateHostedZone.html\">CreateHostedZone</a> request, the following parameters are also required.</p>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**vpCRegion** | [**VPCRegion**](VPCRegion.md) |  |  [optional] |
|**vpCId** | **String** | (Private hosted zones only) The ID of an Amazon VPC.  |  [optional] |



