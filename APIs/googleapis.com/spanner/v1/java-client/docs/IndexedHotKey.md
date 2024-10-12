

# IndexedHotKey

A message representing a (sparse) collection of hot keys for specific key buckets.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**sparseHotKeys** | **Map&lt;String, Integer&gt;** | A (sparse) mapping from key bucket index to the index of the specific hot row key for that key bucket. The index of the hot row key can be translated to the actual row key via the ScanData.VisualizationData.indexed_keys repeated field. |  [optional] |



