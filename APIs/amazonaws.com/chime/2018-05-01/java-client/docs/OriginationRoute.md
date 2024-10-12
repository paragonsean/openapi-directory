

# OriginationRoute

<p>Origination routes define call distribution properties for your SIP hosts to receive inbound calls using your Amazon Chime Voice Connector. Limit: Ten origination routes for each Amazon Chime Voice Connector.</p> <note> <p>The parameters listed below are not required, but you must use at least one. </p> </note>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**host** | [**String**](String.md) |  |  [optional] |
|**port** | [**Integer**](Integer.md) |  |  [optional] |
|**protocol** | [**OriginationRouteProtocol**](OriginationRouteProtocol.md) |  |  [optional] |
|**priority** | [**Integer**](Integer.md) |  |  [optional] |
|**weight** | [**Integer**](Integer.md) |  |  [optional] |



