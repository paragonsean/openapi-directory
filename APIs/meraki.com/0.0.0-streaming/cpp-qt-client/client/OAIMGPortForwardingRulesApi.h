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

#ifndef OAI_OAIMGPortForwardingRulesApi_H
#define OAI_OAIMGPortForwardingRulesApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAIObject.h"
#include "OAIUpdateDeviceCellularGatewaySettingsPortForwardingRules_request.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAIMGPortForwardingRulesApi : public QObject {
    Q_OBJECT

public:
    OAIMGPortForwardingRulesApi(const int timeOut = 0);
    ~OAIMGPortForwardingRulesApi();

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
    */
    virtual void getDeviceCellularGatewaySettingsPortForwardingRules(const QString &serial);

    /**
    * @param[in]  serial QString [required]
    * @param[in]  oai_update_device_cellular_gateway_settings_port_forwarding_rules_request OAIUpdateDeviceCellularGatewaySettingsPortForwardingRules_request [optional]
    */
    virtual void updateDeviceCellularGatewaySettingsPortForwardingRules(const QString &serial, const ::OpenAPI::OptionalParam<OAIUpdateDeviceCellularGatewaySettingsPortForwardingRules_request> &oai_update_device_cellular_gateway_settings_port_forwarding_rules_request = ::OpenAPI::OptionalParam<OAIUpdateDeviceCellularGatewaySettingsPortForwardingRules_request>());


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

    void getDeviceCellularGatewaySettingsPortForwardingRulesCallback(OAIHttpRequestWorker *worker);
    void updateDeviceCellularGatewaySettingsPortForwardingRulesCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void getDeviceCellularGatewaySettingsPortForwardingRulesSignal(OAIObject summary);
    void updateDeviceCellularGatewaySettingsPortForwardingRulesSignal(OAIObject summary);


    void getDeviceCellularGatewaySettingsPortForwardingRulesSignalFull(OAIHttpRequestWorker *worker, OAIObject summary);
    void updateDeviceCellularGatewaySettingsPortForwardingRulesSignalFull(OAIHttpRequestWorker *worker, OAIObject summary);

    Q_DECL_DEPRECATED_X("Use getDeviceCellularGatewaySettingsPortForwardingRulesSignalError() instead")
    void getDeviceCellularGatewaySettingsPortForwardingRulesSignalE(OAIObject summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getDeviceCellularGatewaySettingsPortForwardingRulesSignalError(OAIObject summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use updateDeviceCellularGatewaySettingsPortForwardingRulesSignalError() instead")
    void updateDeviceCellularGatewaySettingsPortForwardingRulesSignalE(OAIObject summary, QNetworkReply::NetworkError error_type, QString error_str);
    void updateDeviceCellularGatewaySettingsPortForwardingRulesSignalError(OAIObject summary, QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use getDeviceCellularGatewaySettingsPortForwardingRulesSignalErrorFull() instead")
    void getDeviceCellularGatewaySettingsPortForwardingRulesSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getDeviceCellularGatewaySettingsPortForwardingRulesSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use updateDeviceCellularGatewaySettingsPortForwardingRulesSignalErrorFull() instead")
    void updateDeviceCellularGatewaySettingsPortForwardingRulesSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void updateDeviceCellularGatewaySettingsPortForwardingRulesSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
