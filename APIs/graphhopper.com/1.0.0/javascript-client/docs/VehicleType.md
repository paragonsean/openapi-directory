# GraphHopperDirectionsApi.VehicleType

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**capacity** | **[Number]** | Specifies an array of capacity dimension values which need to be int values. For example, if there are two dimensions such as volume and weight then it needs to be defined as [ 1000, 300 ] assuming a maximum volume of 1000 and a maximum weight of 300. | [optional] 
**considerTraffic** | **Boolean** | Specifies whether traffic should be considered. if \&quot;tomtom\&quot; is used and this is false, free flow travel times from \&quot;tomtom\&quot; are calculated. If this is true, historical traffic info are used. We do not yet have traffic data for \&quot;openstreetmap\&quot;, thus, setting this true has no effect at all. | [optional] [default to false]
**costPerActivation** | **Number** | **_BETA feature_**! Cost parameter vehicle activation, i.e. fixed costs per vehicle | [optional] 
**costPerMeter** | **Number** | **_BETA feature_**! Cost parameter per distance unit, here meter is used | [optional] 
**costPerSecond** | **Number** | **_BETA feature_**! Cost parameter per time unit, here second is used | [optional] 
**networkDataProvider** | **String** | Specifies the network data provider. Either use [&#x60;openstreetmap&#x60;](#section/Map-Data-and-Routing-Profiles/OpenStreetMap) (default) or [&#x60;tomtom&#x60;](#section/Map-Data-and-Routing-Profiles/TomTom) (add-on required). | [optional] [default to &#39;openstreetmap&#39;]
**profile** | **Object** |  | [optional] 
**serviceTimeFactor** | **Number** | Specifies a service time factor for this vehicle type. If the vehicle/driver that uses this type is able to conduct the service as double as fast as it is determined in the corresponding service or shipment then set it to 0.5. | [optional] [default to 1]
**speedFactor** | **Number** | Specifies a speed factor for this vehicle type. If the vehicle that uses this type needs to be only half as fast as what is actually calculated with our routing engine then set the speed factor to 0.5. | [optional] [default to 1]
**typeId** | **String** | Specifies the id of the vehicle type. If a vehicle needs to be of this type, it should refer to this with its type_id attribute. | 



## Enum: NetworkDataProviderEnum


* `openstreetmap` (value: `"openstreetmap"`)

* `tomtom` (value: `"tomtom"`)




