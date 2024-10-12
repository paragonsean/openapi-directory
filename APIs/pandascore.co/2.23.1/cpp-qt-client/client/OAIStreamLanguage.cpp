/**
 * PandaScore REST API for All Videogames
 *  # Introduction  Whether you're looking to build an official Pandascore integration for your service, or you just want to build something awesome, [we can help you get started](/home).  The API works over the HTTPS protocol, and is accessed from the `api.pandascore.co` domain.  - The current endpoint is [https://api.pandascore.co](https://api.pandascore.co). - All data is sent and received as JSON by default. - Blank fields are included with `null` values instead of being omitted. - All timestamps are returned in ISO-8601 format  ### About this documentation  Clicking on a query parameter like `filter` or `search` will show you the available options: ![filter](/doc/images/query_param_details.jpg)  You can also click on a response to see the detailed response schema: ![response](/doc/images/response_schema.jpg)  ## Events hierarchy  The PandaScore API allows you to access data about eSports events by using a certain structure detailed below.  **Leagues**  Leagues are the top level events. They don't have a date and represent a regular competition. A League is composed of one or several series.   Some League of Legends leagues are: _EU LCS, NA LCS, LCK, etc._   Some Dota 2 leagues are: _ESL One, GESC, The International, PGL, etc._  **Series**  A Serie represents an occurrence of a league event.   The EU LCS league has two series per year: _spring 2017, summer 2017, spring 2016, summer 2016 etc._   Some Dota2 Series examples would be: _Changsha Major, Open Bucharest, Frankfurt, i-League Invitational etc._  **Tournaments**  Tournaments groups all the matches of a serie under \"stages\" and \"groups\".   The tournaments of the EU LCS of summer 2017 are: _Group A, Group B, Playoffs, etc._   Some Dota 2 tournaments are: _Group A, Group B, Playoffs, etc._  **Matches**  Finally we have matches which have two players or teams (depending on the played videogame) and several games (the rounds of the match).   Matches of the group A in the EU LCS of summer 2017 are: _G2 vs FNC, MSF vs NIP, etc._   Matches of the group A in the ESL One, Genting tournamnet are: _Lower Round 1, Quarterfinal, Upper Final, etc._    **Please note that some matches may be listed as \"TBD vs TBD\" if the matchup is not announced yet, for example the date of the Final match is known but the quarterfinal is still being played.**   ![Structure](/doc/images/structure.png)  ## Formats  &lt;!-- The API currently supports the JSON format by default, as well as the XML format. Add the desired extension to your request URL in order to get that format. --&gt; The API currently supports the JSON format by default.  Other formats may be added depending on user needs.  ## Pagination  The Pandascore API paginates all resources on the index method.  Requests that return multiple items will be paginated to 50 items by default. You can specify further pages with the `page[number]` parameter. You can also set a custom page size (up to 100) with the `page[size]` parameter.  The `Link` HTTP response header contains pagination data with `first`, `previous`, `next` and `last` raw page links when available, under the format  ``` Link: &lt;https://api.pandascore.co/{Resource}?page=X+1&gt;; rel=\"next\", &lt;https://api.pandascore.co/{Resource}?page=X-1&gt;; rel=\"prev\", &lt;https://api.pandascore.co/{Resource}?page=1&gt;; rel=\"first\", &lt;https://api.pandascore.co/{Resource}?page=X+n&gt;; rel=\"last\" ```  There is also:  * A `X-Page` header field, which contains the current page. * A `X-Per-Page` header field, which contains the current pagination length. * A `X-Total` header field, which contains the total count of items across all pages.  ## Filtering  The `filter` query parameter can be used to filter a collection by one or several fields for one or several values. The `filter` parameter takes the field to filter as a key, and the values to filter as the value. Multiples values must be comma-separated (`,`).  For example, the following is a request for all the champions with a name matching Twitch or Brand exactly, but only with 21 armor:  ``` GET /lol/champions?filter[name]=Brand,Twitch&amp;filter[armor]=21&amp;token=YOUR_ACCESS_TOKEN ```  ## Range  The `range` parameter is a hash that allows filtering fields by an interval. Only values between the given two comma-separated bounds will be returned. The bounds are inclusive.  For example, the following is a request for all the champions with `hp` within 500 and 1000:  ``` GET /lol/champions?range[hp]=500,1000&amp;token=YOUR_ACCESS_TOKEN ```  ## Search  The `search` parameter is a bit like the `filter` parameter, but it will return all results where the values **contain** the given parameter.  Note: this only works on strings. Searching with integer values is not supported and `filter` or `range` parameters may be better suited for your needs here.  For example, to get all the champions with a name containing `\"twi\"`:  ``` $ curl -sg -H 'Authorization: Bearer YOUR_ACCESS_TOKEN' 'https://api.pandascore.co/lol/champions?search[name]=twi' | jq -S '.[].name' \"Twitch\" \"Twisted Fate\" ```  ## Sorting  All index endpoints support multiple sort fields with comma-separation (`,`); the fields are applied in the order specified.  The sort order for each field is ascending unless it is prefixed with a minus (U+002D HYPHEN-MINUS, “-“), in which case it is descending.  For example, `GET /lol/champions?sort=attackdamage,-name&amp;token=YOUR_ACCESS_TOKEN` will return all the champions sorted by attack damage. Any champions with the same attack damage will then be sorted by their names in descending alphabetical order.  ## Rate limiting  Depending on your current plan, you will have a different rate limit. Your plan and your current request count [are available on your dashboard](https://pandascore.co/settings).  With the **free plan**, you have a limit of 1000 requests per hour, others plans have a limit of 4000 requests per hour. The number of remaining requests is available in the `X-Rate-Limit-Remaining` response header.  Your API key is included in all the examples on this page, so you can test any example right away. **Only you can see this value.**  # Authentication  The authentication on the Pandascore API works with access tokens.  All developers need to [create an account](https://pandascore.co/users/sign_in) before getting started, in order to get an access token. The access token should not be shared.  **Your token can be found and regenerated from [your dashboard](https://pandascore.co/settings).**  The access token can be passed in the URL with the `token` query string parameter, or in the `Authorization: Bearer` header field.  &lt;!-- ReDoc-Inject: &lt;security-definitions&gt; --&gt; 
 *
 * The version of the OpenAPI document: 2.23.1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIStreamLanguage.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIStreamLanguage::OAIStreamLanguage(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIStreamLanguage::OAIStreamLanguage() {
    this->initializeModel();
}

OAIStreamLanguage::~OAIStreamLanguage() {}

void OAIStreamLanguage::initializeModel() {

    m_value_isSet = false;
    m_value_isValid = false;
    m_value = eOAIStreamLanguage::INVALID_VALUE_OPENAPI_GENERATED;
}

void OAIStreamLanguage::fromJson(QString jsonString) {
    
    if ( jsonString.compare("aa", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::AA;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("ab", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::AB;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("ae", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::AE;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("af", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::AF;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("ak", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::AK;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("am", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::AM;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("an", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::AN;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("ar", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::AR;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("as", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::AS;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("av", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::AV;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("ay", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::AY;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("az", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::AZ;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("ba", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::BA;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("be", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::BE;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("bg", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::BG;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("bh", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::BH;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("bi", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::BI;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("bm", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::BM;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("bn", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::BN;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("bo", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::BO;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("br", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::BR;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("bs", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::BS;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("ca", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::CA;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("ce", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::CE;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("ch", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::CH;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("co", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::CO;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("cr", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::CR;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("cs", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::CS;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("cu", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::CU;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("cv", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::CV;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("cy", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::CY;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("da", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::DA;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("de", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::DE;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("dv", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::DV;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("dz", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::DZ;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("ee", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::EE;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("el", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::EL;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("en", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::EN;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("eo", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::EO;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("es", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::ES;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("et", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::ET;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("eu", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::EU;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("fa", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::FA;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("ff", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::FF;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("fi", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::FI;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("fj", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::FJ;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("fo", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::FO;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("fr", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::FR;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("fy", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::FY;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("ga", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::GA;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("gd", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::GD;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("gl", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::GL;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("gn", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::GN;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("gu", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::GU;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("gv", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::GV;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("ha", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::HA;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("he", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::HE;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("hi", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::HI;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("ho", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::HO;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("hr", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::HR;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("ht", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::HT;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("hu", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::HU;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("hy", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::HY;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("hz", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::HZ;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("ia", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::IA;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("id", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::ID;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("ie", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::IE;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("ig", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::IG;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("ii", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::II;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("ik", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::IK;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("io", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::IO;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("is", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::IS;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("it", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::IT;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("iu", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::IU;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("ja", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::JA;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("jv", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::JV;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("ka", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::KA;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("kg", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::KG;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("ki", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::KI;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("kj", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::KJ;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("kk", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::KK;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("kl", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::KL;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("km", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::KM;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("kn", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::KN;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("ko", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::KO;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("kr", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::KR;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("ks", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::KS;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("ku", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::KU;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("kv", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::KV;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("kw", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::KW;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("ky", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::KY;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("la", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::LA;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("lb", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::LB;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("lg", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::LG;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("li", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::LI;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("ln", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::LN;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("lo", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::LO;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("lt", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::LT;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("lu", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::LU;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("lv", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::LV;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("mg", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::MG;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("mh", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::MH;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("mi", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::MI;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("mk", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::MK;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("ml", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::ML;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("mn", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::MN;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("mr", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::MR;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("ms", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::MS;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("mt", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::MT;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("my", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::MY;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("na", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::NA;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("nb", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::NB;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("nd", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::ND;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("ne", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::NE;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("ng", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::NG;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("nl", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::NL;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("nn", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::NN;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("false", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::FALSE;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("nr", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::NR;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("nv", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::NV;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("ny", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::NY;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("oc", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::OC;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("oj", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::OJ;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("om", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::OM;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("or", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::OR;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("os", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::OS;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("pa", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::PA;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("pi", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::PI;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("pl", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::PL;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("ps", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::PS;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("pt", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::PT;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("qu", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::QU;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("rm", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::RM;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("rn", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::RN;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("ro", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::RO;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("ru", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::RU;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("rw", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::RW;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("sa", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::SA;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("sc", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::SC;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("sd", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::SD;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("se", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::SE;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("sg", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::SG;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("si", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::SI;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("sk", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::SK;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("sl", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::SL;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("sm", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::SM;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("sn", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::SN;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("so", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::SO;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("sq", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::SQ;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("sr", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::SR;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("ss", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::SS;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("st", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::ST;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("su", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::SU;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("sv", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::SV;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("sw", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::SW;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("ta", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::TA;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("te", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::TE;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("tg", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::TG;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("th", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::TH;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("ti", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::TI;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("tk", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::TK;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("tl", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::TL;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("tn", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::TN;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("to", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::TO;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("tr", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::TR;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("ts", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::TS;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("tt", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::TT;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("tw", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::TW;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("ty", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::TY;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("ug", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::UG;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("uk", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::UK;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("ur", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::UR;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("uz", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::UZ;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("ve", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::VE;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("vi", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::VI;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("vo", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::VO;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("wa", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::WA;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("wo", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::WO;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("xh", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::XH;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("yi", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::YI;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("yo", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::YO;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("za", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::ZA;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("zh", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::ZH;
        m_value_isSet = m_value_isValid = true;
    }
    else if ( jsonString.compare("zu", Qt::CaseInsensitive) == 0) {
        m_value = eOAIStreamLanguage::ZU;
        m_value_isSet = m_value_isValid = true;
    }
}

void OAIStreamLanguage::fromJsonValue(QJsonValue json) {
fromJson(json.toString());
}

QString OAIStreamLanguage::asJson() const {
    
    QString val;
    switch (m_value){
        case eOAIStreamLanguage::AA:
            val = "aa";
            break;
        case eOAIStreamLanguage::AB:
            val = "ab";
            break;
        case eOAIStreamLanguage::AE:
            val = "ae";
            break;
        case eOAIStreamLanguage::AF:
            val = "af";
            break;
        case eOAIStreamLanguage::AK:
            val = "ak";
            break;
        case eOAIStreamLanguage::AM:
            val = "am";
            break;
        case eOAIStreamLanguage::AN:
            val = "an";
            break;
        case eOAIStreamLanguage::AR:
            val = "ar";
            break;
        case eOAIStreamLanguage::AS:
            val = "as";
            break;
        case eOAIStreamLanguage::AV:
            val = "av";
            break;
        case eOAIStreamLanguage::AY:
            val = "ay";
            break;
        case eOAIStreamLanguage::AZ:
            val = "az";
            break;
        case eOAIStreamLanguage::BA:
            val = "ba";
            break;
        case eOAIStreamLanguage::BE:
            val = "be";
            break;
        case eOAIStreamLanguage::BG:
            val = "bg";
            break;
        case eOAIStreamLanguage::BH:
            val = "bh";
            break;
        case eOAIStreamLanguage::BI:
            val = "bi";
            break;
        case eOAIStreamLanguage::BM:
            val = "bm";
            break;
        case eOAIStreamLanguage::BN:
            val = "bn";
            break;
        case eOAIStreamLanguage::BO:
            val = "bo";
            break;
        case eOAIStreamLanguage::BR:
            val = "br";
            break;
        case eOAIStreamLanguage::BS:
            val = "bs";
            break;
        case eOAIStreamLanguage::CA:
            val = "ca";
            break;
        case eOAIStreamLanguage::CE:
            val = "ce";
            break;
        case eOAIStreamLanguage::CH:
            val = "ch";
            break;
        case eOAIStreamLanguage::CO:
            val = "co";
            break;
        case eOAIStreamLanguage::CR:
            val = "cr";
            break;
        case eOAIStreamLanguage::CS:
            val = "cs";
            break;
        case eOAIStreamLanguage::CU:
            val = "cu";
            break;
        case eOAIStreamLanguage::CV:
            val = "cv";
            break;
        case eOAIStreamLanguage::CY:
            val = "cy";
            break;
        case eOAIStreamLanguage::DA:
            val = "da";
            break;
        case eOAIStreamLanguage::DE:
            val = "de";
            break;
        case eOAIStreamLanguage::DV:
            val = "dv";
            break;
        case eOAIStreamLanguage::DZ:
            val = "dz";
            break;
        case eOAIStreamLanguage::EE:
            val = "ee";
            break;
        case eOAIStreamLanguage::EL:
            val = "el";
            break;
        case eOAIStreamLanguage::EN:
            val = "en";
            break;
        case eOAIStreamLanguage::EO:
            val = "eo";
            break;
        case eOAIStreamLanguage::ES:
            val = "es";
            break;
        case eOAIStreamLanguage::ET:
            val = "et";
            break;
        case eOAIStreamLanguage::EU:
            val = "eu";
            break;
        case eOAIStreamLanguage::FA:
            val = "fa";
            break;
        case eOAIStreamLanguage::FF:
            val = "ff";
            break;
        case eOAIStreamLanguage::FI:
            val = "fi";
            break;
        case eOAIStreamLanguage::FJ:
            val = "fj";
            break;
        case eOAIStreamLanguage::FO:
            val = "fo";
            break;
        case eOAIStreamLanguage::FR:
            val = "fr";
            break;
        case eOAIStreamLanguage::FY:
            val = "fy";
            break;
        case eOAIStreamLanguage::GA:
            val = "ga";
            break;
        case eOAIStreamLanguage::GD:
            val = "gd";
            break;
        case eOAIStreamLanguage::GL:
            val = "gl";
            break;
        case eOAIStreamLanguage::GN:
            val = "gn";
            break;
        case eOAIStreamLanguage::GU:
            val = "gu";
            break;
        case eOAIStreamLanguage::GV:
            val = "gv";
            break;
        case eOAIStreamLanguage::HA:
            val = "ha";
            break;
        case eOAIStreamLanguage::HE:
            val = "he";
            break;
        case eOAIStreamLanguage::HI:
            val = "hi";
            break;
        case eOAIStreamLanguage::HO:
            val = "ho";
            break;
        case eOAIStreamLanguage::HR:
            val = "hr";
            break;
        case eOAIStreamLanguage::HT:
            val = "ht";
            break;
        case eOAIStreamLanguage::HU:
            val = "hu";
            break;
        case eOAIStreamLanguage::HY:
            val = "hy";
            break;
        case eOAIStreamLanguage::HZ:
            val = "hz";
            break;
        case eOAIStreamLanguage::IA:
            val = "ia";
            break;
        case eOAIStreamLanguage::ID:
            val = "id";
            break;
        case eOAIStreamLanguage::IE:
            val = "ie";
            break;
        case eOAIStreamLanguage::IG:
            val = "ig";
            break;
        case eOAIStreamLanguage::II:
            val = "ii";
            break;
        case eOAIStreamLanguage::IK:
            val = "ik";
            break;
        case eOAIStreamLanguage::IO:
            val = "io";
            break;
        case eOAIStreamLanguage::IS:
            val = "is";
            break;
        case eOAIStreamLanguage::IT:
            val = "it";
            break;
        case eOAIStreamLanguage::IU:
            val = "iu";
            break;
        case eOAIStreamLanguage::JA:
            val = "ja";
            break;
        case eOAIStreamLanguage::JV:
            val = "jv";
            break;
        case eOAIStreamLanguage::KA:
            val = "ka";
            break;
        case eOAIStreamLanguage::KG:
            val = "kg";
            break;
        case eOAIStreamLanguage::KI:
            val = "ki";
            break;
        case eOAIStreamLanguage::KJ:
            val = "kj";
            break;
        case eOAIStreamLanguage::KK:
            val = "kk";
            break;
        case eOAIStreamLanguage::KL:
            val = "kl";
            break;
        case eOAIStreamLanguage::KM:
            val = "km";
            break;
        case eOAIStreamLanguage::KN:
            val = "kn";
            break;
        case eOAIStreamLanguage::KO:
            val = "ko";
            break;
        case eOAIStreamLanguage::KR:
            val = "kr";
            break;
        case eOAIStreamLanguage::KS:
            val = "ks";
            break;
        case eOAIStreamLanguage::KU:
            val = "ku";
            break;
        case eOAIStreamLanguage::KV:
            val = "kv";
            break;
        case eOAIStreamLanguage::KW:
            val = "kw";
            break;
        case eOAIStreamLanguage::KY:
            val = "ky";
            break;
        case eOAIStreamLanguage::LA:
            val = "la";
            break;
        case eOAIStreamLanguage::LB:
            val = "lb";
            break;
        case eOAIStreamLanguage::LG:
            val = "lg";
            break;
        case eOAIStreamLanguage::LI:
            val = "li";
            break;
        case eOAIStreamLanguage::LN:
            val = "ln";
            break;
        case eOAIStreamLanguage::LO:
            val = "lo";
            break;
        case eOAIStreamLanguage::LT:
            val = "lt";
            break;
        case eOAIStreamLanguage::LU:
            val = "lu";
            break;
        case eOAIStreamLanguage::LV:
            val = "lv";
            break;
        case eOAIStreamLanguage::MG:
            val = "mg";
            break;
        case eOAIStreamLanguage::MH:
            val = "mh";
            break;
        case eOAIStreamLanguage::MI:
            val = "mi";
            break;
        case eOAIStreamLanguage::MK:
            val = "mk";
            break;
        case eOAIStreamLanguage::ML:
            val = "ml";
            break;
        case eOAIStreamLanguage::MN:
            val = "mn";
            break;
        case eOAIStreamLanguage::MR:
            val = "mr";
            break;
        case eOAIStreamLanguage::MS:
            val = "ms";
            break;
        case eOAIStreamLanguage::MT:
            val = "mt";
            break;
        case eOAIStreamLanguage::MY:
            val = "my";
            break;
        case eOAIStreamLanguage::NA:
            val = "na";
            break;
        case eOAIStreamLanguage::NB:
            val = "nb";
            break;
        case eOAIStreamLanguage::ND:
            val = "nd";
            break;
        case eOAIStreamLanguage::NE:
            val = "ne";
            break;
        case eOAIStreamLanguage::NG:
            val = "ng";
            break;
        case eOAIStreamLanguage::NL:
            val = "nl";
            break;
        case eOAIStreamLanguage::NN:
            val = "nn";
            break;
        case eOAIStreamLanguage::FALSE:
            val = "false";
            break;
        case eOAIStreamLanguage::NR:
            val = "nr";
            break;
        case eOAIStreamLanguage::NV:
            val = "nv";
            break;
        case eOAIStreamLanguage::NY:
            val = "ny";
            break;
        case eOAIStreamLanguage::OC:
            val = "oc";
            break;
        case eOAIStreamLanguage::OJ:
            val = "oj";
            break;
        case eOAIStreamLanguage::OM:
            val = "om";
            break;
        case eOAIStreamLanguage::OR:
            val = "or";
            break;
        case eOAIStreamLanguage::OS:
            val = "os";
            break;
        case eOAIStreamLanguage::PA:
            val = "pa";
            break;
        case eOAIStreamLanguage::PI:
            val = "pi";
            break;
        case eOAIStreamLanguage::PL:
            val = "pl";
            break;
        case eOAIStreamLanguage::PS:
            val = "ps";
            break;
        case eOAIStreamLanguage::PT:
            val = "pt";
            break;
        case eOAIStreamLanguage::QU:
            val = "qu";
            break;
        case eOAIStreamLanguage::RM:
            val = "rm";
            break;
        case eOAIStreamLanguage::RN:
            val = "rn";
            break;
        case eOAIStreamLanguage::RO:
            val = "ro";
            break;
        case eOAIStreamLanguage::RU:
            val = "ru";
            break;
        case eOAIStreamLanguage::RW:
            val = "rw";
            break;
        case eOAIStreamLanguage::SA:
            val = "sa";
            break;
        case eOAIStreamLanguage::SC:
            val = "sc";
            break;
        case eOAIStreamLanguage::SD:
            val = "sd";
            break;
        case eOAIStreamLanguage::SE:
            val = "se";
            break;
        case eOAIStreamLanguage::SG:
            val = "sg";
            break;
        case eOAIStreamLanguage::SI:
            val = "si";
            break;
        case eOAIStreamLanguage::SK:
            val = "sk";
            break;
        case eOAIStreamLanguage::SL:
            val = "sl";
            break;
        case eOAIStreamLanguage::SM:
            val = "sm";
            break;
        case eOAIStreamLanguage::SN:
            val = "sn";
            break;
        case eOAIStreamLanguage::SO:
            val = "so";
            break;
        case eOAIStreamLanguage::SQ:
            val = "sq";
            break;
        case eOAIStreamLanguage::SR:
            val = "sr";
            break;
        case eOAIStreamLanguage::SS:
            val = "ss";
            break;
        case eOAIStreamLanguage::ST:
            val = "st";
            break;
        case eOAIStreamLanguage::SU:
            val = "su";
            break;
        case eOAIStreamLanguage::SV:
            val = "sv";
            break;
        case eOAIStreamLanguage::SW:
            val = "sw";
            break;
        case eOAIStreamLanguage::TA:
            val = "ta";
            break;
        case eOAIStreamLanguage::TE:
            val = "te";
            break;
        case eOAIStreamLanguage::TG:
            val = "tg";
            break;
        case eOAIStreamLanguage::TH:
            val = "th";
            break;
        case eOAIStreamLanguage::TI:
            val = "ti";
            break;
        case eOAIStreamLanguage::TK:
            val = "tk";
            break;
        case eOAIStreamLanguage::TL:
            val = "tl";
            break;
        case eOAIStreamLanguage::TN:
            val = "tn";
            break;
        case eOAIStreamLanguage::TO:
            val = "to";
            break;
        case eOAIStreamLanguage::TR:
            val = "tr";
            break;
        case eOAIStreamLanguage::TS:
            val = "ts";
            break;
        case eOAIStreamLanguage::TT:
            val = "tt";
            break;
        case eOAIStreamLanguage::TW:
            val = "tw";
            break;
        case eOAIStreamLanguage::TY:
            val = "ty";
            break;
        case eOAIStreamLanguage::UG:
            val = "ug";
            break;
        case eOAIStreamLanguage::UK:
            val = "uk";
            break;
        case eOAIStreamLanguage::UR:
            val = "ur";
            break;
        case eOAIStreamLanguage::UZ:
            val = "uz";
            break;
        case eOAIStreamLanguage::VE:
            val = "ve";
            break;
        case eOAIStreamLanguage::VI:
            val = "vi";
            break;
        case eOAIStreamLanguage::VO:
            val = "vo";
            break;
        case eOAIStreamLanguage::WA:
            val = "wa";
            break;
        case eOAIStreamLanguage::WO:
            val = "wo";
            break;
        case eOAIStreamLanguage::XH:
            val = "xh";
            break;
        case eOAIStreamLanguage::YI:
            val = "yi";
            break;
        case eOAIStreamLanguage::YO:
            val = "yo";
            break;
        case eOAIStreamLanguage::ZA:
            val = "za";
            break;
        case eOAIStreamLanguage::ZH:
            val = "zh";
            break;
        case eOAIStreamLanguage::ZU:
            val = "zu";
            break;
        default:
            break;
    }
    return val;
}

QJsonValue OAIStreamLanguage::asJsonValue() const {
    
    return QJsonValue(asJson());
}


OAIStreamLanguage::eOAIStreamLanguage OAIStreamLanguage::getValue() const {
    return m_value;
}

void OAIStreamLanguage::setValue(const OAIStreamLanguage::eOAIStreamLanguage& value){
    m_value = value;
    m_value_isSet = true;
}
bool OAIStreamLanguage::isSet() const {
    
    return m_value_isSet;
}

bool OAIStreamLanguage::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_value_isValid;
}

} // namespace OpenAPI
