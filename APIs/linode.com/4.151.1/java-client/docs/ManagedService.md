

# ManagedService

A service that Linode is monitoring as part of your Managed services. If issues are detected with this service, a ManagedIssue will be opened and, optionally, Linode special forces will attempt to resolve the Issue. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**address** | **String** | The URL at which this Service is monitored.  URL parameters such as &#x60;?no-cache&#x3D;1&#x60; are preserved.  URL fragments/anchors such as &#x60;#monitor&#x60; are **not** preserved.  |  [optional] |
|**body** | **String** | What to expect to find in the response body for the Service to be considered up.  |  [optional] |
|**consultationGroup** | **String** | The group of ManagedContacts who should be notified or consulted with when an Issue is detected.  |  [optional] |
|**created** | **OffsetDateTime** | When this Managed Service was created. |  [optional] [readonly] |
|**credentials** | **List&lt;Integer&gt;** | An array of ManagedCredential IDs that should be used when attempting to resolve issues with this Service.  |  [optional] |
|**id** | **Integer** | This Service&#39;s unique ID.  |  [optional] [readonly] |
|**label** | **String** | The label for this Service. This is for display purposes only.  |  [optional] |
|**notes** | **String** | Any information relevant to the Service that Linode special forces should know when attempting to resolve Issues.  |  [optional] |
|**region** | **String** | The Region in which this Service is located. This is required if address is a private IP, and may not be set otherwise.  |  [optional] |
|**serviceType** | [**ServiceTypeEnum**](#ServiceTypeEnum) | How this Service is monitored.  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | The current status of this Service.  |  [optional] [readonly] |
|**timeout** | **Integer** | How long to wait, in seconds, for a response before considering the Service to be down.  |  [optional] |
|**updated** | **OffsetDateTime** | When this Managed Service was last updated. |  [optional] [readonly] |



## Enum: ServiceTypeEnum

| Name | Value |
|---- | -----|
| URL | &quot;url&quot; |
| TCP | &quot;tcp&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| DISABLED | &quot;disabled&quot; |
| PENDING | &quot;pending&quot; |
| OK | &quot;ok&quot; |
| PROBLEM | &quot;problem&quot; |



