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

#include "OAIBettingLoLGameTeam.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIBettingLoLGameTeam::OAIBettingLoLGameTeam(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIBettingLoLGameTeam::OAIBettingLoLGameTeam() {
    this->initializeModel();
}

OAIBettingLoLGameTeam::~OAIBettingLoLGameTeam() {}

void OAIBettingLoLGameTeam::initializeModel() {

    m_baron_kills_isSet = false;
    m_baron_kills_isValid = false;

    m_color_isSet = false;
    m_color_isValid = false;

    m_dragon_kills_isSet = false;
    m_dragon_kills_isValid = false;

    m_first_baron_isSet = false;
    m_first_baron_isValid = false;

    m_first_blood_isSet = false;
    m_first_blood_isValid = false;

    m_first_dragon_isSet = false;
    m_first_dragon_isValid = false;

    m_first_herald_isSet = false;
    m_first_herald_isValid = false;

    m_first_inhibitor_isSet = false;
    m_first_inhibitor_isValid = false;

    m_first_tower_isSet = false;
    m_first_tower_isValid = false;

    m_gold_earned_isSet = false;
    m_gold_earned_isValid = false;

    m_herald_kill_isSet = false;
    m_herald_kill_isValid = false;

    m_inhibitor_kills_isSet = false;
    m_inhibitor_kills_isValid = false;

    m_team_id_isSet = false;
    m_team_id_isValid = false;

    m_team_kills_isSet = false;
    m_team_kills_isValid = false;

    m_tower_kills_isSet = false;
    m_tower_kills_isValid = false;
}

void OAIBettingLoLGameTeam::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIBettingLoLGameTeam::fromJsonObject(QJsonObject json) {

    m_baron_kills_isValid = ::OpenAPI::fromJsonValue(m_baron_kills, json[QString("baron_kills")]);
    m_baron_kills_isSet = !json[QString("baron_kills")].isNull() && m_baron_kills_isValid;

    m_color_isValid = ::OpenAPI::fromJsonValue(m_color, json[QString("color")]);
    m_color_isSet = !json[QString("color")].isNull() && m_color_isValid;

    m_dragon_kills_isValid = ::OpenAPI::fromJsonValue(m_dragon_kills, json[QString("dragon_kills")]);
    m_dragon_kills_isSet = !json[QString("dragon_kills")].isNull() && m_dragon_kills_isValid;

    m_first_baron_isValid = ::OpenAPI::fromJsonValue(m_first_baron, json[QString("first_baron")]);
    m_first_baron_isSet = !json[QString("first_baron")].isNull() && m_first_baron_isValid;

    m_first_blood_isValid = ::OpenAPI::fromJsonValue(m_first_blood, json[QString("first_blood")]);
    m_first_blood_isSet = !json[QString("first_blood")].isNull() && m_first_blood_isValid;

    m_first_dragon_isValid = ::OpenAPI::fromJsonValue(m_first_dragon, json[QString("first_dragon")]);
    m_first_dragon_isSet = !json[QString("first_dragon")].isNull() && m_first_dragon_isValid;

    m_first_herald_isValid = ::OpenAPI::fromJsonValue(m_first_herald, json[QString("first_herald")]);
    m_first_herald_isSet = !json[QString("first_herald")].isNull() && m_first_herald_isValid;

    m_first_inhibitor_isValid = ::OpenAPI::fromJsonValue(m_first_inhibitor, json[QString("first_inhibitor")]);
    m_first_inhibitor_isSet = !json[QString("first_inhibitor")].isNull() && m_first_inhibitor_isValid;

    m_first_tower_isValid = ::OpenAPI::fromJsonValue(m_first_tower, json[QString("first_tower")]);
    m_first_tower_isSet = !json[QString("first_tower")].isNull() && m_first_tower_isValid;

    m_gold_earned_isValid = ::OpenAPI::fromJsonValue(m_gold_earned, json[QString("gold_earned")]);
    m_gold_earned_isSet = !json[QString("gold_earned")].isNull() && m_gold_earned_isValid;

    m_herald_kill_isValid = ::OpenAPI::fromJsonValue(m_herald_kill, json[QString("herald_kill")]);
    m_herald_kill_isSet = !json[QString("herald_kill")].isNull() && m_herald_kill_isValid;

    m_inhibitor_kills_isValid = ::OpenAPI::fromJsonValue(m_inhibitor_kills, json[QString("inhibitor_kills")]);
    m_inhibitor_kills_isSet = !json[QString("inhibitor_kills")].isNull() && m_inhibitor_kills_isValid;

    m_team_id_isValid = ::OpenAPI::fromJsonValue(m_team_id, json[QString("team_id")]);
    m_team_id_isSet = !json[QString("team_id")].isNull() && m_team_id_isValid;

    m_team_kills_isValid = ::OpenAPI::fromJsonValue(m_team_kills, json[QString("team_kills")]);
    m_team_kills_isSet = !json[QString("team_kills")].isNull() && m_team_kills_isValid;

    m_tower_kills_isValid = ::OpenAPI::fromJsonValue(m_tower_kills, json[QString("tower_kills")]);
    m_tower_kills_isSet = !json[QString("tower_kills")].isNull() && m_tower_kills_isValid;
}

