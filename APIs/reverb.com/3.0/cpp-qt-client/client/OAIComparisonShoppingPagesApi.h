/**
 * reverb
 * reverb
 *
 * The version of the OpenAPI document: 3.0
 * Contact: integrations@reverb.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#ifndef OAI_OAIComparisonShoppingPagesApi_H
#define OAI_OAIComparisonShoppingPagesApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAIComparisonShoppingPagesApi : public QObject {
    Q_OBJECT

public:
    OAIComparisonShoppingPagesApi(const int timeOut = 0);
    ~OAIComparisonShoppingPagesApi();

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
    * @param[in]  id QString [optional]
    * @param[in]  slug QString [optional]
    */
    virtual void comparisonShoppingPagesFindGet(const ::OpenAPI::OptionalParam<QString> &id = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &slug = ::OpenAPI::OptionalParam<QString>());


    virtual void comparisonShoppingPagesGet();

    /**
    * @param[in]  id QString [required]
    */
    virtual void comparisonShoppingPagesIdGet(const QString &id);

    /**
    * @param[in]  id QString [required]
    * @param[in]  condition QString [required]
    * @param[in]  page qint32 [optional]
    * @param[in]  per_page qint32 [optional]
    * @param[in]  offset qint32 [optional]
    */
    virtual void comparisonShoppingPagesIdListingsGet(const QString &id, const QString &condition, const ::OpenAPI::OptionalParam<qint32> &page = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &per_page = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &offset = ::OpenAPI::OptionalParam<qint32>());

    /**
    * @param[in]  id QString [required]
    */
    virtual void comparisonShoppingPagesIdReviewsGet(const QString &id);


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

    void comparisonShoppingPagesFindGetCallback(OAIHttpRequestWorker *worker);
    void comparisonShoppingPagesGetCallback(OAIHttpRequestWorker *worker);
    void comparisonShoppingPagesIdGetCallback(OAIHttpRequestWorker *worker);
    void comparisonShoppingPagesIdListingsGetCallback(OAIHttpRequestWorker *worker);
    void comparisonShoppingPagesIdReviewsGetCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void comparisonShoppingPagesFindGetSignal();
    void comparisonShoppingPagesGetSignal();
    void comparisonShoppingPagesIdGetSignal();
    void comparisonShoppingPagesIdListingsGetSignal();
    void comparisonShoppingPagesIdReviewsGetSignal();


    void comparisonShoppingPagesFindGetSignalFull(OAIHttpRequestWorker *worker);
    void comparisonShoppingPagesGetSignalFull(OAIHttpRequestWorker *worker);
    void comparisonShoppingPagesIdGetSignalFull(OAIHttpRequestWorker *worker);
    void comparisonShoppingPagesIdListingsGetSignalFull(OAIHttpRequestWorker *worker);
    void comparisonShoppingPagesIdReviewsGetSignalFull(OAIHttpRequestWorker *worker);

    Q_DECL_DEPRECATED_X("Use comparisonShoppingPagesFindGetSignalError() instead")
    void comparisonShoppingPagesFindGetSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void comparisonShoppingPagesFindGetSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use comparisonShoppingPagesGetSignalError() instead")
    void comparisonShoppingPagesGetSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void comparisonShoppingPagesGetSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use comparisonShoppingPagesIdGetSignalError() instead")
    void comparisonShoppingPagesIdGetSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void comparisonShoppingPagesIdGetSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use comparisonShoppingPagesIdListingsGetSignalError() instead")
    void comparisonShoppingPagesIdListingsGetSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void comparisonShoppingPagesIdListingsGetSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use comparisonShoppingPagesIdReviewsGetSignalError() instead")
    void comparisonShoppingPagesIdReviewsGetSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void comparisonShoppingPagesIdReviewsGetSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use comparisonShoppingPagesFindGetSignalErrorFull() instead")
    void comparisonShoppingPagesFindGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void comparisonShoppingPagesFindGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use comparisonShoppingPagesGetSignalErrorFull() instead")
    void comparisonShoppingPagesGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void comparisonShoppingPagesGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use comparisonShoppingPagesIdGetSignalErrorFull() instead")
    void comparisonShoppingPagesIdGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void comparisonShoppingPagesIdGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use comparisonShoppingPagesIdListingsGetSignalErrorFull() instead")
    void comparisonShoppingPagesIdListingsGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void comparisonShoppingPagesIdListingsGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use comparisonShoppingPagesIdReviewsGetSignalErrorFull() instead")
    void comparisonShoppingPagesIdReviewsGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void comparisonShoppingPagesIdReviewsGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
