# Netatmo.NAHealthyHomeCoach

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **String** |  | [optional] 
**cipherId** | **String** |  | [optional] 
**co2Calibrating** | **Boolean** |  | [optional] 
**dashboardData** | [**NADashboardData**](NADashboardData.md) |  | [optional] 
**dataType** | **[String]** |  | [optional] 
**dateSetup** | **Number** |  | [optional] 
**firmware** | **Number** |  | [optional] 
**lastSetup** | **Number** |  | [optional] 
**lastStatusStore** | **Number** |  | [optional] 
**lastUpgrade** | **Number** |  | [optional] 
**name** | **String** |  | [optional] 
**place** | [**NAPlace**](NAPlace.md) |  | [optional] 
**type** | **String** | Included in every device or module. It defines the type of the device/module. Its values are among : NHC: Healthy Home Coach  | [optional] 
**wifiStatus** | **Number** | It contains the current wifi status. The different thresholds to take into account are RSSI_THRESHOLD_0 &#x3D; 86 bad signal RSSI_THRESHOLD_1 &#x3D; 71 middle quality signal RSSI_THRESHOLD_2 &#x3D; 56 good signal  | [optional] 


