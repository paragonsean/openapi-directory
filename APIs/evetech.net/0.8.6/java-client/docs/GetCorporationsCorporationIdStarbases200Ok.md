

# GetCorporationsCorporationIdStarbases200Ok

200 ok object

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**moonId** | **Integer** | The moon this starbase (POS) is anchored on, unanchored POSes do not have this information |  [optional] |
|**onlinedSince** | **OffsetDateTime** | When the POS onlined, for starbases (POSes) in online state |  [optional] |
|**reinforcedUntil** | **OffsetDateTime** | When the POS will be out of reinforcement, for starbases (POSes) in reinforced state |  [optional] |
|**starbaseId** | **Long** | Unique ID for this starbase (POS) |  |
|**state** | [**StateEnum**](#StateEnum) | state string |  [optional] |
|**systemId** | **Integer** | The solar system this starbase (POS) is in, unanchored POSes have this information |  |
|**typeId** | **Integer** | Starbase (POS) type |  |
|**unanchorAt** | **OffsetDateTime** | When the POS started unanchoring, for starbases (POSes) in unanchoring state |  [optional] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| OFFLINE | &quot;offline&quot; |
| ONLINE | &quot;online&quot; |
| ONLINING | &quot;onlining&quot; |
| REINFORCED | &quot;reinforced&quot; |
| UNANCHORING | &quot;unanchoring&quot; |



