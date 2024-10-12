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

#include "OAICartAttachmentsApi.h"
#include "OAIServerConfiguration.h"
#include <QJsonArray>
#include <QJsonDocument>

namespace OpenAPI {

OAICartAttachmentsApi::OAICartAttachmentsApi(const int timeOut)
    : _timeOut(timeOut),
      _manager(nullptr),
      _isResponseCompressionEnabled(false),
      _isRequestCompressionEnabled(false) {
    initializeServerConfigs();
}

OAICartAttachmentsApi::~OAICartAttachmentsApi() {
}

void OAICartAttachmentsApi::initializeServerConfigs() {
    //Default server
    QList<OAIServerConfiguration> defaultConf = QList<OAIServerConfiguration>();
    //varying endpoint server
    defaultConf.append(OAIServerConfiguration(
    QUrl("https://vtex.local"),
    "No description provided",
    QMap<QString, OAIServerVariable>()));
    defaultConf.append(OAIServerConfiguration(
    QUrl("https://{accountName}.{environment}.com.br"),
    "VTEX server url",
    QMap<QString, OAIServerVariable>{ 
    {"accountName", OAIServerVariable("Name of the VTEX account. Used as part of the URL","{accountName}",
    QSet<QString>{ {"{accountName}"} })},
    
    {"environment", OAIServerVariable("Environment to use. Used as part of the URL.","{environment}",
    QSet<QString>{ {"{environment}"} })}, }));
    
    _serverConfigs.insert("addClientPreferences", defaultConf);
    _serverIndices.insert("addClientPreferences", 0);
    _serverConfigs.insert("addClientProfile", defaultConf);
    _serverIndices.insert("addClientProfile", 0);
    _serverConfigs.insert("addMarketingData", defaultConf);
    _serverIndices.insert("addMarketingData", 0);
    _serverConfigs.insert("addMerchantContextData", defaultConf);
    _serverIndices.insert("addMerchantContextData", 0);
    _serverConfigs.insert("addPaymentData", defaultConf);
    _serverIndices.insert("addPaymentData", 0);
    _serverConfigs.insert("addShippingAddress", defaultConf);
    _serverIndices.insert("addShippingAddress", 0);
    _serverConfigs.insert("getClientProfileByEmail", defaultConf);
    _serverIndices.insert("getClientProfileByEmail", 0);
}

/**
* returns 0 on success and -1, -2 or -3 on failure.
* -1 when the variable does not exist and -2 if the value is not defined in the enum and -3 if the operation or server index is not found
*/
int OAICartAttachmentsApi::setDefaultServerValue(int serverIndex, const QString &operation, const QString &variable, const QString &value) {
    auto it = _serverConfigs.find(operation);
    if (it != _serverConfigs.end() && serverIndex < it.value().size()) {
      return _serverConfigs[operation][serverIndex].setDefaultValue(variable,value);
    }
    return -3;
}
void OAICartAttachmentsApi::setServerIndex(const QString &operation, int serverIndex) {
    if (_serverIndices.contains(operation) && serverIndex < _serverConfigs.find(operation).value().size()) {
        _serverIndices[operation] = serverIndex;
    }
}

void OAICartAttachmentsApi::setApiKey(const QString &apiKeyName, const QString &apiKey) {
    _apiKeys.insert(apiKeyName, apiKey);
}

void OAICartAttachmentsApi::setBearerToken(const QString &token) {
    _bearerToken = token;
}

void OAICartAttachmentsApi::setUsername(const QString &username) {
    _username = username;
}

void OAICartAttachmentsApi::setPassword(const QString &password) {
    _password = password;
}


void OAICartAttachmentsApi::setTimeOut(const int timeOut) {
    _timeOut = timeOut;
}

void OAICartAttachmentsApi::setWorkingDirectory(const QString &path) {
    _workingDirectory = path;
}

void OAICartAttachmentsApi::setNetworkAccessManager(QNetworkAccessManager* manager) {
    _manager = manager;
}

/**
    * Appends a new ServerConfiguration to the config map for a specific operation.
    * @param operation The id to the target operation.
    * @param url A string that contains the URL of the server
    * @param description A String that describes the server
    * @param variables A map between a variable name and its value. The value is used for substitution in the server's URL template.
    * returns the index of the new server config on success and -1 if the operation is not found
    */
int OAICartAttachmentsApi::addServerConfiguration(const QString &operation, const QUrl &url, const QString &description, const QMap<QString, OAIServerVariable> &variables) {
    if (_serverConfigs.contains(operation)) {
        _serverConfigs[operation].append(OAIServerConfiguration(
                    url,
                    description,
                    variables));
        return _serverConfigs[operation].size()-1;
    } else {
        return -1;
    }
}

/**
    * Appends a new ServerConfiguration to the config map for a all operations and sets the index to that server.
    * @param url A string that contains the URL of the server
    * @param description A String that describes the server
    * @param variables A map between a variable name and its value. The value is used for substitution in the server's URL template.
    */
void OAICartAttachmentsApi::setNewServerForAllOperations(const QUrl &url, const QString &description, const QMap<QString, OAIServerVariable> &variables) {
    for (auto keyIt = _serverIndices.keyBegin(); keyIt != _serverIndices.keyEnd(); keyIt++) {
        setServerIndex(*keyIt, addServerConfiguration(*keyIt, url, description, variables));
    }
}

/**
    * Appends a new ServerConfiguration to the config map for an operations and sets the index to that server.
    * @param URL A string that contains the URL of the server
    * @param description A String that describes the server
    * @param variables A map between a variable name and its value. The value is used for substitution in the server's URL template.
    */
void OAICartAttachmentsApi::setNewServer(const QString &operation, const QUrl &url, const QString &description, const QMap<QString, OAIServerVariable> &variables) {
    setServerIndex(operation, addServerConfiguration(operation, url, description, variables));
}

void OAICartAttachmentsApi::addHeaders(const QString &key, const QString &value) {
    _defaultHeaders.insert(key, value);
}

void OAICartAttachmentsApi::enableRequestCompression() {
    _isRequestCompressionEnabled = true;
}

void OAICartAttachmentsApi::enableResponseCompression() {
    _isResponseCompressionEnabled = true;
}

void OAICartAttachmentsApi::abortRequests() {
    Q_EMIT abortRequestsSignal();
}

QString OAICartAttachmentsApi::getParamStylePrefix(const QString &style) {
    if (style == "matrix") {
        return ";";
    } else if (style == "label") {
        return ".";
    } else if (style == "form") {
        return "&";
    } else if (style == "simple") {
        return "";
    } else if (style == "spaceDelimited") {
        return "&";
    } else if (style == "pipeDelimited") {
        return "&";
    } else {
        return "none";
    }
}

QString OAICartAttachmentsApi::getParamStyleSuffix(const QString &style) {
    if (style == "matrix") {
        return "=";
    } else if (style == "label") {
        return "";
    } else if (style == "form") {
        return "=";
    } else if (style == "simple") {
        return "";
    } else if (style == "spaceDelimited") {
        return "=";
    } else if (style == "pipeDelimited") {
        return "=";
    } else {
        return "none";
    }
}

QString OAICartAttachmentsApi::getParamStyleDelimiter(const QString &style, const QString &name, bool isExplode) {

    if (style == "matrix") {
        return (isExplode) ? ";" + name + "=" : ",";

    } else if (style == "label") {
        return (isExplode) ? "." : ",";

    } else if (style == "form") {
        return (isExplode) ? "&" + name + "=" : ",";

    } else if (style == "simple") {
        return ",";
    } else if (style == "spaceDelimited") {
        return (isExplode) ? "&" + name + "=" : " ";

    } else if (style == "pipeDelimited") {
        return (isExplode) ? "&" + name + "=" : "|";

    } else if (style == "deepObject") {
        return (isExplode) ? "&" : "none";

    } else {
        return "none";
    }
}

void OAICartAttachmentsApi::addClientPreferences(const QString &content_type, const QString &accept, const QString &order_form_id, const OAIAddClientPreferences_request &oai_add_client_preferences_request) {
    QString fullPath = QString(_serverConfigs["addClientPreferences"][_serverIndices.value("addClientPreferences")].URL()+"/api/checkout/pub/orderForm/{orderFormId}/attachments/clientPreferencesData");
    
    
    {
        QString order_form_idPathParam("{");
        order_form_idPathParam.append("orderFormId").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "orderFormId", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"orderFormId"+pathSuffix : pathPrefix;
        fullPath.replace(order_form_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(order_form_id)));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_add_client_preferences_request.asJson().toUtf8();
        input.request_body.append(output);
    }
    
