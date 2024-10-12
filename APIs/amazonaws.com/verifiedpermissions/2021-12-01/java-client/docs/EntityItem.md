

# EntityItem

<p>Contains information about an entity that can be referenced in a Cedar policy.</p> <p>This data type is used as one of the fields in the <a href=\"https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_EntitiesDefinition.html\">EntitiesDefinition</a> structure.</p> <p> <code>{ \"id\": { \"entityType\": \"Photo\", \"entityId\": \"VacationPhoto94.jpg\" }, \"Attributes\": {}, \"Parents\": [ { \"entityType\": \"Album\", \"entityId\": \"alice_folder\" } ] }</code> </p>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**identifier** | [**EntityItemIdentifier**](EntityItemIdentifier.md) |  |  |
|**attributes** | [**Map**](Map.md) |  |  [optional] |
|**parents** | [**List**](List.md) |  |  [optional] |



