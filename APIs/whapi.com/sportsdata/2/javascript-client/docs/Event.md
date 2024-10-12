# SportsDataApi.Event

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**betInRunningDelay** | **Number** | Delay in seconds between bet being sent and bet being placed | [optional] 
**bettingStatus** | **String** | Betting status of the event | [optional] 
**cashinAvailable** | **Boolean** | Whether cashin is available on this event | [optional] 
**channels** | **[String]** | A list of channels that apply to this event | [optional] 
**country** | **String** | A string indicating the country code of this event if available | [optional] 
**description** | **String** | The description of the event | [optional] 
**displayed** | **Boolean** | whether the event should be displayed or not | [optional] 
**eventSort** | **String** | What type of event is this? (e.g. MTCH, TRNMT) | [optional] 
**flags** | **[String]** | A list of flags that apply to this event | [optional] 
**hasInPlayMarkets** | **Boolean** | Whether this event has inplay markets | [optional] 
**hasLivePrices** | **Boolean** | Whether this event has Live Prices | [optional] 
**id** | **String** | The Id of the event | 
**isInPlay** | **Boolean** | Whether this event has started and therefore is inplay | [optional] 
**isPublished** | **Boolean** | Indicates if the item is published | [optional] 
**marketCountActiveInPlay** | **Number** | Count of active markets in play | [optional] 
**marketCountActivePreMatch** | **Number** | count of active market pre-match | [optional] 
**marketCountActiveTotal** | **Number** | Total market count | [optional] 
**marketCountInPlay** | **Number** | Total inplay markets | [optional] 
**marketCountPreMatch** | **Number** | Total prematch markets | [optional] 
**markets** | [**[Market]**](Market.md) | A list of markets belonging to this event | [optional] 
**name** | **String** | The name of the event | 
**order** | **Number** | Display order of the event | [optional] 
**parentIds** | **[String]** | A list of IDs of parent entities | [optional] 
**raceNum** | **String** | Race number for race events | [optional] 
**settled** | **Boolean** | Whether the event has been settled | [optional] 
**startDateTime** | **String** | The start date and time of the event | 
**status** | **String** | Status of the event (A for Active, S for Suspended) | 


