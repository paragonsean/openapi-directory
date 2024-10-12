# MerakiDashboardApi.UpdateNetworkFloorPlanRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bottomLeftCorner** | [**CreateNetworkFloorPlanRequestBottomLeftCorner**](CreateNetworkFloorPlanRequestBottomLeftCorner.md) |  | [optional] 
**bottomRightCorner** | [**CreateNetworkFloorPlanRequestBottomRightCorner**](CreateNetworkFloorPlanRequestBottomRightCorner.md) |  | [optional] 
**center** | [**UpdateNetworkFloorPlanRequestCenter**](UpdateNetworkFloorPlanRequestCenter.md) |  | [optional] 
**imageContents** | **Blob** | The file contents (a base 64 encoded string) of your new image. Supported formats are PNG, GIF, and JPG. Note that all images are saved as PNG files, regardless of the format they are uploaded in. If you upload a new image, and you do NOT specify any new geolocation fields (&#39;center, &#39;topLeftCorner&#39;, etc), the floor plan will be recentered with no rotation in order to maintain the aspect ratio of your new image. | [optional] 
**name** | **String** | The name of your floor plan. | [optional] 
**topLeftCorner** | [**CreateNetworkFloorPlanRequestTopLeftCorner**](CreateNetworkFloorPlanRequestTopLeftCorner.md) |  | [optional] 
**topRightCorner** | [**CreateNetworkFloorPlanRequestTopRightCorner**](CreateNetworkFloorPlanRequestTopRightCorner.md) |  | [optional] 


