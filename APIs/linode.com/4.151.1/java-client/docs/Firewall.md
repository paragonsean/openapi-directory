

# Firewall

A resource that controls incoming and outgoing network traffic to a Linode service. Only one Firewall can be attached to a Linode at any given time. [Create a Firewall Device](/docs/api/networking/#firewall-create) to assign a Firewall to a Linode service. Currently, Firewalls can only be assigned to Linode instances. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**created** | **OffsetDateTime** | When this Firewall was created.  |  [optional] [readonly] |
|**id** | **Integer** | The Firewall&#39;s unique ID.  |  [optional] [readonly] |
|**label** | **String** | The Firewall&#39;s label, for display purposes only.  Firewall labels have the following constraints:    * Must begin and end with an alphanumeric character.   * May only consist of alphanumeric characters, dashes (&#x60;-&#x60;), underscores (&#x60;_&#x60;) or periods (&#x60;.&#x60;).   * Cannot have two dashes (&#x60;--&#x60;), underscores (&#x60;__&#x60;) or periods (&#x60;..&#x60;) in a row.   * Must be between 3 and 32 characters.   * Must be unique.  |  [optional] |
|**rules** | [**FirewallRules**](FirewallRules.md) |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | The status of this Firewall.    * When a Firewall is first created its status is &#x60;enabled&#x60;.   * Use the [Update Firewall](/docs/api/networking/#firewall-update) endpoint to set a Firewall&#39;s status to &#x60;enabled&#x60; or &#x60;disabled&#x60;.   * Use the [Delete Firewall](/docs/api/networking/#firewall-delete) endpoint to delete a Firewall.  |  [optional] [readonly] |
|**tags** | **List&lt;String&gt;** | An array of tags applied to this object. Tags are for organizational purposes only.  |  [optional] |
|**updated** | **OffsetDateTime** | When this Firewall was last updated.  |  [optional] [readonly] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ENABLED | &quot;enabled&quot; |
| DISABLED | &quot;disabled&quot; |
| DELETED | &quot;deleted&quot; |



