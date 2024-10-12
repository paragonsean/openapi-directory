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

#include "OAIBettingGame.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIBettingGame::OAIBettingGame(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIBettingGame::OAIBettingGame() {
    this->initializeModel();
}

OAIBettingGame::~OAIBettingGame() {}

void OAIBettingGame::initializeModel() {

    m_begin_at_isSet = false;
    m_begin_at_isValid = false;

    m_complete_isSet = false;
    m_complete_isValid = false;

    m_detailed_stats_isSet = false;
    m_detailed_stats_isValid = false;

    m_end_at_isSet = false;
    m_end_at_isValid = false;

    m_finished_isSet = false;
    m_finished_isValid = false;

    m_forfeit_isSet = false;
    m_forfeit_isValid = false;

    m_game_round_teams_isSet = false;
    m_game_round_teams_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_length_isSet = false;
    m_length_isValid = false;

    m_map_isSet = false;
    m_map_isValid = false;

    m_match_id_isSet = false;
    m_match_id_isValid = false;

    m_number_of_rounds_isSet = false;
    m_number_of_rounds_isValid = false;

    m_position_isSet = false;
    m_position_isValid = false;

    m_status_isSet = false;
    m_status_isValid = false;

    m_video_url_isSet = false;
    m_video_url_isValid = false;

    m_winner_isSet = false;
    m_winner_isValid = false;

    m_winner_type_isSet = false;
    m_winner_type_isValid = false;

    m_game_teams_isSet = false;
    m_game_teams_isValid = false;
}

void OAIBettingGame::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIBettingGame::fromJsonObject(QJsonObject json) {

    m_begin_at_isValid = ::OpenAPI::fromJsonValue(m_begin_at, json[QString("begin_at")]);
    m_begin_at_isSet = !json[QString("begin_at")].isNull() && m_begin_at_isValid;

    m_complete_isValid = ::OpenAPI::fromJsonValue(m_complete, json[QString("complete")]);
    m_complete_isSet = !json[QString("complete")].isNull() && m_complete_isValid;

    m_detailed_stats_isValid = ::OpenAPI::fromJsonValue(m_detailed_stats, json[QString("detailed_stats")]);
    m_detailed_stats_isSet = !json[QString("detailed_stats")].isNull() && m_detailed_stats_isValid;

    m_end_at_isValid = ::OpenAPI::fromJsonValue(m_end_at, json[QString("end_at")]);
    m_end_at_isSet = !json[QString("end_at")].isNull() && m_end_at_isValid;

    m_finished_isValid = ::OpenAPI::fromJsonValue(m_finished, json[QString("finished")]);
    m_finished_isSet = !json[QString("finished")].isNull() && m_finished_isValid;

    m_forfeit_isValid = ::OpenAPI::fromJsonValue(m_forfeit, json[QString("forfeit")]);
    m_forfeit_isSet = !json[QString("forfeit")].isNull() && m_forfeit_isValid;

    m_game_round_teams_isValid = ::OpenAPI::fromJsonValue(m_game_round_teams, json[QString("game_round_teams")]);
    m_game_round_teams_isSet = !json[QString("game_round_teams")].isNull() && m_game_round_teams_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_length_isValid = ::OpenAPI::fromJsonValue(m_length, json[QString("length")]);
    m_length_isSet = !json[QString("length")].isNull() && m_length_isValid;

    m_map_isValid = ::OpenAPI::fromJsonValue(m_map, json[QString("map")]);
    m_map_isSet = !json[QString("map")].isNull() && m_map_isValid;

    m_match_id_isValid = ::OpenAPI::fromJsonValue(m_match_id, json[QString("match_id")]);
    m_match_id_isSet = !json[QString("match_id")].isNull() && m_match_id_isValid;

    m_number_of_rounds_isValid = ::OpenAPI::fromJsonValue(m_number_of_rounds, json[QString("number_of_rounds")]);
    m_number_of_rounds_isSet = !json[QString("number_of_rounds")].isNull() && m_number_of_rounds_isValid;

    m_position_isValid = ::OpenAPI::fromJsonValue(m_position, json[QString("position")]);
    m_position_isSet = !json[QString("position")].isNull() && m_position_isValid;

    m_status_isValid = ::OpenAPI::fromJsonValue(m_status, json[QString("status")]);
    m_status_isSet = !json[QString("status")].isNull() && m_status_isValid;

    m_video_url_isValid = ::OpenAPI::fromJsonValue(m_video_url, json[QString("video_url")]);
    m_video_url_isSet = !json[QString("video_url")].isNull() && m_video_url_isValid;

    m_winner_isValid = ::OpenAPI::fromJsonValue(m_winner, json[QString("winner")]);
    m_winner_isSet = !json[QString("winner")].isNull() && m_winner_isValid;

    m_winner_type_isValid = ::OpenAPI::fromJsonValue(m_winner_type, json[QString("winner_type")]);
    m_winner_type_isSet = !json[QString("winner_type")].isNull() && m_winner_type_isValid;

    m_game_teams_isValid = ::OpenAPI::fromJsonValue(m_game_teams, json[QString("game_teams")]);
    m_game_teams_isSet = !json[QString("game_teams")].isNull() && m_game_teams_isValid;
}