    {
        if (!::OpenAPI::toStringValue(content_type).isEmpty()) {
            input.headers.insert("Content-Type", ::OpenAPI::toStringValue(content_type));
        }
        }
    
    {
        if (!::OpenAPI::toStringValue(accept).isEmpty()) {
            input.headers.insert("Accept", ::OpenAPI::toStringValue(accept));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAICartAttachmentsApi::addClientPreferencesCallback);
    connect(this, &OAICartAttachmentsApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAICartAttachmentsApi::addClientPreferencesCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    QJsonValue output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT addClientPreferencesSignal(output);
        Q_EMIT addClientPreferencesSignalFull(worker, output);
    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT addClientPreferencesSignalE(output, error_type, error_str);
        Q_EMIT addClientPreferencesSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT addClientPreferencesSignalError(output, error_type, error_str);
        Q_EMIT addClientPreferencesSignalErrorFull(worker, error_type, error_str);
    }
}

void OAICartAttachmentsApi::addClientProfile(const QString &content_type, const QString &accept, const QString &order_form_id, const OAIAddClientProfile_request &oai_add_client_profile_request) {
    QString fullPath = QString(_serverConfigs["addClientProfile"][_serverIndices.value("addClientProfile")].URL()+"/api/checkout/pub/orderForm/{orderFormId}/attachments/clientProfileData");
    
    
    {
        QString order_form_idPathParam("{");
        order_form_idPathParam.append("orderFormId").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "orderFormId", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"orderFormId"+pathSuffix : pathPrefix;
        fullPath.replace(order_form_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(order_form_id)));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_add_client_profile_request.asJson().toUtf8();
        input.request_body.append(output);
    }
    
