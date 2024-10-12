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

#include "OAIBettingSerie_1.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIBettingSerie_1::OAIBettingSerie_1(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIBettingSerie_1::OAIBettingSerie_1() {
    this->initializeModel();
}

OAIBettingSerie_1::~OAIBettingSerie_1() {}

void OAIBettingSerie_1::initializeModel() {

    m_begin_at_isSet = false;
    m_begin_at_isValid = false;

    m_description_isSet = false;
    m_description_isValid = false;

    m_end_at_isSet = false;
    m_end_at_isValid = false;

    m_full_name_isSet = false;
    m_full_name_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_league_id_isSet = false;
    m_league_id_isValid = false;

    m_league_image_url_isSet = false;
    m_league_image_url_isValid = false;

    m_league_name_isSet = false;
    m_league_name_isValid = false;

    m_modified_at_isSet = false;
    m_modified_at_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_season_isSet = false;
    m_season_isValid = false;

    m_slug_isSet = false;
    m_slug_isValid = false;

    m_tier_isSet = false;
    m_tier_isValid = false;

    m_videogame_isSet = false;
    m_videogame_isValid = false;

    m_winner_id_isSet = false;
    m_winner_id_isValid = false;

    m_winner_type_isSet = false;
    m_winner_type_isValid = false;

    m_year_isSet = false;
    m_year_isValid = false;
}

void OAIBettingSerie_1::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIBettingSerie_1::fromJsonObject(QJsonObject json) {

    m_begin_at_isValid = ::OpenAPI::fromJsonValue(m_begin_at, json[QString("begin_at")]);
    m_begin_at_isSet = !json[QString("begin_at")].isNull() && m_begin_at_isValid;

    m_description_isValid = ::OpenAPI::fromJsonValue(m_description, json[QString("description")]);
    m_description_isSet = !json[QString("description")].isNull() && m_description_isValid;

    m_end_at_isValid = ::OpenAPI::fromJsonValue(m_end_at, json[QString("end_at")]);
    m_end_at_isSet = !json[QString("end_at")].isNull() && m_end_at_isValid;

    m_full_name_isValid = ::OpenAPI::fromJsonValue(m_full_name, json[QString("full_name")]);
    m_full_name_isSet = !json[QString("full_name")].isNull() && m_full_name_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_league_id_isValid = ::OpenAPI::fromJsonValue(m_league_id, json[QString("league_id")]);
    m_league_id_isSet = !json[QString("league_id")].isNull() && m_league_id_isValid;

    m_league_image_url_isValid = ::OpenAPI::fromJsonValue(m_league_image_url, json[QString("league_image_url")]);
    m_league_image_url_isSet = !json[QString("league_image_url")].isNull() && m_league_image_url_isValid;

    m_league_name_isValid = ::OpenAPI::fromJsonValue(m_league_name, json[QString("league_name")]);
    m_league_name_isSet = !json[QString("league_name")].isNull() && m_league_name_isValid;

    m_modified_at_isValid = ::OpenAPI::fromJsonValue(m_modified_at, json[QString("modified_at")]);
    m_modified_at_isSet = !json[QString("modified_at")].isNull() && m_modified_at_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_season_isValid = ::OpenAPI::fromJsonValue(m_season, json[QString("season")]);
    m_season_isSet = !json[QString("season")].isNull() && m_season_isValid;

    m_slug_isValid = ::OpenAPI::fromJsonValue(m_slug, json[QString("slug")]);
    m_slug_isSet = !json[QString("slug")].isNull() && m_slug_isValid;

    m_tier_isValid = ::OpenAPI::fromJsonValue(m_tier, json[QString("tier")]);
    m_tier_isSet = !json[QString("tier")].isNull() && m_tier_isValid;

    m_videogame_isValid = ::OpenAPI::fromJsonValue(m_videogame, json[QString("videogame")]);
    m_videogame_isSet = !json[QString("videogame")].isNull() && m_videogame_isValid;

    m_winner_id_isValid = ::OpenAPI::fromJsonValue(m_winner_id, json[QString("winner_id")]);
    m_winner_id_isSet = !json[QString("winner_id")].isNull() && m_winner_id_isValid;

    m_winner_type_isValid = ::OpenAPI::fromJsonValue(m_winner_type, json[QString("winner_type")]);
    m_winner_type_isSet = !json[QString("winner_type")].isNull() && m_winner_type_isValid;

    m_year_isValid = ::OpenAPI::fromJsonValue(m_year, json[QString("year")]);
    m_year_isSet = !json[QString("year")].isNull() && m_year_isValid;
}

