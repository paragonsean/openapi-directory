

# SupersimV1EsimProfile


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountSid** | **String** | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) to which the eSIM Profile resource belongs. |  [optional] |
|**activationCode** | **String** | Combined machine-readable activation code for acquiring an eSIM Profile with the Activation Code download method. Can be used in a QR code to download an eSIM profile. |  [optional] |
|**dateCreated** | **OffsetDateTime** | The date and time in GMT when the resource was created specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. |  [optional] |
|**dateUpdated** | **OffsetDateTime** | The date and time in GMT when the resource was last updated specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. |  [optional] |
|**eid** | **String** | Identifier of the eUICC that can claim the eSIM Profile. |  [optional] |
|**errorCode** | **String** | Code indicating the failure if the download of the SIM Profile failed and the eSIM Profile is in &#x60;failed&#x60; state. |  [optional] |
|**errorMessage** | **String** | Error message describing the failure if the download of the SIM Profile failed and the eSIM Profile is in &#x60;failed&#x60; state. |  [optional] |
|**iccid** | **String** | The [ICCID](https://en.wikipedia.org/wiki/Subscriber_identity_module#ICCID) associated with the Sim resource. |  [optional] |
|**matchingId** | **String** | Unique identifier of the eSIM profile that can be used to identify and download the eSIM profile from the SM-DP+ server. Populated if &#x60;generate_matching_id&#x60; is set to &#x60;true&#x60; when creating the eSIM profile reservation. |  [optional] |
|**sid** | **String** | The unique string that we created to identify the eSIM Profile resource. |  [optional] |
|**simSid** | **String** | The SID of the [Sim](https://www.twilio.com/docs/iot/supersim/api/sim-resource) resource that this eSIM Profile controls. |  [optional] |
|**smdpPlusAddress** | **URI** | Address of the SM-DP+ server from which the Profile will be downloaded. The URL will appear once the eSIM Profile reaches the status &#x60;available&#x60;. |  [optional] |
|**status** | **EsimProfileEnumStatus** |  |  [optional] |
|**url** | **URI** | The absolute URL of the eSIM Profile resource. |  [optional] |



