/**
 * Health ID Service
 * It is important to standardize the process of identification of an individual across healthcare providers, to ensure that the created medical records are issued to the right individual or accessed by a Health Information User through appropriate consent.  In order to issue a Health ID to an individual, one only needs basic demographic details like Name, Year of Birth, Gender. In addition, citizens should be able to update contact information easily.
 *
 * The version of the OpenAPI document: 1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#ifndef OAI_OAISearchApi_H
#define OAI_OAISearchApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAIObject.h"
#include "OAISearchByHealthIdRequest.h"
#include "OAISearchByMobileRequest.h"
#include "OAISearchResponseSingle.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAISearchApi : public QObject {
    Q_OBJECT

public:
    OAISearchApi(const int timeOut = 0);
    ~OAISearchApi();

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
    * @param[in]  search_request OAISearchByHealthIdRequest [required]
    * @param[in]  accept_language QString [optional]
    */
    virtual void searchUserByAccountUsingPOST(const OAISearchByHealthIdRequest &search_request, const ::OpenAPI::OptionalParam<QString> &accept_language = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  search_request OAISearchByMobileRequest [required]
    * @param[in]  accept_language QString [optional]
    */
    virtual void searchUserByMobileUsingPOST(const OAISearchByMobileRequest &search_request, const ::OpenAPI::OptionalParam<QString> &accept_language = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  search_dto OAISearchByHealthIdRequest [required]
    * @param[in]  accept_language QString [optional]
    */
    virtual void searchUserByUseridUsingPOST(const OAISearchByHealthIdRequest &search_dto, const ::OpenAPI::OptionalParam<QString> &accept_language = ::OpenAPI::OptionalParam<QString>());


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

    void searchUserByAccountUsingPOSTCallback(OAIHttpRequestWorker *worker);
    void searchUserByMobileUsingPOSTCallback(OAIHttpRequestWorker *worker);
    void searchUserByUseridUsingPOSTCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void searchUserByAccountUsingPOSTSignal(OAISearchResponseSingle summary);
    void searchUserByMobileUsingPOSTSignal(OAISearchResponseSingle summary);
    void searchUserByUseridUsingPOSTSignal(OAIObject summary);


    void searchUserByAccountUsingPOSTSignalFull(OAIHttpRequestWorker *worker, OAISearchResponseSingle summary);
    void searchUserByMobileUsingPOSTSignalFull(OAIHttpRequestWorker *worker, OAISearchResponseSingle summary);
    void searchUserByUseridUsingPOSTSignalFull(OAIHttpRequestWorker *worker, OAIObject summary);

    Q_DECL_DEPRECATED_X("Use searchUserByAccountUsingPOSTSignalError() instead")
    void searchUserByAccountUsingPOSTSignalE(OAISearchResponseSingle summary, QNetworkReply::NetworkError error_type, QString error_str);
    void searchUserByAccountUsingPOSTSignalError(OAISearchResponseSingle summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use searchUserByMobileUsingPOSTSignalError() instead")
    void searchUserByMobileUsingPOSTSignalE(OAISearchResponseSingle summary, QNetworkReply::NetworkError error_type, QString error_str);
    void searchUserByMobileUsingPOSTSignalError(OAISearchResponseSingle summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use searchUserByUseridUsingPOSTSignalError() instead")
    void searchUserByUseridUsingPOSTSignalE(OAIObject summary, QNetworkReply::NetworkError error_type, QString error_str);
    void searchUserByUseridUsingPOSTSignalError(OAIObject summary, QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use searchUserByAccountUsingPOSTSignalErrorFull() instead")
    void searchUserByAccountUsingPOSTSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void searchUserByAccountUsingPOSTSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use searchUserByMobileUsingPOSTSignalErrorFull() instead")
    void searchUserByMobileUsingPOSTSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void searchUserByMobileUsingPOSTSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use searchUserByUseridUsingPOSTSignalErrorFull() instead")
    void searchUserByUseridUsingPOSTSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void searchUserByUseridUsingPOSTSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
