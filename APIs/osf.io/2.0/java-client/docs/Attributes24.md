

# Attributes24

The properties of the contributor entity.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bibliographic** | **Boolean** | Whether or not the contributor will be included in citations for the Preprint. The default value is true. |  [optional] |
|**index** | **Integer** | The position of this contributor in the list of Preprint&#39;s contributors and in a Preprint&#39;s citations. |  [optional] |
|**permission** | [**PermissionEnum**](#PermissionEnum) | The permission level of the contributor. The default value is &#39;write&#39;. |  [optional] |
|**unregisteredContributor** | **String** | The assigned name of the contributor if the contributor has not yet claimed their account. |  [optional] [readonly] |



## Enum: PermissionEnum

| Name | Value |
|---- | -----|
| READ | &quot;read&quot; |
| WRITE | &quot;write&quot; |
| ADMIN | &quot;admin&quot; |



