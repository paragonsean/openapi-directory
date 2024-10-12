# CloudDeployApi.Automation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**annotations** | **{String: String}** | Optional. User annotations. These attributes can only be set and used by the user, and not by Cloud Deploy. Annotations must meet the following constraints: * Annotations are key/value pairs. * Valid annotation keys have two segments: an optional prefix and name, separated by a slash (&#x60;/&#x60;). * The name segment is required and must be 63 characters or less, beginning and ending with an alphanumeric character (&#x60;[a-z0-9A-Z]&#x60;) with dashes (&#x60;-&#x60;), underscores (&#x60;_&#x60;), dots (&#x60;.&#x60;), and alphanumerics between. * The prefix is optional. If specified, the prefix must be a DNS subdomain: a series of DNS labels separated by dots(&#x60;.&#x60;), not longer than 253 characters in total, followed by a slash (&#x60;/&#x60;). See https://kubernetes.io/docs/concepts/overview/working-with-objects/annotations/#syntax-and-character-set for more details. | [optional] 
**createTime** | **String** | Output only. Time at which the automation was created. | [optional] [readonly] 
**description** | **String** | Optional. Description of the &#x60;Automation&#x60;. Max length is 255 characters. | [optional] 
**etag** | **String** | Optional. The weak etag of the &#x60;Automation&#x60; resource. This checksum is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding. | [optional] 
**labels** | **{String: String}** | Optional. Labels are attributes that can be set and used by both the user and by Cloud Deploy. Labels must meet the following constraints: * Keys and values can contain only lowercase letters, numeric characters, underscores, and dashes. * All characters must use UTF-8 encoding, and international characters are allowed. * Keys must start with a lowercase letter or international character. * Each resource is limited to a maximum of 64 labels. Both keys and values are additionally constrained to be &lt;&#x3D; 63 characters. | [optional] 
**name** | **String** | Output only. Name of the &#x60;Automation&#x60;. Format is &#x60;projects/{project}/locations/{location}/deliveryPipelines/{delivery_pipeline}/automations/{automation}&#x60;. | [optional] [readonly] 
**rules** | [**[AutomationRule]**](AutomationRule.md) | Required. List of Automation rules associated with the Automation resource. Must have at least one rule and limited to 250 rules per Delivery Pipeline. Note: the order of the rules here is not the same as the order of execution. | [optional] 
**selector** | [**AutomationResourceSelector**](AutomationResourceSelector.md) |  | [optional] 
**serviceAccount** | **String** | Required. Email address of the user-managed IAM service account that creates Cloud Deploy release and rollout resources. | [optional] 
**suspended** | **Boolean** | Optional. When Suspended, automation is deactivated from execution. | [optional] 
**uid** | **String** | Output only. Unique identifier of the &#x60;Automation&#x60;. | [optional] [readonly] 
**updateTime** | **String** | Output only. Time at which the automation was updated. | [optional] [readonly] 


