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

#include "OAICustomer_data_address_interface.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAICustomer_data_address_interface::OAICustomer_data_address_interface(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAICustomer_data_address_interface::OAICustomer_data_address_interface() {
    this->initializeModel();
}

OAICustomer_data_address_interface::~OAICustomer_data_address_interface() {}

void OAICustomer_data_address_interface::initializeModel() {

    m_city_isSet = false;
    m_city_isValid = false;

    m_company_isSet = false;
    m_company_isValid = false;

    m_country_id_isSet = false;
    m_country_id_isValid = false;

    m_custom_attributes_isSet = false;
    m_custom_attributes_isValid = false;

    m_customer_id_isSet = false;
    m_customer_id_isValid = false;

    m_default_billing_isSet = false;
    m_default_billing_isValid = false;

    m_default_shipping_isSet = false;
    m_default_shipping_isValid = false;

    m_extension_attributes_isSet = false;
    m_extension_attributes_isValid = false;

    m_fax_isSet = false;
    m_fax_isValid = false;

    m_firstname_isSet = false;
    m_firstname_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_lastname_isSet = false;
    m_lastname_isValid = false;

    m_middlename_isSet = false;
    m_middlename_isValid = false;

    m_postcode_isSet = false;
    m_postcode_isValid = false;

    m_prefix_isSet = false;
    m_prefix_isValid = false;

    m_region_isSet = false;
    m_region_isValid = false;

    m_region_id_isSet = false;
    m_region_id_isValid = false;

    m_street_isSet = false;
    m_street_isValid = false;

    m_suffix_isSet = false;
    m_suffix_isValid = false;

    m_telephone_isSet = false;
    m_telephone_isValid = false;

    m_vat_id_isSet = false;
    m_vat_id_isValid = false;
}

void OAICustomer_data_address_interface::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAICustomer_data_address_interface::fromJsonObject(QJsonObject json) {

    m_city_isValid = ::OpenAPI::fromJsonValue(m_city, json[QString("city")]);
    m_city_isSet = !json[QString("city")].isNull() && m_city_isValid;

    m_company_isValid = ::OpenAPI::fromJsonValue(m_company, json[QString("company")]);
    m_company_isSet = !json[QString("company")].isNull() && m_company_isValid;

    m_country_id_isValid = ::OpenAPI::fromJsonValue(m_country_id, json[QString("country_id")]);
    m_country_id_isSet = !json[QString("country_id")].isNull() && m_country_id_isValid;

    m_custom_attributes_isValid = ::OpenAPI::fromJsonValue(m_custom_attributes, json[QString("custom_attributes")]);
    m_custom_attributes_isSet = !json[QString("custom_attributes")].isNull() && m_custom_attributes_isValid;

    m_customer_id_isValid = ::OpenAPI::fromJsonValue(m_customer_id, json[QString("customer_id")]);
    m_customer_id_isSet = !json[QString("customer_id")].isNull() && m_customer_id_isValid;

    m_default_billing_isValid = ::OpenAPI::fromJsonValue(m_default_billing, json[QString("default_billing")]);
    m_default_billing_isSet = !json[QString("default_billing")].isNull() && m_default_billing_isValid;

    m_default_shipping_isValid = ::OpenAPI::fromJsonValue(m_default_shipping, json[QString("default_shipping")]);
    m_default_shipping_isSet = !json[QString("default_shipping")].isNull() && m_default_shipping_isValid;

    m_extension_attributes_isValid = ::OpenAPI::fromJsonValue(m_extension_attributes, json[QString("extension_attributes")]);
    m_extension_attributes_isSet = !json[QString("extension_attributes")].isNull() && m_extension_attributes_isValid;

    m_fax_isValid = ::OpenAPI::fromJsonValue(m_fax, json[QString("fax")]);
    m_fax_isSet = !json[QString("fax")].isNull() && m_fax_isValid;

    m_firstname_isValid = ::OpenAPI::fromJsonValue(m_firstname, json[QString("firstname")]);
    m_firstname_isSet = !json[QString("firstname")].isNull() && m_firstname_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_lastname_isValid = ::OpenAPI::fromJsonValue(m_lastname, json[QString("lastname")]);
    m_lastname_isSet = !json[QString("lastname")].isNull() && m_lastname_isValid;

    m_middlename_isValid = ::OpenAPI::fromJsonValue(m_middlename, json[QString("middlename")]);
    m_middlename_isSet = !json[QString("middlename")].isNull() && m_middlename_isValid;

    m_postcode_isValid = ::OpenAPI::fromJsonValue(m_postcode, json[QString("postcode")]);
    m_postcode_isSet = !json[QString("postcode")].isNull() && m_postcode_isValid;

    m_prefix_isValid = ::OpenAPI::fromJsonValue(m_prefix, json[QString("prefix")]);
    m_prefix_isSet = !json[QString("prefix")].isNull() && m_prefix_isValid;

    m_region_isValid = ::OpenAPI::fromJsonValue(m_region, json[QString("region")]);
    m_region_isSet = !json[QString("region")].isNull() && m_region_isValid;

    m_region_id_isValid = ::OpenAPI::fromJsonValue(m_region_id, json[QString("region_id")]);
    m_region_id_isSet = !json[QString("region_id")].isNull() && m_region_id_isValid;

    m_street_isValid = ::OpenAPI::fromJsonValue(m_street, json[QString("street")]);
    m_street_isSet = !json[QString("street")].isNull() && m_street_isValid;

    m_suffix_isValid = ::OpenAPI::fromJsonValue(m_suffix, json[QString("suffix")]);
    m_suffix_isSet = !json[QString("suffix")].isNull() && m_suffix_isValid;

    m_telephone_isValid = ::OpenAPI::fromJsonValue(m_telephone, json[QString("telephone")]);
    m_telephone_isSet = !json[QString("telephone")].isNull() && m_telephone_isValid;

    m_vat_id_isValid = ::OpenAPI::fromJsonValue(m_vat_id, json[QString("vat_id")]);
    m_vat_id_isSet = !json[QString("vat_id")].isNull() && m_vat_id_isValid;
}

