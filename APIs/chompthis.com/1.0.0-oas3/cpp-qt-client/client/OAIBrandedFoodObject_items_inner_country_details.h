/**
 * Chomp Food Database API Documentation
 * ## Important An **[API key](https://chompthis.com/api/)** is required for access to this API. Get yours at **[https://chompthis.com/api](https://chompthis.com/api/)**.  ### Getting Started   * **[Subscribe](https://chompthis.com/api/#pricing)** to the API.   * Scroll down and click the \"**Authorize**\" button.   * Enter your API key into the \"**value**\" input, click the \"**Authorize**\" button, then click the \"**Close**\" button.   * Scroll down to the section titled \"**default**\" and click on the API endpoint you wish to use.   * Click the \"**Try it out**\" button.   * Enter the information the endpoint requires.   * Click the \"**Execute**\" button.  ### Example    * Branded food response object: **[View example &raquo;](https://raw.githubusercontent.com/chompfoods/examples/master/branded-food-response-object.json)**   * Ingredient response object: **[View example &raquo;](https://raw.githubusercontent.com/chompfoods/examples/master/ingredient-response-object.json)**   * Error response object: **[View example &raquo;](https://raw.githubusercontent.com/chompfoods/examples/master/error-response-object.json)**  ### How Do I Find My API Key?   * Your API key was sent to the email address you used to create your subscription.   * You will also find your API key in the **[Client Center](https://chompthis.com/api/manage.php)**.   * Read **[this article](https://desk.zoho.com/portal/chompthis/kb/articles/how-do-i-find-my-api-key)** for more information.  ### Helpful Links   * **Help & Support**     * [Knowledge Base &raquo;](https://desk.zoho.com/portal/chompthis/kb/chomp)     * [Support &raquo;](https://chompthis.com/api/ticket-new.php)     * [Client Center &raquo;](https://chompthis.com/api/manage.php)   * **Pricing**     * [Subscription Options &raquo;](https://chompthis.com/api/)     * [Cost Calculator &raquo;](https://chompthis.com/api/cost-calculator.php)   * **Guidelines**     * [Terms & License &raquo;](https://chompthis.com/api/terms.php)     * [Attribution &raquo;](https://chompthis.com/api/docs/attribution.php) 
 *
 * The version of the OpenAPI document: 1.0.0-oas3
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIBrandedFoodObject_items_inner_country_details.h
 *
 * An object containing additional information on the countries where this item is found
 */

#ifndef OAIBrandedFoodObject_items_inner_country_details_H
#define OAIBrandedFoodObject_items_inner_country_details_H

#include <QJsonObject>


#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIBrandedFoodObject_items_inner_country_details : public OAIObject {
public:
    OAIBrandedFoodObject_items_inner_country_details();
    OAIBrandedFoodObject_items_inner_country_details(QString json);
    ~OAIBrandedFoodObject_items_inner_country_details() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    qint32 getEnglishSpeaking() const;
    void setEnglishSpeaking(const qint32 &english_speaking);
    bool is_english_speaking_Set() const;
    bool is_english_speaking_Valid() const;

    qint32 getNonEnglishSpeaking() const;
    void setNonEnglishSpeaking(const qint32 &non_english_speaking);
    bool is_non_english_speaking_Set() const;
    bool is_non_english_speaking_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    qint32 m_english_speaking;
    bool m_english_speaking_isSet;
    bool m_english_speaking_isValid;

    qint32 m_non_english_speaking;
    bool m_non_english_speaking_isSet;
    bool m_non_english_speaking_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIBrandedFoodObject_items_inner_country_details)

#endif // OAIBrandedFoodObject_items_inner_country_details_H
