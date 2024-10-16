/**
 * Clever-Cloud API
 * Public API for managing Clever-Cloud data and products
 *
 * The version of the OpenAPI document: 1.0.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#ifndef OAI_OAIProductsApi_H
#define OAI_OAIProductsApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAICountry.h"
#include "OAIInstance.h"
#include "OAIProvider.h"
#include "OAIZone.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAIProductsApi : public QObject {
    Q_OBJECT

public:
    OAIProductsApi(const int timeOut = 0);
    ~OAIProductsApi();

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
    * @param[in]  provider_id QString [required]
    */
    virtual void getProductsAddonProvidersProviderId(const QString &provider_id);


    virtual void getProductsAddonProviders();


    virtual void getProductsCountries();


    virtual void getProductsCountrycodes();

    /**
    * @param[in]  type QString [required]
    * @param[in]  version QString [required]
    * @param[in]  r_for QString [optional]
    * @param[in]  app QString [optional]
    */
    virtual void getProductsInstancesTypeVersion(const QString &type, const QString &version, const ::OpenAPI::OptionalParam<QString> &r_for = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &app = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  r_for QString [optional]
    */
    virtual void getProductsInstances(const ::OpenAPI::OptionalParam<QString> &r_for = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  coupon QString [optional]
    * @param[in]  orga_id QString [optional]
    * @param[in]  currency QString [optional]
    */
    virtual void getProductsPackages(const ::OpenAPI::OptionalParam<QString> &coupon = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &orga_id = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &currency = ::OpenAPI::OptionalParam<QString>());


    virtual void getProductsPrices();


    virtual void getProductsZones();

    /**
    * @param[in]  provider_id QString [required]
    */
    virtual void productsAddonprovidersProviderIdVersionsGet(const QString &provider_id);


    virtual void productsMfaKindsGet();


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

    void getProductsAddonProvidersProviderIdCallback(OAIHttpRequestWorker *worker);
    void getProductsAddonProvidersCallback(OAIHttpRequestWorker *worker);
    void getProductsCountriesCallback(OAIHttpRequestWorker *worker);
    void getProductsCountrycodesCallback(OAIHttpRequestWorker *worker);
    void getProductsInstancesTypeVersionCallback(OAIHttpRequestWorker *worker);
    void getProductsInstancesCallback(OAIHttpRequestWorker *worker);
    void getProductsPackagesCallback(OAIHttpRequestWorker *worker);
    void getProductsPricesCallback(OAIHttpRequestWorker *worker);
    void getProductsZonesCallback(OAIHttpRequestWorker *worker);
    void productsAddonprovidersProviderIdVersionsGetCallback(OAIHttpRequestWorker *worker);
    void productsMfaKindsGetCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void getProductsAddonProvidersProviderIdSignal(OAIProvider summary);
    void getProductsAddonProvidersSignal(QList<OAIProvider> summary);
    void getProductsCountriesSignal(OAICountry summary);
    void getProductsCountrycodesSignal(OAICountry summary);
    void getProductsInstancesTypeVersionSignal(OAIInstance summary);
    void getProductsInstancesSignal(QList<OAIInstance> summary);
    void getProductsPackagesSignal();
    void getProductsPricesSignal();
    void getProductsZonesSignal(QList<OAIZone> summary);
    void productsAddonprovidersProviderIdVersionsGetSignal();
    void productsMfaKindsGetSignal();


    void getProductsAddonProvidersProviderIdSignalFull(OAIHttpRequestWorker *worker, OAIProvider summary);
    void getProductsAddonProvidersSignalFull(OAIHttpRequestWorker *worker, QList<OAIProvider> summary);
    void getProductsCountriesSignalFull(OAIHttpRequestWorker *worker, OAICountry summary);
    void getProductsCountrycodesSignalFull(OAIHttpRequestWorker *worker, OAICountry summary);
    void getProductsInstancesTypeVersionSignalFull(OAIHttpRequestWorker *worker, OAIInstance summary);
    void getProductsInstancesSignalFull(OAIHttpRequestWorker *worker, QList<OAIInstance> summary);
    void getProductsPackagesSignalFull(OAIHttpRequestWorker *worker);
    void getProductsPricesSignalFull(OAIHttpRequestWorker *worker);
    void getProductsZonesSignalFull(OAIHttpRequestWorker *worker, QList<OAIZone> summary);
    void productsAddonprovidersProviderIdVersionsGetSignalFull(OAIHttpRequestWorker *worker);
    void productsMfaKindsGetSignalFull(OAIHttpRequestWorker *worker);

    Q_DECL_DEPRECATED_X("Use getProductsAddonProvidersProviderIdSignalError() instead")
    void getProductsAddonProvidersProviderIdSignalE(OAIProvider summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getProductsAddonProvidersProviderIdSignalError(OAIProvider summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getProductsAddonProvidersSignalError() instead")
    void getProductsAddonProvidersSignalE(QList<OAIProvider> summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getProductsAddonProvidersSignalError(QList<OAIProvider> summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getProductsCountriesSignalError() instead")
    void getProductsCountriesSignalE(OAICountry summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getProductsCountriesSignalError(OAICountry summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getProductsCountrycodesSignalError() instead")
    void getProductsCountrycodesSignalE(OAICountry summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getProductsCountrycodesSignalError(OAICountry summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getProductsInstancesTypeVersionSignalError() instead")
    void getProductsInstancesTypeVersionSignalE(OAIInstance summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getProductsInstancesTypeVersionSignalError(OAIInstance summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getProductsInstancesSignalError() instead")
    void getProductsInstancesSignalE(QList<OAIInstance> summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getProductsInstancesSignalError(QList<OAIInstance> summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getProductsPackagesSignalError() instead")
    void getProductsPackagesSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void getProductsPackagesSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getProductsPricesSignalError() instead")
    void getProductsPricesSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void getProductsPricesSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getProductsZonesSignalError() instead")
    void getProductsZonesSignalE(QList<OAIZone> summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getProductsZonesSignalError(QList<OAIZone> summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use productsAddonprovidersProviderIdVersionsGetSignalError() instead")
    void productsAddonprovidersProviderIdVersionsGetSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void productsAddonprovidersProviderIdVersionsGetSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use productsMfaKindsGetSignalError() instead")
    void productsMfaKindsGetSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void productsMfaKindsGetSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use getProductsAddonProvidersProviderIdSignalErrorFull() instead")
    void getProductsAddonProvidersProviderIdSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getProductsAddonProvidersProviderIdSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getProductsAddonProvidersSignalErrorFull() instead")
    void getProductsAddonProvidersSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getProductsAddonProvidersSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getProductsCountriesSignalErrorFull() instead")
    void getProductsCountriesSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getProductsCountriesSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getProductsCountrycodesSignalErrorFull() instead")
    void getProductsCountrycodesSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getProductsCountrycodesSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getProductsInstancesTypeVersionSignalErrorFull() instead")
    void getProductsInstancesTypeVersionSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getProductsInstancesTypeVersionSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getProductsInstancesSignalErrorFull() instead")
    void getProductsInstancesSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getProductsInstancesSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getProductsPackagesSignalErrorFull() instead")
    void getProductsPackagesSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getProductsPackagesSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getProductsPricesSignalErrorFull() instead")
    void getProductsPricesSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getProductsPricesSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getProductsZonesSignalErrorFull() instead")
    void getProductsZonesSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getProductsZonesSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use productsAddonprovidersProviderIdVersionsGetSignalErrorFull() instead")
    void productsAddonprovidersProviderIdVersionsGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void productsAddonprovidersProviderIdVersionsGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use productsMfaKindsGetSignalErrorFull() instead")
    void productsMfaKindsGetSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void productsMfaKindsGetSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
