

# WritableRearPort


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**occupied** | **Boolean** |  |  [optional] [readonly] |
|**cable** | [**NestedCable**](NestedCable.md) |  |  [optional] |
|**cableEnd** | **String** |  |  [optional] [readonly] |
|**color** | **String** |  |  [optional] |
|**created** | **OffsetDateTime** |  |  [optional] [readonly] |
|**customFields** | **Object** |  |  [optional] |
|**description** | **String** |  |  [optional] |
|**device** | **Integer** |  |  |
|**display** | **String** |  |  [optional] [readonly] |
|**id** | **Integer** |  |  [optional] [readonly] |
|**label** | **String** | Physical label |  [optional] |
|**lastUpdated** | **OffsetDateTime** |  |  [optional] [readonly] |
|**linkPeers** | **List&lt;String&gt;** |  Return the appropriate serializer for the link termination model.  |  [optional] [readonly] |
|**linkPeersType** | **String** |  |  [optional] [readonly] |
|**markConnected** | **Boolean** | Treat as if a cable is connected |  [optional] |
|**module** | **Integer** |  |  [optional] |
|**name** | **String** |  |  |
|**positions** | **Integer** |  |  [optional] |
|**tags** | [**List&lt;NestedTag&gt;**](NestedTag.md) |  |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) |  |  |
|**url** | **URI** |  |  [optional] [readonly] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| _8P8C | &quot;8p8c&quot; |
| _8P6C | &quot;8p6c&quot; |
| _8P4C | &quot;8p4c&quot; |
| _8P2C | &quot;8p2c&quot; |
| _6P6C | &quot;6p6c&quot; |
| _6P4C | &quot;6p4c&quot; |
| _6P2C | &quot;6p2c&quot; |
| _4P4C | &quot;4p4c&quot; |
| _4P2C | &quot;4p2c&quot; |
| GG45 | &quot;gg45&quot; |
| TERA_4P | &quot;tera-4p&quot; |
| TERA_2P | &quot;tera-2p&quot; |
| TERA_1P | &quot;tera-1p&quot; |
| _110_PUNCH | &quot;110-punch&quot; |
| BNC | &quot;bnc&quot; |
| F | &quot;f&quot; |
| N | &quot;n&quot; |
| MRJ21 | &quot;mrj21&quot; |
| FC | &quot;fc&quot; |
| LC | &quot;lc&quot; |
| LC_PC | &quot;lc-pc&quot; |
| LC_UPC | &quot;lc-upc&quot; |
| LC_APC | &quot;lc-apc&quot; |
| LSH | &quot;lsh&quot; |
| LSH_PC | &quot;lsh-pc&quot; |
| LSH_UPC | &quot;lsh-upc&quot; |
| LSH_APC | &quot;lsh-apc&quot; |
| MPO | &quot;mpo&quot; |
| MTRJ | &quot;mtrj&quot; |
| SC | &quot;sc&quot; |
| SC_PC | &quot;sc-pc&quot; |
| SC_UPC | &quot;sc-upc&quot; |
| SC_APC | &quot;sc-apc&quot; |
| ST | &quot;st&quot; |
| CS | &quot;cs&quot; |
| SN | &quot;sn&quot; |
| SMA_905 | &quot;sma-905&quot; |
| SMA_906 | &quot;sma-906&quot; |
| URM_P2 | &quot;urm-p2&quot; |
| URM_P4 | &quot;urm-p4&quot; |
| URM_P8 | &quot;urm-p8&quot; |
| SPLICE | &quot;splice&quot; |
| OTHER | &quot;other&quot; |



