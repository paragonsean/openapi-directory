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

#include "OAIRange_over_Matches.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIRange_over_Matches::OAIRange_over_Matches(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIRange_over_Matches::OAIRange_over_Matches() {
    this->initializeModel();
}

OAIRange_over_Matches::~OAIRange_over_Matches() {}

void OAIRange_over_Matches::initializeModel() {

    m_begin_at_isSet = false;
    m_begin_at_isValid = false;

    m_detailed_stats_isSet = false;
    m_detailed_stats_isValid = false;

    m_draw_isSet = false;
    m_draw_isValid = false;

    m_end_at_isSet = false;
    m_end_at_isValid = false;

    m_forfeit_isSet = false;
    m_forfeit_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_match_type_isSet = false;
    m_match_type_isValid = false;

    m_modified_at_isSet = false;
    m_modified_at_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_number_of_games_isSet = false;
    m_number_of_games_isValid = false;

    m_scheduled_at_isSet = false;
    m_scheduled_at_isValid = false;

    m_slug_isSet = false;
    m_slug_isValid = false;

    m_status_isSet = false;
    m_status_isValid = false;

    m_tournament_id_isSet = false;
    m_tournament_id_isValid = false;

    m_winner_id_isSet = false;
    m_winner_id_isValid = false;
}

void OAIRange_over_Matches::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIRange_over_Matches::fromJsonObject(QJsonObject json) {

    m_begin_at_isValid = ::OpenAPI::fromJsonValue(m_begin_at, json[QString("begin_at")]);
    m_begin_at_isSet = !json[QString("begin_at")].isNull() && m_begin_at_isValid;

    m_detailed_stats_isValid = ::OpenAPI::fromJsonValue(m_detailed_stats, json[QString("detailed_stats")]);
    m_detailed_stats_isSet = !json[QString("detailed_stats")].isNull() && m_detailed_stats_isValid;

    m_draw_isValid = ::OpenAPI::fromJsonValue(m_draw, json[QString("draw")]);
    m_draw_isSet = !json[QString("draw")].isNull() && m_draw_isValid;

    m_end_at_isValid = ::OpenAPI::fromJsonValue(m_end_at, json[QString("end_at")]);
    m_end_at_isSet = !json[QString("end_at")].isNull() && m_end_at_isValid;

    m_forfeit_isValid = ::OpenAPI::fromJsonValue(m_forfeit, json[QString("forfeit")]);
    m_forfeit_isSet = !json[QString("forfeit")].isNull() && m_forfeit_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_match_type_isValid = ::OpenAPI::fromJsonValue(m_match_type, json[QString("match_type")]);
    m_match_type_isSet = !json[QString("match_type")].isNull() && m_match_type_isValid;

    m_modified_at_isValid = ::OpenAPI::fromJsonValue(m_modified_at, json[QString("modified_at")]);
    m_modified_at_isSet = !json[QString("modified_at")].isNull() && m_modified_at_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_number_of_games_isValid = ::OpenAPI::fromJsonValue(m_number_of_games, json[QString("number_of_games")]);
    m_number_of_games_isSet = !json[QString("number_of_games")].isNull() && m_number_of_games_isValid;

    m_scheduled_at_isValid = ::OpenAPI::fromJsonValue(m_scheduled_at, json[QString("scheduled_at")]);
    m_scheduled_at_isSet = !json[QString("scheduled_at")].isNull() && m_scheduled_at_isValid;

    m_slug_isValid = ::OpenAPI::fromJsonValue(m_slug, json[QString("slug")]);
    m_slug_isSet = !json[QString("slug")].isNull() && m_slug_isValid;

    m_status_isValid = ::OpenAPI::fromJsonValue(m_status, json[QString("status")]);
    m_status_isSet = !json[QString("status")].isNull() && m_status_isValid;

    m_tournament_id_isValid = ::OpenAPI::fromJsonValue(m_tournament_id, json[QString("tournament_id")]);
    m_tournament_id_isSet = !json[QString("tournament_id")].isNull() && m_tournament_id_isValid;

    m_winner_id_isValid = ::OpenAPI::fromJsonValue(m_winner_id, json[QString("winner_id")]);
    m_winner_id_isSet = !json[QString("winner_id")].isNull() && m_winner_id_isValid;
}

