

# ManagedConfiguration

A managed configuration resource contains the set of managed properties defined by the app developer in the app's managed configurations schema, as well as any configuration variables defined for the user.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**configurationVariables** | [**ConfigurationVariables**](ConfigurationVariables.md) |  |  [optional] |
|**kind** | **String** | Deprecated. |  [optional] |
|**managedProperty** | [**List&lt;ManagedProperty&gt;**](ManagedProperty.md) | The set of managed properties for this configuration. |  [optional] |
|**productId** | **String** | The ID of the product that the managed configuration is for, e.g. \&quot;app:com.google.android.gm\&quot;. |  [optional] |