QString OAIBettingGame::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIBettingGame::asJsonObject() const {
    QJsonObject obj;
    if (m_begin_at.isSet()) {
        obj.insert(QString("begin_at"), ::OpenAPI::toJsonValue(m_begin_at));
    }
    if (m_complete_isSet) {
        obj.insert(QString("complete"), ::OpenAPI::toJsonValue(m_complete));
    }
    if (m_detailed_stats_isSet) {
        obj.insert(QString("detailed_stats"), ::OpenAPI::toJsonValue(m_detailed_stats));
    }
    if (m_end_at.isSet()) {
        obj.insert(QString("end_at"), ::OpenAPI::toJsonValue(m_end_at));
    }
    if (m_finished_isSet) {
        obj.insert(QString("finished"), ::OpenAPI::toJsonValue(m_finished));
    }
    if (m_forfeit_isSet) {
        obj.insert(QString("forfeit"), ::OpenAPI::toJsonValue(m_forfeit));
    }
    if (m_game_round_teams.isSet()) {
        obj.insert(QString("game_round_teams"), ::OpenAPI::toJsonValue(m_game_round_teams));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_length.isSet()) {
        obj.insert(QString("length"), ::OpenAPI::toJsonValue(m_length));
    }
    if (m_map.isSet()) {
        obj.insert(QString("map"), ::OpenAPI::toJsonValue(m_map));
    }
    if (m_match_id_isSet) {
        obj.insert(QString("match_id"), ::OpenAPI::toJsonValue(m_match_id));
    }
    if (m_number_of_rounds.isSet()) {
        obj.insert(QString("number_of_rounds"), ::OpenAPI::toJsonValue(m_number_of_rounds));
    }
    if (m_position_isSet) {
        obj.insert(QString("position"), ::OpenAPI::toJsonValue(m_position));
    }
    if (m_status.isSet()) {
        obj.insert(QString("status"), ::OpenAPI::toJsonValue(m_status));
    }
    if (m_video_url.isSet()) {
        obj.insert(QString("video_url"), ::OpenAPI::toJsonValue(m_video_url));
    }
    if (m_winner.isSet()) {
        obj.insert(QString("winner"), ::OpenAPI::toJsonValue(m_winner));
    }
    if (m_winner_type.isSet()) {
        obj.insert(QString("winner_type"), ::OpenAPI::toJsonValue(m_winner_type));
    }
    if (m_game_teams.isSet()) {
        obj.insert(QString("game_teams"), ::OpenAPI::toJsonValue(m_game_teams));
    }
    return obj;
}

OAIObject OAIBettingGame::getBeginAt() const {
    return m_begin_at;
}
void OAIBettingGame::setBeginAt(const OAIObject &begin_at) {
    m_begin_at = begin_at;
    m_begin_at_isSet = true;
}

bool OAIBettingGame::is_begin_at_Set() const{
    return m_begin_at_isSet;
}