QString OAIBettingSerie_1::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIBettingSerie_1::asJsonObject() const {
    QJsonObject obj;
    if (m_begin_at.isSet()) {
        obj.insert(QString("begin_at"), ::OpenAPI::toJsonValue(m_begin_at));
    }
    if (m_description.isSet()) {
        obj.insert(QString("description"), ::OpenAPI::toJsonValue(m_description));
    }
    if (m_end_at.isSet()) {
        obj.insert(QString("end_at"), ::OpenAPI::toJsonValue(m_end_at));
    }
    if (m_full_name_isSet) {
        obj.insert(QString("full_name"), ::OpenAPI::toJsonValue(m_full_name));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_league_id_isSet) {
        obj.insert(QString("league_id"), ::OpenAPI::toJsonValue(m_league_id));
    }
    if (m_league_image_url.isSet()) {
        obj.insert(QString("league_image_url"), ::OpenAPI::toJsonValue(m_league_image_url));
    }
    if (m_league_name_isSet) {
        obj.insert(QString("league_name"), ::OpenAPI::toJsonValue(m_league_name));
    }
    if (m_modified_at_isSet) {
        obj.insert(QString("modified_at"), ::OpenAPI::toJsonValue(m_modified_at));
    }
    if (m_name.isSet()) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_season.isSet()) {
        obj.insert(QString("season"), ::OpenAPI::toJsonValue(m_season));
    }
    if (m_slug_isSet) {
        obj.insert(QString("slug"), ::OpenAPI::toJsonValue(m_slug));
    }
    if (m_tier.isSet()) {
        obj.insert(QString("tier"), ::OpenAPI::toJsonValue(m_tier));
    }
    if (m_videogame.isSet()) {
        obj.insert(QString("videogame"), ::OpenAPI::toJsonValue(m_videogame));
    }
    if (m_winner_id.isSet()) {
        obj.insert(QString("winner_id"), ::OpenAPI::toJsonValue(m_winner_id));
    }
    if (m_winner_type.isSet()) {
        obj.insert(QString("winner_type"), ::OpenAPI::toJsonValue(m_winner_type));
    }
    if (m_year_isSet) {
        obj.insert(QString("year"), ::OpenAPI::toJsonValue(m_year));
    }
    return obj;
}

OAIObject OAIBettingSerie_1::getBeginAt() const {
    return m_begin_at;
}
void OAIBettingSerie_1::setBeginAt(const OAIObject &begin_at) {
    m_begin_at = begin_at;
    m_begin_at_isSet = true;
}

bool OAIBettingSerie_1::is_begin_at_Set() const{
    return m_begin_at_isSet;
}

bool OAIBettingSerie_1::is_begin_at_Valid() const{
    return m_begin_at_isValid;
}

OAIObject OAIBettingSerie_1::getDescription() const {
    return m_description;
}
void OAIBettingSerie_1::setDescription(const OAIObject &description) {
    m_description = description;
    m_description_isSet = true;
}

bool OAIBettingSerie_1::is_description_Set() const{
    return m_description_isSet;
}

bool OAIBettingSerie_1::is_description_Valid() const{
    return m_description_isValid;
}

OAIObject OAIBettingSerie_1::getEndAt() const {
    return m_end_at;
}
void OAIBettingSerie_1::setEndAt(const OAIObject &end_at) {
    m_end_at = end_at;
    m_end_at_isSet = true;
}

bool OAIBettingSerie_1::is_end_at_Set() const{
    return m_end_at_isSet;
}

bool OAIBettingSerie_1::is_end_at_Valid() const{
    return m_end_at_isValid;
}

QString OAIBettingSerie_1::getFullName() const {
    return m_full_name;
}
void OAIBettingSerie_1::setFullName(const QString &full_name) {
    m_full_name = full_name;
    m_full_name_isSet = true;
}

bool OAIBettingSerie_1::is_full_name_Set() const{
    return m_full_name_isSet;
}

bool OAIBettingSerie_1::is_full_name_Valid() const{
    return m_full_name_isValid;
}

