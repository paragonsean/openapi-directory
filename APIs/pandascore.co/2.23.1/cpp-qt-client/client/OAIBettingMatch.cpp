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

#include "OAIBettingMatch.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIBettingMatch::OAIBettingMatch(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIBettingMatch::OAIBettingMatch() {
    this->initializeModel();
}

OAIBettingMatch::~OAIBettingMatch() {}

void OAIBettingMatch::initializeModel() {

    m_begin_at_isSet = false;
    m_begin_at_isValid = false;

    m_betting_metadata_isSet = false;
    m_betting_metadata_isValid = false;

    m_detailed_stats_isSet = false;
    m_detailed_stats_isValid = false;

    m_draw_isSet = false;
    m_draw_isValid = false;

    m_end_at_isSet = false;
    m_end_at_isValid = false;

    m_forfeit_isSet = false;
    m_forfeit_isValid = false;

    m_game_advantage_isSet = false;
    m_game_advantage_isValid = false;

    m_games_isSet = false;
    m_games_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_league_isSet = false;
    m_league_isValid = false;

    m_league_id_isSet = false;
    m_league_id_isValid = false;

    m_live_isSet = false;
    m_live_isValid = false;

    m_live_embed_url_isSet = false;
    m_live_embed_url_isValid = false;

    m_match_type_isSet = false;
    m_match_type_isValid = false;

    m_modified_at_isSet = false;
    m_modified_at_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_number_of_games_isSet = false;
    m_number_of_games_isValid = false;

    m_official_stream_url_isSet = false;
    m_official_stream_url_isValid = false;

    m_opponents_isSet = false;
    m_opponents_isValid = false;

    m_original_scheduled_at_isSet = false;
    m_original_scheduled_at_isValid = false;

    m_rescheduled_isSet = false;
    m_rescheduled_isValid = false;

    m_results_isSet = false;
    m_results_isValid = false;

    m_scheduled_at_isSet = false;
    m_scheduled_at_isValid = false;

    m_serie_isSet = false;
    m_serie_isValid = false;

    m_serie_id_isSet = false;
    m_serie_id_isValid = false;

    m_slug_isSet = false;
    m_slug_isValid = false;

    m_status_isSet = false;
    m_status_isValid = false;

    m_streams_isSet = false;
    m_streams_isValid = false;

    m_streams_list_isSet = false;
    m_streams_list_isValid = false;

    m_tournament_isSet = false;
    m_tournament_isValid = false;

    m_tournament_id_isSet = false;
    m_tournament_id_isValid = false;

    m_videogame_isSet = false;
    m_videogame_isValid = false;

    m_videogame_version_isSet = false;
    m_videogame_version_isValid = false;

    m_winner_isSet = false;
    m_winner_isValid = false;

    m_winner_id_isSet = false;
    m_winner_id_isValid = false;
}

