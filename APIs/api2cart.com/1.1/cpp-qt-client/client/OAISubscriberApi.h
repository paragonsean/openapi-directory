/**
 * Swagger API2Cart
 * API2Cart
 *
 * The version of the OpenAPI document: 1.1
 * Contact: contact@api2cart.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#ifndef OAI_OAISubscriberApi_H
#define OAI_OAISubscriberApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAISubscriberList_200_response.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAISubscriberApi : public QObject {
    Q_OBJECT

public:
    OAISubscriberApi(const int timeOut = 0);
    ~OAISubscriberApi();

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
    * @param[in]  start qint32 [optional]
    * @param[in]  count qint32 [optional]
    * @param[in]  subscribed bool [optional]
    * @param[in]  store_id QString [optional]
    * @param[in]  email QString [optional]
    * @param[in]  params QString [optional]
    * @param[in]  exclude QString [optional]
    * @param[in]  created_from QString [optional]
    * @param[in]  created_to QString [optional]
    * @param[in]  modified_from QString [optional]
    * @param[in]  modified_to QString [optional]
    * @param[in]  page_cursor QString [optional]
    * @param[in]  response_fields QString [optional]
    */
    virtual void subscriberList(const ::OpenAPI::OptionalParam<qint32> &start = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &count = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<bool> &subscribed = ::OpenAPI::OptionalParam<bool>(), const ::OpenAPI::OptionalParam<QString> &store_id = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &email = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &params = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &exclude = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &created_from = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &created_to = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &modified_from = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &modified_to = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &page_cursor = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &response_fields = ::OpenAPI::OptionalParam<QString>());


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

    void subscriberListCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void subscriberListSignal(OAISubscriberList_200_response summary);


    void subscriberListSignalFull(OAIHttpRequestWorker *worker, OAISubscriberList_200_response summary);

    Q_DECL_DEPRECATED_X("Use subscriberListSignalError() instead")
    void subscriberListSignalE(OAISubscriberList_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void subscriberListSignalError(OAISubscriberList_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use subscriberListSignalErrorFull() instead")
    void subscriberListSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void subscriberListSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
