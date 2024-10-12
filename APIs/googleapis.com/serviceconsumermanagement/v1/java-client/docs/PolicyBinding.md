

# PolicyBinding

Translates to IAM Policy bindings (without auditing at this level)

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**members** | **List&lt;String&gt;** | Uses the same format as in IAM policy. &#x60;member&#x60; must include both a prefix and ID. For example, &#x60;user:{emailId}&#x60;, &#x60;serviceAccount:{emailId}&#x60;, &#x60;group:{emailId}&#x60;. |  [optional] |
|**role** | **String** | Role. (https://cloud.google.com/iam/docs/understanding-roles) For example, &#x60;roles/viewer&#x60;, &#x60;roles/editor&#x60;, or &#x60;roles/owner&#x60;. |  [optional] |



