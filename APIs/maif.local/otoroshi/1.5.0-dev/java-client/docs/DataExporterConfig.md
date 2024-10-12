

# DataExporterConfig

Settings to export Otorshi events

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bufferSize** | **Integer** | buffer size |  [optional] |
|**config** | [**DataExporterConfigConfig**](DataExporterConfigConfig.md) |  |  [optional] |
|**desc** | **String** | Description |  [optional] |
|**enabled** | **String** | Boolean |  [optional] |
|**filtering** | [**Filtering**](Filtering.md) |  |  [optional] |
|**groupDuration** | **Long** | duration |  [optional] |
|**groupSize** | **Integer** | Group size |  [optional] |
|**id** | **String** | Id |  [optional] |
|**jsonWorkers** | **Integer** | nb workers |  [optional] |
|**location** | [**Location**](Location.md) |  |  [optional] |
|**metadata** | **Map&lt;String, String&gt;** | Metadata |  [optional] |
|**name** | **String** | Name |  [optional] |
|**projection** | **Map&lt;String, String&gt;** | projection |  [optional] |
|**sendWorkers** | **Integer** | send workers |  [optional] |
|**typ** | [**TypEnum**](#TypEnum) | Type of data exporter |  [optional] |



## Enum: TypEnum

| Name | Value |
|---- | -----|
| KAFKA | &quot;kafka&quot; |
| PULSAR | &quot;pulsar&quot; |
| FILE | &quot;file&quot; |
| MAILER | &quot;mailer&quot; |
| ELASTIC | &quot;elastic&quot; |
| CONSOLE | &quot;console&quot; |
| CUSTOM | &quot;custom&quot; |



