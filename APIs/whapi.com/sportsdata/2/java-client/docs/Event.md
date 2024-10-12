

# Event


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**betInRunningDelay** | **BigDecimal** | Delay in seconds between bet being sent and bet being placed |  [optional] |
|**bettingStatus** | **String** | Betting status of the event |  [optional] |
|**cashinAvailable** | **Boolean** | Whether cashin is available on this event |  [optional] |
|**channels** | **List&lt;String&gt;** | A list of channels that apply to this event |  [optional] |
|**country** | **String** | A string indicating the country code of this event if available |  [optional] |
|**description** | **String** | The description of the event |  [optional] |
|**displayed** | **Boolean** | whether the event should be displayed or not |  [optional] |
|**eventSort** | **String** | What type of event is this? (e.g. MTCH, TRNMT) |  [optional] |
|**flags** | **List&lt;String&gt;** | A list of flags that apply to this event |  [optional] |
|**hasInPlayMarkets** | **Boolean** | Whether this event has inplay markets |  [optional] |
|**hasLivePrices** | **Boolean** | Whether this event has Live Prices |  [optional] |
|**id** | **String** | The Id of the event |  |
|**isInPlay** | **Boolean** | Whether this event has started and therefore is inplay |  [optional] |
|**isPublished** | **Boolean** | Indicates if the item is published |  [optional] |
|**marketCountActiveInPlay** | **BigDecimal** | Count of active markets in play |  [optional] |
|**marketCountActivePreMatch** | **BigDecimal** | count of active market pre-match |  [optional] |
|**marketCountActiveTotal** | **BigDecimal** | Total market count |  [optional] |
|**marketCountInPlay** | **BigDecimal** | Total inplay markets |  [optional] |
|**marketCountPreMatch** | **BigDecimal** | Total prematch markets |  [optional] |
|**markets** | [**List&lt;Market&gt;**](Market.md) | A list of markets belonging to this event |  [optional] |
|**name** | **String** | The name of the event |  |
|**order** | **BigDecimal** | Display order of the event |  [optional] |
|**parentIds** | **List&lt;String&gt;** | A list of IDs of parent entities |  [optional] |
|**raceNum** | **String** | Race number for race events |  [optional] |
|**settled** | **Boolean** | Whether the event has been settled |  [optional] |
|**startDateTime** | **String** | The start date and time of the event |  |
|**status** | **String** | Status of the event (A for Active, S for Suspended) |  |