bool OAIBettingGame::is_begin_at_Valid() const{
    return m_begin_at_isValid;
}

bool OAIBettingGame::isComplete() const {
    return m_complete;
}
void OAIBettingGame::setComplete(const bool &complete) {
    m_complete = complete;
    m_complete_isSet = true;
}

bool OAIBettingGame::is_complete_Set() const{
    return m_complete_isSet;
}

bool OAIBettingGame::is_complete_Valid() const{
    return m_complete_isValid;
}

bool OAIBettingGame::isDetailedStats() const {
    return m_detailed_stats;
}
void OAIBettingGame::setDetailedStats(const bool &detailed_stats) {
    m_detailed_stats = detailed_stats;
    m_detailed_stats_isSet = true;
}

bool OAIBettingGame::is_detailed_stats_Set() const{
    return m_detailed_stats_isSet;
}

bool OAIBettingGame::is_detailed_stats_Valid() const{
    return m_detailed_stats_isValid;
}

OAIObject OAIBettingGame::getEndAt() const {
    return m_end_at;
}
void OAIBettingGame::setEndAt(const OAIObject &end_at) {
    m_end_at = end_at;
    m_end_at_isSet = true;
}

bool OAIBettingGame::is_end_at_Set() const{
    return m_end_at_isSet;
}

bool OAIBettingGame::is_end_at_Valid() const{
    return m_end_at_isValid;
}

bool OAIBettingGame::isFinished() const {
    return m_finished;
}
void OAIBettingGame::setFinished(const bool &finished) {
    m_finished = finished;
    m_finished_isSet = true;
}

bool OAIBettingGame::is_finished_Set() const{
    return m_finished_isSet;
}

bool OAIBettingGame::is_finished_Valid() const{
    return m_finished_isValid;
}

bool OAIBettingGame::isForfeit() const {
    return m_forfeit;
}
void OAIBettingGame::setForfeit(const bool &forfeit) {
    m_forfeit = forfeit;
    m_forfeit_isSet = true;
}

bool OAIBettingGame::is_forfeit_Set() const{
    return m_forfeit_isSet;
}

bool OAIBettingGame::is_forfeit_Valid() const{
    return m_forfeit_isValid;
}

OAIBettingGameRoundTeams_1 OAIBettingGame::getGameRoundTeams() const {
    return m_game_round_teams;
}
void OAIBettingGame::setGameRoundTeams(const OAIBettingGameRoundTeams_1 &game_round_teams) {
    m_game_round_teams = game_round_teams;
    m_game_round_teams_isSet = true;
}

bool OAIBettingGame::is_game_round_teams_Set() const{
    return m_game_round_teams_isSet;
}

bool OAIBettingGame::is_game_round_teams_Valid() const{
    return m_game_round_teams_isValid;
}

