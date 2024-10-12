# ShutterstockApiExplorer.SearchImage

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addedDate** | **Date** | Show images added on the specified date | [optional] 
**addedDateEnd** | **Date** | Show images added before the specified date | [optional] 
**addedDateStart** | **Date** | Show images added on or after the specified date | [optional] 
**aspectRatio** | **Number** | Show images with the specified aspect ratio, using a positive decimal of the width divided by the height, such as 1.7778 for a 16:9 image | [optional] 
**aspectRatioMax** | **Number** | Show images with the specified aspect ratio or lower, using a positive decimal of the width divided by the height, such as 1.7778 for a 16:9 image | [optional] 
**aspectRatioMin** | **Number** | Show images with the specified aspect ratio or higher, using a positive decimal of the width divided by the height, such as 1.7778 for a 16:9 image | [optional] 
**authentic** | **Boolean** | Show only authentic images | [optional] 
**category** | **String** | Show images with the specified Shutterstock-defined category; specify a category name or ID | [optional] 
**color** | **String** | Specify either a hexadecimal color in the format &#39;4F21EA&#39; or &#39;grayscale&#39;; the API returns images that use similar colors | [optional] 
**contributor** | **[String]** | Show images with the specified contributor names or IDs, allows multiple | [optional] 
**contributorCountry** | [**SearchImageContributorCountry**](SearchImageContributorCountry.md) |  | [optional] 
**fields** | **String** | Fields to display in the response; see the documentation for the fields parameter in the overview section | [optional] 
**height** | **Number** | (Deprecated; use height_from and height_to instead) Show images with the specified height | [optional] 
**heightFrom** | **Number** | Show images with the specified height or larger, in pixels | [optional] 
**heightTo** | **Number** | Show images with the specified height or smaller, in pixels | [optional] 
**imageType** | **[String]** | Show images of the specified type | [optional] 
**keywordSafeSearch** | **Boolean** | Hide results with potentially unsafe keywords | [optional] [default to true]
**language** | [**Language**](Language.md) |  | [optional] 
**license** | **[String]** | Show only images with the specified license | [optional] 
**model** | **[String]** | Show image results with the specified model IDs | [optional] 
**orientation** | **String** | Show image results with horizontal or vertical orientation | [optional] 
**page** | **Number** | Page number | [optional] [default to 1]
**peopleAge** | **String** | Show images that feature people of the specified age category | [optional] 
**peopleEthnicity** | **[String]** | Show images with people of the specified ethnicities, or start with NOT to show images without those ethnicities | [optional] 
**peopleGender** | **String** | Show images with people of the specified gender | [optional] 
**peopleModelReleased** | **Boolean** | Show images of people with a signed model release | [optional] 
**peopleNumber** | **Number** | Show images with the specified number of people | [optional] 
**perPage** | **Number** | Number of results per page | [optional] [default to 20]
**query** | **String** | One or more search terms separated by spaces; you can use NOT to filter out images that match a term | [optional] 
**region** | [**SearchImageRegion**](SearchImageRegion.md) |  | [optional] 
**safe** | **Boolean** | Enable or disable safe search | [optional] [default to true]
**sort** | **String** | Sort by | [optional] [default to &#39;popular&#39;]
**spellcheckQuery** | **Boolean** | Spellcheck the search query and return results on suggested spellings | [optional] [default to true]
**view** | **String** | Amount of detail to render in the response | [optional] [default to &#39;minimal&#39;]
**width** | **Number** | (Deprecated; use width_from and width_to instead) Show images with the specified width | [optional] 
**widthFrom** | **Number** | Show images with the specified width or larger, in pixels | [optional] 
**widthTo** | **Number** | Show images with the specified width or smaller, in pixels | [optional] 



## Enum: [ImageTypeEnum]


* `photo` (value: `"photo"`)

* `illustration` (value: `"illustration"`)

* `vector` (value: `"vector"`)





## Enum: [LicenseEnum]


* `commercial` (value: `"commercial"`)

* `editorial` (value: `"editorial"`)

* `enhanced` (value: `"enhanced"`)





## Enum: OrientationEnum


* `horizontal` (value: `"horizontal"`)

* `vertical` (value: `"vertical"`)





## Enum: PeopleAgeEnum


* `infants` (value: `"infants"`)

* `children` (value: `"children"`)

* `teenagers` (value: `"teenagers"`)

* `20s` (value: `"20s"`)

* `30s` (value: `"30s"`)

* `40s` (value: `"40s"`)

* `50s` (value: `"50s"`)

* `60s` (value: `"60s"`)

* `older` (value: `"older"`)





## Enum: [PeopleEthnicityEnum]


* `african` (value: `"african"`)

* `african_american` (value: `"african_american"`)

* `black` (value: `"black"`)

* `brazilian` (value: `"brazilian"`)

* `chinese` (value: `"chinese"`)

* `caucasian` (value: `"caucasian"`)

* `east_asian` (value: `"east_asian"`)

* `hispanic` (value: `"hispanic"`)

* `japanese` (value: `"japanese"`)

* `middle_eastern` (value: `"middle_eastern"`)

* `native_american` (value: `"native_american"`)

* `pacific_islander` (value: `"pacific_islander"`)

* `south_asian` (value: `"south_asian"`)

* `southeast_asian` (value: `"southeast_asian"`)

* `other` (value: `"other"`)

* `NOT african` (value: `"NOT african"`)

* `NOT african_american` (value: `"NOT african_american"`)

* `NOT black` (value: `"NOT black"`)

* `NOT brazilian` (value: `"NOT brazilian"`)

* `NOT chinese` (value: `"NOT chinese"`)

* `NOT caucasian` (value: `"NOT caucasian"`)

* `NOT east_asian` (value: `"NOT east_asian"`)

* `NOT hispanic` (value: `"NOT hispanic"`)

* `NOT japanese` (value: `"NOT japanese"`)

* `NOT middle_eastern` (value: `"NOT middle_eastern"`)

* `NOT native_american` (value: `"NOT native_american"`)

* `NOT pacific_islander` (value: `"NOT pacific_islander"`)

* `NOT south_asian` (value: `"NOT south_asian"`)

* `NOT southeast_asian` (value: `"NOT southeast_asian"`)

* `NOT other` (value: `"NOT other"`)





## Enum: PeopleGenderEnum


* `male` (value: `"male"`)

* `female` (value: `"female"`)

* `both` (value: `"both"`)





## Enum: SortEnum


* `newest` (value: `"newest"`)

* `popular` (value: `"popular"`)

* `relevance` (value: `"relevance"`)

* `random` (value: `"random"`)





## Enum: ViewEnum


* `minimal` (value: `"minimal"`)

* `full` (value: `"full"`)




