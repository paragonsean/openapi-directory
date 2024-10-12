/**
 * StorageManagementClient
 * The Admin Storage Management Client.
 *
 * The version of the OpenAPI document: 2015-12-01-preview
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#ifndef OAI_OAITableServicesApi_H
#define OAI_OAITableServicesApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAITableService.h"
#include "OAITableServices_ListMetricDefinitions_200_response.h"
#include "OAITableServices_ListMetrics_200_response.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAITableServicesApi : public QObject {
    Q_OBJECT

public:
    OAITableServicesApi(const int timeOut = 0);
    ~OAITableServicesApi();

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
    * @param[in]  farm_id QString [required]
    * @param[in]  service_type QString [required]
    * @param[in]  api_version QString [required]
    */
    virtual void tableServicesGet(const QString &subscription_id, const QString &resource_group_name, const QString &farm_id, const QString &service_type, const QString &api_version);

    /**
    * @param[in]  subscription_id QString [required]
    * @param[in]  resource_group_name QString [required]
    * @param[in]  farm_id QString [required]
    * @param[in]  service_type QString [required]
    * @param[in]  api_version QString [required]
    */
    virtual void tableServicesListMetricDefinitions(const QString &subscription_id, const QString &resource_group_name, const QString &farm_id, const QString &service_type, const QString &api_version);

    /**
    * @param[in]  subscription_id QString [required]
    * @param[in]  resource_group_name QString [required]
    * @param[in]  farm_id QString [required]
    * @param[in]  service_type QString [required]
    * @param[in]  api_version QString [required]
    */
    virtual void tableServicesListMetrics(const QString &subscription_id, const QString &resource_group_name, const QString &farm_id, const QString &service_type, const QString &api_version);


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

    void tableServicesGetCallback(OAIHttpRequestWorker *worker);
    void tableServicesListMetricDefinitionsCallback(OAIHttpRequestWorker *worker);
    void tableServicesListMetricsCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void tableServicesGetSignal(OAITableService summary);
    void tableServicesListMetricDefinitionsSignal(OAITableServices_ListMetricDefinitions_200_response summary);
    void tableServicesListMetricsSignal(OAITableServices_ListMetrics_200_response summary);


    void tableServicesGetSignalFull(OAIHttpRequestWorker *worker, OAITableService summary);
    void tableServicesListMetricDefinitionsSignalFull(OAIHttpRequestWorker *worker, OAITableServices_ListMetricDefinitions_200_response summary);
    void tableServicesListMetricsSignalFull(OAIHttpRequestWorker *worker, OAITableServices_ListMetrics_200_response summary);

    Q_DECL_DEPRECATED_X("Use tableServicesGetSignalError() instead")
    void tableServicesGetSignalE(OAITableService summary, QNetworkReply::NetworkError error_type, QString error_str);
    void tableServicesGetSignalError(OAITableService summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use tableServicesListMetricDefinitionsSignalError() instead")
    void tableServicesListMetricDefinitionsSignalE(OAITableServices_ListMetricDefinitions_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void tableServicesListMetricDefinitionsSignalError(OAITableServices_ListMetricDefinitions_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use tableServicesListMetricsSignalError() instead")
    void tableServicesListMetricsSignalE(OAITableServices_ListMetrics_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void tableServicesListMetricsSignalError(OAITableServices_ListMetrics_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use tableServicesGetSignalErrorFull() instead")
    void tableServicesGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void tableServicesGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use tableServicesListMetricDefinitionsSignalErrorFull() instead")
    void tableServicesListMetricDefinitionsSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void tableServicesListMetricDefinitionsSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use tableServicesListMetricsSignalErrorFull() instead")
    void tableServicesListMetricsSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void tableServicesListMetricsSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
