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
 * OAIBracket.h
 *
 * 
 */

#ifndef OAIBracket_H
#define OAIBracket_H

#include <QJsonObject>

#include "OAIGame.h"
#include "OAIMatchLive.h"
#include "OAIMatchLocalizedStreams.h"
#include "OAIMatchStatus.h"
#include "OAIMatchType.h"
#include "OAIOpponent.h"
#include "OAIOpponentID_1.h"
#include "OAIPreviousMatch.h"
#include "OAIStream.h"
#include <QDateTime>
#include <QJsonValue>
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIGame;
class OAIMatchLive;
class OAIOpponent;
class OAIPreviousMatch;
class OAIMatchLocalizedStreams;
class OAIStream;

class OAIBracket : public OAIObject {
public:
    OAIBracket();
    OAIBracket(QString json);
    ~OAIBracket() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QJsonValue getBeginAt() const;
    void setBeginAt(const QJsonValue &begin_at);
    bool is_begin_at_Set() const;
    bool is_begin_at_Valid() const;

    bool isDetailedStats() const;
    void setDetailedStats(const bool &detailed_stats);
    bool is_detailed_stats_Set() const;
    bool is_detailed_stats_Valid() const;

    bool isDraw() const;
    void setDraw(const bool &draw);
    bool is_draw_Set() const;
    bool is_draw_Valid() const;

    QJsonValue getEndAt() const;
    void setEndAt(const QJsonValue &end_at);
    bool is_end_at_Set() const;
    bool is_end_at_Valid() const;

    bool isForfeit() const;
    void setForfeit(const bool &forfeit);
    bool is_forfeit_Set() const;
    bool is_forfeit_Valid() const;

    OAIOpponentID_1 getGameAdvantage() const;
    void setGameAdvantage(const OAIOpponentID_1 &game_advantage);
    bool is_game_advantage_Set() const;
    bool is_game_advantage_Valid() const;

    QList<OAIGame> getGames() const;
    void setGames(const QList<OAIGame> &games);
    bool is_games_Set() const;
    bool is_games_Valid() const;

    qint32 getId() const;
    void setId(const qint32 &id);
    bool is_id_Set() const;
    bool is_id_Valid() const;

    OAIMatchLive getLive() const;
    void setLive(const OAIMatchLive &live);
    bool is_live_Set() const;
    bool is_live_Valid() const;

    Q_DECL_DEPRECATED QJsonValue getLiveEmbedUrl() const;
    Q_DECL_DEPRECATED void setLiveEmbedUrl(const QJsonValue &live_embed_url);
    Q_DECL_DEPRECATED bool is_live_embed_url_Set() const;
    Q_DECL_DEPRECATED bool is_live_embed_url_Valid() const;

    OAIMatchType getMatchType() const;
    void setMatchType(const OAIMatchType &match_type);
    bool is_match_type_Set() const;
    bool is_match_type_Valid() const;

    QDateTime getModifiedAt() const;
    void setModifiedAt(const QDateTime &modified_at);
    bool is_modified_at_Set() const;
    bool is_modified_at_Valid() const;

    QString getName() const;
    void setName(const QString &name);
    bool is_name_Set() const;
    bool is_name_Valid() const;

    qint32 getNumberOfGames() const;
    void setNumberOfGames(const qint32 &number_of_games);
    bool is_number_of_games_Set() const;
    bool is_number_of_games_Valid() const;

    Q_DECL_DEPRECATED QJsonValue getOfficialStreamUrl() const;
    Q_DECL_DEPRECATED void setOfficialStreamUrl(const QJsonValue &official_stream_url);
    Q_DECL_DEPRECATED bool is_official_stream_url_Set() const;
    Q_DECL_DEPRECATED bool is_official_stream_url_Valid() const;

    QList<OAIOpponent> getOpponents() const;
    void setOpponents(const QList<OAIOpponent> &opponents);
    bool is_opponents_Set() const;
    bool is_opponents_Valid() const;

    QJsonValue getOriginalScheduledAt() const;
    void setOriginalScheduledAt(const QJsonValue &original_scheduled_at);
    bool is_original_scheduled_at_Set() const;
    bool is_original_scheduled_at_Valid() const;

    QList<OAIPreviousMatch> getPreviousMatches() const;
    void setPreviousMatches(const QList<OAIPreviousMatch> &previous_matches);
    bool is_previous_matches_Set() const;
    bool is_previous_matches_Valid() const;

