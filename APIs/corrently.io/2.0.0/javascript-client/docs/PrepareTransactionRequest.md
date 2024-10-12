# CorrentlyIo.PrepareTransactionRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account** | **String** | Stromkonto account address of sender | [optional] 
**signature** | **String** | Signature per Stromkonto setting (might be simple email confirmation link) | [optional] 
**to** | **String** | Stromkonto account address of reciever | [optional] 
**value** | **Number** | Amount to transfer (in Watthours for electricity, or pcs for trees) | [optional] 
**variation** | **String** |  | [optional] 



## Enum: VariationEnum


* `gsb` (value: `"gsb"`)

* `erzeugung` (value: `"erzeugung"`)

* `eigenstrom` (value: `"eigenstrom"`)

* `co2` (value: `"co2"`)

* `baeume` (value: `"baeume"`)




