# NetBoxApi.WritablePowerPortTemplate

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allocatedDraw** | **Number** | Allocated power draw (watts) | [optional] 
**created** | **Date** |  | [optional] [readonly] 
**description** | **String** |  | [optional] 
**deviceType** | **Number** |  | [optional] 
**display** | **String** |  | [optional] [readonly] 
**id** | **Number** |  | [optional] [readonly] 
**label** | **String** | Physical label | [optional] 
**lastUpdated** | **Date** |  | [optional] [readonly] 
**maximumDraw** | **Number** | Maximum power draw (watts) | [optional] 
**moduleType** | **Number** |  | [optional] 
**name** | **String** |  {module} is accepted as a substitution for the module bay position when attached to a module type.  | 
**type** | **String** |  | [optional] 
**url** | **String** |  | [optional] [readonly] 



## Enum: TypeEnum


* `iec-60320-c6` (value: `"iec-60320-c6"`)

* `iec-60320-c8` (value: `"iec-60320-c8"`)

* `iec-60320-c14` (value: `"iec-60320-c14"`)

* `iec-60320-c16` (value: `"iec-60320-c16"`)

* `iec-60320-c20` (value: `"iec-60320-c20"`)

* `iec-60320-c22` (value: `"iec-60320-c22"`)

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

* `nema-1-15p` (value: `"nema-1-15p"`)

* `nema-5-15p` (value: `"nema-5-15p"`)

* `nema-5-20p` (value: `"nema-5-20p"`)

* `nema-5-30p` (value: `"nema-5-30p"`)

* `nema-5-50p` (value: `"nema-5-50p"`)

* `nema-6-15p` (value: `"nema-6-15p"`)

* `nema-6-20p` (value: `"nema-6-20p"`)

* `nema-6-30p` (value: `"nema-6-30p"`)

* `nema-6-50p` (value: `"nema-6-50p"`)

* `nema-10-30p` (value: `"nema-10-30p"`)

* `nema-10-50p` (value: `"nema-10-50p"`)

* `nema-14-20p` (value: `"nema-14-20p"`)

* `nema-14-30p` (value: `"nema-14-30p"`)

* `nema-14-50p` (value: `"nema-14-50p"`)

* `nema-14-60p` (value: `"nema-14-60p"`)

* `nema-15-15p` (value: `"nema-15-15p"`)

* `nema-15-20p` (value: `"nema-15-20p"`)

* `nema-15-30p` (value: `"nema-15-30p"`)

* `nema-15-50p` (value: `"nema-15-50p"`)

* `nema-15-60p` (value: `"nema-15-60p"`)

* `nema-l1-15p` (value: `"nema-l1-15p"`)

* `nema-l5-15p` (value: `"nema-l5-15p"`)

* `nema-l5-20p` (value: `"nema-l5-20p"`)

* `nema-l5-30p` (value: `"nema-l5-30p"`)

* `nema-l5-50p` (value: `"nema-l5-50p"`)

* `nema-l6-15p` (value: `"nema-l6-15p"`)

* `nema-l6-20p` (value: `"nema-l6-20p"`)

* `nema-l6-30p` (value: `"nema-l6-30p"`)

* `nema-l6-50p` (value: `"nema-l6-50p"`)

* `nema-l10-30p` (value: `"nema-l10-30p"`)

* `nema-l14-20p` (value: `"nema-l14-20p"`)

* `nema-l14-30p` (value: `"nema-l14-30p"`)

* `nema-l14-50p` (value: `"nema-l14-50p"`)

* `nema-l14-60p` (value: `"nema-l14-60p"`)

* `nema-l15-20p` (value: `"nema-l15-20p"`)

* `nema-l15-30p` (value: `"nema-l15-30p"`)

* `nema-l15-50p` (value: `"nema-l15-50p"`)

* `nema-l15-60p` (value: `"nema-l15-60p"`)

* `nema-l21-20p` (value: `"nema-l21-20p"`)

* `nema-l21-30p` (value: `"nema-l21-30p"`)

* `nema-l22-30p` (value: `"nema-l22-30p"`)

* `cs6361c` (value: `"cs6361c"`)

* `cs6365c` (value: `"cs6365c"`)

* `cs8165c` (value: `"cs8165c"`)

* `cs8265c` (value: `"cs8265c"`)

* `cs8365c` (value: `"cs8365c"`)

* `cs8465c` (value: `"cs8465c"`)

* `ita-c` (value: `"ita-c"`)

* `ita-e` (value: `"ita-e"`)

* `ita-f` (value: `"ita-f"`)

* `ita-ef` (value: `"ita-ef"`)

* `ita-g` (value: `"ita-g"`)

* `ita-h` (value: `"ita-h"`)

* `ita-i` (value: `"ita-i"`)

* `ita-j` (value: `"ita-j"`)

* `ita-k` (value: `"ita-k"`)

* `ita-l` (value: `"ita-l"`)

* `ita-m` (value: `"ita-m"`)

* `ita-n` (value: `"ita-n"`)

* `ita-o` (value: `"ita-o"`)

* `usb-a` (value: `"usb-a"`)

* `usb-b` (value: `"usb-b"`)

* `usb-c` (value: `"usb-c"`)

* `usb-mini-a` (value: `"usb-mini-a"`)

* `usb-mini-b` (value: `"usb-mini-b"`)

* `usb-micro-a` (value: `"usb-micro-a"`)

* `usb-micro-b` (value: `"usb-micro-b"`)

* `usb-micro-ab` (value: `"usb-micro-ab"`)

* `usb-3-b` (value: `"usb-3-b"`)

* `usb-3-micro-b` (value: `"usb-3-micro-b"`)

* `dc-terminal` (value: `"dc-terminal"`)

* `saf-d-grid` (value: `"saf-d-grid"`)

* `neutrik-powercon-20` (value: `"neutrik-powercon-20"`)

* `neutrik-powercon-32` (value: `"neutrik-powercon-32"`)

* `neutrik-powercon-true1` (value: `"neutrik-powercon-true1"`)

* `neutrik-powercon-true1-top` (value: `"neutrik-powercon-true1-top"`)

* `ubiquiti-smartpower` (value: `"ubiquiti-smartpower"`)

* `hardwired` (value: `"hardwired"`)

* `other` (value: `"other"`)




