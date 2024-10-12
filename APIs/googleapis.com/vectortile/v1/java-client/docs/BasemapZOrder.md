

# BasemapZOrder

Metadata necessary to determine the ordering of a particular basemap element relative to others. To render the basemap correctly, sort by z-plane, then z-grade, then z-within-grade.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**zGrade** | **Integer** | The second most significant component of the ordering of a component to be rendered onto the basemap. |  [optional] |
|**zPlane** | **Integer** | The most significant component of the ordering of a component to be rendered onto the basemap. |  [optional] |
|**zWithinGrade** | **Integer** | The least significant component of the ordering of a component to be rendered onto the basemap. |  [optional] |



