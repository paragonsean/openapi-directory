/**
 * LoL v3 Scores
 * LoL v3 Scores
 *
 * The version of the OpenAPI document: 1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#ifndef OAI_OAIDefaultApi_H
#define OAI_OAIDefaultApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAIArea.h"
#include "OAICompetition.h"
#include "OAICompetitionDetail.h"
#include "OAIGame.h"
#include "OAIMembership.h"
#include "OAIPlayer.h"
#include "OAISeasonTeam.h"
#include "OAIStanding.h"
#include "OAITeam.h"
#include "OAIVenue.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAIDefaultApi : public QObject {
    Q_OBJECT

public:
    OAIDefaultApi(const int timeOut = 0);
    ~OAIDefaultApi();

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
    * @param[in]  format QString [required]
    */
    virtual void areasCountries(const QString &format);

    /**
    * @param[in]  format QString [required]
    * @param[in]  competitionid QString [required]
    */
    virtual void competitionFixturesLeagueDetails(const QString &format, const QString &competitionid);

    /**
    * @param[in]  format QString [required]
    */
    virtual void competitionsLeagues(const QString &format);

    /**
    * @param[in]  format QString [required]
    * @param[in]  date QString [required]
    */
    virtual void gamesByDate(const QString &format, const QString &date);

    /**
    * @param[in]  format QString [required]
    */
    virtual void membershipsActive(const QString &format);

    /**
    * @param[in]  format QString [required]
    * @param[in]  teamid QString [required]
    */
    virtual void membershipsByTeamActive(const QString &format, const QString &teamid);

    /**
    * @param[in]  format QString [required]
    * @param[in]  teamid QString [required]
    */
    virtual void membershipsByTeamHistorical(const QString &format, const QString &teamid);

    /**
    * @param[in]  format QString [required]
    */
    virtual void membershipsHistorical(const QString &format);

    /**
    * @param[in]  format QString [required]
    * @param[in]  playerid QString [required]
    */
    virtual void player(const QString &format, const QString &playerid);

    /**
    * @param[in]  format QString [required]
    */
    virtual void players(const QString &format);

    /**
    * @param[in]  format QString [required]
    * @param[in]  teamid QString [required]
    */
    virtual void playersByTeam(const QString &format, const QString &teamid);

    /**
    * @param[in]  format QString [required]
    * @param[in]  roundid QString [required]
    */
    virtual void schedule(const QString &format, const QString &roundid);

    /**
    * @param[in]  format QString [required]
    * @param[in]  seasonid QString [required]
    */
    virtual void seasonTeams(const QString &format, const QString &seasonid);

    /**
    * @param[in]  format QString [required]
    * @param[in]  roundid QString [required]
    */
    virtual void standings(const QString &format, const QString &roundid);

    /**
    * @param[in]  format QString [required]
    */
    virtual void teams(const QString &format);

    /**
    * @param[in]  format QString [required]
    */
    virtual void venues(const QString &format);


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

    void areasCountriesCallback(OAIHttpRequestWorker *worker);
    void competitionFixturesLeagueDetailsCallback(OAIHttpRequestWorker *worker);
    void competitionsLeaguesCallback(OAIHttpRequestWorker *worker);
    void gamesByDateCallback(OAIHttpRequestWorker *worker);
    void membershipsActiveCallback(OAIHttpRequestWorker *worker);
    void membershipsByTeamActiveCallback(OAIHttpRequestWorker *worker);
    void membershipsByTeamHistoricalCallback(OAIHttpRequestWorker *worker);
    void membershipsHistoricalCallback(OAIHttpRequestWorker *worker);
    void playerCallback(OAIHttpRequestWorker *worker);
    void playersCallback(OAIHttpRequestWorker *worker);
    void playersByTeamCallback(OAIHttpRequestWorker *worker);
    void scheduleCallback(OAIHttpRequestWorker *worker);
    void seasonTeamsCallback(OAIHttpRequestWorker *worker);
    void standingsCallback(OAIHttpRequestWorker *worker);
    void teamsCallback(OAIHttpRequestWorker *worker);
    void venuesCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void areasCountriesSignal(QList<OAIArea> summary);
    void competitionFixturesLeagueDetailsSignal(OAICompetitionDetail summary);
    void competitionsLeaguesSignal(QList<OAICompetition> summary);
    void gamesByDateSignal(QList<OAIGame> summary);
    void membershipsActiveSignal(QList<OAIMembership> summary);
    void membershipsByTeamActiveSignal(QList<OAIMembership> summary);
    void membershipsByTeamHistoricalSignal(QList<OAIMembership> summary);
    void membershipsHistoricalSignal(QList<OAIMembership> summary);
    void playerSignal(OAIPlayer summary);
    void playersSignal(QList<OAIPlayer> summary);
    void playersByTeamSignal(QList<OAIPlayer> summary);
    void scheduleSignal(QList<OAIGame> summary);
    void seasonTeamsSignal(QList<OAISeasonTeam> summary);
    void standingsSignal(QList<OAIStanding> summary);
    void teamsSignal(QList<OAITeam> summary);
    void venuesSignal(QList<OAIVenue> summary);


    void areasCountriesSignalFull(OAIHttpRequestWorker *worker, QList<OAIArea> summary);
    void competitionFixturesLeagueDetailsSignalFull(OAIHttpRequestWorker *worker, OAICompetitionDetail summary);
    void competitionsLeaguesSignalFull(OAIHttpRequestWorker *worker, QList<OAICompetition> summary);
    void gamesByDateSignalFull(OAIHttpRequestWorker *worker, QList<OAIGame> summary);
    void membershipsActiveSignalFull(OAIHttpRequestWorker *worker, QList<OAIMembership> summary);
    void membershipsByTeamActiveSignalFull(OAIHttpRequestWorker *worker, QList<OAIMembership> summary);
    void membershipsByTeamHistoricalSignalFull(OAIHttpRequestWorker *worker, QList<OAIMembership> summary);
    void membershipsHistoricalSignalFull(OAIHttpRequestWorker *worker, QList<OAIMembership> summary);
    void playerSignalFull(OAIHttpRequestWorker *worker, OAIPlayer summary);
    void playersSignalFull(OAIHttpRequestWorker *worker, QList<OAIPlayer> summary);
    void playersByTeamSignalFull(OAIHttpRequestWorker *worker, QList<OAIPlayer> summary);
    void scheduleSignalFull(OAIHttpRequestWorker *worker, QList<OAIGame> summary);
    void seasonTeamsSignalFull(OAIHttpRequestWorker *worker, QList<OAISeasonTeam> summary);
    void standingsSignalFull(OAIHttpRequestWorker *worker, QList<OAIStanding> summary);
    void teamsSignalFull(OAIHttpRequestWorker *worker, QList<OAITeam> summary);
    void venuesSignalFull(OAIHttpRequestWorker *worker, QList<OAIVenue> summary);

    Q_DECL_DEPRECATED_X("Use areasCountriesSignalError() instead")
    void areasCountriesSignalE(QList<OAIArea> summary, QNetworkReply::NetworkError error_type, QString error_str);
    void areasCountriesSignalError(QList<OAIArea> summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use competitionFixturesLeagueDetailsSignalError() instead")
    void competitionFixturesLeagueDetailsSignalE(OAICompetitionDetail summary, QNetworkReply::NetworkError error_type, QString error_str);
    void competitionFixturesLeagueDetailsSignalError(OAICompetitionDetail summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use competitionsLeaguesSignalError() instead")
    void competitionsLeaguesSignalE(QList<OAICompetition> summary, QNetworkReply::NetworkError error_type, QString error_str);
    void competitionsLeaguesSignalError(QList<OAICompetition> summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use gamesByDateSignalError() instead")
    void gamesByDateSignalE(QList<OAIGame> summary, QNetworkReply::NetworkError error_type, QString error_str);
    void gamesByDateSignalError(QList<OAIGame> summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use membershipsActiveSignalError() instead")
    void membershipsActiveSignalE(QList<OAIMembership> summary, QNetworkReply::NetworkError error_type, QString error_str);
    void membershipsActiveSignalError(QList<OAIMembership> summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use membershipsByTeamActiveSignalError() instead")
    void membershipsByTeamActiveSignalE(QList<OAIMembership> summary, QNetworkReply::NetworkError error_type, QString error_str);
    void membershipsByTeamActiveSignalError(QList<OAIMembership> summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use membershipsByTeamHistoricalSignalError() instead")
    void membershipsByTeamHistoricalSignalE(QList<OAIMembership> summary, QNetworkReply::NetworkError error_type, QString error_str);
    void membershipsByTeamHistoricalSignalError(QList<OAIMembership> summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use membershipsHistoricalSignalError() instead")
    void membershipsHistoricalSignalE(QList<OAIMembership> summary, QNetworkReply::NetworkError error_type, QString error_str);
    void membershipsHistoricalSignalError(QList<OAIMembership> summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use playerSignalError() instead")
    void playerSignalE(OAIPlayer summary, QNetworkReply::NetworkError error_type, QString error_str);
    void playerSignalError(OAIPlayer summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use playersSignalError() instead")
    void playersSignalE(QList<OAIPlayer> summary, QNetworkReply::NetworkError error_type, QString error_str);
    void playersSignalError(QList<OAIPlayer> summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use playersByTeamSignalError() instead")
    void playersByTeamSignalE(QList<OAIPlayer> summary, QNetworkReply::NetworkError error_type, QString error_str);
    void playersByTeamSignalError(QList<OAIPlayer> summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use scheduleSignalError() instead")
    void scheduleSignalE(QList<OAIGame> summary, QNetworkReply::NetworkError error_type, QString error_str);
    void scheduleSignalError(QList<OAIGame> summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use seasonTeamsSignalError() instead")
    void seasonTeamsSignalE(QList<OAISeasonTeam> summary, QNetworkReply::NetworkError error_type, QString error_str);
    void seasonTeamsSignalError(QList<OAISeasonTeam> summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use standingsSignalError() instead")
    void standingsSignalE(QList<OAIStanding> summary, QNetworkReply::NetworkError error_type, QString error_str);
    void standingsSignalError(QList<OAIStanding> summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use teamsSignalError() instead")
    void teamsSignalE(QList<OAITeam> summary, QNetworkReply::NetworkError error_type, QString error_str);
    void teamsSignalError(QList<OAITeam> summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use venuesSignalError() instead")
    void venuesSignalE(QList<OAIVenue> summary, QNetworkReply::NetworkError error_type, QString error_str);
    void venuesSignalError(QList<OAIVenue> summary, QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use areasCountriesSignalErrorFull() instead")
    void areasCountriesSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void areasCountriesSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use competitionFixturesLeagueDetailsSignalErrorFull() instead")
    void competitionFixturesLeagueDetailsSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void competitionFixturesLeagueDetailsSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use competitionsLeaguesSignalErrorFull() instead")
    void competitionsLeaguesSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void competitionsLeaguesSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use gamesByDateSignalErrorFull() instead")
    void gamesByDateSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void gamesByDateSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use membershipsActiveSignalErrorFull() instead")
    void membershipsActiveSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void membershipsActiveSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use membershipsByTeamActiveSignalErrorFull() instead")
    void membershipsByTeamActiveSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void membershipsByTeamActiveSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use membershipsByTeamHistoricalSignalErrorFull() instead")
    void membershipsByTeamHistoricalSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void membershipsByTeamHistoricalSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use membershipsHistoricalSignalErrorFull() instead")
    void membershipsHistoricalSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void membershipsHistoricalSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use playerSignalErrorFull() instead")
    void playerSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void playerSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use playersSignalErrorFull() instead")
    void playersSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void playersSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use playersByTeamSignalErrorFull() instead")
    void playersByTeamSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void playersByTeamSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use scheduleSignalErrorFull() instead")
    void scheduleSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void scheduleSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use seasonTeamsSignalErrorFull() instead")
    void seasonTeamsSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void seasonTeamsSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use standingsSignalErrorFull() instead")
    void standingsSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void standingsSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use teamsSignalErrorFull() instead")
    void teamsSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void teamsSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use venuesSignalErrorFull() instead")
    void venuesSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void venuesSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
