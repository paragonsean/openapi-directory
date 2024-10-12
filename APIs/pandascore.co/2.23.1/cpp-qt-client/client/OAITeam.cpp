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

#include "OAITeam.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAITeam::OAITeam(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAITeam::OAITeam() {
    this->initializeModel();
}

OAITeam::~OAITeam() {}

void OAITeam::initializeModel() {

    m_acronym_isSet = false;
    m_acronym_isValid = false;

    m_current_videogame_isSet = false;
    m_current_videogame_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_image_url_isSet = false;
    m_image_url_isValid = false;

    m_location_isSet = false;
    m_location_isValid = false;

    m_modified_at_isSet = false;
    m_modified_at_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_players_isSet = false;
    m_players_isValid = false;

    m_slug_isSet = false;
    m_slug_isValid = false;
}

void OAITeam::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAITeam::fromJsonObject(QJsonObject json) {

    m_acronym_isValid = ::OpenAPI::fromJsonValue(m_acronym, json[QString("acronym")]);
    m_acronym_isSet = !json[QString("acronym")].isNull() && m_acronym_isValid;

    m_current_videogame_isValid = ::OpenAPI::fromJsonValue(m_current_videogame, json[QString("current_videogame")]);
    m_current_videogame_isSet = !json[QString("current_videogame")].isNull() && m_current_videogame_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_image_url_isValid = ::OpenAPI::fromJsonValue(m_image_url, json[QString("image_url")]);
    m_image_url_isSet = !json[QString("image_url")].isNull() && m_image_url_isValid;

    m_location_isValid = ::OpenAPI::fromJsonValue(m_location, json[QString("location")]);
    m_location_isSet = !json[QString("location")].isNull() && m_location_isValid;

    m_modified_at_isValid = ::OpenAPI::fromJsonValue(m_modified_at, json[QString("modified_at")]);
    m_modified_at_isSet = !json[QString("modified_at")].isNull() && m_modified_at_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_players_isValid = ::OpenAPI::fromJsonValue(m_players, json[QString("players")]);
    m_players_isSet = !json[QString("players")].isNull() && m_players_isValid;

    m_slug_isValid = ::OpenAPI::fromJsonValue(m_slug, json[QString("slug")]);
    m_slug_isSet = !json[QString("slug")].isNull() && m_slug_isValid;
}

QString OAITeam::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAITeam::asJsonObject() const {
    QJsonObject obj;
    if (m_acronym.isSet()) {
        obj.insert(QString("acronym"), ::OpenAPI::toJsonValue(m_acronym));
    }
    if (m_current_videogame.isSet()) {
        obj.insert(QString("current_videogame"), ::OpenAPI::toJsonValue(m_current_videogame));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_image_url.isSet()) {
        obj.insert(QString("image_url"), ::OpenAPI::toJsonValue(m_image_url));
    }
    if (m_location.isSet()) {
        obj.insert(QString("location"), ::OpenAPI::toJsonValue(m_location));
    }
    if (m_modified_at_isSet) {
        obj.insert(QString("modified_at"), ::OpenAPI::toJsonValue(m_modified_at));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_players.size() > 0) {
        obj.insert(QString("players"), ::OpenAPI::toJsonValue(m_players));
    }
    if (m_slug.isSet()) {
        obj.insert(QString("slug"), ::OpenAPI::toJsonValue(m_slug));
    }
    return obj;
}

QJsonValue OAITeam::getAcronym() const {
    return m_acronym;
}
void OAITeam::setAcronym(const QJsonValue &acronym) {
    m_acronym = acronym;
    m_acronym_isSet = true;
}

bool OAITeam::is_acronym_Set() const{
    return m_acronym_isSet;
}

bool OAITeam::is_acronym_Valid() const{
    return m_acronym_isValid;
}

QJsonValue OAITeam::getCurrentVideogame() const {
    return m_current_videogame;
}
void OAITeam::setCurrentVideogame(const QJsonValue &current_videogame) {
    m_current_videogame = current_videogame;
    m_current_videogame_isSet = true;
}

bool OAITeam::is_current_videogame_Set() const{
    return m_current_videogame_isSet;
}

bool OAITeam::is_current_videogame_Valid() const{
    return m_current_videogame_isValid;
}

qint32 OAITeam::getId() const {
    return m_id;
}
void OAITeam::setId(const qint32 &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAITeam::is_id_Set() const{
    return m_id_isSet;
}

bool OAITeam::is_id_Valid() const{
    return m_id_isValid;
}

QJsonValue OAITeam::getImageUrl() const {
    return m_image_url;
}
void OAITeam::setImageUrl(const QJsonValue &image_url) {
    m_image_url = image_url;
    m_image_url_isSet = true;
}

bool OAITeam::is_image_url_Set() const{
    return m_image_url_isSet;
}

bool OAITeam::is_image_url_Valid() const{
    return m_image_url_isValid;
}

QJsonValue OAITeam::getLocation() const {
    return m_location;
}
void OAITeam::setLocation(const QJsonValue &location) {
    m_location = location;
    m_location_isSet = true;
}

bool OAITeam::is_location_Set() const{
    return m_location_isSet;
}

bool OAITeam::is_location_Valid() const{
    return m_location_isValid;
}

QDateTime OAITeam::getModifiedAt() const {
    return m_modified_at;
}
void OAITeam::setModifiedAt(const QDateTime &modified_at) {
    m_modified_at = modified_at;
    m_modified_at_isSet = true;
}

bool OAITeam::is_modified_at_Set() const{
    return m_modified_at_isSet;
}

bool OAITeam::is_modified_at_Valid() const{
    return m_modified_at_isValid;
}

QString OAITeam::getName() const {
    return m_name;
}
void OAITeam::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAITeam::is_name_Set() const{
    return m_name_isSet;
}

bool OAITeam::is_name_Valid() const{
    return m_name_isValid;
}

QList<OAIBasePlayer> OAITeam::getPlayers() const {
    return m_players;
}
void OAITeam::setPlayers(const QList<OAIBasePlayer> &players) {
    m_players = players;
    m_players_isSet = true;
}

bool OAITeam::is_players_Set() const{
    return m_players_isSet;
}

bool OAITeam::is_players_Valid() const{
    return m_players_isValid;
}

QJsonValue OAITeam::getSlug() const {
    return m_slug;
}
void OAITeam::setSlug(const QJsonValue &slug) {
    m_slug = slug;
    m_slug_isSet = true;
}

bool OAITeam::is_slug_Set() const{
    return m_slug_isSet;
}

bool OAITeam::is_slug_Valid() const{
    return m_slug_isValid;
}

bool OAITeam::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_acronym.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_current_videogame.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_image_url.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_location.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_modified_at_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_players.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_slug.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAITeam::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_acronym_isValid && m_current_videogame_isValid && m_id_isValid && m_image_url_isValid && m_location_isValid && m_modified_at_isValid && m_name_isValid && m_players_isValid && m_slug_isValid && true;
}

} // namespace OpenAPI
