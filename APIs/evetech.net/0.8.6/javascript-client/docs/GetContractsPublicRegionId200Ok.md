# EveSwaggerInterface.GetContractsPublicRegionId200Ok

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**buyout** | **Number** | Buyout price (for Auctions only) | [optional] 
**collateral** | **Number** | Collateral price (for Couriers only) | [optional] 
**contractId** | **Number** | contract_id integer | 
**dateExpired** | **Date** | Expiration date of the contract | 
**dateIssued** | **Date** | Сreation date of the contract | 
**daysToComplete** | **Number** | Number of days to perform the contract | [optional] 
**endLocationId** | **Number** | End location ID (for Couriers contract) | [optional] 
**forCorporation** | **Boolean** | true if the contract was issued on behalf of the issuer&#39;s corporation | [optional] 
**issuerCorporationId** | **Number** | Character&#39;s corporation ID for the issuer | 
**issuerId** | **Number** | Character ID for the issuer | 
**price** | **Number** | Price of contract (for ItemsExchange and Auctions) | [optional] 
**reward** | **Number** | Remuneration for contract (for Couriers only) | [optional] 
**startLocationId** | **Number** | Start location ID (for Couriers contract) | [optional] 
**title** | **String** | Title of the contract | [optional] 
**type** | **String** | Type of the contract | 
**volume** | **Number** | Volume of items in the contract | [optional] 



## Enum: TypeEnum


* `unknown` (value: `"unknown"`)

* `item_exchange` (value: `"item_exchange"`)

* `auction` (value: `"auction"`)

* `courier` (value: `"courier"`)

* `loan` (value: `"loan"`)




