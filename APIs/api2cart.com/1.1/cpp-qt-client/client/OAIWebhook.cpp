/**
 * Swagger API2Cart
 * API2Cart
 *
 * The version of the OpenAPI document: 1.1
 * Contact: contact@api2cart.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIWebhook.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIWebhook::OAIWebhook(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIWebhook::OAIWebhook() {
    this->initializeModel();
}

OAIWebhook::~OAIWebhook() {}

void OAIWebhook::initializeModel() {

    m_action_isSet = false;
    m_action_isValid = false;

    m_active_isSet = false;
    m_active_isValid = false;

    m_additional_fields_isSet = false;
    m_additional_fields_isValid = false;

    m_callback_isSet = false;
    m_callback_isValid = false;

    m_created_at_isSet = false;
    m_created_at_isValid = false;

    m_custom_fields_isSet = false;
    m_custom_fields_isValid = false;

    m_entity_isSet = false;
    m_entity_isValid = false;

    m_fields_isSet = false;
    m_fields_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_label_isSet = false;
    m_label_isValid = false;

    m_store_id_isSet = false;
    m_store_id_isValid = false;

    m_updated_at_isSet = false;
    m_updated_at_isValid = false;
}

void OAIWebhook::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIWebhook::fromJsonObject(QJsonObject json) {

    m_action_isValid = ::OpenAPI::fromJsonValue(m_action, json[QString("action")]);
    m_action_isSet = !json[QString("action")].isNull() && m_action_isValid;

    m_active_isValid = ::OpenAPI::fromJsonValue(m_active, json[QString("active")]);
    m_active_isSet = !json[QString("active")].isNull() && m_active_isValid;

    m_additional_fields_isValid = ::OpenAPI::fromJsonValue(m_additional_fields, json[QString("additional_fields")]);
    m_additional_fields_isSet = !json[QString("additional_fields")].isNull() && m_additional_fields_isValid;

    m_callback_isValid = ::OpenAPI::fromJsonValue(m_callback, json[QString("callback")]);
    m_callback_isSet = !json[QString("callback")].isNull() && m_callback_isValid;

    m_created_at_isValid = ::OpenAPI::fromJsonValue(m_created_at, json[QString("created_at")]);
    m_created_at_isSet = !json[QString("created_at")].isNull() && m_created_at_isValid;

    m_custom_fields_isValid = ::OpenAPI::fromJsonValue(m_custom_fields, json[QString("custom_fields")]);
    m_custom_fields_isSet = !json[QString("custom_fields")].isNull() && m_custom_fields_isValid;

    m_entity_isValid = ::OpenAPI::fromJsonValue(m_entity, json[QString("entity")]);
    m_entity_isSet = !json[QString("entity")].isNull() && m_entity_isValid;

    m_fields_isValid = ::OpenAPI::fromJsonValue(m_fields, json[QString("fields")]);
    m_fields_isSet = !json[QString("fields")].isNull() && m_fields_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_label_isValid = ::OpenAPI::fromJsonValue(m_label, json[QString("label")]);
    m_label_isSet = !json[QString("label")].isNull() && m_label_isValid;

    m_store_id_isValid = ::OpenAPI::fromJsonValue(m_store_id, json[QString("store_id")]);
    m_store_id_isSet = !json[QString("store_id")].isNull() && m_store_id_isValid;

    m_updated_at_isValid = ::OpenAPI::fromJsonValue(m_updated_at, json[QString("updated_at")]);
    m_updated_at_isSet = !json[QString("updated_at")].isNull() && m_updated_at_isValid;
}

QString OAIWebhook::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIWebhook::asJsonObject() const {
    QJsonObject obj;
    if (m_action_isSet) {
        obj.insert(QString("action"), ::OpenAPI::toJsonValue(m_action));
    }
    if (m_active_isSet) {
        obj.insert(QString("active"), ::OpenAPI::toJsonValue(m_active));
    }
    if (m_additional_fields_isSet) {
        obj.insert(QString("additional_fields"), ::OpenAPI::toJsonValue(m_additional_fields));
    }
    if (m_callback_isSet) {
        obj.insert(QString("callback"), ::OpenAPI::toJsonValue(m_callback));
    }
    if (m_created_at_isSet) {
        obj.insert(QString("created_at"), ::OpenAPI::toJsonValue(m_created_at));
    }
    if (m_custom_fields_isSet) {
        obj.insert(QString("custom_fields"), ::OpenAPI::toJsonValue(m_custom_fields));
    }
    if (m_entity_isSet) {
        obj.insert(QString("entity"), ::OpenAPI::toJsonValue(m_entity));
    }
    if (m_fields_isSet) {
        obj.insert(QString("fields"), ::OpenAPI::toJsonValue(m_fields));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_label_isSet) {
        obj.insert(QString("label"), ::OpenAPI::toJsonValue(m_label));
    }
    if (m_store_id_isSet) {
        obj.insert(QString("store_id"), ::OpenAPI::toJsonValue(m_store_id));
    }
    if (m_updated_at_isSet) {
        obj.insert(QString("updated_at"), ::OpenAPI::toJsonValue(m_updated_at));
    }
    return obj;
}

QString OAIWebhook::getAction() const {
    return m_action;
}
void OAIWebhook::setAction(const QString &action) {
    m_action = action;
    m_action_isSet = true;
}

bool OAIWebhook::is_action_Set() const{
    return m_action_isSet;
}

bool OAIWebhook::is_action_Valid() const{
    return m_action_isValid;
}

bool OAIWebhook::isActive() const {
    return m_active;
}
void OAIWebhook::setActive(const bool &active) {
    m_active = active;
    m_active_isSet = true;
}

bool OAIWebhook::is_active_Set() const{
    return m_active_isSet;
}

bool OAIWebhook::is_active_Valid() const{
    return m_active_isValid;
}

OAIObject OAIWebhook::getAdditionalFields() const {
    return m_additional_fields;
}
void OAIWebhook::setAdditionalFields(const OAIObject &additional_fields) {
    m_additional_fields = additional_fields;
    m_additional_fields_isSet = true;
}

bool OAIWebhook::is_additional_fields_Set() const{
    return m_additional_fields_isSet;
}

bool OAIWebhook::is_additional_fields_Valid() const{
    return m_additional_fields_isValid;
}

QString OAIWebhook::getCallback() const {
    return m_callback;
}
void OAIWebhook::setCallback(const QString &callback) {
    m_callback = callback;
    m_callback_isSet = true;
}

bool OAIWebhook::is_callback_Set() const{
    return m_callback_isSet;
}

bool OAIWebhook::is_callback_Valid() const{
    return m_callback_isValid;
}

QString OAIWebhook::getCreatedAt() const {
    return m_created_at;
}
void OAIWebhook::setCreatedAt(const QString &created_at) {
    m_created_at = created_at;
    m_created_at_isSet = true;
}

bool OAIWebhook::is_created_at_Set() const{
    return m_created_at_isSet;
}

bool OAIWebhook::is_created_at_Valid() const{
    return m_created_at_isValid;
}

OAIObject OAIWebhook::getCustomFields() const {
    return m_custom_fields;
}
void OAIWebhook::setCustomFields(const OAIObject &custom_fields) {
    m_custom_fields = custom_fields;
    m_custom_fields_isSet = true;
}

bool OAIWebhook::is_custom_fields_Set() const{
    return m_custom_fields_isSet;
}

bool OAIWebhook::is_custom_fields_Valid() const{
    return m_custom_fields_isValid;
}

QString OAIWebhook::getEntity() const {
    return m_entity;
}
void OAIWebhook::setEntity(const QString &entity) {
    m_entity = entity;
    m_entity_isSet = true;
}

bool OAIWebhook::is_entity_Set() const{
    return m_entity_isSet;
}

bool OAIWebhook::is_entity_Valid() const{
    return m_entity_isValid;
}

QString OAIWebhook::getFields() const {
    return m_fields;
}
void OAIWebhook::setFields(const QString &fields) {
    m_fields = fields;
    m_fields_isSet = true;
}

bool OAIWebhook::is_fields_Set() const{
    return m_fields_isSet;
}

bool OAIWebhook::is_fields_Valid() const{
    return m_fields_isValid;
}

qint32 OAIWebhook::getId() const {
    return m_id;
}
void OAIWebhook::setId(const qint32 &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIWebhook::is_id_Set() const{
    return m_id_isSet;
}

bool OAIWebhook::is_id_Valid() const{
    return m_id_isValid;
}

QString OAIWebhook::getLabel() const {
    return m_label;
}
void OAIWebhook::setLabel(const QString &label) {
    m_label = label;
    m_label_isSet = true;
}

bool OAIWebhook::is_label_Set() const{
    return m_label_isSet;
}

bool OAIWebhook::is_label_Valid() const{
    return m_label_isValid;
}

QString OAIWebhook::getStoreId() const {
    return m_store_id;
}
void OAIWebhook::setStoreId(const QString &store_id) {
    m_store_id = store_id;
    m_store_id_isSet = true;
}

bool OAIWebhook::is_store_id_Set() const{
    return m_store_id_isSet;
}

bool OAIWebhook::is_store_id_Valid() const{
    return m_store_id_isValid;
}

QString OAIWebhook::getUpdatedAt() const {
    return m_updated_at;
}
void OAIWebhook::setUpdatedAt(const QString &updated_at) {
    m_updated_at = updated_at;
    m_updated_at_isSet = true;
}

bool OAIWebhook::is_updated_at_Set() const{
    return m_updated_at_isSet;
}

bool OAIWebhook::is_updated_at_Valid() const{
    return m_updated_at_isValid;
}

bool OAIWebhook::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_action_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_active_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_additional_fields_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_callback_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_created_at_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_custom_fields_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_entity_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_fields_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_label_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_store_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_updated_at_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIWebhook::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
