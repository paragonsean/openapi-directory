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

(function(root, factory) {
  if (typeof define === 'function' && define.amd) {
    // AMD.
    define(['expect.js', process.cwd()+'/src/index'], factory);
  } else if (typeof module === 'object' && module.exports) {
    // CommonJS-like environments that support module.exports, like Node.
    factory(require('expect.js'), require(process.cwd()+'/src/index'));
  } else {
    // Browser globals (root is window)
    factory(root.expect, root.PandaScoreRestApiForAllVideogames);
  }
}(this, function(expect, PandaScoreRestApiForAllVideogames) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new PandaScoreRestApiForAllVideogames.BettingMatch();
  });

  var getProperty = function(object, getter, property) {
    // Use getter method if present; otherwise, get the property directly.
    if (typeof object[getter] === 'function')
      return object[getter]();
    else
      return object[property];
  }

  var setProperty = function(object, setter, property, value) {
    // Use setter method if present; otherwise, set the property directly.
    if (typeof object[setter] === 'function')
      object[setter](value);
    else
      object[property] = value;
  }

  describe('BettingMatch', function() {
    it('should create an instance of BettingMatch', function() {
      // uncomment below and update the code to test BettingMatch
      //var instance = new PandaScoreRestApiForAllVideogames.BettingMatch();
      //expect(instance).to.be.a(PandaScoreRestApiForAllVideogames.BettingMatch);
    });

    it('should have the property beginAt (base name: "begin_at")', function() {
      // uncomment below and update the code to test the property beginAt
      //var instance = new PandaScoreRestApiForAllVideogames.BettingMatch();
      //expect(instance).to.be();
    });

    it('should have the property bettingMetadata (base name: "betting_metadata")', function() {
      // uncomment below and update the code to test the property bettingMetadata
      //var instance = new PandaScoreRestApiForAllVideogames.BettingMatch();
      //expect(instance).to.be();
    });

    it('should have the property detailedStats (base name: "detailed_stats")', function() {
      // uncomment below and update the code to test the property detailedStats
      //var instance = new PandaScoreRestApiForAllVideogames.BettingMatch();
      //expect(instance).to.be();
    });

    it('should have the property draw (base name: "draw")', function() {
      // uncomment below and update the code to test the property draw
      //var instance = new PandaScoreRestApiForAllVideogames.BettingMatch();
      //expect(instance).to.be();
    });

    it('should have the property endAt (base name: "end_at")', function() {
      // uncomment below and update the code to test the property endAt
      //var instance = new PandaScoreRestApiForAllVideogames.BettingMatch();
      //expect(instance).to.be();
    });

    it('should have the property forfeit (base name: "forfeit")', function() {
      // uncomment below and update the code to test the property forfeit
      //var instance = new PandaScoreRestApiForAllVideogames.BettingMatch();
      //expect(instance).to.be();
    });

    it('should have the property gameAdvantage (base name: "game_advantage")', function() {
      // uncomment below and update the code to test the property gameAdvantage
      //var instance = new PandaScoreRestApiForAllVideogames.BettingMatch();
      //expect(instance).to.be();
    });

    it('should have the property games (base name: "games")', function() {
      // uncomment below and update the code to test the property games
      //var instance = new PandaScoreRestApiForAllVideogames.BettingMatch();
      //expect(instance).to.be();
    });

    it('should have the property id (base name: "id")', function() {
      // uncomment below and update the code to test the property id
      //var instance = new PandaScoreRestApiForAllVideogames.BettingMatch();
      //expect(instance).to.be();
    });

    it('should have the property league (base name: "league")', function() {
      // uncomment below and update the code to test the property league
      //var instance = new PandaScoreRestApiForAllVideogames.BettingMatch();
      //expect(instance).to.be();
    });

    it('should have the property leagueId (base name: "league_id")', function() {
      // uncomment below and update the code to test the property leagueId
      //var instance = new PandaScoreRestApiForAllVideogames.BettingMatch();
      //expect(instance).to.be();
    });

    it('should have the property live (base name: "live")', function() {
      // uncomment below and update the code to test the property live
      //var instance = new PandaScoreRestApiForAllVideogames.BettingMatch();
      //expect(instance).to.be();
    });

    it('should have the property liveEmbedUrl (base name: "live_embed_url")', function() {
      // uncomment below and update the code to test the property liveEmbedUrl
      //var instance = new PandaScoreRestApiForAllVideogames.BettingMatch();
      //expect(instance).to.be();
    });

    it('should have the property matchType (base name: "match_type")', function() {
      // uncomment below and update the code to test the property matchType
      //var instance = new PandaScoreRestApiForAllVideogames.BettingMatch();
      //expect(instance).to.be();
    });

    it('should have the property modifiedAt (base name: "modified_at")', function() {
      // uncomment below and update the code to test the property modifiedAt
      //var instance = new PandaScoreRestApiForAllVideogames.BettingMatch();
      //expect(instance).to.be();
    });

    it('should have the property name (base name: "name")', function() {
      // uncomment below and update the code to test the property name
      //var instance = new PandaScoreRestApiForAllVideogames.BettingMatch();
      //expect(instance).to.be();
    });

    it('should have the property numberOfGames (base name: "number_of_games")', function() {
      // uncomment below and update the code to test the property numberOfGames
      //var instance = new PandaScoreRestApiForAllVideogames.BettingMatch();
      //expect(instance).to.be();
    });

    it('should have the property officialStreamUrl (base name: "official_stream_url")', function() {
      // uncomment below and update the code to test the property officialStreamUrl
      //var instance = new PandaScoreRestApiForAllVideogames.BettingMatch();
      //expect(instance).to.be();
    });

    it('should have the property opponents (base name: "opponents")', function() {
      // uncomment below and update the code to test the property opponents
      //var instance = new PandaScoreRestApiForAllVideogames.BettingMatch();
      //expect(instance).to.be();
    });

    it('should have the property originalScheduledAt (base name: "original_scheduled_at")', function() {
      // uncomment below and update the code to test the property originalScheduledAt
      //var instance = new PandaScoreRestApiForAllVideogames.BettingMatch();
      //expect(instance).to.be();
    });

    it('should have the property rescheduled (base name: "rescheduled")', function() {
      // uncomment below and update the code to test the property rescheduled
      //var instance = new PandaScoreRestApiForAllVideogames.BettingMatch();
      //expect(instance).to.be();
    });

    it('should have the property results (base name: "results")', function() {
      // uncomment below and update the code to test the property results
      //var instance = new PandaScoreRestApiForAllVideogames.BettingMatch();
      //expect(instance).to.be();
    });

    it('should have the property scheduledAt (base name: "scheduled_at")', function() {
      // uncomment below and update the code to test the property scheduledAt
      //var instance = new PandaScoreRestApiForAllVideogames.BettingMatch();
      //expect(instance).to.be();
    });

    it('should have the property serie (base name: "serie")', function() {
      // uncomment below and update the code to test the property serie
      //var instance = new PandaScoreRestApiForAllVideogames.BettingMatch();
      //expect(instance).to.be();
    });

    it('should have the property serieId (base name: "serie_id")', function() {
      // uncomment below and update the code to test the property serieId
      //var instance = new PandaScoreRestApiForAllVideogames.BettingMatch();
      //expect(instance).to.be();
    });

    it('should have the property slug (base name: "slug")', function() {
      // uncomment below and update the code to test the property slug
      //var instance = new PandaScoreRestApiForAllVideogames.BettingMatch();
      //expect(instance).to.be();
    });

    it('should have the property status (base name: "status")', function() {
      // uncomment below and update the code to test the property status
      //var instance = new PandaScoreRestApiForAllVideogames.BettingMatch();
      //expect(instance).to.be();
    });

    it('should have the property streams (base name: "streams")', function() {
      // uncomment below and update the code to test the property streams
      //var instance = new PandaScoreRestApiForAllVideogames.BettingMatch();
      //expect(instance).to.be();
    });

    it('should have the property streamsList (base name: "streams_list")', function() {
      // uncomment below and update the code to test the property streamsList
      //var instance = new PandaScoreRestApiForAllVideogames.BettingMatch();
      //expect(instance).to.be();
    });

    it('should have the property tournament (base name: "tournament")', function() {
      // uncomment below and update the code to test the property tournament
      //var instance = new PandaScoreRestApiForAllVideogames.BettingMatch();
      //expect(instance).to.be();
    });

    it('should have the property tournamentId (base name: "tournament_id")', function() {
      // uncomment below and update the code to test the property tournamentId
      //var instance = new PandaScoreRestApiForAllVideogames.BettingMatch();
      //expect(instance).to.be();
    });

    it('should have the property videogame (base name: "videogame")', function() {
      // uncomment below and update the code to test the property videogame
      //var instance = new PandaScoreRestApiForAllVideogames.BettingMatch();
      //expect(instance).to.be();
    });

    it('should have the property videogameVersion (base name: "videogame_version")', function() {
      // uncomment below and update the code to test the property videogameVersion
      //var instance = new PandaScoreRestApiForAllVideogames.BettingMatch();
      //expect(instance).to.be();
    });

    it('should have the property winner (base name: "winner")', function() {
      // uncomment below and update the code to test the property winner
      //var instance = new PandaScoreRestApiForAllVideogames.BettingMatch();
      //expect(instance).to.be();
    });

    it('should have the property winnerId (base name: "winner_id")', function() {
      // uncomment below and update the code to test the property winnerId
      //var instance = new PandaScoreRestApiForAllVideogames.BettingMatch();
      //expect(instance).to.be();
    });

  });

}));
