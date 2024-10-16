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

#ifndef OAI_OAIReportingApi_H
#define OAI_OAIReportingApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAIAPI_Models_ApiError.h"
#include "OAIAPI_PagedResponse_UpdateSystem_Models_Bundle_.h"
#include "OAIAPI_PagedResponse_UpdateSystem_Models_ClientStatus_UpdateSystem_Models_PagedClientStatusMetadata_.h"
#include "OAIAPI_PagedResponse_UpdateSystem_Models_PackageStatusSummary_.h"
#include "OAIAPI_PagedResponse_UpdateSystem_Models_UpdateGroupClientRelationship_.h"
#include "OAIAPI_PagedResponse_UpdateSystem_Models_UpdateGroup_.h"
#include "OAIUpdateSystem_Models_Client.h"
#include "OAIUpdateSystem_Models_ClientInfo.h"
#include "OAIUpdateSystem_Models_Package.h"
#include "OAIUpdateSystem_Models_PackageStatusSummary.h"
#include "OAIUpdateSystem_Models_UpdateMetricsData.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAIReportingApi : public QObject {
    Q_OBJECT

public:
    OAIReportingApi(const int timeOut = 0);
    ~OAIReportingApi();

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
    * @param[in]  bundle_id QString [required]
    * @param[in]  limit qint32 [optional]
    * @param[in]  offset qint32 [optional]
    */
    virtual void reportingBundleStatusSummary(const QString &bundle_id, const ::OpenAPI::OptionalParam<qint32> &limit = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &offset = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  id QString [required]
    * @param[in]  include_inactive bool [required]
    * @param[in]  limit qint32 [optional]
    * @param[in]  offset qint32 [optional]
    */
    virtual void reportingBundlesInUpdateGroup(const QString &id, const bool &include_inactive, const ::OpenAPI::OptionalParam<qint32> &limit = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &offset = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  client_id QString [required]
    */
    virtual void reportingClientInfo(const QString &client_id);

    /**
    * @param[in]  id QString [required]
    * @param[in]  subscription_type_filter QString [optional]
    */
    virtual void reportingCurrentPackagesInUpdateGroup(const QString &id, const ::OpenAPI::OptionalParam<QString> &subscription_type_filter = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  id QString [required]
    */
    virtual void reportingGetClient(const QString &id);

    /**
    * @param[in]  client_id QString [optional]
    * @param[in]  update_group_id QString [optional]
    * @param[in]  limit qint32 [optional]
    * @param[in]  offset qint32 [optional]
    */
    virtual void reportingGetSubscriptions(const ::OpenAPI::OptionalParam<QString> &client_id = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &update_group_id = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &limit = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &offset = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  package_id QString [required]
    */
    virtual void reportingPackageStatusSummary(const QString &package_id);

    /**
    * @param[in]  update_group_id QString [optional]
    * @param[in]  client_id QString [optional]
    * @param[in]  tag QString [optional]
    * @param[in]  report_result QString [optional]
    * @param[in]  report_result_is_valid bool [optional]
    * @param[in]  report_value QString [optional]
    * @param[in]  last_check_in_before QDateTime [optional]
    * @param[in]  last_check_in_after QDateTime [optional]
    * @param[in]  order_by QString [optional]
    * @param[in]  limit qint32 [optional]
    * @param[in]  offset qint32 [optional]
    */
    virtual void reportingRegisteredClients(const ::OpenAPI::OptionalParam<QString> &update_group_id = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &client_id = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &tag = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &report_result = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<bool> &report_result_is_valid = ::OpenAPI::OptionalParam<bool>(), const ::OpenAPI::OptionalParam<QString> &report_value = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QDateTime> &last_check_in_before = ::OpenAPI::OptionalParam<QDateTime>(), const ::OpenAPI::OptionalParam<QDateTime> &last_check_in_after = ::OpenAPI::OptionalParam<QDateTime>(), const ::OpenAPI::OptionalParam<QString> &order_by = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &limit = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &offset = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  limit qint32 [optional]
    * @param[in]  offset qint32 [optional]
    */
    virtual void reportingUpdateGroups(const ::OpenAPI::OptionalParam<qint32> &limit = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &offset = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  update_group_id QString [required]
    * @param[in]  bundle_number qint32 [optional]
    */
    virtual void reportingUpdateMetrics(const QString &update_group_id, const ::OpenAPI::OptionalParam<qint32> &bundle_number = ::OpenAPI::OptionalParam<qint32>());


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

    void reportingBundleStatusSummaryCallback(OAIHttpRequestWorker *worker);
    void reportingBundlesInUpdateGroupCallback(OAIHttpRequestWorker *worker);
    void reportingClientInfoCallback(OAIHttpRequestWorker *worker);
    void reportingCurrentPackagesInUpdateGroupCallback(OAIHttpRequestWorker *worker);
    void reportingGetClientCallback(OAIHttpRequestWorker *worker);
    void reportingGetSubscriptionsCallback(OAIHttpRequestWorker *worker);
    void reportingPackageStatusSummaryCallback(OAIHttpRequestWorker *worker);
    void reportingRegisteredClientsCallback(OAIHttpRequestWorker *worker);
    void reportingUpdateGroupsCallback(OAIHttpRequestWorker *worker);
    void reportingUpdateMetricsCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void reportingBundleStatusSummarySignal(OAIAPI_PagedResponse_UpdateSystem_Models_PackageStatusSummary_ summary);
    void reportingBundlesInUpdateGroupSignal(OAIAPI_PagedResponse_UpdateSystem_Models_Bundle_ summary);
    void reportingClientInfoSignal(OAIUpdateSystem_Models_ClientInfo summary);
    void reportingCurrentPackagesInUpdateGroupSignal(QList<OAIUpdateSystem_Models_Package> summary);
    void reportingGetClientSignal(OAIUpdateSystem_Models_Client summary);
    void reportingGetSubscriptionsSignal(OAIAPI_PagedResponse_UpdateSystem_Models_UpdateGroupClientRelationship_ summary);
    void reportingPackageStatusSummarySignal(OAIUpdateSystem_Models_PackageStatusSummary summary);
    void reportingRegisteredClientsSignal(OAIAPI_PagedResponse_UpdateSystem_Models_ClientStatus_UpdateSystem_Models_PagedClientStatusMetadata_ summary);
    void reportingUpdateGroupsSignal(OAIAPI_PagedResponse_UpdateSystem_Models_UpdateGroup_ summary);
    void reportingUpdateMetricsSignal(OAIUpdateSystem_Models_UpdateMetricsData summary);


    void reportingBundleStatusSummarySignalFull(OAIHttpRequestWorker *worker, OAIAPI_PagedResponse_UpdateSystem_Models_PackageStatusSummary_ summary);
    void reportingBundlesInUpdateGroupSignalFull(OAIHttpRequestWorker *worker, OAIAPI_PagedResponse_UpdateSystem_Models_Bundle_ summary);
    void reportingClientInfoSignalFull(OAIHttpRequestWorker *worker, OAIUpdateSystem_Models_ClientInfo summary);
    void reportingCurrentPackagesInUpdateGroupSignalFull(OAIHttpRequestWorker *worker, QList<OAIUpdateSystem_Models_Package> summary);
    void reportingGetClientSignalFull(OAIHttpRequestWorker *worker, OAIUpdateSystem_Models_Client summary);
    void reportingGetSubscriptionsSignalFull(OAIHttpRequestWorker *worker, OAIAPI_PagedResponse_UpdateSystem_Models_UpdateGroupClientRelationship_ summary);
    void reportingPackageStatusSummarySignalFull(OAIHttpRequestWorker *worker, OAIUpdateSystem_Models_PackageStatusSummary summary);
    void reportingRegisteredClientsSignalFull(OAIHttpRequestWorker *worker, OAIAPI_PagedResponse_UpdateSystem_Models_ClientStatus_UpdateSystem_Models_PagedClientStatusMetadata_ summary);
    void reportingUpdateGroupsSignalFull(OAIHttpRequestWorker *worker, OAIAPI_PagedResponse_UpdateSystem_Models_UpdateGroup_ summary);
    void reportingUpdateMetricsSignalFull(OAIHttpRequestWorker *worker, OAIUpdateSystem_Models_UpdateMetricsData summary);

    Q_DECL_DEPRECATED_X("Use reportingBundleStatusSummarySignalError() instead")
    void reportingBundleStatusSummarySignalE(OAIAPI_PagedResponse_UpdateSystem_Models_PackageStatusSummary_ summary, QNetworkReply::NetworkError error_type, QString error_str);
    void reportingBundleStatusSummarySignalError(OAIAPI_PagedResponse_UpdateSystem_Models_PackageStatusSummary_ summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use reportingBundlesInUpdateGroupSignalError() instead")
    void reportingBundlesInUpdateGroupSignalE(OAIAPI_PagedResponse_UpdateSystem_Models_Bundle_ summary, QNetworkReply::NetworkError error_type, QString error_str);
    void reportingBundlesInUpdateGroupSignalError(OAIAPI_PagedResponse_UpdateSystem_Models_Bundle_ summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use reportingClientInfoSignalError() instead")
    void reportingClientInfoSignalE(OAIUpdateSystem_Models_ClientInfo summary, QNetworkReply::NetworkError error_type, QString error_str);
    void reportingClientInfoSignalError(OAIUpdateSystem_Models_ClientInfo summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use reportingCurrentPackagesInUpdateGroupSignalError() instead")
    void reportingCurrentPackagesInUpdateGroupSignalE(QList<OAIUpdateSystem_Models_Package> summary, QNetworkReply::NetworkError error_type, QString error_str);
    void reportingCurrentPackagesInUpdateGroupSignalError(QList<OAIUpdateSystem_Models_Package> summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use reportingGetClientSignalError() instead")
    void reportingGetClientSignalE(OAIUpdateSystem_Models_Client summary, QNetworkReply::NetworkError error_type, QString error_str);
    void reportingGetClientSignalError(OAIUpdateSystem_Models_Client summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use reportingGetSubscriptionsSignalError() instead")
    void reportingGetSubscriptionsSignalE(OAIAPI_PagedResponse_UpdateSystem_Models_UpdateGroupClientRelationship_ summary, QNetworkReply::NetworkError error_type, QString error_str);
    void reportingGetSubscriptionsSignalError(OAIAPI_PagedResponse_UpdateSystem_Models_UpdateGroupClientRelationship_ summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use reportingPackageStatusSummarySignalError() instead")
    void reportingPackageStatusSummarySignalE(OAIUpdateSystem_Models_PackageStatusSummary summary, QNetworkReply::NetworkError error_type, QString error_str);
    void reportingPackageStatusSummarySignalError(OAIUpdateSystem_Models_PackageStatusSummary summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use reportingRegisteredClientsSignalError() instead")
    void reportingRegisteredClientsSignalE(OAIAPI_PagedResponse_UpdateSystem_Models_ClientStatus_UpdateSystem_Models_PagedClientStatusMetadata_ summary, QNetworkReply::NetworkError error_type, QString error_str);
    void reportingRegisteredClientsSignalError(OAIAPI_PagedResponse_UpdateSystem_Models_ClientStatus_UpdateSystem_Models_PagedClientStatusMetadata_ summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use reportingUpdateGroupsSignalError() instead")
    void reportingUpdateGroupsSignalE(OAIAPI_PagedResponse_UpdateSystem_Models_UpdateGroup_ summary, QNetworkReply::NetworkError error_type, QString error_str);
    void reportingUpdateGroupsSignalError(OAIAPI_PagedResponse_UpdateSystem_Models_UpdateGroup_ summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use reportingUpdateMetricsSignalError() instead")
    void reportingUpdateMetricsSignalE(OAIUpdateSystem_Models_UpdateMetricsData summary, QNetworkReply::NetworkError error_type, QString error_str);
    void reportingUpdateMetricsSignalError(OAIUpdateSystem_Models_UpdateMetricsData summary, QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use reportingBundleStatusSummarySignalErrorFull() instead")
    void reportingBundleStatusSummarySignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void reportingBundleStatusSummarySignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use reportingBundlesInUpdateGroupSignalErrorFull() instead")
    void reportingBundlesInUpdateGroupSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void reportingBundlesInUpdateGroupSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use reportingClientInfoSignalErrorFull() instead")
    void reportingClientInfoSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void reportingClientInfoSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use reportingCurrentPackagesInUpdateGroupSignalErrorFull() instead")
    void reportingCurrentPackagesInUpdateGroupSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void reportingCurrentPackagesInUpdateGroupSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use reportingGetClientSignalErrorFull() instead")
    void reportingGetClientSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void reportingGetClientSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use reportingGetSubscriptionsSignalErrorFull() instead")
    void reportingGetSubscriptionsSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void reportingGetSubscriptionsSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use reportingPackageStatusSummarySignalErrorFull() instead")
    void reportingPackageStatusSummarySignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void reportingPackageStatusSummarySignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use reportingRegisteredClientsSignalErrorFull() instead")
    void reportingRegisteredClientsSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void reportingRegisteredClientsSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use reportingUpdateGroupsSignalErrorFull() instead")
    void reportingUpdateGroupsSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void reportingUpdateGroupsSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use reportingUpdateMetricsSignalErrorFull() instead")
    void reportingUpdateMetricsSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void reportingUpdateMetricsSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
