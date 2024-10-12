/**
 * WeGA API
 * ⚠️<b>DEPRECATION WARNING</b>⚠️<br/>This version of the WeGA API specification is outdated and superseded by [version 1.1.0](https://weber-gesamtausgabe.de/api/v1/openapi.json).  <br/> <br/> For feedback or requests about this API please contact stadler@weber-gesamtausgabe.de or start the discussion at https://github.com/Edirom/WeGA-WebApp
 *
 * The version of the OpenAPI document: 1.0.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#ifndef OAI_OAIDocumentsApi_H
#define OAI_OAIDocumentsApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAIDocument.h"
#include "OAIError.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAIDocumentsApi : public QObject {
    Q_OBJECT

public:
    OAIDocumentsApi(const int timeOut = 0);
    ~OAIDocumentsApi();

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
    * @param[in]  doc_id QString [required]
    */
    virtual void documentsDocIDGet(const QString &doc_id);

    /**
    * @param[in]  author_id QString [required]
    * @param[in]  doc_type QList<QString> [optional]
    * @param[in]  offset qint32 [optional]
    * @param[in]  limit qint32 [optional]
    */
    virtual void documentsFindByAuthorAuthorIDGet(const QString &author_id, const ::OpenAPI::OptionalParam<QList<QString>> &doc_type = ::OpenAPI::OptionalParam<QList<QString>>(), const ::OpenAPI::OptionalParam<qint32> &offset = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &limit = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  from_date QDate [required]
    * @param[in]  to_date QDate [optional]
    * @param[in]  doc_type QList<QString> [optional]
    * @param[in]  offset qint32 [optional]
    * @param[in]  limit qint32 [optional]
    */
    virtual void documentsFindByDateGet(const QDate &from_date, const ::OpenAPI::OptionalParam<QDate> &to_date = ::OpenAPI::OptionalParam<QDate>(), const ::OpenAPI::OptionalParam<QList<QString>> &doc_type = ::OpenAPI::OptionalParam<QList<QString>>(), const ::OpenAPI::OptionalParam<qint32> &offset = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &limit = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  doc_id QString [required]
    * @param[in]  doc_type QList<QString> [optional]
    * @param[in]  offset qint32 [optional]
    * @param[in]  limit qint32 [optional]
    */
    virtual void documentsFindByMentionDocIDGet(const QString &doc_id, const ::OpenAPI::OptionalParam<QList<QString>> &doc_type = ::OpenAPI::OptionalParam<QList<QString>>(), const ::OpenAPI::OptionalParam<qint32> &offset = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &limit = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  doc_type QList<QString> [optional]
    * @param[in]  offset qint32 [optional]
    * @param[in]  limit qint32 [optional]
    */
    virtual void documentsGet(const ::OpenAPI::OptionalParam<QList<QString>> &doc_type = ::OpenAPI::OptionalParam<QList<QString>>(), const ::OpenAPI::OptionalParam<qint32> &offset = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &limit = ::OpenAPI::OptionalParam<qint32>());


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

    void documentsDocIDGetCallback(OAIHttpRequestWorker *worker);
    void documentsFindByAuthorAuthorIDGetCallback(OAIHttpRequestWorker *worker);
    void documentsFindByDateGetCallback(OAIHttpRequestWorker *worker);
    void documentsFindByMentionDocIDGetCallback(OAIHttpRequestWorker *worker);
    void documentsGetCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void documentsDocIDGetSignal(QList<OAIDocument> summary);
    void documentsFindByAuthorAuthorIDGetSignal(QList<OAIDocument> summary);
    void documentsFindByDateGetSignal(QList<OAIDocument> summary);
    void documentsFindByMentionDocIDGetSignal(QList<OAIDocument> summary);
    void documentsGetSignal(QList<OAIDocument> summary);


    void documentsDocIDGetSignalFull(OAIHttpRequestWorker *worker, QList<OAIDocument> summary);
    void documentsFindByAuthorAuthorIDGetSignalFull(OAIHttpRequestWorker *worker, QList<OAIDocument> summary);
    void documentsFindByDateGetSignalFull(OAIHttpRequestWorker *worker, QList<OAIDocument> summary);
    void documentsFindByMentionDocIDGetSignalFull(OAIHttpRequestWorker *worker, QList<OAIDocument> summary);
    void documentsGetSignalFull(OAIHttpRequestWorker *worker, QList<OAIDocument> summary);

    Q_DECL_DEPRECATED_X("Use documentsDocIDGetSignalError() instead")
    void documentsDocIDGetSignalE(QList<OAIDocument> summary, QNetworkReply::NetworkError error_type, QString error_str);
    void documentsDocIDGetSignalError(QList<OAIDocument> summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use documentsFindByAuthorAuthorIDGetSignalError() instead")
    void documentsFindByAuthorAuthorIDGetSignalE(QList<OAIDocument> summary, QNetworkReply::NetworkError error_type, QString error_str);
    void documentsFindByAuthorAuthorIDGetSignalError(QList<OAIDocument> summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use documentsFindByDateGetSignalError() instead")
    void documentsFindByDateGetSignalE(QList<OAIDocument> summary, QNetworkReply::NetworkError error_type, QString error_str);
    void documentsFindByDateGetSignalError(QList<OAIDocument> summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use documentsFindByMentionDocIDGetSignalError() instead")
    void documentsFindByMentionDocIDGetSignalE(QList<OAIDocument> summary, QNetworkReply::NetworkError error_type, QString error_str);
    void documentsFindByMentionDocIDGetSignalError(QList<OAIDocument> summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use documentsGetSignalError() instead")
    void documentsGetSignalE(QList<OAIDocument> summary, QNetworkReply::NetworkError error_type, QString error_str);
    void documentsGetSignalError(QList<OAIDocument> summary, QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use documentsDocIDGetSignalErrorFull() instead")
    void documentsDocIDGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void documentsDocIDGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use documentsFindByAuthorAuthorIDGetSignalErrorFull() instead")
    void documentsFindByAuthorAuthorIDGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void documentsFindByAuthorAuthorIDGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use documentsFindByDateGetSignalErrorFull() instead")
    void documentsFindByDateGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void documentsFindByDateGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use documentsFindByMentionDocIDGetSignalErrorFull() instead")
    void documentsFindByMentionDocIDGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void documentsFindByMentionDocIDGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use documentsGetSignalErrorFull() instead")
    void documentsGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void documentsGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
