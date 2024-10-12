

# DeviceGroup

A group of devices. A group is defined by a set of device selectors. A device belongs to the group if it matches any selector (logical OR).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**deviceSelectors** | [**List&lt;DeviceSelector&gt;**](DeviceSelector.md) | Device selectors for this group. A device matching any of the selectors is included in this group. |  [optional] |
|**name** | **String** | The name of the group. |  [optional] |



