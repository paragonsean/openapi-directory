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

#ifndef OAI_OAICategoriesApi_H
#define OAI_OAICategoriesApi_H

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

class OAICategoriesApi : public QObject {
    Q_OBJECT

public:
    OAICategoriesApi(const int timeOut = 0);
    ~OAICategoriesApi();

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


    virtual void categoriesFlatGet();


    virtual void categoriesGet();

    /**
    * @param[in]  product_type QString [required]
    * @param[in]  category QString [required]
    */
    virtual void categoriesProductTypeCategoryGet(const QString &product_type, const QString &category);


    virtual void categoriesTaxonomyGet();

    /**
    * @param[in]  uuid QString [required]
    */
    virtual void categoriesUuidGet(const QString &uuid);


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

    void categoriesFlatGetCallback(OAIHttpRequestWorker *worker);
    void categoriesGetCallback(OAIHttpRequestWorker *worker);
    void categoriesProductTypeCategoryGetCallback(OAIHttpRequestWorker *worker);
    void categoriesTaxonomyGetCallback(OAIHttpRequestWorker *worker);
    void categoriesUuidGetCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void categoriesFlatGetSignal();
    void categoriesGetSignal();
    void categoriesProductTypeCategoryGetSignal();
    void categoriesTaxonomyGetSignal();
    void categoriesUuidGetSignal();


    void categoriesFlatGetSignalFull(OAIHttpRequestWorker *worker);
    void categoriesGetSignalFull(OAIHttpRequestWorker *worker);
    void categoriesProductTypeCategoryGetSignalFull(OAIHttpRequestWorker *worker);
    void categoriesTaxonomyGetSignalFull(OAIHttpRequestWorker *worker);
    void categoriesUuidGetSignalFull(OAIHttpRequestWorker *worker);

    Q_DECL_DEPRECATED_X("Use categoriesFlatGetSignalError() instead")
    void categoriesFlatGetSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void categoriesFlatGetSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use categoriesGetSignalError() instead")
    void categoriesGetSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void categoriesGetSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use categoriesProductTypeCategoryGetSignalError() instead")
    void categoriesProductTypeCategoryGetSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void categoriesProductTypeCategoryGetSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use categoriesTaxonomyGetSignalError() instead")
    void categoriesTaxonomyGetSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void categoriesTaxonomyGetSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use categoriesUuidGetSignalError() instead")
    void categoriesUuidGetSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void categoriesUuidGetSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use categoriesFlatGetSignalErrorFull() instead")
    void categoriesFlatGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void categoriesFlatGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use categoriesGetSignalErrorFull() instead")
    void categoriesGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void categoriesGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use categoriesProductTypeCategoryGetSignalErrorFull() instead")
    void categoriesProductTypeCategoryGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void categoriesProductTypeCategoryGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use categoriesTaxonomyGetSignalErrorFull() instead")
    void categoriesTaxonomyGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void categoriesTaxonomyGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use categoriesUuidGetSignalErrorFull() instead")
    void categoriesUuidGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void categoriesUuidGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
