

# EventEntity

Detailed information about the Event's entity, including ID, type, label, and URL used to access it. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **Integer** | The unique ID for an Event&#39;s entity.   Some Event entities do not have IDs associated with them, so they will not be returned when filtering by ID. These Events include:   * &#x60;account&#x60;   * &#x60;profile&#x60;  Entities for some Events are assigned the ID of the Linode they correspond to. When filtering by ID for these Events, use the corresponding Linode&#39;s ID. These Events include:   * &#x60;disks&#x60;   * &#x60;backups&#x60;   Tag Events use a tag&#39;s name for the entity ID field. When filtering by ID for tag Events, supply the name of the tag.  |  [optional] |
|**label** | **String** | The current label of this object. The label may reflect changes that occur with this Event.  |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | The type of entity that is being referenced by the Event.  |  [optional] [readonly] |
|**url** | **String** | The URL where you can access the object this Event is for. If a relative URL, it is relative to the domain you retrieved the Event from.  |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| ACCOUNT | &quot;account&quot; |
| BACKUPS | &quot;backups&quot; |
| COMMUNITY | &quot;community&quot; |
| DISKS | &quot;disks&quot; |
| DOMAIN | &quot;domain&quot; |
| ENTITY_TRANSFER | &quot;entity_transfer&quot; |
| FIREWALL | &quot;firewall&quot; |
| IMAGE | &quot;image&quot; |
| IPADDRESS | &quot;ipaddress&quot; |
| LINODE | &quot;linode&quot; |
| LONGVIEW | &quot;longview&quot; |
| MANAGED_SERVICE | &quot;managed_service&quot; |
| NODEBALANCER | &quot;nodebalancer&quot; |
| OAUTH_CLIENT | &quot;oauth_client&quot; |
| PROFILE | &quot;profile&quot; |
| STACKSCRIPT | &quot;stackscript&quot; |
| TAG | &quot;tag&quot; |
| TICKET | &quot;ticket&quot; |
| TOKEN | &quot;token&quot; |
| USER | &quot;user&quot; |
| USER_SSH_KEY | &quot;user_ssh_key&quot; |
| VOLUME | &quot;volume&quot; |



