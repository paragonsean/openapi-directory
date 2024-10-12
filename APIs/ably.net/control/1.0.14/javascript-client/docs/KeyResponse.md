# ControlApiV1.KeyResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**appId** | **String** | The Ably application ID which this key is associated with. | [optional] 
**capability** | **{String: [String]}** | The capabilities that this key has. More information on capabilities can be found in the &lt;a href&#x3D;\&quot;https://ably.com/documentation/core-features/authentication#capabilities-explained\&quot;&gt;Ably documentation&lt;/a&gt;. | [optional] 
**created** | **Number** | Unix timestamp representing the date and time of creation of the key. | [optional] 
**id** | **String** | The key ID. | [optional] 
**key** | **String** | The complete API key including API secret. | [optional] 
**modified** | **Number** | Unix timestamp representing the date and time of the last modification of the key. | [optional] 
**name** | **String** | The name of the application this key is associated with. | [optional] 



## Enum: {String: [String]}


* `publish` (value: `"publish"`)

* `subscribe` (value: `"subscribe"`)

* `history` (value: `"history"`)

* `presence` (value: `"presence"`)

* `channel-metadata` (value: `"channel-metadata"`)

* `push-admin` (value: `"push-admin"`)

* `push-subscribe` (value: `"push-subscribe"`)

* `statistics` (value: `"statistics"`)




