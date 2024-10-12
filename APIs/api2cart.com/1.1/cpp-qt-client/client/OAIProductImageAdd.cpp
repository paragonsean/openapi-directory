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

#include "OAIProductImageAdd.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIProductImageAdd::OAIProductImageAdd(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIProductImageAdd::OAIProductImageAdd() {
    this->initializeModel();
}

OAIProductImageAdd::~OAIProductImageAdd() {}

void OAIProductImageAdd::initializeModel() {

    m_content_isSet = false;
    m_content_isValid = false;

    m_image_name_isSet = false;
    m_image_name_isValid = false;

    m_label_isSet = false;
    m_label_isValid = false;

    m_lang_id_isSet = false;
    m_lang_id_isValid = false;

    m_mime_isSet = false;
    m_mime_isValid = false;

    m_position_isSet = false;
    m_position_isValid = false;

    m_product_id_isSet = false;
    m_product_id_isValid = false;

    m_product_variant_id_isSet = false;
    m_product_variant_id_isValid = false;

    m_store_id_isSet = false;
    m_store_id_isValid = false;

    m_type_isSet = false;
    m_type_isValid = false;

    m_url_isSet = false;
    m_url_isValid = false;

    m_variant_ids_isSet = false;
    m_variant_ids_isValid = false;
}

void OAIProductImageAdd::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIProductImageAdd::fromJsonObject(QJsonObject json) {

    m_content_isValid = ::OpenAPI::fromJsonValue(m_content, json[QString("content")]);
    m_content_isSet = !json[QString("content")].isNull() && m_content_isValid;

    m_image_name_isValid = ::OpenAPI::fromJsonValue(m_image_name, json[QString("image_name")]);
    m_image_name_isSet = !json[QString("image_name")].isNull() && m_image_name_isValid;

    m_label_isValid = ::OpenAPI::fromJsonValue(m_label, json[QString("label")]);
    m_label_isSet = !json[QString("label")].isNull() && m_label_isValid;

    m_lang_id_isValid = ::OpenAPI::fromJsonValue(m_lang_id, json[QString("lang_id")]);
    m_lang_id_isSet = !json[QString("lang_id")].isNull() && m_lang_id_isValid;

    m_mime_isValid = ::OpenAPI::fromJsonValue(m_mime, json[QString("mime")]);
    m_mime_isSet = !json[QString("mime")].isNull() && m_mime_isValid;

    m_position_isValid = ::OpenAPI::fromJsonValue(m_position, json[QString("position")]);
    m_position_isSet = !json[QString("position")].isNull() && m_position_isValid;

    m_product_id_isValid = ::OpenAPI::fromJsonValue(m_product_id, json[QString("product_id")]);
    m_product_id_isSet = !json[QString("product_id")].isNull() && m_product_id_isValid;

    m_product_variant_id_isValid = ::OpenAPI::fromJsonValue(m_product_variant_id, json[QString("product_variant_id")]);
    m_product_variant_id_isSet = !json[QString("product_variant_id")].isNull() && m_product_variant_id_isValid;

    m_store_id_isValid = ::OpenAPI::fromJsonValue(m_store_id, json[QString("store_id")]);
    m_store_id_isSet = !json[QString("store_id")].isNull() && m_store_id_isValid;

    m_type_isValid = ::OpenAPI::fromJsonValue(m_type, json[QString("type")]);
    m_type_isSet = !json[QString("type")].isNull() && m_type_isValid;

    m_url_isValid = ::OpenAPI::fromJsonValue(m_url, json[QString("url")]);
    m_url_isSet = !json[QString("url")].isNull() && m_url_isValid;

    m_variant_ids_isValid = ::OpenAPI::fromJsonValue(m_variant_ids, json[QString("variant_ids")]);
    m_variant_ids_isSet = !json[QString("variant_ids")].isNull() && m_variant_ids_isValid;
}

QString OAIProductImageAdd::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIProductImageAdd::asJsonObject() const {
    QJsonObject obj;
    if (m_content_isSet) {
        obj.insert(QString("content"), ::OpenAPI::toJsonValue(m_content));
    }
    if (m_image_name_isSet) {
        obj.insert(QString("image_name"), ::OpenAPI::toJsonValue(m_image_name));
    }
    if (m_label_isSet) {
        obj.insert(QString("label"), ::OpenAPI::toJsonValue(m_label));
    }
    if (m_lang_id_isSet) {
        obj.insert(QString("lang_id"), ::OpenAPI::toJsonValue(m_lang_id));
    }
    if (m_mime_isSet) {
        obj.insert(QString("mime"), ::OpenAPI::toJsonValue(m_mime));
    }
    if (m_position_isSet) {
        obj.insert(QString("position"), ::OpenAPI::toJsonValue(m_position));
    }
    if (m_product_id_isSet) {
        obj.insert(QString("product_id"), ::OpenAPI::toJsonValue(m_product_id));
    }
    if (m_product_variant_id_isSet) {
        obj.insert(QString("product_variant_id"), ::OpenAPI::toJsonValue(m_product_variant_id));
    }
    if (m_store_id_isSet) {
        obj.insert(QString("store_id"), ::OpenAPI::toJsonValue(m_store_id));
    }
    if (m_type_isSet) {
        obj.insert(QString("type"), ::OpenAPI::toJsonValue(m_type));
    }
    if (m_url_isSet) {
        obj.insert(QString("url"), ::OpenAPI::toJsonValue(m_url));
    }
    if (m_variant_ids_isSet) {
        obj.insert(QString("variant_ids"), ::OpenAPI::toJsonValue(m_variant_ids));
    }
    return obj;
}

