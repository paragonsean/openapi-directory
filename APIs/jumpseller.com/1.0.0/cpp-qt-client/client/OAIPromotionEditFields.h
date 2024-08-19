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
 * OAIPromotionEditFields.h
 *
 * 
 */

#ifndef OAIPromotionEditFields_H
#define OAIPromotionEditFields_H

#include <QJsonObject>

#include "OAIId.h"
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIId;

class OAIPromotionEditFields : public OAIObject {
public:
    OAIPromotionEditFields();
    OAIPromotionEditFields(QString json);
    ~OAIPromotionEditFields() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getBeginsAt() const;
    void setBeginsAt(const QString &begins_at);
    bool is_begins_at_Set() const;
    bool is_begins_at_Valid() const;

    QString getBuysAtLeast() const;
    void setBuysAtLeast(const QString &buys_at_least);
    bool is_buys_at_least_Set() const;
    bool is_buys_at_least_Valid() const;

    QList<OAIId> getCategories() const;
    void setCategories(const QList<OAIId> &categories);
    bool is_categories_Set() const;
    bool is_categories_Valid() const;

    QString getCode() const;
    void setCode(const QString &code);
    bool is_code_Set() const;
    bool is_code_Valid() const;

    float getConditionPrice() const;
    void setConditionPrice(const float &condition_price);
    bool is_condition_price_Set() const;
    bool is_condition_price_Valid() const;

    qint32 getConditionQty() const;
    void setConditionQty(const qint32 &condition_qty);
    bool is_condition_qty_Set() const;
    bool is_condition_qty_Valid() const;

    bool isCumulative() const;
    void setCumulative(const bool &cumulative);
    bool is_cumulative_Set() const;
    bool is_cumulative_Valid() const;

    QList<OAIId> getCustomerCategories() const;
    void setCustomerCategories(const QList<OAIId> &customer_categories);
    bool is_customer_categories_Set() const;
    bool is_customer_categories_Valid() const;

    QString getCustomers() const;
    void setCustomers(const QString &customers);
    bool is_customers_Set() const;
    bool is_customers_Valid() const;

    float getDiscountAmountFix() const;
    void setDiscountAmountFix(const float &discount_amount_fix);
    bool is_discount_amount_fix_Set() const;
    bool is_discount_amount_fix_Valid() const;

    float getDiscountAmountPercent() const;
    void setDiscountAmountPercent(const float &discount_amount_percent);
    bool is_discount_amount_percent_Set() const;
    bool is_discount_amount_percent_Valid() const;

    QString getDiscountTarget() const;
    void setDiscountTarget(const QString &discount_target);
    bool is_discount_target_Set() const;
    bool is_discount_target_Valid() const;

    bool isEnabled() const;
    void setEnabled(const bool &enabled);
    bool is_enabled_Set() const;
    bool is_enabled_Valid() const;

    QString getExpiresAt() const;
    void setExpiresAt(const QString &expires_at);
    bool is_expires_at_Set() const;
    bool is_expires_at_Valid() const;

    QString getLasts() const;
    void setLasts(const QString &lasts);
    bool is_lasts_Set() const;
    bool is_lasts_Valid() const;

    qint32 getMaxTimesUsed() const;
    void setMaxTimesUsed(const qint32 &max_times_used);
    bool is_max_times_used_Set() const;
    bool is_max_times_used_Valid() const;

    QString getName() const;
    void setName(const QString &name);
    bool is_name_Set() const;
    bool is_name_Valid() const;

    QList<OAIId> getProducts() const;
    void setProducts(const QList<OAIId> &products);
    bool is_products_Set() const;
    bool is_products_Valid() const;

    QList<OAIId> getProductsX() const;
    void setProductsX(const QList<OAIId> &products_x);
    bool is_products_x_Set() const;
    bool is_products_x_Valid() const;

    qint32 getQuantityX() const;
    void setQuantityX(const qint32 &quantity_x);
    bool is_quantity_x_Set() const;
    bool is_quantity_x_Valid() const;

    QString getType() const;
    void setType(const QString &type);
    bool is_type_Set() const;
    bool is_type_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_begins_at;
    bool m_begins_at_isSet;
    bool m_begins_at_isValid;

    QString m_buys_at_least;
    bool m_buys_at_least_isSet;
    bool m_buys_at_least_isValid;

    QList<OAIId> m_categories;
    bool m_categories_isSet;
    bool m_categories_isValid;

    QString m_code;
    bool m_code_isSet;
    bool m_code_isValid;

    float m_condition_price;
    bool m_condition_price_isSet;
    bool m_condition_price_isValid;

    qint32 m_condition_qty;
    bool m_condition_qty_isSet;
    bool m_condition_qty_isValid;

    bool m_cumulative;
    bool m_cumulative_isSet;
    bool m_cumulative_isValid;

    QList<OAIId> m_customer_categories;
    bool m_customer_categories_isSet;
    bool m_customer_categories_isValid;

    QString m_customers;
    bool m_customers_isSet;
    bool m_customers_isValid;

    float m_discount_amount_fix;
    bool m_discount_amount_fix_isSet;
    bool m_discount_amount_fix_isValid;

    float m_discount_amount_percent;
    bool m_discount_amount_percent_isSet;
    bool m_discount_amount_percent_isValid;

    QString m_discount_target;
    bool m_discount_target_isSet;
    bool m_discount_target_isValid;

    bool m_enabled;
    bool m_enabled_isSet;
    bool m_enabled_isValid;

    QString m_expires_at;
    bool m_expires_at_isSet;
    bool m_expires_at_isValid;

    QString m_lasts;
    bool m_lasts_isSet;
    bool m_lasts_isValid;

    qint32 m_max_times_used;
    bool m_max_times_used_isSet;
    bool m_max_times_used_isValid;

    QString m_name;
    bool m_name_isSet;
    bool m_name_isValid;

    QList<OAIId> m_products;
    bool m_products_isSet;
    bool m_products_isValid;

    QList<OAIId> m_products_x;
    bool m_products_x_isSet;
    bool m_products_x_isValid;

    qint32 m_quantity_x;
    bool m_quantity_x_isSet;
    bool m_quantity_x_isValid;

    QString m_type;
    bool m_type_isSet;
    bool m_type_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIPromotionEditFields)

#endif // OAIPromotionEditFields_H
