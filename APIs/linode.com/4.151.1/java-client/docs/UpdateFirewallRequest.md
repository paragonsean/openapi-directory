

# UpdateFirewallRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**label** | **String** | The Firewall&#39;s label, for display purposes only.  Firewall labels have the following constraints:    * Must begin and end with an alphanumeric character.   * May only consist of alphanumeric characters, dashes (&#x60;-&#x60;), underscores (&#x60;_&#x60;) or periods (&#x60;.&#x60;).   * Cannot have two dashes (&#x60;--&#x60;), underscores (&#x60;__&#x60;) or periods (&#x60;..&#x60;) in a row.   * Must be between 3 and 32 characters.   * Must be unique.  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | The status to be applied to this Firewall.    * When a Firewall is first created its status is &#x60;enabled&#x60;.  * Use the [Delete Firewall](/docs/api/networking/#firewall-delete) endpoint to delete a Firewall.  |  [optional] |
|**tags** | **List&lt;String&gt;** | An array of tags applied to this object. Tags are for organizational purposes only.  |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ENABLED | &quot;enabled&quot; |
| DISABLED | &quot;disabled&quot; |



