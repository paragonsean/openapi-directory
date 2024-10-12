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

#include "OAIBettingTournament.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIBettingTournament::OAIBettingTournament(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIBettingTournament::OAIBettingTournament() {
    this->initializeModel();
}

OAIBettingTournament::~OAIBettingTournament() {}

void OAIBettingTournament::initializeModel() {

    m_begin_at_isSet = false;
    m_begin_at_isValid = false;

    m_end_at_isSet = false;
    m_end_at_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_live_supported_isSet = false;
    m_live_supported_isValid = false;

    m_modified_at_isSet = false;
    m_modified_at_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_prizepool_isSet = false;
    m_prizepool_isValid = false;

    m_serie_id_isSet = false;
    m_serie_id_isValid = false;

    m_slug_isSet = false;
    m_slug_isValid = false;

    m_videogame_isSet = false;
    m_videogame_isValid = false;

    m_winner_id_isSet = false;
    m_winner_id_isValid = false;

    m_winner_type_isSet = false;
    m_winner_type_isValid = false;
}

void OAIBettingTournament::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIBettingTournament::fromJsonObject(QJsonObject json) {

    m_begin_at_isValid = ::OpenAPI::fromJsonValue(m_begin_at, json[QString("begin_at")]);
    m_begin_at_isSet = !json[QString("begin_at")].isNull() && m_begin_at_isValid;

    m_end_at_isValid = ::OpenAPI::fromJsonValue(m_end_at, json[QString("end_at")]);
    m_end_at_isSet = !json[QString("end_at")].isNull() && m_end_at_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_live_supported_isValid = ::OpenAPI::fromJsonValue(m_live_supported, json[QString("live_supported")]);
    m_live_supported_isSet = !json[QString("live_supported")].isNull() && m_live_supported_isValid;

    m_modified_at_isValid = ::OpenAPI::fromJsonValue(m_modified_at, json[QString("modified_at")]);
    m_modified_at_isSet = !json[QString("modified_at")].isNull() && m_modified_at_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_prizepool_isValid = ::OpenAPI::fromJsonValue(m_prizepool, json[QString("prizepool")]);
    m_prizepool_isSet = !json[QString("prizepool")].isNull() && m_prizepool_isValid;

    m_serie_id_isValid = ::OpenAPI::fromJsonValue(m_serie_id, json[QString("serie_id")]);
    m_serie_id_isSet = !json[QString("serie_id")].isNull() && m_serie_id_isValid;

    m_slug_isValid = ::OpenAPI::fromJsonValue(m_slug, json[QString("slug")]);
    m_slug_isSet = !json[QString("slug")].isNull() && m_slug_isValid;

    m_videogame_isValid = ::OpenAPI::fromJsonValue(m_videogame, json[QString("videogame")]);
    m_videogame_isSet = !json[QString("videogame")].isNull() && m_videogame_isValid;

    m_winner_id_isValid = ::OpenAPI::fromJsonValue(m_winner_id, json[QString("winner_id")]);
    m_winner_id_isSet = !json[QString("winner_id")].isNull() && m_winner_id_isValid;

    m_winner_type_isValid = ::OpenAPI::fromJsonValue(m_winner_type, json[QString("winner_type")]);
    m_winner_type_isSet = !json[QString("winner_type")].isNull() && m_winner_type_isValid;
}

