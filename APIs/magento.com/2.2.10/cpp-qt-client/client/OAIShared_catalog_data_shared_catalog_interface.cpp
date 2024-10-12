/**
 * Magento B2B
 * Magento Commerce is the leading provider of open omnichannel innovation.
 *
 * The version of the OpenAPI document: 2.2.10
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIShared_catalog_data_shared_catalog_interface.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIShared_catalog_data_shared_catalog_interface::OAIShared_catalog_data_shared_catalog_interface(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIShared_catalog_data_shared_catalog_interface::OAIShared_catalog_data_shared_catalog_interface() {
    this->initializeModel();
}

OAIShared_catalog_data_shared_catalog_interface::~OAIShared_catalog_data_shared_catalog_interface() {}

void OAIShared_catalog_data_shared_catalog_interface::initializeModel() {

    m_created_at_isSet = false;
    m_created_at_isValid = false;

    m_created_by_isSet = false;
    m_created_by_isValid = false;

    m_customer_group_id_isSet = false;
    m_customer_group_id_isValid = false;

    m_description_isSet = false;
    m_description_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_store_id_isSet = false;
    m_store_id_isValid = false;

    m_tax_class_id_isSet = false;
    m_tax_class_id_isValid = false;

    m_type_isSet = false;
    m_type_isValid = false;
}

void OAIShared_catalog_data_shared_catalog_interface::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIShared_catalog_data_shared_catalog_interface::fromJsonObject(QJsonObject json) {

    m_created_at_isValid = ::OpenAPI::fromJsonValue(m_created_at, json[QString("created_at")]);
    m_created_at_isSet = !json[QString("created_at")].isNull() && m_created_at_isValid;

    m_created_by_isValid = ::OpenAPI::fromJsonValue(m_created_by, json[QString("created_by")]);
    m_created_by_isSet = !json[QString("created_by")].isNull() && m_created_by_isValid;

    m_customer_group_id_isValid = ::OpenAPI::fromJsonValue(m_customer_group_id, json[QString("customer_group_id")]);
    m_customer_group_id_isSet = !json[QString("customer_group_id")].isNull() && m_customer_group_id_isValid;

    m_description_isValid = ::OpenAPI::fromJsonValue(m_description, json[QString("description")]);
    m_description_isSet = !json[QString("description")].isNull() && m_description_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_store_id_isValid = ::OpenAPI::fromJsonValue(m_store_id, json[QString("store_id")]);
    m_store_id_isSet = !json[QString("store_id")].isNull() && m_store_id_isValid;

    m_tax_class_id_isValid = ::OpenAPI::fromJsonValue(m_tax_class_id, json[QString("tax_class_id")]);
    m_tax_class_id_isSet = !json[QString("tax_class_id")].isNull() && m_tax_class_id_isValid;

    m_type_isValid = ::OpenAPI::fromJsonValue(m_type, json[QString("type")]);
    m_type_isSet = !json[QString("type")].isNull() && m_type_isValid;
}

QString OAIShared_catalog_data_shared_catalog_interface::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIShared_catalog_data_shared_catalog_interface::asJsonObject() const {
    QJsonObject obj;
    if (m_created_at_isSet) {
        obj.insert(QString("created_at"), ::OpenAPI::toJsonValue(m_created_at));
    }
    if (m_created_by_isSet) {
        obj.insert(QString("created_by"), ::OpenAPI::toJsonValue(m_created_by));
    }
    if (m_customer_group_id_isSet) {
        obj.insert(QString("customer_group_id"), ::OpenAPI::toJsonValue(m_customer_group_id));
    }
    if (m_description_isSet) {
        obj.insert(QString("description"), ::OpenAPI::toJsonValue(m_description));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_store_id_isSet) {
        obj.insert(QString("store_id"), ::OpenAPI::toJsonValue(m_store_id));
    }
    if (m_tax_class_id_isSet) {
        obj.insert(QString("tax_class_id"), ::OpenAPI::toJsonValue(m_tax_class_id));
    }
    if (m_type_isSet) {
        obj.insert(QString("type"), ::OpenAPI::toJsonValue(m_type));
    }
    return obj;
}

QString OAIShared_catalog_data_shared_catalog_interface::getCreatedAt() const {
    return m_created_at;
}
void OAIShared_catalog_data_shared_catalog_interface::setCreatedAt(const QString &created_at) {
    m_created_at = created_at;
    m_created_at_isSet = true;
}

bool OAIShared_catalog_data_shared_catalog_interface::is_created_at_Set() const{
    return m_created_at_isSet;
}

bool OAIShared_catalog_data_shared_catalog_interface::is_created_at_Valid() const{
    return m_created_at_isValid;
}

qint32 OAIShared_catalog_data_shared_catalog_interface::getCreatedBy() const {
    return m_created_by;
}
void OAIShared_catalog_data_shared_catalog_interface::setCreatedBy(const qint32 &created_by) {
    m_created_by = created_by;
    m_created_by_isSet = true;
}

bool OAIShared_catalog_data_shared_catalog_interface::is_created_by_Set() const{
    return m_created_by_isSet;
}

bool OAIShared_catalog_data_shared_catalog_interface::is_created_by_Valid() const{
    return m_created_by_isValid;
}

qint32 OAIShared_catalog_data_shared_catalog_interface::getCustomerGroupId() const {
    return m_customer_group_id;
}
void OAIShared_catalog_data_shared_catalog_interface::setCustomerGroupId(const qint32 &customer_group_id) {
    m_customer_group_id = customer_group_id;
    m_customer_group_id_isSet = true;
}

bool OAIShared_catalog_data_shared_catalog_interface::is_customer_group_id_Set() const{
    return m_customer_group_id_isSet;
}

bool OAIShared_catalog_data_shared_catalog_interface::is_customer_group_id_Valid() const{
    return m_customer_group_id_isValid;
}

QString OAIShared_catalog_data_shared_catalog_interface::getDescription() const {
    return m_description;
}
void OAIShared_catalog_data_shared_catalog_interface::setDescription(const QString &description) {
    m_description = description;
    m_description_isSet = true;
}

bool OAIShared_catalog_data_shared_catalog_interface::is_description_Set() const{
    return m_description_isSet;
}

bool OAIShared_catalog_data_shared_catalog_interface::is_description_Valid() const{
    return m_description_isValid;
}

qint32 OAIShared_catalog_data_shared_catalog_interface::getId() const {
    return m_id;
}
void OAIShared_catalog_data_shared_catalog_interface::setId(const qint32 &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIShared_catalog_data_shared_catalog_interface::is_id_Set() const{
    return m_id_isSet;
}

bool OAIShared_catalog_data_shared_catalog_interface::is_id_Valid() const{
    return m_id_isValid;
}

QString OAIShared_catalog_data_shared_catalog_interface::getName() const {
    return m_name;
}
void OAIShared_catalog_data_shared_catalog_interface::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIShared_catalog_data_shared_catalog_interface::is_name_Set() const{
    return m_name_isSet;
}

bool OAIShared_catalog_data_shared_catalog_interface::is_name_Valid() const{
    return m_name_isValid;
}

qint32 OAIShared_catalog_data_shared_catalog_interface::getStoreId() const {
    return m_store_id;
}
void OAIShared_catalog_data_shared_catalog_interface::setStoreId(const qint32 &store_id) {
    m_store_id = store_id;
    m_store_id_isSet = true;
}

bool OAIShared_catalog_data_shared_catalog_interface::is_store_id_Set() const{
    return m_store_id_isSet;
}

bool OAIShared_catalog_data_shared_catalog_interface::is_store_id_Valid() const{
    return m_store_id_isValid;
}

qint32 OAIShared_catalog_data_shared_catalog_interface::getTaxClassId() const {
    return m_tax_class_id;
}
void OAIShared_catalog_data_shared_catalog_interface::setTaxClassId(const qint32 &tax_class_id) {
    m_tax_class_id = tax_class_id;
    m_tax_class_id_isSet = true;
}

bool OAIShared_catalog_data_shared_catalog_interface::is_tax_class_id_Set() const{
    return m_tax_class_id_isSet;
}

bool OAIShared_catalog_data_shared_catalog_interface::is_tax_class_id_Valid() const{
    return m_tax_class_id_isValid;
}

qint32 OAIShared_catalog_data_shared_catalog_interface::getType() const {
    return m_type;
}
void OAIShared_catalog_data_shared_catalog_interface::setType(const qint32 &type) {
    m_type = type;
    m_type_isSet = true;
}

bool OAIShared_catalog_data_shared_catalog_interface::is_type_Set() const{
    return m_type_isSet;
}

bool OAIShared_catalog_data_shared_catalog_interface::is_type_Valid() const{
    return m_type_isValid;
}

bool OAIShared_catalog_data_shared_catalog_interface::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_created_at_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_created_by_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_customer_group_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_description_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_store_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_tax_class_id_isSet) {
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

bool OAIShared_catalog_data_shared_catalog_interface::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_created_at_isValid && m_created_by_isValid && m_customer_group_id_isValid && m_description_isValid && m_name_isValid && m_store_id_isValid && m_tax_class_id_isValid && m_type_isValid && true;
}

} // namespace OpenAPI
