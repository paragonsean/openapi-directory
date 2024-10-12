/**
 * StorSimple8000SeriesManagementClient
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2017-06-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#ifndef OAI_OAIVolumeContainersApi_H
#define OAI_OAIVolumeContainersApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAIMetricDefinitionList.h"
#include "OAIMetricList.h"
#include "OAIVolumeContainer.h"
#include "OAIVolumeContainerList.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAIVolumeContainersApi : public QObject {
    Q_OBJECT

public:
    OAIVolumeContainersApi(const int timeOut = 0);
    ~OAIVolumeContainersApi();

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
    * @param[in]  device_name QString [required]
    * @param[in]  volume_container_name QString [required]
    * @param[in]  subscription_id QString [required]
    * @param[in]  resource_group_name QString [required]
    * @param[in]  manager_name QString [required]
    * @param[in]  api_version QString [required]
    * @param[in]  parameters OAIVolumeContainer [required]
    */
    virtual void volumeContainersCreateOrUpdate(const QString &device_name, const QString &volume_container_name, const QString &subscription_id, const QString &resource_group_name, const QString &manager_name, const QString &api_version, const OAIVolumeContainer &parameters);

    /**
    * @param[in]  device_name QString [required]
    * @param[in]  volume_container_name QString [required]
    * @param[in]  subscription_id QString [required]
    * @param[in]  resource_group_name QString [required]
    * @param[in]  manager_name QString [required]
    * @param[in]  api_version QString [required]
    */
    virtual void volumeContainersDelete(const QString &device_name, const QString &volume_container_name, const QString &subscription_id, const QString &resource_group_name, const QString &manager_name, const QString &api_version);

    /**
    * @param[in]  device_name QString [required]
    * @param[in]  volume_container_name QString [required]
    * @param[in]  subscription_id QString [required]
    * @param[in]  resource_group_name QString [required]
    * @param[in]  manager_name QString [required]
    * @param[in]  api_version QString [required]
    */
    virtual void volumeContainersGet(const QString &device_name, const QString &volume_container_name, const QString &subscription_id, const QString &resource_group_name, const QString &manager_name, const QString &api_version);

    /**
    * @param[in]  device_name QString [required]
    * @param[in]  subscription_id QString [required]
    * @param[in]  resource_group_name QString [required]
    * @param[in]  manager_name QString [required]
    * @param[in]  api_version QString [required]
    */
    virtual void volumeContainersListByDevice(const QString &device_name, const QString &subscription_id, const QString &resource_group_name, const QString &manager_name, const QString &api_version);

    /**
    * @param[in]  device_name QString [required]
    * @param[in]  volume_container_name QString [required]
    * @param[in]  subscription_id QString [required]
    * @param[in]  resource_group_name QString [required]
    * @param[in]  manager_name QString [required]
    * @param[in]  api_version QString [required]
    */
    virtual void volumeContainersListMetricDefinition(const QString &device_name, const QString &volume_container_name, const QString &subscription_id, const QString &resource_group_name, const QString &manager_name, const QString &api_version);

    /**
    * @param[in]  device_name QString [required]
    * @param[in]  volume_container_name QString [required]
    * @param[in]  subscription_id QString [required]
    * @param[in]  resource_group_name QString [required]
    * @param[in]  manager_name QString [required]
    * @param[in]  api_version QString [required]
    * @param[in]  filter QString [required]
    */
    virtual void volumeContainersListMetrics(const QString &device_name, const QString &volume_container_name, const QString &subscription_id, const QString &resource_group_name, const QString &manager_name, const QString &api_version, const QString &filter);


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

    void volumeContainersCreateOrUpdateCallback(OAIHttpRequestWorker *worker);
    void volumeContainersDeleteCallback(OAIHttpRequestWorker *worker);
    void volumeContainersGetCallback(OAIHttpRequestWorker *worker);
    void volumeContainersListByDeviceCallback(OAIHttpRequestWorker *worker);
    void volumeContainersListMetricDefinitionCallback(OAIHttpRequestWorker *worker);
    void volumeContainersListMetricsCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void volumeContainersCreateOrUpdateSignal(OAIVolumeContainer summary);
    void volumeContainersDeleteSignal();
    void volumeContainersGetSignal(OAIVolumeContainer summary);
    void volumeContainersListByDeviceSignal(OAIVolumeContainerList summary);
    void volumeContainersListMetricDefinitionSignal(OAIMetricDefinitionList summary);
    void volumeContainersListMetricsSignal(OAIMetricList summary);


    void volumeContainersCreateOrUpdateSignalFull(OAIHttpRequestWorker *worker, OAIVolumeContainer summary);
    void volumeContainersDeleteSignalFull(OAIHttpRequestWorker *worker);
    void volumeContainersGetSignalFull(OAIHttpRequestWorker *worker, OAIVolumeContainer summary);
    void volumeContainersListByDeviceSignalFull(OAIHttpRequestWorker *worker, OAIVolumeContainerList summary);
    void volumeContainersListMetricDefinitionSignalFull(OAIHttpRequestWorker *worker, OAIMetricDefinitionList summary);
    void volumeContainersListMetricsSignalFull(OAIHttpRequestWorker *worker, OAIMetricList summary);

    Q_DECL_DEPRECATED_X("Use volumeContainersCreateOrUpdateSignalError() instead")
    void volumeContainersCreateOrUpdateSignalE(OAIVolumeContainer summary, QNetworkReply::NetworkError error_type, QString error_str);
    void volumeContainersCreateOrUpdateSignalError(OAIVolumeContainer summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use volumeContainersDeleteSignalError() instead")
    void volumeContainersDeleteSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void volumeContainersDeleteSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use volumeContainersGetSignalError() instead")
    void volumeContainersGetSignalE(OAIVolumeContainer summary, QNetworkReply::NetworkError error_type, QString error_str);
    void volumeContainersGetSignalError(OAIVolumeContainer summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use volumeContainersListByDeviceSignalError() instead")
    void volumeContainersListByDeviceSignalE(OAIVolumeContainerList summary, QNetworkReply::NetworkError error_type, QString error_str);
    void volumeContainersListByDeviceSignalError(OAIVolumeContainerList summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use volumeContainersListMetricDefinitionSignalError() instead")
    void volumeContainersListMetricDefinitionSignalE(OAIMetricDefinitionList summary, QNetworkReply::NetworkError error_type, QString error_str);
    void volumeContainersListMetricDefinitionSignalError(OAIMetricDefinitionList summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use volumeContainersListMetricsSignalError() instead")
    void volumeContainersListMetricsSignalE(OAIMetricList summary, QNetworkReply::NetworkError error_type, QString error_str);
    void volumeContainersListMetricsSignalError(OAIMetricList summary, QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use volumeContainersCreateOrUpdateSignalErrorFull() instead")
    void volumeContainersCreateOrUpdateSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void volumeContainersCreateOrUpdateSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use volumeContainersDeleteSignalErrorFull() instead")
    void volumeContainersDeleteSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void volumeContainersDeleteSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use volumeContainersGetSignalErrorFull() instead")
    void volumeContainersGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void volumeContainersGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use volumeContainersListByDeviceSignalErrorFull() instead")
    void volumeContainersListByDeviceSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void volumeContainersListByDeviceSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use volumeContainersListMetricDefinitionSignalErrorFull() instead")
    void volumeContainersListMetricDefinitionSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void volumeContainersListMetricDefinitionSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use volumeContainersListMetricsSignalErrorFull() instead")
    void volumeContainersListMetricsSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void volumeContainersListMetricsSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
