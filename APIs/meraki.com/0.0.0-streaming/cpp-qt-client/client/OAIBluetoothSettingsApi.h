/**
 * Meraki Dashboard API
 * The Cisco Meraki Dashboard API is a modern REST API based on the OpenAPI specification.  > Date: 23 April, 2023 > > [Recent Updates](https://meraki.io/whats-new/)  ---  [API Documentation](https://meraki.io/api)  [Community Support](https://meraki.io/community)  [Meraki Homepage](https://www.meraki.com) 
 *
 * The version of the OpenAPI document: 0.0.0-streaming
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#ifndef OAI_OAIBluetoothSettingsApi_H
#define OAI_OAIBluetoothSettingsApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAIGetNetworkBluetoothSettings_200_response.h"
#include "OAIUpdateDeviceWirelessBluetoothSettings_200_response.h"
#include "OAIUpdateDeviceWirelessBluetoothSettings_request.h"
#include "OAIUpdateNetworkBluetoothSettings_request.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAIBluetoothSettingsApi : public QObject {
    Q_OBJECT

public:
    OAIBluetoothSettingsApi(const int timeOut = 0);
    ~OAIBluetoothSettingsApi();

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
    * @param[in]  network_id QString [required]
    */
    virtual void getNetworkBluetoothSettings(const QString &network_id);

    /**
    * @param[in]  serial QString [required]
    * @param[in]  oai_update_device_wireless_bluetooth_settings_request OAIUpdateDeviceWirelessBluetoothSettings_request [optional]
    */
    virtual void updateDeviceWirelessBluetoothSettings(const QString &serial, const ::OpenAPI::OptionalParam<OAIUpdateDeviceWirelessBluetoothSettings_request> &oai_update_device_wireless_bluetooth_settings_request = ::OpenAPI::OptionalParam<OAIUpdateDeviceWirelessBluetoothSettings_request>());

    /**
    * @param[in]  network_id QString [required]
    * @param[in]  oai_update_network_bluetooth_settings_request OAIUpdateNetworkBluetoothSettings_request [optional]
    */
    virtual void updateNetworkBluetoothSettings(const QString &network_id, const ::OpenAPI::OptionalParam<OAIUpdateNetworkBluetoothSettings_request> &oai_update_network_bluetooth_settings_request = ::OpenAPI::OptionalParam<OAIUpdateNetworkBluetoothSettings_request>());


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

    void getNetworkBluetoothSettingsCallback(OAIHttpRequestWorker *worker);
    void updateDeviceWirelessBluetoothSettingsCallback(OAIHttpRequestWorker *worker);
    void updateNetworkBluetoothSettingsCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void getNetworkBluetoothSettingsSignal(OAIGetNetworkBluetoothSettings_200_response summary);
    void updateDeviceWirelessBluetoothSettingsSignal(OAIUpdateDeviceWirelessBluetoothSettings_200_response summary);
    void updateNetworkBluetoothSettingsSignal(OAIGetNetworkBluetoothSettings_200_response summary);


    void getNetworkBluetoothSettingsSignalFull(OAIHttpRequestWorker *worker, OAIGetNetworkBluetoothSettings_200_response summary);
    void updateDeviceWirelessBluetoothSettingsSignalFull(OAIHttpRequestWorker *worker, OAIUpdateDeviceWirelessBluetoothSettings_200_response summary);
    void updateNetworkBluetoothSettingsSignalFull(OAIHttpRequestWorker *worker, OAIGetNetworkBluetoothSettings_200_response summary);

    Q_DECL_DEPRECATED_X("Use getNetworkBluetoothSettingsSignalError() instead")
    void getNetworkBluetoothSettingsSignalE(OAIGetNetworkBluetoothSettings_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getNetworkBluetoothSettingsSignalError(OAIGetNetworkBluetoothSettings_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use updateDeviceWirelessBluetoothSettingsSignalError() instead")
    void updateDeviceWirelessBluetoothSettingsSignalE(OAIUpdateDeviceWirelessBluetoothSettings_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void updateDeviceWirelessBluetoothSettingsSignalError(OAIUpdateDeviceWirelessBluetoothSettings_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use updateNetworkBluetoothSettingsSignalError() instead")
    void updateNetworkBluetoothSettingsSignalE(OAIGetNetworkBluetoothSettings_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void updateNetworkBluetoothSettingsSignalError(OAIGetNetworkBluetoothSettings_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use getNetworkBluetoothSettingsSignalErrorFull() instead")
    void getNetworkBluetoothSettingsSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getNetworkBluetoothSettingsSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use updateDeviceWirelessBluetoothSettingsSignalErrorFull() instead")
    void updateDeviceWirelessBluetoothSettingsSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void updateDeviceWirelessBluetoothSettingsSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use updateNetworkBluetoothSettingsSignalErrorFull() instead")
    void updateNetworkBluetoothSettingsSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void updateNetworkBluetoothSettingsSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
