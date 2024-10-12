

# UpdateNetworkDeviceRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**address** | **String** | The address of a device |  [optional] |
|**floorPlanId** | **String** | The floor plan to associate to this device. null disassociates the device from the floorplan. |  [optional] |
|**lat** | **Float** | The latitude of a device |  [optional] |
|**lng** | **Float** | The longitude of a device |  [optional] |
|**moveMapMarker** | **Boolean** | Whether or not to set the latitude and longitude of a device based on the new address. Only applies when lat and lng are not specified. |  [optional] |
|**name** | **String** | The name of a device |  [optional] |
|**notes** | **String** | The notes for the device. String. Limited to 255 characters. |  [optional] |
|**switchProfileId** | **String** | The ID of a switch profile to bind to the device (for available switch profiles, see the &#39;Switch Profiles&#39; endpoint). Use null to unbind the switch device from the current profile. For a device to be bindable to a switch profile, it must (1) be a switch, and (2) belong to a network that is bound to a configuration template. |  [optional] |
|**tags** | **String** | The tags of a device |  [optional] |



