/**
 * AGCO API
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: v1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#ifndef OAI_OAIAuthorizationContactInformationApi_H
#define OAI_OAIAuthorizationContactInformationApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAIAPI_IPagedResponse_AuthorizationCodes_Shared_Models_AuthorizationContactInformation_.h"
#include "OAIAPI_Models_ApiError.h"
#include "OAIAuthorizationCodes_Shared_Models_AuthorizationContactInformation.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAIAuthorizationContactInformationApi : public QObject {
    Q_OBJECT

public:
    OAIAuthorizationContactInformationApi(const int timeOut = 0);
    ~OAIAuthorizationContactInformationApi();

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
    * @param[in]  limit qint32 [optional]
    * @param[in]  offset qint32 [optional]
    * @param[in]  authorization_code QString [optional]
    * @param[in]  after_date QDateTime [optional]
    * @param[in]  before_date QDateTime [optional]
    * @param[in]  dealer_code QString [optional]
    */
    virtual void authorizationContactInformationGet(const ::OpenAPI::OptionalParam<qint32> &limit = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &offset = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &authorization_code = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QDateTime> &after_date = ::OpenAPI::OptionalParam<QDateTime>(), const ::OpenAPI::OptionalParam<QDateTime> &before_date = ::OpenAPI::OptionalParam<QDateTime>(), const ::OpenAPI::OptionalParam<QString> &dealer_code = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  oai_authorization_codes_shared_models_authorization_contact_information OAIAuthorizationCodes_Shared_Models_AuthorizationContactInformation [required]
    */
    virtual void authorizationContactInformationPost(const OAIAuthorizationCodes_Shared_Models_AuthorizationContactInformation &oai_authorization_codes_shared_models_authorization_contact_information);


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

    void authorizationContactInformationGetCallback(OAIHttpRequestWorker *worker);
    void authorizationContactInformationPostCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void authorizationContactInformationGetSignal(OAIAPI_IPagedResponse_AuthorizationCodes_Shared_Models_AuthorizationContactInformation_ summary);
    void authorizationContactInformationPostSignal(qint32 summary);


    void authorizationContactInformationGetSignalFull(OAIHttpRequestWorker *worker, OAIAPI_IPagedResponse_AuthorizationCodes_Shared_Models_AuthorizationContactInformation_ summary);
    void authorizationContactInformationPostSignalFull(OAIHttpRequestWorker *worker, qint32 summary);

    Q_DECL_DEPRECATED_X("Use authorizationContactInformationGetSignalError() instead")
    void authorizationContactInformationGetSignalE(OAIAPI_IPagedResponse_AuthorizationCodes_Shared_Models_AuthorizationContactInformation_ summary, QNetworkReply::NetworkError error_type, QString error_str);
    void authorizationContactInformationGetSignalError(OAIAPI_IPagedResponse_AuthorizationCodes_Shared_Models_AuthorizationContactInformation_ summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use authorizationContactInformationPostSignalError() instead")
    void authorizationContactInformationPostSignalE(qint32 summary, QNetworkReply::NetworkError error_type, QString error_str);
    void authorizationContactInformationPostSignalError(qint32 summary, QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use authorizationContactInformationGetSignalErrorFull() instead")
    void authorizationContactInformationGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void authorizationContactInformationGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use authorizationContactInformationPostSignalErrorFull() instead")
    void authorizationContactInformationPostSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void authorizationContactInformationPostSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