void OAIBettingMatch::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIBettingMatch::fromJsonObject(QJsonObject json) {

    m_begin_at_isValid = ::OpenAPI::fromJsonValue(m_begin_at, json[QString("begin_at")]);
    m_begin_at_isSet = !json[QString("begin_at")].isNull() && m_begin_at_isValid;

    m_betting_metadata_isValid = ::OpenAPI::fromJsonValue(m_betting_metadata, json[QString("betting_metadata")]);
    m_betting_metadata_isSet = !json[QString("betting_metadata")].isNull() && m_betting_metadata_isValid;

    m_detailed_stats_isValid = ::OpenAPI::fromJsonValue(m_detailed_stats, json[QString("detailed_stats")]);
    m_detailed_stats_isSet = !json[QString("detailed_stats")].isNull() && m_detailed_stats_isValid;

    m_draw_isValid = ::OpenAPI::fromJsonValue(m_draw, json[QString("draw")]);
    m_draw_isSet = !json[QString("draw")].isNull() && m_draw_isValid;

    m_end_at_isValid = ::OpenAPI::fromJsonValue(m_end_at, json[QString("end_at")]);
    m_end_at_isSet = !json[QString("end_at")].isNull() && m_end_at_isValid;

    m_forfeit_isValid = ::OpenAPI::fromJsonValue(m_forfeit, json[QString("forfeit")]);
    m_forfeit_isSet = !json[QString("forfeit")].isNull() && m_forfeit_isValid;

    m_game_advantage_isValid = ::OpenAPI::fromJsonValue(m_game_advantage, json[QString("game_advantage")]);
    m_game_advantage_isSet = !json[QString("game_advantage")].isNull() && m_game_advantage_isValid;

    m_games_isValid = ::OpenAPI::fromJsonValue(m_games, json[QString("games")]);
    m_games_isSet = !json[QString("games")].isNull() && m_games_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_league_isValid = ::OpenAPI::fromJsonValue(m_league, json[QString("league")]);
    m_league_isSet = !json[QString("league")].isNull() && m_league_isValid;

    m_league_id_isValid = ::OpenAPI::fromJsonValue(m_league_id, json[QString("league_id")]);
    m_league_id_isSet = !json[QString("league_id")].isNull() && m_league_id_isValid;

    m_live_isValid = ::OpenAPI::fromJsonValue(m_live, json[QString("live")]);
    m_live_isSet = !json[QString("live")].isNull() && m_live_isValid;

    m_live_embed_url_isValid = ::OpenAPI::fromJsonValue(m_live_embed_url, json[QString("live_embed_url")]);
    m_live_embed_url_isSet = !json[QString("live_embed_url")].isNull() && m_live_embed_url_isValid;

    m_match_type_isValid = ::OpenAPI::fromJsonValue(m_match_type, json[QString("match_type")]);
    m_match_type_isSet = !json[QString("match_type")].isNull() && m_match_type_isValid;

    m_modified_at_isValid = ::OpenAPI::fromJsonValue(m_modified_at, json[QString("modified_at")]);
    m_modified_at_isSet = !json[QString("modified_at")].isNull() && m_modified_at_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_number_of_games_isValid = ::OpenAPI::fromJsonValue(m_number_of_games, json[QString("number_of_games")]);
    m_number_of_games_isSet = !json[QString("number_of_games")].isNull() && m_number_of_games_isValid;

    m_official_stream_url_isValid = ::OpenAPI::fromJsonValue(m_official_stream_url, json[QString("official_stream_url")]);
    m_official_stream_url_isSet = !json[QString("official_stream_url")].isNull() && m_official_stream_url_isValid;

    m_opponents_isValid = ::OpenAPI::fromJsonValue(m_opponents, json[QString("opponents")]);
    m_opponents_isSet = !json[QString("opponents")].isNull() && m_opponents_isValid;

    m_original_scheduled_at_isValid = ::OpenAPI::fromJsonValue(m_original_scheduled_at, json[QString("original_scheduled_at")]);
    m_original_scheduled_at_isSet = !json[QString("original_scheduled_at")].isNull() && m_original_scheduled_at_isValid;

    m_rescheduled_isValid = ::OpenAPI::fromJsonValue(m_rescheduled, json[QString("rescheduled")]);
    m_rescheduled_isSet = !json[QString("rescheduled")].isNull() && m_rescheduled_isValid;

    m_results_isValid = ::OpenAPI::fromJsonValue(m_results, json[QString("results")]);
    m_results_isSet = !json[QString("results")].isNull() && m_results_isValid;

    m_scheduled_at_isValid = ::OpenAPI::fromJsonValue(m_scheduled_at, json[QString("scheduled_at")]);
    m_scheduled_at_isSet = !json[QString("scheduled_at")].isNull() && m_scheduled_at_isValid;

    m_serie_isValid = ::OpenAPI::fromJsonValue(m_serie, json[QString("serie")]);
    m_serie_isSet = !json[QString("serie")].isNull() && m_serie_isValid;

    m_serie_id_isValid = ::OpenAPI::fromJsonValue(m_serie_id, json[QString("serie_id")]);
    m_serie_id_isSet = !json[QString("serie_id")].isNull() && m_serie_id_isValid;

    m_slug_isValid = ::OpenAPI::fromJsonValue(m_slug, json[QString("slug")]);
    m_slug_isSet = !json[QString("slug")].isNull() && m_slug_isValid;

    m_status_isValid = ::OpenAPI::fromJsonValue(m_status, json[QString("status")]);
    m_status_isSet = !json[QString("status")].isNull() && m_status_isValid;

    m_streams_isValid = ::OpenAPI::fromJsonValue(m_streams, json[QString("streams")]);
    m_streams_isSet = !json[QString("streams")].isNull() && m_streams_isValid;

    m_streams_list_isValid = ::OpenAPI::fromJsonValue(m_streams_list, json[QString("streams_list")]);
    m_streams_list_isSet = !json[QString("streams_list")].isNull() && m_streams_list_isValid;

    m_tournament_isValid = ::OpenAPI::fromJsonValue(m_tournament, json[QString("tournament")]);
    m_tournament_isSet = !json[QString("tournament")].isNull() && m_tournament_isValid;

    m_tournament_id_isValid = ::OpenAPI::fromJsonValue(m_tournament_id, json[QString("tournament_id")]);
    m_tournament_id_isSet = !json[QString("tournament_id")].isNull() && m_tournament_id_isValid;

    m_videogame_isValid = ::OpenAPI::fromJsonValue(m_videogame, json[QString("videogame")]);
    m_videogame_isSet = !json[QString("videogame")].isNull() && m_videogame_isValid;

    m_videogame_version_isValid = ::OpenAPI::fromJsonValue(m_videogame_version, json[QString("videogame_version")]);
    m_videogame_version_isSet = !json[QString("videogame_version")].isNull() && m_videogame_version_isValid;

    m_winner_isValid = ::OpenAPI::fromJsonValue(m_winner, json[QString("winner")]);
    m_winner_isSet = !json[QString("winner")].isNull() && m_winner_isValid;

    m_winner_id_isValid = ::OpenAPI::fromJsonValue(m_winner_id, json[QString("winner_id")]);
    m_winner_id_isSet = !json[QString("winner_id")].isNull() && m_winner_id_isValid;
}

