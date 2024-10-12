# ApigeeApi.GoogleCloudApigeeV1Instance

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**consumerAcceptList** | **[String]** | Optional. Customer accept list represents the list of projects (id/number) on customer side that can privately connect to the service attachment. It is an optional field which the customers can provide during the instance creation. By default, the customer project associated with the Apigee organization will be included to the list. | [optional] 
**createdAt** | **String** | Output only. Time the instance was created in milliseconds since epoch. | [optional] [readonly] 
**description** | **String** | Optional. Description of the instance. | [optional] 
**diskEncryptionKeyName** | **String** | Customer Managed Encryption Key (CMEK) used for disk and volume encryption. Required for Apigee paid subscriptions only. Use the following format: &#x60;projects/([^/]+)/locations/([^/]+)/keyRings/([^/]+)/cryptoKeys/([^/]+)&#x60; | [optional] 
**displayName** | **String** | Optional. Display name for the instance. | [optional] 
**host** | **String** | Output only. Internal hostname or IP address of the Apigee endpoint used by clients to connect to the service. | [optional] [readonly] 
**ipRange** | **String** | Optional. Comma-separated list of CIDR blocks of length 22 and/or 28 used to create the Apigee instance. Providing CIDR ranges is optional. You can provide just /22 or /28 or both (or neither). Ranges you provide should be freely available as part of a larger named range you have allocated to the Service Networking peering. If this parameter is not provided, Apigee automatically requests an available /22 and /28 CIDR block from Service Networking. Use the /22 CIDR block for configuring your firewall needs to allow traffic from Apigee. Input formats: &#x60;a.b.c.d/22&#x60; or &#x60;e.f.g.h/28&#x60; or &#x60;a.b.c.d/22,e.f.g.h/28&#x60; | [optional] 
**lastModifiedAt** | **String** | Output only. Time the instance was last modified in milliseconds since epoch. | [optional] [readonly] 
**location** | **String** | Required. Compute Engine location where the instance resides. | [optional] 
**name** | **String** | Required. Resource ID of the instance. Values must match the regular expression &#x60;^a-z{0,30}[a-z\\d]$&#x60;. | [optional] 
**peeringCidrRange** | **String** | Optional. Size of the CIDR block range that will be reserved by the instance. PAID organizations support &#x60;SLASH_16&#x60; to &#x60;SLASH_20&#x60; and defaults to &#x60;SLASH_16&#x60;. Evaluation organizations support only &#x60;SLASH_23&#x60;. | [optional] 
**port** | **String** | Output only. Port number of the exposed Apigee endpoint. | [optional] [readonly] 
**runtimeVersion** | **String** | Output only. Version of the runtime system running in the instance. The runtime system is the set of components that serve the API Proxy traffic in your Environments. | [optional] [readonly] 
**serviceAttachment** | **String** | Output only. Resource name of the service attachment created for the instance in the format: &#x60;projects/_*_/regions/_*_/serviceAttachments/_*&#x60; Apigee customers can privately forward traffic to this service attachment using the PSC endpoints. | [optional] [readonly] 
**state** | **String** | Output only. State of the instance. Values other than &#x60;ACTIVE&#x60; means the resource is not ready to use. | [optional] [readonly] 



## Enum: PeeringCidrRangeEnum


* `CIDR_RANGE_UNSPECIFIED` (value: `"CIDR_RANGE_UNSPECIFIED"`)

* `SLASH_16` (value: `"SLASH_16"`)

* `SLASH_17` (value: `"SLASH_17"`)

* `SLASH_18` (value: `"SLASH_18"`)

* `SLASH_19` (value: `"SLASH_19"`)

* `SLASH_20` (value: `"SLASH_20"`)

* `SLASH_22` (value: `"SLASH_22"`)

* `SLASH_23` (value: `"SLASH_23"`)





## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `CREATING` (value: `"CREATING"`)

* `ACTIVE` (value: `"ACTIVE"`)

* `DELETING` (value: `"DELETING"`)

* `UPDATING` (value: `"UPDATING"`)




