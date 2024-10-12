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

#ifndef OAI_OAIStockStatusesProductSkuApi_H
#define OAI_OAIStockStatusesProductSkuApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAICatalog_inventory_data_stock_status_interface.h"
#include "OAIError_response.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAIStockStatusesProductSkuApi : public QObject {
    Q_OBJECT

public:
    OAIStockStatusesProductSkuApi(const int timeOut = 0);
    ~OAIStockStatusesProductSkuApi();

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
    * @param[in]  product_sku QString [required]
    * @param[in]  scope_id qint32 [optional]
    */
    virtual void catalogInventoryStockRegistryV1GetStockStatusBySkuGet(const QString &product_sku, const ::OpenAPI::OptionalParam<qint32> &scope_id = ::OpenAPI::OptionalParam<qint32>());


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

    void catalogInventoryStockRegistryV1GetStockStatusBySkuGetCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void catalogInventoryStockRegistryV1GetStockStatusBySkuGetSignal(OAICatalog_inventory_data_stock_status_interface summary);


    void catalogInventoryStockRegistryV1GetStockStatusBySkuGetSignalFull(OAIHttpRequestWorker *worker, OAICatalog_inventory_data_stock_status_interface summary);

    Q_DECL_DEPRECATED_X("Use catalogInventoryStockRegistryV1GetStockStatusBySkuGetSignalError() instead")
    void catalogInventoryStockRegistryV1GetStockStatusBySkuGetSignalE(OAICatalog_inventory_data_stock_status_interface summary, QNetworkReply::NetworkError error_type, QString error_str);
    void catalogInventoryStockRegistryV1GetStockStatusBySkuGetSignalError(OAICatalog_inventory_data_stock_status_interface summary, QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use catalogInventoryStockRegistryV1GetStockStatusBySkuGetSignalErrorFull() instead")
    void catalogInventoryStockRegistryV1GetStockStatusBySkuGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void catalogInventoryStockRegistryV1GetStockStatusBySkuGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
