/**
 * Meraki Dashboard API
 * The Cisco Meraki Dashboard API is a modern REST API based on the OpenAPI specification.  > Date: 05 April, 2023 > > [Recent Updates](https://meraki.io/whats-new/)  ---  [API Documentation](https://meraki.io/api)  [Community Support](https://meraki.io/community)  [Meraki Homepage](https://www.meraki.com) 
 *
 * The version of the OpenAPI document: 1.32.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#ifndef OAI_OAISummaryApi_H
#define OAI_OAISummaryApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAIGetOrganizationSummaryTopAppliancesByUtilization_200_response_inner.h"
#include "OAIGetOrganizationSummaryTopClientsByUsage_200_response_inner.h"
#include "OAIGetOrganizationSummaryTopClientsManufacturersByUsage_200_response_inner.h"
#include "OAIGetOrganizationSummaryTopDevicesByUsage_200_response_inner.h"
#include "OAIGetOrganizationSummaryTopDevicesModelsByUsage_200_response_inner.h"
#include "OAIGetOrganizationSummaryTopSsidsByUsage_200_response_inner.h"
#include "OAIGetOrganizationSummaryTopSwitchesByEnergyUsage_200_response_inner.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAISummaryApi : public QObject {
    Q_OBJECT

public:
    OAISummaryApi(const int timeOut = 0);
    ~OAISummaryApi();

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
    * @param[in]  organization_id QString [required]
    * @param[in]  t0 QString [optional]
    * @param[in]  t1 QString [optional]
    * @param[in]  timespan float [optional]
    */
    virtual void getOrganizationSummaryTopAppliancesByUtilization(const QString &organization_id, const ::OpenAPI::OptionalParam<QString> &t0 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &t1 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<float> &timespan = ::OpenAPI::OptionalParam<float>());

    /**
    * @param[in]  organization_id QString [required]
    * @param[in]  t0 QString [optional]
    * @param[in]  t1 QString [optional]
    * @param[in]  timespan float [optional]
    */
    virtual void getOrganizationSummaryTopClientsByUsage(const QString &organization_id, const ::OpenAPI::OptionalParam<QString> &t0 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &t1 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<float> &timespan = ::OpenAPI::OptionalParam<float>());

    /**
    * @param[in]  organization_id QString [required]
    * @param[in]  t0 QString [optional]
    * @param[in]  t1 QString [optional]
    * @param[in]  timespan float [optional]
    */
    virtual void getOrganizationSummaryTopClientsManufacturersByUsage(const QString &organization_id, const ::OpenAPI::OptionalParam<QString> &t0 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &t1 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<float> &timespan = ::OpenAPI::OptionalParam<float>());

    /**
    * @param[in]  organization_id QString [required]
    * @param[in]  t0 QString [optional]
    * @param[in]  t1 QString [optional]
    * @param[in]  timespan float [optional]
    */
    virtual void getOrganizationSummaryTopDevicesByUsage(const QString &organization_id, const ::OpenAPI::OptionalParam<QString> &t0 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &t1 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<float> &timespan = ::OpenAPI::OptionalParam<float>());

    /**
    * @param[in]  organization_id QString [required]
    * @param[in]  t0 QString [optional]
    * @param[in]  t1 QString [optional]
    * @param[in]  timespan float [optional]
    */
    virtual void getOrganizationSummaryTopDevicesModelsByUsage(const QString &organization_id, const ::OpenAPI::OptionalParam<QString> &t0 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &t1 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<float> &timespan = ::OpenAPI::OptionalParam<float>());

    /**
    * @param[in]  organization_id QString [required]
    * @param[in]  t0 QString [optional]
    * @param[in]  t1 QString [optional]
    * @param[in]  timespan float [optional]
    */
    virtual void getOrganizationSummaryTopSsidsByUsage(const QString &organization_id, const ::OpenAPI::OptionalParam<QString> &t0 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &t1 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<float> &timespan = ::OpenAPI::OptionalParam<float>());

    /**
    * @param[in]  organization_id QString [required]
    * @param[in]  t0 QString [optional]
    * @param[in]  t1 QString [optional]
    * @param[in]  timespan float [optional]
    */
    virtual void getOrganizationSummaryTopSwitchesByEnergyUsage(const QString &organization_id, const ::OpenAPI::OptionalParam<QString> &t0 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &t1 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<float> &timespan = ::OpenAPI::OptionalParam<float>());


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

    void getOrganizationSummaryTopAppliancesByUtilizationCallback(OAIHttpRequestWorker *worker);
    void getOrganizationSummaryTopClientsByUsageCallback(OAIHttpRequestWorker *worker);
    void getOrganizationSummaryTopClientsManufacturersByUsageCallback(OAIHttpRequestWorker *worker);
    void getOrganizationSummaryTopDevicesByUsageCallback(OAIHttpRequestWorker *worker);
    void getOrganizationSummaryTopDevicesModelsByUsageCallback(OAIHttpRequestWorker *worker);
    void getOrganizationSummaryTopSsidsByUsageCallback(OAIHttpRequestWorker *worker);
    void getOrganizationSummaryTopSwitchesByEnergyUsageCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void getOrganizationSummaryTopAppliancesByUtilizationSignal(QList<OAIGetOrganizationSummaryTopAppliancesByUtilization_200_response_inner> summary);
    void getOrganizationSummaryTopClientsByUsageSignal(QList<OAIGetOrganizationSummaryTopClientsByUsage_200_response_inner> summary);
    void getOrganizationSummaryTopClientsManufacturersByUsageSignal(QList<OAIGetOrganizationSummaryTopClientsManufacturersByUsage_200_response_inner> summary);
    void getOrganizationSummaryTopDevicesByUsageSignal(QList<OAIGetOrganizationSummaryTopDevicesByUsage_200_response_inner> summary);
    void getOrganizationSummaryTopDevicesModelsByUsageSignal(QList<OAIGetOrganizationSummaryTopDevicesModelsByUsage_200_response_inner> summary);
    void getOrganizationSummaryTopSsidsByUsageSignal(QList<OAIGetOrganizationSummaryTopSsidsByUsage_200_response_inner> summary);
    void getOrganizationSummaryTopSwitchesByEnergyUsageSignal(QList<OAIGetOrganizationSummaryTopSwitchesByEnergyUsage_200_response_inner> summary);


    void getOrganizationSummaryTopAppliancesByUtilizationSignalFull(OAIHttpRequestWorker *worker, QList<OAIGetOrganizationSummaryTopAppliancesByUtilization_200_response_inner> summary);
    void getOrganizationSummaryTopClientsByUsageSignalFull(OAIHttpRequestWorker *worker, QList<OAIGetOrganizationSummaryTopClientsByUsage_200_response_inner> summary);
    void getOrganizationSummaryTopClientsManufacturersByUsageSignalFull(OAIHttpRequestWorker *worker, QList<OAIGetOrganizationSummaryTopClientsManufacturersByUsage_200_response_inner> summary);
    void getOrganizationSummaryTopDevicesByUsageSignalFull(OAIHttpRequestWorker *worker, QList<OAIGetOrganizationSummaryTopDevicesByUsage_200_response_inner> summary);
    void getOrganizationSummaryTopDevicesModelsByUsageSignalFull(OAIHttpRequestWorker *worker, QList<OAIGetOrganizationSummaryTopDevicesModelsByUsage_200_response_inner> summary);
    void getOrganizationSummaryTopSsidsByUsageSignalFull(OAIHttpRequestWorker *worker, QList<OAIGetOrganizationSummaryTopSsidsByUsage_200_response_inner> summary);
    void getOrganizationSummaryTopSwitchesByEnergyUsageSignalFull(OAIHttpRequestWorker *worker, QList<OAIGetOrganizationSummaryTopSwitchesByEnergyUsage_200_response_inner> summary);

    Q_DECL_DEPRECATED_X("Use getOrganizationSummaryTopAppliancesByUtilizationSignalError() instead")
    void getOrganizationSummaryTopAppliancesByUtilizationSignalE(QList<OAIGetOrganizationSummaryTopAppliancesByUtilization_200_response_inner> summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getOrganizationSummaryTopAppliancesByUtilizationSignalError(QList<OAIGetOrganizationSummaryTopAppliancesByUtilization_200_response_inner> summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getOrganizationSummaryTopClientsByUsageSignalError() instead")
    void getOrganizationSummaryTopClientsByUsageSignalE(QList<OAIGetOrganizationSummaryTopClientsByUsage_200_response_inner> summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getOrganizationSummaryTopClientsByUsageSignalError(QList<OAIGetOrganizationSummaryTopClientsByUsage_200_response_inner> summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getOrganizationSummaryTopClientsManufacturersByUsageSignalError() instead")
    void getOrganizationSummaryTopClientsManufacturersByUsageSignalE(QList<OAIGetOrganizationSummaryTopClientsManufacturersByUsage_200_response_inner> summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getOrganizationSummaryTopClientsManufacturersByUsageSignalError(QList<OAIGetOrganizationSummaryTopClientsManufacturersByUsage_200_response_inner> summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getOrganizationSummaryTopDevicesByUsageSignalError() instead")
    void getOrganizationSummaryTopDevicesByUsageSignalE(QList<OAIGetOrganizationSummaryTopDevicesByUsage_200_response_inner> summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getOrganizationSummaryTopDevicesByUsageSignalError(QList<OAIGetOrganizationSummaryTopDevicesByUsage_200_response_inner> summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getOrganizationSummaryTopDevicesModelsByUsageSignalError() instead")
    void getOrganizationSummaryTopDevicesModelsByUsageSignalE(QList<OAIGetOrganizationSummaryTopDevicesModelsByUsage_200_response_inner> summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getOrganizationSummaryTopDevicesModelsByUsageSignalError(QList<OAIGetOrganizationSummaryTopDevicesModelsByUsage_200_response_inner> summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getOrganizationSummaryTopSsidsByUsageSignalError() instead")
    void getOrganizationSummaryTopSsidsByUsageSignalE(QList<OAIGetOrganizationSummaryTopSsidsByUsage_200_response_inner> summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getOrganizationSummaryTopSsidsByUsageSignalError(QList<OAIGetOrganizationSummaryTopSsidsByUsage_200_response_inner> summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getOrganizationSummaryTopSwitchesByEnergyUsageSignalError() instead")
    void getOrganizationSummaryTopSwitchesByEnergyUsageSignalE(QList<OAIGetOrganizationSummaryTopSwitchesByEnergyUsage_200_response_inner> summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getOrganizationSummaryTopSwitchesByEnergyUsageSignalError(QList<OAIGetOrganizationSummaryTopSwitchesByEnergyUsage_200_response_inner> summary, QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use getOrganizationSummaryTopAppliancesByUtilizationSignalErrorFull() instead")
    void getOrganizationSummaryTopAppliancesByUtilizationSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getOrganizationSummaryTopAppliancesByUtilizationSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getOrganizationSummaryTopClientsByUsageSignalErrorFull() instead")
    void getOrganizationSummaryTopClientsByUsageSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getOrganizationSummaryTopClientsByUsageSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getOrganizationSummaryTopClientsManufacturersByUsageSignalErrorFull() instead")
    void getOrganizationSummaryTopClientsManufacturersByUsageSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getOrganizationSummaryTopClientsManufacturersByUsageSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getOrganizationSummaryTopDevicesByUsageSignalErrorFull() instead")
    void getOrganizationSummaryTopDevicesByUsageSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getOrganizationSummaryTopDevicesByUsageSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getOrganizationSummaryTopDevicesModelsByUsageSignalErrorFull() instead")
    void getOrganizationSummaryTopDevicesModelsByUsageSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getOrganizationSummaryTopDevicesModelsByUsageSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getOrganizationSummaryTopSsidsByUsageSignalErrorFull() instead")
    void getOrganizationSummaryTopSsidsByUsageSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getOrganizationSummaryTopSsidsByUsageSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getOrganizationSummaryTopSwitchesByEnergyUsageSignalErrorFull() instead")
    void getOrganizationSummaryTopSwitchesByEnergyUsageSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getOrganizationSummaryTopSwitchesByEnergyUsageSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
