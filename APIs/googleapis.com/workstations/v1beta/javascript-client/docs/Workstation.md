# CloudWorkstationsApi.Workstation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**annotations** | **{String: String}** | Optional. Client-specified annotations. | [optional] 
**createTime** | **String** | Output only. Time when this workstation was created. | [optional] [readonly] 
**deleteTime** | **String** | Output only. Time when this workstation was soft-deleted. | [optional] [readonly] 
**displayName** | **String** | Optional. Human-readable name for this workstation. | [optional] 
**env** | **{String: String}** | Optional. Environment variables passed to the workstation container&#39;s entrypoint. | [optional] 
**etag** | **String** | Optional. Checksum computed by the server. May be sent on update and delete requests to make sure that the client has an up-to-date value before proceeding. | [optional] 
**host** | **String** | Output only. Host to which clients can send HTTPS traffic that will be received by the workstation. Authorized traffic will be received to the workstation as HTTP on port 80. To send traffic to a different port, clients may prefix the host with the destination port in the format &#x60;{port}-{host}&#x60;. | [optional] [readonly] 
**kmsKey** | **String** | Output only. The name of the Google Cloud KMS encryption key used to encrypt this workstation. The KMS key can only be configured in the WorkstationConfig. The expected format is &#x60;projects/_*_/locations/_*_/keyRings/_*_/cryptoKeys/_*&#x60;. | [optional] [readonly] 
**labels** | **{String: String}** | Optional. [Labels](https://cloud.google.com/workstations/docs/label-resources) that are applied to the workstation and that are also propagated to the underlying Compute Engine resources. | [optional] 
**name** | **String** | Identifier. Full name of this workstation. | [optional] 
**reconciling** | **Boolean** | Output only. Indicates whether this workstation is currently being updated to match its intended state. | [optional] [readonly] 
**startTime** | **String** | Output only. Time when this workstation was most recently successfully started, regardless of the workstation&#39;s initial state. | [optional] [readonly] 
**state** | **String** | Output only. Current state of the workstation. | [optional] [readonly] 
**uid** | **String** | Output only. A system-assigned unique identifier for this workstation. | [optional] [readonly] 
**updateTime** | **String** | Output only. Time when this workstation was most recently updated. | [optional] [readonly] 



## Enum: StateEnum


* `UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `STARTING` (value: `"STATE_STARTING"`)

* `RUNNING` (value: `"STATE_RUNNING"`)

* `STOPPING` (value: `"STATE_STOPPING"`)

* `STOPPED` (value: `"STATE_STOPPED"`)




