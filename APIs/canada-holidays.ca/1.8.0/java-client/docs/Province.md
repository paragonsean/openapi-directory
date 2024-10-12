

# Province

A Canadian province or territory 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | [**IdEnum**](#IdEnum) | Canadian province abbreviations |  |
|**nameEn** | **String** | English name |  |
|**nameFr** | **String** | French name |  |
|**nextHoliday** | [**Holiday**](Holiday.md) |  |  [optional] |
|**optional** | [**OptionalEnum**](#OptionalEnum) | Whether this province optionally observes a given holiday. |  [optional] |
|**provinces** | [**List&lt;Holiday&gt;**](Holiday.md) |  |  [optional] |
|**sourceEn** | **String** | Name of reference page with public holidays for this region |  |
|**sourceLink** | **URI** | URL to public holidays reference for this region |  |



## Enum: IdEnum

| Name | Value |
|---- | -----|
| AB | &quot;AB&quot; |
| BC | &quot;BC&quot; |
| MB | &quot;MB&quot; |
| NB | &quot;NB&quot; |
| NL | &quot;NL&quot; |
| NS | &quot;NS&quot; |
| NT | &quot;NT&quot; |
| NU | &quot;NU&quot; |
| TRUE | &quot;true&quot; |
| PE | &quot;PE&quot; |
| QC | &quot;QC&quot; |
| SK | &quot;SK&quot; |
| YT | &quot;YT&quot; |



## Enum: OptionalEnum

| Name | Value |
|---- | -----|
| NUMBER_1 | 1 |



