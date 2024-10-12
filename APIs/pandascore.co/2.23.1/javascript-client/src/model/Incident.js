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
import DeletionIncident from './DeletionIncident';
import DeletionIncidentChangeType from './DeletionIncidentChangeType';
import DeletionObject from './DeletionObject';
import IncidentID from './IncidentID';
import IncidentOfTypeLeague from './IncidentOfTypeLeague';
import IncidentOfTypeMatch from './IncidentOfTypeMatch';
import IncidentOfTypePlayer from './IncidentOfTypePlayer';
import IncidentOfTypeSerie from './IncidentOfTypeSerie';
import IncidentOfTypeTeam from './IncidentOfTypeTeam';
import IncidentOfTypeTournament from './IncidentOfTypeTournament';
import IncidentType from './IncidentType';

/**
 * The Incident model module.
 * @module model/Incident
 * @version 2.23.1
 */
class Incident {
    /**
     * Constructs a new <code>Incident</code>.
     * @alias module:model/Incident
     * @param {(module:model/DeletionIncident|module:model/IncidentOfTypeLeague|module:model/IncidentOfTypeMatch|module:model/IncidentOfTypePlayer|module:model/IncidentOfTypeSerie|module:model/IncidentOfTypeTeam|module:model/IncidentOfTypeTournament)} instance The actual instance to initialize Incident.
     */
    constructor(instance = null) {
        if (instance === null) {
            this.actualInstance = null;
            return;
        }
        var match = 0;
        var errorMessages = [];
        try {
            if (typeof instance === "IncidentOfTypeLeague") {
                this.actualInstance = instance;
            } else {
                // plain JS object
                // validate the object
                IncidentOfTypeLeague.validateJSON(instance); // throw an exception if no match
                // create IncidentOfTypeLeague from JS object
                this.actualInstance = IncidentOfTypeLeague.constructFromObject(instance);
            }
            match++;
        } catch(err) {
            // json data failed to deserialize into IncidentOfTypeLeague
            errorMessages.push("Failed to construct IncidentOfTypeLeague: " + err)
        }

        try {
            if (typeof instance === "IncidentOfTypeMatch") {
                this.actualInstance = instance;
            } else {
                // plain JS object
                // validate the object
                IncidentOfTypeMatch.validateJSON(instance); // throw an exception if no match
                // create IncidentOfTypeMatch from JS object
                this.actualInstance = IncidentOfTypeMatch.constructFromObject(instance);
            }
            match++;
        } catch(err) {
            // json data failed to deserialize into IncidentOfTypeMatch
            errorMessages.push("Failed to construct IncidentOfTypeMatch: " + err)
        }

        try {
            if (typeof instance === "IncidentOfTypePlayer") {
                this.actualInstance = instance;
            } else {
                // plain JS object
                // validate the object
                IncidentOfTypePlayer.validateJSON(instance); // throw an exception if no match
                // create IncidentOfTypePlayer from JS object
                this.actualInstance = IncidentOfTypePlayer.constructFromObject(instance);
            }
            match++;
        } catch(err) {
            // json data failed to deserialize into IncidentOfTypePlayer
            errorMessages.push("Failed to construct IncidentOfTypePlayer: " + err)
        }

        try {
            if (typeof instance === "IncidentOfTypeSerie") {
                this.actualInstance = instance;
            } else {
                // plain JS object
                // validate the object
                IncidentOfTypeSerie.validateJSON(instance); // throw an exception if no match
                // create IncidentOfTypeSerie from JS object
                this.actualInstance = IncidentOfTypeSerie.constructFromObject(instance);
            }
            match++;
        } catch(err) {
            // json data failed to deserialize into IncidentOfTypeSerie
            errorMessages.push("Failed to construct IncidentOfTypeSerie: " + err)
        }

        try {
            if (typeof instance === "IncidentOfTypeTeam") {
                this.actualInstance = instance;
            } else {
                // plain JS object
                // validate the object
                IncidentOfTypeTeam.validateJSON(instance); // throw an exception if no match
                // create IncidentOfTypeTeam from JS object
                this.actualInstance = IncidentOfTypeTeam.constructFromObject(instance);
            }
            match++;
        } catch(err) {
            // json data failed to deserialize into IncidentOfTypeTeam
            errorMessages.push("Failed to construct IncidentOfTypeTeam: " + err)
        }

        try {
            if (typeof instance === "IncidentOfTypeTournament") {
                this.actualInstance = instance;
            } else {
                // plain JS object
                // validate the object
                IncidentOfTypeTournament.validateJSON(instance); // throw an exception if no match
                // create IncidentOfTypeTournament from JS object
                this.actualInstance = IncidentOfTypeTournament.constructFromObject(instance);
            }
            match++;
        } catch(err) {
            // json data failed to deserialize into IncidentOfTypeTournament
            errorMessages.push("Failed to construct IncidentOfTypeTournament: " + err)
        }

        try {
            if (typeof instance === "DeletionIncident") {
                this.actualInstance = instance;
            } else {
                // plain JS object
                // validate the object
                DeletionIncident.validateJSON(instance); // throw an exception if no match
                // create DeletionIncident from JS object
                this.actualInstance = DeletionIncident.constructFromObject(instance);
            }
            match++;
        } catch(err) {
            // json data failed to deserialize into DeletionIncident
            errorMessages.push("Failed to construct DeletionIncident: " + err)
        }

        if (match > 1) {
            throw new Error("Multiple matches found constructing `Incident` with oneOf schemas DeletionIncident, IncidentOfTypeLeague, IncidentOfTypeMatch, IncidentOfTypePlayer, IncidentOfTypeSerie, IncidentOfTypeTeam, IncidentOfTypeTournament. Input: " + JSON.stringify(instance));
        } else if (match === 0) {
            this.actualInstance = null; // clear the actual instance in case there are multiple matches
            throw new Error("No match found constructing `Incident` with oneOf schemas DeletionIncident, IncidentOfTypeLeague, IncidentOfTypeMatch, IncidentOfTypePlayer, IncidentOfTypeSerie, IncidentOfTypeTeam, IncidentOfTypeTournament. Details: " +
                            errorMessages.join(", "));
        } else { // only 1 match
            // the input is valid
        }
    }