QString OAICustomer_data_address_interface::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAICustomer_data_address_interface::asJsonObject() const {
    QJsonObject obj;
    if (m_city_isSet) {
        obj.insert(QString("city"), ::OpenAPI::toJsonValue(m_city));
    }
    if (m_company_isSet) {
        obj.insert(QString("company"), ::OpenAPI::toJsonValue(m_company));
    }
    if (m_country_id_isSet) {
        obj.insert(QString("country_id"), ::OpenAPI::toJsonValue(m_country_id));
    }
    if (m_custom_attributes.size() > 0) {
        obj.insert(QString("custom_attributes"), ::OpenAPI::toJsonValue(m_custom_attributes));
    }
    if (m_customer_id_isSet) {
        obj.insert(QString("customer_id"), ::OpenAPI::toJsonValue(m_customer_id));
    }
    if (m_default_billing_isSet) {
        obj.insert(QString("default_billing"), ::OpenAPI::toJsonValue(m_default_billing));
    }
    if (m_default_shipping_isSet) {
        obj.insert(QString("default_shipping"), ::OpenAPI::toJsonValue(m_default_shipping));
    }
    if (m_extension_attributes_isSet) {
        obj.insert(QString("extension_attributes"), ::OpenAPI::toJsonValue(m_extension_attributes));
    }
    if (m_fax_isSet) {
        obj.insert(QString("fax"), ::OpenAPI::toJsonValue(m_fax));
    }
    if (m_firstname_isSet) {
        obj.insert(QString("firstname"), ::OpenAPI::toJsonValue(m_firstname));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_lastname_isSet) {
        obj.insert(QString("lastname"), ::OpenAPI::toJsonValue(m_lastname));
    }
    if (m_middlename_isSet) {
        obj.insert(QString("middlename"), ::OpenAPI::toJsonValue(m_middlename));
    }
    if (m_postcode_isSet) {
        obj.insert(QString("postcode"), ::OpenAPI::toJsonValue(m_postcode));
    }
    if (m_prefix_isSet) {
        obj.insert(QString("prefix"), ::OpenAPI::toJsonValue(m_prefix));
    }
    if (m_region.isSet()) {
        obj.insert(QString("region"), ::OpenAPI::toJsonValue(m_region));
    }
    if (m_region_id_isSet) {
        obj.insert(QString("region_id"), ::OpenAPI::toJsonValue(m_region_id));
    }
    if (m_street.size() > 0) {
        obj.insert(QString("street"), ::OpenAPI::toJsonValue(m_street));
    }
    if (m_suffix_isSet) {
        obj.insert(QString("suffix"), ::OpenAPI::toJsonValue(m_suffix));
    }
    if (m_telephone_isSet) {
        obj.insert(QString("telephone"), ::OpenAPI::toJsonValue(m_telephone));
    }
    if (m_vat_id_isSet) {
        obj.insert(QString("vat_id"), ::OpenAPI::toJsonValue(m_vat_id));
    }
    return obj;
}

QString OAICustomer_data_address_interface::getCity() const {
    return m_city;
}
void OAICustomer_data_address_interface::setCity(const QString &city) {
    m_city = city;
    m_city_isSet = true;
}

bool OAICustomer_data_address_interface::is_city_Set() const{
    return m_city_isSet;
}

bool OAICustomer_data_address_interface::is_city_Valid() const{
    return m_city_isValid;
}

QString OAICustomer_data_address_interface::getCompany() const {
    return m_company;
}
void OAICustomer_data_address_interface::setCompany(const QString &company) {
    m_company = company;
    m_company_isSet = true;
}

