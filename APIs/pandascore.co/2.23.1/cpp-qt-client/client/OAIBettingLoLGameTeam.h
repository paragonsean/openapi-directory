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

/*
 * OAIBettingLoLGameTeam.h
 *
 * Team&#39;s data for a Game
 */

#ifndef OAIBettingLoLGameTeam_H
#define OAIBettingLoLGameTeam_H

#include <QJsonObject>

#include "OAILoLTeamColor.h"
#include <QJsonValue>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIBettingLoLGameTeam : public OAIObject {
public:
    OAIBettingLoLGameTeam();
    OAIBettingLoLGameTeam(QString json);
    ~OAIBettingLoLGameTeam() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QJsonValue getBaronKills() const;
    void setBaronKills(const QJsonValue &baron_kills);
    bool is_baron_kills_Set() const;
    bool is_baron_kills_Valid() const;

    OAILoLTeamColor getColor() const;
    void setColor(const OAILoLTeamColor &color);
    bool is_color_Set() const;
    bool is_color_Valid() const;

    QJsonValue getDragonKills() const;
    void setDragonKills(const QJsonValue &dragon_kills);
    bool is_dragon_kills_Set() const;
    bool is_dragon_kills_Valid() const;

    QJsonValue getFirstBaron() const;
    void setFirstBaron(const QJsonValue &first_baron);
    bool is_first_baron_Set() const;
    bool is_first_baron_Valid() const;

    QJsonValue getFirstBlood() const;
    void setFirstBlood(const QJsonValue &first_blood);
    bool is_first_blood_Set() const;
    bool is_first_blood_Valid() const;

    QJsonValue getFirstDragon() const;
    void setFirstDragon(const QJsonValue &first_dragon);
    bool is_first_dragon_Set() const;
    bool is_first_dragon_Valid() const;

    QJsonValue getFirstHerald() const;
    void setFirstHerald(const QJsonValue &first_herald);
    bool is_first_herald_Set() const;
    bool is_first_herald_Valid() const;

    QJsonValue getFirstInhibitor() const;
    void setFirstInhibitor(const QJsonValue &first_inhibitor);
    bool is_first_inhibitor_Set() const;
    bool is_first_inhibitor_Valid() const;

    QJsonValue getFirstTower() const;
    void setFirstTower(const QJsonValue &first_tower);
    bool is_first_tower_Set() const;
    bool is_first_tower_Valid() const;

    QJsonValue getGoldEarned() const;
    void setGoldEarned(const QJsonValue &gold_earned);
    bool is_gold_earned_Set() const;
    bool is_gold_earned_Valid() const;

    QJsonValue getHeraldKill() const;
    void setHeraldKill(const QJsonValue &herald_kill);
    bool is_herald_kill_Set() const;
    bool is_herald_kill_Valid() const;

    QJsonValue getInhibitorKills() const;
    void setInhibitorKills(const QJsonValue &inhibitor_kills);
    bool is_inhibitor_kills_Set() const;
    bool is_inhibitor_kills_Valid() const;

    qint32 getTeamId() const;
    void setTeamId(const qint32 &team_id);
    bool is_team_id_Set() const;
    bool is_team_id_Valid() const;

    QJsonValue getTeamKills() const;
    void setTeamKills(const QJsonValue &team_kills);
    bool is_team_kills_Set() const;
    bool is_team_kills_Valid() const;

    QJsonValue getTowerKills() const;
    void setTowerKills(const QJsonValue &tower_kills);
    bool is_tower_kills_Set() const;
    bool is_tower_kills_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QJsonValue m_baron_kills;
    bool m_baron_kills_isSet;
    bool m_baron_kills_isValid;

    OAILoLTeamColor m_color;
    bool m_color_isSet;
    bool m_color_isValid;

    QJsonValue m_dragon_kills;
    bool m_dragon_kills_isSet;
    bool m_dragon_kills_isValid;

    QJsonValue m_first_baron;
    bool m_first_baron_isSet;
    bool m_first_baron_isValid;

    QJsonValue m_first_blood;
    bool m_first_blood_isSet;
    bool m_first_blood_isValid;

    QJsonValue m_first_dragon;
    bool m_first_dragon_isSet;
    bool m_first_dragon_isValid;

    QJsonValue m_first_herald;
    bool m_first_herald_isSet;
    bool m_first_herald_isValid;

    QJsonValue m_first_inhibitor;
    bool m_first_inhibitor_isSet;
    bool m_first_inhibitor_isValid;

    QJsonValue m_first_tower;
    bool m_first_tower_isSet;
    bool m_first_tower_isValid;

    QJsonValue m_gold_earned;
    bool m_gold_earned_isSet;
    bool m_gold_earned_isValid;

    QJsonValue m_herald_kill;
    bool m_herald_kill_isSet;
    bool m_herald_kill_isValid;

    QJsonValue m_inhibitor_kills;
    bool m_inhibitor_kills_isSet;
    bool m_inhibitor_kills_isValid;

    qint32 m_team_id;
    bool m_team_id_isSet;
    bool m_team_id_isValid;

    QJsonValue m_team_kills;
    bool m_team_kills_isSet;
    bool m_team_kills_isValid;

    QJsonValue m_tower_kills;
    bool m_tower_kills_isSet;
    bool m_tower_kills_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIBettingLoLGameTeam)

#endif // OAIBettingLoLGameTeam_H
