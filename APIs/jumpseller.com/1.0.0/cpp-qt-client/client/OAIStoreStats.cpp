/**
 * Jumpseller API
 * # Endpoint Structure  All URLs are in the format:   ```text https://api.jumpseller.com/v1/path.json?login=XXXXXX&authtoken=storetoken   ```  The path is prefixed by the API version and the URL takes as parameters the login (your store specific API login) and your authentication token. <br/><br/> ***  # Version  The current version of the API is **v1**.   If we change the API in backward-incompatible ways, we'll increase the version number and maintain stable support for the old urls. <br/><br/> ***  # Authentication  The API uses a token-based authentication with a combination of a login key and an auth token. **Both parameters can be found on the left sidebar of the Account section, accessed from the main menu of your Admin Panel**. The auth token of the user can be reset on the same page.  ![Store Login](/images/support/api/apilogin.png)  The auth token is a **32 characters** string.  If you are developing a Jumpseller App, the authentication should be done using [OAuth-2](/support/oauth-2). Please read the article [Build an App](/support/apps) for more information. <br/><br/> ***  # Curl Examples  To request all the products at your store, you would append the products index path to the base url to create an URL with the format:    ```text https://api.jumpseller.com/v1/products.json?login=XXXXXX&authtoken=XXXXX ```  In curl, you can invoque that URL with:    ```text curl -X GET \"https://api.jumpseller.com/v1/products.json?login=XXXXXX&authtoken=XXXXX\" ```  To create a product, you will include the JSON data and specify the MIME Type:    ```text curl -X POST -d '{ \"product\" : {\"name\": \"My new Product!\", \"price\": 100} }' \"https://api.jumpseller.com/v1/products.json?login=XXXXXX&authtoken=XXXXX\" -H \"Content-Type:application/json\" ```  and to update the product identified with 123:    ```text curl -X PUT -d '{ \"product\" : {\"name\": \"My updated Product!\", \"price\": 99} }' \"https://api.jumpseller.com/v1/products/123.json?login=XXXXXX&authtoken=XXXXX\" -H \"Content-Type:application/json\" ```  or delete it:    ```text curl -X DELETE \"https://api.jumpseller.com/v1/products/123.json?login=XXXXXX&authtoken=XXXXX\" -H \"Content-Type:application/json\" ``` <br/><br/> ***  # PHP Examples  Create a new Product (POST method)  ```php $url = 'https://api.jumpseller.com/v1/products.json?login=XXXXX&authtoken=XXXXX; $ch = curl_init($url); curl_setopt($ch, CURLOPT_RETURNTRANSFER, true); curl_setopt($ch, CURLOPT_HTTPHEADER, array('Content-Type: application/json'));  curl_setopt($ch, CURLOPT_CUSTOMREQUEST, \"POST\"); //post method curl_setopt($ch, CURLOPT_POSTFIELDS, '{ \"product\" : {\"name\": \"My updated Product!\", \"price\": 99} }');  $result = curl_exec($ch); print_r($result); curl_close($ch); ``` <br/><br/> ***  # Plain JSON only. No XML.  * We only support JSON for data serialization. * Our node format has no root element.   * We use snake_case to describe attribute keys (like \"created_at\").   * All empty value are replaced with **null** strings. * All API URLs end in .json to indicate that they accept and return JSON. * POST and PUT methods require you to explicitly state the MIME type of your request's body content as **\"application/json\"**. <br/><br/> ***  # Rate Limit You can perform a maximum of:  + 240 (two hundred forty) requests per minute and + 8 (eight) requests per second   If you exceed this limit, you'll get a 403 Forbidden (Rate Limit Exceeded) response for subsequent requests.    The rate limits apply by IP address and by store. This means that multiple requests on different stores are not counted towards the same rate limit.  This limits are necessary to ensure resources are correctly used. Your application should be aware of this limits and retry any unsuccessful request, check the following Ruby stub:  ```ruby tries = 0; max_tries = 3; begin   HTTParty.send(method, uri) # perform an API call.   sleep 0.5   tries += 1 rescue   unless tries >= max_tries     sleep 1.0 # wait the necessary time before retrying the call again.     retry   end end ```  Finally, you can review the Response Headers of each request:  ```text Jumpseller-PerMinuteRateLimit-Limit: 60   Jumpseller-PerMinuteRateLimit-Remaining: 59 # requests available on the per-second interval   Jumpseller-PerSecondRateLimit-Limit: 2   Jumpseller-PerSecondRateLimit-Remaining: 1 # requests available on the per-second interval ```   to better model your application requests intervals.  In the event of getting your IP banned, the Response Header `Jumpseller-BannedByRateLimit-Reset` informs you the time when will your ban be reseted. <br/><br/> ***  # Pagination  By default we will return 50 objects (products, orders, etc) per page. There is a maximum of 100, using a query string `&limit=100`. If the result set gets paginated it is your responsibility to check the next page for more objects -- you do this by using query strings `&page=2`, `&page=3` and so on.  ```text https://api.jumpseller.com/v1/products.json?login=XXXXXX&authtoken=XXXXX&page=3&limit=100 ``` <br/><br/> ***  # More * [Jumpseller API wrapper](https://gitlab.com/jumpseller-api/ruby) provides a public Ruby abstraction over our API; * [Apps Page](/apps) showcases external integrations with Jumpseller done by technical experts; * [Imgbb API](https://api.imgbb.com/) provides an easy way to upload and temporaly host for images and files. <br/><br/> *** <br/><br/> 
 *
 * The version of the OpenAPI document: 1.0.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIStoreStats.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIStoreStats::OAIStoreStats(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIStoreStats::OAIStoreStats() {
    this->initializeModel();
}

OAIStoreStats::~OAIStoreStats() {}

void OAIStoreStats::initializeModel() {

    m_best_sold_isSet = false;
    m_best_sold_isValid = false;

    m_conversions_isSet = false;
    m_conversions_isValid = false;

    m_currency_isSet = false;
    m_currency_isValid = false;

    m_daily_visits_isSet = false;
    m_daily_visits_isValid = false;

    m_from_isSet = false;
    m_from_isValid = false;

    m_new_vs_returning_customers_isSet = false;
    m_new_vs_returning_customers_isValid = false;

    m_new_vs_returning_orders_isSet = false;
    m_new_vs_returning_orders_isValid = false;

    m_orders_isSet = false;
    m_orders_isValid = false;

    m_payment_methods_isSet = false;
    m_payment_methods_isValid = false;

    m_referrers_isSet = false;
    m_referrers_isValid = false;

    m_region_orders_isSet = false;
    m_region_orders_isValid = false;

    m_search_frequencies_all_isSet = false;
    m_search_frequencies_all_isValid = false;

    m_search_frequencies_without_results_isSet = false;
    m_search_frequencies_without_results_isValid = false;

    m_shipping_methods_isSet = false;
    m_shipping_methods_isValid = false;

    m_to_isSet = false;
    m_to_isValid = false;

    m_traffic_type_isSet = false;
    m_traffic_type_isValid = false;

    m_visits_isSet = false;
    m_visits_isValid = false;
}

void OAIStoreStats::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIStoreStats::fromJsonObject(QJsonObject json) {

    m_best_sold_isValid = ::OpenAPI::fromJsonValue(m_best_sold, json[QString("best_sold")]);
    m_best_sold_isSet = !json[QString("best_sold")].isNull() && m_best_sold_isValid;

    m_conversions_isValid = ::OpenAPI::fromJsonValue(m_conversions, json[QString("conversions")]);
    m_conversions_isSet = !json[QString("conversions")].isNull() && m_conversions_isValid;

    m_currency_isValid = ::OpenAPI::fromJsonValue(m_currency, json[QString("currency")]);
    m_currency_isSet = !json[QString("currency")].isNull() && m_currency_isValid;

    m_daily_visits_isValid = ::OpenAPI::fromJsonValue(m_daily_visits, json[QString("daily_visits")]);
    m_daily_visits_isSet = !json[QString("daily_visits")].isNull() && m_daily_visits_isValid;

    m_from_isValid = ::OpenAPI::fromJsonValue(m_from, json[QString("from")]);
    m_from_isSet = !json[QString("from")].isNull() && m_from_isValid;

    m_new_vs_returning_customers_isValid = ::OpenAPI::fromJsonValue(m_new_vs_returning_customers, json[QString("new_vs_returning_customers")]);
    m_new_vs_returning_customers_isSet = !json[QString("new_vs_returning_customers")].isNull() && m_new_vs_returning_customers_isValid;

    m_new_vs_returning_orders_isValid = ::OpenAPI::fromJsonValue(m_new_vs_returning_orders, json[QString("new_vs_returning_orders")]);
    m_new_vs_returning_orders_isSet = !json[QString("new_vs_returning_orders")].isNull() && m_new_vs_returning_orders_isValid;

    m_orders_isValid = ::OpenAPI::fromJsonValue(m_orders, json[QString("orders")]);
    m_orders_isSet = !json[QString("orders")].isNull() && m_orders_isValid;

    m_payment_methods_isValid = ::OpenAPI::fromJsonValue(m_payment_methods, json[QString("payment_methods")]);
    m_payment_methods_isSet = !json[QString("payment_methods")].isNull() && m_payment_methods_isValid;

    m_referrers_isValid = ::OpenAPI::fromJsonValue(m_referrers, json[QString("referrers")]);
    m_referrers_isSet = !json[QString("referrers")].isNull() && m_referrers_isValid;

    m_region_orders_isValid = ::OpenAPI::fromJsonValue(m_region_orders, json[QString("region_orders")]);
    m_region_orders_isSet = !json[QString("region_orders")].isNull() && m_region_orders_isValid;

    m_search_frequencies_all_isValid = ::OpenAPI::fromJsonValue(m_search_frequencies_all, json[QString("search_frequencies_all")]);
    m_search_frequencies_all_isSet = !json[QString("search_frequencies_all")].isNull() && m_search_frequencies_all_isValid;

    m_search_frequencies_without_results_isValid = ::OpenAPI::fromJsonValue(m_search_frequencies_without_results, json[QString("search_frequencies_without_results")]);
    m_search_frequencies_without_results_isSet = !json[QString("search_frequencies_without_results")].isNull() && m_search_frequencies_without_results_isValid;

    m_shipping_methods_isValid = ::OpenAPI::fromJsonValue(m_shipping_methods, json[QString("shipping_methods")]);
    m_shipping_methods_isSet = !json[QString("shipping_methods")].isNull() && m_shipping_methods_isValid;

    m_to_isValid = ::OpenAPI::fromJsonValue(m_to, json[QString("to")]);
    m_to_isSet = !json[QString("to")].isNull() && m_to_isValid;

    m_traffic_type_isValid = ::OpenAPI::fromJsonValue(m_traffic_type, json[QString("traffic_type")]);
    m_traffic_type_isSet = !json[QString("traffic_type")].isNull() && m_traffic_type_isValid;

    m_visits_isValid = ::OpenAPI::fromJsonValue(m_visits, json[QString("visits")]);
    m_visits_isSet = !json[QString("visits")].isNull() && m_visits_isValid;
}

QString OAIStoreStats::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIStoreStats::asJsonObject() const {
    QJsonObject obj;
    if (m_best_sold.size() > 0) {
        obj.insert(QString("best_sold"), ::OpenAPI::toJsonValue(m_best_sold));
    }
    if (m_conversions.isSet()) {
        obj.insert(QString("conversions"), ::OpenAPI::toJsonValue(m_conversions));
    }
    if (m_currency_isSet) {
        obj.insert(QString("currency"), ::OpenAPI::toJsonValue(m_currency));
    }
    if (m_daily_visits.size() > 0) {
        obj.insert(QString("daily_visits"), ::OpenAPI::toJsonValue(m_daily_visits));
    }
    if (m_from_isSet) {
        obj.insert(QString("from"), ::OpenAPI::toJsonValue(m_from));
    }
    if (m_new_vs_returning_customers.isSet()) {
        obj.insert(QString("new_vs_returning_customers"), ::OpenAPI::toJsonValue(m_new_vs_returning_customers));
    }
    if (m_new_vs_returning_orders.isSet()) {
        obj.insert(QString("new_vs_returning_orders"), ::OpenAPI::toJsonValue(m_new_vs_returning_orders));
    }
    if (m_orders.isSet()) {
        obj.insert(QString("orders"), ::OpenAPI::toJsonValue(m_orders));
    }
    if (m_payment_methods.size() > 0) {
        obj.insert(QString("payment_methods"), ::OpenAPI::toJsonValue(m_payment_methods));
    }
    if (m_referrers.size() > 0) {
        obj.insert(QString("referrers"), ::OpenAPI::toJsonValue(m_referrers));
    }
    if (m_region_orders.isSet()) {
        obj.insert(QString("region_orders"), ::OpenAPI::toJsonValue(m_region_orders));
    }
    if (m_search_frequencies_all.size() > 0) {
        obj.insert(QString("search_frequencies_all"), ::OpenAPI::toJsonValue(m_search_frequencies_all));
    }
    if (m_search_frequencies_without_results.size() > 0) {
        obj.insert(QString("search_frequencies_without_results"), ::OpenAPI::toJsonValue(m_search_frequencies_without_results));
    }
    if (m_shipping_methods.size() > 0) {
        obj.insert(QString("shipping_methods"), ::OpenAPI::toJsonValue(m_shipping_methods));
    }
    if (m_to_isSet) {
        obj.insert(QString("to"), ::OpenAPI::toJsonValue(m_to));
    }
    if (m_traffic_type.size() > 0) {
        obj.insert(QString("traffic_type"), ::OpenAPI::toJsonValue(m_traffic_type));
    }
    if (m_visits_isSet) {
        obj.insert(QString("visits"), ::OpenAPI::toJsonValue(m_visits));
    }
    return obj;
}

QList<OAIBestSold> OAIStoreStats::getBestSold() const {
    return m_best_sold;
}
void OAIStoreStats::setBestSold(const QList<OAIBestSold> &best_sold) {
    m_best_sold = best_sold;
    m_best_sold_isSet = true;
}

bool OAIStoreStats::is_best_sold_Set() const{
    return m_best_sold_isSet;
}

bool OAIStoreStats::is_best_sold_Valid() const{
    return m_best_sold_isValid;
}

OAIStoreStats_conversions OAIStoreStats::getConversions() const {
    return m_conversions;
}
void OAIStoreStats::setConversions(const OAIStoreStats_conversions &conversions) {
    m_conversions = conversions;
    m_conversions_isSet = true;
}

bool OAIStoreStats::is_conversions_Set() const{
    return m_conversions_isSet;
}

bool OAIStoreStats::is_conversions_Valid() const{
    return m_conversions_isValid;
}

QString OAIStoreStats::getCurrency() const {
    return m_currency;
}
void OAIStoreStats::setCurrency(const QString &currency) {
    m_currency = currency;
    m_currency_isSet = true;
}

bool OAIStoreStats::is_currency_Set() const{
    return m_currency_isSet;
}

bool OAIStoreStats::is_currency_Valid() const{
    return m_currency_isValid;
}

QList<OAIDailyVisits> OAIStoreStats::getDailyVisits() const {
    return m_daily_visits;
}
void OAIStoreStats::setDailyVisits(const QList<OAIDailyVisits> &daily_visits) {
    m_daily_visits = daily_visits;
    m_daily_visits_isSet = true;
}

bool OAIStoreStats::is_daily_visits_Set() const{
    return m_daily_visits_isSet;
}

bool OAIStoreStats::is_daily_visits_Valid() const{
    return m_daily_visits_isValid;
}

QString OAIStoreStats::getFrom() const {
    return m_from;
}
void OAIStoreStats::setFrom(const QString &from) {
    m_from = from;
    m_from_isSet = true;
}

bool OAIStoreStats::is_from_Set() const{
    return m_from_isSet;
}

bool OAIStoreStats::is_from_Valid() const{
    return m_from_isValid;
}

OAIStoreStats_new_vs_returning_customers OAIStoreStats::getNewVsReturningCustomers() const {
    return m_new_vs_returning_customers;
}
void OAIStoreStats::setNewVsReturningCustomers(const OAIStoreStats_new_vs_returning_customers &new_vs_returning_customers) {
    m_new_vs_returning_customers = new_vs_returning_customers;
    m_new_vs_returning_customers_isSet = true;
}

bool OAIStoreStats::is_new_vs_returning_customers_Set() const{
    return m_new_vs_returning_customers_isSet;
}

bool OAIStoreStats::is_new_vs_returning_customers_Valid() const{
    return m_new_vs_returning_customers_isValid;
}

OAIStoreStats_new_vs_returning_customers OAIStoreStats::getNewVsReturningOrders() const {
    return m_new_vs_returning_orders;
}
void OAIStoreStats::setNewVsReturningOrders(const OAIStoreStats_new_vs_returning_customers &new_vs_returning_orders) {
    m_new_vs_returning_orders = new_vs_returning_orders;
    m_new_vs_returning_orders_isSet = true;
}

bool OAIStoreStats::is_new_vs_returning_orders_Set() const{
    return m_new_vs_returning_orders_isSet;
}

bool OAIStoreStats::is_new_vs_returning_orders_Valid() const{
    return m_new_vs_returning_orders_isValid;
}

OAIStoreStats_orders OAIStoreStats::getOrders() const {
    return m_orders;
}
void OAIStoreStats::setOrders(const OAIStoreStats_orders &orders) {
    m_orders = orders;
    m_orders_isSet = true;
}

bool OAIStoreStats::is_orders_Set() const{
    return m_orders_isSet;
}

bool OAIStoreStats::is_orders_Valid() const{
    return m_orders_isValid;
}

QList<OAIPaymentMethodFreq> OAIStoreStats::getPaymentMethods() const {
    return m_payment_methods;
}
void OAIStoreStats::setPaymentMethods(const QList<OAIPaymentMethodFreq> &payment_methods) {
    m_payment_methods = payment_methods;
    m_payment_methods_isSet = true;
}

bool OAIStoreStats::is_payment_methods_Set() const{
    return m_payment_methods_isSet;
}

bool OAIStoreStats::is_payment_methods_Valid() const{
    return m_payment_methods_isValid;
}

QList<OAIReferrer> OAIStoreStats::getReferrers() const {
    return m_referrers;
}
void OAIStoreStats::setReferrers(const QList<OAIReferrer> &referrers) {
    m_referrers = referrers;
    m_referrers_isSet = true;
}

bool OAIStoreStats::is_referrers_Set() const{
    return m_referrers_isSet;
}

bool OAIStoreStats::is_referrers_Valid() const{
    return m_referrers_isValid;
}

OAIStoreStats_region_orders OAIStoreStats::getRegionOrders() const {
    return m_region_orders;
}
void OAIStoreStats::setRegionOrders(const OAIStoreStats_region_orders &region_orders) {
    m_region_orders = region_orders;
    m_region_orders_isSet = true;
}

bool OAIStoreStats::is_region_orders_Set() const{
    return m_region_orders_isSet;
}

bool OAIStoreStats::is_region_orders_Valid() const{
    return m_region_orders_isValid;
}

QList<QJsonValue> OAIStoreStats::getSearchFrequenciesAll() const {
    return m_search_frequencies_all;
}
void OAIStoreStats::setSearchFrequenciesAll(const QList<QJsonValue> &search_frequencies_all) {
    m_search_frequencies_all = search_frequencies_all;
    m_search_frequencies_all_isSet = true;
}

bool OAIStoreStats::is_search_frequencies_all_Set() const{
    return m_search_frequencies_all_isSet;
}

bool OAIStoreStats::is_search_frequencies_all_Valid() const{
    return m_search_frequencies_all_isValid;
}

QList<QJsonValue> OAIStoreStats::getSearchFrequenciesWithoutResults() const {
    return m_search_frequencies_without_results;
}
void OAIStoreStats::setSearchFrequenciesWithoutResults(const QList<QJsonValue> &search_frequencies_without_results) {
    m_search_frequencies_without_results = search_frequencies_without_results;
    m_search_frequencies_without_results_isSet = true;
}

bool OAIStoreStats::is_search_frequencies_without_results_Set() const{
    return m_search_frequencies_without_results_isSet;
}

bool OAIStoreStats::is_search_frequencies_without_results_Valid() const{
    return m_search_frequencies_without_results_isValid;
}

QList<OAIShippingMethodFreq> OAIStoreStats::getShippingMethods() const {
    return m_shipping_methods;
}
void OAIStoreStats::setShippingMethods(const QList<OAIShippingMethodFreq> &shipping_methods) {
    m_shipping_methods = shipping_methods;
    m_shipping_methods_isSet = true;
}

bool OAIStoreStats::is_shipping_methods_Set() const{
    return m_shipping_methods_isSet;
}

bool OAIStoreStats::is_shipping_methods_Valid() const{
    return m_shipping_methods_isValid;
}

QString OAIStoreStats::getTo() const {
    return m_to;
}
void OAIStoreStats::setTo(const QString &to) {
    m_to = to;
    m_to_isSet = true;
}

bool OAIStoreStats::is_to_Set() const{
    return m_to_isSet;
}

bool OAIStoreStats::is_to_Valid() const{
    return m_to_isValid;
}

QList<OAITrafficType> OAIStoreStats::getTrafficType() const {
    return m_traffic_type;
}
void OAIStoreStats::setTrafficType(const QList<OAITrafficType> &traffic_type) {
    m_traffic_type = traffic_type;
    m_traffic_type_isSet = true;
}

bool OAIStoreStats::is_traffic_type_Set() const{
    return m_traffic_type_isSet;
}

bool OAIStoreStats::is_traffic_type_Valid() const{
    return m_traffic_type_isValid;
}

qint32 OAIStoreStats::getVisits() const {
    return m_visits;
}
void OAIStoreStats::setVisits(const qint32 &visits) {
    m_visits = visits;
    m_visits_isSet = true;
}

bool OAIStoreStats::is_visits_Set() const{
    return m_visits_isSet;
}

bool OAIStoreStats::is_visits_Valid() const{
    return m_visits_isValid;
}

bool OAIStoreStats::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_best_sold.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_conversions.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_currency_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_daily_visits.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_from_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_new_vs_returning_customers.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_new_vs_returning_orders.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_orders.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_payment_methods.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_referrers.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_region_orders.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_search_frequencies_all.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_search_frequencies_without_results.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_shipping_methods.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_to_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_traffic_type.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_visits_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIStoreStats::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