QString OAIRange_over_Matches::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIRange_over_Matches::asJsonObject() const {
    QJsonObject obj;
    if (m_begin_at.size() > 0) {
        obj.insert(QString("begin_at"), ::OpenAPI::toJsonValue(m_begin_at));
    }
    if (m_detailed_stats.size() > 0) {
        obj.insert(QString("detailed_stats"), ::OpenAPI::toJsonValue(m_detailed_stats));
    }
    if (m_draw.size() > 0) {
        obj.insert(QString("draw"), ::OpenAPI::toJsonValue(m_draw));
    }
    if (m_end_at.size() > 0) {
        obj.insert(QString("end_at"), ::OpenAPI::toJsonValue(m_end_at));
    }
    if (m_forfeit.size() > 0) {
        obj.insert(QString("forfeit"), ::OpenAPI::toJsonValue(m_forfeit));
    }
    if (m_id.size() > 0) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_match_type.size() > 0) {
        obj.insert(QString("match_type"), ::OpenAPI::toJsonValue(m_match_type));
    }
    if (m_modified_at.size() > 0) {
        obj.insert(QString("modified_at"), ::OpenAPI::toJsonValue(m_modified_at));
    }
    if (m_name.size() > 0) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_number_of_games.size() > 0) {
        obj.insert(QString("number_of_games"), ::OpenAPI::toJsonValue(m_number_of_games));
    }
    if (m_scheduled_at.size() > 0) {
        obj.insert(QString("scheduled_at"), ::OpenAPI::toJsonValue(m_scheduled_at));
    }
    if (m_slug.size() > 0) {
        obj.insert(QString("slug"), ::OpenAPI::toJsonValue(m_slug));
    }
    if (m_status.size() > 0) {
        obj.insert(QString("status"), ::OpenAPI::toJsonValue(m_status));
    }
    if (m_tournament_id.size() > 0) {
        obj.insert(QString("tournament_id"), ::OpenAPI::toJsonValue(m_tournament_id));
    }
    if (m_winner_id.size() > 0) {
        obj.insert(QString("winner_id"), ::OpenAPI::toJsonValue(m_winner_id));
    }
    return obj;
}

QList<QDateTime> OAIRange_over_Matches::getBeginAt() const {
    return m_begin_at;
}
void OAIRange_over_Matches::setBeginAt(const QList<QDateTime> &begin_at) {
    m_begin_at = begin_at;
    m_begin_at_isSet = true;
}

bool OAIRange_over_Matches::is_begin_at_Set() const{
    return m_begin_at_isSet;
}

bool OAIRange_over_Matches::is_begin_at_Valid() const{
    return m_begin_at_isValid;
}

QList<bool> OAIRange_over_Matches::getDetailedStats() const {
    return m_detailed_stats;
}
void OAIRange_over_Matches::setDetailedStats(const QList<bool> &detailed_stats) {
    m_detailed_stats = detailed_stats;
    m_detailed_stats_isSet = true;
}

bool OAIRange_over_Matches::is_detailed_stats_Set() const{
    return m_detailed_stats_isSet;
}

bool OAIRange_over_Matches::is_detailed_stats_Valid() const{
    return m_detailed_stats_isValid;
}

QList<bool> OAIRange_over_Matches::getDraw() const {
    return m_draw;
}
void OAIRange_over_Matches::setDraw(const QList<bool> &draw) {
    m_draw = draw;
    m_draw_isSet = true;
}

bool OAIRange_over_Matches::is_draw_Set() const{
    return m_draw_isSet;
}

bool OAIRange_over_Matches::is_draw_Valid() const{
    return m_draw_isValid;
}

QList<QDateTime> OAIRange_over_Matches::getEndAt() const {
    return m_end_at;
}
void OAIRange_over_Matches::setEndAt(const QList<QDateTime> &end_at) {
    m_end_at = end_at;
    m_end_at_isSet = true;
}

bool OAIRange_over_Matches::is_end_at_Set() const{
    return m_end_at_isSet;
}

bool OAIRange_over_Matches::is_end_at_Valid() const{
    return m_end_at_isValid;
}

QList<bool> OAIRange_over_Matches::getForfeit() const {
    return m_forfeit;
}
void OAIRange_over_Matches::setForfeit(const QList<bool> &forfeit) {
    m_forfeit = forfeit;
    m_forfeit_isSet = true;
}

bool OAIRange_over_Matches::is_forfeit_Set() const{
    return m_forfeit_isSet;
}

bool OAIRange_over_Matches::is_forfeit_Valid() const{
    return m_forfeit_isValid;
}