QString OAIProductImageAdd::getContent() const {
    return m_content;
}
void OAIProductImageAdd::setContent(const QString &content) {
    m_content = content;
    m_content_isSet = true;
}

bool OAIProductImageAdd::is_content_Set() const{
    return m_content_isSet;
}

bool OAIProductImageAdd::is_content_Valid() const{
    return m_content_isValid;
}

QString OAIProductImageAdd::getImageName() const {
    return m_image_name;
}
void OAIProductImageAdd::setImageName(const QString &image_name) {
    m_image_name = image_name;
    m_image_name_isSet = true;
}

bool OAIProductImageAdd::is_image_name_Set() const{
    return m_image_name_isSet;
}

bool OAIProductImageAdd::is_image_name_Valid() const{
    return m_image_name_isValid;
}

QString OAIProductImageAdd::getLabel() const {
    return m_label;
}
void OAIProductImageAdd::setLabel(const QString &label) {
    m_label = label;
    m_label_isSet = true;
}

bool OAIProductImageAdd::is_label_Set() const{
    return m_label_isSet;
}

bool OAIProductImageAdd::is_label_Valid() const{
    return m_label_isValid;
}

QString OAIProductImageAdd::getLangId() const {
    return m_lang_id;
}
void OAIProductImageAdd::setLangId(const QString &lang_id) {
    m_lang_id = lang_id;
    m_lang_id_isSet = true;
}

bool OAIProductImageAdd::is_lang_id_Set() const{
    return m_lang_id_isSet;
}

bool OAIProductImageAdd::is_lang_id_Valid() const{
    return m_lang_id_isValid;
}

QString OAIProductImageAdd::getMime() const {
    return m_mime;
}
void OAIProductImageAdd::setMime(const QString &mime) {
    m_mime = mime;
    m_mime_isSet = true;
}

bool OAIProductImageAdd::is_mime_Set() const{
    return m_mime_isSet;
}

bool OAIProductImageAdd::is_mime_Valid() const{
    return m_mime_isValid;
}

qint32 OAIProductImageAdd::getPosition() const {
    return m_position;
}
void OAIProductImageAdd::setPosition(const qint32 &position) {
    m_position = position;
    m_position_isSet = true;
}

bool OAIProductImageAdd::is_position_Set() const{
    return m_position_isSet;
}

bool OAIProductImageAdd::is_position_Valid() const{
    return m_position_isValid;
}

QString OAIProductImageAdd::getProductId() const {
    return m_product_id;
}
void OAIProductImageAdd::setProductId(const QString &product_id) {
    m_product_id = product_id;
    m_product_id_isSet = true;
}

bool OAIProductImageAdd::is_product_id_Set() const{
    return m_product_id_isSet;
}

bool OAIProductImageAdd::is_product_id_Valid() const{
    return m_product_id_isValid;
}

qint32 OAIProductImageAdd::getProductVariantId() const {
    return m_product_variant_id;
}
void OAIProductImageAdd::setProductVariantId(const qint32 &product_variant_id) {
    m_product_variant_id = product_variant_id;
    m_product_variant_id_isSet = true;
}

bool OAIProductImageAdd::is_product_variant_id_Set() const{
    return m_product_variant_id_isSet;
}

bool OAIProductImageAdd::is_product_variant_id_Valid() const{
    return m_product_variant_id_isValid;
}

QString OAIProductImageAdd::getStoreId() const {
    return m_store_id;
}
void OAIProductImageAdd::setStoreId(const QString &store_id) {
    m_store_id = store_id;
    m_store_id_isSet = true;
}

bool OAIProductImageAdd::is_store_id_Set() const{
    return m_store_id_isSet;
}

bool OAIProductImageAdd::is_store_id_Valid() const{
    return m_store_id_isValid;
}

QString OAIProductImageAdd::getType() const {
    return m_type;
}
void OAIProductImageAdd::setType(const QString &type) {
    m_type = type;
    m_type_isSet = true;
}

bool OAIProductImageAdd::is_type_Set() const{
    return m_type_isSet;
}

bool OAIProductImageAdd::is_type_Valid() const{
    return m_type_isValid;
}

QString OAIProductImageAdd::getUrl() const {
    return m_url;
}
void OAIProductImageAdd::setUrl(const QString &url) {
    m_url = url;
    m_url_isSet = true;
}

bool OAIProductImageAdd::is_url_Set() const{
    return m_url_isSet;
}

bool OAIProductImageAdd::is_url_Valid() const{
    return m_url_isValid;
}

QString OAIProductImageAdd::getVariantIds() const {
    return m_variant_ids;
}
void OAIProductImageAdd::setVariantIds(const QString &variant_ids) {
    m_variant_ids = variant_ids;
    m_variant_ids_isSet = true;
}

bool OAIProductImageAdd::is_variant_ids_Set() const{
    return m_variant_ids_isSet;
}

bool OAIProductImageAdd::is_variant_ids_Valid() const{
    return m_variant_ids_isValid;
}

bool OAIProductImageAdd::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_content_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_image_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_label_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_lang_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_mime_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_position_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_product_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_product_variant_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_store_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_type_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_url_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_variant_ids_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIProductImageAdd::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_image_name_isValid && m_type_isValid && true;
}

} // namespace OpenAPI