QString OAIBettingMatch::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIBettingMatch::asJsonObject() const {
    QJsonObject obj;
    if (m_begin_at.isSet()) {
        obj.insert(QString("begin_at"), ::OpenAPI::toJsonValue(m_begin_at));
    }
    if (m_betting_metadata.isSet()) {
        obj.insert(QString("betting_metadata"), ::OpenAPI::toJsonValue(m_betting_metadata));
    }
    if (m_detailed_stats_isSet) {
        obj.insert(QString("detailed_stats"), ::OpenAPI::toJsonValue(m_detailed_stats));
    }
    if (m_draw_isSet) {
        obj.insert(QString("draw"), ::OpenAPI::toJsonValue(m_draw));
    }
    if (m_end_at.isSet()) {
        obj.insert(QString("end_at"), ::OpenAPI::toJsonValue(m_end_at));
    }
    if (m_forfeit_isSet) {
        obj.insert(QString("forfeit"), ::OpenAPI::toJsonValue(m_forfeit));
    }
    if (m_game_advantage.isSet()) {
        obj.insert(QString("game_advantage"), ::OpenAPI::toJsonValue(m_game_advantage));
    }
    if (m_games.size() > 0) {
        obj.insert(QString("games"), ::OpenAPI::toJsonValue(m_games));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_league.isSet()) {
        obj.insert(QString("league"), ::OpenAPI::toJsonValue(m_league));
    }
    if (m_league_id_isSet) {
        obj.insert(QString("league_id"), ::OpenAPI::toJsonValue(m_league_id));
    }
    if (m_live.isSet()) {
        obj.insert(QString("live"), ::OpenAPI::toJsonValue(m_live));
    }
    if (m_live_embed_url.isSet()) {
        obj.insert(QString("live_embed_url"), ::OpenAPI::toJsonValue(m_live_embed_url));
    }
    if (m_match_type.isSet()) {
        obj.insert(QString("match_type"), ::OpenAPI::toJsonValue(m_match_type));
    }
    if (m_modified_at_isSet) {
        obj.insert(QString("modified_at"), ::OpenAPI::toJsonValue(m_modified_at));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_number_of_games_isSet) {
        obj.insert(QString("number_of_games"), ::OpenAPI::toJsonValue(m_number_of_games));
    }
    if (m_official_stream_url.isSet()) {
        obj.insert(QString("official_stream_url"), ::OpenAPI::toJsonValue(m_official_stream_url));
    }
    if (m_opponents.size() > 0) {
        obj.insert(QString("opponents"), ::OpenAPI::toJsonValue(m_opponents));
    }
    if (m_original_scheduled_at.isSet()) {
        obj.insert(QString("original_scheduled_at"), ::OpenAPI::toJsonValue(m_original_scheduled_at));
    }
    if (m_rescheduled.isSet()) {
        obj.insert(QString("rescheduled"), ::OpenAPI::toJsonValue(m_rescheduled));
    }
    if (m_results.size() > 0) {
        obj.insert(QString("results"), ::OpenAPI::toJsonValue(m_results));
    }
    if (m_scheduled_at.isSet()) {
        obj.insert(QString("scheduled_at"), ::OpenAPI::toJsonValue(m_scheduled_at));
    }
    if (m_serie.isSet()) {
        obj.insert(QString("serie"), ::OpenAPI::toJsonValue(m_serie));
    }
    if (m_serie_id_isSet) {
        obj.insert(QString("serie_id"), ::OpenAPI::toJsonValue(m_serie_id));
    }
    if (m_slug.isSet()) {
        obj.insert(QString("slug"), ::OpenAPI::toJsonValue(m_slug));
    }
    if (m_status.isSet()) {
        obj.insert(QString("status"), ::OpenAPI::toJsonValue(m_status));
    }
    if (m_streams.isSet()) {
        obj.insert(QString("streams"), ::OpenAPI::toJsonValue(m_streams));
    }
    if (m_streams_list.size() > 0) {
        obj.insert(QString("streams_list"), ::OpenAPI::toJsonValue(m_streams_list));
    }
    if (m_tournament.isSet()) {
        obj.insert(QString("tournament"), ::OpenAPI::toJsonValue(m_tournament));
    }
    if (m_tournament_id_isSet) {
        obj.insert(QString("tournament_id"), ::OpenAPI::toJsonValue(m_tournament_id));
    }
    if (m_videogame.isSet()) {
        obj.insert(QString("videogame"), ::OpenAPI::toJsonValue(m_videogame));
    }
    if (m_videogame_version.isSet()) {
        obj.insert(QString("videogame_version"), ::OpenAPI::toJsonValue(m_videogame_version));
    }
    if (m_winner.isSet()) {
        obj.insert(QString("winner"), ::OpenAPI::toJsonValue(m_winner));
    }
    if (m_winner_id.isSet()) {
        obj.insert(QString("winner_id"), ::OpenAPI::toJsonValue(m_winner_id));
    }
    return obj;
}

