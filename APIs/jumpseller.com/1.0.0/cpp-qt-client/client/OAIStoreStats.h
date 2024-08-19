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

/*
 * OAIStoreStats.h
 *
 * 
 */

#ifndef OAIStoreStats_H
#define OAIStoreStats_H

#include <QJsonObject>

#include "OAIBestSold.h"
#include "OAIDailyVisits.h"
#include "OAIPaymentMethodFreq.h"
#include "OAIReferrer.h"
#include "OAIShippingMethodFreq.h"
#include "OAIStoreStats_conversions.h"
#include "OAIStoreStats_new_vs_returning_customers.h"
#include "OAIStoreStats_orders.h"
#include "OAIStoreStats_region_orders.h"
#include "OAITrafficType.h"
#include <QJsonValue>
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIBestSold;
class OAIStoreStats_conversions;
class OAIDailyVisits;
class OAIStoreStats_new_vs_returning_customers;
class OAIStoreStats_orders;
class OAIPaymentMethodFreq;
class OAIReferrer;
class OAIStoreStats_region_orders;
class OAIShippingMethodFreq;
class OAITrafficType;

class OAIStoreStats : public OAIObject {
public:
    OAIStoreStats();
    OAIStoreStats(QString json);
    ~OAIStoreStats() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QList<OAIBestSold> getBestSold() const;
    void setBestSold(const QList<OAIBestSold> &best_sold);
    bool is_best_sold_Set() const;
    bool is_best_sold_Valid() const;

    OAIStoreStats_conversions getConversions() const;
    void setConversions(const OAIStoreStats_conversions &conversions);
    bool is_conversions_Set() const;
    bool is_conversions_Valid() const;

    QString getCurrency() const;
    void setCurrency(const QString &currency);
    bool is_currency_Set() const;
    bool is_currency_Valid() const;

    QList<OAIDailyVisits> getDailyVisits() const;
    void setDailyVisits(const QList<OAIDailyVisits> &daily_visits);
    bool is_daily_visits_Set() const;
    bool is_daily_visits_Valid() const;

    QString getFrom() const;
    void setFrom(const QString &from);
    bool is_from_Set() const;
    bool is_from_Valid() const;

    OAIStoreStats_new_vs_returning_customers getNewVsReturningCustomers() const;
    void setNewVsReturningCustomers(const OAIStoreStats_new_vs_returning_customers &new_vs_returning_customers);
    bool is_new_vs_returning_customers_Set() const;
    bool is_new_vs_returning_customers_Valid() const;

    OAIStoreStats_new_vs_returning_customers getNewVsReturningOrders() const;
    void setNewVsReturningOrders(const OAIStoreStats_new_vs_returning_customers &new_vs_returning_orders);
    bool is_new_vs_returning_orders_Set() const;
    bool is_new_vs_returning_orders_Valid() const;

    OAIStoreStats_orders getOrders() const;
    void setOrders(const OAIStoreStats_orders &orders);
    bool is_orders_Set() const;
    bool is_orders_Valid() const;

    QList<OAIPaymentMethodFreq> getPaymentMethods() const;
    void setPaymentMethods(const QList<OAIPaymentMethodFreq> &payment_methods);
    bool is_payment_methods_Set() const;
    bool is_payment_methods_Valid() const;

    QList<OAIReferrer> getReferrers() const;
    void setReferrers(const QList<OAIReferrer> &referrers);
    bool is_referrers_Set() const;
    bool is_referrers_Valid() const;

    OAIStoreStats_region_orders getRegionOrders() const;
    void setRegionOrders(const OAIStoreStats_region_orders &region_orders);
    bool is_region_orders_Set() const;
    bool is_region_orders_Valid() const;

    QList<QJsonValue> getSearchFrequenciesAll() const;
    void setSearchFrequenciesAll(const QList<QJsonValue> &search_frequencies_all);
    bool is_search_frequencies_all_Set() const;
    bool is_search_frequencies_all_Valid() const;

    QList<QJsonValue> getSearchFrequenciesWithoutResults() const;
    void setSearchFrequenciesWithoutResults(const QList<QJsonValue> &search_frequencies_without_results);
    bool is_search_frequencies_without_results_Set() const;
    bool is_search_frequencies_without_results_Valid() const;

    QList<OAIShippingMethodFreq> getShippingMethods() const;
    void setShippingMethods(const QList<OAIShippingMethodFreq> &shipping_methods);
    bool is_shipping_methods_Set() const;
    bool is_shipping_methods_Valid() const;

    QString getTo() const;
    void setTo(const QString &to);
    bool is_to_Set() const;
    bool is_to_Valid() const;

    QList<OAITrafficType> getTrafficType() const;
    void setTrafficType(const QList<OAITrafficType> &traffic_type);
    bool is_traffic_type_Set() const;
    bool is_traffic_type_Valid() const;

    qint32 getVisits() const;
    void setVisits(const qint32 &visits);
    bool is_visits_Set() const;
    bool is_visits_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QList<OAIBestSold> m_best_sold;
    bool m_best_sold_isSet;
    bool m_best_sold_isValid;

    OAIStoreStats_conversions m_conversions;
    bool m_conversions_isSet;
    bool m_conversions_isValid;

    QString m_currency;
    bool m_currency_isSet;
    bool m_currency_isValid;

    QList<OAIDailyVisits> m_daily_visits;
    bool m_daily_visits_isSet;
    bool m_daily_visits_isValid;

    QString m_from;
    bool m_from_isSet;
    bool m_from_isValid;

    OAIStoreStats_new_vs_returning_customers m_new_vs_returning_customers;
    bool m_new_vs_returning_customers_isSet;
    bool m_new_vs_returning_customers_isValid;

    OAIStoreStats_new_vs_returning_customers m_new_vs_returning_orders;
    bool m_new_vs_returning_orders_isSet;
    bool m_new_vs_returning_orders_isValid;

    OAIStoreStats_orders m_orders;
    bool m_orders_isSet;
    bool m_orders_isValid;

    QList<OAIPaymentMethodFreq> m_payment_methods;
    bool m_payment_methods_isSet;
    bool m_payment_methods_isValid;

    QList<OAIReferrer> m_referrers;
    bool m_referrers_isSet;
    bool m_referrers_isValid;

    OAIStoreStats_region_orders m_region_orders;
    bool m_region_orders_isSet;
    bool m_region_orders_isValid;

    QList<QJsonValue> m_search_frequencies_all;
    bool m_search_frequencies_all_isSet;
    bool m_search_frequencies_all_isValid;

    QList<QJsonValue> m_search_frequencies_without_results;
    bool m_search_frequencies_without_results_isSet;
    bool m_search_frequencies_without_results_isValid;

    QList<OAIShippingMethodFreq> m_shipping_methods;
    bool m_shipping_methods_isSet;
    bool m_shipping_methods_isValid;

    QString m_to;
    bool m_to_isSet;
    bool m_to_isValid;

    QList<OAITrafficType> m_traffic_type;
    bool m_traffic_type_isSet;
    bool m_traffic_type_isValid;

    qint32 m_visits;
    bool m_visits_isSet;
    bool m_visits_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIStoreStats)

#endif // OAIStoreStats_H
