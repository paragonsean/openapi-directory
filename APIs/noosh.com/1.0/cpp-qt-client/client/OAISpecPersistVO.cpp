/**
 * Noosh API application
 * Full description of Noosh API
 *
 * The version of the OpenAPI document: 1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAISpecPersistVO.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAISpecPersistVO::OAISpecPersistVO(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAISpecPersistVO::OAISpecPersistVO() {
    this->initializeModel();
}

OAISpecPersistVO::~OAISpecPersistVO() {}

void OAISpecPersistVO::initializeModel() {

    m_json_body_isSet = false;
    m_json_body_isValid = false;

    m_product_type_id_isSet = false;
    m_product_type_id_isValid = false;

    m_quantity_1_isSet = false;
    m_quantity_1_isValid = false;

    m_quantity_2_isSet = false;
    m_quantity_2_isValid = false;

    m_quantity_3_isSet = false;
    m_quantity_3_isValid = false;

    m_quantity_4_isSet = false;
    m_quantity_4_isValid = false;

    m_quantity_5_isSet = false;
    m_quantity_5_isValid = false;

    m_sku_isSet = false;
    m_sku_isValid = false;

    m_spec_name_isSet = false;
    m_spec_name_isValid = false;

    m_spec_template_id_isSet = false;
    m_spec_template_id_isValid = false;

    m_spec_type_id_isSet = false;
    m_spec_type_id_isValid = false;

    m_versions_isSet = false;
    m_versions_isValid = false;
}

void OAISpecPersistVO::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAISpecPersistVO::fromJsonObject(QJsonObject json) {

    m_json_body_isValid = ::OpenAPI::fromJsonValue(m_json_body, json[QString("jsonBody")]);
    m_json_body_isSet = !json[QString("jsonBody")].isNull() && m_json_body_isValid;

    m_product_type_id_isValid = ::OpenAPI::fromJsonValue(m_product_type_id, json[QString("product_type_id")]);
    m_product_type_id_isSet = !json[QString("product_type_id")].isNull() && m_product_type_id_isValid;

    m_quantity_1_isValid = ::OpenAPI::fromJsonValue(m_quantity_1, json[QString("quantity_1")]);
    m_quantity_1_isSet = !json[QString("quantity_1")].isNull() && m_quantity_1_isValid;

    m_quantity_2_isValid = ::OpenAPI::fromJsonValue(m_quantity_2, json[QString("quantity_2")]);
    m_quantity_2_isSet = !json[QString("quantity_2")].isNull() && m_quantity_2_isValid;

    m_quantity_3_isValid = ::OpenAPI::fromJsonValue(m_quantity_3, json[QString("quantity_3")]);
    m_quantity_3_isSet = !json[QString("quantity_3")].isNull() && m_quantity_3_isValid;

    m_quantity_4_isValid = ::OpenAPI::fromJsonValue(m_quantity_4, json[QString("quantity_4")]);
    m_quantity_4_isSet = !json[QString("quantity_4")].isNull() && m_quantity_4_isValid;

    m_quantity_5_isValid = ::OpenAPI::fromJsonValue(m_quantity_5, json[QString("quantity_5")]);
    m_quantity_5_isSet = !json[QString("quantity_5")].isNull() && m_quantity_5_isValid;

    m_sku_isValid = ::OpenAPI::fromJsonValue(m_sku, json[QString("sku")]);
    m_sku_isSet = !json[QString("sku")].isNull() && m_sku_isValid;

    m_spec_name_isValid = ::OpenAPI::fromJsonValue(m_spec_name, json[QString("spec_name")]);
    m_spec_name_isSet = !json[QString("spec_name")].isNull() && m_spec_name_isValid;

    m_spec_template_id_isValid = ::OpenAPI::fromJsonValue(m_spec_template_id, json[QString("spec_template_id")]);
    m_spec_template_id_isSet = !json[QString("spec_template_id")].isNull() && m_spec_template_id_isValid;

    m_spec_type_id_isValid = ::OpenAPI::fromJsonValue(m_spec_type_id, json[QString("spec_type_id")]);
    m_spec_type_id_isSet = !json[QString("spec_type_id")].isNull() && m_spec_type_id_isValid;

    m_versions_isValid = ::OpenAPI::fromJsonValue(m_versions, json[QString("versions")]);
    m_versions_isSet = !json[QString("versions")].isNull() && m_versions_isValid;
}

QString OAISpecPersistVO::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAISpecPersistVO::asJsonObject() const {
    QJsonObject obj;
    if (m_json_body_isSet) {
        obj.insert(QString("jsonBody"), ::OpenAPI::toJsonValue(m_json_body));
    }
    if (m_product_type_id_isSet) {
        obj.insert(QString("product_type_id"), ::OpenAPI::toJsonValue(m_product_type_id));
    }
    if (m_quantity_1_isSet) {
        obj.insert(QString("quantity_1"), ::OpenAPI::toJsonValue(m_quantity_1));
    }
    if (m_quantity_2_isSet) {
        obj.insert(QString("quantity_2"), ::OpenAPI::toJsonValue(m_quantity_2));
    }
    if (m_quantity_3_isSet) {
        obj.insert(QString("quantity_3"), ::OpenAPI::toJsonValue(m_quantity_3));
    }
    if (m_quantity_4_isSet) {
        obj.insert(QString("quantity_4"), ::OpenAPI::toJsonValue(m_quantity_4));
    }
    if (m_quantity_5_isSet) {
        obj.insert(QString("quantity_5"), ::OpenAPI::toJsonValue(m_quantity_5));
    }
    if (m_sku_isSet) {
        obj.insert(QString("sku"), ::OpenAPI::toJsonValue(m_sku));
    }
    if (m_spec_name_isSet) {
        obj.insert(QString("spec_name"), ::OpenAPI::toJsonValue(m_spec_name));
    }
    if (m_spec_template_id_isSet) {
        obj.insert(QString("spec_template_id"), ::OpenAPI::toJsonValue(m_spec_template_id));
    }
    if (m_spec_type_id_isSet) {
        obj.insert(QString("spec_type_id"), ::OpenAPI::toJsonValue(m_spec_type_id));
    }
    if (m_versions.size() > 0) {
        obj.insert(QString("versions"), ::OpenAPI::toJsonValue(m_versions));
    }
    return obj;
}

bool OAISpecPersistVO::isJsonBody() const {
    return m_json_body;
}
void OAISpecPersistVO::setJsonBody(const bool &json_body) {
    m_json_body = json_body;
    m_json_body_isSet = true;
}

bool OAISpecPersistVO::is_json_body_Set() const{
    return m_json_body_isSet;
}

bool OAISpecPersistVO::is_json_body_Valid() const{
    return m_json_body_isValid;
}

qint64 OAISpecPersistVO::getProductTypeId() const {
    return m_product_type_id;
}
void OAISpecPersistVO::setProductTypeId(const qint64 &product_type_id) {
    m_product_type_id = product_type_id;
    m_product_type_id_isSet = true;
}

bool OAISpecPersistVO::is_product_type_id_Set() const{
    return m_product_type_id_isSet;
}

bool OAISpecPersistVO::is_product_type_id_Valid() const{
    return m_product_type_id_isValid;
}

qint64 OAISpecPersistVO::getQuantity1() const {
    return m_quantity_1;
}
void OAISpecPersistVO::setQuantity1(const qint64 &quantity_1) {
    m_quantity_1 = quantity_1;
    m_quantity_1_isSet = true;
}

bool OAISpecPersistVO::is_quantity_1_Set() const{
    return m_quantity_1_isSet;
}

bool OAISpecPersistVO::is_quantity_1_Valid() const{
    return m_quantity_1_isValid;
}

qint64 OAISpecPersistVO::getQuantity2() const {
    return m_quantity_2;
}
void OAISpecPersistVO::setQuantity2(const qint64 &quantity_2) {
    m_quantity_2 = quantity_2;
    m_quantity_2_isSet = true;
}

bool OAISpecPersistVO::is_quantity_2_Set() const{
    return m_quantity_2_isSet;
}

bool OAISpecPersistVO::is_quantity_2_Valid() const{
    return m_quantity_2_isValid;
}

qint64 OAISpecPersistVO::getQuantity3() const {
    return m_quantity_3;
}
void OAISpecPersistVO::setQuantity3(const qint64 &quantity_3) {
    m_quantity_3 = quantity_3;
    m_quantity_3_isSet = true;
}

bool OAISpecPersistVO::is_quantity_3_Set() const{
    return m_quantity_3_isSet;
}

bool OAISpecPersistVO::is_quantity_3_Valid() const{
    return m_quantity_3_isValid;
}

qint64 OAISpecPersistVO::getQuantity4() const {
    return m_quantity_4;
}
void OAISpecPersistVO::setQuantity4(const qint64 &quantity_4) {
    m_quantity_4 = quantity_4;
    m_quantity_4_isSet = true;
}

bool OAISpecPersistVO::is_quantity_4_Set() const{
    return m_quantity_4_isSet;
}

bool OAISpecPersistVO::is_quantity_4_Valid() const{
    return m_quantity_4_isValid;
}

qint64 OAISpecPersistVO::getQuantity5() const {
    return m_quantity_5;
}
void OAISpecPersistVO::setQuantity5(const qint64 &quantity_5) {
    m_quantity_5 = quantity_5;
    m_quantity_5_isSet = true;
}

bool OAISpecPersistVO::is_quantity_5_Set() const{
    return m_quantity_5_isSet;
}

bool OAISpecPersistVO::is_quantity_5_Valid() const{
    return m_quantity_5_isValid;
}

QString OAISpecPersistVO::getSku() const {
    return m_sku;
}
void OAISpecPersistVO::setSku(const QString &sku) {
    m_sku = sku;
    m_sku_isSet = true;
}

bool OAISpecPersistVO::is_sku_Set() const{
    return m_sku_isSet;
}

bool OAISpecPersistVO::is_sku_Valid() const{
    return m_sku_isValid;
}

QString OAISpecPersistVO::getSpecName() const {
    return m_spec_name;
}
void OAISpecPersistVO::setSpecName(const QString &spec_name) {
    m_spec_name = spec_name;
    m_spec_name_isSet = true;
}

bool OAISpecPersistVO::is_spec_name_Set() const{
    return m_spec_name_isSet;
}

bool OAISpecPersistVO::is_spec_name_Valid() const{
    return m_spec_name_isValid;
}

qint64 OAISpecPersistVO::getSpecTemplateId() const {
    return m_spec_template_id;
}
void OAISpecPersistVO::setSpecTemplateId(const qint64 &spec_template_id) {
    m_spec_template_id = spec_template_id;
    m_spec_template_id_isSet = true;
}

bool OAISpecPersistVO::is_spec_template_id_Set() const{
    return m_spec_template_id_isSet;
}

bool OAISpecPersistVO::is_spec_template_id_Valid() const{
    return m_spec_template_id_isValid;
}

qint64 OAISpecPersistVO::getSpecTypeId() const {
    return m_spec_type_id;
}
void OAISpecPersistVO::setSpecTypeId(const qint64 &spec_type_id) {
    m_spec_type_id = spec_type_id;
    m_spec_type_id_isSet = true;
}

bool OAISpecPersistVO::is_spec_type_id_Set() const{
    return m_spec_type_id_isSet;
}

bool OAISpecPersistVO::is_spec_type_id_Valid() const{
    return m_spec_type_id_isValid;
}

QList<OAISpecVersionPersistVO> OAISpecPersistVO::getVersions() const {
    return m_versions;
}
void OAISpecPersistVO::setVersions(const QList<OAISpecVersionPersistVO> &versions) {
    m_versions = versions;
    m_versions_isSet = true;
}

bool OAISpecPersistVO::is_versions_Set() const{
    return m_versions_isSet;
}

bool OAISpecPersistVO::is_versions_Valid() const{
    return m_versions_isValid;
}

bool OAISpecPersistVO::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_json_body_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_product_type_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_quantity_1_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_quantity_2_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_quantity_3_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_quantity_4_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_quantity_5_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_sku_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_spec_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_spec_template_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_spec_type_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_versions.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAISpecPersistVO::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