QList<qint32> OAIRange_over_Matches::getId() const {
    return m_id;
}
void OAIRange_over_Matches::setId(const QList<qint32> &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIRange_over_Matches::is_id_Set() const{
    return m_id_isSet;
}

bool OAIRange_over_Matches::is_id_Valid() const{
    return m_id_isValid;
}

QList<OAIMatchType> OAIRange_over_Matches::getMatchType() const {
    return m_match_type;
}
void OAIRange_over_Matches::setMatchType(const QList<OAIMatchType> &match_type) {
    m_match_type = match_type;
    m_match_type_isSet = true;
}

bool OAIRange_over_Matches::is_match_type_Set() const{
    return m_match_type_isSet;
}

bool OAIRange_over_Matches::is_match_type_Valid() const{
    return m_match_type_isValid;
}

QList<QDateTime> OAIRange_over_Matches::getModifiedAt() const {
    return m_modified_at;
}
void OAIRange_over_Matches::setModifiedAt(const QList<QDateTime> &modified_at) {
    m_modified_at = modified_at;
    m_modified_at_isSet = true;
}

bool OAIRange_over_Matches::is_modified_at_Set() const{
    return m_modified_at_isSet;
}

bool OAIRange_over_Matches::is_modified_at_Valid() const{
    return m_modified_at_isValid;
}

QList<QString> OAIRange_over_Matches::getName() const {
    return m_name;
}
void OAIRange_over_Matches::setName(const QList<QString> &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIRange_over_Matches::is_name_Set() const{
    return m_name_isSet;
}

bool OAIRange_over_Matches::is_name_Valid() const{
    return m_name_isValid;
}

QList<qint32> OAIRange_over_Matches::getNumberOfGames() const {
    return m_number_of_games;
}
void OAIRange_over_Matches::setNumberOfGames(const QList<qint32> &number_of_games) {
    m_number_of_games = number_of_games;
    m_number_of_games_isSet = true;
}

bool OAIRange_over_Matches::is_number_of_games_Set() const{
    return m_number_of_games_isSet;
}

bool OAIRange_over_Matches::is_number_of_games_Valid() const{
    return m_number_of_games_isValid;
}

QList<QDateTime> OAIRange_over_Matches::getScheduledAt() const {
    return m_scheduled_at;
}
void OAIRange_over_Matches::setScheduledAt(const QList<QDateTime> &scheduled_at) {
    m_scheduled_at = scheduled_at;
    m_scheduled_at_isSet = true;
}

bool OAIRange_over_Matches::is_scheduled_at_Set() const{
    return m_scheduled_at_isSet;
}

bool OAIRange_over_Matches::is_scheduled_at_Valid() const{
    return m_scheduled_at_isValid;
}

QList<QString> OAIRange_over_Matches::getSlug() const {
    return m_slug;
}
void OAIRange_over_Matches::setSlug(const QList<QString> &slug) {
    m_slug = slug;
    m_slug_isSet = true;
}

bool OAIRange_over_Matches::is_slug_Set() const{
    return m_slug_isSet;
}

bool OAIRange_over_Matches::is_slug_Valid() const{
    return m_slug_isValid;
}

QList<OAIMatchStatus> OAIRange_over_Matches::getStatus() const {
    return m_status;
}
void OAIRange_over_Matches::setStatus(const QList<OAIMatchStatus> &status) {
    m_status = status;
    m_status_isSet = true;
}

bool OAIRange_over_Matches::is_status_Set() const{
    return m_status_isSet;
}

bool OAIRange_over_Matches::is_status_Valid() const{
    return m_status_isValid;
}

QList<qint32> OAIRange_over_Matches::getTournamentId() const {
    return m_tournament_id;
}
void OAIRange_over_Matches::setTournamentId(const QList<qint32> &tournament_id) {
    m_tournament_id = tournament_id;
    m_tournament_id_isSet = true;
}

bool OAIRange_over_Matches::is_tournament_id_Set() const{
    return m_tournament_id_isSet;
}

bool OAIRange_over_Matches::is_tournament_id_Valid() const{
    return m_tournament_id_isValid;
}

QList<OAIOpponentID> OAIRange_over_Matches::getWinnerId() const {
    return m_winner_id;
}
void OAIRange_over_Matches::setWinnerId(const QList<OAIOpponentID> &winner_id) {
    m_winner_id = winner_id;
    m_winner_id_isSet = true;
}

bool OAIRange_over_Matches::is_winner_id_Set() const{
    return m_winner_id_isSet;
}

bool OAIRange_over_Matches::is_winner_id_Valid() const{
    return m_winner_id_isValid;
}

bool OAIRange_over_Matches::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_begin_at.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_detailed_stats.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_draw.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_end_at.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_forfeit.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_id.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_match_type.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_modified_at.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_name.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_number_of_games.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_scheduled_at.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_slug.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_status.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_tournament_id.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_winner_id.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIRange_over_Matches::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
