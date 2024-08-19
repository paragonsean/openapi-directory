

# BreadcrumbsAPIModelsPathfinderPathfinderRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**chain** | [**ChainEnum**](#ChainEnum) | Blockchain eg: ETH, BTC, SOL |  |
|**destinationAddresses** | **List&lt;String&gt;** | Required if search_type is either Shortest/Multiple Path.  If you know where did the money went or come from. |  [optional] |
|**directionType** | [**DirectionTypeEnum**](#DirectionTypeEnum) | Direction type is what direction it should go. Accepts: 0 &#x3D; Incoming and 1 &#x3D; Outgoing only |  |
|**entityTags** | [**List&lt;EntityTagsEnum&gt;**](#List&lt;EntityTagsEnum&gt;) | Required if search_type is Closest Entity.  Available values are: Exchange, DEX, Mining, ICO, Mixer |  [optional] |
|**searchType** | [**SearchTypeEnum**](#SearchTypeEnum) | Search type values: 1 &#x3D; Shortest Path, 2 &#x3D; Multiple Path, 3 &#x3D; Closest Entity and 4 &#x3D; Closest Illicit |  |
|**sourceAddress** | **String** | Source address is where you want to start your search |  |



## Enum: ChainEnum

| Name | Value |
|---- | -----|
| ETH | &quot;ETH&quot; |
| BTC | &quot;BTC&quot; |
| SOL | &quot;SOL&quot; |



## Enum: DirectionTypeEnum

| Name | Value |
|---- | -----|
| INCOMING | &quot;Incoming&quot; |
| OUTGOING | &quot;Outgoing&quot; |



## Enum: List&lt;EntityTagsEnum&gt;

| Name | Value |
|---- | -----|
| EXCHANGE | &quot;Exchange&quot; |
| DEX | &quot;DEX&quot; |
| MINING | &quot;Mining&quot; |
| ICO | &quot;ICO&quot; |
| MIXER | &quot;Mixer&quot; |



## Enum: SearchTypeEnum

| Name | Value |
|---- | -----|
| SHORTEST_PATH | &quot;ShortestPath&quot; |
| MULTIPLE_PATH | &quot;MultiplePath&quot; |
| CLOSEST_ENTITY | &quot;ClosestEntity&quot; |
| CLOSEST_ILLICIT | &quot;ClosestIllicit&quot; |