bool OAICustomer_data_address_interface::is_company_Set() const{
    return m_company_isSet;
}

bool OAICustomer_data_address_interface::is_company_Valid() const{
    return m_company_isValid;
}

QString OAICustomer_data_address_interface::getCountryId() const {
    return m_country_id;
}
void OAICustomer_data_address_interface::setCountryId(const QString &country_id) {
    m_country_id = country_id;
    m_country_id_isSet = true;
}

bool OAICustomer_data_address_interface::is_country_id_Set() const{
    return m_country_id_isSet;
}

bool OAICustomer_data_address_interface::is_country_id_Valid() const{
    return m_country_id_isValid;
}

QList<OAIFramework_attribute_interface> OAICustomer_data_address_interface::getCustomAttributes() const {
    return m_custom_attributes;
}
void OAICustomer_data_address_interface::setCustomAttributes(const QList<OAIFramework_attribute_interface> &custom_attributes) {
    m_custom_attributes = custom_attributes;
    m_custom_attributes_isSet = true;
}

bool OAICustomer_data_address_interface::is_custom_attributes_Set() const{
    return m_custom_attributes_isSet;
}

bool OAICustomer_data_address_interface::is_custom_attributes_Valid() const{
    return m_custom_attributes_isValid;
}

qint32 OAICustomer_data_address_interface::getCustomerId() const {
    return m_customer_id;
}
void OAICustomer_data_address_interface::setCustomerId(const qint32 &customer_id) {
    m_customer_id = customer_id;
    m_customer_id_isSet = true;
}

bool OAICustomer_data_address_interface::is_customer_id_Set() const{
    return m_customer_id_isSet;
}

bool OAICustomer_data_address_interface::is_customer_id_Valid() const{
    return m_customer_id_isValid;
}

bool OAICustomer_data_address_interface::isDefaultBilling() const {
    return m_default_billing;
}
void OAICustomer_data_address_interface::setDefaultBilling(const bool &default_billing) {
    m_default_billing = default_billing;
    m_default_billing_isSet = true;
}

bool OAICustomer_data_address_interface::is_default_billing_Set() const{
    return m_default_billing_isSet;
}

bool OAICustomer_data_address_interface::is_default_billing_Valid() const{
    return m_default_billing_isValid;
}

bool OAICustomer_data_address_interface::isDefaultShipping() const {
    return m_default_shipping;
}
void OAICustomer_data_address_interface::setDefaultShipping(const bool &default_shipping) {
    m_default_shipping = default_shipping;
    m_default_shipping_isSet = true;
}

bool OAICustomer_data_address_interface::is_default_shipping_Set() const{
    return m_default_shipping_isSet;
}

bool OAICustomer_data_address_interface::is_default_shipping_Valid() const{
    return m_default_shipping_isValid;
}

OAIObject OAICustomer_data_address_interface::getExtensionAttributes() const {
    return m_extension_attributes;
}
void OAICustomer_data_address_interface::setExtensionAttributes(const OAIObject &extension_attributes) {
    m_extension_attributes = extension_attributes;
    m_extension_attributes_isSet = true;
}

bool OAICustomer_data_address_interface::is_extension_attributes_Set() const{
    return m_extension_attributes_isSet;
}

bool OAICustomer_data_address_interface::is_extension_attributes_Valid() const{
    return m_extension_attributes_isValid;
}

QString OAICustomer_data_address_interface::getFax() const {
    return m_fax;
}
void OAICustomer_data_address_interface::setFax(const QString &fax) {
    m_fax = fax;
    m_fax_isSet = true;
}

bool OAICustomer_data_address_interface::is_fax_Set() const{
    return m_fax_isSet;
}

bool OAICustomer_data_address_interface::is_fax_Valid() const{
    return m_fax_isValid;
}

QString OAICustomer_data_address_interface::getFirstname() const {
    return m_firstname;
}
void OAICustomer_data_address_interface::setFirstname(const QString &firstname) {
    m_firstname = firstname;
    m_firstname_isSet = true;
}

bool OAICustomer_data_address_interface::is_firstname_Set() const{
    return m_firstname_isSet;
}

bool OAICustomer_data_address_interface::is_firstname_Valid() const{
    return m_firstname_isValid;
}

