/**
 * DRACOON API
 * REST Web Services for DRACOON<br><br>This page provides an overview of all available and documented DRACOON APIs, which are grouped by tags.<br>Each tag provides a collection of APIs that are intended for a specific area of the DRACOON.<br><br><a title='Developer Information' href='https://developer.dracoon.com'>Developer Information</a>&emsp;&emsp;<a title='Get SDKs on GitHub' href='https://github.com/dracoon'>Get SDKs on GitHub</a><br><br><a title='Terms of service' href='https://www.dracoon.com/terms/general-terms-and-conditions/'>Terms of service</a>
 *
 * The version of the OpenAPI document: 4.42.3
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#ifndef OAI_OAIRolesApi_H
#define OAI_OAIRolesApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAIErrorResponse.h"
#include "OAIGroupIds.h"
#include "OAIRoleGroupList.h"
#include "OAIRoleList.h"
#include "OAIRoleUserList.h"
#include "OAIUserIds.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAIRolesApi : public QObject {
    Q_OBJECT

public:
    OAIRolesApi(const int timeOut = 0);
    ~OAIRolesApi();

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
    * @param[in]  role_id qint32 [required]
    * @param[in]  oai_group_ids OAIGroupIds [required]
    * @param[in]  x_sds_auth_token QString [optional]
    */
    virtual void addRoleGroups(const qint32 &role_id, const OAIGroupIds &oai_group_ids, const ::OpenAPI::OptionalParam<QString> &x_sds_auth_token = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  role_id qint32 [required]
    * @param[in]  oai_user_ids OAIUserIds [required]
    * @param[in]  x_sds_auth_token QString [optional]
    */
    virtual void addRoleUsers(const qint32 &role_id, const OAIUserIds &oai_user_ids, const ::OpenAPI::OptionalParam<QString> &x_sds_auth_token = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  role_id qint32 [required]
    * @param[in]  offset qint32 [optional]
    * @param[in]  limit qint32 [optional]
    * @param[in]  filter QString [optional]
    * @param[in]  x_sds_auth_token QString [optional]
    */
    virtual void requestRoleGroups(const qint32 &role_id, const ::OpenAPI::OptionalParam<qint32> &offset = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &limit = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &filter = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_sds_auth_token = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  role_id qint32 [required]
    * @param[in]  offset qint32 [optional]
    * @param[in]  limit qint32 [optional]
    * @param[in]  filter QString [optional]
    * @param[in]  x_sds_auth_token QString [optional]
    */
    virtual void requestRoleUsers(const qint32 &role_id, const ::OpenAPI::OptionalParam<qint32> &offset = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &limit = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &filter = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &x_sds_auth_token = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  x_sds_auth_token QString [optional]
    */
    virtual void requestRoles(const ::OpenAPI::OptionalParam<QString> &x_sds_auth_token = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  role_id qint32 [required]
    * @param[in]  oai_group_ids OAIGroupIds [required]
    * @param[in]  x_sds_auth_token QString [optional]
    */
    virtual void revokeRoleGroups(const qint32 &role_id, const OAIGroupIds &oai_group_ids, const ::OpenAPI::OptionalParam<QString> &x_sds_auth_token = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  role_id qint32 [required]
    * @param[in]  oai_user_ids OAIUserIds [required]
    * @param[in]  x_sds_auth_token QString [optional]
    */
    virtual void revokeRoleUsers(const qint32 &role_id, const OAIUserIds &oai_user_ids, const ::OpenAPI::OptionalParam<QString> &x_sds_auth_token = ::OpenAPI::OptionalParam<QString>());


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

    void addRoleGroupsCallback(OAIHttpRequestWorker *worker);
    void addRoleUsersCallback(OAIHttpRequestWorker *worker);
    void requestRoleGroupsCallback(OAIHttpRequestWorker *worker);
    void requestRoleUsersCallback(OAIHttpRequestWorker *worker);
    void requestRolesCallback(OAIHttpRequestWorker *worker);
    void revokeRoleGroupsCallback(OAIHttpRequestWorker *worker);
    void revokeRoleUsersCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void addRoleGroupsSignal(OAIRoleGroupList summary);
    void addRoleUsersSignal(OAIRoleUserList summary);
    void requestRoleGroupsSignal(OAIRoleGroupList summary);
    void requestRoleUsersSignal(OAIRoleUserList summary);
    void requestRolesSignal(OAIRoleList summary);
    void revokeRoleGroupsSignal(OAIRoleGroupList summary);
    void revokeRoleUsersSignal(OAIRoleUserList summary);


    void addRoleGroupsSignalFull(OAIHttpRequestWorker *worker, OAIRoleGroupList summary);
    void addRoleUsersSignalFull(OAIHttpRequestWorker *worker, OAIRoleUserList summary);
    void requestRoleGroupsSignalFull(OAIHttpRequestWorker *worker, OAIRoleGroupList summary);
    void requestRoleUsersSignalFull(OAIHttpRequestWorker *worker, OAIRoleUserList summary);
    void requestRolesSignalFull(OAIHttpRequestWorker *worker, OAIRoleList summary);
    void revokeRoleGroupsSignalFull(OAIHttpRequestWorker *worker, OAIRoleGroupList summary);
    void revokeRoleUsersSignalFull(OAIHttpRequestWorker *worker, OAIRoleUserList summary);

    Q_DECL_DEPRECATED_X("Use addRoleGroupsSignalError() instead")
    void addRoleGroupsSignalE(OAIRoleGroupList summary, QNetworkReply::NetworkError error_type, QString error_str);
    void addRoleGroupsSignalError(OAIRoleGroupList summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use addRoleUsersSignalError() instead")
    void addRoleUsersSignalE(OAIRoleUserList summary, QNetworkReply::NetworkError error_type, QString error_str);
    void addRoleUsersSignalError(OAIRoleUserList summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use requestRoleGroupsSignalError() instead")
    void requestRoleGroupsSignalE(OAIRoleGroupList summary, QNetworkReply::NetworkError error_type, QString error_str);
    void requestRoleGroupsSignalError(OAIRoleGroupList summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use requestRoleUsersSignalError() instead")
    void requestRoleUsersSignalE(OAIRoleUserList summary, QNetworkReply::NetworkError error_type, QString error_str);
    void requestRoleUsersSignalError(OAIRoleUserList summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use requestRolesSignalError() instead")
    void requestRolesSignalE(OAIRoleList summary, QNetworkReply::NetworkError error_type, QString error_str);
    void requestRolesSignalError(OAIRoleList summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use revokeRoleGroupsSignalError() instead")
    void revokeRoleGroupsSignalE(OAIRoleGroupList summary, QNetworkReply::NetworkError error_type, QString error_str);
    void revokeRoleGroupsSignalError(OAIRoleGroupList summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use revokeRoleUsersSignalError() instead")
    void revokeRoleUsersSignalE(OAIRoleUserList summary, QNetworkReply::NetworkError error_type, QString error_str);
    void revokeRoleUsersSignalError(OAIRoleUserList summary, QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use addRoleGroupsSignalErrorFull() instead")
    void addRoleGroupsSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void addRoleGroupsSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use addRoleUsersSignalErrorFull() instead")
    void addRoleUsersSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void addRoleUsersSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use requestRoleGroupsSignalErrorFull() instead")
    void requestRoleGroupsSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void requestRoleGroupsSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use requestRoleUsersSignalErrorFull() instead")
    void requestRoleUsersSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void requestRoleUsersSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use requestRolesSignalErrorFull() instead")
    void requestRolesSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void requestRolesSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use revokeRoleGroupsSignalErrorFull() instead")
    void revokeRoleGroupsSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void revokeRoleGroupsSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use revokeRoleUsersSignalErrorFull() instead")
    void revokeRoleUsersSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void revokeRoleUsersSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