QJsonValue OAIBettingMatch::getBeginAt() const {
    return m_begin_at;
}
void OAIBettingMatch::setBeginAt(const QJsonValue &begin_at) {
    m_begin_at = begin_at;
    m_begin_at_isSet = true;
}

bool OAIBettingMatch::is_begin_at_Set() const{
    return m_begin_at_isSet;
}

bool OAIBettingMatch::is_begin_at_Valid() const{
    return m_begin_at_isValid;
}

OAIBettingMetadata OAIBettingMatch::getBettingMetadata() const {
    return m_betting_metadata;
}
void OAIBettingMatch::setBettingMetadata(const OAIBettingMetadata &betting_metadata) {
    m_betting_metadata = betting_metadata;
    m_betting_metadata_isSet = true;
}

bool OAIBettingMatch::is_betting_metadata_Set() const{
    return m_betting_metadata_isSet;
}

bool OAIBettingMatch::is_betting_metadata_Valid() const{
    return m_betting_metadata_isValid;
}

bool OAIBettingMatch::isDetailedStats() const {
    return m_detailed_stats;
}
void OAIBettingMatch::setDetailedStats(const bool &detailed_stats) {
    m_detailed_stats = detailed_stats;
    m_detailed_stats_isSet = true;
}

bool OAIBettingMatch::is_detailed_stats_Set() const{
    return m_detailed_stats_isSet;
}

