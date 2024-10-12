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

#include "OAIIngredientObject_items_inner.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIIngredientObject_items_inner::OAIIngredientObject_items_inner(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIIngredientObject_items_inner::OAIIngredientObject_items_inner() {
    this->initializeModel();
}

OAIIngredientObject_items_inner::~OAIIngredientObject_items_inner() {}

void OAIIngredientObject_items_inner::initializeModel() {

    m_calorie_conversion_factor_isSet = false;
    m_calorie_conversion_factor_isValid = false;

    m_categories_isSet = false;
    m_categories_isValid = false;

    m_common_name_isSet = false;
    m_common_name_isValid = false;

    m_components_isSet = false;
    m_components_isValid = false;

    m_footnote_isSet = false;
    m_footnote_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_nutrients_isSet = false;
    m_nutrients_isValid = false;

    m_portions_isSet = false;
    m_portions_isValid = false;

    m_protein_conversion_factor_isSet = false;
    m_protein_conversion_factor_isValid = false;

    m_score_isSet = false;
    m_score_isValid = false;

    m_search_term_isSet = false;
    m_search_term_isValid = false;
}

void OAIIngredientObject_items_inner::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIIngredientObject_items_inner::fromJsonObject(QJsonObject json) {

    m_calorie_conversion_factor_isValid = ::OpenAPI::fromJsonValue(m_calorie_conversion_factor, json[QString("calorie_conversion_factor")]);
    m_calorie_conversion_factor_isSet = !json[QString("calorie_conversion_factor")].isNull() && m_calorie_conversion_factor_isValid;

    m_categories_isValid = ::OpenAPI::fromJsonValue(m_categories, json[QString("categories")]);
    m_categories_isSet = !json[QString("categories")].isNull() && m_categories_isValid;

    m_common_name_isValid = ::OpenAPI::fromJsonValue(m_common_name, json[QString("common_name")]);
    m_common_name_isSet = !json[QString("common_name")].isNull() && m_common_name_isValid;

    m_components_isValid = ::OpenAPI::fromJsonValue(m_components, json[QString("components")]);
    m_components_isSet = !json[QString("components")].isNull() && m_components_isValid;

    m_footnote_isValid = ::OpenAPI::fromJsonValue(m_footnote, json[QString("footnote")]);
    m_footnote_isSet = !json[QString("footnote")].isNull() && m_footnote_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_nutrients_isValid = ::OpenAPI::fromJsonValue(m_nutrients, json[QString("nutrients")]);
    m_nutrients_isSet = !json[QString("nutrients")].isNull() && m_nutrients_isValid;

    m_portions_isValid = ::OpenAPI::fromJsonValue(m_portions, json[QString("portions")]);
    m_portions_isSet = !json[QString("portions")].isNull() && m_portions_isValid;

    m_protein_conversion_factor_isValid = ::OpenAPI::fromJsonValue(m_protein_conversion_factor, json[QString("protein_conversion_factor")]);
    m_protein_conversion_factor_isSet = !json[QString("protein_conversion_factor")].isNull() && m_protein_conversion_factor_isValid;

    m_score_isValid = ::OpenAPI::fromJsonValue(m_score, json[QString("score")]);
    m_score_isSet = !json[QString("score")].isNull() && m_score_isValid;

    m_search_term_isValid = ::OpenAPI::fromJsonValue(m_search_term, json[QString("search_term")]);
    m_search_term_isSet = !json[QString("search_term")].isNull() && m_search_term_isValid;
}

QString OAIIngredientObject_items_inner::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIIngredientObject_items_inner::asJsonObject() const {
    QJsonObject obj;
    if (m_calorie_conversion_factor.isSet()) {
        obj.insert(QString("calorie_conversion_factor"), ::OpenAPI::toJsonValue(m_calorie_conversion_factor));
    }
    if (m_categories.size() > 0) {
        obj.insert(QString("categories"), ::OpenAPI::toJsonValue(m_categories));
    }
    if (m_common_name_isSet) {
        obj.insert(QString("common_name"), ::OpenAPI::toJsonValue(m_common_name));
    }
    if (m_components.size() > 0) {
        obj.insert(QString("components"), ::OpenAPI::toJsonValue(m_components));
    }
    if (m_footnote_isSet) {
        obj.insert(QString("footnote"), ::OpenAPI::toJsonValue(m_footnote));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_nutrients.size() > 0) {
        obj.insert(QString("nutrients"), ::OpenAPI::toJsonValue(m_nutrients));
    }
    if (m_portions.size() > 0) {
        obj.insert(QString("portions"), ::OpenAPI::toJsonValue(m_portions));
    }
    if (m_protein_conversion_factor_isSet) {
        obj.insert(QString("protein_conversion_factor"), ::OpenAPI::toJsonValue(m_protein_conversion_factor));
    }
    if (m_score_isSet) {
        obj.insert(QString("score"), ::OpenAPI::toJsonValue(m_score));
    }
    if (m_search_term_isSet) {
        obj.insert(QString("search_term"), ::OpenAPI::toJsonValue(m_search_term));
    }
    return obj;
}

OAIIngredientObject_items_inner_calorie_conversion_factor OAIIngredientObject_items_inner::getCalorieConversionFactor() const {
    return m_calorie_conversion_factor;
}
void OAIIngredientObject_items_inner::setCalorieConversionFactor(const OAIIngredientObject_items_inner_calorie_conversion_factor &calorie_conversion_factor) {
    m_calorie_conversion_factor = calorie_conversion_factor;
    m_calorie_conversion_factor_isSet = true;
}

