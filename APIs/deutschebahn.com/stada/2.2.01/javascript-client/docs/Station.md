# Stationsdatenbereitstellung.Station

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dBinformation** | [**Schedule**](Schedule.md) |  | [optional] 
**aufgabentraeger** | [**Aufgabentraeger**](Aufgabentraeger.md) |  | [optional] 
**category** | **Number** | the stations category (-1...7). Stations with category -1 or 0 are not in production, e.g. planned, saled, without train stops. | [optional] 
**evaNumbers** | [**[EVANumber]**](EVANumber.md) | station related EVA-Numbers | [optional] 
**federalState** | **String** | german federal state | [optional] 
**hasBicycleParking** | **Boolean** | public bicycle parking y/n | [optional] 
**hasCarRental** | **Boolean** | car sharing or car rental y/n | [optional] 
**hasDBLounge** | **Boolean** | DB lounge y/n | [optional] 
**hasLocalPublicTransport** | **Boolean** | local public transport y/n | [optional] 
**hasLockerSystem** | **Boolean** | public facilities y/n | [optional] 
**hasLostAndFound** | **Boolean** | lost and found y/n | [optional] 
**hasMobilityService** | **String** | values are &#39;no&#39;, &#39;yes, advance notification is requested...&#39; or &#39;yes, advance notification is required...&#39; | [optional] 
**hasParking** | **Boolean** | public parking y/n | [optional] 
**hasPublicFacilities** | **Boolean** | public facilities y/n | [optional] 
**hasRailwayMission** | **Boolean** | railway mission y/n | [optional] 
**hasSteplessAccess** | [**Partial**](Partial.md) |  | [optional] 
**hasTaxiRank** | **Boolean** | taxi rank in front of the station y/n | [optional] 
**hasTravelCenter** | **Boolean** | local travel center y/n | [optional] 
**hasTravelNecessities** | **Boolean** | a shop for travel necessities y/n | [optional] 
**hasWiFi** | **Boolean** | public Wi-Fi is available y/n | [optional] 
**localServiceStaff** | [**Schedule**](Schedule.md) |  | [optional] 
**mailingAdress** | [**Address**](Address.md) |  | [optional] 
**name** | **String** | the stations name | [optional] 
**number** | **Number** | unique identifier representing a specific railway station | [optional] 
**priceCategory** | **Number** | determines in some respect the price for train stops at a specific station (1..7) | [optional] 
**regionalbereich** | [**RegionalBereichRef**](RegionalBereichRef.md) |  | [optional] 
**riL100Identifiers** | [**[RiL100Identifier]**](RiL100Identifier.md) | station related Ril100s | [optional] 
**stationManagement** | [**StationManagementRef**](StationManagementRef.md) |  | [optional] 
**szentrale** | [**SZentraleRef**](SZentraleRef.md) |  | [optional] 
**timetableOffice** | [**TimetableOffice**](TimetableOffice.md) |  | [optional] 


