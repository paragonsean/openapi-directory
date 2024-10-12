

# CreateExperimentTemplateTargetInput

<p>Specifies a target for an experiment. You must specify at least one Amazon Resource Name (ARN) or at least one resource tag. You cannot specify both ARNs and tags.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/fis/latest/userguide/targets.html\">Targets</a> in the <i>Fault Injection Simulator User Guide</i>.</p>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**resourceType** | [**String**](String.md) |  |  |
|**resourceArns** | [**List**](List.md) |  |  [optional] |
|**resourceTags** | [**Map**](Map.md) |  |  [optional] |
|**filters** | [**List**](List.md) |  |  [optional] |
|**selectionMode** | [**String**](String.md) |  |  |
|**parameters** | [**Map**](Map.md) |  |  [optional] |



