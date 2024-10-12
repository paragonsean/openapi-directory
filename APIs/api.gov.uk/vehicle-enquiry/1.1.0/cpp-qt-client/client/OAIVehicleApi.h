/**
 * Vehicle Enquiry API
 * Interface specification for the DVLA Vehicle Enquiry API
 *
 * The version of the OpenAPI document: 1.1.0
 * Contact: DvlaAPIAccess@dvla.gov.uk
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#ifndef OAI_OAIVehicleApi_H
#define OAI_OAIVehicleApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAIErrorResponse.h"
#include "OAIVehicle.h"
#include "OAIVehicleRequest.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAIVehicleApi : public QObject {
    Q_OBJECT

public:
    OAIVehicleApi(const int timeOut = 0);
    ~OAIVehicleApi();

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
    * @param[in]  x_api_key QString [required]
    * @param[in]  oai_vehicle_request OAIVehicleRequest [required]
    * @param[in]  x_correlation_id QString [optional]
    */
    virtual void getVehicleDetailsByRegistrationNumber(const QString &x_api_key, const OAIVehicleRequest &oai_vehicle_request, const ::OpenAPI::OptionalParam<QString> &x_correlation_id = ::OpenAPI::OptionalParam<QString>());


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

    void getVehicleDetailsByRegistrationNumberCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void getVehicleDetailsByRegistrationNumberSignal(OAIVehicle summary);


    void getVehicleDetailsByRegistrationNumberSignalFull(OAIHttpRequestWorker *worker, OAIVehicle summary);

    Q_DECL_DEPRECATED_X("Use getVehicleDetailsByRegistrationNumberSignalError() instead")
    void getVehicleDetailsByRegistrationNumberSignalE(OAIVehicle summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getVehicleDetailsByRegistrationNumberSignalError(OAIVehicle summary, QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use getVehicleDetailsByRegistrationNumberSignalErrorFull() instead")
    void getVehicleDetailsByRegistrationNumberSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getVehicleDetailsByRegistrationNumberSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
