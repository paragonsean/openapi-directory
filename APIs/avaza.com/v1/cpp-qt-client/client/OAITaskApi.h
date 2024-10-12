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

#ifndef OAI_OAITaskApi_H
#define OAI_OAITaskApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAINewTask.h"
#include "OAIObject.h"
#include "OAITaskDetails.h"
#include "OAITaskDropdownList.h"
#include "OAITaskList.h"
#include "OAIUpdateTask.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAITaskApi : public QObject {
    Q_OBJECT

public:
    OAITaskApi(const int timeOut = 0);
    ~OAITaskApi();

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
    * @param[in]  task_id qint64 [required]
    */
    virtual void taskDelete(const qint64 &task_id);

    /**
    * @param[in]  updated_after QDateTime [optional]
    * @param[in]  page_size qint32 [optional]
    * @param[in]  page_number qint32 [optional]
    * @param[in]  sort QString [optional]
    * @param[in]  is_complete bool [optional]
    * @param[in]  project_id qint32 [optional]
    */
    virtual void taskGet(const ::OpenAPI::OptionalParam<QDateTime> &updated_after = ::OpenAPI::OptionalParam<QDateTime>(), const ::OpenAPI::OptionalParam<qint32> &page_size = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &page_number = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &sort = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<bool> &is_complete = ::OpenAPI::OptionalParam<bool>(), const ::OpenAPI::OptionalParam<qint32> &project_id = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  id qint64 [required]
    */
    virtual void taskGetByID(const qint64 &id);

    /**
    * @param[in]  project_id qint32 [required]
    * @param[in]  page_size qint32 [optional]
    * @param[in]  page_number qint32 [optional]
    * @param[in]  hide_completed bool [optional]
    * @param[in]  search QString [optional]
    */
    virtual void taskLookup(const qint32 &project_id, const ::OpenAPI::OptionalParam<qint32> &page_size = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &page_number = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<bool> &hide_completed = ::OpenAPI::OptionalParam<bool>(), const ::OpenAPI::OptionalParam<QString> &search = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  model OAINewTask [required]
    */
    virtual void taskPost(const OAINewTask &model);

    /**
    * @param[in]  model OAIUpdateTask [required]
    */
    virtual void taskPut(const OAIUpdateTask &model);


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

    void taskDeleteCallback(OAIHttpRequestWorker *worker);
    void taskGetCallback(OAIHttpRequestWorker *worker);
    void taskGetByIDCallback(OAIHttpRequestWorker *worker);
    void taskLookupCallback(OAIHttpRequestWorker *worker);
    void taskPostCallback(OAIHttpRequestWorker *worker);
    void taskPutCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void taskDeleteSignal(OAIObject summary);
    void taskGetSignal(OAITaskList summary);
    void taskGetByIDSignal(OAITaskDetails summary);
    void taskLookupSignal(OAITaskDropdownList summary);
    void taskPostSignal(OAITaskDetails summary);
    void taskPutSignal(OAITaskDetails summary);


    void taskDeleteSignalFull(OAIHttpRequestWorker *worker, OAIObject summary);
    void taskGetSignalFull(OAIHttpRequestWorker *worker, OAITaskList summary);
    void taskGetByIDSignalFull(OAIHttpRequestWorker *worker, OAITaskDetails summary);
    void taskLookupSignalFull(OAIHttpRequestWorker *worker, OAITaskDropdownList summary);
    void taskPostSignalFull(OAIHttpRequestWorker *worker, OAITaskDetails summary);
    void taskPutSignalFull(OAIHttpRequestWorker *worker, OAITaskDetails summary);

    Q_DECL_DEPRECATED_X("Use taskDeleteSignalError() instead")
    void taskDeleteSignalE(OAIObject summary, QNetworkReply::NetworkError error_type, QString error_str);
    void taskDeleteSignalError(OAIObject summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use taskGetSignalError() instead")
    void taskGetSignalE(OAITaskList summary, QNetworkReply::NetworkError error_type, QString error_str);
    void taskGetSignalError(OAITaskList summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use taskGetByIDSignalError() instead")
    void taskGetByIDSignalE(OAITaskDetails summary, QNetworkReply::NetworkError error_type, QString error_str);
    void taskGetByIDSignalError(OAITaskDetails summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use taskLookupSignalError() instead")
    void taskLookupSignalE(OAITaskDropdownList summary, QNetworkReply::NetworkError error_type, QString error_str);
    void taskLookupSignalError(OAITaskDropdownList summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use taskPostSignalError() instead")
    void taskPostSignalE(OAITaskDetails summary, QNetworkReply::NetworkError error_type, QString error_str);
    void taskPostSignalError(OAITaskDetails summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use taskPutSignalError() instead")
    void taskPutSignalE(OAITaskDetails summary, QNetworkReply::NetworkError error_type, QString error_str);
    void taskPutSignalError(OAITaskDetails summary, QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use taskDeleteSignalErrorFull() instead")
    void taskDeleteSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void taskDeleteSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use taskGetSignalErrorFull() instead")
    void taskGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void taskGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use taskGetByIDSignalErrorFull() instead")
    void taskGetByIDSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void taskGetByIDSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use taskLookupSignalErrorFull() instead")
    void taskLookupSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void taskLookupSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use taskPostSignalErrorFull() instead")
    void taskPostSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void taskPostSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use taskPutSignalErrorFull() instead")
    void taskPutSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void taskPutSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
