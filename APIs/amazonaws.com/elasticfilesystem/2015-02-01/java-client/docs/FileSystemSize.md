

# FileSystemSize

The latest known metered size (in bytes) of data stored in the file system, in its <code>Value</code> field, and the time at which that size was determined in its <code>Timestamp</code> field. The value doesn't represent the size of a consistent snapshot of the file system, but it is eventually consistent when there are no writes to the file system. That is, the value represents the actual size only if the file system is not modified for a period longer than a couple of hours. Otherwise, the value is not necessarily the exact size the file system was at any instant in time.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**value** | [**Integer**](Integer.md) |  |  |
|**timestamp** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**valueInIA** | [**Integer**](Integer.md) |  |  [optional] |
|**valueInStandard** | [**Integer**](Integer.md) |  |  [optional] |



