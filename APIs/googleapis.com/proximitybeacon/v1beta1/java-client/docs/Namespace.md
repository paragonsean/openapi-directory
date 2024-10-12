

# Namespace

An attachment namespace defines read and write access for all the attachments created under it. Each namespace is globally unique, and owned by one project which is the only project that can create attachments under it.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**namespaceName** | **String** | Resource name of this namespace. Namespaces names have the format: namespaces/namespace. |  [optional] |
|**servingVisibility** | [**ServingVisibilityEnum**](#ServingVisibilityEnum) | Specifies what clients may receive attachments under this namespace via &#x60;beaconinfo.getforobserved&#x60;. |  [optional] |



## Enum: ServingVisibilityEnum

| Name | Value |
|---- | -----|
| VISIBILITY_UNSPECIFIED | &quot;VISIBILITY_UNSPECIFIED&quot; |
| UNLISTED | &quot;UNLISTED&quot; |
| PUBLIC | &quot;PUBLIC&quot; |



