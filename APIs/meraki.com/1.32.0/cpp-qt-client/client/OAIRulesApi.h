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

#ifndef OAI_OAIRulesApi_H
#define OAI_OAIRulesApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAIObject.h"
#include "OAIUpdateNetworkApplianceTrafficShapingRules_request.h"
#include "OAIUpdateNetworkWirelessSsidTrafficShapingRules_request.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAIRulesApi : public QObject {
    Q_OBJECT

public:
    OAIRulesApi(const int timeOut = 0);
    ~OAIRulesApi();

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
    virtual void getNetworkApplianceTrafficShapingRules(const QString &network_id);

    /**
    * @param[in]  network_id QString [required]
    * @param[in]  number QString [required]
    */
    virtual void getNetworkWirelessSsidTrafficShapingRules(const QString &network_id, const QString &number);

    /**
    * @param[in]  network_id QString [required]
    * @param[in]  oai_update_network_appliance_traffic_shaping_rules_request OAIUpdateNetworkApplianceTrafficShapingRules_request [optional]
    */
    virtual void updateNetworkApplianceTrafficShapingRules(const QString &network_id, const ::OpenAPI::OptionalParam<OAIUpdateNetworkApplianceTrafficShapingRules_request> &oai_update_network_appliance_traffic_shaping_rules_request = ::OpenAPI::OptionalParam<OAIUpdateNetworkApplianceTrafficShapingRules_request>());

    /**
    * @param[in]  network_id QString [required]
    * @param[in]  number QString [required]
    * @param[in]  oai_update_network_wireless_ssid_traffic_shaping_rules_request OAIUpdateNetworkWirelessSsidTrafficShapingRules_request [optional]
    */
    virtual void updateNetworkWirelessSsidTrafficShapingRules(const QString &network_id, const QString &number, const ::OpenAPI::OptionalParam<OAIUpdateNetworkWirelessSsidTrafficShapingRules_request> &oai_update_network_wireless_ssid_traffic_shaping_rules_request = ::OpenAPI::OptionalParam<OAIUpdateNetworkWirelessSsidTrafficShapingRules_request>());


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

    void getNetworkApplianceTrafficShapingRulesCallback(OAIHttpRequestWorker *worker);
    void getNetworkWirelessSsidTrafficShapingRulesCallback(OAIHttpRequestWorker *worker);
    void updateNetworkApplianceTrafficShapingRulesCallback(OAIHttpRequestWorker *worker);
    void updateNetworkWirelessSsidTrafficShapingRulesCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void getNetworkApplianceTrafficShapingRulesSignal(OAIObject summary);
    void getNetworkWirelessSsidTrafficShapingRulesSignal(OAIObject summary);
    void updateNetworkApplianceTrafficShapingRulesSignal(OAIObject summary);
    void updateNetworkWirelessSsidTrafficShapingRulesSignal(OAIObject summary);


    void getNetworkApplianceTrafficShapingRulesSignalFull(OAIHttpRequestWorker *worker, OAIObject summary);
    void getNetworkWirelessSsidTrafficShapingRulesSignalFull(OAIHttpRequestWorker *worker, OAIObject summary);
    void updateNetworkApplianceTrafficShapingRulesSignalFull(OAIHttpRequestWorker *worker, OAIObject summary);
    void updateNetworkWirelessSsidTrafficShapingRulesSignalFull(OAIHttpRequestWorker *worker, OAIObject summary);

    Q_DECL_DEPRECATED_X("Use getNetworkApplianceTrafficShapingRulesSignalError() instead")
    void getNetworkApplianceTrafficShapingRulesSignalE(OAIObject summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getNetworkApplianceTrafficShapingRulesSignalError(OAIObject summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getNetworkWirelessSsidTrafficShapingRulesSignalError() instead")
    void getNetworkWirelessSsidTrafficShapingRulesSignalE(OAIObject summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getNetworkWirelessSsidTrafficShapingRulesSignalError(OAIObject summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use updateNetworkApplianceTrafficShapingRulesSignalError() instead")
    void updateNetworkApplianceTrafficShapingRulesSignalE(OAIObject summary, QNetworkReply::NetworkError error_type, QString error_str);
    void updateNetworkApplianceTrafficShapingRulesSignalError(OAIObject summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use updateNetworkWirelessSsidTrafficShapingRulesSignalError() instead")
    void updateNetworkWirelessSsidTrafficShapingRulesSignalE(OAIObject summary, QNetworkReply::NetworkError error_type, QString error_str);
    void updateNetworkWirelessSsidTrafficShapingRulesSignalError(OAIObject summary, QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use getNetworkApplianceTrafficShapingRulesSignalErrorFull() instead")
    void getNetworkApplianceTrafficShapingRulesSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getNetworkApplianceTrafficShapingRulesSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getNetworkWirelessSsidTrafficShapingRulesSignalErrorFull() instead")
    void getNetworkWirelessSsidTrafficShapingRulesSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getNetworkWirelessSsidTrafficShapingRulesSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use updateNetworkApplianceTrafficShapingRulesSignalErrorFull() instead")
    void updateNetworkApplianceTrafficShapingRulesSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void updateNetworkApplianceTrafficShapingRulesSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use updateNetworkWirelessSsidTrafficShapingRulesSignalErrorFull() instead")
    void updateNetworkWirelessSsidTrafficShapingRulesSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void updateNetworkWirelessSsidTrafficShapingRulesSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
