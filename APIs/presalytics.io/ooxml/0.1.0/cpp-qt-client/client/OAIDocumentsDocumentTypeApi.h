/**
 * OOXML Automation
 * This API helps users convert Excel and Powerpoint documents into rich, live dashboards and stories.
 *
 * The version of the OpenAPI document: 0.1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#ifndef OAI_OAIDocumentsDocumentTypeApi_H
#define OAI_OAIDocumentsDocumentTypeApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAIDocumentType.h"
#include "OAIProblemDetails.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAIDocumentsDocumentTypeApi : public QObject {
    Q_OBJECT

public:
    OAIDocumentsDocumentTypeApi(const int timeOut = 0);
    ~OAIDocumentsDocumentTypeApi();

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


    virtual void documentsDocumenttypeGet();

    /**
    * @param[in]  id QString [required]
    */
    virtual void documentsDocumenttypeGetId(const QString &id);

    /**
    * @param[in]  type_id qint32 [required]
    */
    virtual void documentsDocumenttypeTypeidGetTypeId(const qint32 &type_id);


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

    void documentsDocumenttypeGetCallback(OAIHttpRequestWorker *worker);
    void documentsDocumenttypeGetIdCallback(OAIHttpRequestWorker *worker);
    void documentsDocumenttypeTypeidGetTypeIdCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void documentsDocumenttypeGetSignal(QList<OAIDocumentType> summary);
    void documentsDocumenttypeGetIdSignal(OAIDocumentType summary);
    void documentsDocumenttypeTypeidGetTypeIdSignal(OAIDocumentType summary);


    void documentsDocumenttypeGetSignalFull(OAIHttpRequestWorker *worker, QList<OAIDocumentType> summary);
    void documentsDocumenttypeGetIdSignalFull(OAIHttpRequestWorker *worker, OAIDocumentType summary);
    void documentsDocumenttypeTypeidGetTypeIdSignalFull(OAIHttpRequestWorker *worker, OAIDocumentType summary);

    Q_DECL_DEPRECATED_X("Use documentsDocumenttypeGetSignalError() instead")
    void documentsDocumenttypeGetSignalE(QList<OAIDocumentType> summary, QNetworkReply::NetworkError error_type, QString error_str);
    void documentsDocumenttypeGetSignalError(QList<OAIDocumentType> summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use documentsDocumenttypeGetIdSignalError() instead")
    void documentsDocumenttypeGetIdSignalE(OAIDocumentType summary, QNetworkReply::NetworkError error_type, QString error_str);
    void documentsDocumenttypeGetIdSignalError(OAIDocumentType summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use documentsDocumenttypeTypeidGetTypeIdSignalError() instead")
    void documentsDocumenttypeTypeidGetTypeIdSignalE(OAIDocumentType summary, QNetworkReply::NetworkError error_type, QString error_str);
    void documentsDocumenttypeTypeidGetTypeIdSignalError(OAIDocumentType summary, QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use documentsDocumenttypeGetSignalErrorFull() instead")
    void documentsDocumenttypeGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void documentsDocumenttypeGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use documentsDocumenttypeGetIdSignalErrorFull() instead")
    void documentsDocumenttypeGetIdSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void documentsDocumenttypeGetIdSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use documentsDocumenttypeTypeidGetTypeIdSignalErrorFull() instead")
    void documentsDocumenttypeTypeidGetTypeIdSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void documentsDocumenttypeTypeidGetTypeIdSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
