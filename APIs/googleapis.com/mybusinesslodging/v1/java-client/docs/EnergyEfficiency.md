

# EnergyEfficiency

Energy efficiency practices implemented at the hotel.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**carbonFreeEnergySources** | **Boolean** | Carbon free energy sources. Property sources carbon-free electricity via at least one of the following methods: on-site clean energy generation, power purchase agreement(s) with clean energy generators, green power provided by electricity supplier, or purchases of Energy Attribute Certificates (such as Renewable Energy Certificates or Guarantees of Origin). |  [optional] |
|**carbonFreeEnergySourcesException** | [**CarbonFreeEnergySourcesExceptionEnum**](#CarbonFreeEnergySourcesExceptionEnum) | Carbon free energy sources exception. |  [optional] |
|**energyConservationProgram** | **Boolean** | Energy conservation program. The property tracks corporate-level Scope 1 and 2 GHG emissions, and Scope 3 emissions if available. The property has a commitment to implement initiatives that reduce GHG emissions year over year. The property has shown an absolute reduction in emissions for at least 2 years. Emissions are either verfied by a third-party and/or published in external communications. |  [optional] |
|**energyConservationProgramException** | [**EnergyConservationProgramExceptionEnum**](#EnergyConservationProgramExceptionEnum) | Energy conservation program exception. |  [optional] |
|**energyEfficientHeatingAndCoolingSystems** | **Boolean** | Energy efficient heating and cooling systems. The property doesn&#39;t use chlorofluorocarbon (CFC)-based refrigerants in heating, ventilating, and air-conditioning systems unless a third-party audit shows it&#39;s not economically feasible. The CFC-based refrigerants which are used should have a Global Warming Potential (GWP) ≤ 10. The property uses occupancy sensors on HVAC systems in back-of-house spaces, meeting rooms, and other low-traffic areas. |  [optional] |
|**energyEfficientHeatingAndCoolingSystemsException** | [**EnergyEfficientHeatingAndCoolingSystemsExceptionEnum**](#EnergyEfficientHeatingAndCoolingSystemsExceptionEnum) | Energy efficient heating and cooling systems exception. |  [optional] |
|**energyEfficientLighting** | **Boolean** | Energy efficient lighting. At least 75% of the property&#39;s lighting is energy efficient, using lighting that is more than 45 lumens per watt – typically LED or CFL lightbulbs. |  [optional] |
|**energyEfficientLightingException** | [**EnergyEfficientLightingExceptionEnum**](#EnergyEfficientLightingExceptionEnum) | Energy efficient lighting exception. |  [optional] |
|**energySavingThermostats** | **Boolean** | Energy saving thermostats. The property installed energy-saving thermostats throughout the building to conserve energy when rooms or areas are not in use. Energy-saving thermostats are devices that control heating/cooling in the building by learning temperature preferences and automatically adjusting to energy-saving temperatures as the default. The thermostats are automatically set to a temperature between 68-78 degrees F (20-26 °C), depending on seasonality. In the winter, set the thermostat to 68°F (20°C) when the room is occupied, lowering room temperature when unoccupied. In the summer, set the thermostat to 78°F (26°C) when the room is occupied. |  [optional] |
|**energySavingThermostatsException** | [**EnergySavingThermostatsExceptionEnum**](#EnergySavingThermostatsExceptionEnum) | Energy saving thermostats exception. |  [optional] |
|**greenBuildingDesign** | **Boolean** | Output only. Green building design. True if the property has been awarded a relevant certification. |  [optional] [readonly] |
|**greenBuildingDesignException** | [**GreenBuildingDesignExceptionEnum**](#GreenBuildingDesignExceptionEnum) | Output only. Green building design exception. |  [optional] [readonly] |
|**independentOrganizationAuditsEnergyUse** | **Boolean** | Independent organization audits energy use. The property conducts an energy audit at least every 5 years, the results of which are either verified by a third-party and/or published in external communications. An energy audit is a detailed assessment of the facility which provides recommendations to existing operations and procedures to improve energy efficiency, available incentives or rebates,and opportunities for improvements through renovations or upgrades. Examples of organizations that conduct credible third party audits include: Engie Impact, DNV GL (EU), Dexma, and local utility providers (they often provide energy and water audits). |  [optional] |
|**independentOrganizationAuditsEnergyUseException** | [**IndependentOrganizationAuditsEnergyUseExceptionEnum**](#IndependentOrganizationAuditsEnergyUseExceptionEnum) | Independent organization audits energy use exception. |  [optional] |



## Enum: CarbonFreeEnergySourcesExceptionEnum

| Name | Value |
|---- | -----|
| EXCEPTION_UNSPECIFIED | &quot;EXCEPTION_UNSPECIFIED&quot; |
| UNDER_CONSTRUCTION | &quot;UNDER_CONSTRUCTION&quot; |
| DEPENDENT_ON_SEASON | &quot;DEPENDENT_ON_SEASON&quot; |
| DEPENDENT_ON_DAY_OF_WEEK | &quot;DEPENDENT_ON_DAY_OF_WEEK&quot; |



## Enum: EnergyConservationProgramExceptionEnum

| Name | Value |
|---- | -----|
| EXCEPTION_UNSPECIFIED | &quot;EXCEPTION_UNSPECIFIED&quot; |
| UNDER_CONSTRUCTION | &quot;UNDER_CONSTRUCTION&quot; |
| DEPENDENT_ON_SEASON | &quot;DEPENDENT_ON_SEASON&quot; |
| DEPENDENT_ON_DAY_OF_WEEK | &quot;DEPENDENT_ON_DAY_OF_WEEK&quot; |



## Enum: EnergyEfficientHeatingAndCoolingSystemsExceptionEnum

| Name | Value |
|---- | -----|
| EXCEPTION_UNSPECIFIED | &quot;EXCEPTION_UNSPECIFIED&quot; |
| UNDER_CONSTRUCTION | &quot;UNDER_CONSTRUCTION&quot; |
| DEPENDENT_ON_SEASON | &quot;DEPENDENT_ON_SEASON&quot; |
| DEPENDENT_ON_DAY_OF_WEEK | &quot;DEPENDENT_ON_DAY_OF_WEEK&quot; |



## Enum: EnergyEfficientLightingExceptionEnum

| Name | Value |
|---- | -----|
| EXCEPTION_UNSPECIFIED | &quot;EXCEPTION_UNSPECIFIED&quot; |
| UNDER_CONSTRUCTION | &quot;UNDER_CONSTRUCTION&quot; |
| DEPENDENT_ON_SEASON | &quot;DEPENDENT_ON_SEASON&quot; |
| DEPENDENT_ON_DAY_OF_WEEK | &quot;DEPENDENT_ON_DAY_OF_WEEK&quot; |



## Enum: EnergySavingThermostatsExceptionEnum

| Name | Value |
|---- | -----|
| EXCEPTION_UNSPECIFIED | &quot;EXCEPTION_UNSPECIFIED&quot; |
| UNDER_CONSTRUCTION | &quot;UNDER_CONSTRUCTION&quot; |
| DEPENDENT_ON_SEASON | &quot;DEPENDENT_ON_SEASON&quot; |
| DEPENDENT_ON_DAY_OF_WEEK | &quot;DEPENDENT_ON_DAY_OF_WEEK&quot; |



## Enum: GreenBuildingDesignExceptionEnum

| Name | Value |
|---- | -----|
| EXCEPTION_UNSPECIFIED | &quot;EXCEPTION_UNSPECIFIED&quot; |
| UNDER_CONSTRUCTION | &quot;UNDER_CONSTRUCTION&quot; |
| DEPENDENT_ON_SEASON | &quot;DEPENDENT_ON_SEASON&quot; |
| DEPENDENT_ON_DAY_OF_WEEK | &quot;DEPENDENT_ON_DAY_OF_WEEK&quot; |



## Enum: IndependentOrganizationAuditsEnergyUseExceptionEnum

| Name | Value |
|---- | -----|
| EXCEPTION_UNSPECIFIED | &quot;EXCEPTION_UNSPECIFIED&quot; |
| UNDER_CONSTRUCTION | &quot;UNDER_CONSTRUCTION&quot; |
| DEPENDENT_ON_SEASON | &quot;DEPENDENT_ON_SEASON&quot; |
| DEPENDENT_ON_DAY_OF_WEEK | &quot;DEPENDENT_ON_DAY_OF_WEEK&quot; |



