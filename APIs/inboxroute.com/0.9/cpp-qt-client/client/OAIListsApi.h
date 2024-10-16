/**
 * Mailsquad
 * MailSquad offers an affordable and super easy way to create, send and track delightful emails.
 *
 * The version of the OpenAPI document: 0.9
 * Contact: support@mailsquad.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#ifndef OAI_OAIListsApi_H
#define OAI_OAIListsApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAIContactListPage.h"
#include "OAIContactListUpdate.h"
#include "OAINewId.h"
#include "OAI_contacts_get_401_response_inner.h"
#include "OAI_contacts_get_404_response_inner.h"
#include "OAI_contacts_get_422_response_inner.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAIListsApi : public QObject {
    Q_OBJECT

public:
    OAIListsApi(const int timeOut = 0);
    ~OAIListsApi();

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
    * @param[in]  offset qint32 [optional]
    * @param[in]  limit qint32 [optional]
    * @param[in]  sort QString [optional]
    */
    virtual void contactsListsGet(const ::OpenAPI::OptionalParam<qint32> &offset = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &limit = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<QString> &sort = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  listid QString [required]
    */
    virtual void contactsListsListidDelete(const QString &listid);

    /**
    * @param[in]  listid QString [required]
    * @param[in]  contactlist OAIContactListUpdate [optional]
    */
    virtual void contactsListsListidPut(const QString &listid, const ::OpenAPI::OptionalParam<OAIContactListUpdate> &contactlist = ::OpenAPI::OptionalParam<OAIContactListUpdate>());

    /**
    * @param[in]  contactlist OAIContactListUpdate [optional]
    */
    virtual void contactsListsPost(const ::OpenAPI::OptionalParam<OAIContactListUpdate> &contactlist = ::OpenAPI::OptionalParam<OAIContactListUpdate>());


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

    void contactsListsGetCallback(OAIHttpRequestWorker *worker);
    void contactsListsListidDeleteCallback(OAIHttpRequestWorker *worker);
    void contactsListsListidPutCallback(OAIHttpRequestWorker *worker);
    void contactsListsPostCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void contactsListsGetSignal(OAIContactListPage summary);
    void contactsListsListidDeleteSignal();
    void contactsListsListidPutSignal();
    void contactsListsPostSignal(OAINewId summary);


    void contactsListsGetSignalFull(OAIHttpRequestWorker *worker, OAIContactListPage summary);
    void contactsListsListidDeleteSignalFull(OAIHttpRequestWorker *worker);
    void contactsListsListidPutSignalFull(OAIHttpRequestWorker *worker);
    void contactsListsPostSignalFull(OAIHttpRequestWorker *worker, OAINewId summary);

    Q_DECL_DEPRECATED_X("Use contactsListsGetSignalError() instead")
    void contactsListsGetSignalE(OAIContactListPage summary, QNetworkReply::NetworkError error_type, QString error_str);
    void contactsListsGetSignalError(OAIContactListPage summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use contactsListsListidDeleteSignalError() instead")
    void contactsListsListidDeleteSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void contactsListsListidDeleteSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use contactsListsListidPutSignalError() instead")
    void contactsListsListidPutSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void contactsListsListidPutSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use contactsListsPostSignalError() instead")
    void contactsListsPostSignalE(OAINewId summary, QNetworkReply::NetworkError error_type, QString error_str);
    void contactsListsPostSignalError(OAINewId summary, QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use contactsListsGetSignalErrorFull() instead")
    void contactsListsGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void contactsListsGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use contactsListsListidDeleteSignalErrorFull() instead")
    void contactsListsListidDeleteSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void contactsListsListidDeleteSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use contactsListsListidPutSignalErrorFull() instead")
    void contactsListsListidPutSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void contactsListsListidPutSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use contactsListsPostSignalErrorFull() instead")
    void contactsListsPostSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void contactsListsPostSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
