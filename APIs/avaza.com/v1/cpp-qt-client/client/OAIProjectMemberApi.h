/**
 * Avaza API Documentation
 * Welcome to the autogenerated documentation & test tool for Avaza's API. <br/><br/><strong>API Security & Authentication</strong><br/>Authentication options include OAuth2 Implicit and Authorization Code flows, and Personal Access Token. All connections should be encrypted over SSL/TLS <br/><br/>You can set up and manage your api authentication credentials from within your Avaza account. (requires Administrator permissions on your Avaza account).<br/><br/> OAuth2 Authorization endpoint: https://any.avaza.com/oauth2/authorize  <br/>OAuth2 Token endpoint: https://any.avaza.com/oauth2/token<br/>Base URL for subsequent API Requests: https://api.avaza.com/ <br/><br/>Blogpost about authenticating with Avaza's API:  https://www.avaza.com/avaza-api-oauth2-authentication/ <br/>Blogpost on using Avaza's webhooks: https://www.avaza.com/avaza-api-webhook-notifications/<br/>The OAuth flow currently issues Access Tokens that last 1 day, and Refresh tokens that last 180 days<br/>The Api respects the security Roles assigned to the authenticating Avaza user and filters the data return appropriately. <br/><br><strong>Support</strong><br/>For API Support, and to request access please contact Avaza Support Team via our support chat. <br/><br/><strong>User Contributed Libraries:</strong><br/>Graciously contributed by 3rd party users like you. <br/>Note these are not tested or endorsesd by Avaza. We encourage you to review before use, and use at own risk.<br/> <ul><li> - <a target='blank' href='https://packagist.org/packages/debiprasad/oauth2-avaza'>PHP OAuth Client Package for Azava API (by Debiprasad Sahoo)</a></li></ul>
 *
 * The version of the OpenAPI document: v1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#ifndef OAI_OAIProjectMemberApi_H
#define OAI_OAIProjectMemberApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAINewProjectMember.h"
#include "OAIProjectMemberDetails.h"
#include "OAIProjectMemberList.h"
#include "OAIUpdateProjectMember.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAIProjectMemberApi : public QObject {
    Q_OBJECT

public:
    OAIProjectMemberApi(const int timeOut = 0);
    ~OAIProjectMemberApi();

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
    * @param[in]  project_id qint32 [optional]
    * @param[in]  user_id qint32 [optional]
    */
    virtual void projectMemberGet(const ::OpenAPI::OptionalParam<qint32> &project_id = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &user_id = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  model OAINewProjectMember [required]
    */
    virtual void projectMemberPost(const OAINewProjectMember &model);

    /**
    * @param[in]  model OAIUpdateProjectMember [required]
    */
    virtual void projectMemberPut(const OAIUpdateProjectMember &model);


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

    void projectMemberGetCallback(OAIHttpRequestWorker *worker);
    void projectMemberPostCallback(OAIHttpRequestWorker *worker);
    void projectMemberPutCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void projectMemberGetSignal(OAIProjectMemberList summary);
    void projectMemberPostSignal(OAIProjectMemberDetails summary);
    void projectMemberPutSignal(OAIProjectMemberDetails summary);


    void projectMemberGetSignalFull(OAIHttpRequestWorker *worker, OAIProjectMemberList summary);
    void projectMemberPostSignalFull(OAIHttpRequestWorker *worker, OAIProjectMemberDetails summary);
    void projectMemberPutSignalFull(OAIHttpRequestWorker *worker, OAIProjectMemberDetails summary);

    Q_DECL_DEPRECATED_X("Use projectMemberGetSignalError() instead")
    void projectMemberGetSignalE(OAIProjectMemberList summary, QNetworkReply::NetworkError error_type, QString error_str);
    void projectMemberGetSignalError(OAIProjectMemberList summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use projectMemberPostSignalError() instead")
    void projectMemberPostSignalE(OAIProjectMemberDetails summary, QNetworkReply::NetworkError error_type, QString error_str);
    void projectMemberPostSignalError(OAIProjectMemberDetails summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use projectMemberPutSignalError() instead")
    void projectMemberPutSignalE(OAIProjectMemberDetails summary, QNetworkReply::NetworkError error_type, QString error_str);
    void projectMemberPutSignalError(OAIProjectMemberDetails summary, QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use projectMemberGetSignalErrorFull() instead")
    void projectMemberGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void projectMemberGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use projectMemberPostSignalErrorFull() instead")
    void projectMemberPostSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void projectMemberPostSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use projectMemberPutSignalErrorFull() instead")
    void projectMemberPutSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void projectMemberPutSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
