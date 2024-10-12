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

#include "OAIShoppingCartApi.h"
#include "OAIServerConfiguration.h"
#include <QJsonArray>
#include <QJsonDocument>

namespace OpenAPI {

OAIShoppingCartApi::OAIShoppingCartApi(const int timeOut)
    : _timeOut(timeOut),
      _manager(nullptr),
      _isResponseCompressionEnabled(false),
      _isRequestCompressionEnabled(false) {
    initializeServerConfigs();
}

OAIShoppingCartApi::~OAIShoppingCartApi() {
}

void OAIShoppingCartApi::initializeServerConfigs() {
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
    
    _serverConfigs.insert("addCoupons", defaultConf);
    _serverIndices.insert("addCoupons", 0);
    _serverConfigs.insert("cartSimulation", defaultConf);
    _serverIndices.insert("cartSimulation", 0);
    _serverConfigs.insert("createANewCart", defaultConf);
    _serverIndices.insert("createANewCart", 0);
    _serverConfigs.insert("getCartInformationById", defaultConf);
    _serverIndices.insert("getCartInformationById", 0);
    _serverConfigs.insert("getCartInstallments", defaultConf);
    _serverIndices.insert("getCartInstallments", 0);
    _serverConfigs.insert("ignoreProfileData", defaultConf);
    _serverIndices.insert("ignoreProfileData", 0);
    _serverConfigs.insert("items", defaultConf);
    _serverIndices.insert("items", 0);
    _serverConfigs.insert("itemsUpdate", defaultConf);
    _serverIndices.insert("itemsUpdate", 0);
    _serverConfigs.insert("priceChange", defaultConf);
    _serverIndices.insert("priceChange", 0);
    _serverConfigs.insert("removeAllItems", defaultConf);
    _serverIndices.insert("removeAllItems", 0);
    _serverConfigs.insert("removeallpersonaldata", defaultConf);
    _serverIndices.insert("removeallpersonaldata", 0);
}

/**
* returns 0 on success and -1, -2 or -3 on failure.
* -1 when the variable does not exist and -2 if the value is not defined in the enum and -3 if the operation or server index is not found
*/
int OAIShoppingCartApi::setDefaultServerValue(int serverIndex, const QString &operation, const QString &variable, const QString &value) {
    auto it = _serverConfigs.find(operation);
    if (it != _serverConfigs.end() && serverIndex < it.value().size()) {
      return _serverConfigs[operation][serverIndex].setDefaultValue(variable,value);
    }
    return -3;
}
void OAIShoppingCartApi::setServerIndex(const QString &operation, int serverIndex) {
    if (_serverIndices.contains(operation) && serverIndex < _serverConfigs.find(operation).value().size()) {
        _serverIndices[operation] = serverIndex;
    }
}

void OAIShoppingCartApi::setApiKey(const QString &apiKeyName, const QString &apiKey) {
    _apiKeys.insert(apiKeyName, apiKey);
}

void OAIShoppingCartApi::setBearerToken(const QString &token) {
    _bearerToken = token;
}

void OAIShoppingCartApi::setUsername(const QString &username) {
    _username = username;
}

void OAIShoppingCartApi::setPassword(const QString &password) {
    _password = password;
}


void OAIShoppingCartApi::setTimeOut(const int timeOut) {
    _timeOut = timeOut;
}

void OAIShoppingCartApi::setWorkingDirectory(const QString &path) {
    _workingDirectory = path;
}

void OAIShoppingCartApi::setNetworkAccessManager(QNetworkAccessManager* manager) {
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
int OAIShoppingCartApi::addServerConfiguration(const QString &operation, const QUrl &url, const QString &description, const QMap<QString, OAIServerVariable> &variables) {
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
void OAIShoppingCartApi::setNewServerForAllOperations(const QUrl &url, const QString &description, const QMap<QString, OAIServerVariable> &variables) {
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
void OAIShoppingCartApi::setNewServer(const QString &operation, const QUrl &url, const QString &description, const QMap<QString, OAIServerVariable> &variables) {
    setServerIndex(operation, addServerConfiguration(operation, url, description, variables));
}

void OAIShoppingCartApi::addHeaders(const QString &key, const QString &value) {
    _defaultHeaders.insert(key, value);
}

void OAIShoppingCartApi::enableRequestCompression() {
    _isRequestCompressionEnabled = true;
}

void OAIShoppingCartApi::enableResponseCompression() {
    _isResponseCompressionEnabled = true;
}

void OAIShoppingCartApi::abortRequests() {
    Q_EMIT abortRequestsSignal();
}

QString OAIShoppingCartApi::getParamStylePrefix(const QString &style) {
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

QString OAIShoppingCartApi::getParamStyleSuffix(const QString &style) {
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

QString OAIShoppingCartApi::getParamStyleDelimiter(const QString &style, const QString &name, bool isExplode) {

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

void OAIShoppingCartApi::addCoupons(const QString &order_form_id, const QString &content_type, const QString &accept, const OAIAddCoupons_request &oai_add_coupons_request) {
    QString fullPath = QString(_serverConfigs["addCoupons"][_serverIndices.value("addCoupons")].URL()+"/api/checkout/pub/orderForm/{orderFormId}/coupons");
    
    
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

        
        QByteArray output = oai_add_coupons_request.asJson().toUtf8();
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


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIShoppingCartApi::addCouponsCallback);
    connect(this, &OAIShoppingCartApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIShoppingCartApi::addCouponsCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIAddCoupons_200_response output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT addCouponsSignal(output);
        Q_EMIT addCouponsSignalFull(worker, output);
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

        Q_EMIT addCouponsSignalE(output, error_type, error_str);
        Q_EMIT addCouponsSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT addCouponsSignalError(output, error_type, error_str);
        Q_EMIT addCouponsSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIShoppingCartApi::cartSimulation(const QString &content_type, const QString &accept, const ::OpenAPI::OptionalParam<qint32> &rnb_behavior, const ::OpenAPI::OptionalParam<qint32> &sc, const ::OpenAPI::OptionalParam<OAICartSimulation_request> &oai_cart_simulation_request) {
    QString fullPath = QString(_serverConfigs["cartSimulation"][_serverIndices.value("cartSimulation")].URL()+"/api/checkout/pub/orderForms/simulation");
    
    QString queryPrefix, querySuffix, queryDelimiter, queryStyle;
    if (rnb_behavior.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "RnbBehavior", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("RnbBehavior")).append(querySuffix).append(QUrl::toPercentEncoding(rnb_behavior.stringValue()));
    }
    if (sc.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "sc", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("sc")).append(querySuffix).append(QUrl::toPercentEncoding(sc.stringValue()));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    if (oai_cart_simulation_request.hasValue()){

        
        QByteArray output = oai_cart_simulation_request.value().asJson().toUtf8();
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


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIShoppingCartApi::cartSimulationCallback);
    connect(this, &OAIShoppingCartApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIShoppingCartApi::cartSimulationCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAICartSimulation_200_response output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT cartSimulationSignal(output);
        Q_EMIT cartSimulationSignalFull(worker, output);
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

        Q_EMIT cartSimulationSignalE(output, error_type, error_str);
        Q_EMIT cartSimulationSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT cartSimulationSignalError(output, error_type, error_str);
        Q_EMIT cartSimulationSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIShoppingCartApi::createANewCart(const QString &content_type, const QString &accept, const ::OpenAPI::OptionalParam<bool> &force_new_cart) {
    QString fullPath = QString(_serverConfigs["createANewCart"][_serverIndices.value("createANewCart")].URL()+"/api/checkout/pub/orderForm");
    
    QString queryPrefix, querySuffix, queryDelimiter, queryStyle;
    if (force_new_cart.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "forceNewCart", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("forceNewCart")).append(querySuffix).append(QUrl::toPercentEncoding(force_new_cart.stringValue()));
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


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIShoppingCartApi::createANewCartCallback);
    connect(this, &OAIShoppingCartApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIShoppingCartApi::createANewCartCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT createANewCartSignal();
        Q_EMIT createANewCartSignalFull(worker);
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

        Q_EMIT createANewCartSignalE(error_type, error_str);
        Q_EMIT createANewCartSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT createANewCartSignalError(error_type, error_str);
        Q_EMIT createANewCartSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIShoppingCartApi::getCartInformationById(const QString &order_form_id, const QString &content_type, const QString &accept, const ::OpenAPI::OptionalParam<bool> &refresh_outdated_data) {
    QString fullPath = QString(_serverConfigs["getCartInformationById"][_serverIndices.value("getCartInformationById")].URL()+"/api/checkout/pub/orderForm/{orderFormId}");
    
    
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
    QString queryPrefix, querySuffix, queryDelimiter, queryStyle;
    if (refresh_outdated_data.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "refreshOutdatedData", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("refreshOutdatedData")).append(querySuffix).append(QUrl::toPercentEncoding(refresh_outdated_data.stringValue()));
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


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIShoppingCartApi::getCartInformationByIdCallback);
    connect(this, &OAIShoppingCartApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIShoppingCartApi::getCartInformationByIdCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT getCartInformationByIdSignal();
        Q_EMIT getCartInformationByIdSignalFull(worker);
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

        Q_EMIT getCartInformationByIdSignalE(error_type, error_str);
        Q_EMIT getCartInformationByIdSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT getCartInformationByIdSignalError(error_type, error_str);
        Q_EMIT getCartInformationByIdSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIShoppingCartApi::getCartInstallments(const QString &order_form_id, const qint32 &payment_system, const QString &content_type, const QString &accept) {
    QString fullPath = QString(_serverConfigs["getCartInstallments"][_serverIndices.value("getCartInstallments")].URL()+"/api/checkout/pub/orderForm/{orderFormId}/installments");
    
    
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
    QString queryPrefix, querySuffix, queryDelimiter, queryStyle;
    
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "paymentSystem", true);
        if (fullPath.indexOf("?") > 0)
            fullPath.append(queryPrefix);
        else
            fullPath.append("?");

        fullPath.append(QUrl::toPercentEncoding("paymentSystem")).append(querySuffix).append(QUrl::toPercentEncoding(payment_system));
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


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIShoppingCartApi::getCartInstallmentsCallback);
    connect(this, &OAIShoppingCartApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIShoppingCartApi::getCartInstallmentsCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT getCartInstallmentsSignal();
        Q_EMIT getCartInstallmentsSignalFull(worker);
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

        Q_EMIT getCartInstallmentsSignalE(error_type, error_str);
        Q_EMIT getCartInstallmentsSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT getCartInstallmentsSignalError(error_type, error_str);
        Q_EMIT getCartInstallmentsSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIShoppingCartApi::ignoreProfileData(const QString &order_form_id, const QString &content_type, const QString &accept, const OAIIgnoreProfileData_request &oai_ignore_profile_data_request) {
    QString fullPath = QString(_serverConfigs["ignoreProfileData"][_serverIndices.value("ignoreProfileData")].URL()+"/api/checkout/pub/orderForm/{orderFormId}/profile");
    
    
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
    OAIHttpRequestInput input(fullPath, "PATCH");

    {

        
        QByteArray output = oai_ignore_profile_data_request.asJson().toUtf8();
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


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIShoppingCartApi::ignoreProfileDataCallback);
    connect(this, &OAIShoppingCartApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIShoppingCartApi::ignoreProfileDataCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT ignoreProfileDataSignal();
        Q_EMIT ignoreProfileDataSignalFull(worker);
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

        Q_EMIT ignoreProfileDataSignalE(error_type, error_str);
        Q_EMIT ignoreProfileDataSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT ignoreProfileDataSignalError(error_type, error_str);
        Q_EMIT ignoreProfileDataSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIShoppingCartApi::items(const QString &content_type, const QString &accept, const QString &order_form_id, const OAIItems_request &oai_items_request, const ::OpenAPI::OptionalParam<QList<QJsonValue>> &allowed_outdated_data) {
    QString fullPath = QString(_serverConfigs["items"][_serverIndices.value("items")].URL()+"/api/checkout/pub/orderForm/{orderFormId}/items");
    
    
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
    QString queryPrefix, querySuffix, queryDelimiter, queryStyle;
    if (allowed_outdated_data.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "allowedOutdatedData", true);
        if (allowed_outdated_data.value().size() > 0) {
            if (QString("multi").indexOf("multi") == 0) {
                for (QJsonValue t : allowed_outdated_data.value()) {
                    if (fullPath.indexOf("?") > 0)
                        fullPath.append(queryPrefix);
                    else
                        fullPath.append("?");
                    fullPath.append("allowedOutdatedData=").append(::OpenAPI::toStringValue(t));
                }
            } else if (QString("multi").indexOf("ssv") == 0) {
                if (fullPath.indexOf("?") > 0)
                    fullPath.append("&");
                else
                    fullPath.append("?").append(queryPrefix).append("allowedOutdatedData").append(querySuffix);
                qint32 count = 0;
                for (QJsonValue t : allowed_outdated_data.value()) {
                    if (count > 0) {
                        fullPath.append((true)? queryDelimiter : QUrl::toPercentEncoding(queryDelimiter));
                    }
                    fullPath.append(::OpenAPI::toStringValue(t));
                    count++;
                }
            } else if (QString("multi").indexOf("tsv") == 0) {
                if (fullPath.indexOf("?") > 0)
                    fullPath.append("&");
                else
                    fullPath.append("?").append(queryPrefix).append("allowedOutdatedData").append(querySuffix);
                qint32 count = 0;
                for (QJsonValue t : allowed_outdated_data.value()) {
                    if (count > 0) {
                        fullPath.append("\t");
                    }
                    fullPath.append(::OpenAPI::toStringValue(t));
                    count++;
                }
            } else if (QString("multi").indexOf("csv") == 0) {
                if (fullPath.indexOf("?") > 0)
                    fullPath.append("&");
                else
                    fullPath.append("?").append(queryPrefix).append("allowedOutdatedData").append(querySuffix);
                qint32 count = 0;
                for (QJsonValue t : allowed_outdated_data.value()) {
                    if (count > 0) {
                        fullPath.append(queryDelimiter);
                    }
                    fullPath.append(::OpenAPI::toStringValue(t));
                    count++;
                }
            } else if (QString("multi").indexOf("pipes") == 0) {
                if (fullPath.indexOf("?") > 0)
                    fullPath.append("&");
                else
                    fullPath.append("?").append(queryPrefix).append("allowedOutdatedData").append(querySuffix);
                qint32 count = 0;
                for (QJsonValue t : allowed_outdated_data.value()) {
                    if (count > 0) {
                        fullPath.append(queryDelimiter);
                    }
                    fullPath.append(::OpenAPI::toStringValue(t));
                    count++;
                }
            } else if (QString("multi").indexOf("deepObject") == 0) {
                if (fullPath.indexOf("?") > 0)
                    fullPath.append("&");
                else
                    fullPath.append("?").append(queryPrefix).append("allowedOutdatedData").append(querySuffix);
                qint32 count = 0;
                for (QJsonValue t : allowed_outdated_data.value()) {
                    if (count > 0) {
                        fullPath.append(queryDelimiter);
                    }
                    fullPath.append(::OpenAPI::toStringValue(t));
                    count++;
                }
            }
        }
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_items_request.asJson().toUtf8();
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


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIShoppingCartApi::itemsCallback);
    connect(this, &OAIShoppingCartApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIShoppingCartApi::itemsCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIItems_200_response output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT itemsSignal(output);
        Q_EMIT itemsSignalFull(worker, output);
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

        Q_EMIT itemsSignalE(output, error_type, error_str);
        Q_EMIT itemsSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT itemsSignalError(output, error_type, error_str);
        Q_EMIT itemsSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIShoppingCartApi::itemsUpdate(const QString &content_type, const QString &accept, const QString &order_form_id, const OAIItemsUpdate_request &oai_items_update_request, const ::OpenAPI::OptionalParam<QList<QJsonValue>> &allowed_outdated_data) {
    QString fullPath = QString(_serverConfigs["itemsUpdate"][_serverIndices.value("itemsUpdate")].URL()+"/api/checkout/pub/orderForm/{orderFormId}/items/update");
    
    
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
    QString queryPrefix, querySuffix, queryDelimiter, queryStyle;
    if (allowed_outdated_data.hasValue())
    {
        queryStyle = "form";
        if (queryStyle == "")
            queryStyle = "form";
        queryPrefix = getParamStylePrefix(queryStyle);
        querySuffix = getParamStyleSuffix(queryStyle);
        queryDelimiter = getParamStyleDelimiter(queryStyle, "allowedOutdatedData", true);
        if (allowed_outdated_data.value().size() > 0) {
            if (QString("multi").indexOf("multi") == 0) {
                for (QJsonValue t : allowed_outdated_data.value()) {
                    if (fullPath.indexOf("?") > 0)
                        fullPath.append(queryPrefix);
                    else
                        fullPath.append("?");
                    fullPath.append("allowedOutdatedData=").append(::OpenAPI::toStringValue(t));
                }
            } else if (QString("multi").indexOf("ssv") == 0) {
                if (fullPath.indexOf("?") > 0)
                    fullPath.append("&");
                else
                    fullPath.append("?").append(queryPrefix).append("allowedOutdatedData").append(querySuffix);
                qint32 count = 0;
                for (QJsonValue t : allowed_outdated_data.value()) {
                    if (count > 0) {
                        fullPath.append((true)? queryDelimiter : QUrl::toPercentEncoding(queryDelimiter));
                    }
                    fullPath.append(::OpenAPI::toStringValue(t));
                    count++;
                }
            } else if (QString("multi").indexOf("tsv") == 0) {
                if (fullPath.indexOf("?") > 0)
                    fullPath.append("&");
                else
                    fullPath.append("?").append(queryPrefix).append("allowedOutdatedData").append(querySuffix);
                qint32 count = 0;
                for (QJsonValue t : allowed_outdated_data.value()) {
                    if (count > 0) {
                        fullPath.append("\t");
                    }
                    fullPath.append(::OpenAPI::toStringValue(t));
                    count++;
                }
            } else if (QString("multi").indexOf("csv") == 0) {
                if (fullPath.indexOf("?") > 0)
                    fullPath.append("&");
                else
                    fullPath.append("?").append(queryPrefix).append("allowedOutdatedData").append(querySuffix);
                qint32 count = 0;
                for (QJsonValue t : allowed_outdated_data.value()) {
                    if (count > 0) {
                        fullPath.append(queryDelimiter);
                    }
                    fullPath.append(::OpenAPI::toStringValue(t));
                    count++;
                }
            } else if (QString("multi").indexOf("pipes") == 0) {
                if (fullPath.indexOf("?") > 0)
                    fullPath.append("&");
                else
                    fullPath.append("?").append(queryPrefix).append("allowedOutdatedData").append(querySuffix);
                qint32 count = 0;
                for (QJsonValue t : allowed_outdated_data.value()) {
                    if (count > 0) {
                        fullPath.append(queryDelimiter);
                    }
                    fullPath.append(::OpenAPI::toStringValue(t));
                    count++;
                }
            } else if (QString("multi").indexOf("deepObject") == 0) {
                if (fullPath.indexOf("?") > 0)
                    fullPath.append("&");
                else
                    fullPath.append("?").append(queryPrefix).append("allowedOutdatedData").append(querySuffix);
                qint32 count = 0;
                for (QJsonValue t : allowed_outdated_data.value()) {
                    if (count > 0) {
                        fullPath.append(queryDelimiter);
                    }
                    fullPath.append(::OpenAPI::toStringValue(t));
                    count++;
                }
            }
        }
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "POST");

    {

        
        QByteArray output = oai_items_update_request.asJson().toUtf8();
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


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIShoppingCartApi::itemsUpdateCallback);
    connect(this, &OAIShoppingCartApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIShoppingCartApi::itemsUpdateCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIItemsUpdate_200_response output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT itemsUpdateSignal(output);
        Q_EMIT itemsUpdateSignalFull(worker, output);
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

        Q_EMIT itemsUpdateSignalE(output, error_type, error_str);
        Q_EMIT itemsUpdateSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT itemsUpdateSignalError(output, error_type, error_str);
        Q_EMIT itemsUpdateSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIShoppingCartApi::priceChange(const QString &order_form_id, const QString &item_index, const QString &content_type, const QString &accept, const OAIPriceChangeRequest &oai_price_change_request) {
    QString fullPath = QString(_serverConfigs["priceChange"][_serverIndices.value("priceChange")].URL()+"/api/checkout/pub/orderForm/{orderFormId}/items/{itemIndex}/price");
    
    if (_apiKeys.contains("appToken")) {
        addHeaders("appToken",_apiKeys.find("appToken").value());
    }
    
    if (_apiKeys.contains("appKey")) {
        addHeaders("appKey",_apiKeys.find("appKey").value());
    }
    
    
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
    
    {
        QString item_indexPathParam("{");
        item_indexPathParam.append("itemIndex").append("}");
        QString pathPrefix, pathSuffix, pathDelimiter;
        QString pathStyle = "simple";
        if (pathStyle == "")
            pathStyle = "simple";
        pathPrefix = getParamStylePrefix(pathStyle);
        pathSuffix = getParamStyleSuffix(pathStyle);
        pathDelimiter = getParamStyleDelimiter(pathStyle, "itemIndex", false);
        QString paramString = (pathStyle == "matrix") ? pathPrefix+"itemIndex"+pathSuffix : pathPrefix;
        fullPath.replace(item_indexPathParam, paramString+QUrl::toPercentEncoding(::OpenAPI::toStringValue(item_index)));
    }
    OAIHttpRequestWorker *worker = new OAIHttpRequestWorker(this, _manager);
    worker->setTimeOut(_timeOut);
    worker->setWorkingDirectory(_workingDirectory);
    OAIHttpRequestInput input(fullPath, "PUT");

    {

        
        QByteArray output = oai_price_change_request.asJson().toUtf8();
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


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIShoppingCartApi::priceChangeCallback);
    connect(this, &OAIShoppingCartApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIShoppingCartApi::priceChangeCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT priceChangeSignal();
        Q_EMIT priceChangeSignalFull(worker);
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

        Q_EMIT priceChangeSignalE(error_type, error_str);
        Q_EMIT priceChangeSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT priceChangeSignalError(error_type, error_str);
        Q_EMIT priceChangeSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIShoppingCartApi::removeAllItems(const QString &order_form_id, const QString &content_type, const QString &accept, const ::OpenAPI::OptionalParam<OAIObject> &body) {
    QString fullPath = QString(_serverConfigs["removeAllItems"][_serverIndices.value("removeAllItems")].URL()+"/api/checkout/pub/orderForm/{orderFormId}/items/removeAll");
    
    
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

    if (body.hasValue()){

        
        QByteArray output = body.value().asJson().toUtf8();
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


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIShoppingCartApi::removeAllItemsCallback);
    connect(this, &OAIShoppingCartApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIShoppingCartApi::removeAllItemsCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIObject output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT removeAllItemsSignal(output);
        Q_EMIT removeAllItemsSignalFull(worker, output);
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

        Q_EMIT removeAllItemsSignalE(output, error_type, error_str);
        Q_EMIT removeAllItemsSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT removeAllItemsSignalError(output, error_type, error_str);
        Q_EMIT removeAllItemsSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIShoppingCartApi::removeallpersonaldata(const QString &content_type, const QString &accept, const QString &order_form_id) {
    QString fullPath = QString(_serverConfigs["removeallpersonaldata"][_serverIndices.value("removeallpersonaldata")].URL()+"/checkout/changeToAnonymousUser/{orderFormId}");
    
    
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


    connect(worker, &OAIHttpRequestWorker::on_execution_finished, this, &OAIShoppingCartApi::removeallpersonaldataCallback);
    connect(this, &OAIShoppingCartApi::abortRequestsSignal, worker, &QObject::deleteLater);
    connect(worker, &QObject::destroyed, this, [this]() {
        if (findChildren<OAIHttpRequestWorker*>().count() == 0) {
            Q_EMIT allPendingRequestsCompleted();
        }
    });

    worker->execute(&input);
}

void OAIShoppingCartApi::removeallpersonaldataCallback(OAIHttpRequestWorker *worker) {
    QString error_str = worker->error_str;
    QNetworkReply::NetworkError error_type = worker->error_type;

    if (worker->error_type != QNetworkReply::NoError) {
        error_str = QString("%1, %2").arg(worker->error_str, QString(worker->response));
    }
    OAIObject output(QString(worker->response));
    worker->deleteLater();

    if (worker->error_type == QNetworkReply::NoError) {
        Q_EMIT removeallpersonaldataSignal(output);
        Q_EMIT removeallpersonaldataSignalFull(worker, output);
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

        Q_EMIT removeallpersonaldataSignalE(output, error_type, error_str);
        Q_EMIT removeallpersonaldataSignalEFull(worker, error_type, error_str);

#if defined(_MSC_VER)
#pragma warning(pop)
#elif defined(__clang__)
#pragma clang diagnostic pop
#elif defined(__GNUC__)
#pragma GCC diagnostic pop
#endif

        Q_EMIT removeallpersonaldataSignalError(output, error_type, error_str);
        Q_EMIT removeallpersonaldataSignalErrorFull(worker, error_type, error_str);
    }
}

void OAIShoppingCartApi::tokenAvailable(){

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
