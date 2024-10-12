# SportsDataApi.Market

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**antepostMarket** | **Boolean** | Antepost Market | [optional] 
**bestOddsGuaranteed** | **Boolean** | BOG Available | [optional] 
**betInRunningDelay** | **Number** |  | [optional] 
**channels** | **String** | A channel indicates where an entry can be accessed. Its made up of a string containing a number of characters | [optional] 
**description** | **String** | Additional market information | [optional] 
**displayed** | **Boolean** | Indicates if the item should be displayed | [optional] 
**eachWay** | **Boolean** | Indicates if each way betting is available | [optional] 
**eachWayFactorDen** | **Number** | Where each way terms are stored with the bet, this holds the denominator for the each way factor. For example, if the each way terms are: 5 places pay ¼, this value will be 4 | [optional] 
**eachWayFactorNum** | **Number** | Where each way terms are stored with the bet, this holds the numerator for the each way factor. For example, if the each way terms are: 5 places pay ¼, this value will be 1 | [optional] 
**eachWayPlaces** | **Number** | Where each way terms are stored with the bet, this holds the number of places paid. For example, if the each way terms are: 5 places pay ¼, this value will be 5 | [optional] 
**earlyPriceAvailable** | **Boolean** | Early Pricing Active | [optional] 
**fcAvailable** | **Boolean** | Is tricast betting available | [optional] 
**firstFourAvailable** | **Boolean** | Is firstFour betting available | [optional] 
**firstPriceAvailable** | **Boolean** | Is firstPrice betting available | [optional] 
**flags** | **String** | Flags for the market | [optional] 
**hcapMakeup** | **Number** | Handicap score | [optional] 
**hcapValue** | **Number** | This value indicates the current handicap set on the Event Market, assuming it has a handicap type. | [optional] 
**id** | **String** | ID (e.g. OB_MA{id} (e.g. OB_MA1), OB_SP (Sport), OB_CL (Class), OB_TY (Competition / type), OB_EV (event) OB_MA (Market), OB_OU (Selection / outcome) | 
**isInPlayMarket** | **Boolean** | Is this an in-play market | [optional] 
**isPublished** | **Boolean** | Indicates if the item is published | [optional] 
**livePriceAvailable** | **Boolean** | Live Price | [optional] 
**marketGroupCollectionId** | **String** | The collectionId of the Market Group inherited from | [optional] 
**marketGroupId** | **String** | The group id the market was inherited from | [optional] 
**marketGroupName** | **String** | The group name the market was inherited from | [optional] 
**marketSort** | **String** | The sort defines the market template | [optional] 
**name** | **String** | Human-friendly name of the market | 
**order** | **Number** | Display order of the items (Ascending) | [optional] 
**parentIds** | **[String]** | A list of IDs of parent entities | [optional] 
**quinellaAvailable** | **Boolean** | Is firstFour betting available | [optional] 
**selections** | [**[Selection]**](Selection.md) | A list of selections belonging to the market | [optional] 
**settled** | **Boolean** | Whether the market is settled or not | [optional] 
**startingPriceAvailable** | **Boolean** | Starting Price Available | [optional] 
**status** | **String** | Indicates the status of the Market (A &#x3D; Active/S &#x3D; Suspended) | 
**tcAvailable** | **Boolean** | Is forecast betting available | [optional] 


