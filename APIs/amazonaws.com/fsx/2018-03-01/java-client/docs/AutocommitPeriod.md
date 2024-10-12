

# AutocommitPeriod

<p>Sets the autocommit period of files in an FSx for ONTAP SnapLock volume, which determines how long the files must remain unmodified before they're automatically transitioned to the write once, read many (WORM) state. </p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/worm-state.html#worm-state-autocommit\">Autocommit</a>. </p>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**type** | [**AutocommitPeriodType**](AutocommitPeriodType.md) |  |  |
|**value** | [**Integer**](Integer.md) |  |  [optional] |



