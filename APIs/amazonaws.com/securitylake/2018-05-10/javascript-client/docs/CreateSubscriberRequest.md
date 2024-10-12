# AmazonSecurityLake.CreateSubscriberRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accessTypes** | [**[AccessType]**](AccessType.md) | The Amazon S3 or Lake Formation access type. | [optional] 
**sources** | [**[LogSourceResource]**](LogSourceResource.md) | The supported Amazon Web Services from which logs and events are collected. Security Lake supports log and event collection for natively supported Amazon Web Services. | 
**subscriberDescription** | **String** | The description for your subscriber account in Security Lake. | [optional] 
**subscriberIdentity** | [**CreateSubscriberRequestSubscriberIdentity**](CreateSubscriberRequestSubscriberIdentity.md) |  | 
**subscriberName** | **String** | The name of your Security Lake subscriber account. | 
**tags** | [**[Tag]**](Tag.md) | An array of objects, one for each tag to associate with the subscriber. For each tag, you must specify both a tag key and a tag value. A tag value cannot be null, but it can be an empty string. | [optional] 


