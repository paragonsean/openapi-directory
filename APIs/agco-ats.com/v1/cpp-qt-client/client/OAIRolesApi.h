/**
 * AGCO API
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: v1
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

#include "OAIAPI_Models_Role.h"
#include "OAIAPI_Models_RolePermissionChange.h"
#include "OAIAPI_PagedResponse_API_Models_Permission_.h"
#include "OAIAPI_PagedResponse_API_Models_Role_.h"
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
    * @param[in]  id qint32 [required]
    */
    virtual void rolesDeleteRole(const qint32 &id);

    /**
    * @param[in]  id qint32 [required]
    */
    virtual void rolesGetRole(const qint32 &id);

    /**
    * @param[in]  id qint32 [required]
    * @param[in]  name QString [optional]
    * @param[in]  limit qint32 [optional]
    * @param[in]  offset qint32 [optional]
    */
    virtual void rolesGetRolePermissions(const qint32 &id, const ::OpenAPI::OptionalParam<QString> &name = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &limit = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &offset = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  limit qint32 [optional]
    * @param[in]  offset qint32 [optional]
    * @param[in]  name QString [optional]
    * @param[in]  permission_id qint32 [optional]
    * @param[in]  permission_name QString [optional]
    */
    virtual void rolesGetRoles(const ::OpenAPI::OptionalParam<qint32> &limit = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &offset = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &name = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &permission_id = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &permission_name = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  oaiapi_models_role OAIAPI_Models_Role [required]
    */
    virtual void rolesPostRole(const OAIAPI_Models_Role &oaiapi_models_role);

    /**
    * @param[in]  id qint32 [required]
    * @param[in]  oaiapi_models_role OAIAPI_Models_Role [required]
    */
    virtual void rolesPutRole(const qint32 &id, const OAIAPI_Models_Role &oaiapi_models_role);

    /**
    * @param[in]  id qint32 [required]
    * @param[in]  oaiapi_models_role_permission_change QList<OAIAPI_Models_RolePermissionChange> [required]
    */
    virtual void rolesPutRolePermissions(const qint32 &id, const QList<OAIAPI_Models_RolePermissionChange> &oaiapi_models_role_permission_change);


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

    void rolesDeleteRoleCallback(OAIHttpRequestWorker *worker);
    void rolesGetRoleCallback(OAIHttpRequestWorker *worker);
    void rolesGetRolePermissionsCallback(OAIHttpRequestWorker *worker);
    void rolesGetRolesCallback(OAIHttpRequestWorker *worker);
    void rolesPostRoleCallback(OAIHttpRequestWorker *worker);
    void rolesPutRoleCallback(OAIHttpRequestWorker *worker);
    void rolesPutRolePermissionsCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void rolesDeleteRoleSignal();
    void rolesGetRoleSignal(OAIAPI_Models_Role summary);
    void rolesGetRolePermissionsSignal(OAIAPI_PagedResponse_API_Models_Permission_ summary);
    void rolesGetRolesSignal(OAIAPI_PagedResponse_API_Models_Role_ summary);
    void rolesPostRoleSignal(qint32 summary);
    void rolesPutRoleSignal();
    void rolesPutRolePermissionsSignal();


    void rolesDeleteRoleSignalFull(OAIHttpRequestWorker *worker);
    void rolesGetRoleSignalFull(OAIHttpRequestWorker *worker, OAIAPI_Models_Role summary);
    void rolesGetRolePermissionsSignalFull(OAIHttpRequestWorker *worker, OAIAPI_PagedResponse_API_Models_Permission_ summary);
    void rolesGetRolesSignalFull(OAIHttpRequestWorker *worker, OAIAPI_PagedResponse_API_Models_Role_ summary);
    void rolesPostRoleSignalFull(OAIHttpRequestWorker *worker, qint32 summary);
    void rolesPutRoleSignalFull(OAIHttpRequestWorker *worker);
    void rolesPutRolePermissionsSignalFull(OAIHttpRequestWorker *worker);

    Q_DECL_DEPRECATED_X("Use rolesDeleteRoleSignalError() instead")
    void rolesDeleteRoleSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void rolesDeleteRoleSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use rolesGetRoleSignalError() instead")
    void rolesGetRoleSignalE(OAIAPI_Models_Role summary, QNetworkReply::NetworkError error_type, QString error_str);
    void rolesGetRoleSignalError(OAIAPI_Models_Role summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use rolesGetRolePermissionsSignalError() instead")
    void rolesGetRolePermissionsSignalE(OAIAPI_PagedResponse_API_Models_Permission_ summary, QNetworkReply::NetworkError error_type, QString error_str);
    void rolesGetRolePermissionsSignalError(OAIAPI_PagedResponse_API_Models_Permission_ summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use rolesGetRolesSignalError() instead")
    void rolesGetRolesSignalE(OAIAPI_PagedResponse_API_Models_Role_ summary, QNetworkReply::NetworkError error_type, QString error_str);
    void rolesGetRolesSignalError(OAIAPI_PagedResponse_API_Models_Role_ summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use rolesPostRoleSignalError() instead")
    void rolesPostRoleSignalE(qint32 summary, QNetworkReply::NetworkError error_type, QString error_str);
    void rolesPostRoleSignalError(qint32 summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use rolesPutRoleSignalError() instead")
    void rolesPutRoleSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void rolesPutRoleSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use rolesPutRolePermissionsSignalError() instead")
    void rolesPutRolePermissionsSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void rolesPutRolePermissionsSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use rolesDeleteRoleSignalErrorFull() instead")
    void rolesDeleteRoleSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void rolesDeleteRoleSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use rolesGetRoleSignalErrorFull() instead")
    void rolesGetRoleSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void rolesGetRoleSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use rolesGetRolePermissionsSignalErrorFull() instead")
    void rolesGetRolePermissionsSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void rolesGetRolePermissionsSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use rolesGetRolesSignalErrorFull() instead")
    void rolesGetRolesSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void rolesGetRolesSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use rolesPostRoleSignalErrorFull() instead")
    void rolesPostRoleSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void rolesPostRoleSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use rolesPutRoleSignalErrorFull() instead")
    void rolesPutRoleSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void rolesPutRoleSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use rolesPutRolePermissionsSignalErrorFull() instead")
    void rolesPutRolePermissionsSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void rolesPutRolePermissionsSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
