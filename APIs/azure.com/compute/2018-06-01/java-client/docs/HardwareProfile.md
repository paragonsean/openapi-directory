

# HardwareProfile

Specifies the hardware settings for the virtual machine.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**vmSize** | [**VmSizeEnum**](#VmSizeEnum) | Specifies the size of the virtual machine. For more information about virtual machine sizes, see [Sizes for virtual machines](https://docs.microsoft.com/azure/virtual-machines/virtual-machines-windows-sizes?toc&#x3D;%2fazure%2fvirtual-machines%2fwindows%2ftoc.json). &lt;br&gt;&lt;br&gt; The available VM sizes depend on region and availability set. For a list of available sizes use these APIs:  &lt;br&gt;&lt;br&gt; [List all available virtual machine sizes in an availability set](https://docs.microsoft.com/rest/api/compute/availabilitysets/listavailablesizes) &lt;br&gt;&lt;br&gt; [List all available virtual machine sizes in a region](https://docs.microsoft.com/rest/api/compute/virtualmachinesizes/list) &lt;br&gt;&lt;br&gt; [List all available virtual machine sizes for resizing](https://docs.microsoft.com/rest/api/compute/virtualmachines/listavailablesizes) |  [optional] |



## Enum: VmSizeEnum

| Name | Value |
|---- | -----|
| BASIC_A0 | &quot;Basic_A0&quot; |
| BASIC_A1 | &quot;Basic_A1&quot; |
| BASIC_A2 | &quot;Basic_A2&quot; |
| BASIC_A3 | &quot;Basic_A3&quot; |
| BASIC_A4 | &quot;Basic_A4&quot; |
| STANDARD_A0 | &quot;Standard_A0&quot; |
| STANDARD_A1 | &quot;Standard_A1&quot; |
| STANDARD_A2 | &quot;Standard_A2&quot; |
| STANDARD_A3 | &quot;Standard_A3&quot; |
| STANDARD_A4 | &quot;Standard_A4&quot; |
| STANDARD_A5 | &quot;Standard_A5&quot; |
| STANDARD_A6 | &quot;Standard_A6&quot; |
| STANDARD_A7 | &quot;Standard_A7&quot; |
| STANDARD_A8 | &quot;Standard_A8&quot; |
| STANDARD_A9 | &quot;Standard_A9&quot; |
| STANDARD_A10 | &quot;Standard_A10&quot; |
| STANDARD_A11 | &quot;Standard_A11&quot; |
| STANDARD_A1_V2 | &quot;Standard_A1_v2&quot; |
| STANDARD_A2_V2 | &quot;Standard_A2_v2&quot; |
| STANDARD_A4_V2 | &quot;Standard_A4_v2&quot; |
| STANDARD_A8_V2 | &quot;Standard_A8_v2&quot; |
| STANDARD_A2M_V2 | &quot;Standard_A2m_v2&quot; |
| STANDARD_A4M_V2 | &quot;Standard_A4m_v2&quot; |
| STANDARD_A8M_V2 | &quot;Standard_A8m_v2&quot; |
| STANDARD_B1S | &quot;Standard_B1s&quot; |
| STANDARD_B1MS | &quot;Standard_B1ms&quot; |
| STANDARD_B2S | &quot;Standard_B2s&quot; |
| STANDARD_B2MS | &quot;Standard_B2ms&quot; |
| STANDARD_B4MS | &quot;Standard_B4ms&quot; |
| STANDARD_B8MS | &quot;Standard_B8ms&quot; |
| STANDARD_D1 | &quot;Standard_D1&quot; |
| STANDARD_D2 | &quot;Standard_D2&quot; |
| STANDARD_D3 | &quot;Standard_D3&quot; |
| STANDARD_D4 | &quot;Standard_D4&quot; |
| STANDARD_D11 | &quot;Standard_D11&quot; |
| STANDARD_D12 | &quot;Standard_D12&quot; |
| STANDARD_D13 | &quot;Standard_D13&quot; |
| STANDARD_D14 | &quot;Standard_D14&quot; |
| STANDARD_D1_V2 | &quot;Standard_D1_v2&quot; |
| STANDARD_D2_V2 | &quot;Standard_D2_v2&quot; |
| STANDARD_D3_V2 | &quot;Standard_D3_v2&quot; |
| STANDARD_D4_V2 | &quot;Standard_D4_v2&quot; |
| STANDARD_D5_V2 | &quot;Standard_D5_v2&quot; |
| STANDARD_D2_V3 | &quot;Standard_D2_v3&quot; |
| STANDARD_D4_V3 | &quot;Standard_D4_v3&quot; |
| STANDARD_D8_V3 | &quot;Standard_D8_v3&quot; |
| STANDARD_D16_V3 | &quot;Standard_D16_v3&quot; |
| STANDARD_D32_V3 | &quot;Standard_D32_v3&quot; |
| STANDARD_D64_V3 | &quot;Standard_D64_v3&quot; |
| STANDARD_D2S_V3 | &quot;Standard_D2s_v3&quot; |
| STANDARD_D4S_V3 | &quot;Standard_D4s_v3&quot; |
| STANDARD_D8S_V3 | &quot;Standard_D8s_v3&quot; |
| STANDARD_D16S_V3 | &quot;Standard_D16s_v3&quot; |
| STANDARD_D32S_V3 | &quot;Standard_D32s_v3&quot; |
| STANDARD_D64S_V3 | &quot;Standard_D64s_v3&quot; |
| STANDARD_D11_V2 | &quot;Standard_D11_v2&quot; |
| STANDARD_D12_V2 | &quot;Standard_D12_v2&quot; |
| STANDARD_D13_V2 | &quot;Standard_D13_v2&quot; |
| STANDARD_D14_V2 | &quot;Standard_D14_v2&quot; |
| STANDARD_D15_V2 | &quot;Standard_D15_v2&quot; |
| STANDARD_DS1 | &quot;Standard_DS1&quot; |
| STANDARD_DS2 | &quot;Standard_DS2&quot; |
| STANDARD_DS3 | &quot;Standard_DS3&quot; |
| STANDARD_DS4 | &quot;Standard_DS4&quot; |
| STANDARD_DS11 | &quot;Standard_DS11&quot; |
| STANDARD_DS12 | &quot;Standard_DS12&quot; |
| STANDARD_DS13 | &quot;Standard_DS13&quot; |
| STANDARD_DS14 | &quot;Standard_DS14&quot; |
| STANDARD_DS1_V2 | &quot;Standard_DS1_v2&quot; |
| STANDARD_DS2_V2 | &quot;Standard_DS2_v2&quot; |
| STANDARD_DS3_V2 | &quot;Standard_DS3_v2&quot; |
| STANDARD_DS4_V2 | &quot;Standard_DS4_v2&quot; |
| STANDARD_DS5_V2 | &quot;Standard_DS5_v2&quot; |
| STANDARD_DS11_V2 | &quot;Standard_DS11_v2&quot; |
| STANDARD_DS12_V2 | &quot;Standard_DS12_v2&quot; |
| STANDARD_DS13_V2 | &quot;Standard_DS13_v2&quot; |
| STANDARD_DS14_V2 | &quot;Standard_DS14_v2&quot; |
| STANDARD_DS15_V2 | &quot;Standard_DS15_v2&quot; |
| STANDARD_DS13_4_V2 | &quot;Standard_DS13-4_v2&quot; |
| STANDARD_DS13_2_V2 | &quot;Standard_DS13-2_v2&quot; |
| STANDARD_DS14_8_V2 | &quot;Standard_DS14-8_v2&quot; |
| STANDARD_DS14_4_V2 | &quot;Standard_DS14-4_v2&quot; |
| STANDARD_E2_V3 | &quot;Standard_E2_v3&quot; |
| STANDARD_E4_V3 | &quot;Standard_E4_v3&quot; |
| STANDARD_E8_V3 | &quot;Standard_E8_v3&quot; |
| STANDARD_E16_V3 | &quot;Standard_E16_v3&quot; |
| STANDARD_E32_V3 | &quot;Standard_E32_v3&quot; |
| STANDARD_E64_V3 | &quot;Standard_E64_v3&quot; |
| STANDARD_E2S_V3 | &quot;Standard_E2s_v3&quot; |
| STANDARD_E4S_V3 | &quot;Standard_E4s_v3&quot; |
| STANDARD_E8S_V3 | &quot;Standard_E8s_v3&quot; |
| STANDARD_E16S_V3 | &quot;Standard_E16s_v3&quot; |
| STANDARD_E32S_V3 | &quot;Standard_E32s_v3&quot; |
| STANDARD_E64S_V3 | &quot;Standard_E64s_v3&quot; |
| STANDARD_E32_16_V3 | &quot;Standard_E32-16_v3&quot; |
| STANDARD_E32_8S_V3 | &quot;Standard_E32-8s_v3&quot; |
| STANDARD_E64_32S_V3 | &quot;Standard_E64-32s_v3&quot; |
| STANDARD_E64_16S_V3 | &quot;Standard_E64-16s_v3&quot; |
| STANDARD_F1 | &quot;Standard_F1&quot; |
| STANDARD_F2 | &quot;Standard_F2&quot; |
| STANDARD_F4 | &quot;Standard_F4&quot; |
| STANDARD_F8 | &quot;Standard_F8&quot; |
| STANDARD_F16 | &quot;Standard_F16&quot; |
| STANDARD_F1S | &quot;Standard_F1s&quot; |
| STANDARD_F2S | &quot;Standard_F2s&quot; |
| STANDARD_F4S | &quot;Standard_F4s&quot; |
| STANDARD_F8S | &quot;Standard_F8s&quot; |
| STANDARD_F16S | &quot;Standard_F16s&quot; |
| STANDARD_F2S_V2 | &quot;Standard_F2s_v2&quot; |
| STANDARD_F4S_V2 | &quot;Standard_F4s_v2&quot; |
| STANDARD_F8S_V2 | &quot;Standard_F8s_v2&quot; |
| STANDARD_F16S_V2 | &quot;Standard_F16s_v2&quot; |
| STANDARD_F32S_V2 | &quot;Standard_F32s_v2&quot; |
| STANDARD_F64S_V2 | &quot;Standard_F64s_v2&quot; |
| STANDARD_F72S_V2 | &quot;Standard_F72s_v2&quot; |
| STANDARD_G1 | &quot;Standard_G1&quot; |
| STANDARD_G2 | &quot;Standard_G2&quot; |
| STANDARD_G3 | &quot;Standard_G3&quot; |
| STANDARD_G4 | &quot;Standard_G4&quot; |
| STANDARD_G5 | &quot;Standard_G5&quot; |
| STANDARD_GS1 | &quot;Standard_GS1&quot; |
| STANDARD_GS2 | &quot;Standard_GS2&quot; |
| STANDARD_GS3 | &quot;Standard_GS3&quot; |
| STANDARD_GS4 | &quot;Standard_GS4&quot; |
| STANDARD_GS5 | &quot;Standard_GS5&quot; |
| STANDARD_GS4_8 | &quot;Standard_GS4-8&quot; |
| STANDARD_GS4_4 | &quot;Standard_GS4-4&quot; |
| STANDARD_GS5_16 | &quot;Standard_GS5-16&quot; |
| STANDARD_GS5_8 | &quot;Standard_GS5-8&quot; |
| STANDARD_H8 | &quot;Standard_H8&quot; |
| STANDARD_H16 | &quot;Standard_H16&quot; |
| STANDARD_H8M | &quot;Standard_H8m&quot; |
| STANDARD_H16M | &quot;Standard_H16m&quot; |
| STANDARD_H16R | &quot;Standard_H16r&quot; |
| STANDARD_H16MR | &quot;Standard_H16mr&quot; |
| STANDARD_L4S | &quot;Standard_L4s&quot; |
| STANDARD_L8S | &quot;Standard_L8s&quot; |
| STANDARD_L16S | &quot;Standard_L16s&quot; |
| STANDARD_L32S | &quot;Standard_L32s&quot; |
| STANDARD_M64S | &quot;Standard_M64s&quot; |
| STANDARD_M64MS | &quot;Standard_M64ms&quot; |
| STANDARD_M128S | &quot;Standard_M128s&quot; |
| STANDARD_M128MS | &quot;Standard_M128ms&quot; |
| STANDARD_M64_32MS | &quot;Standard_M64-32ms&quot; |
| STANDARD_M64_16MS | &quot;Standard_M64-16ms&quot; |
| STANDARD_M128_64MS | &quot;Standard_M128-64ms&quot; |
| STANDARD_M128_32MS | &quot;Standard_M128-32ms&quot; |
| STANDARD_NC6 | &quot;Standard_NC6&quot; |
| STANDARD_NC12 | &quot;Standard_NC12&quot; |
| STANDARD_NC24 | &quot;Standard_NC24&quot; |
| STANDARD_NC24R | &quot;Standard_NC24r&quot; |
| STANDARD_NC6S_V2 | &quot;Standard_NC6s_v2&quot; |
| STANDARD_NC12S_V2 | &quot;Standard_NC12s_v2&quot; |
| STANDARD_NC24S_V2 | &quot;Standard_NC24s_v2&quot; |
| STANDARD_NC24RS_V2 | &quot;Standard_NC24rs_v2&quot; |
| STANDARD_NC6S_V3 | &quot;Standard_NC6s_v3&quot; |
| STANDARD_NC12S_V3 | &quot;Standard_NC12s_v3&quot; |
| STANDARD_NC24S_V3 | &quot;Standard_NC24s_v3&quot; |
| STANDARD_NC24RS_V3 | &quot;Standard_NC24rs_v3&quot; |
| STANDARD_ND6S | &quot;Standard_ND6s&quot; |
| STANDARD_ND12S | &quot;Standard_ND12s&quot; |
| STANDARD_ND24S | &quot;Standard_ND24s&quot; |
| STANDARD_ND24RS | &quot;Standard_ND24rs&quot; |
| STANDARD_NV6 | &quot;Standard_NV6&quot; |
| STANDARD_NV12 | &quot;Standard_NV12&quot; |
| STANDARD_NV24 | &quot;Standard_NV24&quot; |