QString OAIBettingLoLGameTeam::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIBettingLoLGameTeam::asJsonObject() const {
    QJsonObject obj;
    if (m_baron_kills.isSet()) {
        obj.insert(QString("baron_kills"), ::OpenAPI::toJsonValue(m_baron_kills));
    }
    if (m_color.isSet()) {
        obj.insert(QString("color"), ::OpenAPI::toJsonValue(m_color));
    }
    if (m_dragon_kills.isSet()) {
        obj.insert(QString("dragon_kills"), ::OpenAPI::toJsonValue(m_dragon_kills));
    }
    if (m_first_baron.isSet()) {
        obj.insert(QString("first_baron"), ::OpenAPI::toJsonValue(m_first_baron));
    }
    if (m_first_blood.isSet()) {
        obj.insert(QString("first_blood"), ::OpenAPI::toJsonValue(m_first_blood));
    }
    if (m_first_dragon.isSet()) {
        obj.insert(QString("first_dragon"), ::OpenAPI::toJsonValue(m_first_dragon));
    }
    if (m_first_herald.isSet()) {
        obj.insert(QString("first_herald"), ::OpenAPI::toJsonValue(m_first_herald));
    }
    if (m_first_inhibitor.isSet()) {
        obj.insert(QString("first_inhibitor"), ::OpenAPI::toJsonValue(m_first_inhibitor));
    }
    if (m_first_tower.isSet()) {
        obj.insert(QString("first_tower"), ::OpenAPI::toJsonValue(m_first_tower));
    }
    if (m_gold_earned.isSet()) {
        obj.insert(QString("gold_earned"), ::OpenAPI::toJsonValue(m_gold_earned));
    }
    if (m_herald_kill.isSet()) {
        obj.insert(QString("herald_kill"), ::OpenAPI::toJsonValue(m_herald_kill));
    }
    if (m_inhibitor_kills.isSet()) {
        obj.insert(QString("inhibitor_kills"), ::OpenAPI::toJsonValue(m_inhibitor_kills));
    }
    if (m_team_id_isSet) {
        obj.insert(QString("team_id"), ::OpenAPI::toJsonValue(m_team_id));
    }
    if (m_team_kills.isSet()) {
        obj.insert(QString("team_kills"), ::OpenAPI::toJsonValue(m_team_kills));
    }
    if (m_tower_kills.isSet()) {
        obj.insert(QString("tower_kills"), ::OpenAPI::toJsonValue(m_tower_kills));
    }
    return obj;
}

QJsonValue OAIBettingLoLGameTeam::getBaronKills() const {
    return m_baron_kills;
}
void OAIBettingLoLGameTeam::setBaronKills(const QJsonValue &baron_kills) {
    m_baron_kills = baron_kills;
    m_baron_kills_isSet = true;
}

bool OAIBettingLoLGameTeam::is_baron_kills_Set() const{
    return m_baron_kills_isSet;
}

bool OAIBettingLoLGameTeam::is_baron_kills_Valid() const{
    return m_baron_kills_isValid;
}

