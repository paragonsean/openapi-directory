

# ChannelConversionPing

Pings that the app shall fire (authenticated by biscotti cookie). Each ping has a context, in which the app must fire the ping, and a url identifying the ping.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**context** | [**ContextEnum**](#ContextEnum) | Defines the context of the ping. |  [optional] |
|**conversionUrl** | **String** | The url (without the schema) that the player shall send the ping to. It&#39;s at caller&#39;s descretion to decide which schema to use (http vs https) Example of a returned url: //googleads.g.doubleclick.net/pagead/ viewthroughconversion/962985656/?data&#x3D;path%3DtHe_path%3Btype%3D cview%3Butuid%3DGISQtTNGYqaYl4sKxoVvKA&amp;labe&#x3D;default The caller must append biscotti authentication (ms param in case of mobile, for example) to this ping. |  [optional] |



## Enum: ContextEnum

| Name | Value |
|---- | -----|
| SUBSCRIBE | &quot;subscribe&quot; |
| UNSUBSCRIBE | &quot;unsubscribe&quot; |
| CVIEW | &quot;cview&quot; |



