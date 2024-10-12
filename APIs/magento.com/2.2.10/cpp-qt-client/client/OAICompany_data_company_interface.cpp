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

#include "OAICompany_data_company_interface.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAICompany_data_company_interface::OAICompany_data_company_interface(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAICompany_data_company_interface::OAICompany_data_company_interface() {
    this->initializeModel();
}

OAICompany_data_company_interface::~OAICompany_data_company_interface() {}

void OAICompany_data_company_interface::initializeModel() {

    m_city_isSet = false;
    m_city_isValid = false;

    m_comment_isSet = false;
    m_comment_isValid = false;

    m_company_email_isSet = false;
    m_company_email_isValid = false;

    m_company_name_isSet = false;
    m_company_name_isValid = false;

    m_country_id_isSet = false;
    m_country_id_isValid = false;

    m_customer_group_id_isSet = false;
    m_customer_group_id_isValid = false;

    m_extension_attributes_isSet = false;
    m_extension_attributes_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_legal_name_isSet = false;
    m_legal_name_isValid = false;

    m_postcode_isSet = false;
    m_postcode_isValid = false;

    m_region_isSet = false;
    m_region_isValid = false;

    m_region_id_isSet = false;
    m_region_id_isValid = false;

    m_reject_reason_isSet = false;
    m_reject_reason_isValid = false;

    m_rejected_at_isSet = false;
    m_rejected_at_isValid = false;

    m_reseller_id_isSet = false;
    m_reseller_id_isValid = false;

    m_sales_representative_id_isSet = false;
    m_sales_representative_id_isValid = false;

    m_status_isSet = false;
    m_status_isValid = false;

    m_street_isSet = false;
    m_street_isValid = false;

    m_super_user_id_isSet = false;
    m_super_user_id_isValid = false;

    m_telephone_isSet = false;
    m_telephone_isValid = false;

    m_vat_tax_id_isSet = false;
    m_vat_tax_id_isValid = false;
}