OAILoLTeamColor OAIBettingLoLGameTeam::getColor() const {
    return m_color;
}
void OAIBettingLoLGameTeam::setColor(const OAILoLTeamColor &color) {
    m_color = color;
    m_color_isSet = true;
}

bool OAIBettingLoLGameTeam::is_color_Set() const{
    return m_color_isSet;
}

bool OAIBettingLoLGameTeam::is_color_Valid() const{
    return m_color_isValid;
}

QJsonValue OAIBettingLoLGameTeam::getDragonKills() const {
    return m_dragon_kills;
}
void OAIBettingLoLGameTeam::setDragonKills(const QJsonValue &dragon_kills) {
    m_dragon_kills = dragon_kills;
    m_dragon_kills_isSet = true;
}

bool OAIBettingLoLGameTeam::is_dragon_kills_Set() const{
    return m_dragon_kills_isSet;
}

bool OAIBettingLoLGameTeam::is_dragon_kills_Valid() const{
    return m_dragon_kills_isValid;
}

QJsonValue OAIBettingLoLGameTeam::getFirstBaron() const {
    return m_first_baron;
}
void OAIBettingLoLGameTeam::setFirstBaron(const QJsonValue &first_baron) {
    m_first_baron = first_baron;
    m_first_baron_isSet = true;
}

bool OAIBettingLoLGameTeam::is_first_baron_Set() const{
    return m_first_baron_isSet;
}

bool OAIBettingLoLGameTeam::is_first_baron_Valid() const{
    return m_first_baron_isValid;
}

QJsonValue OAIBettingLoLGameTeam::getFirstBlood() const {
    return m_first_blood;
}
void OAIBettingLoLGameTeam::setFirstBlood(const QJsonValue &first_blood) {
    m_first_blood = first_blood;
    m_first_blood_isSet = true;
}

bool OAIBettingLoLGameTeam::is_first_blood_Set() const{
    return m_first_blood_isSet;
}

bool OAIBettingLoLGameTeam::is_first_blood_Valid() const{
    return m_first_blood_isValid;
}

QJsonValue OAIBettingLoLGameTeam::getFirstDragon() const {
    return m_first_dragon;
}
void OAIBettingLoLGameTeam::setFirstDragon(const QJsonValue &first_dragon) {
    m_first_dragon = first_dragon;
    m_first_dragon_isSet = true;
}

bool OAIBettingLoLGameTeam::is_first_dragon_Set() const{
    return m_first_dragon_isSet;
}

bool OAIBettingLoLGameTeam::is_first_dragon_Valid() const{
    return m_first_dragon_isValid;
}

QJsonValue OAIBettingLoLGameTeam::getFirstHerald() const {
    return m_first_herald;
}
void OAIBettingLoLGameTeam::setFirstHerald(const QJsonValue &first_herald) {
    m_first_herald = first_herald;
    m_first_herald_isSet = true;
}

bool OAIBettingLoLGameTeam::is_first_herald_Set() const{
    return m_first_herald_isSet;
}

bool OAIBettingLoLGameTeam::is_first_herald_Valid() const{
    return m_first_herald_isValid;
}

QJsonValue OAIBettingLoLGameTeam::getFirstInhibitor() const {
    return m_first_inhibitor;
}
void OAIBettingLoLGameTeam::setFirstInhibitor(const QJsonValue &first_inhibitor) {
    m_first_inhibitor = first_inhibitor;
    m_first_inhibitor_isSet = true;
}

bool OAIBettingLoLGameTeam::is_first_inhibitor_Set() const{
    return m_first_inhibitor_isSet;
}

bool OAIBettingLoLGameTeam::is_first_inhibitor_Valid() const{
    return m_first_inhibitor_isValid;
}

QJsonValue OAIBettingLoLGameTeam::getFirstTower() const {
    return m_first_tower;
}
void OAIBettingLoLGameTeam::setFirstTower(const QJsonValue &first_tower) {
    m_first_tower = first_tower;
    m_first_tower_isSet = true;
}

bool OAIBettingLoLGameTeam::is_first_tower_Set() const{
    return m_first_tower_isSet;
}

