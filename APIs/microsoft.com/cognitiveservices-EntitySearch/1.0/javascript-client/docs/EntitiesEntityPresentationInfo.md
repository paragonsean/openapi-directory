# EntitySearchClient.EntitiesEntityPresentationInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entityScenario** | **String** | The supported scenario. | [default to &#39;DominantEntity&#39;]
**entityTypeDisplayHint** | **String** | A display version of the entity hint. For example, if entityTypeHints is Artist, this field may be set to American Singer. | [optional] [readonly] 
**entityTypeHints** | **[String]** | A list of hints that indicate the entity&#39;s type. The list could contain a single hint such as Movie or a list of hints such as Place, LocalBusiness, Restaurant. Each successive hint in the array narrows the entity&#39;s type. | [optional] [readonly] 



## Enum: EntityScenarioEnum


* `DominantEntity` (value: `"DominantEntity"`)

* `DisambiguationItem` (value: `"DisambiguationItem"`)

* `ListItem` (value: `"ListItem"`)





## Enum: [EntityTypeHintsEnum]


* `Generic` (value: `"Generic"`)

* `Person` (value: `"Person"`)

* `Place` (value: `"Place"`)

* `Media` (value: `"Media"`)

* `Organization` (value: `"Organization"`)

* `LocalBusiness` (value: `"LocalBusiness"`)

* `Restaurant` (value: `"Restaurant"`)

* `Hotel` (value: `"Hotel"`)

* `TouristAttraction` (value: `"TouristAttraction"`)

* `Travel` (value: `"Travel"`)

* `City` (value: `"City"`)

* `Country` (value: `"Country"`)

* `Attraction` (value: `"Attraction"`)

* `House` (value: `"House"`)

* `State` (value: `"State"`)

* `RadioStation` (value: `"RadioStation"`)

* `StreetAddress` (value: `"StreetAddress"`)

* `Neighborhood` (value: `"Neighborhood"`)

* `Locality` (value: `"Locality"`)

* `PostalCode` (value: `"PostalCode"`)

* `Region` (value: `"Region"`)

* `SubRegion` (value: `"SubRegion"`)

* `MinorRegion` (value: `"MinorRegion"`)

* `Continent` (value: `"Continent"`)

* `PointOfInterest` (value: `"PointOfInterest"`)

* `Other` (value: `"Other"`)

* `Movie` (value: `"Movie"`)

* `Book` (value: `"Book"`)

* `TelevisionShow` (value: `"TelevisionShow"`)

* `TelevisionSeason` (value: `"TelevisionSeason"`)

* `VideoGame` (value: `"VideoGame"`)

* `MusicAlbum` (value: `"MusicAlbum"`)

* `MusicRecording` (value: `"MusicRecording"`)

* `MusicGroup` (value: `"MusicGroup"`)

* `Composition` (value: `"Composition"`)

* `TheaterPlay` (value: `"TheaterPlay"`)

* `Event` (value: `"Event"`)

* `Actor` (value: `"Actor"`)

* `Artist` (value: `"Artist"`)

* `Attorney` (value: `"Attorney"`)

* `Speciality` (value: `"Speciality"`)

* `CollegeOrUniversity` (value: `"CollegeOrUniversity"`)

* `School` (value: `"School"`)

* `Food` (value: `"Food"`)

* `Drug` (value: `"Drug"`)

* `Animal` (value: `"Animal"`)

* `SportsTeam` (value: `"SportsTeam"`)

* `Product` (value: `"Product"`)

* `Car` (value: `"Car"`)




