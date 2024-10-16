/**
 * Taxamo
 * Taxamo’s elegant suite of APIs and comprehensive reporting dashboard enables digital merchants to easily comply with EU regulatory requirements on tax calculation, evidence collection, tax return creation and data storage.
 *
 * The version of the OpenAPI document: 1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#ifndef OAI_OAITaxApi_H
#define OAI_OAITaxApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAICalculateSimpleTaxOut.h"
#include "OAICalculateTaxIn.h"
#include "OAICalculateTaxLocationOut.h"
#include "OAICalculateTaxOut.h"
#include "OAIValidateTaxNumberOut.h"
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAITaxApi : public QObject {
    Q_OBJECT

public:
    OAITaxApi(const int timeOut = 0);
    ~OAITaxApi();

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
    * @param[in]  currency_code QString [required]
    * @param[in]  product_type QString [optional]
    * @param[in]  invoice_address_city QString [optional]
    * @param[in]  buyer_credit_card_prefix QString [optional]
    * @param[in]  invoice_address_region QString [optional]
    * @param[in]  unit_price double [optional]
    * @param[in]  quantity double [optional]
    * @param[in]  buyer_tax_number QString [optional]
    * @param[in]  force_country_code QString [optional]
    * @param[in]  order_date QString [optional]
    * @param[in]  amount double [optional]
    * @param[in]  billing_country_code QString [optional]
    * @param[in]  invoice_address_postal_code QString [optional]
    * @param[in]  total_amount double [optional]
    * @param[in]  tax_deducted bool [optional]
    */
    virtual void calculateSimpleTax(const QString &currency_code, const ::OpenAPI::OptionalParam<QString> &product_type = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &invoice_address_city = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &buyer_credit_card_prefix = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &invoice_address_region = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<double> &unit_price = ::OpenAPI::OptionalParam<double>(), const ::OpenAPI::OptionalParam<double> &quantity = ::OpenAPI::OptionalParam<double>(), const ::OpenAPI::OptionalParam<QString> &buyer_tax_number = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &force_country_code = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &order_date = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<double> &amount = ::OpenAPI::OptionalParam<double>(), const ::OpenAPI::OptionalParam<QString> &billing_country_code = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &invoice_address_postal_code = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<double> &total_amount = ::OpenAPI::OptionalParam<double>(), const ::OpenAPI::OptionalParam<bool> &tax_deducted = ::OpenAPI::OptionalParam<bool>());

    /**
    * @param[in]  input OAICalculateTaxIn [required]
    */
    virtual void calculateTax(const OAICalculateTaxIn &input);

    /**
    * @param[in]  billing_country_code QString [optional]
    * @param[in]  buyer_credit_card_prefix QString [optional]
    */
    virtual void calculateTaxLocation(const ::OpenAPI::OptionalParam<QString> &billing_country_code = ::OpenAPI::OptionalParam<QString>(), const ::OpenAPI::OptionalParam<QString> &buyer_credit_card_prefix = ::OpenAPI::OptionalParam<QString>());

    /**
    * @param[in]  tax_number QString [required]
    * @param[in]  country_code QString [optional]
    */
    virtual void validateTaxNumber(const QString &tax_number, const ::OpenAPI::OptionalParam<QString> &country_code = ::OpenAPI::OptionalParam<QString>());


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

    void calculateSimpleTaxCallback(OAIHttpRequestWorker *worker);
    void calculateTaxCallback(OAIHttpRequestWorker *worker);
    void calculateTaxLocationCallback(OAIHttpRequestWorker *worker);
    void validateTaxNumberCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void calculateSimpleTaxSignal(OAICalculateSimpleTaxOut summary);
    void calculateTaxSignal(OAICalculateTaxOut summary);
    void calculateTaxLocationSignal(OAICalculateTaxLocationOut summary);
    void validateTaxNumberSignal(OAIValidateTaxNumberOut summary);


    void calculateSimpleTaxSignalFull(OAIHttpRequestWorker *worker, OAICalculateSimpleTaxOut summary);
    void calculateTaxSignalFull(OAIHttpRequestWorker *worker, OAICalculateTaxOut summary);
    void calculateTaxLocationSignalFull(OAIHttpRequestWorker *worker, OAICalculateTaxLocationOut summary);
    void validateTaxNumberSignalFull(OAIHttpRequestWorker *worker, OAIValidateTaxNumberOut summary);

    Q_DECL_DEPRECATED_X("Use calculateSimpleTaxSignalError() instead")
    void calculateSimpleTaxSignalE(OAICalculateSimpleTaxOut summary, QNetworkReply::NetworkError error_type, QString error_str);
    void calculateSimpleTaxSignalError(OAICalculateSimpleTaxOut summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use calculateTaxSignalError() instead")
    void calculateTaxSignalE(OAICalculateTaxOut summary, QNetworkReply::NetworkError error_type, QString error_str);
    void calculateTaxSignalError(OAICalculateTaxOut summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use calculateTaxLocationSignalError() instead")
    void calculateTaxLocationSignalE(OAICalculateTaxLocationOut summary, QNetworkReply::NetworkError error_type, QString error_str);
    void calculateTaxLocationSignalError(OAICalculateTaxLocationOut summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use validateTaxNumberSignalError() instead")
    void validateTaxNumberSignalE(OAIValidateTaxNumberOut summary, QNetworkReply::NetworkError error_type, QString error_str);
    void validateTaxNumberSignalError(OAIValidateTaxNumberOut summary, QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use calculateSimpleTaxSignalErrorFull() instead")
    void calculateSimpleTaxSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void calculateSimpleTaxSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use calculateTaxSignalErrorFull() instead")
    void calculateTaxSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void calculateTaxSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use calculateTaxLocationSignalErrorFull() instead")
    void calculateTaxLocationSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void calculateTaxLocationSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use validateTaxNumberSignalErrorFull() instead")
    void validateTaxNumberSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void validateTaxNumberSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
