/**
 * Clever-Cloud API
 * Public API for managing Clever-Cloud data and products
 *
 * The version of the OpenAPI document: 1.0.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#ifndef OAI_OAIUsersApi_H
#define OAI_OAIUsersApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAIApplication.h"
#include "OAIUser.h"
#include "OAIWannabeUser.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAIUsersApi : public QObject {
    Q_OBJECT

public:
    OAIUsersApi(const int timeOut = 0);
    ~OAIUsersApi();

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
    * @param[in]  id QString [required]
    */
    virtual void getUsersIdApplications(const QString &id);

    /**
    * @param[in]  id QString [required]
    */
    virtual void getUsersId(const QString &id);

    /**
    * @param[in]  user_id QString [required]
    */
    virtual void getUsersUserIdGitInfo(const QString &user_id);

    /**
    * @param[in]  oai_wannabe_user OAIWannabeUser [required]
    * @param[in]  invitation_key QString [optional]
    * @param[in]  addon_beta_invitation_key QString [optional]
    * @param[in]  email QString [optional]
    * @param[in]  pass QString [optional]
    * @param[in]  url_next QString [optional]
    * @param[in]  terms QString [optional]
    */
    virtual void postUsers(const OAIWannabeUser &oai_wannabe_user, const ::OpenAPI::OptionalParam<QString> &invitation_key = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &addon_beta_invitation_key = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &email = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &pass = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &url_next = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &terms = ::OpenAPI::OptionalParam<QString>());


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

    void getUsersIdApplicationsCallback(OAIHttpRequestWorker *worker);
    void getUsersIdCallback(OAIHttpRequestWorker *worker);
    void getUsersUserIdGitInfoCallback(OAIHttpRequestWorker *worker);
    void postUsersCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void getUsersIdApplicationsSignal(QList<OAIApplication> summary);
    void getUsersIdSignal(OAIUser summary);
    void getUsersUserIdGitInfoSignal();
    void postUsersSignal();


    void getUsersIdApplicationsSignalFull(OAIHttpRequestWorker *worker, QList<OAIApplication> summary);
    void getUsersIdSignalFull(OAIHttpRequestWorker *worker, OAIUser summary);
    void getUsersUserIdGitInfoSignalFull(OAIHttpRequestWorker *worker);
    void postUsersSignalFull(OAIHttpRequestWorker *worker);

    Q_DECL_DEPRECATED_X("Use getUsersIdApplicationsSignalError() instead")
    void getUsersIdApplicationsSignalE(QList<OAIApplication> summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getUsersIdApplicationsSignalError(QList<OAIApplication> summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getUsersIdSignalError() instead")
    void getUsersIdSignalE(OAIUser summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getUsersIdSignalError(OAIUser summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getUsersUserIdGitInfoSignalError() instead")
    void getUsersUserIdGitInfoSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void getUsersUserIdGitInfoSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use postUsersSignalError() instead")
    void postUsersSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void postUsersSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use getUsersIdApplicationsSignalErrorFull() instead")
    void getUsersIdApplicationsSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getUsersIdApplicationsSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getUsersIdSignalErrorFull() instead")
    void getUsersIdSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getUsersIdSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getUsersUserIdGitInfoSignalErrorFull() instead")
    void getUsersUserIdGitInfoSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getUsersUserIdGitInfoSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use postUsersSignalErrorFull() instead")
    void postUsersSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void postUsersSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
