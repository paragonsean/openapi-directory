/**
 * Noosh API application
 * Full description of Noosh API
 *
 * The version of the OpenAPI document: 1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#ifndef OAI_OAITimeCardApi_H
#define OAI_OAITimeCardApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAIHTTPStatusVO.h"
#include "OAITimeCardDetailVO.h"
#include "OAITimeCardListVO.h"
#include "OAITimeCardReceivedDetailVO.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAITimeCardApi : public QObject {
    Q_OBJECT

public:
    OAITimeCardApi(const int timeOut = 0);
    ~OAITimeCardApi();

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
    * @param[in]  workgroup_id QString [required]
    * @param[in]  time_card_id QString [required]
    */
    virtual void getMyTimeCard(const QString &workgroup_id, const QString &time_card_id);

    /**
    * @param[in]  workgroup_id QString [required]
    */
    virtual void getMyTimeCardList(const QString &workgroup_id);

    /**
    * @param[in]  workgroup_id QString [required]
    * @param[in]  time_card_id QString [required]
    */
    virtual void getReceivedTimeCard(const QString &workgroup_id, const QString &time_card_id);

    /**
    * @param[in]  workgroup_id QString [required]
    */
    virtual void getReceivedTimeCardList(const QString &workgroup_id);


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

    void getMyTimeCardCallback(OAIHttpRequestWorker *worker);
    void getMyTimeCardListCallback(OAIHttpRequestWorker *worker);
    void getReceivedTimeCardCallback(OAIHttpRequestWorker *worker);
    void getReceivedTimeCardListCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void getMyTimeCardSignal(OAITimeCardDetailVO summary);
    void getMyTimeCardListSignal(OAITimeCardListVO summary);
    void getReceivedTimeCardSignal(OAITimeCardReceivedDetailVO summary);
    void getReceivedTimeCardListSignal(OAITimeCardListVO summary);


    void getMyTimeCardSignalFull(OAIHttpRequestWorker *worker, OAITimeCardDetailVO summary);
    void getMyTimeCardListSignalFull(OAIHttpRequestWorker *worker, OAITimeCardListVO summary);
    void getReceivedTimeCardSignalFull(OAIHttpRequestWorker *worker, OAITimeCardReceivedDetailVO summary);
    void getReceivedTimeCardListSignalFull(OAIHttpRequestWorker *worker, OAITimeCardListVO summary);

    Q_DECL_DEPRECATED_X("Use getMyTimeCardSignalError() instead")
    void getMyTimeCardSignalE(OAITimeCardDetailVO summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getMyTimeCardSignalError(OAITimeCardDetailVO summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getMyTimeCardListSignalError() instead")
    void getMyTimeCardListSignalE(OAITimeCardListVO summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getMyTimeCardListSignalError(OAITimeCardListVO summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getReceivedTimeCardSignalError() instead")
    void getReceivedTimeCardSignalE(OAITimeCardReceivedDetailVO summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getReceivedTimeCardSignalError(OAITimeCardReceivedDetailVO summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getReceivedTimeCardListSignalError() instead")
    void getReceivedTimeCardListSignalE(OAITimeCardListVO summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getReceivedTimeCardListSignalError(OAITimeCardListVO summary, QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use getMyTimeCardSignalErrorFull() instead")
    void getMyTimeCardSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getMyTimeCardSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getMyTimeCardListSignalErrorFull() instead")
    void getMyTimeCardListSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getMyTimeCardListSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getReceivedTimeCardSignalErrorFull() instead")
    void getReceivedTimeCardSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getReceivedTimeCardSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getReceivedTimeCardListSignalErrorFull() instead")
    void getReceivedTimeCardListSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getReceivedTimeCardListSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
