/**
 * MLB v3 Projections
 * MLB projections API.
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

#include "OAIDfsSlate.h"
#include "OAIPlayer.h"
#include "OAIPlayerGameProjection.h"
#include "OAIPlayerSeasonProjection.h"
#include "OAIStartingLineups.h"
#include "OAITeamDepthChart.h"
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
    virtual void depthCharts(const QString &format);

    /**
    * @param[in]  format QString [required]
    * @param[in]  date QString [required]
    */
    virtual void dfsSlatesByDate(const QString &format, const QString &date);

    /**
    * @param[in]  format QString [required]
    */
    virtual void injuredPlayers(const QString &format);

    /**
    * @param[in]  format QString [required]
    * @param[in]  date QString [required]
    */
    virtual void projectedPlayerGameStatsByDateWInjuriesDfsSalaries(const QString &format, const QString &date);

    /**
    * @param[in]  format QString [required]
    * @param[in]  date QString [required]
    * @param[in]  playerid QString [required]
    */
    virtual void projectedPlayerGameStatsByPlayerWInjuriesDfsSalaries(const QString &format, const QString &date, const QString &playerid);

    /**
    * @param[in]  format QString [required]
    * @param[in]  season QString [required]
    */
    virtual void projectedPlayerSeasonStatsWithAdp(const QString &format, const QString &season);

    /**
    * @param[in]  format QString [required]
    * @param[in]  date QString [required]
    */
    virtual void startingLineupsByDate(const QString &format, const QString &date);


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

    void depthChartsCallback(OAIHttpRequestWorker *worker);
    void dfsSlatesByDateCallback(OAIHttpRequestWorker *worker);
    void injuredPlayersCallback(OAIHttpRequestWorker *worker);
    void projectedPlayerGameStatsByDateWInjuriesDfsSalariesCallback(OAIHttpRequestWorker *worker);
    void projectedPlayerGameStatsByPlayerWInjuriesDfsSalariesCallback(OAIHttpRequestWorker *worker);
    void projectedPlayerSeasonStatsWithAdpCallback(OAIHttpRequestWorker *worker);
    void startingLineupsByDateCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void depthChartsSignal(QList<OAITeamDepthChart> summary);
    void dfsSlatesByDateSignal(QList<OAIDfsSlate> summary);
    void injuredPlayersSignal(QList<OAIPlayer> summary);
    void projectedPlayerGameStatsByDateWInjuriesDfsSalariesSignal(QList<OAIPlayerGameProjection> summary);
    void projectedPlayerGameStatsByPlayerWInjuriesDfsSalariesSignal(QList<OAIPlayerGameProjection> summary);
    void projectedPlayerSeasonStatsWithAdpSignal(QList<OAIPlayerSeasonProjection> summary);
    void startingLineupsByDateSignal(QList<OAIStartingLineups> summary);


    void depthChartsSignalFull(OAIHttpRequestWorker *worker, QList<OAITeamDepthChart> summary);
    void dfsSlatesByDateSignalFull(OAIHttpRequestWorker *worker, QList<OAIDfsSlate> summary);
    void injuredPlayersSignalFull(OAIHttpRequestWorker *worker, QList<OAIPlayer> summary);
    void projectedPlayerGameStatsByDateWInjuriesDfsSalariesSignalFull(OAIHttpRequestWorker *worker, QList<OAIPlayerGameProjection> summary);
    void projectedPlayerGameStatsByPlayerWInjuriesDfsSalariesSignalFull(OAIHttpRequestWorker *worker, QList<OAIPlayerGameProjection> summary);
    void projectedPlayerSeasonStatsWithAdpSignalFull(OAIHttpRequestWorker *worker, QList<OAIPlayerSeasonProjection> summary);
    void startingLineupsByDateSignalFull(OAIHttpRequestWorker *worker, QList<OAIStartingLineups> summary);

    Q_DECL_DEPRECATED_X("Use depthChartsSignalError() instead")
    void depthChartsSignalE(QList<OAITeamDepthChart> summary, QNetworkReply::NetworkError error_type, QString error_str);
    void depthChartsSignalError(QList<OAITeamDepthChart> summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use dfsSlatesByDateSignalError() instead")
    void dfsSlatesByDateSignalE(QList<OAIDfsSlate> summary, QNetworkReply::NetworkError error_type, QString error_str);
    void dfsSlatesByDateSignalError(QList<OAIDfsSlate> summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use injuredPlayersSignalError() instead")
    void injuredPlayersSignalE(QList<OAIPlayer> summary, QNetworkReply::NetworkError error_type, QString error_str);
    void injuredPlayersSignalError(QList<OAIPlayer> summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use projectedPlayerGameStatsByDateWInjuriesDfsSalariesSignalError() instead")
    void projectedPlayerGameStatsByDateWInjuriesDfsSalariesSignalE(QList<OAIPlayerGameProjection> summary, QNetworkReply::NetworkError error_type, QString error_str);
    void projectedPlayerGameStatsByDateWInjuriesDfsSalariesSignalError(QList<OAIPlayerGameProjection> summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use projectedPlayerGameStatsByPlayerWInjuriesDfsSalariesSignalError() instead")
    void projectedPlayerGameStatsByPlayerWInjuriesDfsSalariesSignalE(QList<OAIPlayerGameProjection> summary, QNetworkReply::NetworkError error_type, QString error_str);
    void projectedPlayerGameStatsByPlayerWInjuriesDfsSalariesSignalError(QList<OAIPlayerGameProjection> summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use projectedPlayerSeasonStatsWithAdpSignalError() instead")
    void projectedPlayerSeasonStatsWithAdpSignalE(QList<OAIPlayerSeasonProjection> summary, QNetworkReply::NetworkError error_type, QString error_str);
    void projectedPlayerSeasonStatsWithAdpSignalError(QList<OAIPlayerSeasonProjection> summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use startingLineupsByDateSignalError() instead")
    void startingLineupsByDateSignalE(QList<OAIStartingLineups> summary, QNetworkReply::NetworkError error_type, QString error_str);
    void startingLineupsByDateSignalError(QList<OAIStartingLineups> summary, QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use depthChartsSignalErrorFull() instead")
    void depthChartsSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void depthChartsSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use dfsSlatesByDateSignalErrorFull() instead")
    void dfsSlatesByDateSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void dfsSlatesByDateSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use injuredPlayersSignalErrorFull() instead")
    void injuredPlayersSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void injuredPlayersSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use projectedPlayerGameStatsByDateWInjuriesDfsSalariesSignalErrorFull() instead")
    void projectedPlayerGameStatsByDateWInjuriesDfsSalariesSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void projectedPlayerGameStatsByDateWInjuriesDfsSalariesSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use projectedPlayerGameStatsByPlayerWInjuriesDfsSalariesSignalErrorFull() instead")
    void projectedPlayerGameStatsByPlayerWInjuriesDfsSalariesSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void projectedPlayerGameStatsByPlayerWInjuriesDfsSalariesSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use projectedPlayerSeasonStatsWithAdpSignalErrorFull() instead")
    void projectedPlayerSeasonStatsWithAdpSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void projectedPlayerSeasonStatsWithAdpSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use startingLineupsByDateSignalErrorFull() instead")
    void startingLineupsByDateSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void startingLineupsByDateSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
