

# AggregationAudioItemListDocument

An array of audio recommendations with additional metadata about the aggregation they are associated with

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**attributes** | [**AggregationData**](AggregationData.md) |  |  |
|**errors** | **List&lt;Object&gt;** | A list of encountered errors, ignored on POST, PUT |  |
|**href** | **String** | A URL representation of the resource; should generally be ignored by clients unless noted otherwise |  |
|**items** | [**List&lt;AudioItemDocument&gt;**](AudioItemDocument.md) | An array of Audio Items (recommendations) |  |
|**links** | [**AggregationLinks**](AggregationLinks.md) |  |  |
|**version** | **String** | The version of the Collection.Doc+JSON spec being used |  |



