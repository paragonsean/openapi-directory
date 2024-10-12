

# CredasApiModelsRegistrationsRegistrationSettings


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**capturePersonalDetails** | **Boolean** |  |  [optional] |
|**nameMatchRoutine** | [**NameMatchRoutineEnum**](#NameMatchRoutineEnum) | Fuzzy &#x3D; 1, Strict &#x3D; 2 |  [optional] |
|**requiredChecks** | [**List&lt;RequiredChecksEnum&gt;**](#List&lt;RequiredChecksEnum&gt;) | The value of required checks determines what checks are performed. &lt;br/&gt;Unknown &#x3D; 0,Id Documents &#x3D; 1, Standard Checks &#x3D; 2, International Sanctions and Pep &#x3D; 3, Credit Status Check &#x3D; 4, Bank Account Check &#x3D; 5, Proof of Ownership &#x3D; 6, Right to Work &#x3D; 7, Right to Rent &#x3D; 8&lt;br /&gt; |  [optional] |
|**skipEmailStep** | **Boolean** |  |  [optional] |



## Enum: NameMatchRoutineEnum

| Name | Value |
|---- | -----|
| NUMBER_1 | 1 |
| NUMBER_2 | 2 |



## Enum: List&lt;RequiredChecksEnum&gt;

| Name | Value |
|---- | -----|
| NUMBER_0 | 0 |
| NUMBER_1 | 1 |
| NUMBER_2 | 2 |
| NUMBER_3 | 3 |
| NUMBER_4 | 4 |
| NUMBER_5 | 5 |
| NUMBER_6 | 6 |
| NUMBER_7 | 7 |
| NUMBER_8 | 8 |



