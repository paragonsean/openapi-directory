/**
 * Airport & City Search
 *  Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.   Please also be aware that our test environment is based on a subset of the production, in test this API only contains data from the United States, Spain, United Kingdom, Germany and India. 
 *
 * The version of the OpenAPI document: 1.2.3
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#ifndef OAI_OAILocationApi_H
#define OAI_OAILocationApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAIError_400.h"
#include "OAIError_404.h"
#include "OAIError_500.h"
#include "OAISuccess.h"
#include "OAISuccess_1.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAILocationApi : public QObject {
    Q_OBJECT

public:
    OAILocationApi(const int timeOut = 0);
    ~OAILocationApi();

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
    * @param[in]  location_id QString [required]
    */
    virtual void getAirportCity(const QString &location_id);

    /**
    * @param[in]  sub_type QList<QString> [required]
    * @param[in]  keyword QString [required]
    * @param[in]  country_code QString [optional]
    * @param[in]  page_limit qint32 [optional]
    * @param[in]  page_offset qint32 [optional]
    * @param[in]  sort QString [optional]
    * @param[in]  view QString [optional]
    */
    virtual void getAirportCitySearch(const QList<QString> &sub_type, const QString &keyword, const ::OpenAPI::OptionalParam<QString> &country_code = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<qint32> &page_limit = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &page_offset = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &sort = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &view = ::OpenAPI::OptionalParam<QString>());


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

    void getAirportCityCallback(OAIHttpRequestWorker *worker);
    void getAirportCitySearchCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void getAirportCitySignal(OAISuccess_1 summary);
    void getAirportCitySearchSignal(OAISuccess summary);


    void getAirportCitySignalFull(OAIHttpRequestWorker *worker, OAISuccess_1 summary);
    void getAirportCitySearchSignalFull(OAIHttpRequestWorker *worker, OAISuccess summary);

    Q_DECL_DEPRECATED_X("Use getAirportCitySignalError() instead")
    void getAirportCitySignalE(OAISuccess_1 summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getAirportCitySignalError(OAISuccess_1 summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getAirportCitySearchSignalError() instead")
    void getAirportCitySearchSignalE(OAISuccess summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getAirportCitySearchSignalError(OAISuccess summary, QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use getAirportCitySignalErrorFull() instead")
    void getAirportCitySignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getAirportCitySignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getAirportCitySearchSignalErrorFull() instead")
    void getAirportCitySearchSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getAirportCitySearchSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