void OAICompany_data_company_interface::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAICompany_data_company_interface::fromJsonObject(QJsonObject json) {

    m_city_isValid = ::OpenAPI::fromJsonValue(m_city, json[QString("city")]);
    m_city_isSet = !json[QString("city")].isNull() && m_city_isValid;

    m_comment_isValid = ::OpenAPI::fromJsonValue(m_comment, json[QString("comment")]);
    m_comment_isSet = !json[QString("comment")].isNull() && m_comment_isValid;

    m_company_email_isValid = ::OpenAPI::fromJsonValue(m_company_email, json[QString("company_email")]);
    m_company_email_isSet = !json[QString("company_email")].isNull() && m_company_email_isValid;

    m_company_name_isValid = ::OpenAPI::fromJsonValue(m_company_name, json[QString("company_name")]);
    m_company_name_isSet = !json[QString("company_name")].isNull() && m_company_name_isValid;

    m_country_id_isValid = ::OpenAPI::fromJsonValue(m_country_id, json[QString("country_id")]);
    m_country_id_isSet = !json[QString("country_id")].isNull() && m_country_id_isValid;

    m_customer_group_id_isValid = ::OpenAPI::fromJsonValue(m_customer_group_id, json[QString("customer_group_id")]);
    m_customer_group_id_isSet = !json[QString("customer_group_id")].isNull() && m_customer_group_id_isValid;

    m_extension_attributes_isValid = ::OpenAPI::fromJsonValue(m_extension_attributes, json[QString("extension_attributes")]);
    m_extension_attributes_isSet = !json[QString("extension_attributes")].isNull() && m_extension_attributes_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_legal_name_isValid = ::OpenAPI::fromJsonValue(m_legal_name, json[QString("legal_name")]);
    m_legal_name_isSet = !json[QString("legal_name")].isNull() && m_legal_name_isValid;

    m_postcode_isValid = ::OpenAPI::fromJsonValue(m_postcode, json[QString("postcode")]);
    m_postcode_isSet = !json[QString("postcode")].isNull() && m_postcode_isValid;

    m_region_isValid = ::OpenAPI::fromJsonValue(m_region, json[QString("region")]);
    m_region_isSet = !json[QString("region")].isNull() && m_region_isValid;

    m_region_id_isValid = ::OpenAPI::fromJsonValue(m_region_id, json[QString("region_id")]);
    m_region_id_isSet = !json[QString("region_id")].isNull() && m_region_id_isValid;

    m_reject_reason_isValid = ::OpenAPI::fromJsonValue(m_reject_reason, json[QString("reject_reason")]);
    m_reject_reason_isSet = !json[QString("reject_reason")].isNull() && m_reject_reason_isValid;

    m_rejected_at_isValid = ::OpenAPI::fromJsonValue(m_rejected_at, json[QString("rejected_at")]);
    m_rejected_at_isSet = !json[QString("rejected_at")].isNull() && m_rejected_at_isValid;

    m_reseller_id_isValid = ::OpenAPI::fromJsonValue(m_reseller_id, json[QString("reseller_id")]);
    m_reseller_id_isSet = !json[QString("reseller_id")].isNull() && m_reseller_id_isValid;

    m_sales_representative_id_isValid = ::OpenAPI::fromJsonValue(m_sales_representative_id, json[QString("sales_representative_id")]);
    m_sales_representative_id_isSet = !json[QString("sales_representative_id")].isNull() && m_sales_representative_id_isValid;

    m_status_isValid = ::OpenAPI::fromJsonValue(m_status, json[QString("status")]);
    m_status_isSet = !json[QString("status")].isNull() && m_status_isValid;

    m_street_isValid = ::OpenAPI::fromJsonValue(m_street, json[QString("street")]);
    m_street_isSet = !json[QString("street")].isNull() && m_street_isValid;

    m_super_user_id_isValid = ::OpenAPI::fromJsonValue(m_super_user_id, json[QString("super_user_id")]);
    m_super_user_id_isSet = !json[QString("super_user_id")].isNull() && m_super_user_id_isValid;

    m_telephone_isValid = ::OpenAPI::fromJsonValue(m_telephone, json[QString("telephone")]);
    m_telephone_isSet = !json[QString("telephone")].isNull() && m_telephone_isValid;

    m_vat_tax_id_isValid = ::OpenAPI::fromJsonValue(m_vat_tax_id, json[QString("vat_tax_id")]);
    m_vat_tax_id_isSet = !json[QString("vat_tax_id")].isNull() && m_vat_tax_id_isValid;
}