qint32 OAIBettingGame::getId() const {
    return m_id;
}
void OAIBettingGame::setId(const qint32 &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIBettingGame::is_id_Set() const{
    return m_id_isSet;
}

bool OAIBettingGame::is_id_Valid() const{
    return m_id_isValid;
}

OAIObject OAIBettingGame::getLength() const {
    return m_length;
}
void OAIBettingGame::setLength(const OAIObject &length) {
    m_length = length;
    m_length_isSet = true;
}

bool OAIBettingGame::is_length_Set() const{
    return m_length_isSet;
}

bool OAIBettingGame::is_length_Valid() const{
    return m_length_isValid;
}

OAICSGOMap_1 OAIBettingGame::getMap() const {
    return m_map;
}
void OAIBettingGame::setMap(const OAICSGOMap_1 &map) {
    m_map = map;
    m_map_isSet = true;
}

bool OAIBettingGame::is_map_Set() const{
    return m_map_isSet;
}

bool OAIBettingGame::is_map_Valid() const{
    return m_map_isValid;
}

qint32 OAIBettingGame::getMatchId() const {
    return m_match_id;
}
void OAIBettingGame::setMatchId(const qint32 &match_id) {
    m_match_id = match_id;
    m_match_id_isSet = true;
}

bool OAIBettingGame::is_match_id_Set() const{
    return m_match_id_isSet;
}

bool OAIBettingGame::is_match_id_Valid() const{
    return m_match_id_isValid;
}

OAIObject OAIBettingGame::getNumberOfRounds() const {
    return m_number_of_rounds;
}
void OAIBettingGame::setNumberOfRounds(const OAIObject &number_of_rounds) {
    m_number_of_rounds = number_of_rounds;
    m_number_of_rounds_isSet = true;
}

bool OAIBettingGame::is_number_of_rounds_Set() const{
    return m_number_of_rounds_isSet;
}

bool OAIBettingGame::is_number_of_rounds_Valid() const{
    return m_number_of_rounds_isValid;
}

qint32 OAIBettingGame::getPosition() const {
    return m_position;
}
void OAIBettingGame::setPosition(const qint32 &position) {
    m_position = position;
    m_position_isSet = true;
}

bool OAIBettingGame::is_position_Set() const{
    return m_position_isSet;
}

bool OAIBettingGame::is_position_Valid() const{
    return m_position_isValid;
}

OAIGameStatus OAIBettingGame::getStatus() const {
    return m_status;
}
void OAIBettingGame::setStatus(const OAIGameStatus &status) {
    m_status = status;
    m_status_isSet = true;
}

bool OAIBettingGame::is_status_Set() const{
    return m_status_isSet;
}

bool OAIBettingGame::is_status_Valid() const{
    return m_status_isValid;
}

OAIObject OAIBettingGame::getVideoUrl() const {
    return m_video_url;
}
void OAIBettingGame::setVideoUrl(const OAIObject &video_url) {
    m_video_url = video_url;
    m_video_url_isSet = true;
}

bool OAIBettingGame::is_video_url_Set() const{
    return m_video_url_isSet;
}

bool OAIBettingGame::is_video_url_Valid() const{
    return m_video_url_isValid;
}

OAIGameWinner OAIBettingGame::getWinner() const {
    return m_winner;
}
void OAIBettingGame::setWinner(const OAIGameWinner &winner) {
    m_winner = winner;
    m_winner_isSet = true;
}

bool OAIBettingGame::is_winner_Set() const{
    return m_winner_isSet;
}

bool OAIBettingGame::is_winner_Valid() const{
    return m_winner_isValid;
}

OAIObject OAIBettingGame::getWinnerType() const {
    return m_winner_type;
}
void OAIBettingGame::setWinnerType(const OAIObject &winner_type) {
    m_winner_type = winner_type;
    m_winner_type_isSet = true;
}

bool OAIBettingGame::is_winner_type_Set() const{
    return m_winner_type_isSet;
}

bool OAIBettingGame::is_winner_type_Valid() const{
    return m_winner_type_isValid;
}

OAIBettingGameTeams_1 OAIBettingGame::getGameTeams() const {
    return m_game_teams;
}
void OAIBettingGame::setGameTeams(const OAIBettingGameTeams_1 &game_teams) {
    m_game_teams = game_teams;
    m_game_teams_isSet = true;
}

bool OAIBettingGame::is_game_teams_Set() const{
    return m_game_teams_isSet;
}

bool OAIBettingGame::is_game_teams_Valid() const{
    return m_game_teams_isValid;
}

bool OAIBettingGame::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_begin_at.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_complete_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_detailed_stats_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_end_at.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_finished_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_forfeit_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_game_round_teams.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_length.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_map.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_match_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_number_of_rounds.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_position_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_status.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_video_url.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_winner.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_winner_type.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_game_teams.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIBettingGame::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_begin_at_isValid && m_complete_isValid && m_detailed_stats_isValid && m_end_at_isValid && m_finished_isValid && m_forfeit_isValid && m_game_round_teams_isValid && m_id_isValid && m_length_isValid && m_map_isValid && m_match_id_isValid && m_number_of_rounds_isValid && m_position_isValid && m_status_isValid && m_video_url_isValid && m_winner_isValid && m_winner_type_isValid && m_game_teams_isValid && true;
}

} // namespace OpenAPI
