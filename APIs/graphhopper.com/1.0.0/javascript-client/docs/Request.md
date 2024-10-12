# GraphHopperDirectionsApi.Request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**algorithm** | [**Algorithm**](Algorithm.md) |  | [optional] 
**configuration** | [**Configuration**](Configuration.md) |  | [optional] 
**costMatrices** | [**[CostMatrix]**](CostMatrix.md) | Specifies your own tranport time and distance matrices. | [optional] 
**objectives** | [**[Objective]**](Objective.md) | Specifies an objective function. The vehicle routing problem is solved in such a way that this objective function is minimized. | [optional] 
**relations** | [**[RequestRelationsInner]**](RequestRelationsInner.md) | Defines additional relationships between orders. | [optional] 
**services** | [**[Service]**](Service.md) | Specifies the orders of the type \&quot;service\&quot;. These are, for example, pick-ups, deliveries or other stops that are to be approached by the specified vehicles. Each of these orders contains only one location. | [optional] 
**shipments** | [**[Shipment]**](Shipment.md) | Specifies the available shipments. Each shipment contains a pickup and a delivery stop, which must be processed one after the other. | [optional] 
**vehicleTypes** | [**[VehicleType]**](VehicleType.md) | Specifies the available vehicle types. These types can be assigned to vehicles. | [optional] 
**vehicles** | [**[Vehicle]**](Vehicle.md) | Specifies the available vehicles. | [optional] 