    /**
     * Constructs a <code>Incident</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/Incident} obj Optional instance to populate.
     * @return {module:model/Incident} The populated <code>Incident</code> instance.
     */
    static constructFromObject(data, obj) {
        return new Incident(data);
    }

    /**
     * Gets the actual instance, which can be <code>DeletionIncident</code>, <code>IncidentOfTypeLeague</code>, <code>IncidentOfTypeMatch</code>, <code>IncidentOfTypePlayer</code>, <code>IncidentOfTypeSerie</code>, <code>IncidentOfTypeTeam</code>, <code>IncidentOfTypeTournament</code>.
     * @return {(module:model/DeletionIncident|module:model/IncidentOfTypeLeague|module:model/IncidentOfTypeMatch|module:model/IncidentOfTypePlayer|module:model/IncidentOfTypeSerie|module:model/IncidentOfTypeTeam|module:model/IncidentOfTypeTournament)} The actual instance.
     */
    getActualInstance() {
        return this.actualInstance;
    }

    /**
     * Sets the actual instance, which can be <code>DeletionIncident</code>, <code>IncidentOfTypeLeague</code>, <code>IncidentOfTypeMatch</code>, <code>IncidentOfTypePlayer</code>, <code>IncidentOfTypeSerie</code>, <code>IncidentOfTypeTeam</code>, <code>IncidentOfTypeTournament</code>.
     * @param {(module:model/DeletionIncident|module:model/IncidentOfTypeLeague|module:model/IncidentOfTypeMatch|module:model/IncidentOfTypePlayer|module:model/IncidentOfTypeSerie|module:model/IncidentOfTypeTeam|module:model/IncidentOfTypeTournament)} obj The actual instance.
     */
    setActualInstance(obj) {
       this.actualInstance = Incident.constructFromObject(obj).getActualInstance();
    }

    /**
     * Returns the JSON representation of the actual instance.
     * @return {string}
     */
    toJSON = function(){
        return this.getActualInstance();
    }

    /**
     * Create an instance of Incident from a JSON string.
     * @param {string} json_string JSON string.
     * @return {module:model/Incident} An instance of Incident.
     */
    static fromJSON = function(json_string){
        return Incident.constructFromObject(JSON.parse(json_string));
    }
}

/**
 * @member {module:model/DeletionIncidentChangeType} change_type
 */
Incident.prototype['change_type'] = undefined;

/**
 * @member {module:model/IncidentID} id
 */
Incident.prototype['id'] = undefined;

/**
 * @member {Date} modified_at
 */
Incident.prototype['modified_at'] = undefined;

/**
 * @member {module:model/DeletionObject} object
 */
Incident.prototype['object'] = undefined;

/**
 * @member {module:model/IncidentType} type
 */
Incident.prototype['type'] = undefined;


Incident.OneOf = ["DeletionIncident", "IncidentOfTypeLeague", "IncidentOfTypeMatch", "IncidentOfTypePlayer", "IncidentOfTypeSerie", "IncidentOfTypeTeam", "IncidentOfTypeTournament"];

export default Incident;

