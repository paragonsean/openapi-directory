# openapi-java-client

CBB v3 Scores
- API version: 1.0
  - Build date: 2024-10-12T10:05:10.258689-04:00[America/New_York]
  - Generator version: 7.9.0

No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)


*Automatically generated by the [OpenAPI Generator](https://openapi-generator.tech)*


## Requirements

Building the API client library requires:
1. Java 1.8+
2. Maven (3.8.3+)/Gradle (7.2+)

## Installation

To install the API client library to your local Maven repository, simply execute:

```shell
mvn clean install
```

To deploy it to a remote Maven repository instead, configure the settings of the repository and execute:

```shell
mvn clean deploy
```

Refer to the [OSSRH Guide](http://central.sonatype.org/pages/ossrh-guide.html) for more information.

### Maven users

Add this dependency to your project's POM:

```xml
<dependency>
  <groupId>org.openapitools</groupId>
  <artifactId>openapi-java-client</artifactId>
  <version>1.0</version>
  <scope>compile</scope>
</dependency>
```

### Gradle users

Add this dependency to your project's build file:

```groovy
  repositories {
    mavenCentral()     // Needed if the 'openapi-java-client' jar has been published to maven central.
    mavenLocal()       // Needed if the 'openapi-java-client' jar has been published to the local maven repo.
  }

  dependencies {
     implementation "org.openapitools:openapi-java-client:1.0"
  }
```

### Others

At first generate the JAR by executing:

```shell
mvn clean package
```

Then manually install the following JARs:

* `target/openapi-java-client-1.0.jar`
* `target/lib/*.jar`

## Getting Started

Please follow the [installation](#installation) instruction and execute the following Java code:

```java

// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.model.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://azure-api.sportsdata.io/v3/cbb/scores");
    
    // Configure API key authorization: apiKeyQuery
    ApiKeyAuth apiKeyQuery = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyQuery");
    apiKeyQuery.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyQuery.setApiKeyPrefix("Token");

    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String format = "XML"; // String | Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
    try {
      Boolean result = apiInstance.areGamesInProgress(format);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#areGamesInProgress");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}

```

## Documentation for API Endpoints

All URIs are relative to *http://azure-api.sportsdata.io/v3/cbb/scores*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DefaultApi* | [**areGamesInProgress**](docs/DefaultApi.md#areGamesInProgress) | **GET** /{format}/AreAnyGamesInProgress | Are Games In Progress
*DefaultApi* | [**currentSeason**](docs/DefaultApi.md#currentSeason) | **GET** /{format}/CurrentSeason | Current Season
*DefaultApi* | [**gamesByDate**](docs/DefaultApi.md#gamesByDate) | **GET** /{format}/GamesByDate/{date} | Games by Date
*DefaultApi* | [**gamesByDateBasic**](docs/DefaultApi.md#gamesByDateBasic) | **GET** /{format}/ScoresBasic/{date} | Games by Date (Basic)
*DefaultApi* | [**injuredPlayers**](docs/DefaultApi.md#injuredPlayers) | **GET** /{format}/InjuredPlayers | Injured Players
*DefaultApi* | [**leagueHierarchy**](docs/DefaultApi.md#leagueHierarchy) | **GET** /{format}/LeagueHierarchy | League Hierarchy
*DefaultApi* | [**playerDetailsByActive**](docs/DefaultApi.md#playerDetailsByActive) | **GET** /{format}/Players | Player Details by Active
*DefaultApi* | [**playerDetailsByPlayer**](docs/DefaultApi.md#playerDetailsByPlayer) | **GET** /{format}/Player/{playerid} | Player Details by Player
*DefaultApi* | [**playerDetailsByTeam**](docs/DefaultApi.md#playerDetailsByTeam) | **GET** /{format}/Players/{team} | Player Details by Team
*DefaultApi* | [**playersByTeamBasic**](docs/DefaultApi.md#playersByTeamBasic) | **GET** /{format}/PlayersBasic/{team} | Players by Team (Basic)
*DefaultApi* | [**schedules**](docs/DefaultApi.md#schedules) | **GET** /{format}/Games/{season} | Schedules
*DefaultApi* | [**schedulesBasic**](docs/DefaultApi.md#schedulesBasic) | **GET** /{format}/SchedulesBasic/{season} | Schedules (Basic)
*DefaultApi* | [**stadiums**](docs/DefaultApi.md#stadiums) | **GET** /{format}/Stadiums | Stadiums
*DefaultApi* | [**teamGameLogsBySeason**](docs/DefaultApi.md#teamGameLogsBySeason) | **GET** /{format}/TeamGameStatsBySeason/{season}/{teamid}/{numberofgames} | Team Game Logs By Season
*DefaultApi* | [**teamGameStatsByDate**](docs/DefaultApi.md#teamGameStatsByDate) | **GET** /{format}/TeamGameStatsByDate/{date} | Team Game Stats by Date
*DefaultApi* | [**teamSchedule**](docs/DefaultApi.md#teamSchedule) | **GET** /{format}/TeamSchedule/{season}/{team} | Team Schedule
*DefaultApi* | [**teamSeasonStats**](docs/DefaultApi.md#teamSeasonStats) | **GET** /{format}/TeamSeasonStats/{season} | Team Season Stats
*DefaultApi* | [**teams**](docs/DefaultApi.md#teams) | **GET** /{format}/teams | Teams
*DefaultApi* | [**teamsBasic**](docs/DefaultApi.md#teamsBasic) | **GET** /{format}/TeamsBasic | Teams (Basic)
*DefaultApi* | [**tournamentHierarchy**](docs/DefaultApi.md#tournamentHierarchy) | **GET** /{format}/Tournament/{season} | Tournament Hierarchy


## Documentation for Models

 - [Conference](docs/Conference.md)
 - [Game](docs/Game.md)
 - [Period](docs/Period.md)
 - [Player](docs/Player.md)
 - [PlayerBasic](docs/PlayerBasic.md)
 - [ScheduleBasic](docs/ScheduleBasic.md)
 - [ScoreBasic](docs/ScoreBasic.md)
 - [Season](docs/Season.md)
 - [Stadium](docs/Stadium.md)
 - [Team](docs/Team.md)
 - [TeamBasic](docs/TeamBasic.md)
 - [TeamGame](docs/TeamGame.md)
 - [TeamSeason](docs/TeamSeason.md)
 - [Tournament](docs/Tournament.md)


<a id="documentation-for-authorization"></a>
## Documentation for Authorization


Authentication schemes defined for the API:
<a id="apiKeyHeader"></a>
### apiKeyHeader

- **Type**: API key
- **API key parameter name**: Ocp-Apim-Subscription-Key
- **Location**: HTTP header

<a id="apiKeyQuery"></a>
### apiKeyQuery

- **Type**: API key
- **API key parameter name**: key
- **Location**: URL query string


## Recommendation

It's recommended to create an instance of `ApiClient` per thread in a multithreaded environment to avoid any potential issues.

## Author



