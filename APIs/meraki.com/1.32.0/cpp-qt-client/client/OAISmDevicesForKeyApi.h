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

#ifndef OAI_OAISmDevicesForKeyApi_H
#define OAI_OAISmDevicesForKeyApi_H

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

class OAISmDevicesForKeyApi : public QObject {
    Q_OBJECT

public:
    OAISmDevicesForKeyApi(const int timeOut = 0);
    ~OAISmDevicesForKeyApi();

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
    * @param[in]  username QString [optional]
    * @param[in]  email QString [optional]
    * @param[in]  mac QString [optional]
    * @param[in]  serial QString [optional]
    * @param[in]  imei QString [optional]
    * @param[in]  bluetooth_mac QString [optional]
    */
    virtual void getNetworkPiiSmDevicesForKey(const QString &network_id, const ::OpenAPI::OptionalParam<QString> &username = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &email = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &mac = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &serial = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &imei = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &bluetooth_mac = ::OpenAPI::OptionalParam<QString>());


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

    void getNetworkPiiSmDevicesForKeyCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void getNetworkPiiSmDevicesForKeySignal(OAIObject summary);


    void getNetworkPiiSmDevicesForKeySignalFull(OAIHttpRequestWorker *worker, OAIObject summary);

    Q_DECL_DEPRECATED_X("Use getNetworkPiiSmDevicesForKeySignalError() instead")
    void getNetworkPiiSmDevicesForKeySignalE(OAIObject summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getNetworkPiiSmDevicesForKeySignalError(OAIObject summary, QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use getNetworkPiiSmDevicesForKeySignalErrorFull() instead")
    void getNetworkPiiSmDevicesForKeySignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getNetworkPiiSmDevicesForKeySignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
