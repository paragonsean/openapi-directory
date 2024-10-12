# LinodeApi.ManagedService

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **String** | The URL at which this Service is monitored.  URL parameters such as &#x60;?no-cache&#x3D;1&#x60; are preserved.  URL fragments/anchors such as &#x60;#monitor&#x60; are **not** preserved.  | [optional] 
**body** | **String** | What to expect to find in the response body for the Service to be considered up.  | [optional] 
**consultationGroup** | **String** | The group of ManagedContacts who should be notified or consulted with when an Issue is detected.  | [optional] 
**created** | **Date** | When this Managed Service was created. | [optional] [readonly] 
**credentials** | **[Number]** | An array of ManagedCredential IDs that should be used when attempting to resolve issues with this Service.  | [optional] 
**id** | **Number** | This Service&#39;s unique ID.  | [optional] [readonly] 
**label** | **String** | The label for this Service. This is for display purposes only.  | [optional] 
**notes** | **String** | Any information relevant to the Service that Linode special forces should know when attempting to resolve Issues.  | [optional] 
**region** | **String** | The Region in which this Service is located. This is required if address is a private IP, and may not be set otherwise.  | [optional] 
**serviceType** | **String** | How this Service is monitored.  | [optional] 
**status** | **String** | The current status of this Service.  | [optional] [readonly] 
**timeout** | **Number** | How long to wait, in seconds, for a response before considering the Service to be down.  | [optional] 
**updated** | **Date** | When this Managed Service was last updated. | [optional] [readonly] 



## Enum: ServiceTypeEnum


* `url` (value: `"url"`)

* `tcp` (value: `"tcp"`)





## Enum: StatusEnum


* `disabled` (value: `"disabled"`)

* `pending` (value: `"pending"`)

* `ok` (value: `"ok"`)

* `problem` (value: `"problem"`)




