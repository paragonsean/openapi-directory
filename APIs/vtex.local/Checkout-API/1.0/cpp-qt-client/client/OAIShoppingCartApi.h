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

#ifndef OAI_OAIShoppingCartApi_H
#define OAI_OAIShoppingCartApi_H

#include "OAIHelpers.h"
#include "OAIHttpRequest.h"
#include "OAIServerConfiguration.h"
#include "OAIOauth.h"

#include "OAIAddCoupons_200_response.h"
#include "OAIAddCoupons_request.h"
#include "OAICartSimulation_200_response.h"
#include "OAICartSimulation_request.h"
#include "OAIIgnoreProfileData_request.h"
#include "OAIItemsUpdate_200_response.h"
#include "OAIItemsUpdate_request.h"
#include "OAIItems_200_response.h"
#include "OAIItems_request.h"
#include "OAIObject.h"
#include "OAIPriceChangeRequest.h"
#include <QJsonValue>
#include <QString>

#include <QObject>
#include <QByteArray>
#include <QStringList>
#include <QList>
#include <QNetworkAccessManager>

namespace OpenAPI {

class OAIShoppingCartApi : public QObject {
    Q_OBJECT

public:
    OAIShoppingCartApi(const int timeOut = 0);
    ~OAIShoppingCartApi();

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
    * @param[in]  order_form_id QString [required]
    * @param[in]  content_type QString [required]
    * @param[in]  accept QString [required]
    * @param[in]  oai_add_coupons_request OAIAddCoupons_request [required]
    */
    virtual void addCoupons(const QString &order_form_id, const QString &content_type, const QString &accept, const OAIAddCoupons_request &oai_add_coupons_request);

    /**
    * @param[in]  content_type QString [required]
    * @param[in]  accept QString [required]
    * @param[in]  rnb_behavior qint32 [optional]
    * @param[in]  sc qint32 [optional]
    * @param[in]  oai_cart_simulation_request OAICartSimulation_request [optional]
    */
    virtual void cartSimulation(const QString &content_type, const QString &accept, const ::OpenAPI::OptionalParam<qint32> &rnb_behavior = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<qint32> &sc = ::OpenAPI::OptionalParam<qint32>(), const ::OpenAPI::OptionalParam<OAICartSimulation_request> &oai_cart_simulation_request = ::OpenAPI::OptionalParam<OAICartSimulation_request>());

    /**
    * @param[in]  content_type QString [required]
    * @param[in]  accept QString [required]
    * @param[in]  force_new_cart bool [optional]
    */
    virtual void createANewCart(const QString &content_type, const QString &accept, const ::OpenAPI::OptionalParam<bool> &force_new_cart = ::OpenAPI::OptionalParam<bool>());

    /**
    * @param[in]  order_form_id QString [required]
    * @param[in]  content_type QString [required]
    * @param[in]  accept QString [required]
    * @param[in]  refresh_outdated_data bool [optional]
    */
    virtual void getCartInformationById(const QString &order_form_id, const QString &content_type, const QString &accept, const ::OpenAPI::OptionalParam<bool> &refresh_outdated_data = ::OpenAPI::OptionalParam<bool>());

    /**
    * @param[in]  order_form_id QString [required]
    * @param[in]  payment_system qint32 [required]
    * @param[in]  content_type QString [required]
    * @param[in]  accept QString [required]
    */
    virtual void getCartInstallments(const QString &order_form_id, const qint32 &payment_system, const QString &content_type, const QString &accept);

    /**
    * @param[in]  order_form_id QString [required]
    * @param[in]  content_type QString [required]
    * @param[in]  accept QString [required]
    * @param[in]  oai_ignore_profile_data_request OAIIgnoreProfileData_request [required]
    */
    virtual void ignoreProfileData(const QString &order_form_id, const QString &content_type, const QString &accept, const OAIIgnoreProfileData_request &oai_ignore_profile_data_request);

