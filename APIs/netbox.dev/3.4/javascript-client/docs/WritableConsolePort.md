# NetBoxApi.WritableConsolePort

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**occupied** | **Boolean** |  | [optional] [readonly] 
**cable** | [**NestedCable**](NestedCable.md) |  | [optional] 
**cableEnd** | **String** |  | [optional] [readonly] 
**connectedEndpoints** | **[String]** |  Return the appropriate serializer for the type of connected object.  | [optional] [readonly] 
**connectedEndpointsReachable** | **Boolean** |  | [optional] [readonly] 
**connectedEndpointsType** | **String** |  | [optional] [readonly] 
**created** | **Date** |  | [optional] [readonly] 
**customFields** | **Object** |  | [optional] 
**description** | **String** |  | [optional] 
**device** | **Number** |  | 
**display** | **String** |  | [optional] [readonly] 
**id** | **Number** |  | [optional] [readonly] 
**label** | **String** | Physical label | [optional] 
**lastUpdated** | **Date** |  | [optional] [readonly] 
**linkPeers** | **[String]** |  Return the appropriate serializer for the link termination model.  | [optional] [readonly] 
**linkPeersType** | **String** |  | [optional] [readonly] 
**markConnected** | **Boolean** | Treat as if a cable is connected | [optional] 
**module** | **Number** |  | [optional] 
**name** | **String** |  | 
**speed** | **Number** | Port speed in bits per second | [optional] 
**tags** | [**[NestedTag]**](NestedTag.md) |  | [optional] 
**type** | **String** | Physical port type | [optional] 
**url** | **String** |  | [optional] [readonly] 



## Enum: SpeedEnum


* `1200` (value: `1200`)

* `2400` (value: `2400`)

* `4800` (value: `4800`)

* `9600` (value: `9600`)

* `19200` (value: `19200`)

* `38400` (value: `38400`)

* `57600` (value: `57600`)

* `115200` (value: `115200`)





## Enum: TypeEnum


* `de-9` (value: `"de-9"`)

* `db-25` (value: `"db-25"`)

* `rj-11` (value: `"rj-11"`)

* `rj-12` (value: `"rj-12"`)

* `rj-45` (value: `"rj-45"`)

* `mini-din-8` (value: `"mini-din-8"`)

* `usb-a` (value: `"usb-a"`)

* `usb-b` (value: `"usb-b"`)

* `usb-c` (value: `"usb-c"`)

* `usb-mini-a` (value: `"usb-mini-a"`)

* `usb-mini-b` (value: `"usb-mini-b"`)

* `usb-micro-a` (value: `"usb-micro-a"`)

* `usb-micro-b` (value: `"usb-micro-b"`)

* `usb-micro-ab` (value: `"usb-micro-ab"`)

* `other` (value: `"other"`)




