

# Domain

A domain zonefile in our DNS system.  You must own the domain name and tell your registrar to use Linode's nameservers in order for a domain in our system to be treated as authoritative. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**axfrIps** | **List&lt;String&gt;** | The list of IPs that may perform a zone transfer for this Domain. The total combined length of all data within this array cannot exceed 1000 characters.  **Note**: This is potentially dangerous, and should be set to an empty list unless you intend to use it.  |  [optional] |
|**description** | **String** | A description for this Domain. This is for display purposes only.  |  [optional] |
|**domain** | **String** | The domain this Domain represents. Domain labels cannot be longer than 63 characters and must conform to [RFC1035](https://tools.ietf.org/html/rfc1035). Domains must be unique on Linode&#39;s platform, including across different Linode accounts; there cannot be two Domains representing the same domain.  |  [optional] |
|**expireSec** | **Integer** | The amount of time in seconds that may pass before this Domain is no longer authoritative.  * Valid values are 0, 300, 3600, 7200, 14400, 28800, 57600, 86400, 172800, 345600, 604800, 1209600, and 2419200.  * Any other value is rounded up to the nearest valid value.  * A value of 0 is equivalent to the default value of 1209600.  |  [optional] |
|**group** | **String** | The group this Domain belongs to.  This is for display purposes only.  |  [optional] |
|**id** | **Integer** | This Domain&#39;s unique ID |  [optional] [readonly] |
|**masterIps** | **List&lt;String&gt;** | The IP addresses representing the master DNS for this Domain. At least one value is required for &#x60;type&#x60; slave Domains. The total combined length of all data within this array cannot exceed 1000 characters.  |  [optional] |
|**refreshSec** | **Integer** | The amount of time in seconds before this Domain should be refreshed.  * Valid values are 0, 300, 3600, 7200, 14400, 28800, 57600, 86400, 172800, 345600, 604800, 1209600, and 2419200.  * Any other value is rounded up to the nearest valid value.  * A value of 0 is equivalent to the default value of 14400.  |  [optional] |
|**retrySec** | **Integer** | The interval, in seconds, at which a failed refresh should be retried.  * Valid values are 0, 300, 3600, 7200, 14400, 28800, 57600, 86400, 172800, 345600, 604800, 1209600, and 2419200.  * Any other value is rounded up to the nearest valid value.  * A value of 0 is equivalent to the default value of 14400.  |  [optional] |
|**soaEmail** | **String** | Start of Authority email address. This is required for &#x60;type&#x60; master Domains.  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | Used to control whether this Domain is currently being rendered.  |  [optional] |
|**tags** | **List&lt;String&gt;** | An array of tags applied to this object.  Tags are for organizational purposes only.  |  [optional] |
|**ttlSec** | **Integer** | \&quot;Time to Live\&quot; - the amount of time in seconds that this Domain&#39;s records may be cached by resolvers or other domain servers. * Valid values are 0, 300, 3600, 7200, 14400, 28800, 57600, 86400, 172800, 345600, 604800, 1209600, and 2419200. * Any other value is rounded up to the nearest valid value. * A value of 0 is equivalent to the default value of 86400.  |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Whether this Domain represents the authoritative source of information for the domain it describes (\&quot;master\&quot;), or whether it is a read-only copy of a master (\&quot;slave\&quot;).  |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| DISABLED | &quot;disabled&quot; |
| ACTIVE | &quot;active&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| MASTER | &quot;master&quot; |
| SLAVE | &quot;slave&quot; |



