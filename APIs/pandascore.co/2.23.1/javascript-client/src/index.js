/**
 * PandaScore REST API for All Videogames
 *  # Introduction  Whether you're looking to build an official Pandascore integration for your service, or you just want to build something awesome, [we can help you get started](/home).  The API works over the HTTPS protocol, and is accessed from the `api.pandascore.co` domain.  - The current endpoint is [https://api.pandascore.co](https://api.pandascore.co). - All data is sent and received as JSON by default. - Blank fields are included with `null` values instead of being omitted. - All timestamps are returned in ISO-8601 format  ### About this documentation  Clicking on a query parameter like `filter` or `search` will show you the available options: ![filter](/doc/images/query_param_details.jpg)  You can also click on a response to see the detailed response schema: ![response](/doc/images/response_schema.jpg)  ## Events hierarchy  The PandaScore API allows you to access data about eSports events by using a certain structure detailed below.  **Leagues**  Leagues are the top level events. They don't have a date and represent a regular competition. A League is composed of one or several series.   Some League of Legends leagues are: _EU LCS, NA LCS, LCK, etc._   Some Dota 2 leagues are: _ESL One, GESC, The International, PGL, etc._  **Series**  A Serie represents an occurrence of a league event.   The EU LCS league has two series per year: _spring 2017, summer 2017, spring 2016, summer 2016 etc._   Some Dota2 Series examples would be: _Changsha Major, Open Bucharest, Frankfurt, i-League Invitational etc._  **Tournaments**  Tournaments groups all the matches of a serie under \"stages\" and \"groups\".   The tournaments of the EU LCS of summer 2017 are: _Group A, Group B, Playoffs, etc._   Some Dota 2 tournaments are: _Group A, Group B, Playoffs, etc._  **Matches**  Finally we have matches which have two players or teams (depending on the played videogame) and several games (the rounds of the match).   Matches of the group A in the EU LCS of summer 2017 are: _G2 vs FNC, MSF vs NIP, etc._   Matches of the group A in the ESL One, Genting tournamnet are: _Lower Round 1, Quarterfinal, Upper Final, etc._    **Please note that some matches may be listed as \"TBD vs TBD\" if the matchup is not announced yet, for example the date of the Final match is known but the quarterfinal is still being played.**   ![Structure](/doc/images/structure.png)  ## Formats  &lt;!-- The API currently supports the JSON format by default, as well as the XML format. Add the desired extension to your request URL in order to get that format. --&gt; The API currently supports the JSON format by default.  Other formats may be added depending on user needs.  ## Pagination  The Pandascore API paginates all resources on the index method.  Requests that return multiple items will be paginated to 50 items by default. You can specify further pages with the `page[number]` parameter. You can also set a custom page size (up to 100) with the `page[size]` parameter.  The `Link` HTTP response header contains pagination data with `first`, `previous`, `next` and `last` raw page links when available, under the format  ``` Link: &lt;https://api.pandascore.co/{Resource}?page=X+1&gt;; rel=\"next\", &lt;https://api.pandascore.co/{Resource}?page=X-1&gt;; rel=\"prev\", &lt;https://api.pandascore.co/{Resource}?page=1&gt;; rel=\"first\", &lt;https://api.pandascore.co/{Resource}?page=X+n&gt;; rel=\"last\" ```  There is also:  * A `X-Page` header field, which contains the current page. * A `X-Per-Page` header field, which contains the current pagination length. * A `X-Total` header field, which contains the total count of items across all pages.  ## Filtering  The `filter` query parameter can be used to filter a collection by one or several fields for one or several values. The `filter` parameter takes the field to filter as a key, and the values to filter as the value. Multiples values must be comma-separated (`,`).  For example, the following is a request for all the champions with a name matching Twitch or Brand exactly, but only with 21 armor:  ``` GET /lol/champions?filter[name]=Brand,Twitch&amp;filter[armor]=21&amp;token=YOUR_ACCESS_TOKEN ```  ## Range  The `range` parameter is a hash that allows filtering fields by an interval. Only values between the given two comma-separated bounds will be returned. The bounds are inclusive.  For example, the following is a request for all the champions with `hp` within 500 and 1000:  ``` GET /lol/champions?range[hp]=500,1000&amp;token=YOUR_ACCESS_TOKEN ```  ## Search  The `search` parameter is a bit like the `filter` parameter, but it will return all results where the values **contain** the given parameter.  Note: this only works on strings. Searching with integer values is not supported and `filter` or `range` parameters may be better suited for your needs here.  For example, to get all the champions with a name containing `\"twi\"`:  ``` $ curl -sg -H 'Authorization: Bearer YOUR_ACCESS_TOKEN' 'https://api.pandascore.co/lol/champions?search[name]=twi' | jq -S '.[].name' \"Twitch\" \"Twisted Fate\" ```  ## Sorting  All index endpoints support multiple sort fields with comma-separation (`,`); the fields are applied in the order specified.  The sort order for each field is ascending unless it is prefixed with a minus (U+002D HYPHEN-MINUS, “-“), in which case it is descending.  For example, `GET /lol/champions?sort=attackdamage,-name&amp;token=YOUR_ACCESS_TOKEN` will return all the champions sorted by attack damage. Any champions with the same attack damage will then be sorted by their names in descending alphabetical order.  ## Rate limiting  Depending on your current plan, you will have a different rate limit. Your plan and your current request count [are available on your dashboard](https://pandascore.co/settings).  With the **free plan**, you have a limit of 1000 requests per hour, others plans have a limit of 4000 requests per hour. The number of remaining requests is available in the `X-Rate-Limit-Remaining` response header.  Your API key is included in all the examples on this page, so you can test any example right away. **Only you can see this value.**  # Authentication  The authentication on the Pandascore API works with access tokens.  All developers need to [create an account](https://pandascore.co/users/sign_in) before getting started, in order to get an access token. The access token should not be shared.  **Your token can be found and regenerated from [your dashboard](https://pandascore.co/settings).**  The access token can be passed in the URL with the `token` query string parameter, or in the `Authorization: Bearer` header field.  &lt;!-- ReDoc-Inject: &lt;security-definitions&gt; --&gt; 
 *
 * The version of the OpenAPI document: 2.23.1
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from './ApiClient';
import BaseLeague from './model/BaseLeague';
import BaseMatch from './model/BaseMatch';
import BaseOpponent from './model/BaseOpponent';
import BaseOpponent1 from './model/BaseOpponent1';
import BasePlayer from './model/BasePlayer';
import BaseSerie from './model/BaseSerie';
import BaseTeam from './model/BaseTeam';
import BaseTeam1 from './model/BaseTeam1';
import BaseTournament from './model/BaseTournament';
import BettingBaseTournament from './model/BettingBaseTournament';
import BettingCSGOGame from './model/BettingCSGOGame';
import BettingCSGOGameRoundTeam from './model/BettingCSGOGameRoundTeam';
import BettingDota2Game from './model/BettingDota2Game';
import BettingGame from './model/BettingGame';
import BettingGameRoundTeams from './model/BettingGameRoundTeams';
import BettingGameRoundTeams1 from './model/BettingGameRoundTeams1';
import BettingGameTeams from './model/BettingGameTeams';
import BettingGameTeams1 from './model/BettingGameTeams1';
import BettingGroup from './model/BettingGroup';
import BettingGroup1 from './model/BettingGroup1';
import BettingLeague from './model/BettingLeague';
import BettingLeague1 from './model/BettingLeague1';
import BettingLeagueVideogame from './model/BettingLeagueVideogame';
import BettingLoLGame from './model/BettingLoLGame';
import BettingLoLGameTeam from './model/BettingLoLGameTeam';
import BettingMatch from './model/BettingMatch';
import BettingMatchStatus from './model/BettingMatchStatus';
import BettingMetadata from './model/BettingMetadata';
import BettingOwGame from './model/BettingOwGame';
import BettingPUBGGame from './model/BettingPUBGGame';
import BettingSerie from './model/BettingSerie';
import BettingSerie1 from './model/BettingSerie1';
import BettingTournament from './model/BettingTournament';
import Blueprint from './model/Blueprint';
import Blueprint1 from './model/Blueprint1';
import Bracket from './model/Bracket';
import BracketStanding from './model/BracketStanding';
import CSGOMap from './model/CSGOMap';
import CSGOMap1 from './model/CSGOMap1';
import CSGOOutcome from './model/CSGOOutcome';
import CSGOWeaponIDOrSlug from './model/CSGOWeaponIDOrSlug';
import CurrentVideogame from './model/CurrentVideogame';
import DeletionIncident from './model/DeletionIncident';
import DeletionIncidentChangeType from './model/DeletionIncidentChangeType';
import DeletionObject from './model/DeletionObject';
import Dota2AbilityIDOrSlug from './model/Dota2AbilityIDOrSlug';
import Dota2HeroIDOrSlug from './model/Dota2HeroIDOrSlug';
import Dota2ItemIDOrSlug from './model/Dota2ItemIDOrSlug';
import Esport from './model/Esport';
import EsportCSGO from './model/EsportCSGO';
import EsportCodmw from './model/EsportCodmw';
import EsportDota2 from './model/EsportDota2';
import EsportFifa from './model/EsportFifa';
import EsportFortnite from './model/EsportFortnite';
import EsportLoL from './model/EsportLoL';
import EsportOverwatch from './model/EsportOverwatch';
import EsportPUBG from './model/EsportPUBG';
import EsportR6siege from './model/EsportR6siege';
import EsportRocketLeague from './model/EsportRocketLeague';
import EsportValorant from './model/EsportValorant';
import FilterOverBrackets from './model/FilterOverBrackets';
import FilterOverLeagues from './model/FilterOverLeagues';
import FilterOverMatches from './model/FilterOverMatches';
import FilterOverPlayers from './model/FilterOverPlayers';
import FilterOverSeries from './model/FilterOverSeries';
import FilterOverShortTournaments from './model/FilterOverShortTournaments';
import FilterOverShortVideogameVersions from './model/FilterOverShortVideogameVersions';
import FilterOverTeams from './model/FilterOverTeams';
import Game from './model/Game';
import GameID from './model/GameID';
import GameStatus from './model/GameStatus';
import GameWinner from './model/GameWinner';
import GetAdditions400Response from './model/GetAdditions400Response';
import GetAdditionsPageParameter from './model/GetAdditionsPageParameter';
import GetAdditionsPageParameterOneOf from './model/GetAdditionsPageParameterOneOf';
import GroupStanding from './model/GroupStanding';
import Incident from './model/Incident';
import IncidentChangeType from './model/IncidentChangeType';
import IncidentDeletionReason from './model/IncidentDeletionReason';
import IncidentDeletionReasonDeleted from './model/IncidentDeletionReasonDeleted';
import IncidentID from './model/IncidentID';
import IncidentOfTypeLeague from './model/IncidentOfTypeLeague';
import IncidentOfTypeMatch from './model/IncidentOfTypeMatch';
import IncidentOfTypePlayer from './model/IncidentOfTypePlayer';
import IncidentOfTypeSerie from './model/IncidentOfTypeSerie';
import IncidentOfTypeTeam from './model/IncidentOfTypeTeam';
import IncidentOfTypeTournament from './model/IncidentOfTypeTournament';
import IncidentType from './model/IncidentType';
import League from './model/League';
import LeagueIDOrSlug from './model/LeagueIDOrSlug';
import LeagueVideogame from './model/LeagueVideogame';
import LeagueVideogameCSGO from './model/LeagueVideogameCSGO';
import LeagueVideogameCodmw from './model/LeagueVideogameCodmw';
import LeagueVideogameDota2 from './model/LeagueVideogameDota2';
import LeagueVideogameFifa from './model/LeagueVideogameFifa';
import LeagueVideogameFortnite from './model/LeagueVideogameFortnite';
import LeagueVideogameLoL from './model/LeagueVideogameLoL';
import LeagueVideogameOverwatch from './model/LeagueVideogameOverwatch';
import LeagueVideogamePUBG from './model/LeagueVideogamePUBG';
import LeagueVideogameR6siege from './model/LeagueVideogameR6siege';
import LeagueVideogameRocketLeague from './model/LeagueVideogameRocketLeague';
import LeagueVideogameValorant from './model/LeagueVideogameValorant';
import Live from './model/Live';
import LiveEndpoint from './model/LiveEndpoint';
import LiveEvent from './model/LiveEvent';
import LiveEvent1 from './model/LiveEvent1';
import LiveType from './model/LiveType';
import LoLTeamColor from './model/LoLTeamColor';
import Market from './model/Market';
import MarketSelection from './model/MarketSelection';
import MarketStatus from './model/MarketStatus';
import Match from './model/Match';
import MatchIDOrSlug from './model/MatchIDOrSlug';
import MatchLive from './model/MatchLive';
import MatchLocalizedStream from './model/MatchLocalizedStream';
import MatchLocalizedStreams from './model/MatchLocalizedStreams';
import MatchMarketGame from './model/MatchMarketGame';
import MatchMarkets from './model/MatchMarkets';
import MatchOpponentBasePlayer from './model/MatchOpponentBasePlayer';
import MatchOpponentsObject from './model/MatchOpponentsObject';
import MatchPlayerOpponentsObject from './model/MatchPlayerOpponentsObject';
import MatchPlayerResult from './model/MatchPlayerResult';
import MatchResult from './model/MatchResult';
import MatchStatus from './model/MatchStatus';
import MatchTeamOpponentsObject from './model/MatchTeamOpponentsObject';
import MatchTeamResult from './model/MatchTeamResult';
import MatchType from './model/MatchType';
import NonDeletionIncident from './model/NonDeletionIncident';
import Opponent from './model/Opponent';
import OpponentID from './model/OpponentID';
import OpponentID1 from './model/OpponentID1';
import OpponentType from './model/OpponentType';
import OpponentTypePlayer from './model/OpponentTypePlayer';
import OpponentTypeTeam from './model/OpponentTypeTeam';
import OwHeroIDOrSlug from './model/OwHeroIDOrSlug';
import OwMapIDOrSlug from './model/OwMapIDOrSlug';
import Player from './model/Player';
import PlayerIDOrSlug from './model/PlayerIDOrSlug';
import PreviousMatch from './model/PreviousMatch';
import PreviousMatchType from './model/PreviousMatchType';
import RangeOverBrackets from './model/RangeOverBrackets';
import RangeOverLeagues from './model/RangeOverLeagues';
import RangeOverMatches from './model/RangeOverMatches';
import RangeOverPlayers from './model/RangeOverPlayers';
import RangeOverSeries from './model/RangeOverSeries';
import RangeOverShortTournaments from './model/RangeOverShortTournaments';
import RangeOverShortVideogameVersions from './model/RangeOverShortVideogameVersions';
import RangeOverTeams from './model/RangeOverTeams';
import SearchOverBrackets from './model/SearchOverBrackets';
import SearchOverLeagues from './model/SearchOverLeagues';
import SearchOverMatches from './model/SearchOverMatches';
import SearchOverPlayers from './model/SearchOverPlayers';
import SearchOverSeries from './model/SearchOverSeries';
import SearchOverShortTournaments from './model/SearchOverShortTournaments';
import SearchOverShortVideogameVersions from './model/SearchOverShortVideogameVersions';
import SearchOverTeams from './model/SearchOverTeams';
import SelectionResult from './model/SelectionResult';
import Serie from './model/Serie';
import SerieIDOrSlug from './model/SerieIDOrSlug';
import ShortTournament from './model/ShortTournament';
import ShortVideogameVersion from './model/ShortVideogameVersion';
import ShortVideogameVersion1 from './model/ShortVideogameVersion1';
import Standing from './model/Standing';
import Stream from './model/Stream';
import StreamLanguage from './model/StreamLanguage';
import Team from './model/Team';
import TeamIDOrSlug from './model/TeamIDOrSlug';
import Tournament from './model/Tournament';
import TournamentIDOrSlug from './model/TournamentIDOrSlug';
import TournamentPlayerRosters from './model/TournamentPlayerRosters';
import TournamentRosterItem from './model/TournamentRosterItem';
import TournamentRosters from './model/TournamentRosters';
import TournamentTeamRosters from './model/TournamentTeamRosters';
import Videogame from './model/Videogame';
import VideogameCSGO from './model/VideogameCSGO';
import VideogameCodmw from './model/VideogameCodmw';
import VideogameDota2 from './model/VideogameDota2';
import VideogameFifa from './model/VideogameFifa';
import VideogameID from './model/VideogameID';
import VideogameIDOrSlug from './model/VideogameIDOrSlug';
import VideogameLeague from './model/VideogameLeague';
import VideogameLoL from './model/VideogameLoL';
import VideogameOverwatch from './model/VideogameOverwatch';
import VideogamePUBG from './model/VideogamePUBG';
import VideogameR6siege from './model/VideogameR6siege';
import VideogameRocketLeague from './model/VideogameRocketLeague';
import VideogameSlug from './model/VideogameSlug';
import VideogameTitle from './model/VideogameTitle';
import VideogameTitle1 from './model/VideogameTitle1';
import VideogameValorant from './model/VideogameValorant';
import IncidentsApi from './api/IncidentsApi';
import LeaguesApi from './api/LeaguesApi';
import LivesApi from './api/LivesApi';
import MatchesApi from './api/MatchesApi';
import PlayersApi from './api/PlayersApi';
import SeriesApi from './api/SeriesApi';
import TeamsApi from './api/TeamsApi';
import TournamentsApi from './api/TournamentsApi';
import VideogamesApi from './api/VideogamesApi';


/**
*  # Introduction  Whether you&#39;re looking to build an official Pandascore integration for your service, or you just want to build something awesome, [we can help you get started](/home).  The API works over the HTTPS protocol, and is accessed from the &#x60;api.pandascore.co&#x60; domain.  - The current endpoint is [https://api.pandascore.co](https://api.pandascore.co). - All data is sent and received as JSON by default. - Blank fields are included with &#x60;null&#x60; values instead of being omitted. - All timestamps are returned in ISO-8601 format  ### About this documentation  Clicking on a query parameter like &#x60;filter&#x60; or &#x60;search&#x60; will show you the available options: ![filter](/doc/images/query_param_details.jpg)  You can also click on a response to see the detailed response schema: ![response](/doc/images/response_schema.jpg)  ## Events hierarchy  The PandaScore API allows you to access data about eSports events by using a certain structure detailed below.  **Leagues**  Leagues are the top level events. They don&#39;t have a date and represent a regular competition. A League is composed of one or several series.   Some League of Legends leagues are: _EU LCS, NA LCS, LCK, etc._   Some Dota 2 leagues are: _ESL One, GESC, The International, PGL, etc._  **Series**  A Serie represents an occurrence of a league event.   The EU LCS league has two series per year: _spring 2017, summer 2017, spring 2016, summer 2016 etc._   Some Dota2 Series examples would be: _Changsha Major, Open Bucharest, Frankfurt, i-League Invitational etc._  **Tournaments**  Tournaments groups all the matches of a serie under \&quot;stages\&quot; and \&quot;groups\&quot;.   The tournaments of the EU LCS of summer 2017 are: _Group A, Group B, Playoffs, etc._   Some Dota 2 tournaments are: _Group A, Group B, Playoffs, etc._  **Matches**  Finally we have matches which have two players or teams (depending on the played videogame) and several games (the rounds of the match).   Matches of the group A in the EU LCS of summer 2017 are: _G2 vs FNC, MSF vs NIP, etc._   Matches of the group A in the ESL One, Genting tournamnet are: _Lower Round 1, Quarterfinal, Upper Final, etc._    **Please note that some matches may be listed as \&quot;TBD vs TBD\&quot; if the matchup is not announced yet, for example the date of the Final match is known but the quarterfinal is still being played.**   ![Structure](/doc/images/structure.png)  ## Formats  &amp;lt;!-- The API currently supports the JSON format by default, as well as the XML format. Add the desired extension to your request URL in order to get that format. --&amp;gt; The API currently supports the JSON format by default.  Other formats may be added depending on user needs.  ## Pagination  The Pandascore API paginates all resources on the index method.  Requests that return multiple items will be paginated to 50 items by default. You can specify further pages with the &#x60;page[number]&#x60; parameter. You can also set a custom page size (up to 100) with the &#x60;page[size]&#x60; parameter.  The &#x60;Link&#x60; HTTP response header contains pagination data with &#x60;first&#x60;, &#x60;previous&#x60;, &#x60;next&#x60; and &#x60;last&#x60; raw page links when available, under the format  &#x60;&#x60;&#x60; Link: &amp;lt;https://api.pandascore.co/{Resource}?page&#x3D;X+1&amp;gt;; rel&#x3D;\&quot;next\&quot;, &amp;lt;https://api.pandascore.co/{Resource}?page&#x3D;X-1&amp;gt;; rel&#x3D;\&quot;prev\&quot;, &amp;lt;https://api.pandascore.co/{Resource}?page&#x3D;1&amp;gt;; rel&#x3D;\&quot;first\&quot;, &amp;lt;https://api.pandascore.co/{Resource}?page&#x3D;X+n&amp;gt;; rel&#x3D;\&quot;last\&quot; &#x60;&#x60;&#x60;  There is also:  * A &#x60;X-Page&#x60; header field, which contains the current page. * A &#x60;X-Per-Page&#x60; header field, which contains the current pagination length. * A &#x60;X-Total&#x60; header field, which contains the total count of items across all pages.  ## Filtering  The &#x60;filter&#x60; query parameter can be used to filter a collection by one or several fields for one or several values. The &#x60;filter&#x60; parameter takes the field to filter as a key, and the values to filter as the value. Multiples values must be comma-separated (&#x60;,&#x60;).  For example, the following is a request for all the champions with a name matching Twitch or Brand exactly, but only with 21 armor:  &#x60;&#x60;&#x60; GET /lol/champions?filter[name]&#x3D;Brand,Twitch&amp;amp;filter[armor]&#x3D;21&amp;amp;token&#x3D;YOUR_ACCESS_TOKEN &#x60;&#x60;&#x60;  ## Range  The &#x60;range&#x60; parameter is a hash that allows filtering fields by an interval. Only values between the given two comma-separated bounds will be returned. The bounds are inclusive.  For example, the following is a request for all the champions with &#x60;hp&#x60; within 500 and 1000:  &#x60;&#x60;&#x60; GET /lol/champions?range[hp]&#x3D;500,1000&amp;amp;token&#x3D;YOUR_ACCESS_TOKEN &#x60;&#x60;&#x60;  ## Search  The &#x60;search&#x60; parameter is a bit like the &#x60;filter&#x60; parameter, but it will return all results where the values **contain** the given parameter.  Note: this only works on strings. Searching with integer values is not supported and &#x60;filter&#x60; or &#x60;range&#x60; parameters may be better suited for your needs here.  For example, to get all the champions with a name containing &#x60;\&quot;twi\&quot;&#x60;:  &#x60;&#x60;&#x60; $ curl -sg -H &#39;Authorization: Bearer YOUR_ACCESS_TOKEN&#39; &#39;https://api.pandascore.co/lol/champions?search[name]&#x3D;twi&#39; | jq -S &#39;.[].name&#39; \&quot;Twitch\&quot; \&quot;Twisted Fate\&quot; &#x60;&#x60;&#x60;  ## Sorting  All index endpoints support multiple sort fields with comma-separation (&#x60;,&#x60;); the fields are applied in the order specified.  The sort order for each field is ascending unless it is prefixed with a minus (U+002D HYPHEN-MINUS, “-“), in which case it is descending.  For example, &#x60;GET /lol/champions?sort&#x3D;attackdamage,-name&amp;amp;token&#x3D;YOUR_ACCESS_TOKEN&#x60; will return all the champions sorted by attack damage. Any champions with the same attack damage will then be sorted by their names in descending alphabetical order.  ## Rate limiting  Depending on your current plan, you will have a different rate limit. Your plan and your current request count [are available on your dashboard](https://pandascore.co/settings).  With the **free plan**, you have a limit of 1000 requests per hour, others plans have a limit of 4000 requests per hour. The number of remaining requests is available in the &#x60;X-Rate-Limit-Remaining&#x60; response header.  Your API key is included in all the examples on this page, so you can test any example right away. **Only you can see this value.**  # Authentication  The authentication on the Pandascore API works with access tokens.  All developers need to [create an account](https://pandascore.co/users/sign_in) before getting started, in order to get an access token. The access token should not be shared.  **Your token can be found and regenerated from [your dashboard](https://pandascore.co/settings).**  The access token can be passed in the URL with the &#x60;token&#x60; query string parameter, or in the &#x60;Authorization: Bearer&#x60; header field.  &amp;lt;!-- ReDoc-Inject: &amp;lt;security-definitions&amp;gt; --&amp;gt; .<br>
* The <code>index</code> module provides access to constructors for all the classes which comprise the public API.
* <p>
* An AMD (recommended!) or CommonJS application will generally do something equivalent to the following:
* <pre>
* var PandaScoreRestApiForAllVideogames = require('index'); // See note below*.
* var xxxSvc = new PandaScoreRestApiForAllVideogames.XxxApi(); // Allocate the API class we're going to use.
* var yyyModel = new PandaScoreRestApiForAllVideogames.Yyy(); // Construct a model instance.
* yyyModel.someProperty = 'someValue';
* ...
* var zzz = xxxSvc.doSomething(yyyModel); // Invoke the service.
* ...
* </pre>
* <em>*NOTE: For a top-level AMD script, use require(['index'], function(){...})
* and put the application logic within the callback function.</em>
* </p>
* <p>
* A non-AMD browser application (discouraged) might do something like this:
* <pre>
* var xxxSvc = new PandaScoreRestApiForAllVideogames.XxxApi(); // Allocate the API class we're going to use.
* var yyy = new PandaScoreRestApiForAllVideogames.Yyy(); // Construct a model instance.
* yyyModel.someProperty = 'someValue';
* ...
* var zzz = xxxSvc.doSomething(yyyModel); // Invoke the service.
* ...
* </pre>
* </p>
* @module index
* @version 2.23.1
*/
export {
    /**
     * The ApiClient constructor.
     * @property {module:ApiClient}
     */
    ApiClient,

    /**
     * The BaseLeague model constructor.
     * @property {module:model/BaseLeague}
     */
    BaseLeague,

    /**
     * The BaseMatch model constructor.
     * @property {module:model/BaseMatch}
     */
    BaseMatch,

    /**
     * The BaseOpponent model constructor.
     * @property {module:model/BaseOpponent}
     */
    BaseOpponent,

    /**
     * The BaseOpponent1 model constructor.
     * @property {module:model/BaseOpponent1}
     */
    BaseOpponent1,

    /**
     * The BasePlayer model constructor.
     * @property {module:model/BasePlayer}
     */
    BasePlayer,

    /**
     * The BaseSerie model constructor.
     * @property {module:model/BaseSerie}
     */
    BaseSerie,

    /**
     * The BaseTeam model constructor.
     * @property {module:model/BaseTeam}
     */
    BaseTeam,

    /**
     * The BaseTeam1 model constructor.
     * @property {module:model/BaseTeam1}
     */
    BaseTeam1,

    /**
     * The BaseTournament model constructor.
     * @property {module:model/BaseTournament}
     */
    BaseTournament,

    /**
     * The BettingBaseTournament model constructor.
     * @property {module:model/BettingBaseTournament}
     */
    BettingBaseTournament,

    /**
     * The BettingCSGOGame model constructor.
     * @property {module:model/BettingCSGOGame}
     */
    BettingCSGOGame,

    /**
     * The BettingCSGOGameRoundTeam model constructor.
     * @property {module:model/BettingCSGOGameRoundTeam}
     */
    BettingCSGOGameRoundTeam,

    /**
     * The BettingDota2Game model constructor.
     * @property {module:model/BettingDota2Game}
     */
    BettingDota2Game,

    /**
     * The BettingGame model constructor.
     * @property {module:model/BettingGame}
     */
    BettingGame,

    /**
     * The BettingGameRoundTeams model constructor.
     * @property {module:model/BettingGameRoundTeams}
     */
    BettingGameRoundTeams,

    /**
     * The BettingGameRoundTeams1 model constructor.
     * @property {module:model/BettingGameRoundTeams1}
     */
    BettingGameRoundTeams1,

    /**
     * The BettingGameTeams model constructor.
     * @property {module:model/BettingGameTeams}
     */
    BettingGameTeams,

    /**
     * The BettingGameTeams1 model constructor.
     * @property {module:model/BettingGameTeams1}
     */
    BettingGameTeams1,

    /**
     * The BettingGroup model constructor.
     * @property {module:model/BettingGroup}
     */
    BettingGroup,

    /**
     * The BettingGroup1 model constructor.
     * @property {module:model/BettingGroup1}
     */
    BettingGroup1,

    /**
     * The BettingLeague model constructor.
     * @property {module:model/BettingLeague}
     */
    BettingLeague,

    /**
     * The BettingLeague1 model constructor.
     * @property {module:model/BettingLeague1}
     */
    BettingLeague1,

    /**
     * The BettingLeagueVideogame model constructor.
     * @property {module:model/BettingLeagueVideogame}
     */
    BettingLeagueVideogame,

    /**
     * The BettingLoLGame model constructor.
     * @property {module:model/BettingLoLGame}
     */
    BettingLoLGame,

    /**
     * The BettingLoLGameTeam model constructor.
     * @property {module:model/BettingLoLGameTeam}
     */
    BettingLoLGameTeam,

    /**
     * The BettingMatch model constructor.
     * @property {module:model/BettingMatch}
     */
    BettingMatch,

    /**
     * The BettingMatchStatus model constructor.
     * @property {module:model/BettingMatchStatus}
     */
    BettingMatchStatus,

    /**
     * The BettingMetadata model constructor.
     * @property {module:model/BettingMetadata}
     */
    BettingMetadata,

    /**
     * The BettingOwGame model constructor.
     * @property {module:model/BettingOwGame}
     */
    BettingOwGame,

    /**
     * The BettingPUBGGame model constructor.
     * @property {module:model/BettingPUBGGame}
     */
    BettingPUBGGame,

    /**
     * The BettingSerie model constructor.
     * @property {module:model/BettingSerie}
     */
    BettingSerie,

    /**
     * The BettingSerie1 model constructor.
     * @property {module:model/BettingSerie1}
     */
    BettingSerie1,

    /**
     * The BettingTournament model constructor.
     * @property {module:model/BettingTournament}
     */
    BettingTournament,

    /**
     * The Blueprint model constructor.
     * @property {module:model/Blueprint}
     */
    Blueprint,

    /**
     * The Blueprint1 model constructor.
     * @property {module:model/Blueprint1}
     */
    Blueprint1,

    /**
     * The Bracket model constructor.
     * @property {module:model/Bracket}
     */
    Bracket,

    /**
     * The BracketStanding model constructor.
     * @property {module:model/BracketStanding}
     */
    BracketStanding,

    /**
     * The CSGOMap model constructor.
     * @property {module:model/CSGOMap}
     */
    CSGOMap,

    /**
     * The CSGOMap1 model constructor.
     * @property {module:model/CSGOMap1}
     */
    CSGOMap1,

    /**
     * The CSGOOutcome model constructor.
     * @property {module:model/CSGOOutcome}
     */
    CSGOOutcome,

    /**
     * The CSGOWeaponIDOrSlug model constructor.
     * @property {module:model/CSGOWeaponIDOrSlug}
     */
    CSGOWeaponIDOrSlug,

    /**
     * The CurrentVideogame model constructor.
     * @property {module:model/CurrentVideogame}
     */
    CurrentVideogame,

    /**
     * The DeletionIncident model constructor.
     * @property {module:model/DeletionIncident}
     */
    DeletionIncident,

    /**
     * The DeletionIncidentChangeType model constructor.
     * @property {module:model/DeletionIncidentChangeType}
     */
    DeletionIncidentChangeType,

    /**
     * The DeletionObject model constructor.
     * @property {module:model/DeletionObject}
     */
    DeletionObject,

    /**
     * The Dota2AbilityIDOrSlug model constructor.
     * @property {module:model/Dota2AbilityIDOrSlug}
     */
    Dota2AbilityIDOrSlug,

    /**
     * The Dota2HeroIDOrSlug model constructor.
     * @property {module:model/Dota2HeroIDOrSlug}
     */
    Dota2HeroIDOrSlug,

    /**
     * The Dota2ItemIDOrSlug model constructor.
     * @property {module:model/Dota2ItemIDOrSlug}
     */
    Dota2ItemIDOrSlug,

    /**
     * The Esport model constructor.
     * @property {module:model/Esport}
     */
    Esport,

    /**
     * The EsportCSGO model constructor.
     * @property {module:model/EsportCSGO}
     */
    EsportCSGO,

    /**
     * The EsportCodmw model constructor.
     * @property {module:model/EsportCodmw}
     */
    EsportCodmw,

    /**
     * The EsportDota2 model constructor.
     * @property {module:model/EsportDota2}
     */
    EsportDota2,

    /**
     * The EsportFifa model constructor.
     * @property {module:model/EsportFifa}
     */
    EsportFifa,

    /**
     * The EsportFortnite model constructor.
     * @property {module:model/EsportFortnite}
     */
    EsportFortnite,

    /**
     * The EsportLoL model constructor.
     * @property {module:model/EsportLoL}
     */
    EsportLoL,

    /**
     * The EsportOverwatch model constructor.
     * @property {module:model/EsportOverwatch}
     */
    EsportOverwatch,

    /**
     * The EsportPUBG model constructor.
     * @property {module:model/EsportPUBG}
     */
    EsportPUBG,

    /**
     * The EsportR6siege model constructor.
     * @property {module:model/EsportR6siege}
     */
    EsportR6siege,

    /**
     * The EsportRocketLeague model constructor.
     * @property {module:model/EsportRocketLeague}
     */
    EsportRocketLeague,

    /**
     * The EsportValorant model constructor.
     * @property {module:model/EsportValorant}
     */
    EsportValorant,

    /**
     * The FilterOverBrackets model constructor.
     * @property {module:model/FilterOverBrackets}
     */
    FilterOverBrackets,

    /**
     * The FilterOverLeagues model constructor.
     * @property {module:model/FilterOverLeagues}
     */
    FilterOverLeagues,

    /**
     * The FilterOverMatches model constructor.
     * @property {module:model/FilterOverMatches}
     */
    FilterOverMatches,

    /**
     * The FilterOverPlayers model constructor.
     * @property {module:model/FilterOverPlayers}
     */
    FilterOverPlayers,

    /**
     * The FilterOverSeries model constructor.
     * @property {module:model/FilterOverSeries}
     */
    FilterOverSeries,

    /**
     * The FilterOverShortTournaments model constructor.
     * @property {module:model/FilterOverShortTournaments}
     */
    FilterOverShortTournaments,

    /**
     * The FilterOverShortVideogameVersions model constructor.
     * @property {module:model/FilterOverShortVideogameVersions}
     */
    FilterOverShortVideogameVersions,

    /**
     * The FilterOverTeams model constructor.
     * @property {module:model/FilterOverTeams}
     */
    FilterOverTeams,

    /**
     * The Game model constructor.
     * @property {module:model/Game}
     */
    Game,

    /**
     * The GameID model constructor.
     * @property {module:model/GameID}
     */
    GameID,

    /**
     * The GameStatus model constructor.
     * @property {module:model/GameStatus}
     */
    GameStatus,

    /**
     * The GameWinner model constructor.
     * @property {module:model/GameWinner}
     */
    GameWinner,

    /**
     * The GetAdditions400Response model constructor.
     * @property {module:model/GetAdditions400Response}
     */
    GetAdditions400Response,

    /**
     * The GetAdditionsPageParameter model constructor.
     * @property {module:model/GetAdditionsPageParameter}
     */
    GetAdditionsPageParameter,

    /**
     * The GetAdditionsPageParameterOneOf model constructor.
     * @property {module:model/GetAdditionsPageParameterOneOf}
     */
    GetAdditionsPageParameterOneOf,

    /**
     * The GroupStanding model constructor.
     * @property {module:model/GroupStanding}
     */
    GroupStanding,

    /**
     * The Incident model constructor.
     * @property {module:model/Incident}
     */
    Incident,

    /**
     * The IncidentChangeType model constructor.
     * @property {module:model/IncidentChangeType}
     */
    IncidentChangeType,

    /**
     * The IncidentDeletionReason model constructor.
     * @property {module:model/IncidentDeletionReason}
     */
    IncidentDeletionReason,

    /**
     * The IncidentDeletionReasonDeleted model constructor.
     * @property {module:model/IncidentDeletionReasonDeleted}
     */
    IncidentDeletionReasonDeleted,

    /**
     * The IncidentID model constructor.
     * @property {module:model/IncidentID}
     */
    IncidentID,

    /**
     * The IncidentOfTypeLeague model constructor.
     * @property {module:model/IncidentOfTypeLeague}
     */
    IncidentOfTypeLeague,

    /**
     * The IncidentOfTypeMatch model constructor.
     * @property {module:model/IncidentOfTypeMatch}
     */
    IncidentOfTypeMatch,

    /**
     * The IncidentOfTypePlayer model constructor.
     * @property {module:model/IncidentOfTypePlayer}
     */
    IncidentOfTypePlayer,

    /**
     * The IncidentOfTypeSerie model constructor.
     * @property {module:model/IncidentOfTypeSerie}
     */
    IncidentOfTypeSerie,

    /**
     * The IncidentOfTypeTeam model constructor.
     * @property {module:model/IncidentOfTypeTeam}
     */
    IncidentOfTypeTeam,

    /**
     * The IncidentOfTypeTournament model constructor.
     * @property {module:model/IncidentOfTypeTournament}
     */
    IncidentOfTypeTournament,

    /**
     * The IncidentType model constructor.
     * @property {module:model/IncidentType}
     */
    IncidentType,

    /**
     * The League model constructor.
     * @property {module:model/League}
     */
    League,

    /**
     * The LeagueIDOrSlug model constructor.
     * @property {module:model/LeagueIDOrSlug}
     */
    LeagueIDOrSlug,

    /**
     * The LeagueVideogame model constructor.
     * @property {module:model/LeagueVideogame}
     */
    LeagueVideogame,

    /**
     * The LeagueVideogameCSGO model constructor.
     * @property {module:model/LeagueVideogameCSGO}
     */
    LeagueVideogameCSGO,

    /**
     * The LeagueVideogameCodmw model constructor.
     * @property {module:model/LeagueVideogameCodmw}
     */
    LeagueVideogameCodmw,

    /**
     * The LeagueVideogameDota2 model constructor.
     * @property {module:model/LeagueVideogameDota2}
     */
    LeagueVideogameDota2,

    /**
     * The LeagueVideogameFifa model constructor.
     * @property {module:model/LeagueVideogameFifa}
     */
    LeagueVideogameFifa,

    /**
     * The LeagueVideogameFortnite model constructor.
     * @property {module:model/LeagueVideogameFortnite}
     */
    LeagueVideogameFortnite,

    /**
     * The LeagueVideogameLoL model constructor.
     * @property {module:model/LeagueVideogameLoL}
     */
    LeagueVideogameLoL,

    /**
     * The LeagueVideogameOverwatch model constructor.
     * @property {module:model/LeagueVideogameOverwatch}
     */
    LeagueVideogameOverwatch,

    /**
     * The LeagueVideogamePUBG model constructor.
     * @property {module:model/LeagueVideogamePUBG}
     */
    LeagueVideogamePUBG,

    /**
     * The LeagueVideogameR6siege model constructor.
     * @property {module:model/LeagueVideogameR6siege}
     */
    LeagueVideogameR6siege,

    /**
     * The LeagueVideogameRocketLeague model constructor.
     * @property {module:model/LeagueVideogameRocketLeague}
     */
    LeagueVideogameRocketLeague,

    /**
     * The LeagueVideogameValorant model constructor.
     * @property {module:model/LeagueVideogameValorant}
     */
    LeagueVideogameValorant,

    /**
     * The Live model constructor.
     * @property {module:model/Live}
     */
    Live,

    /**
     * The LiveEndpoint model constructor.
     * @property {module:model/LiveEndpoint}
     */
    LiveEndpoint,

    /**
     * The LiveEvent model constructor.
     * @property {module:model/LiveEvent}
     */
    LiveEvent,

    /**
     * The LiveEvent1 model constructor.
     * @property {module:model/LiveEvent1}
     */
    LiveEvent1,

    /**
     * The LiveType model constructor.
     * @property {module:model/LiveType}
     */
    LiveType,

    /**
     * The LoLTeamColor model constructor.
     * @property {module:model/LoLTeamColor}
     */
    LoLTeamColor,

    /**
     * The Market model constructor.
     * @property {module:model/Market}
     */
    Market,

    /**
     * The MarketSelection model constructor.
     * @property {module:model/MarketSelection}
     */
    MarketSelection,

    /**
     * The MarketStatus model constructor.
     * @property {module:model/MarketStatus}
     */
    MarketStatus,

    /**
     * The Match model constructor.
     * @property {module:model/Match}
     */
    Match,

    /**
     * The MatchIDOrSlug model constructor.
     * @property {module:model/MatchIDOrSlug}
     */
    MatchIDOrSlug,

    /**
     * The MatchLive model constructor.
     * @property {module:model/MatchLive}
     */
    MatchLive,

    /**
     * The MatchLocalizedStream model constructor.
     * @property {module:model/MatchLocalizedStream}
     */
    MatchLocalizedStream,

    /**
     * The MatchLocalizedStreams model constructor.
     * @property {module:model/MatchLocalizedStreams}
     */
    MatchLocalizedStreams,

    /**
     * The MatchMarketGame model constructor.
     * @property {module:model/MatchMarketGame}
     */
    MatchMarketGame,

    /**
     * The MatchMarkets model constructor.
     * @property {module:model/MatchMarkets}
     */
    MatchMarkets,

    /**
     * The MatchOpponentBasePlayer model constructor.
     * @property {module:model/MatchOpponentBasePlayer}
     */
    MatchOpponentBasePlayer,

    /**
     * The MatchOpponentsObject model constructor.
     * @property {module:model/MatchOpponentsObject}
     */
    MatchOpponentsObject,

    /**
     * The MatchPlayerOpponentsObject model constructor.
     * @property {module:model/MatchPlayerOpponentsObject}
     */
    MatchPlayerOpponentsObject,

    /**
     * The MatchPlayerResult model constructor.
     * @property {module:model/MatchPlayerResult}
     */
    MatchPlayerResult,

    /**
     * The MatchResult model constructor.
     * @property {module:model/MatchResult}
     */
    MatchResult,

    /**
     * The MatchStatus model constructor.
     * @property {module:model/MatchStatus}
     */
    MatchStatus,

    /**
     * The MatchTeamOpponentsObject model constructor.
     * @property {module:model/MatchTeamOpponentsObject}
     */
    MatchTeamOpponentsObject,

    /**
     * The MatchTeamResult model constructor.
     * @property {module:model/MatchTeamResult}
     */
    MatchTeamResult,

    /**
     * The MatchType model constructor.
     * @property {module:model/MatchType}
     */
    MatchType,

    /**
     * The NonDeletionIncident model constructor.
     * @property {module:model/NonDeletionIncident}
     */
    NonDeletionIncident,

    /**
     * The Opponent model constructor.
     * @property {module:model/Opponent}
     */
    Opponent,

    /**
     * The OpponentID model constructor.
     * @property {module:model/OpponentID}
     */
    OpponentID,

    /**
     * The OpponentID1 model constructor.
     * @property {module:model/OpponentID1}
     */
    OpponentID1,

    /**
     * The OpponentType model constructor.
     * @property {module:model/OpponentType}
     */
    OpponentType,

    /**
     * The OpponentTypePlayer model constructor.
     * @property {module:model/OpponentTypePlayer}
     */
    OpponentTypePlayer,

    /**
     * The OpponentTypeTeam model constructor.
     * @property {module:model/OpponentTypeTeam}
     */
    OpponentTypeTeam,

    /**
     * The OwHeroIDOrSlug model constructor.
     * @property {module:model/OwHeroIDOrSlug}
     */
    OwHeroIDOrSlug,

    /**
     * The OwMapIDOrSlug model constructor.
     * @property {module:model/OwMapIDOrSlug}
     */
    OwMapIDOrSlug,

    /**
     * The Player model constructor.
     * @property {module:model/Player}
     */
    Player,

    /**
     * The PlayerIDOrSlug model constructor.
     * @property {module:model/PlayerIDOrSlug}
     */
    PlayerIDOrSlug,

    /**
     * The PreviousMatch model constructor.
     * @property {module:model/PreviousMatch}
     */
    PreviousMatch,

    /**
     * The PreviousMatchType model constructor.
     * @property {module:model/PreviousMatchType}
     */
    PreviousMatchType,

    /**
     * The RangeOverBrackets model constructor.
     * @property {module:model/RangeOverBrackets}
     */
    RangeOverBrackets,

    /**
     * The RangeOverLeagues model constructor.
     * @property {module:model/RangeOverLeagues}
     */
    RangeOverLeagues,

    /**
     * The RangeOverMatches model constructor.
     * @property {module:model/RangeOverMatches}
     */
    RangeOverMatches,

    /**
     * The RangeOverPlayers model constructor.
     * @property {module:model/RangeOverPlayers}
     */
    RangeOverPlayers,

    /**
     * The RangeOverSeries model constructor.
     * @property {module:model/RangeOverSeries}
     */
    RangeOverSeries,

    /**
     * The RangeOverShortTournaments model constructor.
     * @property {module:model/RangeOverShortTournaments}
     */
    RangeOverShortTournaments,

    /**
     * The RangeOverShortVideogameVersions model constructor.
     * @property {module:model/RangeOverShortVideogameVersions}
     */
    RangeOverShortVideogameVersions,

    /**
     * The RangeOverTeams model constructor.
     * @property {module:model/RangeOverTeams}
     */
    RangeOverTeams,

    /**
     * The SearchOverBrackets model constructor.
     * @property {module:model/SearchOverBrackets}
     */
    SearchOverBrackets,

    /**
     * The SearchOverLeagues model constructor.
     * @property {module:model/SearchOverLeagues}
     */
    SearchOverLeagues,

    /**
     * The SearchOverMatches model constructor.
     * @property {module:model/SearchOverMatches}
     */
    SearchOverMatches,

    /**
     * The SearchOverPlayers model constructor.
     * @property {module:model/SearchOverPlayers}
     */
    SearchOverPlayers,

    /**
     * The SearchOverSeries model constructor.
     * @property {module:model/SearchOverSeries}
     */
    SearchOverSeries,

    /**
     * The SearchOverShortTournaments model constructor.
     * @property {module:model/SearchOverShortTournaments}
     */
    SearchOverShortTournaments,

    /**
     * The SearchOverShortVideogameVersions model constructor.
     * @property {module:model/SearchOverShortVideogameVersions}
     */
    SearchOverShortVideogameVersions,

    /**
     * The SearchOverTeams model constructor.
     * @property {module:model/SearchOverTeams}
     */
    SearchOverTeams,

    /**
     * The SelectionResult model constructor.
     * @property {module:model/SelectionResult}
     */
    SelectionResult,

    /**
     * The Serie model constructor.
     * @property {module:model/Serie}
     */
    Serie,

    /**
     * The SerieIDOrSlug model constructor.
     * @property {module:model/SerieIDOrSlug}
     */
    SerieIDOrSlug,

    /**
     * The ShortTournament model constructor.
     * @property {module:model/ShortTournament}
     */
    ShortTournament,

    /**
     * The ShortVideogameVersion model constructor.
     * @property {module:model/ShortVideogameVersion}
     */
    ShortVideogameVersion,

    /**
     * The ShortVideogameVersion1 model constructor.
     * @property {module:model/ShortVideogameVersion1}
     */
    ShortVideogameVersion1,

    /**
     * The Standing model constructor.
     * @property {module:model/Standing}
     */
    Standing,

    /**
     * The Stream model constructor.
     * @property {module:model/Stream}
     */
    Stream,

    /**
     * The StreamLanguage model constructor.
     * @property {module:model/StreamLanguage}
     */
    StreamLanguage,

    /**
     * The Team model constructor.
     * @property {module:model/Team}
     */
    Team,

    /**
     * The TeamIDOrSlug model constructor.
     * @property {module:model/TeamIDOrSlug}
     */
    TeamIDOrSlug,

    /**
     * The Tournament model constructor.
     * @property {module:model/Tournament}
     */
    Tournament,

    /**
     * The TournamentIDOrSlug model constructor.
     * @property {module:model/TournamentIDOrSlug}
     */
    TournamentIDOrSlug,

    /**
     * The TournamentPlayerRosters model constructor.
     * @property {module:model/TournamentPlayerRosters}
     */
    TournamentPlayerRosters,

    /**
     * The TournamentRosterItem model constructor.
     * @property {module:model/TournamentRosterItem}
     */
    TournamentRosterItem,

    /**
     * The TournamentRosters model constructor.
     * @property {module:model/TournamentRosters}
     */
    TournamentRosters,

    /**
     * The TournamentTeamRosters model constructor.
     * @property {module:model/TournamentTeamRosters}
     */
    TournamentTeamRosters,

    /**
     * The Videogame model constructor.
     * @property {module:model/Videogame}
     */
    Videogame,

    /**
     * The VideogameCSGO model constructor.
     * @property {module:model/VideogameCSGO}
     */
    VideogameCSGO,

    /**
     * The VideogameCodmw model constructor.
     * @property {module:model/VideogameCodmw}
     */
    VideogameCodmw,

    /**
     * The VideogameDota2 model constructor.
     * @property {module:model/VideogameDota2}
     */
    VideogameDota2,

    /**
     * The VideogameFifa model constructor.
     * @property {module:model/VideogameFifa}
     */
    VideogameFifa,

    /**
     * The VideogameID model constructor.
     * @property {module:model/VideogameID}
     */
    VideogameID,

    /**
     * The VideogameIDOrSlug model constructor.
     * @property {module:model/VideogameIDOrSlug}
     */
    VideogameIDOrSlug,

    /**
     * The VideogameLeague model constructor.
     * @property {module:model/VideogameLeague}
     */
    VideogameLeague,

    /**
     * The VideogameLoL model constructor.
     * @property {module:model/VideogameLoL}
     */
    VideogameLoL,

    /**
     * The VideogameOverwatch model constructor.
     * @property {module:model/VideogameOverwatch}
     */
    VideogameOverwatch,

    /**
     * The VideogamePUBG model constructor.
     * @property {module:model/VideogamePUBG}
     */
    VideogamePUBG,

    /**
     * The VideogameR6siege model constructor.
     * @property {module:model/VideogameR6siege}
     */
    VideogameR6siege,

    /**
     * The VideogameRocketLeague model constructor.
     * @property {module:model/VideogameRocketLeague}
     */
    VideogameRocketLeague,

    /**
     * The VideogameSlug model constructor.
     * @property {module:model/VideogameSlug}
     */
    VideogameSlug,

    /**
     * The VideogameTitle model constructor.
     * @property {module:model/VideogameTitle}
     */
    VideogameTitle,

    /**
     * The VideogameTitle1 model constructor.
     * @property {module:model/VideogameTitle1}
     */
    VideogameTitle1,

    /**
     * The VideogameValorant model constructor.
     * @property {module:model/VideogameValorant}
     */
    VideogameValorant,

    /**
    * The IncidentsApi service constructor.
    * @property {module:api/IncidentsApi}
    */
    IncidentsApi,

    /**
    * The LeaguesApi service constructor.
    * @property {module:api/LeaguesApi}
    */
    LeaguesApi,

    /**
    * The LivesApi service constructor.
    * @property {module:api/LivesApi}
    */
    LivesApi,

    /**
    * The MatchesApi service constructor.
    * @property {module:api/MatchesApi}
    */
    MatchesApi,

    /**
    * The PlayersApi service constructor.
    * @property {module:api/PlayersApi}
    */
    PlayersApi,

    /**
    * The SeriesApi service constructor.
    * @property {module:api/SeriesApi}
    */
    SeriesApi,

    /**
    * The TeamsApi service constructor.
    * @property {module:api/TeamsApi}
    */
    TeamsApi,

    /**
    * The TournamentsApi service constructor.
    * @property {module:api/TournamentsApi}
    */
    TournamentsApi,

    /**
    * The VideogamesApi service constructor.
    * @property {module:api/VideogamesApi}
    */
    VideogamesApi
};
