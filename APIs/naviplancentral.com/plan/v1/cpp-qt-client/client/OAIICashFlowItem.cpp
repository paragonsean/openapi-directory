/**
 * NaviPlan API
 * An API for accessing NaviPlan plan data for a client.
 *
 * The version of the OpenAPI document: v1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIICashFlowItem.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIICashFlowItem::OAIICashFlowItem(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIICashFlowItem::OAIICashFlowItem() {
    this->initializeModel();
}

OAIICashFlowItem::~OAIICashFlowItem() {}

void OAIICashFlowItem::initializeModel() {

    m_description_isSet = false;
    m_description_isValid = false;

    m_description_with_owner_isSet = false;
    m_description_with_owner_isValid = false;

    m_is_cpp_isSet = false;
    m_is_cpp_isValid = false;

    m_is_oas_isSet = false;
    m_is_oas_isValid = false;

    m_source_id_isSet = false;
    m_source_id_isValid = false;

    m_type_description_isSet = false;
    m_type_description_isValid = false;

    m_value_isSet = false;
    m_value_isValid = false;
}

void OAIICashFlowItem::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIICashFlowItem::fromJsonObject(QJsonObject json) {

    m_description_isValid = ::OpenAPI::fromJsonValue(m_description, json[QString("description")]);
    m_description_isSet = !json[QString("description")].isNull() && m_description_isValid;

    m_description_with_owner_isValid = ::OpenAPI::fromJsonValue(m_description_with_owner, json[QString("descriptionWithOwner")]);
    m_description_with_owner_isSet = !json[QString("descriptionWithOwner")].isNull() && m_description_with_owner_isValid;

    m_is_cpp_isValid = ::OpenAPI::fromJsonValue(m_is_cpp, json[QString("isCPP")]);
    m_is_cpp_isSet = !json[QString("isCPP")].isNull() && m_is_cpp_isValid;

    m_is_oas_isValid = ::OpenAPI::fromJsonValue(m_is_oas, json[QString("isOAS")]);
    m_is_oas_isSet = !json[QString("isOAS")].isNull() && m_is_oas_isValid;

    m_source_id_isValid = ::OpenAPI::fromJsonValue(m_source_id, json[QString("sourceId")]);
    m_source_id_isSet = !json[QString("sourceId")].isNull() && m_source_id_isValid;

    m_type_description_isValid = ::OpenAPI::fromJsonValue(m_type_description, json[QString("typeDescription")]);
    m_type_description_isSet = !json[QString("typeDescription")].isNull() && m_type_description_isValid;

    m_value_isValid = ::OpenAPI::fromJsonValue(m_value, json[QString("value")]);
    m_value_isSet = !json[QString("value")].isNull() && m_value_isValid;
}

QString OAIICashFlowItem::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIICashFlowItem::asJsonObject() const {
    QJsonObject obj;
    if (m_description_isSet) {
        obj.insert(QString("description"), ::OpenAPI::toJsonValue(m_description));
    }
    if (m_description_with_owner_isSet) {
        obj.insert(QString("descriptionWithOwner"), ::OpenAPI::toJsonValue(m_description_with_owner));
    }
    if (m_is_cpp_isSet) {
        obj.insert(QString("isCPP"), ::OpenAPI::toJsonValue(m_is_cpp));
    }
    if (m_is_oas_isSet) {
        obj.insert(QString("isOAS"), ::OpenAPI::toJsonValue(m_is_oas));
    }
    if (m_source_id_isSet) {
        obj.insert(QString("sourceId"), ::OpenAPI::toJsonValue(m_source_id));
    }
    if (m_type_description_isSet) {
        obj.insert(QString("typeDescription"), ::OpenAPI::toJsonValue(m_type_description));
    }
    if (m_value.isSet()) {
        obj.insert(QString("value"), ::OpenAPI::toJsonValue(m_value));
    }
    return obj;
}

QString OAIICashFlowItem::getDescription() const {
    return m_description;
}
void OAIICashFlowItem::setDescription(const QString &description) {
    m_description = description;
    m_description_isSet = true;
}

bool OAIICashFlowItem::is_description_Set() const{
    return m_description_isSet;
}

bool OAIICashFlowItem::is_description_Valid() const{
    return m_description_isValid;
}

QString OAIICashFlowItem::getDescriptionWithOwner() const {
    return m_description_with_owner;
}
void OAIICashFlowItem::setDescriptionWithOwner(const QString &description_with_owner) {
    m_description_with_owner = description_with_owner;
    m_description_with_owner_isSet = true;
}

bool OAIICashFlowItem::is_description_with_owner_Set() const{
    return m_description_with_owner_isSet;
}

bool OAIICashFlowItem::is_description_with_owner_Valid() const{
    return m_description_with_owner_isValid;
}

bool OAIICashFlowItem::isIsCpp() const {
    return m_is_cpp;
}
void OAIICashFlowItem::setIsCpp(const bool &is_cpp) {
    m_is_cpp = is_cpp;
    m_is_cpp_isSet = true;
}

bool OAIICashFlowItem::is_is_cpp_Set() const{
    return m_is_cpp_isSet;
}

bool OAIICashFlowItem::is_is_cpp_Valid() const{
    return m_is_cpp_isValid;
}

bool OAIICashFlowItem::isIsOas() const {
    return m_is_oas;
}
void OAIICashFlowItem::setIsOas(const bool &is_oas) {
    m_is_oas = is_oas;
    m_is_oas_isSet = true;
}

bool OAIICashFlowItem::is_is_oas_Set() const{
    return m_is_oas_isSet;
}

bool OAIICashFlowItem::is_is_oas_Valid() const{
    return m_is_oas_isValid;
}

QString OAIICashFlowItem::getSourceId() const {
    return m_source_id;
}
void OAIICashFlowItem::setSourceId(const QString &source_id) {
    m_source_id = source_id;
    m_source_id_isSet = true;
}

bool OAIICashFlowItem::is_source_id_Set() const{
    return m_source_id_isSet;
}

bool OAIICashFlowItem::is_source_id_Valid() const{
    return m_source_id_isValid;
}

QString OAIICashFlowItem::getTypeDescription() const {
    return m_type_description;
}
void OAIICashFlowItem::setTypeDescription(const QString &type_description) {
    m_type_description = type_description;
    m_type_description_isSet = true;
}

bool OAIICashFlowItem::is_type_description_Set() const{
    return m_type_description_isSet;
}

bool OAIICashFlowItem::is_type_description_Valid() const{
    return m_type_description_isValid;
}

OAICurrency OAIICashFlowItem::getValue() const {
    return m_value;
}
void OAIICashFlowItem::setValue(const OAICurrency &value) {
    m_value = value;
    m_value_isSet = true;
}

bool OAIICashFlowItem::is_value_Set() const{
    return m_value_isSet;
}

bool OAIICashFlowItem::is_value_Valid() const{
    return m_value_isValid;
}

bool OAIICashFlowItem::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_description_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_description_with_owner_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_cpp_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_oas_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_source_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_type_description_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_value.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIICashFlowItem::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
