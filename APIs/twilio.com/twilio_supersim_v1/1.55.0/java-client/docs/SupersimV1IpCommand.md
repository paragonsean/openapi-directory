

# SupersimV1IpCommand


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountSid** | **String** | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the IP Command resource. |  [optional] |
|**dateCreated** | **OffsetDateTime** | The date and time in GMT when the resource was created specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. |  [optional] |
|**dateUpdated** | **OffsetDateTime** | The date and time in GMT when the resource was last updated specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. |  [optional] |
|**deviceIp** | **String** | The IP address of the device that the IP Command was sent to or received from. For an IP Command sent to a Super SIM, &#x60;device_ip&#x60; starts out as &#x60;null&#x60;, and once the IP Command is “sent”, the &#x60;device_ip&#x60; will be filled out. An IP Command sent from a Super SIM have its &#x60;device_ip&#x60; always set. |  [optional] |
|**devicePort** | **Integer** | For an IP Command sent to a Super SIM, it would be the destination port of the IP message. For an IP Command sent from a Super SIM, it would be the source port of the IP message. |  [optional] |
|**direction** | **IpCommandEnumDirection** |  |  [optional] |
|**payload** | **String** | The payload that is carried in the IP/UDP message. The payload can be encoded in either text or binary format. For text payload, UTF-8 encoding must be used.  For an IP Command sent to a Super SIM, the payload is appended to the IP/UDP message “as is”. The payload should not exceed 1300 bytes.  For an IP Command sent from a Super SIM, the payload from the received IP/UDP message is extracted and sent in binary encoding. For an IP Command sent from a Super SIM, the payload should not exceed 1300 bytes. If it is larger than 1300 bytes, there might be fragmentation on the upstream and the message may appear truncated. |  [optional] |
|**payloadType** | **IpCommandEnumPayloadType** |  |  [optional] |
|**sid** | **String** | The unique string that we created to identify the IP Command resource. |  [optional] |
|**simIccid** | **String** | The [ICCID](https://en.wikipedia.org/wiki/Subscriber_identity_module#ICCID) of the [Super SIM](https://www.twilio.com/docs/iot/supersim/api/sim-resource) that this IP Command was sent to or from. |  [optional] |
|**simSid** | **String** | The SID of the [Super SIM](https://www.twilio.com/docs/iot/supersim/api/sim-resource) that this IP Command was sent to or from. |  [optional] |
|**status** | **IpCommandEnumStatus** |  |  [optional] |
|**url** | **URI** | The absolute URL of the IP Command resource. |  [optional] |



