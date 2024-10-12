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

/**
 * The BasePlayer model module.
 * @module model/BasePlayer
 * @version 2.23.1
 */
class BasePlayer {
    /**
     * Constructs a new <code>BasePlayer</code>.
     * @alias module:model/BasePlayer
     * @param birthYear {Object} 
     * @param birthday {Object} 
     * @param firstName {Object} 
     * @param hometown {Object} 
     * @param id {Number} 
     * @param imageUrl {Object} 
     * @param lastName {Object} 
     * @param name {String} 
     * @param nationality {Object} 
     * @param role {Object} 
     * @param slug {Object} 
     */
    constructor(birthYear, birthday, firstName, hometown, id, imageUrl, lastName, name, nationality, role, slug) { 
        
        BasePlayer.initialize(this, birthYear, birthday, firstName, hometown, id, imageUrl, lastName, name, nationality, role, slug);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, birthYear, birthday, firstName, hometown, id, imageUrl, lastName, name, nationality, role, slug) { 
        obj['birth_year'] = birthYear;
        obj['birthday'] = birthday;
        obj['first_name'] = firstName;
        obj['hometown'] = hometown;
        obj['id'] = id;
        obj['image_url'] = imageUrl;
        obj['last_name'] = lastName;
        obj['name'] = name;
        obj['nationality'] = nationality;
        obj['role'] = role;
        obj['slug'] = slug;
    }

    /**
     * Constructs a <code>BasePlayer</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/BasePlayer} obj Optional instance to populate.
     * @return {module:model/BasePlayer} The populated <code>BasePlayer</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new BasePlayer();

            if (data.hasOwnProperty('birth_year')) {
                obj['birth_year'] = ApiClient.convertToType(data['birth_year'], Object);
            }
            if (data.hasOwnProperty('birthday')) {
                obj['birthday'] = ApiClient.convertToType(data['birthday'], Object);
            }
            if (data.hasOwnProperty('first_name')) {
                obj['first_name'] = ApiClient.convertToType(data['first_name'], Object);
            }
            if (data.hasOwnProperty('hometown')) {
                obj['hometown'] = ApiClient.convertToType(data['hometown'], Object);
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'Number');
            }
            if (data.hasOwnProperty('image_url')) {
                obj['image_url'] = ApiClient.convertToType(data['image_url'], Object);
            }
            if (data.hasOwnProperty('last_name')) {
                obj['last_name'] = ApiClient.convertToType(data['last_name'], Object);
            }
            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
            if (data.hasOwnProperty('nationality')) {
                obj['nationality'] = ApiClient.convertToType(data['nationality'], Object);
            }
            if (data.hasOwnProperty('role')) {
                obj['role'] = ApiClient.convertToType(data['role'], Object);
            }
            if (data.hasOwnProperty('slug')) {
                obj['slug'] = ApiClient.convertToType(data['slug'], Object);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>BasePlayer</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>BasePlayer</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of BasePlayer.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // validate the optional field `birth_year`
        if (data['birth_year']) { // data not null
          Object.validateJSON(data['birth_year']);
        }
        // validate the optional field `birthday`
        if (data['birthday']) { // data not null
          Object.validateJSON(data['birthday']);
        }
        // validate the optional field `first_name`
        if (data['first_name']) { // data not null
          Object.validateJSON(data['first_name']);
        }
        // validate the optional field `hometown`
        if (data['hometown']) { // data not null
          Object.validateJSON(data['hometown']);
        }
        // validate the optional field `image_url`
        if (data['image_url']) { // data not null
          Object.validateJSON(data['image_url']);
        }
        // validate the optional field `last_name`
        if (data['last_name']) { // data not null
          Object.validateJSON(data['last_name']);
        }
        // ensure the json data is a string
        if (data['name'] && !(typeof data['name'] === 'string' || data['name'] instanceof String)) {
            throw new Error("Expected the field `name` to be a primitive type in the JSON string but got " + data['name']);
        }
        // validate the optional field `nationality`
        if (data['nationality']) { // data not null
          Object.validateJSON(data['nationality']);
        }
        // validate the optional field `role`
        if (data['role']) { // data not null
          Object.validateJSON(data['role']);
        }
        // validate the optional field `slug`
        if (data['slug']) { // data not null
          Object.validateJSON(data['slug']);
        }

        return true;
    }


}

BasePlayer.RequiredProperties = ["birth_year", "birthday", "first_name", "hometown", "id", "image_url", "last_name", "name", "nationality", "role", "slug"];

/**
 * @member {Object} birth_year
 */
BasePlayer.prototype['birth_year'] = undefined;

/**
 * @member {Object} birthday
 */
BasePlayer.prototype['birthday'] = undefined;

/**
 * @member {Object} first_name
 */
BasePlayer.prototype['first_name'] = undefined;

/**
 * @member {Object} hometown
 */
BasePlayer.prototype['hometown'] = undefined;

/**
 * @member {Number} id
 */
BasePlayer.prototype['id'] = undefined;

/**
 * @member {Object} image_url
 */
BasePlayer.prototype['image_url'] = undefined;

/**
 * @member {Object} last_name
 */
BasePlayer.prototype['last_name'] = undefined;

/**
 * @member {String} name
 */
BasePlayer.prototype['name'] = undefined;

/**
 * @member {Object} nationality
 */
BasePlayer.prototype['nationality'] = undefined;

/**
 * @member {Object} role
 */
BasePlayer.prototype['role'] = undefined;

/**
 * @member {Object} slug
 */
BasePlayer.prototype['slug'] = undefined;






export default BasePlayer;

