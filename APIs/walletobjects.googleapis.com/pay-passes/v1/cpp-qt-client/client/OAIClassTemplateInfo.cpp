/**
 * Google Pay Passes API
 * API for issuers to save and manage Google Wallet Objects.
 *
 * The version of the OpenAPI document: v1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIClassTemplateInfo.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIClassTemplateInfo::OAIClassTemplateInfo(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIClassTemplateInfo::OAIClassTemplateInfo() {
    this->initializeModel();
}

OAIClassTemplateInfo::~OAIClassTemplateInfo() {}

void OAIClassTemplateInfo::initializeModel() {

    m_card_barcode_section_details_isSet = false;
    m_card_barcode_section_details_isValid = false;

    m_card_template_override_isSet = false;
    m_card_template_override_isValid = false;

    m_details_template_override_isSet = false;
    m_details_template_override_isValid = false;

    m_list_template_override_isSet = false;
    m_list_template_override_isValid = false;
}

void OAIClassTemplateInfo::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIClassTemplateInfo::fromJsonObject(QJsonObject json) {

    m_card_barcode_section_details_isValid = ::OpenAPI::fromJsonValue(m_card_barcode_section_details, json[QString("cardBarcodeSectionDetails")]);
    m_card_barcode_section_details_isSet = !json[QString("cardBarcodeSectionDetails")].isNull() && m_card_barcode_section_details_isValid;

    m_card_template_override_isValid = ::OpenAPI::fromJsonValue(m_card_template_override, json[QString("cardTemplateOverride")]);
    m_card_template_override_isSet = !json[QString("cardTemplateOverride")].isNull() && m_card_template_override_isValid;

    m_details_template_override_isValid = ::OpenAPI::fromJsonValue(m_details_template_override, json[QString("detailsTemplateOverride")]);
    m_details_template_override_isSet = !json[QString("detailsTemplateOverride")].isNull() && m_details_template_override_isValid;

    m_list_template_override_isValid = ::OpenAPI::fromJsonValue(m_list_template_override, json[QString("listTemplateOverride")]);
    m_list_template_override_isSet = !json[QString("listTemplateOverride")].isNull() && m_list_template_override_isValid;
}

QString OAIClassTemplateInfo::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIClassTemplateInfo::asJsonObject() const {
    QJsonObject obj;
    if (m_card_barcode_section_details.isSet()) {
        obj.insert(QString("cardBarcodeSectionDetails"), ::OpenAPI::toJsonValue(m_card_barcode_section_details));
    }
    if (m_card_template_override.isSet()) {
        obj.insert(QString("cardTemplateOverride"), ::OpenAPI::toJsonValue(m_card_template_override));
    }
    if (m_details_template_override.isSet()) {
        obj.insert(QString("detailsTemplateOverride"), ::OpenAPI::toJsonValue(m_details_template_override));
    }
    if (m_list_template_override.isSet()) {
        obj.insert(QString("listTemplateOverride"), ::OpenAPI::toJsonValue(m_list_template_override));
    }
    return obj;
}

OAICardBarcodeSectionDetails OAIClassTemplateInfo::getCardBarcodeSectionDetails() const {
    return m_card_barcode_section_details;
}
void OAIClassTemplateInfo::setCardBarcodeSectionDetails(const OAICardBarcodeSectionDetails &card_barcode_section_details) {
    m_card_barcode_section_details = card_barcode_section_details;
    m_card_barcode_section_details_isSet = true;
}

bool OAIClassTemplateInfo::is_card_barcode_section_details_Set() const{
    return m_card_barcode_section_details_isSet;
}

bool OAIClassTemplateInfo::is_card_barcode_section_details_Valid() const{
    return m_card_barcode_section_details_isValid;
}

OAICardTemplateOverride OAIClassTemplateInfo::getCardTemplateOverride() const {
    return m_card_template_override;
}
void OAIClassTemplateInfo::setCardTemplateOverride(const OAICardTemplateOverride &card_template_override) {
    m_card_template_override = card_template_override;
    m_card_template_override_isSet = true;
}

bool OAIClassTemplateInfo::is_card_template_override_Set() const{
    return m_card_template_override_isSet;
}

bool OAIClassTemplateInfo::is_card_template_override_Valid() const{
    return m_card_template_override_isValid;
}

OAIDetailsTemplateOverride OAIClassTemplateInfo::getDetailsTemplateOverride() const {
    return m_details_template_override;
}
void OAIClassTemplateInfo::setDetailsTemplateOverride(const OAIDetailsTemplateOverride &details_template_override) {
    m_details_template_override = details_template_override;
    m_details_template_override_isSet = true;
}

bool OAIClassTemplateInfo::is_details_template_override_Set() const{
    return m_details_template_override_isSet;
}

bool OAIClassTemplateInfo::is_details_template_override_Valid() const{
    return m_details_template_override_isValid;
}

OAIListTemplateOverride OAIClassTemplateInfo::getListTemplateOverride() const {
    return m_list_template_override;
}
void OAIClassTemplateInfo::setListTemplateOverride(const OAIListTemplateOverride &list_template_override) {
    m_list_template_override = list_template_override;
    m_list_template_override_isSet = true;
}

bool OAIClassTemplateInfo::is_list_template_override_Set() const{
    return m_list_template_override_isSet;
}

bool OAIClassTemplateInfo::is_list_template_override_Valid() const{
    return m_list_template_override_isValid;
}

bool OAIClassTemplateInfo::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_card_barcode_section_details.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_card_template_override.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_details_template_override.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_list_template_override.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIClassTemplateInfo::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
