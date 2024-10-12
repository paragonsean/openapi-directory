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

#include "OAISales_rule_data_coupon_generation_spec_interface.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAISales_rule_data_coupon_generation_spec_interface::OAISales_rule_data_coupon_generation_spec_interface(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAISales_rule_data_coupon_generation_spec_interface::OAISales_rule_data_coupon_generation_spec_interface() {
    this->initializeModel();
}

OAISales_rule_data_coupon_generation_spec_interface::~OAISales_rule_data_coupon_generation_spec_interface() {}

void OAISales_rule_data_coupon_generation_spec_interface::initializeModel() {

    m_delimiter_isSet = false;
    m_delimiter_isValid = false;

    m_delimiter_at_every_isSet = false;
    m_delimiter_at_every_isValid = false;

    m_extension_attributes_isSet = false;
    m_extension_attributes_isValid = false;

    m_format_isSet = false;
    m_format_isValid = false;

    m_length_isSet = false;
    m_length_isValid = false;

    m_prefix_isSet = false;
    m_prefix_isValid = false;

    m_quantity_isSet = false;
    m_quantity_isValid = false;

    m_rule_id_isSet = false;
    m_rule_id_isValid = false;

    m_suffix_isSet = false;
    m_suffix_isValid = false;
}

void OAISales_rule_data_coupon_generation_spec_interface::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAISales_rule_data_coupon_generation_spec_interface::fromJsonObject(QJsonObject json) {

    m_delimiter_isValid = ::OpenAPI::fromJsonValue(m_delimiter, json[QString("delimiter")]);
    m_delimiter_isSet = !json[QString("delimiter")].isNull() && m_delimiter_isValid;

    m_delimiter_at_every_isValid = ::OpenAPI::fromJsonValue(m_delimiter_at_every, json[QString("delimiter_at_every")]);
    m_delimiter_at_every_isSet = !json[QString("delimiter_at_every")].isNull() && m_delimiter_at_every_isValid;

    m_extension_attributes_isValid = ::OpenAPI::fromJsonValue(m_extension_attributes, json[QString("extension_attributes")]);
    m_extension_attributes_isSet = !json[QString("extension_attributes")].isNull() && m_extension_attributes_isValid;

    m_format_isValid = ::OpenAPI::fromJsonValue(m_format, json[QString("format")]);
    m_format_isSet = !json[QString("format")].isNull() && m_format_isValid;

    m_length_isValid = ::OpenAPI::fromJsonValue(m_length, json[QString("length")]);
    m_length_isSet = !json[QString("length")].isNull() && m_length_isValid;

    m_prefix_isValid = ::OpenAPI::fromJsonValue(m_prefix, json[QString("prefix")]);
    m_prefix_isSet = !json[QString("prefix")].isNull() && m_prefix_isValid;

    m_quantity_isValid = ::OpenAPI::fromJsonValue(m_quantity, json[QString("quantity")]);
    m_quantity_isSet = !json[QString("quantity")].isNull() && m_quantity_isValid;

    m_rule_id_isValid = ::OpenAPI::fromJsonValue(m_rule_id, json[QString("rule_id")]);
    m_rule_id_isSet = !json[QString("rule_id")].isNull() && m_rule_id_isValid;

    m_suffix_isValid = ::OpenAPI::fromJsonValue(m_suffix, json[QString("suffix")]);
    m_suffix_isSet = !json[QString("suffix")].isNull() && m_suffix_isValid;
}

QString OAISales_rule_data_coupon_generation_spec_interface::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAISales_rule_data_coupon_generation_spec_interface::asJsonObject() const {
    QJsonObject obj;
    if (m_delimiter_isSet) {
        obj.insert(QString("delimiter"), ::OpenAPI::toJsonValue(m_delimiter));
    }
    if (m_delimiter_at_every_isSet) {
        obj.insert(QString("delimiter_at_every"), ::OpenAPI::toJsonValue(m_delimiter_at_every));
    }
    if (m_extension_attributes_isSet) {
        obj.insert(QString("extension_attributes"), ::OpenAPI::toJsonValue(m_extension_attributes));
    }
    if (m_format_isSet) {
        obj.insert(QString("format"), ::OpenAPI::toJsonValue(m_format));
    }
    if (m_length_isSet) {
        obj.insert(QString("length"), ::OpenAPI::toJsonValue(m_length));
    }
    if (m_prefix_isSet) {
        obj.insert(QString("prefix"), ::OpenAPI::toJsonValue(m_prefix));
    }
    if (m_quantity_isSet) {
        obj.insert(QString("quantity"), ::OpenAPI::toJsonValue(m_quantity));
    }
    if (m_rule_id_isSet) {
        obj.insert(QString("rule_id"), ::OpenAPI::toJsonValue(m_rule_id));
    }
    if (m_suffix_isSet) {
        obj.insert(QString("suffix"), ::OpenAPI::toJsonValue(m_suffix));
    }
    return obj;
}

QString OAISales_rule_data_coupon_generation_spec_interface::getDelimiter() const {
    return m_delimiter;
}
void OAISales_rule_data_coupon_generation_spec_interface::setDelimiter(const QString &delimiter) {
    m_delimiter = delimiter;
    m_delimiter_isSet = true;
}

