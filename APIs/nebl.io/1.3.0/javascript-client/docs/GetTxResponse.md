# NeblioRestApiSuite.GetTxResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**blockhash** | **String** | Hash of the block this transaction is in | [optional] 
**blockheight** | **Number** | Block height of this transaction | [optional] 
**blocktime** | **Number** | Block time of this transaction | [optional] 
**confirmations** | **Number** | Number of transaction confirmations | [optional] 
**fee** | **Number** | Total NEBL used as fee for this transcation in satoshis | [optional] 
**fees** | **Number** | Total NEBL used in fees for this transaction | [optional] 
**locktime** | **Number** | Transaction locktime | [optional] 
**size** | **Number** | Transcation size in bytes | [optional] 
**time** | **Number** | Transaction time | [optional] 
**totalsent** | **Number** | Total NEBL sent in this transaction in satoshis | [optional] 
**txid** | **String** | TXID of transaction | [optional] 
**valueIn** | **Number** | Total NEBL input in this transaction | [optional] 
**valueOut** | **Number** | Total NEBL output in this transaction | [optional] 
**version** | **Number** | Transaction version | [optional] 
**vin** | [**[GetTxResponseVinInner]**](GetTxResponseVinInner.md) | Array of transaction inputs | [optional] 
**vout** | [**[GetTxResponseVoutInner]**](GetTxResponseVoutInner.md) | Array of transaction outputs | [optional] 