    /**
    * @param[in]  content_type QString [required]
    * @param[in]  accept QString [required]
    * @param[in]  order_form_id QString [required]
    * @param[in]  oai_items_request OAIItems_request [required]
    * @param[in]  allowed_outdated_data QList<QJsonValue> [optional]
    */
    virtual void items(const QString &content_type, const QString &accept, const QString &order_form_id, const OAIItems_request &oai_items_request, const ::OpenAPI::OptionalParam<QList<QJsonValue>> &allowed_outdated_data = ::OpenAPI::OptionalParam<QList<QJsonValue>>());

    /**
    * @param[in]  content_type QString [required]
    * @param[in]  accept QString [required]
    * @param[in]  order_form_id QString [required]
    * @param[in]  oai_items_update_request OAIItemsUpdate_request [required]
    * @param[in]  allowed_outdated_data QList<QJsonValue> [optional]
    */
    virtual void itemsUpdate(const QString &content_type, const QString &accept, const QString &order_form_id, const OAIItemsUpdate_request &oai_items_update_request, const ::OpenAPI::OptionalParam<QList<QJsonValue>> &allowed_outdated_data = ::OpenAPI::OptionalParam<QList<QJsonValue>>());

    /**
    * @param[in]  order_form_id QString [required]
    * @param[in]  item_index QString [required]
    * @param[in]  content_type QString [required]
    * @param[in]  accept QString [required]
    * @param[in]  oai_price_change_request OAIPriceChangeRequest [required]
    */
    virtual void priceChange(const QString &order_form_id, const QString &item_index, const QString &content_type, const QString &accept, const OAIPriceChangeRequest &oai_price_change_request);

    /**
    * @param[in]  order_form_id QString [required]
    * @param[in]  content_type QString [required]
    * @param[in]  accept QString [required]
    * @param[in]  body OAIObject [optional]
    */
    virtual void removeAllItems(const QString &order_form_id, const QString &content_type, const QString &accept, const ::OpenAPI::OptionalParam<OAIObject> &body = ::OpenAPI::OptionalParam<OAIObject>());

    /**
    * @param[in]  content_type QString [required]
    * @param[in]  accept QString [required]
    * @param[in]  order_form_id QString [required]
    */
    virtual void removeallpersonaldata(const QString &content_type, const QString &accept, const QString &order_form_id);


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

    void addCouponsCallback(OAIHttpRequestWorker *worker);
    void cartSimulationCallback(OAIHttpRequestWorker *worker);
    void createANewCartCallback(OAIHttpRequestWorker *worker);
    void getCartInformationByIdCallback(OAIHttpRequestWorker *worker);
    void getCartInstallmentsCallback(OAIHttpRequestWorker *worker);
    void ignoreProfileDataCallback(OAIHttpRequestWorker *worker);
    void itemsCallback(OAIHttpRequestWorker *worker);
    void itemsUpdateCallback(OAIHttpRequestWorker *worker);
    void priceChangeCallback(OAIHttpRequestWorker *worker);
    void removeAllItemsCallback(OAIHttpRequestWorker *worker);
    void removeallpersonaldataCallback(OAIHttpRequestWorker *worker);

Q_SIGNALS:

    void addCouponsSignal(OAIAddCoupons_200_response summary);
    void cartSimulationSignal(OAICartSimulation_200_response summary);
    void createANewCartSignal();
    void getCartInformationByIdSignal();
    void getCartInstallmentsSignal();
    void ignoreProfileDataSignal();
    void itemsSignal(OAIItems_200_response summary);
    void itemsUpdateSignal(OAIItemsUpdate_200_response summary);
    void priceChangeSignal();
    void removeAllItemsSignal(OAIObject summary);
    void removeallpersonaldataSignal(OAIObject summary);


