/**
 * Magento B2B
 * Magento Commerce is the leading provider of open omnichannel innovation.
 *
 * The version of the OpenAPI document: 2.2.10
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#ifndef OAI_OAIProductsSkuDownloadableLinksIdApi_H
#define OAI_OAIProductsSkuDownloadableLinksIdApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAIDownloadableLinkRepositoryV1SavePost_request.h"
#include "OAIError_response.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAIProductsSkuDownloadableLinksIdApi : public QObject {
    Q_OBJECT

public:
    OAIProductsSkuDownloadableLinksIdApi(const int timeOut = 0);
    ~OAIProductsSkuDownloadableLinksIdApi();

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
    * @param[in]  sku QString [required]
    * @param[in]  id QString [required]
    * @param[in]  oai_downloadable_link_repository_v1_save_post_request OAIDownloadableLinkRepositoryV1SavePost_request [optional]
    */
    virtual void downloadableLinkRepositoryV1SavePut(const QString &sku, const QString &id, const ::OpenAPI::OptionalParam<OAIDownloadableLinkRepositoryV1SavePost_request> &oai_downloadable_link_repository_v1_save_post_request = ::OpenAPI::OptionalParam<OAIDownloadableLinkRepositoryV1SavePost_request>());


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

    void downloadableLinkRepositoryV1SavePutCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void downloadableLinkRepositoryV1SavePutSignal(qint32 summary);


    void downloadableLinkRepositoryV1SavePutSignalFull(OAIHttpRequestWorker *worker, qint32 summary);

    Q_DECL_DEPRECATED_X("Use downloadableLinkRepositoryV1SavePutSignalError() instead")
    void downloadableLinkRepositoryV1SavePutSignalE(qint32 summary, QNetworkReply::NetworkError error_type, QString error_str);
    void downloadableLinkRepositoryV1SavePutSignalError(qint32 summary, QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use downloadableLinkRepositoryV1SavePutSignalErrorFull() instead")
    void downloadableLinkRepositoryV1SavePutSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void downloadableLinkRepositoryV1SavePutSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
