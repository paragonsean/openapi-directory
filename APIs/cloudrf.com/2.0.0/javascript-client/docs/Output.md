# CloudRfApi.Output

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ber** | **Number** | Bit error rate. 1&#x3D;0.1, 2&#x3D;0.01, 3&#x3D;0.001, 4&#x3D;0.0001,5&#x3D;0.00001,6&#x3D;0.000001. &gt;6&#x3D;Lora: 7&#x3D;SF7,8&#x3D;SF8,9&#x3D;SF9,10&#x3D;SF10,11&#x3D;SF11,12&#x3D;SF12 | [optional] [default to 0]
**col** | **String** | Colour schema code OR filename. 1 &#x3D; Cellular (5), 2&#x3D;Red, 3&#x3D;Green, 4&#x3D;Blue, 5&#x3D;Microwave(7), 7&#x3D;Custom RGB, 8&#x3D;Automatic by frequency, 9&#x3D;Greyscale / GIS, 10&#x3D;Rainbow(24), 11&#x3D;Green/Blue/Red, 13&#x3D;Sub noise floor (10), 14&#x3D;TV broadcasting (4), 15&#x3D;Red threshold, 16&#x3D;Green threshold, 17&#x3D;Blue threshold. RAINBOW.dBm, CUSTOMSCHEMA.dBm.. | [optional] [default to &#39;RAINBOW.dBm&#39;]
**mod** | **Number** | Modulation. 1&#x3D;4QAM,2&#x3D;16QAM,3&#x3D;64QAM,4&#x3D;256QAM,5&#x3D;1024QAM,6&#x3D;BPSK,7&#x3D;QPSK,8&#x3D;8PSK,9&#x3D;16PSK,10&#x3D;32PSK,11&#x3D;LoRa | [optional] [default to 0]
**nf** | **Number** | Noise floor in dBm for use with out&#x3D;4 / SNR | [optional] [default to -114]
**out** | **Number** | Measured units. 1&#x3D;dB,2&#x3D;dBm,3&#x3D;dBuV,4&#x3D;SNR | [optional] [default to 2]
**rad** | **Number** | Radius in kilometres for output | [optional] [default to 5]
**res** | **Number** | Resolution in metres for output | [optional] [default to 10]
**units** | **String** | Distance units in either metres/kilometres (metric) or feet/miles (imperial) | [optional] [default to &#39;metric&#39;]



## Enum: UnitsEnum


* `metric` (value: `"metric"`)

* `imperial` (value: `"imperial"`)




