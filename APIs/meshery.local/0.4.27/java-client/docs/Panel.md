

# Panel


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**alert** | [**Alert**](Alert.md) |  |  [optional] |
|**aliasColors** | **Object** |  |  [optional] |
|**bars** | **Boolean** |  |  [optional] |
|**cards** | [**PanelCards**](PanelCards.md) |  |  [optional] |
|**collapsed** | **Boolean** |  |  [optional] |
|**color** | [**PanelColor**](PanelColor.md) |  |  [optional] |
|**colorBackground** | **Boolean** |  |  [optional] |
|**colorValue** | **Boolean** |  |  [optional] |
|**colors** | **List&lt;String&gt;** |  |  [optional] |
|**columns** | [**List&lt;Column&gt;**](Column.md) |  |  [optional] |
|**content** | **String** |  |  [optional] |
|**dashLength** | **Integer** |  |  [optional] |
|**dashboardTags** | **List&lt;String&gt;** |  |  [optional] |
|**dashes** | **Boolean** |  |  [optional] |
|**dataFormat** | **String** |  |  [optional] |
|**datasource** | **String** |  |  [optional] |
|**decimals** | **Long** |  |  [optional] |
|**description** | **String** |  |  [optional] |
|**editable** | **Boolean** |  |  [optional] |
|**error** | **Boolean** |  |  [optional] |
|**fieldConfig** | [**FieldConfig**](FieldConfig.md) |  |  [optional] |
|**fill** | **Long** |  |  [optional] |
|**folderId** | **Long** |  |  [optional] |
|**format** | **String** |  |  [optional] |
|**gauge** | [**Gauge**](Gauge.md) |  |  [optional] |
|**gridPos** | [**PanelGridPos**](PanelGridPos.md) |  |  [optional] |
|**headings** | **Boolean** |  |  [optional] |
|**height** | **Object** |  |  [optional] |
|**hideTimeOverride** | **Boolean** |  |  [optional] |
|**hideZeroBuckets** | **Boolean** |  |  [optional] |
|**highlightCards** | **Boolean** |  |  [optional] |
|**id** | **Integer** |  |  [optional] |
|**isNew** | **Boolean** |  |  [optional] |
|**leftYAxisLabel** | **String** |  |  [optional] |
|**legend** | [**Legend**](Legend.md) |  |  [optional] |
|**limit** | **Long** |  |  [optional] |
|**lines** | **Boolean** |  |  [optional] |
|**linewidth** | **Integer** |  |  [optional] |
|**links** | [**List&lt;Link&gt;**](Link.md) |  |  [optional] |
|**mappingType** | **Integer** |  |  [optional] |
|**mappingTypes** | [**List&lt;MapType&gt;**](MapType.md) |  |  [optional] |
|**maxDataPoints** | [**IntString**](IntString.md) |  |  [optional] |
|**minSpan** | **Float** |  |  [optional] |
|**mode** | **String** |  |  [optional] |
|**nameFilter** | **String** |  |  [optional] |
|**nullPointMode** | **String** |  |  [optional] |
|**onlyAlertsOnDashboard** | **Boolean** |  |  [optional] |
|**options** | [**Options**](Options.md) |  |  [optional] |
|**pageSize** | **Integer** |  |  [optional] |
|**panels** | [**List&lt;Panel&gt;**](Panel.md) |  |  [optional] |
|**percentage** | **Boolean** |  |  [optional] |
|**pointradius** | **Float** |  |  [optional] |
|**points** | **Boolean** |  |  [optional] |
|**postfix** | **String** |  |  [optional] |
|**postfixFontSize** | **String** |  |  [optional] |
|**prefix** | **String** |  |  [optional] |
|**prefixFontSize** | **String** |  |  [optional] |
|**query** | **String** |  |  [optional] |
|**rangeMaps** | [**List&lt;RangeMap&gt;**](RangeMap.md) |  |  [optional] |
|**recent** | **Boolean** |  |  [optional] |
|**renderer** | **String** |  |  [optional] |
|**repeat** | **String** |  |  [optional] |
|**repeatPanelId** | **Integer** | RepeatIteration *int64   &#x60;json:\&quot;repeatIteration,omitempty\&quot;&#x60; |  [optional] |
|**reverseYBuckets** | **Boolean** |  |  [optional] |
|**rightYAxisLabel** | **String** |  |  [optional] |
|**scopedVars** | [**Map&lt;String, PanelScopedVarsValue&gt;**](PanelScopedVarsValue.md) |  |  [optional] |
|**scroll** | **Boolean** |  |  [optional] |
|**search** | **Boolean** |  |  [optional] |
|**seriesOverrides** | [**List&lt;SeriesOverride&gt;**](SeriesOverride.md) |  |  [optional] |
|**show** | **String** |  |  [optional] |
|**showHeader** | **Boolean** |  |  [optional] |
|**sort** | [**Sort**](Sort.md) |  |  [optional] |
|**sortOrder** | **Long** |  |  [optional] |
|**spaceLength** | **Integer** |  |  [optional] |
|**span** | **Float** |  |  [optional] |
|**sparkline** | [**SparkLine**](SparkLine.md) |  |  [optional] |
|**stack** | **Boolean** |  |  [optional] |
|**starred** | **Boolean** |  |  [optional] |
|**stateFilter** | **List&lt;String&gt;** |  |  [optional] |
|**steppedLine** | **Boolean** |  |  [optional] |
|**styles** | [**List&lt;ColumnStyle&gt;**](ColumnStyle.md) |  |  [optional] |
|**tags** | **List&lt;String&gt;** |  |  [optional] |
|**targets** | [**List&lt;Target&gt;**](Target.md) |  |  [optional] |
|**thresholds** | [**List&lt;Threshold&gt;**](Threshold.md) |  |  [optional] |
|**timeFrom** | **String** |  |  [optional] |
|**timeShift** | **String** |  |  [optional] |
|**title** | **String** |  |  [optional] |
|**tooltip** | [**Tooltip**](Tooltip.md) |  |  [optional] |
|**tooltipDecimals** | **Long** |  |  [optional] |
|**transform** | **String** |  |  [optional] |
|**transparent** | **Boolean** |  |  [optional] |
|**type** | **String** |  |  [optional] |
|**valueFontSize** | **String** |  |  [optional] |
|**valueMaps** | [**List&lt;ValueMap&gt;**](ValueMap.md) |  |  [optional] |
|**valueName** | **String** |  |  [optional] |
|**xAxis** | **Boolean** |  |  [optional] |
|**xAxis** | [**PanelXAxis**](PanelXAxis.md) |  |  [optional] |
|**xBucketNumber** | **Double** |  |  [optional] |
|**xBucketSize** | **String** |  |  [optional] |
|**xaxis** | [**Axis**](Axis.md) |  |  [optional] |
|**yAxis** | **Boolean** |  |  [optional] |
|**yAxis** | [**PanelYAxis**](PanelYAxis.md) |  |  [optional] |
|**yBucketBound** | **String** |  |  [optional] |
|**yBucketNumber** | **Double** |  |  [optional] |
|**yBucketSize** | **Double** |  |  [optional] |
|**yFormats** | **List&lt;String&gt;** |  |  [optional] |
|**yaxes** | [**List&lt;Axis&gt;**](Axis.md) |  |  [optional] |