    QJsonValue getScheduledAt() const;
    void setScheduledAt(const QJsonValue &scheduled_at);
    bool is_scheduled_at_Set() const;
    bool is_scheduled_at_Valid() const;

    QJsonValue getSlug() const;
    void setSlug(const QJsonValue &slug);
    bool is_slug_Set() const;
    bool is_slug_Valid() const;

    OAIMatchStatus getStatus() const;
    void setStatus(const OAIMatchStatus &status);
    bool is_status_Set() const;
    bool is_status_Valid() const;

    Q_DECL_DEPRECATED OAIMatchLocalizedStreams getStreams() const;
    Q_DECL_DEPRECATED void setStreams(const OAIMatchLocalizedStreams &streams);
    Q_DECL_DEPRECATED bool is_streams_Set() const;
    Q_DECL_DEPRECATED bool is_streams_Valid() const;

    QList<OAIStream> getStreamsList() const;
    void setStreamsList(const QList<OAIStream> &streams_list);
    bool is_streams_list_Set() const;
    bool is_streams_list_Valid() const;

    qint32 getTournamentId() const;
    void setTournamentId(const qint32 &tournament_id);
    bool is_tournament_id_Set() const;
    bool is_tournament_id_Valid() const;

    OAIOpponentID_1 getWinnerId() const;
    void setWinnerId(const OAIOpponentID_1 &winner_id);
    bool is_winner_id_Set() const;
    bool is_winner_id_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QJsonValue m_begin_at;
    bool m_begin_at_isSet;
    bool m_begin_at_isValid;

    bool m_detailed_stats;
    bool m_detailed_stats_isSet;
    bool m_detailed_stats_isValid;

    bool m_draw;
    bool m_draw_isSet;
    bool m_draw_isValid;

    QJsonValue m_end_at;
    bool m_end_at_isSet;
    bool m_end_at_isValid;

    bool m_forfeit;
    bool m_forfeit_isSet;
    bool m_forfeit_isValid;

    OAIOpponentID_1 m_game_advantage;
    bool m_game_advantage_isSet;
    bool m_game_advantage_isValid;

    QList<OAIGame> m_games;
    bool m_games_isSet;
    bool m_games_isValid;

    qint32 m_id;
    bool m_id_isSet;
    bool m_id_isValid;

    OAIMatchLive m_live;
    bool m_live_isSet;
    bool m_live_isValid;

    QJsonValue m_live_embed_url;
    bool m_live_embed_url_isSet;
    bool m_live_embed_url_isValid;

    OAIMatchType m_match_type;
    bool m_match_type_isSet;
    bool m_match_type_isValid;

    QDateTime m_modified_at;
    bool m_modified_at_isSet;
    bool m_modified_at_isValid;

    QString m_name;
    bool m_name_isSet;
    bool m_name_isValid;

    qint32 m_number_of_games;
    bool m_number_of_games_isSet;
    bool m_number_of_games_isValid;

    QJsonValue m_official_stream_url;
    bool m_official_stream_url_isSet;
    bool m_official_stream_url_isValid;

    QList<OAIOpponent> m_opponents;
    bool m_opponents_isSet;
    bool m_opponents_isValid;

    QJsonValue m_original_scheduled_at;
    bool m_original_scheduled_at_isSet;
    bool m_original_scheduled_at_isValid;

    QList<OAIPreviousMatch> m_previous_matches;
    bool m_previous_matches_isSet;
    bool m_previous_matches_isValid;

    QJsonValue m_scheduled_at;
    bool m_scheduled_at_isSet;
    bool m_scheduled_at_isValid;

    QJsonValue m_slug;
    bool m_slug_isSet;
    bool m_slug_isValid;

    OAIMatchStatus m_status;
    bool m_status_isSet;
    bool m_status_isValid;

    OAIMatchLocalizedStreams m_streams;
    bool m_streams_isSet;
    bool m_streams_isValid;

    QList<OAIStream> m_streams_list;
    bool m_streams_list_isSet;
    bool m_streams_list_isValid;

    qint32 m_tournament_id;
    bool m_tournament_id_isSet;
    bool m_tournament_id_isValid;

    OAIOpponentID_1 m_winner_id;
    bool m_winner_id_isSet;
    bool m_winner_id_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIBracket)

#endif // OAIBracket_H
