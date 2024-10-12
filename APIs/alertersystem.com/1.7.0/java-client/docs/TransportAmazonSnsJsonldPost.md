

# TransportAmazonSnsJsonldPost

The TransportAmazonSns resource is a collection of transports that carry dispatched alerts to the external Amazon SNS service.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**amazonSnsAccessKey** | **String** | The access key for the Amazon SNS service. |  |
|**amazonSnsRegion** | **String** | The region for the Amazon SNS service. |  |
|**amazonSnsSecretKey** | **String** | The secret key for the Amazon SNS service. Stored in encrypted format. |  |
|**dataSegmentCode** | **String** | User-provided string on which to segment and filter data. Max 50 characters. |  [optional] |
|**partition** | **String** | The partition that contains this resource instance. The resource cannot be moved to another partition. |  |
|**transportName** | **String** | The name of the transport. |  |



