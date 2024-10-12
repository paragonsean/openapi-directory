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

#include "OAIIngredientObject_items_inner_portions_inner.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIIngredientObject_items_inner_portions_inner::OAIIngredientObject_items_inner_portions_inner(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIIngredientObject_items_inner_portions_inner::OAIIngredientObject_items_inner_portions_inner() {
    this->initializeModel();
}

OAIIngredientObject_items_inner_portions_inner::~OAIIngredientObject_items_inner_portions_inner() {}

void OAIIngredientObject_items_inner_portions_inner::initializeModel() {

    m_data_points_isSet = false;
    m_data_points_isValid = false;

    m_description_isSet = false;
    m_description_isValid = false;

    m_footnote_isSet = false;
    m_footnote_isValid = false;

    m_gram_weight_isSet = false;
    m_gram_weight_isValid = false;

    m_measurement_unit_isSet = false;
    m_measurement_unit_isValid = false;

    m_modifier_isSet = false;
    m_modifier_isValid = false;
}

void OAIIngredientObject_items_inner_portions_inner::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIIngredientObject_items_inner_portions_inner::fromJsonObject(QJsonObject json) {

    m_data_points_isValid = ::OpenAPI::fromJsonValue(m_data_points, json[QString("data_points")]);
    m_data_points_isSet = !json[QString("data_points")].isNull() && m_data_points_isValid;

    m_description_isValid = ::OpenAPI::fromJsonValue(m_description, json[QString("description")]);
    m_description_isSet = !json[QString("description")].isNull() && m_description_isValid;

    m_footnote_isValid = ::OpenAPI::fromJsonValue(m_footnote, json[QString("footnote")]);
    m_footnote_isSet = !json[QString("footnote")].isNull() && m_footnote_isValid;

    m_gram_weight_isValid = ::OpenAPI::fromJsonValue(m_gram_weight, json[QString("gram_weight")]);
    m_gram_weight_isSet = !json[QString("gram_weight")].isNull() && m_gram_weight_isValid;

    m_measurement_unit_isValid = ::OpenAPI::fromJsonValue(m_measurement_unit, json[QString("measurement_unit")]);
    m_measurement_unit_isSet = !json[QString("measurement_unit")].isNull() && m_measurement_unit_isValid;

    m_modifier_isValid = ::OpenAPI::fromJsonValue(m_modifier, json[QString("modifier")]);
    m_modifier_isSet = !json[QString("modifier")].isNull() && m_modifier_isValid;
}

QString OAIIngredientObject_items_inner_portions_inner::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIIngredientObject_items_inner_portions_inner::asJsonObject() const {
    QJsonObject obj;
    if (m_data_points_isSet) {
        obj.insert(QString("data_points"), ::OpenAPI::toJsonValue(m_data_points));
    }
    if (m_description_isSet) {
        obj.insert(QString("description"), ::OpenAPI::toJsonValue(m_description));
    }
    if (m_footnote_isSet) {
        obj.insert(QString("footnote"), ::OpenAPI::toJsonValue(m_footnote));
    }
    if (m_gram_weight_isSet) {
        obj.insert(QString("gram_weight"), ::OpenAPI::toJsonValue(m_gram_weight));
    }
    if (m_measurement_unit_isSet) {
        obj.insert(QString("measurement_unit"), ::OpenAPI::toJsonValue(m_measurement_unit));
    }
    if (m_modifier_isSet) {
        obj.insert(QString("modifier"), ::OpenAPI::toJsonValue(m_modifier));
    }
    return obj;
}

qint32 OAIIngredientObject_items_inner_portions_inner::getDataPoints() const {
    return m_data_points;
}
void OAIIngredientObject_items_inner_portions_inner::setDataPoints(const qint32 &data_points) {
    m_data_points = data_points;
    m_data_points_isSet = true;
}

bool OAIIngredientObject_items_inner_portions_inner::is_data_points_Set() const{
    return m_data_points_isSet;
}

bool OAIIngredientObject_items_inner_portions_inner::is_data_points_Valid() const{
    return m_data_points_isValid;
}

QString OAIIngredientObject_items_inner_portions_inner::getDescription() const {
    return m_description;
}
void OAIIngredientObject_items_inner_portions_inner::setDescription(const QString &description) {
    m_description = description;
    m_description_isSet = true;
}

bool OAIIngredientObject_items_inner_portions_inner::is_description_Set() const{
    return m_description_isSet;
}

bool OAIIngredientObject_items_inner_portions_inner::is_description_Valid() const{
    return m_description_isValid;
}

QString OAIIngredientObject_items_inner_portions_inner::getFootnote() const {
    return m_footnote;
}
void OAIIngredientObject_items_inner_portions_inner::setFootnote(const QString &footnote) {
    m_footnote = footnote;
    m_footnote_isSet = true;
}

bool OAIIngredientObject_items_inner_portions_inner::is_footnote_Set() const{
    return m_footnote_isSet;
}

bool OAIIngredientObject_items_inner_portions_inner::is_footnote_Valid() const{
    return m_footnote_isValid;
}

double OAIIngredientObject_items_inner_portions_inner::getGramWeight() const {
    return m_gram_weight;
}
void OAIIngredientObject_items_inner_portions_inner::setGramWeight(const double &gram_weight) {
    m_gram_weight = gram_weight;
    m_gram_weight_isSet = true;
}

bool OAIIngredientObject_items_inner_portions_inner::is_gram_weight_Set() const{
    return m_gram_weight_isSet;
}

bool OAIIngredientObject_items_inner_portions_inner::is_gram_weight_Valid() const{
    return m_gram_weight_isValid;
}

QString OAIIngredientObject_items_inner_portions_inner::getMeasurementUnit() const {
    return m_measurement_unit;
}
void OAIIngredientObject_items_inner_portions_inner::setMeasurementUnit(const QString &measurement_unit) {
    m_measurement_unit = measurement_unit;
    m_measurement_unit_isSet = true;
}

bool OAIIngredientObject_items_inner_portions_inner::is_measurement_unit_Set() const{
    return m_measurement_unit_isSet;
}

bool OAIIngredientObject_items_inner_portions_inner::is_measurement_unit_Valid() const{
    return m_measurement_unit_isValid;
}

QString OAIIngredientObject_items_inner_portions_inner::getModifier() const {
    return m_modifier;
}
void OAIIngredientObject_items_inner_portions_inner::setModifier(const QString &modifier) {
    m_modifier = modifier;
    m_modifier_isSet = true;
}

bool OAIIngredientObject_items_inner_portions_inner::is_modifier_Set() const{
    return m_modifier_isSet;
}

bool OAIIngredientObject_items_inner_portions_inner::is_modifier_Valid() const{
    return m_modifier_isValid;
}

bool OAIIngredientObject_items_inner_portions_inner::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_data_points_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_description_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_footnote_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_gram_weight_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_measurement_unit_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_modifier_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIIngredientObject_items_inner_portions_inner::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
