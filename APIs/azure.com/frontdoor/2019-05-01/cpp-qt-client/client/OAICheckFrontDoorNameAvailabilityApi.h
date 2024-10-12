/**
 * FrontDoorManagementClient
 * Use these APIs to manage Azure Front Door resources through the Azure Resource Manager. You must make sure that requests made to these resources are secure.
 *
 * The version of the OpenAPI document: 2019-05-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#ifndef OAI_OAICheckFrontDoorNameAvailabilityApi_H
#define OAI_OAICheckFrontDoorNameAvailabilityApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAICheckNameAvailabilityInput.h"
#include "OAICheckNameAvailabilityOutput.h"
#include "OAIErrorResponse.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAICheckFrontDoorNameAvailabilityApi : public QObject {
    Q_OBJECT

public:
    OAICheckFrontDoorNameAvailabilityApi(const int timeOut = 0);
    ~OAICheckFrontDoorNameAvailabilityApi();

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
    * @param[in]  api_version QString [required]
    * @param[in]  check_front_door_name_availability_input OAICheckNameAvailabilityInput [required]
    */
    virtual void checkFrontDoorNameAvailability(const QString &api_version, const OAICheckNameAvailabilityInput &check_front_door_name_availability_input);


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

    void checkFrontDoorNameAvailabilityCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void checkFrontDoorNameAvailabilitySignal(OAICheckNameAvailabilityOutput summary);


    void checkFrontDoorNameAvailabilitySignalFull(OAIHttpRequestWorker *worker, OAICheckNameAvailabilityOutput summary);

    Q_DECL_DEPRECATED_X("Use checkFrontDoorNameAvailabilitySignalError() instead")
    void checkFrontDoorNameAvailabilitySignalE(OAICheckNameAvailabilityOutput summary, QNetworkReply::NetworkError error_type, QString error_str);
    void checkFrontDoorNameAvailabilitySignalError(OAICheckNameAvailabilityOutput summary, QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use checkFrontDoorNameAvailabilitySignalErrorFull() instead")
    void checkFrontDoorNameAvailabilitySignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void checkFrontDoorNameAvailabilitySignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
