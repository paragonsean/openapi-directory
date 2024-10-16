/**
 * ExaVault
 * ExaVaults API allows you to incorporate ExaVaults suite of file transfer and user management tools into your own application.\\nExaVault supports both POST (recommended when requesting large data sets) and GET operations, and requires an API key in order to use.
 *
 * The version of the OpenAPI document: 2.0
 * Contact: support@exavault.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIUpdateFormByIdRequestBody_elements_inner.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIUpdateFormByIdRequestBody_elements_inner::OAIUpdateFormByIdRequestBody_elements_inner(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIUpdateFormByIdRequestBody_elements_inner::OAIUpdateFormByIdRequestBody_elements_inner() {
    this->initializeModel();
}

OAIUpdateFormByIdRequestBody_elements_inner::~OAIUpdateFormByIdRequestBody_elements_inner() {}

void OAIUpdateFormByIdRequestBody_elements_inner::initializeModel() {

    m_id_isSet = false;
    m_id_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_order_isSet = false;
    m_order_isValid = false;

    m_settings_isSet = false;
    m_settings_isValid = false;

    m_type_isSet = false;
    m_type_isValid = false;
}

void OAIUpdateFormByIdRequestBody_elements_inner::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIUpdateFormByIdRequestBody_elements_inner::fromJsonObject(QJsonObject json) {

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_order_isValid = ::OpenAPI::fromJsonValue(m_order, json[QString("order")]);
    m_order_isSet = !json[QString("order")].isNull() && m_order_isValid;

    m_settings_isValid = ::OpenAPI::fromJsonValue(m_settings, json[QString("settings")]);
    m_settings_isSet = !json[QString("settings")].isNull() && m_settings_isValid;

    m_type_isValid = ::OpenAPI::fromJsonValue(m_type, json[QString("type")]);
    m_type_isSet = !json[QString("type")].isNull() && m_type_isValid;
}

QString OAIUpdateFormByIdRequestBody_elements_inner::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIUpdateFormByIdRequestBody_elements_inner::asJsonObject() const {
    QJsonObject obj;
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_order_isSet) {
        obj.insert(QString("order"), ::OpenAPI::toJsonValue(m_order));
    }
    if (m_settings.isSet()) {
        obj.insert(QString("settings"), ::OpenAPI::toJsonValue(m_settings));
    }
    if (m_type_isSet) {
        obj.insert(QString("type"), ::OpenAPI::toJsonValue(m_type));
    }
    return obj;
}

qint32 OAIUpdateFormByIdRequestBody_elements_inner::getId() const {
    return m_id;
}
void OAIUpdateFormByIdRequestBody_elements_inner::setId(const qint32 &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIUpdateFormByIdRequestBody_elements_inner::is_id_Set() const{
    return m_id_isSet;
}

bool OAIUpdateFormByIdRequestBody_elements_inner::is_id_Valid() const{
    return m_id_isValid;
}

QString OAIUpdateFormByIdRequestBody_elements_inner::getName() const {
    return m_name;
}
void OAIUpdateFormByIdRequestBody_elements_inner::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIUpdateFormByIdRequestBody_elements_inner::is_name_Set() const{
    return m_name_isSet;
}

bool OAIUpdateFormByIdRequestBody_elements_inner::is_name_Valid() const{
    return m_name_isValid;
}

qint32 OAIUpdateFormByIdRequestBody_elements_inner::getOrder() const {
    return m_order;
}
void OAIUpdateFormByIdRequestBody_elements_inner::setOrder(const qint32 &order) {
    m_order = order;
    m_order_isSet = true;
}

bool OAIUpdateFormByIdRequestBody_elements_inner::is_order_Set() const{
    return m_order_isSet;
}

bool OAIUpdateFormByIdRequestBody_elements_inner::is_order_Valid() const{
    return m_order_isValid;
}

OAIUpdateFormByIdRequestBody_elements_inner_settings OAIUpdateFormByIdRequestBody_elements_inner::getSettings() const {
    return m_settings;
}
void OAIUpdateFormByIdRequestBody_elements_inner::setSettings(const OAIUpdateFormByIdRequestBody_elements_inner_settings &settings) {
    m_settings = settings;
    m_settings_isSet = true;
}

bool OAIUpdateFormByIdRequestBody_elements_inner::is_settings_Set() const{
    return m_settings_isSet;
}

bool OAIUpdateFormByIdRequestBody_elements_inner::is_settings_Valid() const{
    return m_settings_isValid;
}

QString OAIUpdateFormByIdRequestBody_elements_inner::getType() const {
    return m_type;
}
void OAIUpdateFormByIdRequestBody_elements_inner::setType(const QString &type) {
    m_type = type;
    m_type_isSet = true;
}

bool OAIUpdateFormByIdRequestBody_elements_inner::is_type_Set() const{
    return m_type_isSet;
}

bool OAIUpdateFormByIdRequestBody_elements_inner::is_type_Valid() const{
    return m_type_isValid;
}

bool OAIUpdateFormByIdRequestBody_elements_inner::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_order_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_settings.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_type_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIUpdateFormByIdRequestBody_elements_inner::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
