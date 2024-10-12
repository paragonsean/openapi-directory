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
* Enum class StreamLanguage.
* @enum {}
* @readonly
*/
export default class StreamLanguage {
    
        /**
         * value: "aa"
         * @const
         */
        "aa" = "aa";

    
        /**
         * value: "ab"
         * @const
         */
        "ab" = "ab";

    
        /**
         * value: "ae"
         * @const
         */
        "ae" = "ae";

    
        /**
         * value: "af"
         * @const
         */
        "af" = "af";

    
        /**
         * value: "ak"
         * @const
         */
        "ak" = "ak";

    
        /**
         * value: "am"
         * @const
         */
        "am" = "am";

    
        /**
         * value: "an"
         * @const
         */
        "an" = "an";

    
        /**
         * value: "ar"
         * @const
         */
        "ar" = "ar";

    
        /**
         * value: "as"
         * @const
         */
        "as" = "as";

    
        /**
         * value: "av"
         * @const
         */
        "av" = "av";

    
        /**
         * value: "ay"
         * @const
         */
        "ay" = "ay";

    
        /**
         * value: "az"
         * @const
         */
        "az" = "az";

    
        /**
         * value: "ba"
         * @const
         */
        "ba" = "ba";

    
        /**
         * value: "be"
         * @const
         */
        "be" = "be";

    
        /**
         * value: "bg"
         * @const
         */
        "bg" = "bg";

    
        /**
         * value: "bh"
         * @const
         */
        "bh" = "bh";

    
        /**
         * value: "bi"
         * @const
         */
        "bi" = "bi";

    
        /**
         * value: "bm"
         * @const
         */
        "bm" = "bm";

    
        /**
         * value: "bn"
         * @const
         */
        "bn" = "bn";

    
        /**
         * value: "bo"
         * @const
         */
        "bo" = "bo";

    
        /**
         * value: "br"
         * @const
         */
        "br" = "br";

    
        /**
         * value: "bs"
         * @const
         */
        "bs" = "bs";

    
        /**
         * value: "ca"
         * @const
         */
        "ca" = "ca";

    
        /**
         * value: "ce"
         * @const
         */
        "ce" = "ce";

    
        /**
         * value: "ch"
         * @const
         */
        "ch" = "ch";

    
        /**
         * value: "co"
         * @const
         */
        "co" = "co";

    
        /**
         * value: "cr"
         * @const
         */
        "cr" = "cr";

    
        /**
         * value: "cs"
         * @const
         */
        "cs" = "cs";

    
        /**
         * value: "cu"
         * @const
         */
        "cu" = "cu";

    
        /**
         * value: "cv"
         * @const
         */
        "cv" = "cv";

    
        /**
         * value: "cy"
         * @const
         */
        "cy" = "cy";

    
        /**
         * value: "da"
         * @const
         */
        "da" = "da";

    
        /**
         * value: "de"
         * @const
         */
        "de" = "de";

    
        /**
         * value: "dv"
         * @const
         */
        "dv" = "dv";

    
        /**
         * value: "dz"
         * @const
         */
        "dz" = "dz";

    
        /**
         * value: "ee"
         * @const
         */
        "ee" = "ee";

    
        /**
         * value: "el"
         * @const
         */
        "el" = "el";

    
        /**
         * value: "en"
         * @const
         */
        "en" = "en";

    
        /**
         * value: "eo"
         * @const
         */
        "eo" = "eo";

    
        /**
         * value: "es"
         * @const
         */
        "es" = "es";

    
        /**
         * value: "et"
         * @const
         */
        "et" = "et";

    
        /**
         * value: "eu"
         * @const
         */
        "eu" = "eu";

    
        /**
         * value: "fa"
         * @const
         */
        "fa" = "fa";

    
        /**
         * value: "ff"
         * @const
         */
        "ff" = "ff";

    
        /**
         * value: "fi"
         * @const
         */
        "fi" = "fi";

    
        /**
         * value: "fj"
         * @const
         */
        "fj" = "fj";

    
        /**
         * value: "fo"
         * @const
         */
        "fo" = "fo";

    
        /**
         * value: "fr"
         * @const
         */
        "fr" = "fr";

    
        /**
         * value: "fy"
         * @const
         */
        "fy" = "fy";

    
        /**
         * value: "ga"
         * @const
         */
        "ga" = "ga";

    
        /**
         * value: "gd"
         * @const
         */
        "gd" = "gd";

    
        /**
         * value: "gl"
         * @const
         */
        "gl" = "gl";

    
        /**
         * value: "gn"
         * @const
         */
        "gn" = "gn";

    
        /**
         * value: "gu"
         * @const
         */
        "gu" = "gu";

    
        /**
         * value: "gv"
         * @const
         */
        "gv" = "gv";

    
        /**
         * value: "ha"
         * @const
         */
        "ha" = "ha";

    
        /**
         * value: "he"
         * @const
         */
        "he" = "he";

    
        /**
         * value: "hi"
         * @const
         */
        "hi" = "hi";

    
        /**
         * value: "ho"
         * @const
         */
        "ho" = "ho";

    
        /**
         * value: "hr"
         * @const
         */
        "hr" = "hr";

    
        /**
         * value: "ht"
         * @const
         */
        "ht" = "ht";

    
        /**
         * value: "hu"
         * @const
         */
        "hu" = "hu";

    
        /**
         * value: "hy"
         * @const
         */
        "hy" = "hy";

    
        /**
         * value: "hz"
         * @const
         */
        "hz" = "hz";

    
        /**
         * value: "ia"
         * @const
         */
        "ia" = "ia";

    
        /**
         * value: "id"
         * @const
         */
        "id" = "id";

    
        /**
         * value: "ie"
         * @const
         */
        "ie" = "ie";

    
        /**
         * value: "ig"
         * @const
         */
        "ig" = "ig";

    
        /**
         * value: "ii"
         * @const
         */
        "ii" = "ii";

    
        /**
         * value: "ik"
         * @const
         */
        "ik" = "ik";

    
        /**
         * value: "io"
         * @const
         */
        "io" = "io";

    
        /**
         * value: "is"
         * @const
         */
        "is" = "is";

    
        /**
         * value: "it"
         * @const
         */
        "it" = "it";

    
        /**
         * value: "iu"
         * @const
         */
        "iu" = "iu";

    
        /**
         * value: "ja"
         * @const
         */
        "ja" = "ja";

    
        /**
         * value: "jv"
         * @const
         */
        "jv" = "jv";

    
        /**
         * value: "ka"
         * @const
         */
        "ka" = "ka";

    
        /**
         * value: "kg"
         * @const
         */
        "kg" = "kg";

    
        /**
         * value: "ki"
         * @const
         */
        "ki" = "ki";

    
        /**
         * value: "kj"
         * @const
         */
        "kj" = "kj";

    
        /**
         * value: "kk"
         * @const
         */
        "kk" = "kk";

    
        /**
         * value: "kl"
         * @const
         */
        "kl" = "kl";

    
        /**
         * value: "km"
         * @const
         */
        "km" = "km";

    
        /**
         * value: "kn"
         * @const
         */
        "kn" = "kn";

    
        /**
         * value: "ko"
         * @const
         */
        "ko" = "ko";

    
        /**
         * value: "kr"
         * @const
         */
        "kr" = "kr";

    
        /**
         * value: "ks"
         * @const
         */
        "ks" = "ks";

    
        /**
         * value: "ku"
         * @const
         */
        "ku" = "ku";

    
        /**
         * value: "kv"
         * @const
         */
        "kv" = "kv";

    
        /**
         * value: "kw"
         * @const
         */
        "kw" = "kw";

    
        /**
         * value: "ky"
         * @const
         */
        "ky" = "ky";

    
        /**
         * value: "la"
         * @const
         */
        "la" = "la";

    
        /**
         * value: "lb"
         * @const
         */
        "lb" = "lb";

    
        /**
         * value: "lg"
         * @const
         */
        "lg" = "lg";

    
        /**
         * value: "li"
         * @const
         */
        "li" = "li";

    
        /**
         * value: "ln"
         * @const
         */
        "ln" = "ln";

    
        /**
         * value: "lo"
         * @const
         */
        "lo" = "lo";

    
        /**
         * value: "lt"
         * @const
         */
        "lt" = "lt";

    
        /**
         * value: "lu"
         * @const
         */
        "lu" = "lu";

    
        /**
         * value: "lv"
         * @const
         */
        "lv" = "lv";

    
        /**
         * value: "mg"
         * @const
         */
        "mg" = "mg";

    
        /**
         * value: "mh"
         * @const
         */
        "mh" = "mh";

    
        /**
         * value: "mi"
         * @const
         */
        "mi" = "mi";

    
        /**
         * value: "mk"
         * @const
         */
        "mk" = "mk";

    
        /**
         * value: "ml"
         * @const
         */
        "ml" = "ml";

    
        /**
         * value: "mn"
         * @const
         */
        "mn" = "mn";

    
        /**
         * value: "mr"
         * @const
         */
        "mr" = "mr";

    
        /**
         * value: "ms"
         * @const
         */
        "ms" = "ms";

    
        /**
         * value: "mt"
         * @const
         */
        "mt" = "mt";

    
        /**
         * value: "my"
         * @const
         */
        "my" = "my";

    
        /**
         * value: "na"
         * @const
         */
        "na" = "na";

    
        /**
         * value: "nb"
         * @const
         */
        "nb" = "nb";

    
        /**
         * value: "nd"
         * @const
         */
        "nd" = "nd";

    
        /**
         * value: "ne"
         * @const
         */
        "ne" = "ne";

    
        /**
         * value: "ng"
         * @const
         */
        "ng" = "ng";

    
        /**
         * value: "nl"
         * @const
         */
        "nl" = "nl";

    
        /**
         * value: "nn"
         * @const
         */
        "nn" = "nn";

    
        /**
         * value: "false"
         * @const
         */
        "false" = "false";

    
        /**
         * value: "nr"
         * @const
         */
        "nr" = "nr";

    
        /**
         * value: "nv"
         * @const
         */
        "nv" = "nv";

    
        /**
         * value: "ny"
         * @const
         */
        "ny" = "ny";

    
        /**
         * value: "oc"
         * @const
         */
        "oc" = "oc";

    
        /**
         * value: "oj"
         * @const
         */
        "oj" = "oj";

    
        /**
         * value: "om"
         * @const
         */
        "om" = "om";

    
        /**
         * value: "or"
         * @const
         */
        "or" = "or";

    
        /**
         * value: "os"
         * @const
         */
        "os" = "os";

    
        /**
         * value: "pa"
         * @const
         */
        "pa" = "pa";

    
        /**
         * value: "pi"
         * @const
         */
        "pi" = "pi";

    
        /**
         * value: "pl"
         * @const
         */
        "pl" = "pl";

    
        /**
         * value: "ps"
         * @const
         */
        "ps" = "ps";

    
        /**
         * value: "pt"
         * @const
         */
        "pt" = "pt";

    
        /**
         * value: "qu"
         * @const
         */
        "qu" = "qu";

    
        /**
         * value: "rm"
         * @const
         */
        "rm" = "rm";

    
        /**
         * value: "rn"
         * @const
         */
        "rn" = "rn";

    
        /**
         * value: "ro"
         * @const
         */
        "ro" = "ro";

    
        /**
         * value: "ru"
         * @const
         */
        "ru" = "ru";

    
        /**
         * value: "rw"
         * @const
         */
        "rw" = "rw";

    
        /**
         * value: "sa"
         * @const
         */
        "sa" = "sa";

    
        /**
         * value: "sc"
         * @const
         */
        "sc" = "sc";

    
        /**
         * value: "sd"
         * @const
         */
        "sd" = "sd";

    
        /**
         * value: "se"
         * @const
         */
        "se" = "se";

    
        /**
         * value: "sg"
         * @const
         */
        "sg" = "sg";

    
        /**
         * value: "si"
         * @const
         */
        "si" = "si";

    
        /**
         * value: "sk"
         * @const
         */
        "sk" = "sk";

    
        /**
         * value: "sl"
         * @const
         */
        "sl" = "sl";

    
        /**
         * value: "sm"
         * @const
         */
        "sm" = "sm";

    
        /**
         * value: "sn"
         * @const
         */
        "sn" = "sn";

    
        /**
         * value: "so"
         * @const
         */
        "so" = "so";

    
        /**
         * value: "sq"
         * @const
         */
        "sq" = "sq";

    
        /**
         * value: "sr"
         * @const
         */
        "sr" = "sr";

    
        /**
         * value: "ss"
         * @const
         */
        "ss" = "ss";

    
        /**
         * value: "st"
         * @const
         */
        "st" = "st";

    
        /**
         * value: "su"
         * @const
         */
        "su" = "su";

    
        /**
         * value: "sv"
         * @const
         */
        "sv" = "sv";

    
        /**
         * value: "sw"
         * @const
         */
        "sw" = "sw";

    
        /**
         * value: "ta"
         * @const
         */
        "ta" = "ta";

    
        /**
         * value: "te"
         * @const
         */
        "te" = "te";

    
        /**
         * value: "tg"
         * @const
         */
        "tg" = "tg";

    
        /**
         * value: "th"
         * @const
         */
        "th" = "th";

    
        /**
         * value: "ti"
         * @const
         */
        "ti" = "ti";

    
        /**
         * value: "tk"
         * @const
         */
        "tk" = "tk";

    
        /**
         * value: "tl"
         * @const
         */
        "tl" = "tl";

    
        /**
         * value: "tn"
         * @const
         */
        "tn" = "tn";

    
        /**
         * value: "to"
         * @const
         */
        "to" = "to";

    
        /**
         * value: "tr"
         * @const
         */
        "tr" = "tr";

    
        /**
         * value: "ts"
         * @const
         */
        "ts" = "ts";

    
        /**
         * value: "tt"
         * @const
         */
        "tt" = "tt";

    
        /**
         * value: "tw"
         * @const
         */
        "tw" = "tw";

    
        /**
         * value: "ty"
         * @const
         */
        "ty" = "ty";

    
        /**
         * value: "ug"
         * @const
         */
        "ug" = "ug";

    
        /**
         * value: "uk"
         * @const
         */
        "uk" = "uk";

    
        /**
         * value: "ur"
         * @const
         */
        "ur" = "ur";

    
        /**
         * value: "uz"
         * @const
         */
        "uz" = "uz";

    
        /**
         * value: "ve"
         * @const
         */
        "ve" = "ve";

    
        /**
         * value: "vi"
         * @const
         */
        "vi" = "vi";

    
        /**
         * value: "vo"
         * @const
         */
        "vo" = "vo";

    
        /**
         * value: "wa"
         * @const
         */
        "wa" = "wa";

    
        /**
         * value: "wo"
         * @const
         */
        "wo" = "wo";

    
        /**
         * value: "xh"
         * @const
         */
        "xh" = "xh";

    
        /**
         * value: "yi"
         * @const
         */
        "yi" = "yi";

    
        /**
         * value: "yo"
         * @const
         */
        "yo" = "yo";

    
        /**
         * value: "za"
         * @const
         */
        "za" = "za";

    
        /**
         * value: "zh"
         * @const
         */
        "zh" = "zh";

    
        /**
         * value: "zu"
         * @const
         */
        "zu" = "zu";

    

    /**
    * Returns a <code>StreamLanguage</code> enum value from a Javascript object name.
    * @param {Object} data The plain JavaScript object containing the name of the enum value.
    * @return {module:model/StreamLanguage} The enum <code>StreamLanguage</code> value.
    */
    static constructFromObject(object) {
        return object;
    }
}

