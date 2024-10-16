# lo_l_v3_scores

LoLV3Scores - JavaScript client for lo_l_v3_scores
LoL v3 Scores
This SDK is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.0
- Package version: 1.0
- Generator version: 7.9.0
- Build package: org.openapitools.codegen.languages.JavascriptClientCodegen

## Installation

### For [Node.js](https://nodejs.org/)

#### npm

To publish the library as a [npm](https://www.npmjs.com/), please follow the procedure in ["Publishing npm packages"](https://docs.npmjs.com/getting-started/publishing-npm-packages).

Then install it via:

```shell
npm install lo_l_v3_scores --save
```

Finally, you need to build the module:

```shell
npm run build
```

##### Local development

To use the library locally without publishing to a remote npm registry, first install the dependencies by changing into the directory containing `package.json` (and this README). Let's call this `JAVASCRIPT_CLIENT_DIR`. Then run:

```shell
npm install
```

Next, [link](https://docs.npmjs.com/cli/link) it globally in npm with the following, also from `JAVASCRIPT_CLIENT_DIR`:

```shell
npm link
```

To use the link you just defined in your project, switch to the directory you want to use your lo_l_v3_scores from, and run:

```shell
npm link /path/to/<JAVASCRIPT_CLIENT_DIR>
```

Finally, you need to build the module:

```shell
npm run build
```

#### git

If the library is hosted at a git repository, e.g.https://github.com/GIT_USER_ID/GIT_REPO_ID
then install it via:

```shell
    npm install GIT_USER_ID/GIT_REPO_ID --save
```

### For browser

The library also works in the browser environment via npm and [browserify](http://browserify.org/). After following
the above steps with Node.js and installing browserify with `npm install -g browserify`,
perform the following (assuming *main.js* is your entry file):

```shell
browserify main.js > bundle.js
```

Then include *bundle.js* in the HTML pages.

### Webpack Configuration

Using Webpack you may encounter the following error: "Module not found: Error:
Cannot resolve module", most certainly you should disable AMD loader. Add/merge
the following section to your webpack config:

```javascript
module: {
  rules: [
    {
      parser: {
        amd: false
      }
    }
  ]
}
```

## Getting Started

Please follow the [installation](#installation) instruction and execute the following JS code:

```javascript
var LoLV3Scores = require('lo_l_v3_scores');

var defaultClient = LoLV3Scores.ApiClient.instance;
// Configure API key authorization: apiKeyQuery
var apiKeyQuery = defaultClient.authentications['apiKeyQuery'];
apiKeyQuery.apiKey = "YOUR API KEY"
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyQuery.apiKeyPrefix['key'] = "Token"
// Configure API key authorization: apiKeyHeader
var apiKeyHeader = defaultClient.authentications['apiKeyHeader'];
apiKeyHeader.apiKey = "YOUR API KEY"
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyHeader.apiKeyPrefix['Ocp-Apim-Subscription-Key'] = "Token"

var api = new LoLV3Scores.DefaultApi()
var format = "'xml'"; // {String} Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
api.areasCountries(format, callback);

```

## Documentation for API Endpoints

All URIs are relative to *http://azure-api.sportsdata.io/v3/lol/scores*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*LoLV3Scores.DefaultApi* | [**areasCountries**](docs/DefaultApi.md#areasCountries) | **GET** /{format}/Areas | Areas (Countries)
*LoLV3Scores.DefaultApi* | [**competitionFixturesLeagueDetails**](docs/DefaultApi.md#competitionFixturesLeagueDetails) | **GET** /{format}/CompetitionDetails/{competitionid} | Competition Fixtures (League Details)
*LoLV3Scores.DefaultApi* | [**competitionsLeagues**](docs/DefaultApi.md#competitionsLeagues) | **GET** /{format}/Competitions | Competitions (Leagues)
*LoLV3Scores.DefaultApi* | [**gamesByDate**](docs/DefaultApi.md#gamesByDate) | **GET** /{format}/GamesByDate/{date} | Games by Date
*LoLV3Scores.DefaultApi* | [**membershipsActive**](docs/DefaultApi.md#membershipsActive) | **GET** /{format}/ActiveMemberships | Memberships (Active)
*LoLV3Scores.DefaultApi* | [**membershipsByTeamActive**](docs/DefaultApi.md#membershipsByTeamActive) | **GET** /{format}/MembershipsByTeam/{teamid} | Memberships by Team (Active)
*LoLV3Scores.DefaultApi* | [**membershipsByTeamHistorical**](docs/DefaultApi.md#membershipsByTeamHistorical) | **GET** /{format}/HistoricalMembershipsByTeam/{teamid} | Memberships by Team (Historical)
*LoLV3Scores.DefaultApi* | [**membershipsHistorical**](docs/DefaultApi.md#membershipsHistorical) | **GET** /{format}/HistoricalMemberships | Memberships (Historical)
*LoLV3Scores.DefaultApi* | [**player**](docs/DefaultApi.md#player) | **GET** /{format}/Player/{playerid} | Player
*LoLV3Scores.DefaultApi* | [**players**](docs/DefaultApi.md#players) | **GET** /{format}/Players | Players
*LoLV3Scores.DefaultApi* | [**playersByTeam**](docs/DefaultApi.md#playersByTeam) | **GET** /{format}/PlayersByTeam/{teamid} | Players by Team
*LoLV3Scores.DefaultApi* | [**schedule**](docs/DefaultApi.md#schedule) | **GET** /{format}/Schedule/{roundid} | Schedule
*LoLV3Scores.DefaultApi* | [**seasonTeams**](docs/DefaultApi.md#seasonTeams) | **GET** /{format}/SeasonTeams/{seasonid} | Season Teams
*LoLV3Scores.DefaultApi* | [**standings**](docs/DefaultApi.md#standings) | **GET** /{format}/Standings/{roundid} | Standings
*LoLV3Scores.DefaultApi* | [**teams**](docs/DefaultApi.md#teams) | **GET** /{format}/Teams | Teams
*LoLV3Scores.DefaultApi* | [**venues**](docs/DefaultApi.md#venues) | **GET** /{format}/Venues | Venues


## Documentation for Models

 - [LoLV3Scores.Area](docs/Area.md)
 - [LoLV3Scores.Competition](docs/Competition.md)
 - [LoLV3Scores.CompetitionDetail](docs/CompetitionDetail.md)
 - [LoLV3Scores.Game](docs/Game.md)
 - [LoLV3Scores.Membership](docs/Membership.md)
 - [LoLV3Scores.Player](docs/Player.md)
 - [LoLV3Scores.Round](docs/Round.md)
 - [LoLV3Scores.Season](docs/Season.md)
 - [LoLV3Scores.SeasonTeam](docs/SeasonTeam.md)
 - [LoLV3Scores.Standing](docs/Standing.md)
 - [LoLV3Scores.Team](docs/Team.md)
 - [LoLV3Scores.TeamDetail](docs/TeamDetail.md)
 - [LoLV3Scores.Venue](docs/Venue.md)


## Documentation for Authorization


Authentication schemes defined for the API:
### apiKeyHeader


- **Type**: API key
- **API key parameter name**: Ocp-Apim-Subscription-Key
- **Location**: HTTP header

### apiKeyQuery


- **Type**: API key
- **API key parameter name**: key
- **Location**: URL query string