bool OAISales_rule_data_coupon_generation_spec_interface::is_delimiter_Set() const{
    return m_delimiter_isSet;
}

bool OAISales_rule_data_coupon_generation_spec_interface::is_delimiter_Valid() const{
    return m_delimiter_isValid;
}

qint32 OAISales_rule_data_coupon_generation_spec_interface::getDelimiterAtEvery() const {
    return m_delimiter_at_every;
}
void OAISales_rule_data_coupon_generation_spec_interface::setDelimiterAtEvery(const qint32 &delimiter_at_every) {
    m_delimiter_at_every = delimiter_at_every;
    m_delimiter_at_every_isSet = true;
}

bool OAISales_rule_data_coupon_generation_spec_interface::is_delimiter_at_every_Set() const{
    return m_delimiter_at_every_isSet;
}

bool OAISales_rule_data_coupon_generation_spec_interface::is_delimiter_at_every_Valid() const{
    return m_delimiter_at_every_isValid;
}

OAIObject OAISales_rule_data_coupon_generation_spec_interface::getExtensionAttributes() const {
    return m_extension_attributes;
}
void OAISales_rule_data_coupon_generation_spec_interface::setExtensionAttributes(const OAIObject &extension_attributes) {
    m_extension_attributes = extension_attributes;
    m_extension_attributes_isSet = true;
}

bool OAISales_rule_data_coupon_generation_spec_interface::is_extension_attributes_Set() const{
    return m_extension_attributes_isSet;
}

bool OAISales_rule_data_coupon_generation_spec_interface::is_extension_attributes_Valid() const{
    return m_extension_attributes_isValid;
}

QString OAISales_rule_data_coupon_generation_spec_interface::getFormat() const {
    return m_format;
}
void OAISales_rule_data_coupon_generation_spec_interface::setFormat(const QString &format) {
    m_format = format;
    m_format_isSet = true;
}

bool OAISales_rule_data_coupon_generation_spec_interface::is_format_Set() const{
    return m_format_isSet;
}

bool OAISales_rule_data_coupon_generation_spec_interface::is_format_Valid() const{
    return m_format_isValid;
}

qint32 OAISales_rule_data_coupon_generation_spec_interface::getLength() const {
    return m_length;
}
void OAISales_rule_data_coupon_generation_spec_interface::setLength(const qint32 &length) {
    m_length = length;
    m_length_isSet = true;
}

bool OAISales_rule_data_coupon_generation_spec_interface::is_length_Set() const{
    return m_length_isSet;
}

bool OAISales_rule_data_coupon_generation_spec_interface::is_length_Valid() const{
    return m_length_isValid;
}

QString OAISales_rule_data_coupon_generation_spec_interface::getPrefix() const {
    return m_prefix;
}
void OAISales_rule_data_coupon_generation_spec_interface::setPrefix(const QString &prefix) {
    m_prefix = prefix;
    m_prefix_isSet = true;
}

bool OAISales_rule_data_coupon_generation_spec_interface::is_prefix_Set() const{
    return m_prefix_isSet;
}

bool OAISales_rule_data_coupon_generation_spec_interface::is_prefix_Valid() const{
    return m_prefix_isValid;
}

qint32 OAISales_rule_data_coupon_generation_spec_interface::getQuantity() const {
    return m_quantity;
}
void OAISales_rule_data_coupon_generation_spec_interface::setQuantity(const qint32 &quantity) {
    m_quantity = quantity;
    m_quantity_isSet = true;
}

bool OAISales_rule_data_coupon_generation_spec_interface::is_quantity_Set() const{
    return m_quantity_isSet;
}

bool OAISales_rule_data_coupon_generation_spec_interface::is_quantity_Valid() const{
    return m_quantity_isValid;
}

qint32 OAISales_rule_data_coupon_generation_spec_interface::getRuleId() const {
    return m_rule_id;
}
void OAISales_rule_data_coupon_generation_spec_interface::setRuleId(const qint32 &rule_id) {
    m_rule_id = rule_id;
    m_rule_id_isSet = true;
}

bool OAISales_rule_data_coupon_generation_spec_interface::is_rule_id_Set() const{
    return m_rule_id_isSet;
}

bool OAISales_rule_data_coupon_generation_spec_interface::is_rule_id_Valid() const{
    return m_rule_id_isValid;
}

QString OAISales_rule_data_coupon_generation_spec_interface::getSuffix() const {
    return m_suffix;
}
void OAISales_rule_data_coupon_generation_spec_interface::setSuffix(const QString &suffix) {
    m_suffix = suffix;
    m_suffix_isSet = true;
}

bool OAISales_rule_data_coupon_generation_spec_interface::is_suffix_Set() const{
    return m_suffix_isSet;
}

bool OAISales_rule_data_coupon_generation_spec_interface::is_suffix_Valid() const{
    return m_suffix_isValid;
}

bool OAISales_rule_data_coupon_generation_spec_interface::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_delimiter_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_delimiter_at_every_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_extension_attributes_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_format_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_length_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_prefix_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_quantity_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_rule_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_suffix_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAISales_rule_data_coupon_generation_spec_interface::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_format_isValid && m_length_isValid && m_quantity_isValid && m_rule_id_isValid && true;
}

} // namespace OpenAPI
