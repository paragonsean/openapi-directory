

# Row

A row of altitude points in the elevation grid, ordered from west to east.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**altitudeDiffs** | **List&lt;Integer&gt;** | The difference between each successive pair of altitudes, from west to east. The first, westmost point, is just the altitude rather than a diff. The units are specified by the altitude_multiplier parameter above; the value in meters is given by altitude_multiplier * altitude_diffs[n]. The altitude row (in metres above sea level) can be reconstructed with: a[0] &#x3D; altitude_diffs[0] * altitude_multiplier when n &gt; 0, a[n] &#x3D; a[n-1] + altitude_diffs[n-1] * altitude_multiplier. |  [optional] |



