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
 * OAIProductFields.h
 *
 * 
 */

#ifndef OAIProductFields_H
#define OAIProductFields_H

#include <QJsonObject>

#include "OAICategoryFields.h"
#include "OAIImageFields.h"
#include "OAIVariantFields.h"
#include <QList>
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAICategoryFields;
class OAIImageFields;
class OAIVariantFields;

class OAIProductFields : public OAIObject {
public:
    OAIProductFields();
    OAIProductFields(QString json);
    ~OAIProductFields() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getBarcode() const;
    void setBarcode(const QString &barcode);
    bool is_barcode_Set() const;
    bool is_barcode_Valid() const;

    QList<OAICategoryFields> getCategories() const;
    void setCategories(const QList<OAICategoryFields> &categories);
    bool is_categories_Set() const;
    bool is_categories_Valid() const;

    QString getCreatedAt() const;
    void setCreatedAt(const QString &created_at);
    bool is_created_at_Set() const;
    bool is_created_at_Valid() const;

    QString getDescription() const;
    void setDescription(const QString &description);
    bool is_description_Set() const;
    bool is_description_Valid() const;

    float getDiameter() const;
    void setDiameter(const float &diameter);
    bool is_diameter_Set() const;
    bool is_diameter_Valid() const;

    float getDiscount() const;
    void setDiscount(const float &discount);
    bool is_discount_Set() const;
    bool is_discount_Valid() const;

    bool isFeatured() const;
    void setFeatured(const bool &featured);
    bool is_featured_Set() const;
    bool is_featured_Valid() const;

    QString getGoogleProductCategory() const;
    void setGoogleProductCategory(const QString &google_product_category);
    bool is_google_product_category_Set() const;
    bool is_google_product_category_Valid() const;

    float getHeight() const;
    void setHeight(const float &height);
    bool is_height_Set() const;
    bool is_height_Valid() const;

    qint32 getId() const;
    void setId(const qint32 &id);
    bool is_id_Set() const;
    bool is_id_Valid() const;

    QList<OAIImageFields> getImages() const;
    void setImages(const QList<OAIImageFields> &images);
    bool is_images_Set() const;
    bool is_images_Valid() const;

    float getLength() const;
    void setLength(const float &length);
    bool is_length_Set() const;
    bool is_length_Valid() const;

    QString getName() const;
    void setName(const QString &name);
    bool is_name_Set() const;
    bool is_name_Valid() const;

    QString getPackageFormat() const;
    void setPackageFormat(const QString &package_format);
    bool is_package_format_Set() const;
    bool is_package_format_Valid() const;

    QString getPermalink() const;
    void setPermalink(const QString &permalink);
    bool is_permalink_Set() const;
    bool is_permalink_Valid() const;

    float getPrice() const;
    void setPrice(const float &price);
    bool is_price_Set() const;
    bool is_price_Valid() const;

    QString getSku() const;
    void setSku(const QString &sku);
    bool is_sku_Set() const;
    bool is_sku_Valid() const;

    QString getStatus() const;
    void setStatus(const QString &status);
    bool is_status_Set() const;
    bool is_status_Valid() const;

    qint32 getStock() const;
    void setStock(const qint32 &stock);
    bool is_stock_Set() const;
    bool is_stock_Valid() const;

    bool isStockUnlimited() const;
    void setStockUnlimited(const bool &stock_unlimited);
    bool is_stock_unlimited_Set() const;
    bool is_stock_unlimited_Valid() const;

    QList<OAIVariantFields> getVariants() const;
    void setVariants(const QList<OAIVariantFields> &variants);
    bool is_variants_Set() const;
    bool is_variants_Valid() const;

    float getWeight() const;
    void setWeight(const float &weight);
    bool is_weight_Set() const;
    bool is_weight_Valid() const;

    float getWidth() const;
    void setWidth(const float &width);
    bool is_width_Set() const;
    bool is_width_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_barcode;
    bool m_barcode_isSet;
    bool m_barcode_isValid;

    QList<OAICategoryFields> m_categories;
    bool m_categories_isSet;
    bool m_categories_isValid;

    QString m_created_at;
    bool m_created_at_isSet;
    bool m_created_at_isValid;

    QString m_description;
    bool m_description_isSet;
    bool m_description_isValid;

    float m_diameter;
    bool m_diameter_isSet;
    bool m_diameter_isValid;

    float m_discount;
    bool m_discount_isSet;
    bool m_discount_isValid;

    bool m_featured;
    bool m_featured_isSet;
    bool m_featured_isValid;

    QString m_google_product_category;
    bool m_google_product_category_isSet;
    bool m_google_product_category_isValid;

    float m_height;
    bool m_height_isSet;
    bool m_height_isValid;

    qint32 m_id;
    bool m_id_isSet;
    bool m_id_isValid;

    QList<OAIImageFields> m_images;
    bool m_images_isSet;
    bool m_images_isValid;

    float m_length;
    bool m_length_isSet;
    bool m_length_isValid;

    QString m_name;
    bool m_name_isSet;
    bool m_name_isValid;

    QString m_package_format;
    bool m_package_format_isSet;
    bool m_package_format_isValid;

    QString m_permalink;
    bool m_permalink_isSet;
    bool m_permalink_isValid;

    float m_price;
    bool m_price_isSet;
    bool m_price_isValid;

    QString m_sku;
    bool m_sku_isSet;
    bool m_sku_isValid;

    QString m_status;
    bool m_status_isSet;
    bool m_status_isValid;

    qint32 m_stock;
    bool m_stock_isSet;
    bool m_stock_isValid;

    bool m_stock_unlimited;
    bool m_stock_unlimited_isSet;
    bool m_stock_unlimited_isValid;

    QList<OAIVariantFields> m_variants;
    bool m_variants_isSet;
    bool m_variants_isValid;

    float m_weight;
    bool m_weight_isSet;
    bool m_weight_isValid;

    float m_width;
    bool m_width_isSet;
    bool m_width_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIProductFields)

#endif // OAIProductFields_H
