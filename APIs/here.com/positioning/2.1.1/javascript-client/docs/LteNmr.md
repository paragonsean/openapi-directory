# HereNetworkPositioningApiV2.LteNmr

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cid** | **Number** | E-UTRA Cell Identifier (UC-Id), 28 bits (20 bits eNodeB and 8 bits Cell ID). MCC + MNC + CID uniquely identifies the LTE cell, TAC is optional.  | [optional] 
**earfcn** | **Number** | Evolved Absolute Radio Frequency Channel (E-ARFCN) | 
**pci** | **Number** | Physical Cell Identity (PCI) | 
**rsrp** | **Number** | Reference Signal Received Power (RSRP) in dBm. Power less than -140dBm should be mapped to -140. Power greater than -44dBm should be mapped to -44.  | [optional] 
**rsrq** | **Number** | Reference Signal Received Quality (RSRQ) in dBm. Values less than -19.5dB should be mapped to -19.5, and values greater than -3dB should be mapped to -3dB.  | [optional] 


