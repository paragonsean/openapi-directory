

# CountrySpecification


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**country** | **Country** |  |  [optional] |
|**receiver** | [**Receiver**](Receiver.md) |  |  [optional] |
|**region** | [**RegionEnum**](#RegionEnum) | The region this country belongs to. Within this region exchanging invoices is well defined. Between regions some care needs to be taken and Storecove may help in automatically converting some items. Contact us for details of inter-regional document exchange. |  [optional] |
|**sender** | [**Sender**](Sender.md) |  |  [optional] |



## Enum: RegionEnum

| Name | Value |
|---- | -----|
| EU_EEA | &quot;eu_eea&quot; |
| SG | &quot;sg&quot; |
| AUNZ | &quot;aunz&quot; |
| IN | &quot;in&quot; |
| WORLD | &quot;world&quot; |



