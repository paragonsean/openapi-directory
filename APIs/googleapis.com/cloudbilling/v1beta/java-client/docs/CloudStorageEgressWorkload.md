

# CloudStorageEgressWorkload

Specification of a network type. Network data transfer within Google Cloud applies when you move or copy data from one Cloud Storage bucket to another or when another Google Cloud service accesses data in your Cloud Storage bucket.This includes the network data transfer within Google Cloud and the general network usage.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**destinationContinent** | [**DestinationContinentEnum**](#DestinationContinentEnum) | Where the data is sent to. |  [optional] |
|**egressRate** | [**Usage**](Usage.md) |  |  [optional] |
|**sourceContinent** | [**SourceContinentEnum**](#SourceContinentEnum) | Where the data comes from. |  [optional] |



## Enum: DestinationContinentEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;DESTINATION_CONTINENT_UNSPECIFIED&quot; |
| ASIA_PACIFIC | &quot;DESTINATION_CONTINENT_ASIA_PACIFIC&quot; |
| AUTRALIA | &quot;DESTINATION_CONTINENT_AUTRALIA&quot; |
| EUROPE | &quot;DESTINATION_CONTINENT_EUROPE&quot; |
| NORTH_AMERICA | &quot;DESTINATION_CONTINENT_NORTH_AMERICA&quot; |
| SOUTH_AMERICA | &quot;DESTINATION_CONTINENT_SOUTH_AMERICA&quot; |



## Enum: SourceContinentEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;SOURCE_CONTINENT_UNSPECIFIED&quot; |
| ASIA_PACIFIC | &quot;SOURCE_CONTINENT_ASIA_PACIFIC&quot; |
| AUSTRALIA | &quot;SOURCE_CONTINENT_AUSTRALIA&quot; |
| EUROPE | &quot;SOURCE_CONTINENT_EUROPE&quot; |
| NORTH_AMERICA | &quot;SOURCE_CONTINENT_NORTH_AMERICA&quot; |
| SOUTH_AMERICA | &quot;SOURCE_CONTINENT_SOUTH_AMERICA&quot; |



