

# MemberSearchQueryParameters


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**divisionNumber** | **Integer** | Division Number - as specified by the House, unique within a session. This is different to the division id which uniquely identifies a division in this system and is passed to the GET division endpoint |  [optional] |
|**endDate** | **OffsetDateTime** | Divisions where division date in one or before date provided. Date format is yyyy-MM-dd |  [optional] |
|**includeWhenMemberWasTeller** | **Boolean** | Divisions where member was a teller as well as if they actually voted |  [optional] |
|**memberId** | **Integer** | Id number of a Member whose voting records are to be returned |  |
|**searchTerm** | **String** | Divisions containing search term within title or number |  [optional] |
|**skip** | **Integer** | The number of records to skip. Default is 0 |  [optional] |
|**startDate** | **OffsetDateTime** | Divisions where division date in one or after date provided. Date format is yyyy-MM-dd |  [optional] |
|**take** | **Integer** | The number of records to return per page. Default is 25 |  [optional] |



