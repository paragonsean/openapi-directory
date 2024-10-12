

# LKENodePoolDisksInner

The values to assign to each partition in this Node Pool's custom disk layout. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**size** | **Integer** | The size of this custom disk partition in MB.    * The size of this disk partition must not exceed the capacity of the node&#39;s plan type.  |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | This custom disk partition&#39;s filesystem type.  |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| RAW | &quot;raw&quot; |
| EXT4 | &quot;ext4&quot; |