QString OAICompany_data_company_interface::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAICompany_data_company_interface::asJsonObject() const {
    QJsonObject obj;
    if (m_city_isSet) {
        obj.insert(QString("city"), ::OpenAPI::toJsonValue(m_city));
    }
    if (m_comment_isSet) {
        obj.insert(QString("comment"), ::OpenAPI::toJsonValue(m_comment));
    }
    if (m_company_email_isSet) {
        obj.insert(QString("company_email"), ::OpenAPI::toJsonValue(m_company_email));
    }
    if (m_company_name_isSet) {
        obj.insert(QString("company_name"), ::OpenAPI::toJsonValue(m_company_name));
    }
    if (m_country_id_isSet) {
        obj.insert(QString("country_id"), ::OpenAPI::toJsonValue(m_country_id));
    }
    if (m_customer_group_id_isSet) {
        obj.insert(QString("customer_group_id"), ::OpenAPI::toJsonValue(m_customer_group_id));
    }
    if (m_extension_attributes.isSet()) {
        obj.insert(QString("extension_attributes"), ::OpenAPI::toJsonValue(m_extension_attributes));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_legal_name_isSet) {
        obj.insert(QString("legal_name"), ::OpenAPI::toJsonValue(m_legal_name));
    }
    if (m_postcode_isSet) {
        obj.insert(QString("postcode"), ::OpenAPI::toJsonValue(m_postcode));
    }
    if (m_region_isSet) {
        obj.insert(QString("region"), ::OpenAPI::toJsonValue(m_region));
    }
    if (m_region_id_isSet) {
        obj.insert(QString("region_id"), ::OpenAPI::toJsonValue(m_region_id));
    }
    if (m_reject_reason_isSet) {
        obj.insert(QString("reject_reason"), ::OpenAPI::toJsonValue(m_reject_reason));
    }
    if (m_rejected_at_isSet) {
        obj.insert(QString("rejected_at"), ::OpenAPI::toJsonValue(m_rejected_at));
    }
    if (m_reseller_id_isSet) {
        obj.insert(QString("reseller_id"), ::OpenAPI::toJsonValue(m_reseller_id));
    }
    if (m_sales_representative_id_isSet) {
        obj.insert(QString("sales_representative_id"), ::OpenAPI::toJsonValue(m_sales_representative_id));
    }
    if (m_status_isSet) {
        obj.insert(QString("status"), ::OpenAPI::toJsonValue(m_status));
    }
    if (m_street.size() > 0) {
        obj.insert(QString("street"), ::OpenAPI::toJsonValue(m_street));
    }
    if (m_super_user_id_isSet) {
        obj.insert(QString("super_user_id"), ::OpenAPI::toJsonValue(m_super_user_id));
    }
    if (m_telephone_isSet) {
        obj.insert(QString("telephone"), ::OpenAPI::toJsonValue(m_telephone));
    }
    if (m_vat_tax_id_isSet) {
        obj.insert(QString("vat_tax_id"), ::OpenAPI::toJsonValue(m_vat_tax_id));
    }
    return obj;
}

QString OAICompany_data_company_interface::getCity() const {
    return m_city;
}
void OAICompany_data_company_interface::setCity(const QString &city) {
    m_city = city;
    m_city_isSet = true;
}

bool OAICompany_data_company_interface::is_city_Set() const{
    return m_city_isSet;
}

bool OAICompany_data_company_interface::is_city_Valid() const{
    return m_city_isValid;
}

QString OAICompany_data_company_interface::getComment() const {
    return m_comment;
}
void OAICompany_data_company_interface::setComment(const QString &comment) {
    m_comment = comment;
    m_comment_isSet = true;
}

bool OAICompany_data_company_interface::is_comment_Set() const{
    return m_comment_isSet;
}

bool OAICompany_data_company_interface::is_comment_Valid() const{
    return m_comment_isValid;
}

QString OAICompany_data_company_interface::getCompanyEmail() const {
    return m_company_email;
}
void OAICompany_data_company_interface::setCompanyEmail(const QString &company_email) {
    m_company_email = company_email;
    m_company_email_isSet = true;
}

bool OAICompany_data_company_interface::is_company_email_Set() const{
    return m_company_email_isSet;
}

bool OAICompany_data_company_interface::is_company_email_Valid() const{
    return m_company_email_isValid;
}

QString OAICompany_data_company_interface::getCompanyName() const {
    return m_company_name;
}
void OAICompany_data_company_interface::setCompanyName(const QString &company_name) {
    m_company_name = company_name;
    m_company_name_isSet = true;
}

bool OAICompany_data_company_interface::is_company_name_Set() const{
    return m_company_name_isSet;
}

bool OAICompany_data_company_interface::is_company_name_Valid() const{
    return m_company_name_isValid;
}

QString OAICompany_data_company_interface::getCountryId() const {
    return m_country_id;
}
void OAICompany_data_company_interface::setCountryId(const QString &country_id) {
    m_country_id = country_id;
    m_country_id_isSet = true;
}

bool OAICompany_data_company_interface::is_country_id_Set() const{
    return m_country_id_isSet;
}

bool OAICompany_data_company_interface::is_country_id_Valid() const{
    return m_country_id_isValid;
}

qint32 OAICompany_data_company_interface::getCustomerGroupId() const {
    return m_customer_group_id;
}
void OAICompany_data_company_interface::setCustomerGroupId(const qint32 &customer_group_id) {
    m_customer_group_id = customer_group_id;
    m_customer_group_id_isSet = true;
}

