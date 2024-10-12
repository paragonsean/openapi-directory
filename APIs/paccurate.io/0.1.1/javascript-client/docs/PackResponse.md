# PaccurateIo.PackResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**boxes** | [**[Box]**](Box.md) | List of boxes, packed, with their contained items. | [optional] 
**built** | **String** | build timestamp of engine. | [optional] 
**leftovers** | [**[Item]**](Item.md) | items left over that could not be packed into any available boxes. | [optional] 
**lenBoxes** | **Number** | cardinality of all packed boxes | [optional] 
**lenItems** | **Number** | cardinality of all items | [optional] 
**lenLeftovers** | **Number** | cardinality of items unabled to be packed | [optional] 
**packTime** | **Number** | seconds spent in packing | [optional] 
**renderTime** | **Number** | seconds spent in rendering and placement instruction creation of packing solution | [optional] 
**scripts** | **String** | additional javascripts for any image loading. | [optional] 
**styles** | **String** | additional styles for pack images | [optional] 
**svgs** | **String** | all box SVG images | [optional] 
**title** | **String** | title of packing result, when applicable. | [optional] 
**totalCost** | **Number** | total estimated cost of all packed boxes, when applicable, in cents. | [optional] 
**totalTime** | **Number** | seconds spent generating response, total. | [optional] 
**version** | **String** | version of engine | [optional] 


