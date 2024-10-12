# Json2VideoApi.BaseElement

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cache** | **Boolean** | Element&#39;s cache policy. When true, the cached version (if exists) is used. When false, the assets is downloaded. | [optional] [default to true]
**comment** | **String** | Used for adding your comments | [optional] 
**duration** | **Number** | Element&#39;s duration in seconds. A value of -1 auto calculates the duration based on the asset intrinsic length or the scene duration. | [optional] [default to -1]
**extraTime** | **Number** | Element&#39;s time span added after the playback. | [optional] [default to 0]
**fadeIn** | **Number** | Adds a fade in effect to the element. Value in seconds. | [optional] 
**fadeOut** | **Number** | Adds a fade out effect to the element. Value in seconds. | [optional] 
**start** | **Number** | Element&#39;s starting time in seconds relative to the container scene or the movie if the element is in the Movie&#39;s elements array. | [optional] [default to 0]
**zIndex** | **Number** | Element&#39;s z-index. Use this property to reorganize the layering of the elements like in HTML | [optional] [default to 0]