    void addCouponsSignalFull(OAIHttpRequestWorker *worker, OAIAddCoupons_200_response summary);
    void cartSimulationSignalFull(OAIHttpRequestWorker *worker, OAICartSimulation_200_response summary);
    void createANewCartSignalFull(OAIHttpRequestWorker *worker);
    void getCartInformationByIdSignalFull(OAIHttpRequestWorker *worker);
    void getCartInstallmentsSignalFull(OAIHttpRequestWorker *worker);
    void ignoreProfileDataSignalFull(OAIHttpRequestWorker *worker);
    void itemsSignalFull(OAIHttpRequestWorker *worker, OAIItems_200_response summary);
    void itemsUpdateSignalFull(OAIHttpRequestWorker *worker, OAIItemsUpdate_200_response summary);
    void priceChangeSignalFull(OAIHttpRequestWorker *worker);
    void removeAllItemsSignalFull(OAIHttpRequestWorker *worker, OAIObject summary);
    void removeallpersonaldataSignalFull(OAIHttpRequestWorker *worker, OAIObject summary);

    Q_DECL_DEPRECATED_X("Use addCouponsSignalError() instead")
    void addCouponsSignalE(OAIAddCoupons_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void addCouponsSignalError(OAIAddCoupons_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use cartSimulationSignalError() instead")
    void cartSimulationSignalE(OAICartSimulation_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void cartSimulationSignalError(OAICartSimulation_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use createANewCartSignalError() instead")
    void createANewCartSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void createANewCartSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getCartInformationByIdSignalError() instead")
    void getCartInformationByIdSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void getCartInformationByIdSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getCartInstallmentsSignalError() instead")
    void getCartInstallmentsSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void getCartInstallmentsSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use ignoreProfileDataSignalError() instead")
    void ignoreProfileDataSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void ignoreProfileDataSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use itemsSignalError() instead")
    void itemsSignalE(OAIItems_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void itemsSignalError(OAIItems_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use itemsUpdateSignalError() instead")
    void itemsUpdateSignalE(OAIItemsUpdate_200_response summary, QNetworkReply::NetworkError error_type, QString error_str);
    void itemsUpdateSignalError(OAIItemsUpdate_200_response summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use priceChangeSignalError() instead")
    void priceChangeSignalE(QNetworkReply::NetworkError error_type, QString error_str);
    void priceChangeSignalError(QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use removeAllItemsSignalError() instead")
    void removeAllItemsSignalE(OAIObject summary, QNetworkReply::NetworkError error_type, QString error_str);
    void removeAllItemsSignalError(OAIObject summary, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use removeallpersonaldataSignalError() instead")
    void removeallpersonaldataSignalE(OAIObject summary, QNetworkReply::NetworkError error_type, QString error_str);
    void removeallpersonaldataSignalError(OAIObject summary, QNetworkReply::NetworkError error_type, const QString &error_str);

    Q_DECL_DEPRECATED_X("Use addCouponsSignalErrorFull() instead")
    void addCouponsSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void addCouponsSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use cartSimulationSignalErrorFull() instead")
    void cartSimulationSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void cartSimulationSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use createANewCartSignalErrorFull() instead")
    void createANewCartSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void createANewCartSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getCartInformationByIdSignalErrorFull() instead")
    void getCartInformationByIdSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getCartInformationByIdSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use getCartInstallmentsSignalErrorFull() instead")
    void getCartInstallmentsSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void getCartInstallmentsSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use ignoreProfileDataSignalErrorFull() instead")
    void ignoreProfileDataSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void ignoreProfileDataSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use itemsSignalErrorFull() instead")
    void itemsSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void itemsSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use itemsUpdateSignalErrorFull() instead")
    void itemsUpdateSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void itemsUpdateSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use priceChangeSignalErrorFull() instead")
    void priceChangeSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void priceChangeSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use removeAllItemsSignalErrorFull() instead")
    void removeAllItemsSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void removeAllItemsSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);
    Q_DECL_DEPRECATED_X("Use removeallpersonaldataSignalErrorFull() instead")
    void removeallpersonaldataSignalEFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, QString error_str);
    void removeallpersonaldataSignalErrorFull(OAIHttpRequestWorker *worker, QNetworkReply::NetworkError error_type, const QString &error_str);

    void abortRequestsSignal();
    void allPendingRequestsCompleted();

public Q_SLOTS:
    void tokenAvailable();
};

} // namespace OpenAPI
#endif
