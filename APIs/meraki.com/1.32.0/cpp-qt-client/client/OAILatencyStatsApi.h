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

#ifndef OAI_OAILatencyStatsApi_H
#define OAI_OAILatencyStatsApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAIObject.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAILatencyStatsApi : public QObject {
    Q_OBJECT

public:
    OAILatencyStatsApi(const int timeOut = 0);
    ~OAILatencyStatsApi();

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
    * @param[in]  serial QString [required]
    * @param[in]  t0 QString [optional]
    * @param[in]  t1 QString [optional]
    * @param[in]  timespan float [optional]
    * @param[in]  band QString [optional]
    * @param[in]  ssid qint32 [optional]
    * @param[in]  vlan qint32 [optional]
    * @param[in]  ap_tag QString [optional]
    * @param[in]  fields QString [optional]
    */
    virtual void getDeviceWirelessLatencyStats(const QString &serial, const ::OpenAPI::OptionalParam<QString> &t0 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &t1 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<float> &timespan = ::OpenAPI::OptionalParam<float>(), const ::OpenAPI::OptionalParam<QString> &band = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &ssid = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &vlan = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &ap_tag = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &fields = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  network_id QString [required]
    * @param[in]  client_id QString [required]
    * @param[in]  t0 QString [optional]
    * @param[in]  t1 QString [optional]
    * @param[in]  timespan float [optional]
    * @param[in]  band QString [optional]
    * @param[in]  ssid qint32 [optional]
    * @param[in]  vlan qint32 [optional]
    * @param[in]  ap_tag QString [optional]
    * @param[in]  fields QString [optional]
    */
    virtual void getNetworkWirelessClientLatencyStats(const QString &network_id, const QString &client_id, const ::OpenAPI::OptionalParam<QString> &t0 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &t1 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<float> &timespan = ::OpenAPI::OptionalParam<float>(), const ::OpenAPI::OptionalParam<QString> &band = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &ssid = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &vlan = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &ap_tag = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &fields = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  network_id QString [required]
    * @param[in]  t0 QString [optional]
    * @param[in]  t1 QString [optional]
    * @param[in]  timespan float [optional]
    * @param[in]  band QString [optional]
    * @param[in]  ssid qint32 [optional]
    * @param[in]  vlan qint32 [optional]
    * @param[in]  ap_tag QString [optional]
    * @param[in]  fields QString [optional]
    */
    virtual void getNetworkWirelessClientsLatencyStats(const QString &network_id, const ::OpenAPI::OptionalParam<QString> &t0 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &t1 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<float> &timespan = ::OpenAPI::OptionalParam<float>(), const ::OpenAPI::OptionalParam<QString> &band = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &ssid = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &vlan = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &ap_tag = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &fields = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  network_id QString [required]
    * @param[in]  t0 QString [optional]
    * @param[in]  t1 QString [optional]
    * @param[in]  timespan float [optional]
    * @param[in]  band QString [optional]
    * @param[in]  ssid qint32 [optional]
    * @param[in]  vlan qint32 [optional]
    * @param[in]  ap_tag QString [optional]
    * @param[in]  fields QString [optional]
    */
    virtual void getNetworkWirelessDevicesLatencyStats(const QString &network_id, const ::OpenAPI::OptionalParam<QString> &t0 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &t1 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<float> &timespan = ::OpenAPI::OptionalParam<float>(), const ::OpenAPI::OptionalParam<QString> &band = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &ssid = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &vlan = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &ap_tag = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &fields = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  network_id QString [required]
    * @param[in]  t0 QString [optional]
    * @param[in]  t1 QString [optional]
    * @param[in]  timespan float [optional]
    * @param[in]  band QString [optional]
    * @param[in]  ssid qint32 [optional]
    * @param[in]  vlan qint32 [optional]
    * @param[in]  ap_tag QString [optional]
    * @param[in]  fields QString [optional]
    */
    virtual void getNetworkWirelessLatencyStats(const QString &network_id, const ::OpenAPI::OptionalParam<QString> &t0 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &t1 = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<float> &timespan = ::OpenAPI::OptionalParam<float>(), const ::OpenAPI::OptionalParam<QString> &band = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &ssid = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &vlan = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &ap_tag = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &fields = ::OpenAPI::OptionalParam<QString>());


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

    void getDeviceWirelessLatencyStatsCallback(OAIHttpRequestWorker *worker);
    void getNetworkWirelessClientLatencyStatsCallback(OAIHttpRequestWorker *worker);
    void getNetworkWirelessClientsLatencyStatsCallback(OAIHttpRequestWorker *worker);
    void getNetworkWirelessDevicesLatencyStatsCallback(OAIHttpRequestWorker *worker);
    void getNetworkWirelessLatencyStatsCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void getDeviceWirelessLatencyStatsSignal(OAIObject summary);
    void getNetworkWirelessClientLatencyStatsSignal(OAIObject summary);
    void getNetworkWirelessClientsLatencyStatsSignal(QList<OAIObject> summary);
    void getNetworkWirelessDevicesLatencyStatsSignal(QList<OAIObject> summary);
    void getNetworkWirelessLatencyStatsSignal(OAIObject summary);


    void getDeviceWirelessLatencyStatsSignalFull(OAIHttpRequestWorker *worker, OAIObject summary);
    void getNetworkWirelessClientLatencyStatsSignalFull(OAIHttpRequestWorker *worker, OAIObject summary);
    void getNetworkWirelessClientsLatencyStatsSignalFull(OAIHttpRequestWorker *worker, QList<OAIObject> summary);
    void getNetworkWirelessDevicesLatencyStatsSignalFull(OAIHttpRequestWorker *worker, QList<OAIObject> summary);
    void getNetworkWirelessLatencyStatsSignalFull(OAIHttpRequestWorker *worker, OAIObject summary);

    Q_DECL_DEPRECATED_X("Use getDeviceWirelessLatencyStatsSignalError() instead")
    void getDeviceWirelessLatencyStatsSignalE(OAIObject summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getDeviceWirelessLatencyStatsSignalError(OAIObject summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getNetworkWirelessClientLatencyStatsSignalError() instead")
    void getNetworkWirelessClientLatencyStatsSignalE(OAIObject summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getNetworkWirelessClientLatencyStatsSignalError(OAIObject summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getNetworkWirelessClientsLatencyStatsSignalError() instead")
    void getNetworkWirelessClientsLatencyStatsSignalE(QList<OAIObject> summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getNetworkWirelessClientsLatencyStatsSignalError(QList<OAIObject> summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getNetworkWirelessDevicesLatencyStatsSignalError() instead")
    void getNetworkWirelessDevicesLatencyStatsSignalE(QList<OAIObject> summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getNetworkWirelessDevicesLatencyStatsSignalError(QList<OAIObject> summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getNetworkWirelessLatencyStatsSignalError() instead")
    void getNetworkWirelessLatencyStatsSignalE(OAIObject summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getNetworkWirelessLatencyStatsSignalError(OAIObject summary, QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use getDeviceWirelessLatencyStatsSignalErrorFull() instead")
    void getDeviceWirelessLatencyStatsSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getDeviceWirelessLatencyStatsSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getNetworkWirelessClientLatencyStatsSignalErrorFull() instead")
    void getNetworkWirelessClientLatencyStatsSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getNetworkWirelessClientLatencyStatsSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getNetworkWirelessClientsLatencyStatsSignalErrorFull() instead")
    void getNetworkWirelessClientsLatencyStatsSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getNetworkWirelessClientsLatencyStatsSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getNetworkWirelessDevicesLatencyStatsSignalErrorFull() instead")
    void getNetworkWirelessDevicesLatencyStatsSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getNetworkWirelessDevicesLatencyStatsSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getNetworkWirelessLatencyStatsSignalErrorFull() instead")
    void getNetworkWirelessLatencyStatsSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getNetworkWirelessLatencyStatsSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
