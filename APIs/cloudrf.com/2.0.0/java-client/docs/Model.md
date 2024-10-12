

# Model


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cli** | **Integer** | Radio climate for ITM model (1). 1: Equatorial (Congo) 2: Continental Subtropical (Sudan) 3: Maritime Subtropical (West coast of Africa) 4: Desert (Sahara) 5: Continental Temperate 6: Maritime Temperate, over land (UK and west coasts of US &amp; EU) 7: Maritime Temperate, over sea |  [optional] |
|**ked** | **Integer** | Knife edge diffraction for enhancing basic empirical models (Already in ITM) |  [optional] |
|**pe** | **Integer** | Propagation model subtype/environment. 1&#x3D;Conservative/Urban,2&#x3D;Average/Suburban,3&#x3D;Optimistic/rural |  [optional] |
|**pm** | **Integer** | Propagation model. 1&#x3D;Irregular Terrain Model, 2&#x3D;Line of Sight (LOS), 3&#x3D;Hata, 4&#x3D;ECC33, 5&#x3D;SUI Microwave, 6&#x3D;COST231, 7&#x3D;Free space path loss, 9&#x3D;Ericsson9999, 10&#x3D;Plane earth loss, 11&#x3D;Egli. |  [optional] |
|**rel** | **Integer** | ITM model required reliability as % |  [optional] |
|**ter** | **Integer** | Terrain code for ITM model (1). 1&#x3D;Water,2&#x3D;Wet ground,3&#x3D;Farmland,4&#x3D;Forest/Average,5&#x3D;Mountain/Sand,6&#x3D;City/Poor ground |  [optional] |