qint32 OAICustomer_data_address_interface::getId() const {
    return m_id;
}
void OAICustomer_data_address_interface::setId(const qint32 &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAICustomer_data_address_interface::is_id_Set() const{
    return m_id_isSet;
}

bool OAICustomer_data_address_interface::is_id_Valid() const{
    return m_id_isValid;
}

QString OAICustomer_data_address_interface::getLastname() const {
    return m_lastname;
}
void OAICustomer_data_address_interface::setLastname(const QString &lastname) {
    m_lastname = lastname;
    m_lastname_isSet = true;
}

bool OAICustomer_data_address_interface::is_lastname_Set() const{
    return m_lastname_isSet;
}

bool OAICustomer_data_address_interface::is_lastname_Valid() const{
    return m_lastname_isValid;
}

QString OAICustomer_data_address_interface::getMiddlename() const {
    return m_middlename;
}
void OAICustomer_data_address_interface::setMiddlename(const QString &middlename) {
    m_middlename = middlename;
    m_middlename_isSet = true;
}

bool OAICustomer_data_address_interface::is_middlename_Set() const{
    return m_middlename_isSet;
}

bool OAICustomer_data_address_interface::is_middlename_Valid() const{
    return m_middlename_isValid;
}

QString OAICustomer_data_address_interface::getPostcode() const {
    return m_postcode;
}
void OAICustomer_data_address_interface::setPostcode(const QString &postcode) {
    m_postcode = postcode;
    m_postcode_isSet = true;
}

bool OAICustomer_data_address_interface::is_postcode_Set() const{
    return m_postcode_isSet;
}

bool OAICustomer_data_address_interface::is_postcode_Valid() const{
    return m_postcode_isValid;
}

QString OAICustomer_data_address_interface::getPrefix() const {
    return m_prefix;
}
void OAICustomer_data_address_interface::setPrefix(const QString &prefix) {
    m_prefix = prefix;
    m_prefix_isSet = true;
}

bool OAICustomer_data_address_interface::is_prefix_Set() const{
    return m_prefix_isSet;
}

bool OAICustomer_data_address_interface::is_prefix_Valid() const{
    return m_prefix_isValid;
}

OAICustomer_data_region_interface OAICustomer_data_address_interface::getRegion() const {
    return m_region;
}
void OAICustomer_data_address_interface::setRegion(const OAICustomer_data_region_interface &region) {
    m_region = region;
    m_region_isSet = true;
}

bool OAICustomer_data_address_interface::is_region_Set() const{
    return m_region_isSet;
}

bool OAICustomer_data_address_interface::is_region_Valid() const{
    return m_region_isValid;
}

qint32 OAICustomer_data_address_interface::getRegionId() const {
    return m_region_id;
}
void OAICustomer_data_address_interface::setRegionId(const qint32 &region_id) {
    m_region_id = region_id;
    m_region_id_isSet = true;
}

bool OAICustomer_data_address_interface::is_region_id_Set() const{
    return m_region_id_isSet;
}

bool OAICustomer_data_address_interface::is_region_id_Valid() const{
    return m_region_id_isValid;
}

QList<QString> OAICustomer_data_address_interface::getStreet() const {
    return m_street;
}
void OAICustomer_data_address_interface::setStreet(const QList<QString> &street) {
    m_street = street;
    m_street_isSet = true;
}

bool OAICustomer_data_address_interface::is_street_Set() const{
    return m_street_isSet;
}

bool OAICustomer_data_address_interface::is_street_Valid() const{
    return m_street_isValid;
}

QString OAICustomer_data_address_interface::getSuffix() const {
    return m_suffix;
}
void OAICustomer_data_address_interface::setSuffix(const QString &suffix) {
    m_suffix = suffix;
    m_suffix_isSet = true;
}

bool OAICustomer_data_address_interface::is_suffix_Set() const{
    return m_suffix_isSet;
}

bool OAICustomer_data_address_interface::is_suffix_Valid() const{
    return m_suffix_isValid;
}

QString OAICustomer_data_address_interface::getTelephone() const {
    return m_telephone;
}
void OAICustomer_data_address_interface::setTelephone(const QString &telephone) {
    m_telephone = telephone;
    m_telephone_isSet = true;
}

bool OAICustomer_data_address_interface::is_telephone_Set() const{
    return m_telephone_isSet;
}

bool OAICustomer_data_address_interface::is_telephone_Valid() const{
    return m_telephone_isValid;
}

QString OAICustomer_data_address_interface::getVatId() const {
    return m_vat_id;
}
void OAICustomer_data_address_interface::setVatId(const QString &vat_id) {
    m_vat_id = vat_id;
    m_vat_id_isSet = true;
}

bool OAICustomer_data_address_interface::is_vat_id_Set() const{
    return m_vat_id_isSet;
}

bool OAICustomer_data_address_interface::is_vat_id_Valid() const{
    return m_vat_id_isValid;
}

bool OAICustomer_data_address_interface::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_city_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_company_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_country_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_custom_attributes.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_customer_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_default_billing_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_default_shipping_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_extension_attributes_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_fax_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_firstname_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_lastname_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_middlename_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_postcode_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_prefix_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_region.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_region_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_street.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_suffix_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_telephone_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_vat_id_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAICustomer_data_address_interface::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
