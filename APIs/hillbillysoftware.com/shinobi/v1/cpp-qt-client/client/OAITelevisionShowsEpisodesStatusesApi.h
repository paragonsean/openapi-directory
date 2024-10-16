/**
 * shinobiapi
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: v1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#ifndef OAI_OAITelevisionShowsEpisodesStatusesApi_H
#define OAI_OAITelevisionShowsEpisodesStatusesApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAIEpisode.h"
#include "OAILastAvailableSeason.h"
#include "OAIPostResult.h"
#include "OAITVInformation.h"
#include "OAITVInformationPost.h"
#include "OAITVShowSeasons.h"
#include "OAI_ShowStatus.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAITelevisionShowsEpisodesStatusesApi : public QObject {
    Q_OBJECT

public:
    OAITelevisionShowsEpisodesStatusesApi(const int timeOut = 0);
    ~OAITelevisionShowsEpisodesStatusesApi();

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
    * @param[in]  value OAITVInformationPost [required]
    */
    virtual void addTVShowPost(const OAITVInformationPost &value);

    /**
    * @param[in]  access_token QString [required]
    * @param[in]  id QString [required]
    */
    virtual void episodesByIDGet(const QString &access_token, const QString &id);

    /**
    * @param[in]  access_token QString [required]
    * @param[in]  id QString [required]
    * @param[in]  season QString [required]
    */
    virtual void episodesBySeasonGet(const QString &access_token, const QString &id, const QString &season);

    /**
    * @param[in]  access_token QString [required]
    * @param[in]  showname QString [required]
    */
    virtual void episodesGet(const QString &access_token, const QString &showname);

    /**
    * @param[in]  access_token QString [required]
    * @param[in]  id QString [required]
    */
    virtual void episodesLastAvailableSeasonGet(const QString &access_token, const QString &id);

    /**
    * @param[in]  access_token QString [required]
    * @param[in]  name QString [required]
    */
    virtual void episodesLastAvailableSeasonbyNameGet(const QString &access_token, const QString &name);

    /**
    * @param[in]  access_token QString [required]
    * @param[in]  id QString [required]
    */
    virtual void episodesSeasonCountGet(const QString &access_token, const QString &id);

    /**
    * @param[in]  access_token QString [required]
    * @param[in]  query QString [required]
    */
    virtual void showStatusGet(const QString &access_token, const QString &query);

    /**
    * @param[in]  access_token QString [required]
    * @param[in]  query QString [required]
    */
    virtual void tVShowByNameGet(const QString &access_token, const QString &query);

    /**
    * @param[in]  accesstoken QString [required]
    * @param[in]  id QString [required]
    * @param[in]  imdb_id QString [required]
    */
    virtual void tVShowIDGet(const QString &accesstoken, const QString &id, const QString &imdb_id);


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

    void addTVShowPostCallback(OAIHttpRequestWorker *worker);
    void episodesByIDGetCallback(OAIHttpRequestWorker *worker);
    void episodesBySeasonGetCallback(OAIHttpRequestWorker *worker);
    void episodesGetCallback(OAIHttpRequestWorker *worker);
    void episodesLastAvailableSeasonGetCallback(OAIHttpRequestWorker *worker);
    void episodesLastAvailableSeasonbyNameGetCallback(OAIHttpRequestWorker *worker);
    void episodesSeasonCountGetCallback(OAIHttpRequestWorker *worker);
    void showStatusGetCallback(OAIHttpRequestWorker *worker);
    void tVShowByNameGetCallback(OAIHttpRequestWorker *worker);
    void tVShowIDGetCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void addTVShowPostSignal(OAIPostResult summary);
    void episodesByIDGetSignal(QList<OAIEpisode> summary);
    void episodesBySeasonGetSignal(QList<OAIEpisode> summary);
    void episodesGetSignal(QList<OAIEpisode> summary);
    void episodesLastAvailableSeasonGetSignal(OAILastAvailableSeason summary);
    void episodesLastAvailableSeasonbyNameGetSignal(OAILastAvailableSeason summary);
    void episodesSeasonCountGetSignal(OAITVShowSeasons summary);
    void showStatusGetSignal(QList<OAI_ShowStatus> summary);
    void tVShowByNameGetSignal(QList<OAITVInformation> summary);
    void tVShowIDGetSignal(OAITVInformation summary);


    void addTVShowPostSignalFull(OAIHttpRequestWorker *worker, OAIPostResult summary);
    void episodesByIDGetSignalFull(OAIHttpRequestWorker *worker, QList<OAIEpisode> summary);
    void episodesBySeasonGetSignalFull(OAIHttpRequestWorker *worker, QList<OAIEpisode> summary);
    void episodesGetSignalFull(OAIHttpRequestWorker *worker, QList<OAIEpisode> summary);
    void episodesLastAvailableSeasonGetSignalFull(OAIHttpRequestWorker *worker, OAILastAvailableSeason summary);
    void episodesLastAvailableSeasonbyNameGetSignalFull(OAIHttpRequestWorker *worker, OAILastAvailableSeason summary);
    void episodesSeasonCountGetSignalFull(OAIHttpRequestWorker *worker, OAITVShowSeasons summary);
    void showStatusGetSignalFull(OAIHttpRequestWorker *worker, QList<OAI_ShowStatus> summary);
    void tVShowByNameGetSignalFull(OAIHttpRequestWorker *worker, QList<OAITVInformation> summary);
    void tVShowIDGetSignalFull(OAIHttpRequestWorker *worker, OAITVInformation summary);

    Q_DECL_DEPRECATED_X("Use addTVShowPostSignalError() instead")
    void addTVShowPostSignalE(OAIPostResult summary, QNetworkReply::NetworkError error_type, QString error_str);
    void addTVShowPostSignalError(OAIPostResult summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use episodesByIDGetSignalError() instead")
    void episodesByIDGetSignalE(QList<OAIEpisode> summary, QNetworkReply::NetworkError error_type, QString error_str);
    void episodesByIDGetSignalError(QList<OAIEpisode> summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use episodesBySeasonGetSignalError() instead")
    void episodesBySeasonGetSignalE(QList<OAIEpisode> summary, QNetworkReply::NetworkError error_type, QString error_str);
    void episodesBySeasonGetSignalError(QList<OAIEpisode> summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use episodesGetSignalError() instead")
    void episodesGetSignalE(QList<OAIEpisode> summary, QNetworkReply::NetworkError error_type, QString error_str);
    void episodesGetSignalError(QList<OAIEpisode> summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use episodesLastAvailableSeasonGetSignalError() instead")
    void episodesLastAvailableSeasonGetSignalE(OAILastAvailableSeason summary, QNetworkReply::NetworkError error_type, QString error_str);
    void episodesLastAvailableSeasonGetSignalError(OAILastAvailableSeason summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use episodesLastAvailableSeasonbyNameGetSignalError() instead")
    void episodesLastAvailableSeasonbyNameGetSignalE(OAILastAvailableSeason summary, QNetworkReply::NetworkError error_type, QString error_str);
    void episodesLastAvailableSeasonbyNameGetSignalError(OAILastAvailableSeason summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use episodesSeasonCountGetSignalError() instead")
    void episodesSeasonCountGetSignalE(OAITVShowSeasons summary, QNetworkReply::NetworkError error_type, QString error_str);
    void episodesSeasonCountGetSignalError(OAITVShowSeasons summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use showStatusGetSignalError() instead")
    void showStatusGetSignalE(QList<OAI_ShowStatus> summary, QNetworkReply::NetworkError error_type, QString error_str);
    void showStatusGetSignalError(QList<OAI_ShowStatus> summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use tVShowByNameGetSignalError() instead")
    void tVShowByNameGetSignalE(QList<OAITVInformation> summary, QNetworkReply::NetworkError error_type, QString error_str);
    void tVShowByNameGetSignalError(QList<OAITVInformation> summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use tVShowIDGetSignalError() instead")
    void tVShowIDGetSignalE(OAITVInformation summary, QNetworkReply::NetworkError error_type, QString error_str);
    void tVShowIDGetSignalError(OAITVInformation summary, QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use addTVShowPostSignalErrorFull() instead")
    void addTVShowPostSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void addTVShowPostSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use episodesByIDGetSignalErrorFull() instead")
    void episodesByIDGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void episodesByIDGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use episodesBySeasonGetSignalErrorFull() instead")
    void episodesBySeasonGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void episodesBySeasonGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use episodesGetSignalErrorFull() instead")
    void episodesGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void episodesGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use episodesLastAvailableSeasonGetSignalErrorFull() instead")
    void episodesLastAvailableSeasonGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void episodesLastAvailableSeasonGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use episodesLastAvailableSeasonbyNameGetSignalErrorFull() instead")
    void episodesLastAvailableSeasonbyNameGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void episodesLastAvailableSeasonbyNameGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use episodesSeasonCountGetSignalErrorFull() instead")
    void episodesSeasonCountGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void episodesSeasonCountGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use showStatusGetSignalErrorFull() instead")
    void showStatusGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void showStatusGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use tVShowByNameGetSignalErrorFull() instead")
    void tVShowByNameGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void tVShowByNameGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use tVShowIDGetSignalErrorFull() instead")
    void tVShowIDGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void tVShowIDGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
