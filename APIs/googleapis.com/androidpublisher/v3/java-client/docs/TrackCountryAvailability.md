

# TrackCountryAvailability

Resource for per-track country availability information.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**countries** | [**List&lt;TrackTargetedCountry&gt;**](TrackTargetedCountry.md) | A list of one or more countries where artifacts in this track are available. This list includes all countries that are targeted by the track, even if only specific carriers are targeted in that country. |  [optional] |
|**restOfWorld** | **Boolean** | Whether artifacts in this track are available to \&quot;rest of the world\&quot; countries. |  [optional] |
|**syncWithProduction** | **Boolean** | Whether this track&#39;s availability is synced with the default production track. See https://support.google.com/googleplay/android-developer/answer/7550024 for more information on syncing country availability with production. Note that if this is true, the returned \&quot;countries\&quot; and \&quot;rest_of_world\&quot; fields will reflect the values for the default production track. |  [optional] |



