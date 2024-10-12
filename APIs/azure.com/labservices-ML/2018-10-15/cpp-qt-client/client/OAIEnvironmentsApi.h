/**
 * ManagedLabsClient
 * The Managed Labs Client.
 *
 * The version of the OpenAPI document: 2018-10-15
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#ifndef OAI_OAIEnvironmentsApi_H
#define OAI_OAIEnvironmentsApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAICloudError.h"
#include "OAIEnvironment.h"
#include "OAIEnvironmentFragment.h"
#include "OAIResetPasswordPayload.h"
#include "OAIResponseWithContinuation_Environment.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAIEnvironmentsApi : public QObject {
    Q_OBJECT

public:
    OAIEnvironmentsApi(const int timeOut = 0);
    ~OAIEnvironmentsApi();

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
    * @param[in]  subscription_id QString [required]
    * @param[in]  resource_group_name QString [required]
    * @param[in]  lab_account_name QString [required]
    * @param[in]  lab_name QString [required]
    * @param[in]  environment_setting_name QString [required]
    * @param[in]  environment_name QString [required]
    * @param[in]  api_version QString [required]
    */
    virtual void environmentsClaim(const QString &subscription_id, const QString &resource_group_name, const QString &lab_account_name, const QString &lab_name, const QString &environment_setting_name, const QString &environment_name, const QString &api_version);

    /**
    * @param[in]  subscription_id QString [required]
    * @param[in]  resource_group_name QString [required]
    * @param[in]  lab_account_name QString [required]
    * @param[in]  lab_name QString [required]
    * @param[in]  environment_setting_name QString [required]
    * @param[in]  environment_name QString [required]
    * @param[in]  api_version QString [required]
    * @param[in]  environment OAIEnvironment [required]
    */
    virtual void environmentsCreateOrUpdate(const QString &subscription_id, const QString &resource_group_name, const QString &lab_account_name, const QString &lab_name, const QString &environment_setting_name, const QString &environment_name, const QString &api_version, const OAIEnvironment &environment);

    /**
    * @param[in]  subscription_id QString [required]
    * @param[in]  resource_group_name QString [required]
    * @param[in]  lab_account_name QString [required]
    * @param[in]  lab_name QString [required]
    * @param[in]  environment_setting_name QString [required]
    * @param[in]  environment_name QString [required]
    * @param[in]  api_version QString [required]
    */
    virtual void environmentsDelete(const QString &subscription_id, const QString &resource_group_name, const QString &lab_account_name, const QString &lab_name, const QString &environment_setting_name, const QString &environment_name, const QString &api_version);

    /**
    * @param[in]  subscription_id QString [required]
    * @param[in]  resource_group_name QString [required]
    * @param[in]  lab_account_name QString [required]
    * @param[in]  lab_name QString [required]
    * @param[in]  environment_setting_name QString [required]
    * @param[in]  environment_name QString [required]
    * @param[in]  api_version QString [required]
    * @param[in]  expand QString [optional]
    */
    virtual void environmentsGet(const QString &subscription_id, const QString &resource_group_name, const QString &lab_account_name, const QString &lab_name, const QString &environment_setting_name, const QString &environment_name, const QString &api_version, const ::OpenAPI::OptionalParam<QString> &expand = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  subscription_id QString [required]
    * @param[in]  resource_group_name QString [required]
    * @param[in]  lab_account_name QString [required]
    * @param[in]  lab_name QString [required]
    * @param[in]  environment_setting_name QString [required]
    * @param[in]  api_version QString [required]
    * @param[in]  expand QString [optional]
    * @param[in]  filter QString [optional]
    * @param[in]  top qint32 [optional]
    * @param[in]  orderby QString [optional]
    */
    virtual void environmentsList(const QString &subscription_id, const QString &resource_group_name, const QString &lab_account_name, const QString &lab_name, const QString &environment_setting_name, const QString &api_version, const ::OpenAPI::OptionalParam<QString> &expand = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &filter = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &top = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &orderby = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  subscription_id QString [required]
    * @param[in]  resource_group_name QString [required]
    * @param[in]  lab_account_name QString [required]
    * @param[in]  lab_name QString [required]
    * @param[in]  environment_setting_name QString [required]
    * @param[in]  environment_name QString [required]
    * @param[in]  api_version QString [required]
    * @param[in]  reset_password_payload OAIResetPasswordPayload [required]
    */
    virtual void environmentsResetPassword(const QString &subscription_id, const QString &resource_group_name, const QString &lab_account_name, const QString &lab_name, const QString &environment_setting_name, const QString &environment_name, const QString &api_version, const OAIResetPasswordPayload &reset_password_payload);

    /**
    * @param[in]  subscription_id QString [required]
    * @param[in]  resource_group_name QString [required]
    * @param[in]  lab_account_name QString [required]
    * @param[in]  lab_name QString [required]
    * @param[in]  environment_setting_name QString [required]
    * @param[in]  environment_name QString [required]
    * @param[in]  api_version QString [required]
    */
    virtual void environmentsStart(const QString &subscription_id, const QString &resource_group_name, const QString &lab_account_name, const QString &lab_name, const QString &environment_setting_name, const QString &environment_name, const QString &api_version);

    /**
    * @param[in]  subscription_id QString [required]
    * @param[in]  resource_group_name QString [required]
    * @param[in]  lab_account_name QString [required]
    * @param[in]  lab_name QString [required]
    * @param[in]  environment_setting_name QString [required]
    * @param[in]  environment_name QString [required]
    * @param[in]  api_version QString [required]
    */
    virtual void environmentsStop(const QString &subscription_id, const QString &resource_group_name, const QString &lab_account_name, const QString &lab_name, const QString &environment_setting_name, const QString &environment_name, const QString &api_version);

    /**
    * @param[in]  subscription_id QString [required]
    * @param[in]  resource_group_name QString [required]
    * @param[in]  lab_account_name QString [required]
    * @param[in]  lab_name QString [required]
    * @param[in]  environment_setting_name QString [required]
    * @param[in]  environment_name QString [required]
    * @param[in]  api_version QString [required]
    * @param[in]  environment OAIEnvironmentFragment [required]
    */
    virtual void environmentsUpdate(const QString &subscription_id, const QString &resource_group_name, const QString &lab_account_name, const QString &lab_name, const QString &environment_setting_name, const QString &environment_name, const QString &api_version, const OAIEnvironmentFragment &environment);


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

    void environmentsClaimCallback(OAIHttpRequestWorker *worker);
    void environmentsCreateOrUpdateCallback(OAIHttpRequestWorker *worker);
    void environmentsDeleteCallback(OAIHttpRequestWorker *worker);
    void environmentsGetCallback(OAIHttpRequestWorker *worker);
    void environmentsListCallback(OAIHttpRequestWorker *worker);
    void environmentsResetPasswordCallback(OAIHttpRequestWorker *worker);
    void environmentsStartCallback(OAIHttpRequestWorker *worker);
    void environmentsStopCallback(OAIHttpRequestWorker *worker);
    void environmentsUpdateCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void environmentsClaimSignal();
    void environmentsCreateOrUpdateSignal(OAIEnvironment summary);
    void environmentsDeleteSignal();
    void environmentsGetSignal(OAIEnvironment summary);
    void environmentsListSignal(OAIResponseWithContinuation_Environment summary);
    void environmentsResetPasswordSignal();
    void environmentsStartSignal();
    void environmentsStopSignal();
    void environmentsUpdateSignal(OAIEnvironment summary);


    void environmentsClaimSignalFull(OAIHttpRequestWorker *worker);
    void environmentsCreateOrUpdateSignalFull(OAIHttpRequestWorker *worker, OAIEnvironment summary);
    void environmentsDeleteSignalFull(OAIHttpRequestWorker *worker);
    void environmentsGetSignalFull(OAIHttpRequestWorker *worker, OAIEnvironment summary);
    void environmentsListSignalFull(OAIHttpRequestWorker *worker, OAIResponseWithContinuation_Environment summary);
    void environmentsResetPasswordSignalFull(OAIHttpRequestWorker *worker);
    void environmentsStartSignalFull(OAIHttpRequestWorker *worker);
    void environmentsStopSignalFull(OAIHttpRequestWorker *worker);
    void environmentsUpdateSignalFull(OAIHttpRequestWorker *worker, OAIEnvironment summary);

    Q_DECL_DEPRECATED_X("Use environmentsClaimSignalError() instead")
    void environmentsClaimSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void environmentsClaimSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use environmentsCreateOrUpdateSignalError() instead")
    void environmentsCreateOrUpdateSignalE(OAIEnvironment summary, QNetworkReply::NetworkError error_type, QString error_str);
    void environmentsCreateOrUpdateSignalError(OAIEnvironment summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use environmentsDeleteSignalError() instead")
    void environmentsDeleteSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void environmentsDeleteSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use environmentsGetSignalError() instead")
    void environmentsGetSignalE(OAIEnvironment summary, QNetworkReply::NetworkError error_type, QString error_str);
    void environmentsGetSignalError(OAIEnvironment summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use environmentsListSignalError() instead")
    void environmentsListSignalE(OAIResponseWithContinuation_Environment summary, QNetworkReply::NetworkError error_type, QString error_str);
    void environmentsListSignalError(OAIResponseWithContinuation_Environment summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use environmentsResetPasswordSignalError() instead")
    void environmentsResetPasswordSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void environmentsResetPasswordSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use environmentsStartSignalError() instead")
    void environmentsStartSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void environmentsStartSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use environmentsStopSignalError() instead")
    void environmentsStopSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void environmentsStopSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use environmentsUpdateSignalError() instead")
    void environmentsUpdateSignalE(OAIEnvironment summary, QNetworkReply::NetworkError error_type, QString error_str);
    void environmentsUpdateSignalError(OAIEnvironment summary, QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use environmentsClaimSignalErrorFull() instead")
    void environmentsClaimSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void environmentsClaimSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use environmentsCreateOrUpdateSignalErrorFull() instead")
    void environmentsCreateOrUpdateSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void environmentsCreateOrUpdateSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use environmentsDeleteSignalErrorFull() instead")
    void environmentsDeleteSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void environmentsDeleteSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use environmentsGetSignalErrorFull() instead")
    void environmentsGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void environmentsGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use environmentsListSignalErrorFull() instead")
    void environmentsListSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void environmentsListSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use environmentsResetPasswordSignalErrorFull() instead")
    void environmentsResetPasswordSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void environmentsResetPasswordSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use environmentsStartSignalErrorFull() instead")
    void environmentsStartSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void environmentsStartSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use environmentsStopSignalErrorFull() instead")
    void environmentsStopSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void environmentsStopSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use environmentsUpdateSignalErrorFull() instead")
    void environmentsUpdateSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void environmentsUpdateSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
