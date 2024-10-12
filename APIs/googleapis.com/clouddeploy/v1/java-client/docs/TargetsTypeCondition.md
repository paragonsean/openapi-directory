

# TargetsTypeCondition

TargetsTypeCondition contains information on whether the Targets defined in the Delivery Pipeline are of the same type.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**errorDetails** | **String** | Human readable error message. |  [optional] |
|**status** | **Boolean** | True if the targets are all a comparable type. For example this is true if all targets are GKE clusters. This is false if some targets are Cloud Run targets and others are GKE clusters. |  [optional] |



