

# InboundEnvironmentEndpoint

The IP Addresses and Ports that require inbound network access to and within the subnet of the App Service Environment.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**description** | **String** | Short text describing the purpose of the network traffic. |  [optional] |
|**endpoints** | **List&lt;String&gt;** | The IP addresses that network traffic will originate from in cidr notation. |  [optional] |
|**ports** | **List&lt;String&gt;** | The ports that network traffic will arrive to the App Service Environment at. |  [optional] |