bool OAIBettingMatch::is_detailed_stats_Valid() const{
    return m_detailed_stats_isValid;
}

bool OAIBettingMatch::isDraw() const {
    return m_draw;
}
void OAIBettingMatch::setDraw(const bool &draw) {
    m_draw = draw;
    m_draw_isSet = true;
}

bool OAIBettingMatch::is_draw_Set() const{
    return m_draw_isSet;
}

bool OAIBettingMatch::is_draw_Valid() const{
    return m_draw_isValid;
}

QJsonValue OAIBettingMatch::getEndAt() const {
    return m_end_at;
}
void OAIBettingMatch::setEndAt(const QJsonValue &end_at) {
    m_end_at = end_at;
    m_end_at_isSet = true;
}

bool OAIBettingMatch::is_end_at_Set() const{
    return m_end_at_isSet;
}

bool OAIBettingMatch::is_end_at_Valid() const{
    return m_end_at_isValid;
}

bool OAIBettingMatch::isForfeit() const {
    return m_forfeit;
}
void OAIBettingMatch::setForfeit(const bool &forfeit) {
    m_forfeit = forfeit;
    m_forfeit_isSet = true;
}

bool OAIBettingMatch::is_forfeit_Set() const{
    return m_forfeit_isSet;
}

bool OAIBettingMatch::is_forfeit_Valid() const{
    return m_forfeit_isValid;
}

OAIOpponentID_1 OAIBettingMatch::getGameAdvantage() const {
    return m_game_advantage;
}
void OAIBettingMatch::setGameAdvantage(const OAIOpponentID_1 &game_advantage) {
    m_game_advantage = game_advantage;
    m_game_advantage_isSet = true;
}

bool OAIBettingMatch::is_game_advantage_Set() const{
    return m_game_advantage_isSet;
}

bool OAIBettingMatch::is_game_advantage_Valid() const{
    return m_game_advantage_isValid;
}

QList<OAIBettingGame> OAIBettingMatch::getGames() const {
    return m_games;
}
void OAIBettingMatch::setGames(const QList<OAIBettingGame> &games) {
    m_games = games;
    m_games_isSet = true;
}

bool OAIBettingMatch::is_games_Set() const{
    return m_games_isSet;
}

bool OAIBettingMatch::is_games_Valid() const{
    return m_games_isValid;
}

