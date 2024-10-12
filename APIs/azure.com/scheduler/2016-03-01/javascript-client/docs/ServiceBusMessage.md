# SchedulerManagementClient.ServiceBusMessage

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authentication** | [**ServiceBusAuthentication**](ServiceBusAuthentication.md) |  | [optional] 
**brokeredMessageProperties** | [**ServiceBusBrokeredMessageProperties**](ServiceBusBrokeredMessageProperties.md) |  | [optional] 
**customMessageProperties** | **{String: String}** | Gets or sets the custom message properties. | [optional] 
**message** | **String** | Gets or sets the message. | [optional] 
**namespace** | **String** | Gets or sets the namespace. | [optional] 
**transportType** | **String** | Gets or sets the transport type. | [optional] 



## Enum: TransportTypeEnum


* `NotSpecified` (value: `"NotSpecified"`)

* `NetMessaging` (value: `"NetMessaging"`)

* `AMQP` (value: `"AMQP"`)