    {
        if (!::OpenAPI::toStringValue(content_type).isEmpty()) {
            input.headers.insert("Content-Type", ::OpenAPI::toStringValue(content_type));
        }
        }
    
    {
        if (!::OpenAPI::toStringValue(accept).isEmpty()) {
            input.headers.insert("Accept", ::OpenAPI::toStringValue(accept));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAICartAttachmentsApi::addClientProfileCallback);
    connect(this, &OAICartAttachmentsApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAICartAttachmentsApi::addClientProfileCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT addClientProfileSignal();
        Q_EMIT addClientProfileSignalFull(worker);
    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT addClientProfileSignalE(error_type, error_str);
        Q_EMIT addClientProfileSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT addClientProfileSignalError(error_type, error_str);
        Q_EMIT addClientProfileSignalErrorFull(worker, error_type, error_str);
    }
}

void OAICartAttachmentsApi::addMarketingData(const QString &content_type, const QString &accept, const QString &order_form_id, const OAIAddMarketingData_request &oai_add_marketing_data_request) {
    QString fullPath = QString(_serverConfigs["addMarketingData"][_serverIndices.value("addMarketingData")].URL()+"/api/checkout/pub/orderForm/{orderFormId}/attachments/marketingData");
    
    
    {
        QString order_form_idPathParam("{");
        order_form_idPathParam.append("orderFormId").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "orderFormId", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"orderFormId"+pathSuffix : pathPrefix;
        fullPath.replace(order_form_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(order_form_id)));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_add_marketing_data_request.asJson().toUtf8();
        input.request_body.append(output);
    }
    
    {
        if (!::OpenAPI::toStringValue(content_type).isEmpty()) {
            input.headers.insert("Content-Type", ::OpenAPI::toStringValue(content_type));
        }
        }
    
    {
        if (!::OpenAPI::toStringValue(accept).isEmpty()) {
            input.headers.insert("Accept", ::OpenAPI::toStringValue(accept));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAICartAttachmentsApi::addMarketingDataCallback);
    connect(this, &OAICartAttachmentsApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAICartAttachmentsApi::addMarketingDataCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT addMarketingDataSignal();
        Q_EMIT addMarketingDataSignalFull(worker);
    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT addMarketingDataSignalE(error_type, error_str);
        Q_EMIT addMarketingDataSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT addMarketingDataSignalError(error_type, error_str);
        Q_EMIT addMarketingDataSignalErrorFull(worker, error_type, error_str);
    }
}

void OAICartAttachmentsApi::addMerchantContextData(const QString &content_type, const QString &accept, const QString &order_form_id, const OAIAddMerchantContextData_request &oai_add_merchant_context_data_request) {
    QString fullPath = QString(_serverConfigs["addMerchantContextData"][_serverIndices.value("addMerchantContextData")].URL()+"/api/checkout/pub/orderForm/{orderFormId}/attachments/merchantContextData");
    
    
    {
        QString order_form_idPathParam("{");
        order_form_idPathParam.append("orderFormId").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "orderFormId", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"orderFormId"+pathSuffix : pathPrefix;
        fullPath.replace(order_form_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(order_form_id)));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_add_merchant_context_data_request.asJson().toUtf8();
        input.request_body.append(output);
    }
    
