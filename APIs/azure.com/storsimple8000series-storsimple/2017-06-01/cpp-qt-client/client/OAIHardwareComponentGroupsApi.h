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

#ifndef OAI_OAIHardwareComponentGroupsApi_H
#define OAI_OAIHardwareComponentGroupsApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAIControllerPowerStateChangeRequest.h"
#include "OAIHardwareComponentGroupList.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAIHardwareComponentGroupsApi : public QObject {
    Q_OBJECT

public:
    OAIHardwareComponentGroupsApi(const int timeOut = 0);
    ~OAIHardwareComponentGroupsApi();

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
    * @param[in]  hardware_component_group_name QString [required]
    * @param[in]  subscription_id QString [required]
    * @param[in]  resource_group_name QString [required]
    * @param[in]  manager_name QString [required]
    * @param[in]  api_version QString [required]
    * @param[in]  parameters OAIControllerPowerStateChangeRequest [required]
    */
    virtual void hardwareComponentGroupsChangeControllerPowerState(const QString &device_name, const QString &hardware_component_group_name, const QString &subscription_id, const QString &resource_group_name, const QString &manager_name, const QString &api_version, const OAIControllerPowerStateChangeRequest &parameters);

    /**
    * @param[in]  device_name QString [required]
    * @param[in]  subscription_id QString [required]
    * @param[in]  resource_group_name QString [required]
    * @param[in]  manager_name QString [required]
    * @param[in]  api_version QString [required]
    */
    virtual void hardwareComponentGroupsListByDevice(const QString &device_name, const QString &subscription_id, const QString &resource_group_name, const QString &manager_name, const QString &api_version);


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

    void hardwareComponentGroupsChangeControllerPowerStateCallback(OAIHttpRequestWorker *worker);
    void hardwareComponentGroupsListByDeviceCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void hardwareComponentGroupsChangeControllerPowerStateSignal();
    void hardwareComponentGroupsListByDeviceSignal(OAIHardwareComponentGroupList summary);


    void hardwareComponentGroupsChangeControllerPowerStateSignalFull(OAIHttpRequestWorker *worker);
    void hardwareComponentGroupsListByDeviceSignalFull(OAIHttpRequestWorker *worker, OAIHardwareComponentGroupList summary);

    Q_DECL_DEPRECATED_X("Use hardwareComponentGroupsChangeControllerPowerStateSignalError() instead")
    void hardwareComponentGroupsChangeControllerPowerStateSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void hardwareComponentGroupsChangeControllerPowerStateSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use hardwareComponentGroupsListByDeviceSignalError() instead")
    void hardwareComponentGroupsListByDeviceSignalE(OAIHardwareComponentGroupList summary, QNetworkReply::NetworkError error_type, QString error_str);
    void hardwareComponentGroupsListByDeviceSignalError(OAIHardwareComponentGroupList summary, QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use hardwareComponentGroupsChangeControllerPowerStateSignalErrorFull() instead")
    void hardwareComponentGroupsChangeControllerPowerStateSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void hardwareComponentGroupsChangeControllerPowerStateSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use hardwareComponentGroupsListByDeviceSignalErrorFull() instead")
    void hardwareComponentGroupsListByDeviceSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void hardwareComponentGroupsListByDeviceSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