bool OAIIngredientObject_items_inner::is_calorie_conversion_factor_Set() const{
    return m_calorie_conversion_factor_isSet;
}

bool OAIIngredientObject_items_inner::is_calorie_conversion_factor_Valid() const{
    return m_calorie_conversion_factor_isValid;
}

QList<QString> OAIIngredientObject_items_inner::getCategories() const {
    return m_categories;
}
void OAIIngredientObject_items_inner::setCategories(const QList<QString> &categories) {
    m_categories = categories;
    m_categories_isSet = true;
}

bool OAIIngredientObject_items_inner::is_categories_Set() const{
    return m_categories_isSet;
}

bool OAIIngredientObject_items_inner::is_categories_Valid() const{
    return m_categories_isValid;
}

QString OAIIngredientObject_items_inner::getCommonName() const {
    return m_common_name;
}
void OAIIngredientObject_items_inner::setCommonName(const QString &common_name) {
    m_common_name = common_name;
    m_common_name_isSet = true;
}

bool OAIIngredientObject_items_inner::is_common_name_Set() const{
    return m_common_name_isSet;
}

bool OAIIngredientObject_items_inner::is_common_name_Valid() const{
    return m_common_name_isValid;
}

QList<OAIIngredientObject_items_inner_components_inner> OAIIngredientObject_items_inner::getComponents() const {
    return m_components;
}
void OAIIngredientObject_items_inner::setComponents(const QList<OAIIngredientObject_items_inner_components_inner> &components) {
    m_components = components;
    m_components_isSet = true;
}

bool OAIIngredientObject_items_inner::is_components_Set() const{
    return m_components_isSet;
}

bool OAIIngredientObject_items_inner::is_components_Valid() const{
    return m_components_isValid;
}

QString OAIIngredientObject_items_inner::getFootnote() const {
    return m_footnote;
}
void OAIIngredientObject_items_inner::setFootnote(const QString &footnote) {
    m_footnote = footnote;
    m_footnote_isSet = true;
}

bool OAIIngredientObject_items_inner::is_footnote_Set() const{
    return m_footnote_isSet;
}

bool OAIIngredientObject_items_inner::is_footnote_Valid() const{
    return m_footnote_isValid;
}

QString OAIIngredientObject_items_inner::getName() const {
    return m_name;
}
void OAIIngredientObject_items_inner::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIIngredientObject_items_inner::is_name_Set() const{
    return m_name_isSet;
}

bool OAIIngredientObject_items_inner::is_name_Valid() const{
    return m_name_isValid;
}

QList<OAIIngredientObject_items_inner_nutrients_inner> OAIIngredientObject_items_inner::getNutrients() const {
    return m_nutrients;
}
void OAIIngredientObject_items_inner::setNutrients(const QList<OAIIngredientObject_items_inner_nutrients_inner> &nutrients) {
    m_nutrients = nutrients;
    m_nutrients_isSet = true;
}

bool OAIIngredientObject_items_inner::is_nutrients_Set() const{
    return m_nutrients_isSet;
}

bool OAIIngredientObject_items_inner::is_nutrients_Valid() const{
    return m_nutrients_isValid;
}

QList<OAIIngredientObject_items_inner_portions_inner> OAIIngredientObject_items_inner::getPortions() const {
    return m_portions;
}
void OAIIngredientObject_items_inner::setPortions(const QList<OAIIngredientObject_items_inner_portions_inner> &portions) {
    m_portions = portions;
    m_portions_isSet = true;
}

bool OAIIngredientObject_items_inner::is_portions_Set() const{
    return m_portions_isSet;
}

bool OAIIngredientObject_items_inner::is_portions_Valid() const{
    return m_portions_isValid;
}

double OAIIngredientObject_items_inner::getProteinConversionFactor() const {
    return m_protein_conversion_factor;
}
void OAIIngredientObject_items_inner::setProteinConversionFactor(const double &protein_conversion_factor) {
    m_protein_conversion_factor = protein_conversion_factor;
    m_protein_conversion_factor_isSet = true;
}

bool OAIIngredientObject_items_inner::is_protein_conversion_factor_Set() const{
    return m_protein_conversion_factor_isSet;
}

bool OAIIngredientObject_items_inner::is_protein_conversion_factor_Valid() const{
    return m_protein_conversion_factor_isValid;
}

QString OAIIngredientObject_items_inner::getScore() const {
    return m_score;
}
void OAIIngredientObject_items_inner::setScore(const QString &score) {
    m_score = score;
    m_score_isSet = true;
}

bool OAIIngredientObject_items_inner::is_score_Set() const{
    return m_score_isSet;
}

bool OAIIngredientObject_items_inner::is_score_Valid() const{
    return m_score_isValid;
}

QString OAIIngredientObject_items_inner::getSearchTerm() const {
    return m_search_term;
}
void OAIIngredientObject_items_inner::setSearchTerm(const QString &search_term) {
    m_search_term = search_term;
    m_search_term_isSet = true;
}

bool OAIIngredientObject_items_inner::is_search_term_Set() const{
    return m_search_term_isSet;
}

bool OAIIngredientObject_items_inner::is_search_term_Valid() const{
    return m_search_term_isValid;
}

bool OAIIngredientObject_items_inner::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_calorie_conversion_factor.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_categories.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_common_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_components.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_footnote_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_nutrients.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_portions.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_protein_conversion_factor_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_score_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_search_term_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIIngredientObject_items_inner::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
