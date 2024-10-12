/**
 * Checkout API
 * >ℹ️ Check the new [Checkout onboarding guide](https://developers.vtex.com/vtex-rest-api/docs/checkout-overview). We created this guide to improve the onboarding experience for developers at VTEX. It assembles all documentation on our Developer Portal about the Checkout and is organized by focusing on the developer's journey.    The Checkout API allows you to obtain and configure information about the shopping cart and its attachments, personalization of custom fields, orderForm structure, fulfillment data, order management, and identification of the sellers delivery region.    >ℹ️ Data modification operations (`POST`, `PATCH`, `PUT` or `DELETE` endpoints) shall not be performed in parallel in the Checkout APIs. They need to be enqueued by the client/requester. Otherwise, old values ​​can be overwritten incorrectly or competition errors may occur.    >⚠️ All endpoints that consult or edit the orderForm can change the authentication depending on the customer context. If you are handling information from a customer with a complete profile on the store, authentication will be required. You can only access or modify the customer data for these profiles with an authenticated request.    ## Shopping cart    Allows merchants to simulate, configure and customize shopping cart information.    - [POST - Cart Simulation](https://developers.vtex.com/vtex-rest-api/reference/cartsimulation)  - [GET - Get current or create a new cart](https://developers.vtex.com/vtex-rest-api/reference/createanewcart)  - [GET - Get cart information by ID](https://developers.vtex.com/vtex-rest-api/reference/getcartinformationbyid)  - [POST - Remove all items](https://developers.vtex.com/vtex-rest-api/reference/removeallitems)  - [GET - Remove all personal data](https://developers.vtex.com/vtex-rest-api/reference/removeallpersonaldata)  - [POST - Update cart items](https://developers.vtex.com/vtex-rest-api/reference/itemsupdate)  - [POST - Add cart items](https://developers.vtex.com/vtex-rest-api/reference/items)  - [PUT - Change price](https://developers.vtex.com/vtex-rest-api/reference/pricechange)  - [PATCH - Ignore profile data](https://developers.vtex.com/vtex-rest-api/reference/ignoreprofiledata)  - [GET - Cart installments](https://developers.vtex.com/vtex-rest-api/reference/getcartinstallments)  - [POST - Add coupons to the cart](https://developers.vtex.com/vtex-rest-api/reference/addcoupons)      ## Cart attachments    Allows merchants to obtain client profiles and add information to a given shopping cart.    - [GET - Get client profile by email](https://developers.vtex.com/vtex-rest-api/reference/getclientprofilebyemail)  - [POST - Add client profile](https://developers.vtex.com/vtex-rest-api/reference/addclientprofile)  - [POST - Add shipping address and select delivery option](https://developers.vtex.com/vtex-rest-api/reference/addshippingaddress)  - [POST - Add client preferences](https://developers.vtex.com/vtex-rest-api/reference/addclientpreferences)  - [POST - Add marketing data](https://developers.vtex.com/vtex-rest-api/reference/addmarketingdata)  - [POST - Add payment data](https://developers.vtex.com/vtex-rest-api/reference/addpaymentdata)  - [POST - Add merchant context data](https://developers.vtex.com/vtex-rest-api/reference/addmerchantcontextdata)      ## Custom data    Allows merchants to manage custom fields that were created by an app in their account.    - [PUT - Set multiple custom field values](https://developers.vtex.com/vtex-rest-api/reference/setmultiplecustomfieldvalues)  - [PUT - Set single custom field value](https://developers.vtex.com/vtex-rest-api/reference/setsinglecustomfieldvalue)  - [DELETE - Remove single custom field value](https://developers.vtex.com/vtex-rest-api/reference/removesinglecustomfieldvalue)      ## Configuration    Allows merchants to configure orderForm in the account and seller exchange on a given order.    - [GET - Get orderForm configuration](https://developers.vtex.com/vtex-rest-api/reference/getorderformconfiguration)  - [POST - Update orderForm configuration](https://developers.vtex.com/vtex-rest-api/reference/updateorderformconfiguration)  - [GET - Get window to change seller](https://developers.vtex.com/vtex-rest-api/reference/getwindowtochangeseller)  - [POST - Update window to change seller](https://developers.vtex.com/vtex-rest-api/reference/updatewindowtochangeseller)  - [POST - Clear orderForm messages](https://developers.vtex.com/vtex-rest-api/reference/clearorderformmessages)      ## Fulfillment    Allows merchants to obtain pickup points and address information.    - [GET - List pickup points by location](https://developers.vtex.com/vtex-rest-api/reference/listpickupppointsbylocation)  - [GET - Get address by postal code](https://developers.vtex.com/vtex-rest-api/reference/getaddressbypostalcode)      ## Order placement    Allows merchants to place and process orders by creating a new cart or using an existing cart.    - [POST - Place order from an existing cart](https://developers.vtex.com/vtex-rest-api/reference/placeorderfromexistingorderform)  - [PUT - Place order](https://developers.vtex.com/vtex-rest-api/reference/placeorder)  - [POST - Process order](https://developers.vtex.com/vtex-rest-api/reference/processorder)      ## Region    Allows merchants to obtain a list of sellers serving a specific delivery region.    - [GET - Get sellers by region or address](https://developers.vtex.com/vtex-rest-api/reference/getsellersbyregion)
 *
 * The version of the OpenAPI document: 1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#ifndef OAI_OAICartAttachmentsApi_H
#define OAI_OAICartAttachmentsApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAIAddClientPreferences_request.h"
#include "OAIAddClientProfile_request.h"
#include "OAIAddMarketingData_request.h"
#include "OAIAddMerchantContextData_200_response.h"
#include "OAIAddMerchantContextData_request.h"
#include "OAIAddPaymentData_request.h"
#include "OAIAddShippingAddress_request.h"
#include "OAIGetClientProfileByEmail_200_response.h"
#include <QJsonValue>
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAICartAttachmentsApi : public QObject {
    Q_OBJECT

public:
    OAICartAttachmentsApi(const int timeOut = 0);
    ~OAICartAttachmentsApi();

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
    * @param[in]  content_type QString [required]
    * @param[in]  accept QString [required]
    * @param[in]  order_form_id QString [required]
    * @param[in]  oai_add_client_preferences_request OAIAddClientPreferences_request [required]
    */
    virtual void addClientPreferences(const QString &content_type, const QString &accept, const QString &order_form_id, const OAIAddClientPreferences_request &oai_add_client_preferences_request);

    /**
    * @param[in]  content_type QString [required]
    * @param[in]  accept QString [required]
    * @param[in]  order_form_id QString [required]
    * @param[in]  oai_add_client_profile_request OAIAddClientProfile_request [required]
    */
    virtual void addClientProfile(const QString &content_type, const QString &accept, const QString &order_form_id, const OAIAddClientProfile_request &oai_add_client_profile_request);

    /**
    * @param[in]  content_type QString [required]
    * @param[in]  accept QString [required]
    * @param[in]  order_form_id QString [required]
    * @param[in]  oai_add_marketing_data_request OAIAddMarketingData_request [required]
    */
    virtual void addMarketingData(const QString &content_type, const QString &accept, const QString &order_form_id, const OAIAddMarketingData_request &oai_add_marketing_data_request);

    /**
    * @param[in]  content_type QString [required]
    * @param[in]  accept QString [required]
    * @param[in]  order_form_id QString [required]
    * @param[in]  oai_add_merchant_context_data_request OAIAddMerchantContextData_request [required]
    */
    virtual void addMerchantContextData(const QString &content_type, const QString &accept, const QString &order_form_id, const OAIAddMerchantContextData_request &oai_add_merchant_context_data_request);

    /**
    * @param[in]  content_type QString [required]
    * @param[in]  accept QString [required]
    * @param[in]  order_form_id QString [required]
    * @param[in]  oai_add_payment_data_request OAIAddPaymentData_request [required]
    */
    virtual void addPaymentData(const QString &content_type, const QString &accept, const QString &order_form_id, const OAIAddPaymentData_request &oai_add_payment_data_request);

    /**
    * @param[in]  content_type QString [required]
    * @param[in]  accept QString [required]
    * @param[in]  order_form_id QString [required]
    * @param[in]  oai_add_shipping_address_request OAIAddShippingAddress_request [required]
    */
    virtual void addShippingAddress(const QString &content_type, const QString &accept, const QString &order_form_id, const OAIAddShippingAddress_request &oai_add_shipping_address_request);

    /**
    * @param[in]  content_type QString [required]
    * @param[in]  accept QString [required]
    * @param[in]  email QString [required]
    */
    virtual void getClientProfileByEmail(const QString &content_type, const QString &accept, const QString &email);


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

    void addClientPreferencesCallback(OAIHttpRequestWorker *worker);
    void addClientProfileCallback(OAIHttpRequestWorker *worker);
    void addMarketingDataCallback(OAIHttpRequestWorker *worker);
    void addMerchantContextDataCallback(OAIHttpRequestWorker *worker);
    void addPaymentDataCallback(OAIHttpRequestWorker *worker);
    void addShippingAddressCallback(OAIHttpRequestWorker *worker);
    void getClientProfileByEmailCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void addClientPreferencesSignal(QJsonValue summary);
    void addClientProfileSignal();
    void addMarketingDataSignal();
    void addMerchantContextDataSignal(OAIAddMerchantContextData_200_response summary);
    void addPaymentDataSignal();
    void addShippingAddressSignal();
    void getClientProfileByEmailSignal(OAIGetClientProfileByEmail_200_response summary);


    void addClientPreferencesSignalFull(OAIHttpRequestWorker *worker, QJsonValue summary);
    void addClientProfileSignalFull(OAIHttpRequestWorker *worker);
    void addMarketingDataSignalFull(OAIHttpRequestWorker *worker);
    void addMerchantContextDataSignalFull(OAIHttpRequestWorker *worker, OAIAddMerchantContextData_200_response summary);
    void addPaymentDataSignalFull(OAIHttpRequestWorker *worker);
    void addShippingAddressSignalFull(OAIHttpRequestWorker *worker);
    void getClientProfileByEmailSignalFull(OAIHttpRequestWorker *worker, OAIGetClientProfileByEmail_200_response summary);

    Q_DECL_DEPRECATED_X("Use addClientPreferencesSignalError() instead")
    void addClientPreferencesSignalE(QJsonValue summary, QNetworkReply::NetworkError error_type, QString error_str);
    void addClientPreferencesSignalError(QJsonValue summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use addClientProfileSignalError() instead")
    void addClientProfileSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void addClientProfileSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use addMarketingDataSignalError() instead")
    void addMarketingDataSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void addMarketingDataSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use addMerchantContextDataSignalError() instead")
    void addMerchantContextDataSignalE(OAIAddMerchantContextData_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void addMerchantContextDataSignalError(OAIAddMerchantContextData_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use addPaymentDataSignalError() instead")
    void addPaymentDataSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void addPaymentDataSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use addShippingAddressSignalError() instead")
    void addShippingAddressSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void addShippingAddressSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getClientProfileByEmailSignalError() instead")
    void getClientProfileByEmailSignalE(OAIGetClientProfileByEmail_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void getClientProfileByEmailSignalError(OAIGetClientProfileByEmail_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use addClientPreferencesSignalErrorFull() instead")
    void addClientPreferencesSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void addClientPreferencesSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use addClientProfileSignalErrorFull() instead")
    void addClientProfileSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void addClientProfileSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use addMarketingDataSignalErrorFull() instead")
    void addMarketingDataSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void addMarketingDataSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use addMerchantContextDataSignalErrorFull() instead")
    void addMerchantContextDataSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void addMerchantContextDataSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use addPaymentDataSignalErrorFull() instead")
    void addPaymentDataSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void addPaymentDataSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use addShippingAddressSignalErrorFull() instead")
    void addShippingAddressSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void addShippingAddressSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getClientProfileByEmailSignalErrorFull() instead")
    void getClientProfileByEmailSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getClientProfileByEmailSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
