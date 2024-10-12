

# ReportingReceivershipExitStrategyModel

Helper Model - Exit Strategy

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**compiled** | **OffsetDateTime** | The date Compiled |  [optional] |
|**compiledByID** | **String** | Compiled By ID (ApplicationStaff) |  [optional] |
|**displayCompiledByID** | **String** | Compiled By ID |  [optional] |
|**extraNotes** | **String** | Extra Notes |  [optional] |
|**lenderResponse** | [**LenderResponseEnum**](#LenderResponseEnum) | Lender Response |  [optional] |
|**lenderResponseDate** | **OffsetDateTime** | Lender Response Date |  [optional] |
|**lockChanged** | **OffsetDateTime** | Lock Changed |  [optional] |
|**mortgageArrears** | **Double** | Mortgage Arrears |  [optional] |
|**mortgageBalance** | **Double** | Mortgage Balance |  [optional] |
|**mortgageCMI** | **Double** | Mortgage CMI |  [optional] |
|**recommendation** | [**RecommendationEnum**](#RecommendationEnum) | Recommendation |  [optional] |
|**reviewDate** | **OffsetDateTime** | The Review Date |  [optional] |
|**sentToLender** | **OffsetDateTime** | Sent To Lender |  [optional] |



## Enum: LenderResponseEnum

| Name | Value |
|---- | -----|
| AGREE_LET | &quot;AgreeLet&quot; |
| AGREE_SELL | &quot;AgreeSell&quot; |
| AGREE_DISPOSAL_REC | &quot;AgreeDisposalRec&quot; |
| AGREE_OTHER | &quot;AgreeOther&quot; |
| DISAGREE_LET | &quot;DisagreeLet&quot; |
| DISAGREE_SELL | &quot;DisagreeSell&quot; |
| DISAGREE_DISPOSAL_REC | &quot;DisagreeDisposalRec&quot; |
| DISAGREE_OTHER | &quot;DisagreeOther&quot; |



## Enum: RecommendationEnum

| Name | Value |
|---- | -----|
| LET | &quot;Let&quot; |
| SELL | &quot;Sell&quot; |
| DISPOSAL_REC | &quot;DisposalRec&quot; |
| PENDING_EXIT | &quot;PendingExit&quot; |
| OTHER | &quot;Other&quot; |