QString OAIBettingTournament::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIBettingTournament::asJsonObject() const {
    QJsonObject obj;
    if (m_begin_at.isSet()) {
        obj.insert(QString("begin_at"), ::OpenAPI::toJsonValue(m_begin_at));
    }
    if (m_end_at.isSet()) {
        obj.insert(QString("end_at"), ::OpenAPI::toJsonValue(m_end_at));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_live_supported_isSet) {
        obj.insert(QString("live_supported"), ::OpenAPI::toJsonValue(m_live_supported));
    }
    if (m_modified_at_isSet) {
        obj.insert(QString("modified_at"), ::OpenAPI::toJsonValue(m_modified_at));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_prizepool.isSet()) {
        obj.insert(QString("prizepool"), ::OpenAPI::toJsonValue(m_prizepool));
    }
    if (m_serie_id_isSet) {
        obj.insert(QString("serie_id"), ::OpenAPI::toJsonValue(m_serie_id));
    }
    if (m_slug_isSet) {
        obj.insert(QString("slug"), ::OpenAPI::toJsonValue(m_slug));
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
    return obj;
}

QJsonValue OAIBettingTournament::getBeginAt() const {
    return m_begin_at;
}
void OAIBettingTournament::setBeginAt(const QJsonValue &begin_at) {
    m_begin_at = begin_at;
    m_begin_at_isSet = true;
}

bool OAIBettingTournament::is_begin_at_Set() const{
    return m_begin_at_isSet;
}

bool OAIBettingTournament::is_begin_at_Valid() const{
    return m_begin_at_isValid;
}

QJsonValue OAIBettingTournament::getEndAt() const {
    return m_end_at;
}
void OAIBettingTournament::setEndAt(const QJsonValue &end_at) {
    m_end_at = end_at;
    m_end_at_isSet = true;
}

bool OAIBettingTournament::is_end_at_Set() const{
    return m_end_at_isSet;
}

bool OAIBettingTournament::is_end_at_Valid() const{
    return m_end_at_isValid;
}

qint32 OAIBettingTournament::getId() const {
    return m_id;
}
void OAIBettingTournament::setId(const qint32 &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIBettingTournament::is_id_Set() const{
    return m_id_isSet;
}

bool OAIBettingTournament::is_id_Valid() const{
    return m_id_isValid;
}

bool OAIBettingTournament::isLiveSupported() const {
    return m_live_supported;
}
void OAIBettingTournament::setLiveSupported(const bool &live_supported) {
    m_live_supported = live_supported;
    m_live_supported_isSet = true;
}

bool OAIBettingTournament::is_live_supported_Set() const{
    return m_live_supported_isSet;
}

bool OAIBettingTournament::is_live_supported_Valid() const{
    return m_live_supported_isValid;
}

QDateTime OAIBettingTournament::getModifiedAt() const {
    return m_modified_at;
}
void OAIBettingTournament::setModifiedAt(const QDateTime &modified_at) {
    m_modified_at = modified_at;
    m_modified_at_isSet = true;
}

bool OAIBettingTournament::is_modified_at_Set() const{
    return m_modified_at_isSet;
}

bool OAIBettingTournament::is_modified_at_Valid() const{
    return m_modified_at_isValid;
}

QString OAIBettingTournament::getName() const {
    return m_name;
}
void OAIBettingTournament::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIBettingTournament::is_name_Set() const{
    return m_name_isSet;
}

bool OAIBettingTournament::is_name_Valid() const{
    return m_name_isValid;
}

QJsonValue OAIBettingTournament::getPrizepool() const {
    return m_prizepool;
}
void OAIBettingTournament::setPrizepool(const QJsonValue &prizepool) {
    m_prizepool = prizepool;
    m_prizepool_isSet = true;
}

bool OAIBettingTournament::is_prizepool_Set() const{
    return m_prizepool_isSet;
}

bool OAIBettingTournament::is_prizepool_Valid() const{
    return m_prizepool_isValid;
}

qint32 OAIBettingTournament::getSerieId() const {
    return m_serie_id;
}
void OAIBettingTournament::setSerieId(const qint32 &serie_id) {
    m_serie_id = serie_id;
    m_serie_id_isSet = true;
}

bool OAIBettingTournament::is_serie_id_Set() const{
    return m_serie_id_isSet;
}

bool OAIBettingTournament::is_serie_id_Valid() const{
    return m_serie_id_isValid;
}

QString OAIBettingTournament::getSlug() const {
    return m_slug;
}
void OAIBettingTournament::setSlug(const QString &slug) {
    m_slug = slug;
    m_slug_isSet = true;
}

bool OAIBettingTournament::is_slug_Set() const{
    return m_slug_isSet;
}

bool OAIBettingTournament::is_slug_Valid() const{
    return m_slug_isValid;
}

OAICurrentVideogame OAIBettingTournament::getVideogame() const {
    return m_videogame;
}
void OAIBettingTournament::setVideogame(const OAICurrentVideogame &videogame) {
    m_videogame = videogame;
    m_videogame_isSet = true;
}

bool OAIBettingTournament::is_videogame_Set() const{
    return m_videogame_isSet;
}

bool OAIBettingTournament::is_videogame_Valid() const{
    return m_videogame_isValid;
}

OAIOpponentID_1 OAIBettingTournament::getWinnerId() const {
    return m_winner_id;
}
void OAIBettingTournament::setWinnerId(const OAIOpponentID_1 &winner_id) {
    m_winner_id = winner_id;
    m_winner_id_isSet = true;
}

bool OAIBettingTournament::is_winner_id_Set() const{
    return m_winner_id_isSet;
}

bool OAIBettingTournament::is_winner_id_Valid() const{
    return m_winner_id_isValid;
}

QJsonValue OAIBettingTournament::getWinnerType() const {
    return m_winner_type;
}
void OAIBettingTournament::setWinnerType(const QJsonValue &winner_type) {
    m_winner_type = winner_type;
    m_winner_type_isSet = true;
}

bool OAIBettingTournament::is_winner_type_Set() const{
    return m_winner_type_isSet;
}

bool OAIBettingTournament::is_winner_type_Valid() const{
    return m_winner_type_isValid;
}

bool OAIBettingTournament::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_begin_at.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_end_at.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_live_supported_isSet) {
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

        if (m_prizepool.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_serie_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_slug_isSet) {
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
    } while (false);
    return isObjectUpdated;
}

bool OAIBettingTournament::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_begin_at_isValid && m_end_at_isValid && m_id_isValid && m_live_supported_isValid && m_modified_at_isValid && m_name_isValid && m_prizepool_isValid && m_serie_id_isValid && m_slug_isValid && m_videogame_isValid && m_winner_id_isValid && m_winner_type_isValid && true;
}

} // namespace OpenAPI
