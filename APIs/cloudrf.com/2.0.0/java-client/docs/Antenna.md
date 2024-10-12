

# Antenna


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**ant** | **Integer** | Antenna pattern code. 1&#x3D;Vertical dipole (Omni-directional) |  [optional] |
|**azi** | **Integer** | Antenna azimuth in degrees north |  [optional] |
|**hbw** | **Integer** | Custom antenna horizontal beamwidth in degrees. For use only with ant&#x3D;0 |  [optional] |
|**pol** | [**PolEnum**](#PolEnum) | Antenna polarization as either h or v |  [optional] |
|**tlt** | **Float** | Antenna tilt in degrees below the horizon (inverted) |  [optional] |
|**txg** | **Float** | Transmitter antenna gain in dBi |  [optional] |
|**txl** | **Float** | Feeder loss in dB |  [optional] |
|**vbw** | **Integer** | Custom antenna vertical beamwidth in degrees. For use only with ant&#x3D;0 |  [optional] |



## Enum: PolEnum

| Name | Value |
|---- | -----|
| H | &quot;h&quot; |
| V | &quot;v&quot; |



