

# DeployParameters

DeployParameters contains deploy parameters information.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**matchTargetLabels** | **Map&lt;String, String&gt;** | Optional. Deploy parameters are applied to targets with match labels. If unspecified, deploy parameters are applied to all targets (including child targets of a multi-target). |  [optional] |
|**values** | **Map&lt;String, String&gt;** | Required. Values are deploy parameters in key-value pairs. |  [optional] |