bool OAIBettingLoLGameTeam::is_first_tower_Valid() const{
    return m_first_tower_isValid;
}

QJsonValue OAIBettingLoLGameTeam::getGoldEarned() const {
    return m_gold_earned;
}
void OAIBettingLoLGameTeam::setGoldEarned(const QJsonValue &gold_earned) {
    m_gold_earned = gold_earned;
    m_gold_earned_isSet = true;
}

bool OAIBettingLoLGameTeam::is_gold_earned_Set() const{
    return m_gold_earned_isSet;
}

bool OAIBettingLoLGameTeam::is_gold_earned_Valid() const{
    return m_gold_earned_isValid;
}

QJsonValue OAIBettingLoLGameTeam::getHeraldKill() const {
    return m_herald_kill;
}
void OAIBettingLoLGameTeam::setHeraldKill(const QJsonValue &herald_kill) {
    m_herald_kill = herald_kill;
    m_herald_kill_isSet = true;
}

bool OAIBettingLoLGameTeam::is_herald_kill_Set() const{
    return m_herald_kill_isSet;
}

bool OAIBettingLoLGameTeam::is_herald_kill_Valid() const{
    return m_herald_kill_isValid;
}

QJsonValue OAIBettingLoLGameTeam::getInhibitorKills() const {
    return m_inhibitor_kills;
}
void OAIBettingLoLGameTeam::setInhibitorKills(const QJsonValue &inhibitor_kills) {
    m_inhibitor_kills = inhibitor_kills;
    m_inhibitor_kills_isSet = true;
}

bool OAIBettingLoLGameTeam::is_inhibitor_kills_Set() const{
    return m_inhibitor_kills_isSet;
}

bool OAIBettingLoLGameTeam::is_inhibitor_kills_Valid() const{
    return m_inhibitor_kills_isValid;
}

qint32 OAIBettingLoLGameTeam::getTeamId() const {
    return m_team_id;
}
void OAIBettingLoLGameTeam::setTeamId(const qint32 &team_id) {
    m_team_id = team_id;
    m_team_id_isSet = true;
}

bool OAIBettingLoLGameTeam::is_team_id_Set() const{
    return m_team_id_isSet;
}

bool OAIBettingLoLGameTeam::is_team_id_Valid() const{
    return m_team_id_isValid;
}

QJsonValue OAIBettingLoLGameTeam::getTeamKills() const {
    return m_team_kills;
}
void OAIBettingLoLGameTeam::setTeamKills(const QJsonValue &team_kills) {
    m_team_kills = team_kills;
    m_team_kills_isSet = true;
}

bool OAIBettingLoLGameTeam::is_team_kills_Set() const{
    return m_team_kills_isSet;
}

bool OAIBettingLoLGameTeam::is_team_kills_Valid() const{
    return m_team_kills_isValid;
}

QJsonValue OAIBettingLoLGameTeam::getTowerKills() const {
    return m_tower_kills;
}
void OAIBettingLoLGameTeam::setTowerKills(const QJsonValue &tower_kills) {
    m_tower_kills = tower_kills;
    m_tower_kills_isSet = true;
}

bool OAIBettingLoLGameTeam::is_tower_kills_Set() const{
    return m_tower_kills_isSet;
}

bool OAIBettingLoLGameTeam::is_tower_kills_Valid() const{
    return m_tower_kills_isValid;
}

bool OAIBettingLoLGameTeam::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_baron_kills.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_color.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_dragon_kills.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_first_baron.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_first_blood.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_first_dragon.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_first_herald.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_first_inhibitor.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_first_tower.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_gold_earned.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_herald_kill.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_inhibitor_kills.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_team_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_team_kills.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_tower_kills.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIBettingLoLGameTeam::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_baron_kills_isValid && m_color_isValid && m_dragon_kills_isValid && m_first_baron_isValid && m_first_blood_isValid && m_first_dragon_isValid && m_first_herald_isValid && m_first_inhibitor_isValid && m_first_tower_isValid && m_gold_earned_isValid && m_herald_kill_isValid && m_inhibitor_kills_isValid && m_team_id_isValid && m_team_kills_isValid && m_tower_kills_isValid && true;
}

} // namespace OpenAPI
