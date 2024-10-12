# ApiKeysApi.V2Key

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**annotations** | **{String: String}** | Annotations is an unstructured key-value map stored with a policy that may be set by external tools to store and retrieve arbitrary metadata. They are not queryable and should be preserved when modifying objects. | [optional] 
**createTime** | **String** | Output only. A timestamp identifying the time this key was originally created. | [optional] [readonly] 
**deleteTime** | **String** | Output only. A timestamp when this key was deleted. If the resource is not deleted, this must be empty. | [optional] [readonly] 
**displayName** | **String** | Human-readable display name of this key that you can modify. The maximum length is 63 characters. | [optional] 
**etag** | **String** | Output only. A checksum computed by the server based on the current value of the Key resource. This may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding. See https://google.aip.dev/154. | [optional] [readonly] 
**keyString** | **String** | Output only. An encrypted and signed value held by this key. This field can be accessed only through the &#x60;GetKeyString&#x60; method. | [optional] [readonly] 
**name** | **String** | Output only. The resource name of the key. The &#x60;name&#x60; has the form: &#x60;projects//locations/global/keys/&#x60;. For example: &#x60;projects/123456867718/locations/global/keys/b7ff1f9f-8275-410a-94dd-3855ee9b5dd2&#x60; NOTE: Key is a global resource; hence the only supported value for location is &#x60;global&#x60;. | [optional] [readonly] 
**restrictions** | [**V2Restrictions**](V2Restrictions.md) |  | [optional] 
**uid** | **String** | Output only. Unique id in UUID4 format. | [optional] [readonly] 
**updateTime** | **String** | Output only. A timestamp identifying the time this key was last updated. | [optional] [readonly] 