qint32 OAIBettingSerie_1::getId() const {
    return m_id;
}
void OAIBettingSerie_1::setId(const qint32 &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIBettingSerie_1::is_id_Set() const{
    return m_id_isSet;
}

bool OAIBettingSerie_1::is_id_Valid() const{
    return m_id_isValid;
}

qint32 OAIBettingSerie_1::getLeagueId() const {
    return m_league_id;
}
void OAIBettingSerie_1::setLeagueId(const qint32 &league_id) {
    m_league_id = league_id;
    m_league_id_isSet = true;
}

bool OAIBettingSerie_1::is_league_id_Set() const{
    return m_league_id_isSet;
}

bool OAIBettingSerie_1::is_league_id_Valid() const{
    return m_league_id_isValid;
}

OAIObject OAIBettingSerie_1::getLeagueImageUrl() const {
    return m_league_image_url;
}
void OAIBettingSerie_1::setLeagueImageUrl(const OAIObject &league_image_url) {
    m_league_image_url = league_image_url;
    m_league_image_url_isSet = true;
}

bool OAIBettingSerie_1::is_league_image_url_Set() const{
    return m_league_image_url_isSet;
}

bool OAIBettingSerie_1::is_league_image_url_Valid() const{
    return m_league_image_url_isValid;
}

QString OAIBettingSerie_1::getLeagueName() const {
    return m_league_name;
}
void OAIBettingSerie_1::setLeagueName(const QString &league_name) {
    m_league_name = league_name;
    m_league_name_isSet = true;
}

bool OAIBettingSerie_1::is_league_name_Set() const{
    return m_league_name_isSet;
}

bool OAIBettingSerie_1::is_league_name_Valid() const{
    return m_league_name_isValid;
}

QDateTime OAIBettingSerie_1::getModifiedAt() const {
    return m_modified_at;
}
void OAIBettingSerie_1::setModifiedAt(const QDateTime &modified_at) {
    m_modified_at = modified_at;
    m_modified_at_isSet = true;
}

bool OAIBettingSerie_1::is_modified_at_Set() const{
    return m_modified_at_isSet;
}

bool OAIBettingSerie_1::is_modified_at_Valid() const{
    return m_modified_at_isValid;
}

OAIObject OAIBettingSerie_1::getName() const {
    return m_name;
}
void OAIBettingSerie_1::setName(const OAIObject &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIBettingSerie_1::is_name_Set() const{
    return m_name_isSet;
}

bool OAIBettingSerie_1::is_name_Valid() const{
    return m_name_isValid;
}

OAIObject OAIBettingSerie_1::getSeason() const {
    return m_season;
}
void OAIBettingSerie_1::setSeason(const OAIObject &season) {
    m_season = season;
    m_season_isSet = true;
}

bool OAIBettingSerie_1::is_season_Set() const{
    return m_season_isSet;
}

bool OAIBettingSerie_1::is_season_Valid() const{
    return m_season_isValid;
}

QString OAIBettingSerie_1::getSlug() const {
    return m_slug;
}
void OAIBettingSerie_1::setSlug(const QString &slug) {
    m_slug = slug;
    m_slug_isSet = true;
}

bool OAIBettingSerie_1::is_slug_Set() const{
    return m_slug_isSet;
}

bool OAIBettingSerie_1::is_slug_Valid() const{
    return m_slug_isValid;
}

OAIObject OAIBettingSerie_1::getTier() const {
    return m_tier;
}
void OAIBettingSerie_1::setTier(const OAIObject &tier) {
    m_tier = tier;
    m_tier_isSet = true;
}

bool OAIBettingSerie_1::is_tier_Set() const{
    return m_tier_isSet;
}

bool OAIBettingSerie_1::is_tier_Valid() const{
    return m_tier_isValid;
}

OAICurrentVideogame OAIBettingSerie_1::getVideogame() const {
    return m_videogame;
}
void OAIBettingSerie_1::setVideogame(const OAICurrentVideogame &videogame) {
    m_videogame = videogame;
    m_videogame_isSet = true;
}

bool OAIBettingSerie_1::is_videogame_Set() const{
    return m_videogame_isSet;
}

bool OAIBettingSerie_1::is_videogame_Valid() const{
    return m_videogame_isValid;
}

OAIOpponentID_1 OAIBettingSerie_1::getWinnerId() const {
    return m_winner_id;
}
void OAIBettingSerie_1::setWinnerId(const OAIOpponentID_1 &winner_id) {
    m_winner_id = winner_id;
    m_winner_id_isSet = true;
}

bool OAIBettingSerie_1::is_winner_id_Set() const{
    return m_winner_id_isSet;
}

bool OAIBettingSerie_1::is_winner_id_Valid() const{
    return m_winner_id_isValid;
}

OAIObject OAIBettingSerie_1::getWinnerType() const {
    return m_winner_type;
}
void OAIBettingSerie_1::setWinnerType(const OAIObject &winner_type) {
    m_winner_type = winner_type;
    m_winner_type_isSet = true;
}

bool OAIBettingSerie_1::is_winner_type_Set() const{
    return m_winner_type_isSet;
}

bool OAIBettingSerie_1::is_winner_type_Valid() const{
    return m_winner_type_isValid;
}

qint32 OAIBettingSerie_1::getYear() const {
    return m_year;
}
void OAIBettingSerie_1::setYear(const qint32 &year) {
    m_year = year;
    m_year_isSet = true;
}

bool OAIBettingSerie_1::is_year_Set() const{
    return m_year_isSet;
}

bool OAIBettingSerie_1::is_year_Valid() const{
    return m_year_isValid;
}

bool OAIBettingSerie_1::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_begin_at.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_description.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_end_at.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_full_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_league_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_league_image_url.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_league_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_modified_at_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_season.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_slug_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_tier.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_videogame.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_winner_id.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_winner_type.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_year_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIBettingSerie_1::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_begin_at_isValid && m_description_isValid && m_end_at_isValid && m_full_name_isValid && m_id_isValid && m_league_id_isValid && m_league_image_url_isValid && m_league_name_isValid && m_modified_at_isValid && m_name_isValid && m_season_isValid && m_slug_isValid && m_tier_isValid && m_videogame_isValid && m_winner_id_isValid && m_winner_type_isValid && m_year_isValid && true;
}

} // namespace OpenAPI