qint32 OAIBettingMatch::getId() const {
    return m_id;
}
void OAIBettingMatch::setId(const qint32 &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIBettingMatch::is_id_Set() const{
    return m_id_isSet;
}

bool OAIBettingMatch::is_id_Valid() const{
    return m_id_isValid;
}

OAIBettingLeague_1 OAIBettingMatch::getLeague() const {
    return m_league;
}
void OAIBettingMatch::setLeague(const OAIBettingLeague_1 &league) {
    m_league = league;
    m_league_isSet = true;
}

bool OAIBettingMatch::is_league_Set() const{
    return m_league_isSet;
}

bool OAIBettingMatch::is_league_Valid() const{
    return m_league_isValid;
}

qint32 OAIBettingMatch::getLeagueId() const {
    return m_league_id;
}
void OAIBettingMatch::setLeagueId(const qint32 &league_id) {
    m_league_id = league_id;
    m_league_id_isSet = true;
}

bool OAIBettingMatch::is_league_id_Set() const{
    return m_league_id_isSet;
}

bool OAIBettingMatch::is_league_id_Valid() const{
    return m_league_id_isValid;
}

OAIMatchLive OAIBettingMatch::getLive() const {
    return m_live;
}
void OAIBettingMatch::setLive(const OAIMatchLive &live) {
    m_live = live;
    m_live_isSet = true;
}

bool OAIBettingMatch::is_live_Set() const{
    return m_live_isSet;
}

bool OAIBettingMatch::is_live_Valid() const{
    return m_live_isValid;
}

QJsonValue OAIBettingMatch::getLiveEmbedUrl() const {
    return m_live_embed_url;
}
void OAIBettingMatch::setLiveEmbedUrl(const QJsonValue &live_embed_url) {
    m_live_embed_url = live_embed_url;
    m_live_embed_url_isSet = true;
}

bool OAIBettingMatch::is_live_embed_url_Set() const{
    return m_live_embed_url_isSet;
}

bool OAIBettingMatch::is_live_embed_url_Valid() const{
    return m_live_embed_url_isValid;
}

OAIMatchType OAIBettingMatch::getMatchType() const {
    return m_match_type;
}
void OAIBettingMatch::setMatchType(const OAIMatchType &match_type) {
    m_match_type = match_type;
    m_match_type_isSet = true;
}

bool OAIBettingMatch::is_match_type_Set() const{
    return m_match_type_isSet;
}

bool OAIBettingMatch::is_match_type_Valid() const{
    return m_match_type_isValid;
}

QDateTime OAIBettingMatch::getModifiedAt() const {
    return m_modified_at;
}
void OAIBettingMatch::setModifiedAt(const QDateTime &modified_at) {
    m_modified_at = modified_at;
    m_modified_at_isSet = true;
}

bool OAIBettingMatch::is_modified_at_Set() const{
    return m_modified_at_isSet;
}

bool OAIBettingMatch::is_modified_at_Valid() const{
    return m_modified_at_isValid;
}

QString OAIBettingMatch::getName() const {
    return m_name;
}
void OAIBettingMatch::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIBettingMatch::is_name_Set() const{
    return m_name_isSet;
}

bool OAIBettingMatch::is_name_Valid() const{
    return m_name_isValid;
}

qint32 OAIBettingMatch::getNumberOfGames() const {
    return m_number_of_games;
}
void OAIBettingMatch::setNumberOfGames(const qint32 &number_of_games) {
    m_number_of_games = number_of_games;
    m_number_of_games_isSet = true;
}

bool OAIBettingMatch::is_number_of_games_Set() const{
    return m_number_of_games_isSet;
}

bool OAIBettingMatch::is_number_of_games_Valid() const{
    return m_number_of_games_isValid;
}

QJsonValue OAIBettingMatch::getOfficialStreamUrl() const {
    return m_official_stream_url;
}
void OAIBettingMatch::setOfficialStreamUrl(const QJsonValue &official_stream_url) {
    m_official_stream_url = official_stream_url;
    m_official_stream_url_isSet = true;
}

bool OAIBettingMatch::is_official_stream_url_Set() const{
    return m_official_stream_url_isSet;
}

bool OAIBettingMatch::is_official_stream_url_Valid() const{
    return m_official_stream_url_isValid;
}

QList<OAIOpponent> OAIBettingMatch::getOpponents() const {
    return m_opponents;
}
void OAIBettingMatch::setOpponents(const QList<OAIOpponent> &opponents) {
    m_opponents = opponents;
    m_opponents_isSet = true;
}

bool OAIBettingMatch::is_opponents_Set() const{
    return m_opponents_isSet;
}

bool OAIBettingMatch::is_opponents_Valid() const{
    return m_opponents_isValid;
}

QJsonValue OAIBettingMatch::getOriginalScheduledAt() const {
    return m_original_scheduled_at;
}
void OAIBettingMatch::setOriginalScheduledAt(const QJsonValue &original_scheduled_at) {
    m_original_scheduled_at = original_scheduled_at;
    m_original_scheduled_at_isSet = true;
}

bool OAIBettingMatch::is_original_scheduled_at_Set() const{
    return m_original_scheduled_at_isSet;
}

bool OAIBettingMatch::is_original_scheduled_at_Valid() const{
    return m_original_scheduled_at_isValid;
}

QJsonValue OAIBettingMatch::getRescheduled() const {
    return m_rescheduled;
}
void OAIBettingMatch::setRescheduled(const QJsonValue &rescheduled) {
    m_rescheduled = rescheduled;
    m_rescheduled_isSet = true;
}

bool OAIBettingMatch::is_rescheduled_Set() const{
    return m_rescheduled_isSet;
}

bool OAIBettingMatch::is_rescheduled_Valid() const{
    return m_rescheduled_isValid;
}

QList<OAIMatchResult> OAIBettingMatch::getResults() const {
    return m_results;
}
void OAIBettingMatch::setResults(const QList<OAIMatchResult> &results) {
    m_results = results;
    m_results_isSet = true;
}

bool OAIBettingMatch::is_results_Set() const{
    return m_results_isSet;
}

bool OAIBettingMatch::is_results_Valid() const{
    return m_results_isValid;
}

QJsonValue OAIBettingMatch::getScheduledAt() const {
    return m_scheduled_at;
}
void OAIBettingMatch::setScheduledAt(const QJsonValue &scheduled_at) {
    m_scheduled_at = scheduled_at;
    m_scheduled_at_isSet = true;
}

bool OAIBettingMatch::is_scheduled_at_Set() const{
    return m_scheduled_at_isSet;
}

bool OAIBettingMatch::is_scheduled_at_Valid() const{
    return m_scheduled_at_isValid;
}

OAIBettingSerie_1 OAIBettingMatch::getSerie() const {
    return m_serie;
}
void OAIBettingMatch::setSerie(const OAIBettingSerie_1 &serie) {
    m_serie = serie;
    m_serie_isSet = true;
}

bool OAIBettingMatch::is_serie_Set() const{
    return m_serie_isSet;
}

bool OAIBettingMatch::is_serie_Valid() const{
    return m_serie_isValid;
}

qint32 OAIBettingMatch::getSerieId() const {
    return m_serie_id;
}
void OAIBettingMatch::setSerieId(const qint32 &serie_id) {
    m_serie_id = serie_id;
    m_serie_id_isSet = true;
}

bool OAIBettingMatch::is_serie_id_Set() const{
    return m_serie_id_isSet;
}

bool OAIBettingMatch::is_serie_id_Valid() const{
    return m_serie_id_isValid;
}

QJsonValue OAIBettingMatch::getSlug() const {
    return m_slug;
}
void OAIBettingMatch::setSlug(const QJsonValue &slug) {
    m_slug = slug;
    m_slug_isSet = true;
}

bool OAIBettingMatch::is_slug_Set() const{
    return m_slug_isSet;
}

bool OAIBettingMatch::is_slug_Valid() const{
    return m_slug_isValid;
}

OAIBettingMatchStatus OAIBettingMatch::getStatus() const {
    return m_status;
}
void OAIBettingMatch::setStatus(const OAIBettingMatchStatus &status) {
    m_status = status;
    m_status_isSet = true;
}

bool OAIBettingMatch::is_status_Set() const{
    return m_status_isSet;
}

bool OAIBettingMatch::is_status_Valid() const{
    return m_status_isValid;
}

OAIMatchLocalizedStreams OAIBettingMatch::getStreams() const {
    return m_streams;
}
void OAIBettingMatch::setStreams(const OAIMatchLocalizedStreams &streams) {
    m_streams = streams;
    m_streams_isSet = true;
}

bool OAIBettingMatch::is_streams_Set() const{
    return m_streams_isSet;
}

bool OAIBettingMatch::is_streams_Valid() const{
    return m_streams_isValid;
}

QList<OAIStream> OAIBettingMatch::getStreamsList() const {
    return m_streams_list;
}
void OAIBettingMatch::setStreamsList(const QList<OAIStream> &streams_list) {
    m_streams_list = streams_list;
    m_streams_list_isSet = true;
}

bool OAIBettingMatch::is_streams_list_Set() const{
    return m_streams_list_isSet;
}

bool OAIBettingMatch::is_streams_list_Valid() const{
    return m_streams_list_isValid;
}

OAIBettingBaseTournament OAIBettingMatch::getTournament() const {
    return m_tournament;
}
void OAIBettingMatch::setTournament(const OAIBettingBaseTournament &tournament) {
    m_tournament = tournament;
    m_tournament_isSet = true;
}

bool OAIBettingMatch::is_tournament_Set() const{
    return m_tournament_isSet;
}

bool OAIBettingMatch::is_tournament_Valid() const{
    return m_tournament_isValid;
}

qint32 OAIBettingMatch::getTournamentId() const {
    return m_tournament_id;
}
void OAIBettingMatch::setTournamentId(const qint32 &tournament_id) {
    m_tournament_id = tournament_id;
    m_tournament_id_isSet = true;
}

bool OAIBettingMatch::is_tournament_id_Set() const{
    return m_tournament_id_isSet;
}

bool OAIBettingMatch::is_tournament_id_Valid() const{
    return m_tournament_id_isValid;
}

OAICurrentVideogame OAIBettingMatch::getVideogame() const {
    return m_videogame;
}
void OAIBettingMatch::setVideogame(const OAICurrentVideogame &videogame) {
    m_videogame = videogame;
    m_videogame_isSet = true;
}

bool OAIBettingMatch::is_videogame_Set() const{
    return m_videogame_isSet;
}

bool OAIBettingMatch::is_videogame_Valid() const{
    return m_videogame_isValid;
}

OAIShortVideogameVersion_1 OAIBettingMatch::getVideogameVersion() const {
    return m_videogame_version;
}
void OAIBettingMatch::setVideogameVersion(const OAIShortVideogameVersion_1 &videogame_version) {
    m_videogame_version = videogame_version;
    m_videogame_version_isSet = true;
}

bool OAIBettingMatch::is_videogame_version_Set() const{
    return m_videogame_version_isSet;
}

bool OAIBettingMatch::is_videogame_version_Valid() const{
    return m_videogame_version_isValid;
}

OAIBaseOpponent_1 OAIBettingMatch::getWinner() const {
    return m_winner;
}
void OAIBettingMatch::setWinner(const OAIBaseOpponent_1 &winner) {
    m_winner = winner;
    m_winner_isSet = true;
}

bool OAIBettingMatch::is_winner_Set() const{
    return m_winner_isSet;
}

bool OAIBettingMatch::is_winner_Valid() const{
    return m_winner_isValid;
}

OAIOpponentID_1 OAIBettingMatch::getWinnerId() const {
    return m_winner_id;
}
void OAIBettingMatch::setWinnerId(const OAIOpponentID_1 &winner_id) {
    m_winner_id = winner_id;
    m_winner_id_isSet = true;
}

bool OAIBettingMatch::is_winner_id_Set() const{
    return m_winner_id_isSet;
}

bool OAIBettingMatch::is_winner_id_Valid() const{
    return m_winner_id_isValid;
}

bool OAIBettingMatch::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_begin_at.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_betting_metadata.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_detailed_stats_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_draw_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_end_at.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_forfeit_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_game_advantage.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_games.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_league.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_league_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_live.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_live_embed_url.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_match_type.isSet()) {
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

        if (m_number_of_games_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_official_stream_url.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_opponents.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_original_scheduled_at.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_rescheduled.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_results.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_scheduled_at.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_serie.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_serie_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_slug.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_status.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_streams.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_streams_list.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_tournament.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_tournament_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_videogame.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_videogame_version.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_winner.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_winner_id.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIBettingMatch::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_begin_at_isValid && m_betting_metadata_isValid && m_detailed_stats_isValid && m_draw_isValid && m_end_at_isValid && m_forfeit_isValid && m_game_advantage_isValid && m_games_isValid && m_id_isValid && m_league_isValid && m_league_id_isValid && m_live_isValid && m_live_embed_url_isValid && m_match_type_isValid && m_modified_at_isValid && m_name_isValid && m_number_of_games_isValid && m_official_stream_url_isValid && m_opponents_isValid && m_original_scheduled_at_isValid && m_rescheduled_isValid && m_results_isValid && m_scheduled_at_isValid && m_serie_isValid && m_serie_id_isValid && m_slug_isValid && m_status_isValid && m_streams_isValid && m_streams_list_isValid && m_tournament_isValid && m_tournament_id_isValid && m_videogame_isValid && m_videogame_version_isValid && m_winner_isValid && m_winner_id_isValid && true;
}

} // namespace OpenAPI
