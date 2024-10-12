

# GetInfoForObservedBeaconsRequest

Request for beacon and attachment information about beacons that a mobile client has encountered \"in the wild\".

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**namespacedTypes** | **List&lt;String&gt;** | Specifies what kind of attachments to include in the response. When given, the response will include only attachments of the given types. When empty, no attachments will be returned. Must be in the format namespace/type. Accepts &#x60;*&#x60; to specify all types in all namespaces owned by the client. Optional. |  [optional] |
|**observations** | [**List&lt;Observation&gt;**](Observation.md) | The beacons that the client has encountered. At least one must be given. |  [optional] |



