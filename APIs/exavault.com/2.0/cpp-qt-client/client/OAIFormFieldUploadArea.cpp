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

#include "OAIFormFieldUploadArea.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIFormFieldUploadArea::OAIFormFieldUploadArea(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIFormFieldUploadArea::OAIFormFieldUploadArea() {
    this->initializeModel();
}

OAIFormFieldUploadArea::~OAIFormFieldUploadArea() {}

void OAIFormFieldUploadArea::initializeModel() {

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

void OAIFormFieldUploadArea::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIFormFieldUploadArea::fromJsonObject(QJsonObject json) {

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

QString OAIFormFieldUploadArea::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIFormFieldUploadArea::asJsonObject() const {
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

qint32 OAIFormFieldUploadArea::getId() const {
    return m_id;
}
void OAIFormFieldUploadArea::setId(const qint32 &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIFormFieldUploadArea::is_id_Set() const{
    return m_id_isSet;
}

bool OAIFormFieldUploadArea::is_id_Valid() const{
    return m_id_isValid;
}

QString OAIFormFieldUploadArea::getName() const {
    return m_name;
}
void OAIFormFieldUploadArea::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIFormFieldUploadArea::is_name_Set() const{
    return m_name_isSet;
}

bool OAIFormFieldUploadArea::is_name_Valid() const{
    return m_name_isValid;
}

qint32 OAIFormFieldUploadArea::getOrder() const {
    return m_order;
}
void OAIFormFieldUploadArea::setOrder(const qint32 &order) {
    m_order = order;
    m_order_isSet = true;
}

bool OAIFormFieldUploadArea::is_order_Set() const{
    return m_order_isSet;
}

bool OAIFormFieldUploadArea::is_order_Valid() const{
    return m_order_isValid;
}

OAIFormFieldUploadArea_settings OAIFormFieldUploadArea::getSettings() const {
    return m_settings;
}
void OAIFormFieldUploadArea::setSettings(const OAIFormFieldUploadArea_settings &settings) {
    m_settings = settings;
    m_settings_isSet = true;
}

bool OAIFormFieldUploadArea::is_settings_Set() const{
    return m_settings_isSet;
}

bool OAIFormFieldUploadArea::is_settings_Valid() const{
    return m_settings_isValid;
}

QString OAIFormFieldUploadArea::getType() const {
    return m_type;
}
void OAIFormFieldUploadArea::setType(const QString &type) {
    m_type = type;
    m_type_isSet = true;
}

bool OAIFormFieldUploadArea::is_type_Set() const{
    return m_type_isSet;
}

bool OAIFormFieldUploadArea::is_type_Valid() const{
    return m_type_isValid;
}

bool OAIFormFieldUploadArea::isSet() const {
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

bool OAIFormFieldUploadArea::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
