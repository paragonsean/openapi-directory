# NeblioRestApiSuite.GetTransactionInfoResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**blockhash** | **String** | Hash of the block this transaction is in | [optional] 
**blockheight** | **Number** | Block height of this transaction | [optional] 
**blocktime** | **Number** | Block time of this transaction | [optional] 
**confirmations** | **Number** | Number of transaction confirmations | [optional] 
**fee** | **Number** | Total NEBL used as fee for this transcation in satoshis | [optional] 
**hex** | **String** | Transaction in raw hex | [optional] 
**locktime** | **Number** | Transaction locktime | [optional] 
**time** | **Number** | Transaction time | [optional] 
**totalsent** | **Number** | Total NEBL sent in this transaction in satoshis | [optional] 
**txid** | **String** | TXID of transaction | [optional] 
**version** | **Number** | Transaction version | [optional] 
**vin** | [**[GetTransactionInfoResponseVinInner]**](GetTransactionInfoResponseVinInner.md) | Array of transaction inputs | [optional] 
**vout** | [**[GetTransactionInfoResponseVoutInner]**](GetTransactionInfoResponseVoutInner.md) | Array of transaction outputs | [optional] 


