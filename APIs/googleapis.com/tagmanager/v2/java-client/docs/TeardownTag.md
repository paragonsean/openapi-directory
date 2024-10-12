

# TeardownTag

Represents a tag that fires after another tag in order to tear down dependencies.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**stopTeardownOnFailure** | **Boolean** | If true, fire the teardown tag if and only if the main tag fires successfully. If false, fire the teardown tag regardless of main tag firing status. |  [optional] |
|**tagName** | **String** | The name of the teardown tag. |  [optional] |



