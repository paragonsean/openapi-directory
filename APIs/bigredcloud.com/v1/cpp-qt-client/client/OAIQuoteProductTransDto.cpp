/**
 * Big Red Cloud API
 *   <div style='line-height: 30px;'>      <strong>Welcome to the Big Red Cloud API</strong><br/>      This API enables programmatic access to Big Red Cloud data.<br/>      We have used Swagger to auto generate the API documentation on this page, and it also enables direct interaction with the API in this page. <br/>      To get started, you will require an API Key - check out our guide at <a target='_blank' href='https://www.bigredcloud.com/support/generating-api-key-guide/'>https://www.bigredcloud.com/support/generating-api-key-guide/</a> for information on how to get one. <br/>      Use the  'Enter API Key' button below to enter your API key and start interacting with your Big Red Cloud data right on this page. <br/>      The API key will be stored in your browsers local storage for convenience, but you will be able to delete it at any time if you wish. <br/>      For additional information on the API, check out our support article at <a target='_blank' href='https://www.bigredcloud.com/support/api/'>https://www.bigredcloud.com/support/api/</a><br/>  </div>
 *
 * The version of the OpenAPI document: v1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIQuoteProductTransDto.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIQuoteProductTransDto::OAIQuoteProductTransDto(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIQuoteProductTransDto::OAIQuoteProductTransDto() {
    this->initializeModel();
}

OAIQuoteProductTransDto::~OAIQuoteProductTransDto() {}

void OAIQuoteProductTransDto::initializeModel() {

    m_ac_entries_isSet = false;
    m_ac_entries_isValid = false;

    m_amount_isSet = false;
    m_amount_isValid = false;

    m_company_id_isSet = false;
    m_company_id_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_percentage_isSet = false;
    m_percentage_isValid = false;

    m_product_code_isSet = false;
    m_product_code_isValid = false;

    m_product_id_isSet = false;
    m_product_id_isValid = false;

    m_quantity_isSet = false;
    m_quantity_isValid = false;

    m_tran_notes_isSet = false;
    m_tran_notes_isValid = false;

    m_unit_price_isSet = false;
    m_unit_price_isValid = false;

    m_vat_amount_isSet = false;
    m_vat_amount_isValid = false;

    m_vat_analysis_type_id_isSet = false;
    m_vat_analysis_type_id_isValid = false;

    m_vat_rate_id_isSet = false;
    m_vat_rate_id_isValid = false;
}

void OAIQuoteProductTransDto::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIQuoteProductTransDto::fromJsonObject(QJsonObject json) {

    m_ac_entries_isValid = ::OpenAPI::fromJsonValue(m_ac_entries, json[QString("acEntries")]);
    m_ac_entries_isSet = !json[QString("acEntries")].isNull() && m_ac_entries_isValid;

    m_amount_isValid = ::OpenAPI::fromJsonValue(m_amount, json[QString("amount")]);
    m_amount_isSet = !json[QString("amount")].isNull() && m_amount_isValid;

    m_company_id_isValid = ::OpenAPI::fromJsonValue(m_company_id, json[QString("companyId")]);
    m_company_id_isSet = !json[QString("companyId")].isNull() && m_company_id_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_percentage_isValid = ::OpenAPI::fromJsonValue(m_percentage, json[QString("percentage")]);
    m_percentage_isSet = !json[QString("percentage")].isNull() && m_percentage_isValid;

    m_product_code_isValid = ::OpenAPI::fromJsonValue(m_product_code, json[QString("productCode")]);
    m_product_code_isSet = !json[QString("productCode")].isNull() && m_product_code_isValid;

    m_product_id_isValid = ::OpenAPI::fromJsonValue(m_product_id, json[QString("productId")]);
    m_product_id_isSet = !json[QString("productId")].isNull() && m_product_id_isValid;

    m_quantity_isValid = ::OpenAPI::fromJsonValue(m_quantity, json[QString("quantity")]);
    m_quantity_isSet = !json[QString("quantity")].isNull() && m_quantity_isValid;

    m_tran_notes_isValid = ::OpenAPI::fromJsonValue(m_tran_notes, json[QString("tranNotes")]);
    m_tran_notes_isSet = !json[QString("tranNotes")].isNull() && m_tran_notes_isValid;

    m_unit_price_isValid = ::OpenAPI::fromJsonValue(m_unit_price, json[QString("unitPrice")]);
    m_unit_price_isSet = !json[QString("unitPrice")].isNull() && m_unit_price_isValid;

    m_vat_amount_isValid = ::OpenAPI::fromJsonValue(m_vat_amount, json[QString("vatAmount")]);
    m_vat_amount_isSet = !json[QString("vatAmount")].isNull() && m_vat_amount_isValid;

    m_vat_analysis_type_id_isValid = ::OpenAPI::fromJsonValue(m_vat_analysis_type_id, json[QString("vatAnalysisTypeId")]);
    m_vat_analysis_type_id_isSet = !json[QString("vatAnalysisTypeId")].isNull() && m_vat_analysis_type_id_isValid;

    m_vat_rate_id_isValid = ::OpenAPI::fromJsonValue(m_vat_rate_id, json[QString("vatRateId")]);
    m_vat_rate_id_isSet = !json[QString("vatRateId")].isNull() && m_vat_rate_id_isValid;
}

QString OAIQuoteProductTransDto::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIQuoteProductTransDto::asJsonObject() const {
    QJsonObject obj;
    if (m_ac_entries.size() > 0) {
        obj.insert(QString("acEntries"), ::OpenAPI::toJsonValue(m_ac_entries));
    }
    if (m_amount_isSet) {
        obj.insert(QString("amount"), ::OpenAPI::toJsonValue(m_amount));
    }
    if (m_company_id_isSet) {
        obj.insert(QString("companyId"), ::OpenAPI::toJsonValue(m_company_id));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_percentage_isSet) {
        obj.insert(QString("percentage"), ::OpenAPI::toJsonValue(m_percentage));
    }
    if (m_product_code_isSet) {
        obj.insert(QString("productCode"), ::OpenAPI::toJsonValue(m_product_code));
    }
    if (m_product_id_isSet) {
        obj.insert(QString("productId"), ::OpenAPI::toJsonValue(m_product_id));
    }
    if (m_quantity_isSet) {
        obj.insert(QString("quantity"), ::OpenAPI::toJsonValue(m_quantity));
    }
    if (m_tran_notes.size() > 0) {
        obj.insert(QString("tranNotes"), ::OpenAPI::toJsonValue(m_tran_notes));
    }
    if (m_unit_price_isSet) {
        obj.insert(QString("unitPrice"), ::OpenAPI::toJsonValue(m_unit_price));
    }
    if (m_vat_amount_isSet) {
        obj.insert(QString("vatAmount"), ::OpenAPI::toJsonValue(m_vat_amount));
    }
    if (m_vat_analysis_type_id_isSet) {
        obj.insert(QString("vatAnalysisTypeId"), ::OpenAPI::toJsonValue(m_vat_analysis_type_id));
    }
    if (m_vat_rate_id_isSet) {
        obj.insert(QString("vatRateId"), ::OpenAPI::toJsonValue(m_vat_rate_id));
    }
    return obj;
}

QList<OAIQuoteAcEntriesDto> OAIQuoteProductTransDto::getAcEntries() const {
    return m_ac_entries;
}
void OAIQuoteProductTransDto::setAcEntries(const QList<OAIQuoteAcEntriesDto> &ac_entries) {
    m_ac_entries = ac_entries;
    m_ac_entries_isSet = true;
}

bool OAIQuoteProductTransDto::is_ac_entries_Set() const{
    return m_ac_entries_isSet;
}

bool OAIQuoteProductTransDto::is_ac_entries_Valid() const{
    return m_ac_entries_isValid;
}

double OAIQuoteProductTransDto::getAmount() const {
    return m_amount;
}
void OAIQuoteProductTransDto::setAmount(const double &amount) {
    m_amount = amount;
    m_amount_isSet = true;
}

bool OAIQuoteProductTransDto::is_amount_Set() const{
    return m_amount_isSet;
}

bool OAIQuoteProductTransDto::is_amount_Valid() const{
    return m_amount_isValid;
}

qint64 OAIQuoteProductTransDto::getCompanyId() const {
    return m_company_id;
}
void OAIQuoteProductTransDto::setCompanyId(const qint64 &company_id) {
    m_company_id = company_id;
    m_company_id_isSet = true;
}

bool OAIQuoteProductTransDto::is_company_id_Set() const{
    return m_company_id_isSet;
}

bool OAIQuoteProductTransDto::is_company_id_Valid() const{
    return m_company_id_isValid;
}

qint64 OAIQuoteProductTransDto::getId() const {
    return m_id;
}
void OAIQuoteProductTransDto::setId(const qint64 &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIQuoteProductTransDto::is_id_Set() const{
    return m_id_isSet;
}

bool OAIQuoteProductTransDto::is_id_Valid() const{
    return m_id_isValid;
}

double OAIQuoteProductTransDto::getPercentage() const {
    return m_percentage;
}
void OAIQuoteProductTransDto::setPercentage(const double &percentage) {
    m_percentage = percentage;
    m_percentage_isSet = true;
}

bool OAIQuoteProductTransDto::is_percentage_Set() const{
    return m_percentage_isSet;
}

bool OAIQuoteProductTransDto::is_percentage_Valid() const{
    return m_percentage_isValid;
}

QString OAIQuoteProductTransDto::getProductCode() const {
    return m_product_code;
}
void OAIQuoteProductTransDto::setProductCode(const QString &product_code) {
    m_product_code = product_code;
    m_product_code_isSet = true;
}

bool OAIQuoteProductTransDto::is_product_code_Set() const{
    return m_product_code_isSet;
}

bool OAIQuoteProductTransDto::is_product_code_Valid() const{
    return m_product_code_isValid;
}

qint64 OAIQuoteProductTransDto::getProductId() const {
    return m_product_id;
}
void OAIQuoteProductTransDto::setProductId(const qint64 &product_id) {
    m_product_id = product_id;
    m_product_id_isSet = true;
}

bool OAIQuoteProductTransDto::is_product_id_Set() const{
    return m_product_id_isSet;
}

bool OAIQuoteProductTransDto::is_product_id_Valid() const{
    return m_product_id_isValid;
}

double OAIQuoteProductTransDto::getQuantity() const {
    return m_quantity;
}
void OAIQuoteProductTransDto::setQuantity(const double &quantity) {
    m_quantity = quantity;
    m_quantity_isSet = true;
}

bool OAIQuoteProductTransDto::is_quantity_Set() const{
    return m_quantity_isSet;
}

bool OAIQuoteProductTransDto::is_quantity_Valid() const{
    return m_quantity_isValid;
}

QList<QString> OAIQuoteProductTransDto::getTranNotes() const {
    return m_tran_notes;
}
void OAIQuoteProductTransDto::setTranNotes(const QList<QString> &tran_notes) {
    m_tran_notes = tran_notes;
    m_tran_notes_isSet = true;
}

bool OAIQuoteProductTransDto::is_tran_notes_Set() const{
    return m_tran_notes_isSet;
}

bool OAIQuoteProductTransDto::is_tran_notes_Valid() const{
    return m_tran_notes_isValid;
}

double OAIQuoteProductTransDto::getUnitPrice() const {
    return m_unit_price;
}
void OAIQuoteProductTransDto::setUnitPrice(const double &unit_price) {
    m_unit_price = unit_price;
    m_unit_price_isSet = true;
}

bool OAIQuoteProductTransDto::is_unit_price_Set() const{
    return m_unit_price_isSet;
}

bool OAIQuoteProductTransDto::is_unit_price_Valid() const{
    return m_unit_price_isValid;
}

double OAIQuoteProductTransDto::getVatAmount() const {
    return m_vat_amount;
}
void OAIQuoteProductTransDto::setVatAmount(const double &vat_amount) {
    m_vat_amount = vat_amount;
    m_vat_amount_isSet = true;
}

bool OAIQuoteProductTransDto::is_vat_amount_Set() const{
    return m_vat_amount_isSet;
}

bool OAIQuoteProductTransDto::is_vat_amount_Valid() const{
    return m_vat_amount_isValid;
}

qint64 OAIQuoteProductTransDto::getVatAnalysisTypeId() const {
    return m_vat_analysis_type_id;
}
void OAIQuoteProductTransDto::setVatAnalysisTypeId(const qint64 &vat_analysis_type_id) {
    m_vat_analysis_type_id = vat_analysis_type_id;
    m_vat_analysis_type_id_isSet = true;
}

bool OAIQuoteProductTransDto::is_vat_analysis_type_id_Set() const{
    return m_vat_analysis_type_id_isSet;
}

bool OAIQuoteProductTransDto::is_vat_analysis_type_id_Valid() const{
    return m_vat_analysis_type_id_isValid;
}

qint64 OAIQuoteProductTransDto::getVatRateId() const {
    return m_vat_rate_id;
}
void OAIQuoteProductTransDto::setVatRateId(const qint64 &vat_rate_id) {
    m_vat_rate_id = vat_rate_id;
    m_vat_rate_id_isSet = true;
}

bool OAIQuoteProductTransDto::is_vat_rate_id_Set() const{
    return m_vat_rate_id_isSet;
}

bool OAIQuoteProductTransDto::is_vat_rate_id_Valid() const{
    return m_vat_rate_id_isValid;
}

bool OAIQuoteProductTransDto::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_ac_entries.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_amount_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_company_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_percentage_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_product_code_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_product_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_quantity_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_tran_notes.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_unit_price_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_vat_amount_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_vat_analysis_type_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_vat_rate_id_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIQuoteProductTransDto::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