    {
        if (!::OpenAPI::toStringValue(content_type).isEmpty()) {
            input.headers.insert("Content-Type", ::OpenAPI::toStringValue(content_type));
        }
        }
    
    {
        if (!::OpenAPI::toStringValue(accept).isEmpty()) {
            input.headers.insert("Accept", ::OpenAPI::toStringValue(accept));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAICartAttachmentsApi::addMerchantContextDataCallback);
    connect(this, &OAICartAttachmentsApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAICartAttachmentsApi::addMerchantContextDataCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIAddMerchantContextData_200_response output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT addMerchantContextDataSignal(output);
        Q_EMIT addMerchantContextDataSignalFull(worker, output);
    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT addMerchantContextDataSignalE(output, error_type, error_str);
        Q_EMIT addMerchantContextDataSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT addMerchantContextDataSignalError(output, error_type, error_str);
        Q_EMIT addMerchantContextDataSignalErrorFull(worker, error_type, error_str);
    }
}

void OAICartAttachmentsApi::addPaymentData(const QString &content_type, const QString &accept, const QString &order_form_id, const OAIAddPaymentData_request &oai_add_payment_data_request) {
    QString fullPath = QString(_serverConfigs["addPaymentData"][_serverIndices.value("addPaymentData")].URL()+"/api/checkout/pub/orderForm/{orderFormId}/attachments/paymentData");
    
    
    {
        QString order_form_idPathParam("{");
        order_form_idPathParam.append("orderFormId").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "orderFormId", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"orderFormId"+pathSuffix : pathPrefix;
        fullPath.replace(order_form_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(order_form_id)));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_add_payment_data_request.asJson().toUtf8();
        input.request_body.append(output);
    }
    
    {
        if (!::OpenAPI::toStringValue(content_type).isEmpty()) {
            input.headers.insert("Content-Type", ::OpenAPI::toStringValue(content_type));
        }
        }
    
    {
        if (!::OpenAPI::toStringValue(accept).isEmpty()) {
            input.headers.insert("Accept", ::OpenAPI::toStringValue(accept));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAICartAttachmentsApi::addPaymentDataCallback);
    connect(this, &OAICartAttachmentsApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAICartAttachmentsApi::addPaymentDataCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT addPaymentDataSignal();
        Q_EMIT addPaymentDataSignalFull(worker);
    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT addPaymentDataSignalE(error_type, error_str);
        Q_EMIT addPaymentDataSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT addPaymentDataSignalError(error_type, error_str);
        Q_EMIT addPaymentDataSignalErrorFull(worker, error_type, error_str);
    }
}

void OAICartAttachmentsApi::addShippingAddress(const QString &content_type, const QString &accept, const QString &order_form_id, const OAIAddShippingAddress_request &oai_add_shipping_address_request) {
    QString fullPath = QString(_serverConfigs["addShippingAddress"][_serverIndices.value("addShippingAddress")].URL()+"/api/checkout/pub/orderForm/{orderFormId}/attachments/shippingData");
    
    
    {
        QString order_form_idPathParam("{");
        order_form_idPathParam.append("orderFormId").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "orderFormId", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"orderFormId"+pathSuffix : pathPrefix;
        fullPath.replace(order_form_idPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(order_form_id)));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_add_shipping_address_request.asJson().toUtf8();
        input.request_body.append(output);
    }
    
    {
        if (!::OpenAPI::toStringValue(content_type).isEmpty()) {
            input.headers.insert("Content-Type", ::OpenAPI::toStringValue(content_type));
        }
        }
    
