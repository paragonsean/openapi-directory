# BreadcrumbsOne.BreadcrumbsAPIModelsPathfinderPathfinderRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chain** | **String** | Blockchain eg: ETH, BTC, SOL | [default to &#39;ETH&#39;]
**destinationAddresses** | **[String]** | Required if search_type is either Shortest/Multiple Path.  If you know where did the money went or come from. | [optional] 
**directionType** | **String** | Direction type is what direction it should go. Accepts: 0 &#x3D; Incoming and 1 &#x3D; Outgoing only | [default to &#39;Incoming&#39;]
**entityTags** | **[String]** | Required if search_type is Closest Entity.  Available values are: Exchange, DEX, Mining, ICO, Mixer | [optional] 
**searchType** | **String** | Search type values: 1 &#x3D; Shortest Path, 2 &#x3D; Multiple Path, 3 &#x3D; Closest Entity and 4 &#x3D; Closest Illicit | [default to &#39;ShortestPath&#39;]
**sourceAddress** | **String** | Source address is where you want to start your search | 



## Enum: ChainEnum


* `ETH` (value: `"ETH"`)

* `BTC` (value: `"BTC"`)

* `SOL` (value: `"SOL"`)





## Enum: DirectionTypeEnum


* `Incoming` (value: `"Incoming"`)

* `Outgoing` (value: `"Outgoing"`)





## Enum: [EntityTagsEnum]


* `Exchange` (value: `"Exchange"`)

* `DEX` (value: `"DEX"`)

* `Mining` (value: `"Mining"`)

* `ICO` (value: `"ICO"`)

* `Mixer` (value: `"Mixer"`)





## Enum: SearchTypeEnum


* `ShortestPath` (value: `"ShortestPath"`)

* `MultiplePath` (value: `"MultiplePath"`)

* `ClosestEntity` (value: `"ClosestEntity"`)

* `ClosestIllicit` (value: `"ClosestIllicit"`)