bool OAICompany_data_company_interface::is_customer_group_id_Set() const{
    return m_customer_group_id_isSet;
}

bool OAICompany_data_company_interface::is_customer_group_id_Valid() const{
    return m_customer_group_id_isValid;
}

OAICompany_data_company_extension_interface OAICompany_data_company_interface::getExtensionAttributes() const {
    return m_extension_attributes;
}
void OAICompany_data_company_interface::setExtensionAttributes(const OAICompany_data_company_extension_interface &extension_attributes) {
    m_extension_attributes = extension_attributes;
    m_extension_attributes_isSet = true;
}

bool OAICompany_data_company_interface::is_extension_attributes_Set() const{
    return m_extension_attributes_isSet;
}

bool OAICompany_data_company_interface::is_extension_attributes_Valid() const{
    return m_extension_attributes_isValid;
}

qint32 OAICompany_data_company_interface::getId() const {
    return m_id;
}
void OAICompany_data_company_interface::setId(const qint32 &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAICompany_data_company_interface::is_id_Set() const{
    return m_id_isSet;
}

bool OAICompany_data_company_interface::is_id_Valid() const{
    return m_id_isValid;
}

QString OAICompany_data_company_interface::getLegalName() const {
    return m_legal_name;
}
void OAICompany_data_company_interface::setLegalName(const QString &legal_name) {
    m_legal_name = legal_name;
    m_legal_name_isSet = true;
}

bool OAICompany_data_company_interface::is_legal_name_Set() const{
    return m_legal_name_isSet;
}

bool OAICompany_data_company_interface::is_legal_name_Valid() const{
    return m_legal_name_isValid;
}

QString OAICompany_data_company_interface::getPostcode() const {
    return m_postcode;
}
void OAICompany_data_company_interface::setPostcode(const QString &postcode) {
    m_postcode = postcode;
    m_postcode_isSet = true;
}

bool OAICompany_data_company_interface::is_postcode_Set() const{
    return m_postcode_isSet;
}

bool OAICompany_data_company_interface::is_postcode_Valid() const{
    return m_postcode_isValid;
}

QString OAICompany_data_company_interface::getRegion() const {
    return m_region;
}
void OAICompany_data_company_interface::setRegion(const QString &region) {
    m_region = region;
    m_region_isSet = true;
}

bool OAICompany_data_company_interface::is_region_Set() const{
    return m_region_isSet;
}

bool OAICompany_data_company_interface::is_region_Valid() const{
    return m_region_isValid;
}

QString OAICompany_data_company_interface::getRegionId() const {
    return m_region_id;
}
void OAICompany_data_company_interface::setRegionId(const QString &region_id) {
    m_region_id = region_id;
    m_region_id_isSet = true;
}

bool OAICompany_data_company_interface::is_region_id_Set() const{
    return m_region_id_isSet;
}

bool OAICompany_data_company_interface::is_region_id_Valid() const{
    return m_region_id_isValid;
}

QString OAICompany_data_company_interface::getRejectReason() const {
    return m_reject_reason;
}
void OAICompany_data_company_interface::setRejectReason(const QString &reject_reason) {
    m_reject_reason = reject_reason;
    m_reject_reason_isSet = true;
}

bool OAICompany_data_company_interface::is_reject_reason_Set() const{
    return m_reject_reason_isSet;
}

bool OAICompany_data_company_interface::is_reject_reason_Valid() const{
    return m_reject_reason_isValid;
}

QString OAICompany_data_company_interface::getRejectedAt() const {
    return m_rejected_at;
}
void OAICompany_data_company_interface::setRejectedAt(const QString &rejected_at) {
    m_rejected_at = rejected_at;
    m_rejected_at_isSet = true;
}

bool OAICompany_data_company_interface::is_rejected_at_Set() const{
    return m_rejected_at_isSet;
}

bool OAICompany_data_company_interface::is_rejected_at_Valid() const{
    return m_rejected_at_isValid;
}

QString OAICompany_data_company_interface::getResellerId() const {
    return m_reseller_id;
}
void OAICompany_data_company_interface::setResellerId(const QString &reseller_id) {
    m_reseller_id = reseller_id;
    m_reseller_id_isSet = true;
}

bool OAICompany_data_company_interface::is_reseller_id_Set() const{
    return m_reseller_id_isSet;
}

bool OAICompany_data_company_interface::is_reseller_id_Valid() const{
    return m_reseller_id_isValid;
}

qint32 OAICompany_data_company_interface::getSalesRepresentativeId() const {
    return m_sales_representative_id;
}
void OAICompany_data_company_interface::setSalesRepresentativeId(const qint32 &sales_representative_id) {
    m_sales_representative_id = sales_representative_id;
    m_sales_representative_id_isSet = true;
}

bool OAICompany_data_company_interface::is_sales_representative_id_Set() const{
    return m_sales_representative_id_isSet;
}

bool OAICompany_data_company_interface::is_sales_representative_id_Valid() const{
    return m_sales_representative_id_isValid;
}

qint32 OAICompany_data_company_interface::getStatus() const {
    return m_status;
}
void OAICompany_data_company_interface::setStatus(const qint32 &status) {
    m_status = status;
    m_status_isSet = true;
}

bool OAICompany_data_company_interface::is_status_Set() const{
    return m_status_isSet;
}

bool OAICompany_data_company_interface::is_status_Valid() const{
    return m_status_isValid;
}

QList<QString> OAICompany_data_company_interface::getStreet() const {
    return m_street;
}
void OAICompany_data_company_interface::setStreet(const QList<QString> &street) {
    m_street = street;
    m_street_isSet = true;
}

bool OAICompany_data_company_interface::is_street_Set() const{
    return m_street_isSet;
}

bool OAICompany_data_company_interface::is_street_Valid() const{
    return m_street_isValid;
}

qint32 OAICompany_data_company_interface::getSuperUserId() const {
    return m_super_user_id;
}
void OAICompany_data_company_interface::setSuperUserId(const qint32 &super_user_id) {
    m_super_user_id = super_user_id;
    m_super_user_id_isSet = true;
}

bool OAICompany_data_company_interface::is_super_user_id_Set() const{
    return m_super_user_id_isSet;
}

bool OAICompany_data_company_interface::is_super_user_id_Valid() const{
    return m_super_user_id_isValid;
}

QString OAICompany_data_company_interface::getTelephone() const {
    return m_telephone;
}
void OAICompany_data_company_interface::setTelephone(const QString &telephone) {
    m_telephone = telephone;
    m_telephone_isSet = true;
}

bool OAICompany_data_company_interface::is_telephone_Set() const{
    return m_telephone_isSet;
}

bool OAICompany_data_company_interface::is_telephone_Valid() const{
    return m_telephone_isValid;
}

QString OAICompany_data_company_interface::getVatTaxId() const {
    return m_vat_tax_id;
}
void OAICompany_data_company_interface::setVatTaxId(const QString &vat_tax_id) {
    m_vat_tax_id = vat_tax_id;
    m_vat_tax_id_isSet = true;
}

bool OAICompany_data_company_interface::is_vat_tax_id_Set() const{
    return m_vat_tax_id_isSet;
}

bool OAICompany_data_company_interface::is_vat_tax_id_Valid() const{
    return m_vat_tax_id_isValid;
}

bool OAICompany_data_company_interface::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_city_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_comment_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_company_email_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_company_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_country_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_customer_group_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_extension_attributes.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_legal_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_postcode_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_region_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_region_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_reject_reason_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_rejected_at_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_reseller_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_sales_representative_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_status_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_street.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_super_user_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_telephone_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_vat_tax_id_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAICompany_data_company_interface::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_customer_group_id_isValid && m_reject_reason_isValid && m_rejected_at_isValid && m_sales_representative_id_isValid && m_street_isValid && m_super_user_id_isValid && true;
}

} // namespace OpenAPI