    {
        if (!::OpenAPI::toStringValue(accept).isEmpty()) {
            input.headers.insert("Accept", ::OpenAPI::toStringValue(accept));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAICartAttachmentsApi::addShippingAddressCallback);
    connect(this, &OAICartAttachmentsApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAICartAttachmentsApi::addShippingAddressCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT addShippingAddressSignal();
        Q_EMIT addShippingAddressSignalFull(worker);
    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT addShippingAddressSignalE(error_type, error_str);
        Q_EMIT addShippingAddressSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT addShippingAddressSignalError(error_type, error_str);
        Q_EMIT addShippingAddressSignalErrorFull(worker, error_type, error_str);
    }
}

void OAICartAttachmentsApi::getClientProfileByEmail(const QString &content_type, const QString &accept, const QString &email) {
    QString fullPath = QString(_serverConfigs["getClientProfileByEmail"][_serverIndices.value("getClientProfileByEmail")].URL()+"/api/checkout/pub/profiles");
    
    QString queryPrefix, querySuffix, queryDelimiter, queryStyle;
    
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "email", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("email")).append(querySuffix).append(QUrl::toPercentEncoding(email));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "GET");


    
    {
        if (!::OpenAPI::toStringValue(content_type).isEmpty()) {
            input.headers.insert("Content-Type", ::OpenAPI::toStringValue(content_type));
        }
        }
    
    {
        if (!::OpenAPI::toStringValue(accept).isEmpty()) {
            input.headers.insert("Accept", ::OpenAPI::toStringValue(accept));
        }
        }
    for (auto keyValueIt = _defaultHeaders.keyValueBegin(); keyValueIt != _defaultHeaders.keyValueEnd(); keyValueIt++) {
        input.headers.insert(keyValueIt->first, keyValueIt->second);
    }


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAICartAttachmentsApi::getClientProfileByEmailCallback);
    connect(this, &OAICartAttachmentsApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAICartAttachmentsApi::getClientProfileByEmailCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIGetClientProfileByEmail_200_response output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT getClientProfileByEmailSignal(output);
        Q_EMIT getClientProfileByEmailSignalFull(worker, output);
    } else {

#if defined(_MSC_VER)
// For MSVC
#pragma warning(push)
#pragma warning(disable : 4996)
#elif defined(__clang__)
// For Clang
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wdeprecated-declarations"
#elif defined(__GNUC__)
// For GCC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

        Q_EMIT getClientProfileByEmailSignalE(output, error_type, error_str);
        Q_EMIT getClientProfileByEmailSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT getClientProfileByEmailSignalError(output, error_type, error_str);
        Q_EMIT getClientProfileByEmailSignalErrorFull(worker, error_type, error_str);
    }
}

void OAICartAttachmentsApi::tokenAvailable(){

    oauthToken token;
    switch (_OauthMethod) {
    case 1: //implicit flow
        token = _implicitFlow.getToken(_latestScope.join(" "));
        if(token.isValid()){
            _latestInput.headers.insert("Authorization", "Bearer " + token.getToken());
            _latestWorker->execute(&_latestInput);
        }else{
            _implicitFlow.removeToken(_latestScope.join(" "));
            qDebug() << "Could not retrieve a valid token";
        }
        break;
    case 2: //authorization flow
        token = _authFlow.getToken(_latestScope.join(" "));
        if(token.isValid()){
            _latestInput.headers.insert("Authorization", "Bearer " + token.getToken());
            _latestWorker->execute(&_latestInput);
        }else{
            _authFlow.removeToken(_latestScope.join(" "));
            qDebug() << "Could not retrieve a valid token";
        }
        break;
    case 3: //client credentials flow
        token = _credentialFlow.getToken(_latestScope.join(" "));
        if(token.isValid()){
            _latestInput.headers.insert("Authorization", "Bearer " + token.getToken());
            _latestWorker->execute(&_latestInput);
        }else{
            _credentialFlow.removeToken(_latestScope.join(" "));
            qDebug() << "Could not retrieve a valid token";
        }
        break;
    case 4: //resource owner password flow
        token = _passwordFlow.getToken(_latestScope.join(" "));
        if(token.isValid()){
            _latestInput.headers.insert("Authorization", "Bearer " + token.getToken());
            _latestWorker->execute(&_latestInput);
        }else{
            _credentialFlow.removeToken(_latestScope.join(" "));
            qDebug() << "Could not retrieve a valid token";
        }
        break;
    default:
        qDebug() << "No Oauth method set!";
        break;
    }
}
} // namespace OpenAPI
