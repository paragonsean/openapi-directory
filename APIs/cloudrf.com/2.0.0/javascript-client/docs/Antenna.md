# CloudRfApi.Antenna

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ant** | **Number** | Antenna pattern code. 1&#x3D;Vertical dipole (Omni-directional) | [optional] [default to 1]
**azi** | **Number** | Antenna azimuth in degrees north | [optional] [default to 0]
**hbw** | **Number** | Custom antenna horizontal beamwidth in degrees. For use only with ant&#x3D;0 | [optional] [default to 0]
**pol** | **String** | Antenna polarization as either h or v | [optional] [default to &#39;v&#39;]
**tlt** | **Number** | Antenna tilt in degrees below the horizon (inverted) | [optional] [default to 0]
**txg** | **Number** | Transmitter antenna gain in dBi | [optional] [default to 2.15]
**txl** | **Number** | Feeder loss in dB | [optional] [default to 0]
**vbw** | **Number** | Custom antenna vertical beamwidth in degrees. For use only with ant&#x3D;0 | [optional] [default to 0]



## Enum: PolEnum


* `h` (value: `"h"`)

* `v` (value: `"v"`)




