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

import ApiClient from '../ApiClient';
import VideogameCSGO from './VideogameCSGO';
import VideogameCodmw from './VideogameCodmw';
import VideogameDota2 from './VideogameDota2';
import VideogameFifa from './VideogameFifa';
import VideogameLeague from './VideogameLeague';
import VideogameLoL from './VideogameLoL';
import VideogameOverwatch from './VideogameOverwatch';
import VideogamePUBG from './VideogamePUBG';
import VideogameR6siege from './VideogameR6siege';
import VideogameRocketLeague from './VideogameRocketLeague';
import VideogameValorant from './VideogameValorant';

/**
 * The Videogame model module.
 * @module model/Videogame
 * @version 2.23.1
 */
class Videogame {
    /**
     * Constructs a new <code>Videogame</code>.
     * @alias module:model/Videogame
     * @param {(module:model/VideogameCSGO|module:model/VideogameCodmw|module:model/VideogameDota2|module:model/VideogameFifa|module:model/VideogameLoL|module:model/VideogameOverwatch|module:model/VideogamePUBG|module:model/VideogameR6siege|module:model/VideogameRocketLeague|module:model/VideogameValorant)} instance The actual instance to initialize Videogame.
     */
    constructor(instance = null) {
        if (instance === null) {
            this.actualInstance = null;
            return;
        }
        var match = 0;
        var errorMessages = [];
        try {
            if (typeof instance === "VideogameLoL") {
                this.actualInstance = instance;
            } else {
                // plain JS object
                // validate the object
                VideogameLoL.validateJSON(instance); // throw an exception if no match
                // create VideogameLoL from JS object
                this.actualInstance = VideogameLoL.constructFromObject(instance);
            }
            match++;
        } catch(err) {
            // json data failed to deserialize into VideogameLoL
            errorMessages.push("Failed to construct VideogameLoL: " + err)
        }

        try {
            if (typeof instance === "VideogameCSGO") {
                this.actualInstance = instance;
            } else {
                // plain JS object
                // validate the object
                VideogameCSGO.validateJSON(instance); // throw an exception if no match
                // create VideogameCSGO from JS object
                this.actualInstance = VideogameCSGO.constructFromObject(instance);
            }
            match++;
        } catch(err) {
            // json data failed to deserialize into VideogameCSGO
            errorMessages.push("Failed to construct VideogameCSGO: " + err)
        }

        try {
            if (typeof instance === "VideogameDota2") {
                this.actualInstance = instance;
            } else {
                // plain JS object
                // validate the object
                VideogameDota2.validateJSON(instance); // throw an exception if no match
                // create VideogameDota2 from JS object
                this.actualInstance = VideogameDota2.constructFromObject(instance);
            }
            match++;
        } catch(err) {
            // json data failed to deserialize into VideogameDota2
            errorMessages.push("Failed to construct VideogameDota2: " + err)
        }

        try {
            if (typeof instance === "VideogameOverwatch") {
                this.actualInstance = instance;
            } else {
                // plain JS object
                // validate the object
                VideogameOverwatch.validateJSON(instance); // throw an exception if no match
                // create VideogameOverwatch from JS object
                this.actualInstance = VideogameOverwatch.constructFromObject(instance);
            }
            match++;
        } catch(err) {
            // json data failed to deserialize into VideogameOverwatch
            errorMessages.push("Failed to construct VideogameOverwatch: " + err)
        }

        try {
            if (typeof instance === "VideogamePUBG") {
                this.actualInstance = instance;
            } else {
                // plain JS object
                // validate the object
                VideogamePUBG.validateJSON(instance); // throw an exception if no match
                // create VideogamePUBG from JS object
                this.actualInstance = VideogamePUBG.constructFromObject(instance);
            }
            match++;
        } catch(err) {
            // json data failed to deserialize into VideogamePUBG
            errorMessages.push("Failed to construct VideogamePUBG: " + err)
        }

        try {
            if (typeof instance === "VideogameRocketLeague") {
                this.actualInstance = instance;
            } else {
                // plain JS object
                // validate the object
                VideogameRocketLeague.validateJSON(instance); // throw an exception if no match
                // create VideogameRocketLeague from JS object
                this.actualInstance = VideogameRocketLeague.constructFromObject(instance);
            }
            match++;
        } catch(err) {
            // json data failed to deserialize into VideogameRocketLeague
            errorMessages.push("Failed to construct VideogameRocketLeague: " + err)
        }

        try {
            if (typeof instance === "VideogameCodmw") {
                this.actualInstance = instance;
            } else {
                // plain JS object
                // validate the object
                VideogameCodmw.validateJSON(instance); // throw an exception if no match
                // create VideogameCodmw from JS object
                this.actualInstance = VideogameCodmw.constructFromObject(instance);
            }
            match++;
        } catch(err) {
            // json data failed to deserialize into VideogameCodmw
            errorMessages.push("Failed to construct VideogameCodmw: " + err)
        }

        try {
            if (typeof instance === "VideogameR6siege") {
                this.actualInstance = instance;
            } else {
                // plain JS object
                // validate the object
                VideogameR6siege.validateJSON(instance); // throw an exception if no match
                // create VideogameR6siege from JS object
                this.actualInstance = VideogameR6siege.constructFromObject(instance);
            }
            match++;
        } catch(err) {
            // json data failed to deserialize into VideogameR6siege
            errorMessages.push("Failed to construct VideogameR6siege: " + err)
        }

        try {
            if (typeof instance === "VideogameFifa") {
                this.actualInstance = instance;
            } else {
                // plain JS object
                // validate the object
                VideogameFifa.validateJSON(instance); // throw an exception if no match
                // create VideogameFifa from JS object
                this.actualInstance = VideogameFifa.constructFromObject(instance);
            }
            match++;
        } catch(err) {
            // json data failed to deserialize into VideogameFifa
            errorMessages.push("Failed to construct VideogameFifa: " + err)
        }

        try {
            if (typeof instance === "VideogameValorant") {
                this.actualInstance = instance;
            } else {
                // plain JS object
                // validate the object
                VideogameValorant.validateJSON(instance); // throw an exception if no match
                // create VideogameValorant from JS object
                this.actualInstance = VideogameValorant.constructFromObject(instance);
            }
            match++;
        } catch(err) {
            // json data failed to deserialize into VideogameValorant
            errorMessages.push("Failed to construct VideogameValorant: " + err)
        }

        if (match > 1) {
            throw new Error("Multiple matches found constructing `Videogame` with oneOf schemas VideogameCSGO, VideogameCodmw, VideogameDota2, VideogameFifa, VideogameLoL, VideogameOverwatch, VideogamePUBG, VideogameR6siege, VideogameRocketLeague, VideogameValorant. Input: " + JSON.stringify(instance));
        } else if (match === 0) {
            this.actualInstance = null; // clear the actual instance in case there are multiple matches
            throw new Error("No match found constructing `Videogame` with oneOf schemas VideogameCSGO, VideogameCodmw, VideogameDota2, VideogameFifa, VideogameLoL, VideogameOverwatch, VideogamePUBG, VideogameR6siege, VideogameRocketLeague, VideogameValorant. Details: " +
                            errorMessages.join(", "));
        } else { // only 1 match
            // the input is valid
        }
    }

