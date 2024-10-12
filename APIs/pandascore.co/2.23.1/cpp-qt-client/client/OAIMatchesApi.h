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

#ifndef OAI_OAIMatchesApi_H
#define OAI_OAIMatchesApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAIFilter_over_Matches.h"
#include "OAIGet_additions_400_response.h"
#include "OAIGet_additions_page_parameter.h"
#include "OAILive.h"
#include "OAIMatch.h"
#include "OAIMatchIDOrSlug.h"
#include "OAIMatchOpponentsObject.h"
#include "OAIRange_over_Matches.h"
#include "OAISearch_over_Matches.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAIMatchesApi : public QObject {
    Q_OBJECT

public:
    OAIMatchesApi(const int timeOut = 0);
    ~OAIMatchesApi();

    void initializeServerConfigs();
    int setDefaultServerValue(int serverIndex,const QString &operation, const QString &variable,const QString &val);
    void setServerIndex(const QString &operation, int serverIndex);
    void setApiKey(const QString &apiKeyName, const QString &apiKey);
    void setBearerToken(const QString &token);
    void setUsername(const QString &username);
    void setPassword(const QString &password);
    void setTimeOut(const int timeOut);
    void setWorkingDirectory(const QString &path);
    void setNetworkAccessManager(QNetworkAccessManager* manager);
    int addServerConfiguration(const QString &operation, const QUrl &url, const QString &description = "", const QMap<QString, OAIServerVariable> &variables = QMap<QString, OAIServerVariable>());
    void setNewServerForAllOperations(const QUrl &url, const QString &description = "", const QMap<QString, OAIServerVariable> &variables =  QMap<QString, OAIServerVariable>());
    void setNewServer(const QString &operation, const QUrl &url, const QString &description = "", const QMap<QString, OAIServerVariable> &variables =  QMap<QString, OAIServerVariable>());
    void addHeaders(const QString &key, const QString &value);
    void enableRequestCompression();
    void enableResponseCompression();
    void abortRequests();
    QString getParamStylePrefix(const QString &style);
    QString getParamStyleSuffix(const QString &style);
    QString getParamStyleDelimiter(const QString &style, const QString &name, bool isExplode);

    /**
    * @param[in]  page OAIGet_additions_page_parameter [optional]
    * @param[in]  per_page qint32 [optional]
    */
    virtual void getLives(const ::OpenAPI::OptionalParam<OAIGet_additions_page_parameter> &page = ::OpenAPI::OptionalParam<OAIGet_additions_page_parameter>(), const ::OpenAPI::OptionalParam<qint32> &per_page = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  filter OAIFilter_over_Matches [optional]
    * @param[in]  search OAISearch_over_Matches [optional]
    * @param[in]  sort QList<QString> [optional]
    * @param[in]  range OAIRange_over_Matches [optional]
    * @param[in]  page OAIGet_additions_page_parameter [optional]
    * @param[in]  per_page qint32 [optional]
    */
    virtual void getMatches(const ::OpenAPI::OptionalParam<OAIFilter_over_Matches> &filter = ::OpenAPI::OptionalParam<OAIFilter_over_Matches>(), const ::OpenAPI::OptionalParam<OAISearch_over_Matches> &search = ::OpenAPI::OptionalParam<OAISearch_over_Matches>(), const ::OpenAPI::OptionalParam<QList<QString>> &sort = ::OpenAPI::OptionalParam<QList<QString>>(), const ::OpenAPI::OptionalParam<OAIRange_over_Matches> &range = ::OpenAPI::OptionalParam<OAIRange_over_Matches>(), const ::OpenAPI::OptionalParam<OAIGet_additions_page_parameter> &page = ::OpenAPI::OptionalParam<OAIGet_additions_page_parameter>(), const ::OpenAPI::OptionalParam<qint32> &per_page = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  match_id_or_slug OAIMatchIDOrSlug [required]
    */
    virtual void getMatchesMatchIdOrSlug(const OAIMatchIDOrSlug &match_id_or_slug);

    /**
    * @param[in]  match_id_or_slug OAIMatchIDOrSlug [required]
    */
    virtual void getMatchesMatchIdOrSlugOpponents(const OAIMatchIDOrSlug &match_id_or_slug);

    /**
    * @param[in]  filter OAIFilter_over_Matches [optional]
    * @param[in]  search OAISearch_over_Matches [optional]
    * @param[in]  sort QList<QString> [optional]
    * @param[in]  range OAIRange_over_Matches [optional]
    * @param[in]  page OAIGet_additions_page_parameter [optional]
    * @param[in]  per_page qint32 [optional]
    */
    virtual void getMatchesPast(const ::OpenAPI::OptionalParam<OAIFilter_over_Matches> &filter = ::OpenAPI::OptionalParam<OAIFilter_over_Matches>(), const ::OpenAPI::OptionalParam<OAISearch_over_Matches> &search = ::OpenAPI::OptionalParam<OAISearch_over_Matches>(), const ::OpenAPI::OptionalParam<QList<QString>> &sort = ::OpenAPI::OptionalParam<QList<QString>>(), const ::OpenAPI::OptionalParam<OAIRange_over_Matches> &range = ::OpenAPI::OptionalParam<OAIRange_over_Matches>(), const ::OpenAPI::OptionalParam<OAIGet_additions_page_parameter> &page = ::OpenAPI::OptionalParam<OAIGet_additions_page_parameter>(), const ::OpenAPI::OptionalParam<qint32> &per_page = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  filter OAIFilter_over_Matches [optional]
    * @param[in]  search OAISearch_over_Matches [optional]
    * @param[in]  sort QList<QString> [optional]
    * @param[in]  range OAIRange_over_Matches [optional]
    * @param[in]  page OAIGet_additions_page_parameter [optional]
    * @param[in]  per_page qint32 [optional]
    */
    virtual void getMatchesRunning(const ::OpenAPI::OptionalParam<OAIFilter_over_Matches> &filter = ::OpenAPI::OptionalParam<OAIFilter_over_Matches>(), const ::OpenAPI::OptionalParam<OAISearch_over_Matches> &search = ::OpenAPI::OptionalParam<OAISearch_over_Matches>(), const ::OpenAPI::OptionalParam<QList<QString>> &sort = ::OpenAPI::OptionalParam<QList<QString>>(), const ::OpenAPI::OptionalParam<OAIRange_over_Matches> &range = ::OpenAPI::OptionalParam<OAIRange_over_Matches>(), const ::OpenAPI::OptionalParam<OAIGet_additions_page_parameter> &page = ::OpenAPI::OptionalParam<OAIGet_additions_page_parameter>(), const ::OpenAPI::OptionalParam<qint32> &per_page = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  filter OAIFilter_over_Matches [optional]
    * @param[in]  search OAISearch_over_Matches [optional]
    * @param[in]  sort QList<QString> [optional]
    * @param[in]  range OAIRange_over_Matches [optional]
    * @param[in]  page OAIGet_additions_page_parameter [optional]
    * @param[in]  per_page qint32 [optional]
    */
    virtual void getMatchesUpcoming(const ::OpenAPI::OptionalParam<OAIFilter_over_Matches> &filter = ::OpenAPI::OptionalParam<OAIFilter_over_Matches>(), const ::OpenAPI::OptionalParam<OAISearch_over_Matches> &search = ::OpenAPI::OptionalParam<OAISearch_over_Matches>(), const ::OpenAPI::OptionalParam<QList<QString>> &sort = ::OpenAPI::OptionalParam<QList<QString>>(), const ::OpenAPI::OptionalParam<OAIRange_over_Matches> &range = ::OpenAPI::OptionalParam<OAIRange_over_Matches>(), const ::OpenAPI::OptionalParam<OAIGet_additions_page_parameter> &page = ::OpenAPI::OptionalParam<OAIGet_additions_page_parameter>(), const ::OpenAPI::OptionalParam<qint32> &per_page = ::OpenAPI::OptionalParam<qint32>());


private:
    QMap<QString,int> _serverIndices;
    QMap<QString,QList<OAIServerConfiguration>> _serverConfigs;
    QMap<QString, QString> _apiKeys;
    QString _bearerToken;
    QString _username;
    QString _password;
    int _timeOut;
    QString _workingDirectory;
    QNetworkAccessManager* _manager;
    QMap<QString, QString> _defaultHeaders;
    bool _isResponseCompressionEnabled;
    bool _isRequestCompressionEnabled;
    OAIHttpRequestInput _latestInput;
    OAIHttpRequestWorker *_latestWorker;
    QStringList _latestScope;
    OauthCode _authFlow;
    OauthImplicit _implicitFlow;
    OauthCredentials _credentialFlow;
    OauthPassword _passwordFlow;
    int _OauthMethod = 0;

    void getLivesCallback(OAIHttpRequestWorker *worker);
    void getMatchesCallback(OAIHttpRequestWorker *worker);
    void getMatchesMatchIdOrSlugCallback(OAIHttpRequestWorker *worker);
    void getMatchesMatchIdOrSlugOpponentsCallback(OAIHttpRequestWorker *worker);
    void getMatchesPastCallback(OAIHttpRequestWorker *worker);
    void getMatchesRunningCallback(OAIHttpRequestWorker *worker);
    void getMatchesUpcomingCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void getLivesSignal(QList<OAILive> summary);
    void getMatchesSignal(QList<OAIMatch> summary);
    void getMatchesMatchIdOrSlugSignal(OAIMatch summary);
    void getMatchesMatchIdOrSlugOpponentsSignal(OAIMatchOpponentsObject summary);
    void getMatchesPastSignal(QList<OAIMatch> summary);
    void getMatchesRunningSignal(QList<OAIMatch> summary);
    void getMatchesUpcomingSignal(QList<OAIMatch> summary);


    void getLivesSignalFull(OAIHttpRequestWorker *worker, QList<OAILive> summary);
    void getMatchesSignalFull(OAIHttpRequestWorker *worker, QList<OAIMatch> summary);
    void getMatchesMatchIdOrSlugSignalFull(OAIHttpRequestWorker *worker, OAIMatch summary);
    void getMatchesMatchIdOrSlugOpponentsSignalFull(OAIHttpRequestWorker *worker, OAIMatchOpponentsObject summary);
    void getMatchesPastSignalFull(OAIHttpRequestWorker *worker, QList<OAIMatch> summary);
    void getMatchesRunningSignalFull(OAIHttpRequestWorker *worker, QList<OAIMatch> summary);
    void getMatchesUpcomingSignalFull(OAIHttpRequestWorker *worker, QList<OAIMatch> summary);

    Q_DECL_DEPRECATED_X("Use getLivesSignalError() instead")
    void getLivesSignalE(QList<OAILive> summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getLivesSignalError(QList<OAILive> summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getMatchesSignalError() instead")
    void getMatchesSignalE(QList<OAIMatch> summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getMatchesSignalError(QList<OAIMatch> summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getMatchesMatchIdOrSlugSignalError() instead")
    void getMatchesMatchIdOrSlugSignalE(OAIMatch summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getMatchesMatchIdOrSlugSignalError(OAIMatch summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getMatchesMatchIdOrSlugOpponentsSignalError() instead")
    void getMatchesMatchIdOrSlugOpponentsSignalE(OAIMatchOpponentsObject summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getMatchesMatchIdOrSlugOpponentsSignalError(OAIMatchOpponentsObject summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getMatchesPastSignalError() instead")
    void getMatchesPastSignalE(QList<OAIMatch> summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getMatchesPastSignalError(QList<OAIMatch> summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getMatchesRunningSignalError() instead")
    void getMatchesRunningSignalE(QList<OAIMatch> summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getMatchesRunningSignalError(QList<OAIMatch> summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getMatchesUpcomingSignalError() instead")
    void getMatchesUpcomingSignalE(QList<OAIMatch> summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getMatchesUpcomingSignalError(QList<OAIMatch> summary, QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use getLivesSignalErrorFull() instead")
    void getLivesSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getLivesSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getMatchesSignalErrorFull() instead")
    void getMatchesSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getMatchesSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getMatchesMatchIdOrSlugSignalErrorFull() instead")
    void getMatchesMatchIdOrSlugSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getMatchesMatchIdOrSlugSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getMatchesMatchIdOrSlugOpponentsSignalErrorFull() instead")
    void getMatchesMatchIdOrSlugOpponentsSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getMatchesMatchIdOrSlugOpponentsSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getMatchesPastSignalErrorFull() instead")
    void getMatchesPastSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getMatchesPastSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getMatchesRunningSignalErrorFull() instead")
    void getMatchesRunningSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getMatchesRunningSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getMatchesUpcomingSignalErrorFull() instead")
    void getMatchesUpcomingSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getMatchesUpcomingSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
