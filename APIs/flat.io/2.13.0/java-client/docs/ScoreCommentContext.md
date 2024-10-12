

# ScoreCommentContext

The context of the comment (for inline/contextualized comments). A context will include all the information related to the location of the comment (i.e. score parts, range of measure, time position). 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**measureUuids** | **List&lt;String&gt;** | The list of measure UUIds |  |
|**partUuid** | **String** | The unique identifier (UUID) of the score part |  |
|**staffIdx** | **BigDecimal** | (Deprecated, use &#x60;staffUuid&#x60;) The identififer of the staff |  [optional] |
|**staffUuid** | **String** | The unique identififer (UUID) of the staff |  [optional] |
|**startDpq** | **BigDecimal** |  |  |
|**startTimePos** | **BigDecimal** |  |  |
|**stopDpq** | **BigDecimal** |  |  |
|**stopTimePos** | **BigDecimal** |  |  |