    /**
     * Constructs a <code>Videogame</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/Videogame} obj Optional instance to populate.
     * @return {module:model/Videogame} The populated <code>Videogame</code> instance.
     */
    static constructFromObject(data, obj) {
        return new Videogame(data);
    }

    /**
     * Gets the actual instance, which can be <code>VideogameCSGO</code>, <code>VideogameCodmw</code>, <code>VideogameDota2</code>, <code>VideogameFifa</code>, <code>VideogameLoL</code>, <code>VideogameOverwatch</code>, <code>VideogamePUBG</code>, <code>VideogameR6siege</code>, <code>VideogameRocketLeague</code>, <code>VideogameValorant</code>.
     * @return {(module:model/VideogameCSGO|module:model/VideogameCodmw|module:model/VideogameDota2|module:model/VideogameFifa|module:model/VideogameLoL|module:model/VideogameOverwatch|module:model/VideogamePUBG|module:model/VideogameR6siege|module:model/VideogameRocketLeague|module:model/VideogameValorant)} The actual instance.
     */
    getActualInstance() {
        return this.actualInstance;
    }

    /**
     * Sets the actual instance, which can be <code>VideogameCSGO</code>, <code>VideogameCodmw</code>, <code>VideogameDota2</code>, <code>VideogameFifa</code>, <code>VideogameLoL</code>, <code>VideogameOverwatch</code>, <code>VideogamePUBG</code>, <code>VideogameR6siege</code>, <code>VideogameRocketLeague</code>, <code>VideogameValorant</code>.
     * @param {(module:model/VideogameCSGO|module:model/VideogameCodmw|module:model/VideogameDota2|module:model/VideogameFifa|module:model/VideogameLoL|module:model/VideogameOverwatch|module:model/VideogamePUBG|module:model/VideogameR6siege|module:model/VideogameRocketLeague|module:model/VideogameValorant)} obj The actual instance.
     */
    setActualInstance(obj) {
       this.actualInstance = Videogame.constructFromObject(obj).getActualInstance();
    }

    /**
     * Returns the JSON representation of the actual instance.
     * @return {string}
     */
    toJSON = function(){
        return this.getActualInstance();
    }

    /**
     * Create an instance of Videogame from a JSON string.
     * @param {string} json_string JSON string.
     * @return {module:model/Videogame} An instance of Videogame.
     */
    static fromJSON = function(json_string){
        return Videogame.constructFromObject(JSON.parse(json_string));
    }
}

/**
 * @member {Object} current_version
 */
Videogame.prototype['current_version'] = undefined;

/**
 * @member {module:model/Videogame.IdEnum} id
 */
Videogame.prototype['id'] = undefined;

/**
 * @member {Array.<module:model/VideogameLeague>} leagues
 */
Videogame.prototype['leagues'] = undefined;

/**
 * @member {module:model/Videogame.NameEnum} name
 */
Videogame.prototype['name'] = undefined;

/**
 * @member {module:model/Videogame.SlugEnum} slug
 */
Videogame.prototype['slug'] = undefined;


Videogame.OneOf = ["VideogameCSGO", "VideogameCodmw", "VideogameDota2", "VideogameFifa", "VideogameLoL", "VideogameOverwatch", "VideogamePUBG", "VideogameR6siege", "VideogameRocketLeague", "VideogameValorant"];

export default Videogame;

