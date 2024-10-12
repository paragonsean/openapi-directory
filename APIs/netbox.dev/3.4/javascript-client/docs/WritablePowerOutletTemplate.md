# NetBoxApi.WritablePowerOutletTemplate

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **Date** |  | [optional] [readonly] 
**description** | **String** |  | [optional] 
**deviceType** | **Number** |  | [optional] 
**display** | **String** |  | [optional] [readonly] 
**feedLeg** | **String** | Phase (for three-phase feeds) | [optional] 
**id** | **Number** |  | [optional] [readonly] 
**label** | **String** | Physical label | [optional] 
**lastUpdated** | **Date** |  | [optional] [readonly] 
**moduleType** | **Number** |  | [optional] 
**name** | **String** |  {module} is accepted as a substitution for the module bay position when attached to a module type.  | 
**powerPort** | **Number** |  | [optional] 
**type** | **String** |  | [optional] 
**url** | **String** |  | [optional] [readonly] 



## Enum: FeedLegEnum


* `A` (value: `"A"`)

* `B` (value: `"B"`)

* `C` (value: `"C"`)





## Enum: TypeEnum


* `iec-60320-c5` (value: `"iec-60320-c5"`)

* `iec-60320-c7` (value: `"iec-60320-c7"`)

* `iec-60320-c13` (value: `"iec-60320-c13"`)

* `iec-60320-c15` (value: `"iec-60320-c15"`)

* `iec-60320-c19` (value: `"iec-60320-c19"`)

* `iec-60320-c21` (value: `"iec-60320-c21"`)

* `iec-60309-p-n-e-4h` (value: `"iec-60309-p-n-e-4h"`)

* `iec-60309-p-n-e-6h` (value: `"iec-60309-p-n-e-6h"`)

* `iec-60309-p-n-e-9h` (value: `"iec-60309-p-n-e-9h"`)

* `iec-60309-2p-e-4h` (value: `"iec-60309-2p-e-4h"`)

* `iec-60309-2p-e-6h` (value: `"iec-60309-2p-e-6h"`)

* `iec-60309-2p-e-9h` (value: `"iec-60309-2p-e-9h"`)

* `iec-60309-3p-e-4h` (value: `"iec-60309-3p-e-4h"`)

* `iec-60309-3p-e-6h` (value: `"iec-60309-3p-e-6h"`)

* `iec-60309-3p-e-9h` (value: `"iec-60309-3p-e-9h"`)

* `iec-60309-3p-n-e-4h` (value: `"iec-60309-3p-n-e-4h"`)

* `iec-60309-3p-n-e-6h` (value: `"iec-60309-3p-n-e-6h"`)

* `iec-60309-3p-n-e-9h` (value: `"iec-60309-3p-n-e-9h"`)

* `nema-1-15r` (value: `"nema-1-15r"`)

* `nema-5-15r` (value: `"nema-5-15r"`)

* `nema-5-20r` (value: `"nema-5-20r"`)

* `nema-5-30r` (value: `"nema-5-30r"`)

* `nema-5-50r` (value: `"nema-5-50r"`)

* `nema-6-15r` (value: `"nema-6-15r"`)

* `nema-6-20r` (value: `"nema-6-20r"`)

* `nema-6-30r` (value: `"nema-6-30r"`)

* `nema-6-50r` (value: `"nema-6-50r"`)

* `nema-10-30r` (value: `"nema-10-30r"`)

* `nema-10-50r` (value: `"nema-10-50r"`)

* `nema-14-20r` (value: `"nema-14-20r"`)

* `nema-14-30r` (value: `"nema-14-30r"`)

* `nema-14-50r` (value: `"nema-14-50r"`)

* `nema-14-60r` (value: `"nema-14-60r"`)

* `nema-15-15r` (value: `"nema-15-15r"`)

* `nema-15-20r` (value: `"nema-15-20r"`)

* `nema-15-30r` (value: `"nema-15-30r"`)

* `nema-15-50r` (value: `"nema-15-50r"`)

* `nema-15-60r` (value: `"nema-15-60r"`)

* `nema-l1-15r` (value: `"nema-l1-15r"`)

* `nema-l5-15r` (value: `"nema-l5-15r"`)

* `nema-l5-20r` (value: `"nema-l5-20r"`)

* `nema-l5-30r` (value: `"nema-l5-30r"`)

* `nema-l5-50r` (value: `"nema-l5-50r"`)

* `nema-l6-15r` (value: `"nema-l6-15r"`)

* `nema-l6-20r` (value: `"nema-l6-20r"`)

* `nema-l6-30r` (value: `"nema-l6-30r"`)

* `nema-l6-50r` (value: `"nema-l6-50r"`)

* `nema-l10-30r` (value: `"nema-l10-30r"`)

* `nema-l14-20r` (value: `"nema-l14-20r"`)

* `nema-l14-30r` (value: `"nema-l14-30r"`)

* `nema-l14-50r` (value: `"nema-l14-50r"`)

* `nema-l14-60r` (value: `"nema-l14-60r"`)

* `nema-l15-20r` (value: `"nema-l15-20r"`)

* `nema-l15-30r` (value: `"nema-l15-30r"`)

* `nema-l15-50r` (value: `"nema-l15-50r"`)

* `nema-l15-60r` (value: `"nema-l15-60r"`)

* `nema-l21-20r` (value: `"nema-l21-20r"`)

* `nema-l21-30r` (value: `"nema-l21-30r"`)

* `nema-l22-30r` (value: `"nema-l22-30r"`)

* `CS6360C` (value: `"CS6360C"`)

* `CS6364C` (value: `"CS6364C"`)

* `CS8164C` (value: `"CS8164C"`)

* `CS8264C` (value: `"CS8264C"`)

* `CS8364C` (value: `"CS8364C"`)

* `CS8464C` (value: `"CS8464C"`)

* `ita-e` (value: `"ita-e"`)

* `ita-f` (value: `"ita-f"`)

* `ita-g` (value: `"ita-g"`)

* `ita-h` (value: `"ita-h"`)

* `ita-i` (value: `"ita-i"`)

* `ita-j` (value: `"ita-j"`)

* `ita-k` (value: `"ita-k"`)

* `ita-l` (value: `"ita-l"`)

* `ita-m` (value: `"ita-m"`)

* `ita-n` (value: `"ita-n"`)

* `ita-o` (value: `"ita-o"`)

* `ita-multistandard` (value: `"ita-multistandard"`)

* `usb-a` (value: `"usb-a"`)

* `usb-micro-b` (value: `"usb-micro-b"`)

* `usb-c` (value: `"usb-c"`)

* `dc-terminal` (value: `"dc-terminal"`)

* `hdot-cx` (value: `"hdot-cx"`)

* `saf-d-grid` (value: `"saf-d-grid"`)

* `neutrik-powercon-20a` (value: `"neutrik-powercon-20a"`)

* `neutrik-powercon-32a` (value: `"neutrik-powercon-32a"`)

* `neutrik-powercon-true1` (value: `"neutrik-powercon-true1"`)

* `neutrik-powercon-true1-top` (value: `"neutrik-powercon-true1-top"`)

* `ubiquiti-smartpower` (value: `"ubiquiti-smartpower"`)

* `hardwired` (value: `"hardwired"`)

* `other` (value: `"other"`)




