

# EditAtom

Edit atom.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**endTimeOffset** | **String** | End time in seconds for the atom, relative to the input file timeline. When &#x60;end_time_offset&#x60; is not specified, the &#x60;inputs&#x60; are used until the end of the atom. |  [optional] |
|**inputs** | **List&lt;String&gt;** | List of &#x60;Input.key&#x60;s identifying files that should be used in this atom. The listed &#x60;inputs&#x60; must have the same timeline. |  [optional] |
|**key** | **String** | A unique key for this atom. Must be specified when using advanced mapping. |  [optional] |
|**startTimeOffset** | **String** | Start time in seconds for the atom, relative to the input file timeline. The default is &#x60;0s&#x60;. |  [optional] |



