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

#ifndef OAI_OAICastCrewCastCrewInMoviesTelevisionShowsApi_H
#define OAI_OAICastCrewCastCrewInMoviesTelevisionShowsApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAIActor.h"
#include "OAIActorPost.h"
#include "OAICrew.h"
#include "OAIPostResult.h"
#include "OAITVShowActor.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAICastCrewCastCrewInMoviesTelevisionShowsApi : public QObject {
    Q_OBJECT

public:
    OAICastCrewCastCrewInMoviesTelevisionShowsApi(const int timeOut = 0);
    ~OAICastCrewCastCrewInMoviesTelevisionShowsApi();

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
    * @param[in]  accesstoken QString [required]
    * @param[in]  query QString [required]
    */
    virtual void actorGet(const QString &accesstoken, const QString &query);

    /**
    * @param[in]  access_token QString [required]
    * @param[in]  actor QString [required]
    */
    virtual void actorInShowsGet(const QString &access_token, const QString &actor);

    /**
    * @param[in]  accesstoken QString [required]
    * @param[in]  show_name QString [required]
    */
    virtual void actorsInTVShowGet(const QString &accesstoken, const QString &show_name);

    /**
    * @param[in]  value OAIActorPost [required]
    */
    virtual void addActorPost(const OAIActorPost &value);

    /**
    * @param[in]  access_token QString [required]
    * @param[in]  actor QString [required]
    */
    virtual void castByActorGet(const QString &access_token, const QString &actor);

    /**
    * @param[in]  access_token QString [required]
    * @param[in]  id QString [required]
    */
    virtual void crewByIDGet(const QString &access_token, const QString &id);

    /**
    * @param[in]  access_token QString [required]
    * @param[in]  person_name QString [required]
    */
    virtual void crewByPersonGet(const QString &access_token, const QString &person_name);

    /**
    * @param[in]  access_token QString [required]
    * @param[in]  phrase QString [required]
    */
    virtual void crewGet(const QString &access_token, const QString &phrase);

    /**
    * @param[in]  access_token QString [required]
    * @param[in]  show_name QString [required]
    */
    virtual void crewbyShownameGet(const QString &access_token, const QString &show_name);


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

    void actorGetCallback(OAIHttpRequestWorker *worker);
    void actorInShowsGetCallback(OAIHttpRequestWorker *worker);
    void actorsInTVShowGetCallback(OAIHttpRequestWorker *worker);
    void addActorPostCallback(OAIHttpRequestWorker *worker);
    void castByActorGetCallback(OAIHttpRequestWorker *worker);
    void crewByIDGetCallback(OAIHttpRequestWorker *worker);
    void crewByPersonGetCallback(OAIHttpRequestWorker *worker);
    void crewGetCallback(OAIHttpRequestWorker *worker);
    void crewbyShownameGetCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void actorGetSignal(QList<OAIActor> summary);
    void actorInShowsGetSignal(QList<OAITVShowActor> summary);
    void actorsInTVShowGetSignal(QList<OAITVShowActor> summary);
    void addActorPostSignal(OAIPostResult summary);
    void castByActorGetSignal(QList<OAITVShowActor> summary);
    void crewByIDGetSignal(QList<OAICrew> summary);
    void crewByPersonGetSignal(QList<OAICrew> summary);
    void crewGetSignal(QList<OAICrew> summary);
    void crewbyShownameGetSignal(QList<OAICrew> summary);


    void actorGetSignalFull(OAIHttpRequestWorker *worker, QList<OAIActor> summary);
    void actorInShowsGetSignalFull(OAIHttpRequestWorker *worker, QList<OAITVShowActor> summary);
    void actorsInTVShowGetSignalFull(OAIHttpRequestWorker *worker, QList<OAITVShowActor> summary);
    void addActorPostSignalFull(OAIHttpRequestWorker *worker, OAIPostResult summary);
    void castByActorGetSignalFull(OAIHttpRequestWorker *worker, QList<OAITVShowActor> summary);
    void crewByIDGetSignalFull(OAIHttpRequestWorker *worker, QList<OAICrew> summary);
    void crewByPersonGetSignalFull(OAIHttpRequestWorker *worker, QList<OAICrew> summary);
    void crewGetSignalFull(OAIHttpRequestWorker *worker, QList<OAICrew> summary);
    void crewbyShownameGetSignalFull(OAIHttpRequestWorker *worker, QList<OAICrew> summary);

    Q_DECL_DEPRECATED_X("Use actorGetSignalError() instead")
    void actorGetSignalE(QList<OAIActor> summary, QNetworkReply::NetworkError error_type, QString error_str);
    void actorGetSignalError(QList<OAIActor> summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use actorInShowsGetSignalError() instead")
    void actorInShowsGetSignalE(QList<OAITVShowActor> summary, QNetworkReply::NetworkError error_type, QString error_str);
    void actorInShowsGetSignalError(QList<OAITVShowActor> summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use actorsInTVShowGetSignalError() instead")
    void actorsInTVShowGetSignalE(QList<OAITVShowActor> summary, QNetworkReply::NetworkError error_type, QString error_str);
    void actorsInTVShowGetSignalError(QList<OAITVShowActor> summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use addActorPostSignalError() instead")
    void addActorPostSignalE(OAIPostResult summary, QNetworkReply::NetworkError error_type, QString error_str);
    void addActorPostSignalError(OAIPostResult summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use castByActorGetSignalError() instead")
    void castByActorGetSignalE(QList<OAITVShowActor> summary, QNetworkReply::NetworkError error_type, QString error_str);
    void castByActorGetSignalError(QList<OAITVShowActor> summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use crewByIDGetSignalError() instead")
    void crewByIDGetSignalE(QList<OAICrew> summary, QNetworkReply::NetworkError error_type, QString error_str);
    void crewByIDGetSignalError(QList<OAICrew> summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use crewByPersonGetSignalError() instead")
    void crewByPersonGetSignalE(QList<OAICrew> summary, QNetworkReply::NetworkError error_type, QString error_str);
    void crewByPersonGetSignalError(QList<OAICrew> summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use crewGetSignalError() instead")
    void crewGetSignalE(QList<OAICrew> summary, QNetworkReply::NetworkError error_type, QString error_str);
    void crewGetSignalError(QList<OAICrew> summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use crewbyShownameGetSignalError() instead")
    void crewbyShownameGetSignalE(QList<OAICrew> summary, QNetworkReply::NetworkError error_type, QString error_str);
    void crewbyShownameGetSignalError(QList<OAICrew> summary, QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use actorGetSignalErrorFull() instead")
    void actorGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void actorGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use actorInShowsGetSignalErrorFull() instead")
    void actorInShowsGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void actorInShowsGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use actorsInTVShowGetSignalErrorFull() instead")
    void actorsInTVShowGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void actorsInTVShowGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use addActorPostSignalErrorFull() instead")
    void addActorPostSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void addActorPostSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use castByActorGetSignalErrorFull() instead")
    void castByActorGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void castByActorGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use crewByIDGetSignalErrorFull() instead")
    void crewByIDGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void crewByIDGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use crewByPersonGetSignalErrorFull() instead")
    void crewByPersonGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void crewByPersonGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use crewGetSignalErrorFull() instead")
    void crewGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void crewGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use crewbyShownameGetSignalErrorFull() instead")
    void crewbyShownameGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void crewbyShownameGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
